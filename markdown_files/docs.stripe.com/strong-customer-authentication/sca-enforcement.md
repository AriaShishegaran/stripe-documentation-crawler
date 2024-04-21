htmlSCA enforcement | Stripe Documentation[Skip to content](#main-content)SCA enforcement[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstrong-customer-authentication%2Fsca-enforcement)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstrong-customer-authentication%2Fsca-enforcement)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)
[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)Regulation support[SCA readiness](/docs/strong-customer-authentication)# SCA enforcement

Learn how European regulators enforce Strong Customer Authentication (SCA).Although Europe is phasing it in unevenly, you should prepare your payment flows to be ready for SCA as soon as possible if SCA regulations impact you. Preparing for SCA helps prevent an increase in declines from European cards, and prepares you in case of early enforcement by banks. Read more about how enforcement varies by country.

## Make sure your integration is SCA-ready

Your integration is SCA-ready when you process all of your payments volume using SCA-ready products.  Your business must use an SCA-ready product, such as a recent version of Stripe Checkout, Billing, the Payment Intents API, or an SCA-ready partner solution. Additionally, you should:

- Test[3D Secure](/payments/3d-secure)(3DS) authentication thoroughly. Use our[regulatory test cards](/testing#regulatory-cards)to ensure that your integration can handle 3DS.
- Foroff-sessionpayments, make sure you set up and authenticate the card when saving the payment method, and use the API to[flag off-session payments](/payments/save-and-reuse?platform=web&ui=elements#charge-saved-payment-method).
- If your business uses the Stripe Billing[Subscriptions](/billing/subscriptions/creating)or[Invoice](/api/invoices)APIs, make sure your integration can handle[incomplete statuses](/billing/migration/strong-customer-authentication).

## Understand incomplete, declined, or failed payments

Payments can be unsuccessful for a number of reasons, including incomplete, declined, or failed payments.  If you look in the Dashboard and see that your payments aren’t advancing past the incomplete status (requires_action in the API):

- Make sure that your customer isn’t in the process of authenticating. If they’re authenticating and it’s anon-sessionpayment, they may expect to see this. It’s also possible that they’ve abandoned the checkout flow.
- Check that you’re[handling next actions](/payments/payment-intents/verifying-status#next-actions)such as authentication—next actions failures can also cause payments to fail.
- For off-session payments, set[off_session](/api/payment_intents/create#create_payment_intent-off_session)to`true`when creating the payment.

Banks can decline payments that require 3DS authentication but don’t have 3DS enabled. Go to the Dashboard to see which payments were declined for this reason. For off-session payments, filter by failed payments in the Dashboard. Hovering over the status badge highlights the decline reason (for example, authentication required). You can view on-session payments by applying the incomplete payments filter and seeing if the payment is incomplete, since it requires authentication.

You may see off-session payments failing even though you think they’re exempt from SCA requirements. For off-session payments, make sure that you’re authenticating the card when saving card details, either without a payment or during a payment. When saving cards without a payment, use the Setup Intents API and set usage to off_session. When saving cards during a payment, set setup_future_usage to off_session. Finally, be aware that exemptions aren’t guaranteed and off-session payments may still require authentication by the bank.

## Monitor disputes

When monitoring disputes, it’s important to understand the mechanics of the dispute process as it pertains to payments that have been authenticated using 3DS. Payments that 3DS successfully authenticates are covered by what’s known as a liability shift. If a cardholder disputes a 3D Secure payment as fraudulent, the liability shifts from you to the card issuer. If the card issuer applies exemptions, the payment isn’t authenticated through 3D Secure, and is therefore not covered by a liability shift.

## Collect permission to reuse cards

When you set up your payment flow to properly save a card with the Payment Intents or Setup Intents API, Stripe marks any subsequent off-session payment as a merchant-initiated transaction (MIT) to reduce the need to authenticate. Merchant-initiated transactions require an agreement (also known as a mandate) between you and your customer. Add terms to your website or application on how you plan to process payments that your customer can opt into. At a minimum, make sure that your terms cover the following:

- The customer’s permission for you to initiate a payment or a series of payments on their behalf
- The anticipated frequency of payments (that is, one-time or recurring)
- How you determine the payment amount

Add text in your checkout flow that references the terms of the payment, for example: I authorize [your business name] to send instructions to the financial institution that issued my card to take payments from my card account in accordance with the terms of my agreement with you.

## Use SCA-ready Stripe plugins

If you’re searching for an SCA-ready plugin, refer to Stripe Partners. If you want to migrate an existing Stripe plugin or developer library to support SCA, refer to the SCA migration guide for plugins and developer libraries.

## See also

- [SCA readiness](/strong-customer-authentication)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Make sure your integration is SCA-ready](#make-sure-your-integration-is-sca-ready)[Understand incomplete, declined, or failed payments](#unsuccessful-payments)[Monitor disputes](#monitor-disputes)[Collect permission to reuse cards](#collect-permission-to-reuse-cards)[Use SCA-ready Stripe plugins](#use-sca-ready-stripe-plugins)[See also](#see-also)Products Used[Payments](/payments)[Billing](/billing)[Invoicing](/invoicing)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`