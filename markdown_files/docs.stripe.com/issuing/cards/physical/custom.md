htmlHow custom physical cards work | Stripe Documentation[Skip to content](#main-content)How custom cards work[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fphysical%2Fcustom)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fphysical%2Fcustom)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)[Physical cards](/docs/issuing/cards/physical)# How custom physical cards work

You can customize most elements of a card.You can design custom cards with Stripe that showcase your brand to your end users.

You can choose from various options, but before designing your card, it’s important to understand how they’re created and what key elements make up a card. This helps inform the choices available and requirements that need to be followed. Reach out to your account representative to learn more about custom card pricing.

[How to create custom physical cards](#how-cards-are-created)The following table describes the different stages needed to get a card from the design file to live and in your hands. This is what you should expect at every step of the process:

StepTimelineWhat to expect1: Design2 weeksUpload artwork on the card design template and choose desired features. Stripe reviews and provides feedback as needed.2: Proofing1 weekThe card printer generates a proof with the card artwork, colors, quantity, and material details that are provided for your approval prior to finalizing the order. Simultaneously, the printer submits the card artwork to Visa or MasterCard to make sure it meets compliance requirements.3: Manufacturing12+ weeksCards are manufactured using specialized machinery at the card printer. The artwork is printed on plastic, collated with all required card layers, laminated with desired finish, and cut into cards. Due to material supply challenges, card lead times are currently a few months longer compared to the standard timeline.4: Testing2 weeksAfter cards are manufactured, they’re shipped to the personalization site to conduct testing to ensure that the cards are functional and set up correctly.5: Go live2 business days after testing completesCards are made live in your Stripe account. At this point, they’re ready to start issuing.### Use your custom bundle to create a personalization design

After your custom bundle is ready for use, Stripe creates a physical bundle object on your behalf. You can also list all of your physical bundles.

A personalization design is how you control the appearance of your physical cards in the API. It consists of a physical bundle, and a logo and carrier text if your bundle supports it.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/personalization_designs \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d physical_bundle=ics_Kc3MX9PPsUFFMp`We also provide a number of features to help manage personalization designs, including:

- Setting default designs to use when you issue a card
- Using lookup keys to use many designs without having to change code
- Using Connect to manage personalization designs across many accounts

See managing personalization designs to learn more.

### Create a card

After you have a personalization design, you can start creating physical cards with that design. Include the ID of the personalization_design you want to use when creating the card. If the design has already been approved, cards you create with it are fulfilled right away. If the design is in review, the cards are fulfilled when the design is approved.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d cardholder={{CARDHOLDER_ID}} \
  -d currency=usd \
  -d type=physical \
  -d personalization_design=ipcd_OhggKRta0zu2Te`If you have any design set as default, any card you create without specifying a design uses that default. See default personalization designs to learn more.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`