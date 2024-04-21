htmlCreate cards with the API | Stripe Documentation[Skip to content](#main-content)Create cards[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)# Create cards with the API

Learn how to create cardholders and issue cards.You can create virtual and physical cards on Mastercard or Visa (or both) with the Cards API. Cardholders can use virtual cards instantly after you create them. Stripe sends you physical cards in the mail.

You can also create virtual and physical cards with the Dashboard.

[Create a cardholder](#create-cardholder)The Cardholder object represents an individual or business entity that you can issue cards to. Create a Cardholder with a name to display on cards and the billing address, which is often requested when the cardholder makes online purchases, and is usually the business address of the connected account or your platform.

When you create a cardholder, or update it later, you can include additional information such as a phone_number or email, which are required for some features like digital wallets. You can also specify preferred_locales to customize the cardholder’s language for features like 3D Secure.

NoteEuropean law requires you to apply Strong Customer Authentication (SCA) to transactions, unless exempt. In such cases, the cardholder phone_number is required.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cardholders \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "name"="Damian Michelfelder" \
  -d "email"="damian.michelfelder@example.de" \
  -d "phone_number"="+49 30 12345-67" \
  -d "status"="active" \
  -d "type"="individual" \
  -d "individual[first_name]"="Damian" \
  -d "individual[last_name]"="Michelfelder" \
  -d "individual[dob][day]"=1 \
  -d "individual[dob][month]"=11 \
  -d "individual[dob][year]"=1981 \
  -d "billing[address][line1]"="20 Waldweg" \
  -d "billing[address][city]"="Berlin" \
  -d "billing[address][postal_code]"="45276" \
  -d "billing[address][country]"="DE"`Stripe returns a Cardholder object that contains the information you provided and sends the issuing_cardholder.created webhook event.

### Individual type cardholder requirements

The cardholder type defaults to individual, but you can set the type to company if you choose.

You must provide values for the first and last names of individual cardholders, which Stripe screens in accordance with regulatory guidelines. Consider also providing date of birth, which might help reduce watchlist reviews.

### Accept authorized user terms

If you’re issuing cards to individuals for programs backed by Celtic Bank (not required for company type cardholders), you must record acceptance of the Celtic Bank Authorized User Terms before activating a card for that cardholder. See the Required Agreements for Issuing and Treasury for more information about which agreements you’re required to present to accountholders and cardholders.

If applicable, Stripe alerts you to this requirement in the requirements property of the Cardholder object:

`{
  "id": "ich_1MGlTC2eZvKYlo2CJnowP9Z5",
  "name": "Damian Michelfelder",
  ...
  "requirements": {
    "disabled_reason": "requirements.past_due",
    "past_due": [
      "individual.card_issuing.user_terms_acceptance.date",
      "individual.card_issuing.user_terms_acceptance.ip",
    ],
  },
  ...
}`You can accept the terms on behalf of the Cardholder by passing in the Unix timestamp of when the cardholder accepted their terms and also their IP address.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cardholders/ich_1MGlTC2eZvKYlo2CJnowP9Z5 \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "individual[card_issuing][user_terms_acceptance][date]"=1470266163 \
  -d "individual[card_issuing][user_terms_acceptance][ip]"="91.121.146.224"`When you’ve met the requirements for card activation (such as first and last names, plus proof of user terms acceptance) you can activate cards for them.

[Create a card](#create-card)Create a Card and assign it to the cardholder. This request contains the ID of the Cardholder object, currency, and type (either virtual or physical) of the card.

Creating a physical card requires a shipping address, and you can provide additional arguments to specify shipment packaging and delivery service.

Issuing-onlyIssuing with TreasuryCommand Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d cardholder=ich_1MGlTC2eZvKYlo2CJnowP9Z5 \
  -d currency=usd \
  -d type=virtual`Stripe returns a Card object upon creation, and sends the issuing_card.created webhook event.

[Activate the card](#activate-card)In order for authorizations to be approved on a card, its status must be set to active. Note that past-due requirements block card activation.

### Activate on creation

The card can be activated when creating it using the Dashboard or the API. In the Dashboard, when creating a card, click Activate card. Using the API, set status to active when using the create card endpoint.

### Activate after creation

Alternatively, after creating an inactive card, the card can be activated using the Dashboard or the API. To activate using the Dashboard, select the card you wish to activate, then click Activate card. To activate using the API, use the update card endpoint to set its status to active.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards/ic_1Cm3paIyNTgGDVfzBqq1uqxR \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d status=active`### Re-activate after blocking

In some cases, multiple incorrect PIN attempts on a transaction deactivates a card, preventing further authorizations. To reactivate the card, use the Dashboard or the update card API to set the card’s status to active.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a cardholder](#create-cardholder)[Create a card](#create-card)[Activate the card](#activate-card)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`