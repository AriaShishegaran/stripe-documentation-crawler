htmlAccept a Klarna payment | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fklarna%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fklarna%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Buy now, pay later](/docs/payments/buy-now-pay-later)[Klarna](/docs/payments/klarna)# Accept a Klarna payment

Learn how to accept Klarna, a global buy now, pay later payment method.BetaTo create recurring or off-session payments with Klarna, sign up for the beta.

WebMobilePrebuilt checkout pageDirect APICautionStripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

Klarna is a single use, immediate notification payment method that requires customers to authenticate their payment. Customers are redirected to a Klarna page, where they select among multiple payment options (immediate full payment, payment in installments, or deferred payment). When the customer accepts the terms, Klarna guarantees that the funds are available to the customer and transfers the funds to your Stripe account. The customer repays Klarna according to their selected payment option.

NoteBefore you start the integration, make sure your account is eligible for Klarna by navigating to your Payment methods settings.

[Determine compatibility](#compatibility)Supported business locations: AT, BE, DE, DK, ES, FI, GB, IE, IT, NL, NO, SE, US, FR, CZ, EE, GR, LV, LT, SK, SI, AU, NZ, CA, PL, PT, CH

Supported currencies: eur, dkk, gbp, nok, sek, usd, czk, aud, nzd, cad, pln, chf

Presentment currencies: eur, dkk, gbp, nok, sek, usd, czk, aud, nzd, cad, pln, chf

Payment mode: Yes

Setup mode: No

Subscription mode: No

A Checkout Session must satisfy all of the following conditions to support Klarna payments:

- [Prices](/api/prices)for all line items must be in the same currency. If you have line items in different currencies, create separate Checkout Sessions for each currency.
- You can only use one-time line items (recurring[subscription](/billing/subscriptions/creating)plans are not supported).

[Accept a payment](#accept-a-payment)NoteBuild an integration to accept a payment with Checkout before using this guide.

Use this guide to learn how to enable Klarna—it shows the differences between accepting a card payment and using Klarna.

### Enable Klarna as a payment method

When creating a new Checkout Session, you need to:

1. Add`klarna`to the list of`payment_method_types`
2. Make sure all your`line_items`use the same currency.

[Ruby](#)`Stripe::Checkout::Session.create({
  mode: 'payment',
  payment_method_types: ['card'],
  payment_method_types: ['card', 'klarna'],
  line_items: [{
    price_data: {
      currency: 'usd',
      # To accept `klarna`, all line items must have currency: eur, dkk, gbp, nok, sek, usd, czk, aud, nzd, cad, pln, chf
      currency: 'eur',
      product_data: {
        name: 'T-shirt',
      },
      unit_amount: 2000,
    },
    quantity: 1,
  }],
  success_url: 'https://example.com/success',
  cancel_url: 'https://example.com/cancel',
})`### Fulfill your orders

After accepting a payment, learn how to fulfill orders.

[Test your integration](#test-integration)When testing your Checkout integration, select Klarna as the payment method and click the Pay button. In test mode, you can then simulate different outcomes within Klarna’s redirect.

Below, we have specially selected test data for the currently supported customer countries. In test mode, Klarna approves or denies a transaction based on the supplied email address.

AustraliaAustriaBelgiumCanadaCzechiaDenmarkFinlandFranceGermanyGreeceIrelandItalyNetherlandsNew ZealandNorwayPolandPortugalSpainSwedenSwitzerlandUnited KingdomUnited StatesApprovedDeniedDriving License Number1111111111111111Date of Birth10-07-197010-07-1970First NameTestTestLast NamePerson-auPerson-auStreetWharf streetWharf streetHouse number44Postal Code48774877CityPort DouglasPort DouglasRegionQLDQLDPhone+61473752244+61473763254Emailcustomer@email.aucustomer+denied@email.auFor production testing, you can use an amount of 3500 in your local currency to test all Klarna payment options besides Financing. For example, if you want to test “Pay in 3” in Italy, you can use a transaction of 35.00 EUR.

### Two-step authentication

Any six digit number is a valid two-step authentication code. Use 999999 for authentication to fail.

### Repayment method

Inside the Klarna flow, you can use the following test values to try various repayment types:

TypeValueDirect DebitDE11520513735120710131Bank transferDemo BankCredit Card- Number: 4111 1111 1111 1111
- CVV: 123
- Expiration: any valid date in the future

[Handle refunds and disputes](#refunds-and-disputes)Learn more about Klarna disputes and refunds.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Determine compatibility](#compatibility)[Accept a payment](#accept-a-payment)[Test your integration](#test-integration)[Handle refunds and disputes](#refunds-and-disputes)Products Used[Payments](/payments)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`