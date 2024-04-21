htmlAdd funds to your card program | Stripe Documentation[Skip to content](#main-content)Add funds to your card program[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fadding-funds-to-your-card-program)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fadding-funds-to-your-card-program)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)# Add funds to your card program

Learn about your options to fund card spend.In order to power card spend, Stripe Issuing users must fund an Issuing Balance. Your default funding option is using an external bank account. Depending on your integration and region, you have the option to pull funds or to push funds from an external bank account to your Issuing balance. If you use Stripe Payments, you can fund your Issuing balance from your Stripe acquiring balance and/or from your external bank account. This page provides information to help you decide which mechanism works better for your integration.

## Funding your card program

Determining how to fund your card program is a core part of your Stripe Issuing integration. In order to avoid insufficient funds declines when making purchases on issued cards, your account needs to have sufficient funds in the Issuing Balance. As a best practice you should:

1. Add funds to cover planned spending.
2. Create alerts that tell you when your Issuing balance is low.
3. Review funding options to efficiently move money into your Issuing balance.

For businesses on Stripe Issuing, the default way to fund your card spend is a top-up from an external bank account. Specifically, in the US, the default is a pull-funded top-up, and in the UK and Euro zone the default is a push-funded top-up.

### Funding option

Pull-funded top-ups

Default method in the US. Sufficient as sole funding method.

Push-funded top-ups

Default method in the UK and Euro area; optional in the US. Sufficient as sole funding method.

Stripe balance transfers

Requires Stripe Payments. Optional in the US, UK and Euro area.

Connect balance transfers

Requires Stripe Connect. Optional in the US, UK and Euro area.

### How it works

Pull-funded top-ups fund your Issuing balance from an external bank account.

Users with a direct or Connect integration can initiate pull-funded top-ups via the create top-up endpoint or in the Dashboard. A platform’s connected accounts can initiate pull-funded top-ups via the API only.

Push-funded top-ups also fund your Issuing balance from an external bank account. However, unlike pull-funded top-ups, you don’t need to add your external bank account to Stripe.

Instead, push-funded top-ups use an account or routing number to push funds to your Issuing balance via: Same-day wire or ACH credit transfer (US) BACS / FPS (UK) Sepa Credit Transfer (Euro area)

Routing information can be found via the Dashboard or by making a create or list call to the Funding Instruction endpoint. However, connected accounts can only view routing information by calling List Funding Instructions.

Balance transfers move funds to your Issuing balance from your Stripe balance, which contains your payments proceeds.

Users with a direct or Connect integration can initiate Stripe balance transfers via the balance transfer API endpoint or in the Dashboard. A platform’s connected accounts can only initiate Stripe balance transfers to Issuing balance via the API.

If you need to pay out excess funds in the Issuing balance, you can initiate a Payout.

Transfers funds to or from the Issuing balance of a connected account from the platform’s Issuing balance.

### Fund origination

External bank accountExternal bank accountStripe balance (Payments)Platform Issuing balance (Connect)### Settlement time

Funds can take up to 5 business days to become available. Expedited top-ups may be available.Funding speed depends on the rails that the funds are pushed over. There may be additional delays for your first few top-ups.Funds settle instantly in the US and within one business day in the UK and Euro area.Funds settle instantly in all available regions.### Availability

Available in the US on Direct and Connect integrations.

See documentation for pull-funded top-ups for Connect and Direct integrations.

Not currently available in the UK or Euro area.

Available in the US in the APIbeta and Dashboard. See documentation for push-funded top-ups for Connect or Direct integrations.

Available in the UK and Euro area. See the documentation for push-funded top-ups for Connect (UK, Euro area) and Direct integrations.

Available in the USbeta, UKbeta, and Euro areabeta. See documentation for Connect and Direct integrations.

Available in the USbeta, UKbeta, and Euro areabeta. See documentation for Connect integrations.

### Best for

Pull-funded top-ups are best for users who want to build their own logic around when they want to top up. For example, you can build a flow to use the Balances API to view your current balances and automatically trigger a pull-funded top-up if your Issuing balance goes below a certain threshold.

For US users, this is the easiest funding method to start with, especially when using the Dashboard.

Push-funded top-ups are best for users focused on capital efficiency, since this funding method allows platforms to fund their Issuing balance on the same day. Platforms can then hold more funds in an interest-bearing account outside of Stripe and quickly move those funds into their Issuing balance as needed.

Push-funded top-ups are also good for users who have originating banks with APIs that support automated integrations. Some users also prefer not to connect an external bank account to their Issuing balance.

Balance transfers are best for users that also use Stripe to process their payments since it allows the user to use their acquiring balance to fund their Issuing balance.

Platform Issuing balance transfers are best for users that have a Connect integration and plan to programmatically fund connected accounts, since this funding mechanism allows the platform to instantly pre-fund any connected account’s Issuing balance to the right level to avoid transaction declines.

## Using funding methods in practice

Businesses on Stripe Issuing can operate a card program with the default funding method and nothing more. But if your business is integrated with additional Stripe products such as Connect or Payments, you can benefit by using multiple methods.

For example, suppose you are an e-commerce platform providing an expense management card to each of the online shops on your platform. In this case, build a Connect integration where each shop on your platform represents a connected account. Shops on your platform can accept payments and fund cards by transferring balances, all on Stripe. If your merchants also collect funds from users outside of Stripe, they can use push-funded top-ups from an external bank account. When you’re ready, allocate collected funds by transferring funds from your platform Issuing balance to the Issuing balance of specific connected accounts.

Taking a US platform as an example, your funding setup could look like this:

You could also enable your shops, represented as connected accounts, to directly accept payments and move funds into their account to pay for their expenses.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Funding your card program](#funding-your-card-program)[Using funding methods in practice](#using-funding-methods-in-practice)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`