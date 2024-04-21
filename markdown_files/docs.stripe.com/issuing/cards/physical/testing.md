htmlTesting physical card shipment | Stripe Documentation[Skip to content](#main-content)Testing physical cards[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fphysical%2Ftesting)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fphysical%2Ftesting)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)# Testing physical card shipment

Learn how to test physical card fulfilment and simulate the shipping process.### Test mode funding

Refer to the Issuing testing documentation to learn more about funding your test mode Issuing balance.

A physical card starts off with its shipping status as pending by default. As it progresses through fulfillment, subsequent possible values include: shipped, delivered, returned, failure, and canceled.

Refer to the following diagram to see how the status transitions for physical card shipping:

In test mode, you can update a card’s shipping state yourself to test out the different values. You can only use cards created in test mode for testing within your Stripe account and not for external purchases. No cards are actually shipped in test mode.

Without codeWith codeYou can simulate shipping a card by updating its shipping status in the Dashboard.

[Create a cardDashboard](#without-code-create-card)Use the Dashboard to create a cardholder and physical card in test mode.

[Ship the cardDashboard](#without-code-ship-card)1. In the Dashboard, first make sure you’re viewing test data.
2. Go to the[Issuing Cards page](https://dashboard.stripe.com/issuing/cards)and find your newly-created card.
3. Scroll to theCard detailssection.
4. ClickUpdate shipping statusand select the shipping action you want to simulate (for example,`Ship`).
5. ClickSubmitto apply your update and refresh the page.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a card](#without-code-create-card)[Ship the card](#without-code-ship-card)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`