htmlB2B Payments integration guide | Stripe Documentation[Skip to content](#main-content)B2B Payments integration guide[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbaas%2Fstart-integration%2Fintegration-guides%2Fb2b-payments)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbaas%2Fstart-integration%2Fintegration-guides%2Fb2b-payments)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)
Products[Issuing cards](#)[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Banking as a service](/docs/financial-services)[Start an integration](/docs/baas/start-integration/sample-app)[Integration guides](/docs/baas/start-integration/integration-guides)# B2B Payments integration guide

Build a B2B Payments integration with Issuing.### Unfamiliar with BaaS?

Check out our introductory guide to using BaaS for SaaS Platforms.

Build a US B2B Payments integration by using Stripe Issuing to create cards for your business, employees, or contractors to make purchases on your behalf.

By the end of this guide, you’ll know how to:

- Fund your Issuing Balance
- Create virtual cards for your own business
- Use these cards to spend funds from your Issuing Balance

## Before you begin

1. Sign up for a Stripe account.
2. [Activate Issuing test mode](https://dashboard.stripe.com/test/issuing/overview)in the Dashboard.

[Add funds](#add-funds)To spend money using cards, add funds to the Issuing balance on your account. This balance represents funds reserved for Issuing and is safely separated from your earnings, payouts, and funds from other Stripe products.

You can add funds from your Dashboard or using the create top-up endpoint.

Command Line[curl](#)`curl https://api.stripe.com/v1/topups \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d destination_balance=issuing \
  -d amount=2000 \
  -d currency=usd \
  -d description="Top-up for Issuing, April 21, 2024" \
  -d statement_descriptor=Top-up`[Create cardholders and cards](#create-cardholders-cards)### Create a cardholder

The Cardholder is the company or business entity that’s authorized to use card funding by the Issuing balance. The Cardholder object includes relevant details, such as a name to display on cards and a billing address, which is usually the business address.

The following API call creates a new Cardholder:

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cardholders \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d name="Company Card" \
  --data-urlencode email="company@example.com" \
  --data-urlencode phone_number="+18008675309" \
  -d status=active \
  -d type=company \
  -d "billing[address][line1]"="123 Main Street" \
  -d "billing[address][city]"="San Francisco" \
  -d "billing[address][state]"=CA \
  -d "billing[address][postal_code]"=94111 \
  -d "billing[address][country]"=US`Stripe returns a Cardholder object that contains the information you provided and sends the issuing_cardholder.created webhook event.

### Create a card

Create a card and attach it to the Cardholder that you want to make the authorized user of the card.

In the following examples, we show you how to create a virtual card. You can, however, create physical cards and ship them to cardholders in live mode.

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d currency=usd \
  -d type=virtual \
  -d cardholder={{CARDHOLDER_ID}}`Stripe returns a Card object on creation, and sends the issuing_card.created webhook event:

`{
  "id": "ic_1NvPjF2SSJdH5vn2OVbE7r0b",
  "object": "issuing.card",
  "brand": "Visa",
  ...
  "status": "inactive",
  "type": "virtual"
}`You need to activate the card before a user can use it. While you can activate virtual cards in the same API call you used to create it, physical cards must be activated separately. When ready, activate the card by marking the status as active:

Command Line[curl](#)`curl https://api.stripe.com/v1/issuing/cards/ic_1NvPjF2SSJdH5vn2OVbE7r0b \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d status=active`At this point, there’s now an active card attached to a cardholder. See the Issuing page to view the card and cardholder information.

`{
  "id": "ic_1NvPjF2SSJdH5vn2OVbE7r0b",
  "object": "issuing.card",
  "brand": "Visa",
  ...
  "status": "active",
  "type": "virtual",
}`To learn more, see:

- [Read more about virtual cards](/issuing/cards/virtual).
- [Read more about physical cards](/issuing/cards/physical).
- [Using the Dashboard for Issuing with Connect](/issuing/connect#using-dashboard-issuing)
- [Create cards with the API](/issuing/cards)
- [Testing physical card shipment](/issuing/cards/physical/testing)

[Use the card](#use-card)### Create an authorization

To observe the impact of card activity on the financial account, generate a test authorization. You can do this in the Issuing page of the Dashboard for the connected account, or with the following call to the Authorization API:

Command Line[curl](#)`curl https://api.stripe.com/v1/test_helpers/issuing/authorizations \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d card={{CARD_ID}} \
  -d amount=1000 \
  -d authorization_method=chip \
  -d "merchant_data[category]"=taxicabs_limousines \
  -d "merchant_data[city]"="San Francisco" \
  -d "merchant_data[country]"=US \
  -d "merchant_data[name]"="Rocket Rides" \
  -d "merchant_data[network_id]"=1234567890 \
  -d "merchant_data[postal_code]"=94107 \
  -d "merchant_data[state]"=CA`After approval, Stripe creates an Authorization in a pending state while it waits for capture. Note the authorization id that you’ll use to capture the funds:

`{
  "id": "iauth_1NvPyY2SSJdH5vn2xZQE8C7k",
  "object": "issuing.authorization",
  "amount": 1000,
  ...
  "status": "pending",
  "transactions": [],
}`### Capture the funds

Capture the funds using the following code:

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/test_helpers/issuing/authorizations/{{AUTHORIZATION_ID}}/capture \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`After the authorization is captured, Stripe creates an Issuing Transaction, the status of the authorization is set to closed.

## See also

- [Handling real-time auth webhooks](/issuing/controls/real-time-authorizations)
- [Spending controls](/issuing/controls/spending-controls)
- [Issuing authorizations](/issuing/purchases/authorizations)
- [Issuing transactions](/issuing/purchases/transactions)
- [Testing Issuing](/issuing/testing)
- [Working with Stripe Issuing cards and Treasury](/treasury/account-management/issuing-cards)
- [Manage transaction fraud](/issuing/manage-fraud)
- [Issue regulated customer notices](/issuing/compliance-us/issuing-regulated-customer-notices)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Add funds](#add-funds)[Create cardholders and cards](#create-cardholders-cards)[Use the card](#use-card)[See also](#see-also)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`