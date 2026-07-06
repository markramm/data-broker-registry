#!/usr/bin/env python3
"""
Shared logic for authoring/validating/compiling data/brokers/*.md against broker.schema.json.
Used by validate_broker.py (single-file, pre-commit), build_brokers.py (full compile), and
check_links.py (URL collection). No third-party dependencies -- hand-rolled frontmatter parsing
and schema checks, matching this project's existing zero-dependency scripts.

MIT, (C) 2026 Transparency Cascade Press.
"""
import json, os, re

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_PATH = os.path.join(HERE, "broker.schema.json")
BROKERS_DIR = os.path.join(HERE, "data", "brokers")
DROP_PATH = os.path.join(HERE, "data", "brokers-drop.json")

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n?(.*)$", re.DOTALL)

PII_URL_PATTERNS = (
    r"[?&]email=", r"[?&]ssn=", r"[?&]name=", r"[?&]dob=", r"[?&]address=",
)


class BrokerFileError(Exception):
    """A single broker markdown file failed to parse or validate."""
    def __init__(self, path, errors):
        self.path = path
        self.errors = errors
        super().__init__(f"{path}: {'; '.join(errors)}")


def load_schema():
    return json.load(open(SCHEMA_PATH))


def load_drop_list():
    if not os.path.exists(DROP_PATH):
        return set()
    return set(d.lower() for d in json.load(open(DROP_PATH)))


def _parse_scalar(raw):
    raw = raw.strip()
    if raw == "null" or raw == "":
        return None
    if raw == "true":
        return True
    if raw == "false":
        return False
    if raw.startswith('"') and raw.endswith('"'):
        return raw[1:-1]
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(item.strip()) for item in inner.split(",")]
    if re.match(r"^-?\d+$", raw):
        return int(raw)
    return raw


def parse_frontmatter(text, path="<string>"):
    """Split a broker markdown file into (frontmatter_dict, body_markdown).

    Hand-rolled, single-document, flat-key YAML subset -- sufficient for this schema's
    scalar/enum/array-of-scalar fields. Does not support nested mappings.
    """
    m = _FRONTMATTER_RE.match(text)
    if not m:
        raise BrokerFileError(path, ["no --- frontmatter block found"])
    fm_text, body = m.group(1), m.group(2)
    data = {}
    for line in fm_text.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            raise BrokerFileError(path, [f"malformed frontmatter line: {line!r}"])
        key, _, raw_value = line.partition(":")
        data[key.strip()] = _parse_scalar(raw_value)
    return data, body.strip()


