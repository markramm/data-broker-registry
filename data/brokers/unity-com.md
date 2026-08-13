---
id: unity-com
name: Unity Technologies (Unity Ads)
domain: unity.com
category: adtech
people_search: false
tier: guided
priority: high
method: portal
opt_out_url: "https://unity.com/legal/do-not-sell-my-personal-information"
opt_out_email: "dpo@unity3d.com"
phone: null
captcha: false
id_required: false
phone_required: false
charges_fee: false
required_fields: [email]
readd_days: null
legal_basis: [ccpa]
last_verified: null
source: "dbw+tcp-research"
notes: "Fetched unity.com/legal/privacy-policy and unity.com/legal/do-not-sell-my-personal-information directly (HTTP 200 via curl with a browser user-agent; Claude's built-in WebFetch got 403 on both). Unity Technologies is the well-known game-engine company; the data-broker-relevant part is specifically Unity Ads / its advertising SDK. The CCPA opt-out page explicitly discloses that Unity 'shares' (and under CCPA's broad definition may 'sell') personal information via the Ad ID sent when a game using Unity's Ad Network is played, which Unity's advertising/publishing partners may use to look up your online activity. Opt-out mechanics differ by user type: (1) game players opt out via an in-game 'privacy settings' banner/icon shown inside personalized Unity ads -- there is no separate web form outside the game itself; (2) developers opt out via their Unity account privacy settings; (3) website visitors use the 'Your Privacy Choices (Cookie Settings)' footer link on unity.com. For all cases the page also offers a fallback: email dpo@unity3d.com. Because the primary channel is in-app/in-ad UI rather than a fetchable web form, and there's no way to id_required/phone_required check it directly, classified tier:guided and method:portal (the do-not-sell page functions as an explanatory portal directing to different in-product controls) with the DPO email as the concrete fallback. legal_basis is ccpa only since that's what the page cites; last_verified left null since only the static page text was confirmed, not the actual in-game/in-ad opt-out flow."
---

1. If you are opting out as a game player: while playing a game that shows Unity-powered ads, look for the small privacy icon in the bottom-left corner of a personalized ad, or a privacy settings banner. Tap it and follow the steps to opt out of personalized ads and data sharing for that game.
2. If you are a Unity developer: log in to your Unity account, open your account's privacy settings page, and adjust or opt out of the data uses listed there.
3. If you are only a visitor to unity.com: open the "Your Privacy Choices (Cookie Settings)" link in the site footer and select your opt-out preferences in the pop-up.
4. In any case, for a broader request (deletion, correction, or a disclosure of what Unity holds on you) that the in-product controls don't cover, email dpo@unity3d.com directly and describe your request.
5. Because Unity Ads opt-outs are largely per-app/per-device (tied to your device's advertising ID), you may need to repeat step 1 separately in each game/app that uses Unity's ad network.
