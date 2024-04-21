# OAuth changes for platform-controlled Standard accounts

[account types](https://stripe.com/docs/connect/accounts)

[platform controls](https://stripe.com/docs/connect/platform-controls-for-standard-accounts)

We’ve updated OAuth to isolate platforms’ processing activity on platform-controlled Standard accounts. Platforms using OAuth with read_write scope can’t connect to Standard accounts that are controlled by another platform. Prior to June 2021, multiple platforms could connect to the same Standard account.

This change ensures that in the rare case that a Connect user with access to the Stripe Dashboard interacts with two platforms, each platform’s activity is kept distinct in separate Standard accounts.

[Connect](/connect)

When a user of a Standard account controlled by another platform connects to your platform, the Connect onboarding flow directs them to create a separate Standard account to use with your platform. The new account automatically connects to your platform.

If you registered your Connect application as an Extension integration, it can still connect to accounts that are connected to another platform. Extensions need to connect to existing Standard accounts that might also be connected to another Platform or Extension. Only Extensions can use read_only, which ensures that platforms can’t read other applications’ data.

[Extension integration](/building-extensions)

However, if you had previously selected ‘Platform’ for your Connect application, and find that you need Extension functionality, then you will need to contact us to modify your integration selection. Your selection can be found at the Connect Settings page in the ‘Availability’ section.

[contact us](https://support.stripe.com/contact/email?topic=connect)

[Connect Settings page](https://dashboard.stripe.com/settings/connect)