def render_frontmatter(data):
    """Inverse of parse_frontmatter's scalar parsing, for the migration script."""
    lines = ["---"]
    for key, value in data.items():
        lines.append(f"{key}: {_render_scalar(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def _render_scalar(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list):
        return "[" + ", ".join(_render_scalar(v) for v in value) + "]"
    if isinstance(value, str):
        # Bare digit strings, and the true/false/null keywords, must be quoted -- otherwise
        # parse_frontmatter's scalar parser reads them back as int/bool/None instead of str
        # (this is how phone numbers like "2069735100" round-tripped as int before this fix).
        looks_like_other_type = (
            re.match(r"^-?\d+$", value) or value in ("true", "false", "null")
        )
        if re.match(r"^[a-zA-Z0-9_.\-]+$", value) and not looks_like_other_type:
            return value
        return json.dumps(value)
    return json.dumps(value)


def validate_entry(entry, schema):
    """Validate one parsed frontmatter dict against broker.schema.json's shape.

    Returns a list of human-readable error strings (empty = valid). Covers the subset of
    JSON Schema this project's fields actually need (required/type/enum/pattern/oneOf for
    the specific shapes used here) -- not a general-purpose validator.
    """
    errors = []
    props = schema["properties"]

    for field in schema["required"]:
        if field not in entry:
            errors.append(f"missing required field: {field}")

    for field, value in entry.items():
        if field not in props:
            errors.append(f"unknown field: {field}")
            continue
        spec = props[field]
        err = _validate_field(field, value, spec)
        if err:
            errors.append(err)

    errors.extend(_cross_field_checks(entry))
    return errors


def _validate_field(field, value, spec):
    if "enum" in spec:
        if value not in spec["enum"]:
            return f"{field}: {value!r} not in {spec['enum']}"
        return None
    if "oneOf" in spec:
        for sub in spec["oneOf"]:
            if _matches(value, sub):
                return None
        return f"{field}: {value!r} matches none of the allowed shapes"
    if "pattern" in spec and value is not None:
        if not re.match(spec["pattern"], str(value)):
            return f"{field}: {value!r} does not match pattern {spec['pattern']}"
    if spec.get("type") == "array":
        if not isinstance(value, list):
            return f"{field}: expected array, got {type(value).__name__}"
        item_enum = spec.get("items", {}).get("enum")
        if item_enum:
            bad = [v for v in value if v not in item_enum]
            if bad:
                return f"{field}: invalid item(s) {bad} not in {item_enum}"
    return None


def _matches(value, spec):
    t = spec.get("type")
    if t == "null":
        return value is None
    if t == "string":
        if not isinstance(value, str):
            return False
        if "pattern" in spec:
            return bool(re.match(spec["pattern"], value))
        if spec.get("format") == "uri":
            return value.startswith("http://") or value.startswith("https://")
        if spec.get("format") == "email":
            return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", value))
        return True
    return False


def _cross_field_checks(entry):
    errors = []
    placeholder = re.compile(r"^<verify:.*>$")

    url = entry.get("opt_out_url")
    email = entry.get("opt_out_email")
    last_verified = entry.get("last_verified")

    url_is_placeholder = isinstance(url, str) and placeholder.match(url)
    email_is_placeholder = isinstance(email, str) and placeholder.match(email)

    if (url_is_placeholder or email_is_placeholder) and last_verified is not None:
        errors.append(
            "last_verified must be null when opt_out_url or opt_out_email is a <verify:...> placeholder"
        )

    if entry.get("tier") == "auto":
        if not email or email_is_placeholder:
            errors.append("tier 'auto' requires a real (non-null, non-placeholder) opt_out_email")

    if isinstance(url, str) and not url_is_placeholder:
        for pat in PII_URL_PATTERNS:
            if re.search(pat, url, re.IGNORECASE):
                errors.append(f"opt_out_url appears to contain PII in a query param (matched {pat}): {url}")

    fm_id = entry.get("id")
    if fm_id is not None and not re.match(r"^[a-z0-9-]+$", fm_id):
        errors.append(f"id {fm_id!r} does not match ^[a-z0-9-]+$")

    return errors


def iter_broker_files(directory=BROKERS_DIR):
    if not os.path.isdir(directory):
        return
    for fname in sorted(os.listdir(directory)):
        if fname.endswith(".md"):
            yield os.path.join(directory, fname)


def load_and_validate_all(directory=BROKERS_DIR):
    """Parse + validate every broker file. Returns (entries, errors_by_path).

    Collects every file's errors before returning, rather than stopping at the first
    failure, so one run reports every broken file at once.
    """
    schema = load_schema()
    entries = []
    errors_by_path = {}
    seen_ids = {}
    seen_domains = {}

    for path in iter_broker_files(directory):
        fname_id = os.path.splitext(os.path.basename(path))[0]
        try:
            text = open(path, encoding="utf-8").read()
            entry, body = parse_frontmatter(text, path)
        except BrokerFileError as e:
            errors_by_path[path] = e.errors
            continue

        errs = validate_entry(entry, schema)
        if entry.get("id") and entry["id"] != fname_id:
            errs.append(f"frontmatter id {entry['id']!r} does not match filename-derived id {fname_id!r}")

        entry_id = entry.get("id", fname_id)
        if entry_id in seen_ids:
            errs.append(f"duplicate id {entry_id!r} (also in {seen_ids[entry_id]})")
        else:
            seen_ids[entry_id] = path

        domain = entry.get("domain")
        if domain:
            if domain in seen_domains:
                errs.append(f"duplicate domain {domain!r} (also in {seen_domains[domain]})")
            else:
                seen_domains[domain] = path

        if errs:
            errors_by_path[path] = errs
        else:
            entry["instructions_md"] = body
            entries.append(entry)

    return entries, errors_by_path
