htmlPlacing a hold on a card | Stripe Documentation[Skip to content](#main-content)Place a hold on a card[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcharges%2Fplacing-a-hold)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fcharges%2Fplacing-a-hold)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)[Older APIs](/docs/payments/older-apis)[Charges](/docs/payments/charges-api)# Placing a hold on a cardCharges API

Legacy APIThe content of this section refers to a Legacy feature. Use the PaymentIntents API instead.

The Charges API doesn’t support the following features, many of which are required for credit card compliance:

- Merchants in India
- [Bank requests for card authentication](/payments/cards/overview)
- [Strong Customer Authentication](/strong-customer-authentication)

Use the Charges API to authorize a payment now, capture funds later.

CautionAs of September 2019, a regulation called Strong Customer Authentication (SCA) requires businesses in Europe to request additional authentication for online payments. Businesses based in the European Economic Area (EEA) with customers in the EEA should follow the accept a payment guide to use the Payment Intents API to meet these rules.

Stripe supports two-step card payments so you can first authorize a charge, then wait to settle (capture) it later. When a charge is authorized, the card issuer guarantees the funds and the amount held on the customer’s card for up to 7 days, or 2 days for in-person payments using Terminal. The payment_method_details.card.capture_before attribute on the charge indicates the time when the authorization expires.

If the charge isn’t captured within this time, the authorization is canceled and funds released.

## Authorize a payment

To authorize a payment without capturing it, make a charge request that also includes the capture parameter with a value of false. This instructs Stripe to only authorize the amount on the customer’s card.

CautionOnly some payment methods support separate authorization and capture. For example, card payments, Afterpay, and Klarna support separating these steps. With payment methods that don’t support this functionality, like ACH or iDEAL, you can’t capture manually. Refer to the full list of payment methods that support manual capture.

If you need to cancel an authorization, you can release it by refunding the relevant Charge object.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "amount"=999 \
  -d "currency"="usd" \
  -d "description"="Example charge" \
  -d "source"="tok_visa" \
  -d "capture"="false"`## Capture the funds

To settle an authorized charge, make a capture charge request. The total authorized amount is captured by default, and you cannot capture more than this. To capture less than the initial amount (for example, 8 USD of a 10 USD authorization), pass the amount parameter. Partially capturing a charge automatically releases the remaining amount.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/charges/{{CHARGE_ID}}/capture \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Card statements from some issuers do not distinguish between authorizations and captured (settled) charges, which can sometimes lead to confusion for your customers. In addition, authorized charges can only be captured once. If you partially capture a charge, you cannot perform another capture for the difference. Depending on your requirements, you may be better served by saving customer’s card details for later and creating charges as needed.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Authorize a payment](#authorize-a-payment)[Capture the funds](#capture-the-funds)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`