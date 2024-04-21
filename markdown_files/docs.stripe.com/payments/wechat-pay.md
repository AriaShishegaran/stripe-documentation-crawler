htmlWeChat Pay payments | Stripe Documentation[Skip to content](#main-content)WeChat Pay[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fwechat-pay)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fwechat-pay)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)# WeChat Pay payments

Learn about WeChat Pay, a digital wallet popular with customers from China.As China’s largest internet company, Tencent offers a number of web and mobile products across social networking, communications, media, games, finance, and so on. WeChat, owned by Tencent, is China’s leading mobile app with over 1 billion monthly active users.

WeChat is a leading lifestyle ‘super app’ used for messaging between people, as well as connecting people, services and businesses in China and around the world through a number of e-commerce and social features inside the app. WeChat Pay, the payment wallet inside the WeChat app, has over 800 million users.

Chinese consumers can use WeChat Pay to pay for goods and services inside of businesses’ apps and websites. WeChat Pay users buy most frequently in gaming, e-commerce, travel, online education and food/nutrition.

Payment method propertiesCountry availability- Customer locations

Chinese consumers, overseas Chinese, and Chinese travelers


- Presentment currency

CNY, AUD, CAD, EUR, GBP, HKD, JPY, SGD, USD, DKK, NOK, SEK, CHF (depending on business location)


- Payment confirmation

Customer-initiated


- Payment method family

Digital wallet


- Recurring payments

No


- Payout timing

Standard payout timing applies


- Connect support

Partial (request an invite to create charges on behalf of other accounts)


- Dispute support

No


- Refunds / Partial refunds

Yes / yes



## Get started

You don’t actually have to integrate WeChat Pay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

### Other payment products

The following Stripe products also support adding WeChat Pay from the Dashboard:

- [Invoicing](/invoicing/quickstart-guide)
- [Payment Links](/payment-links)
- [Subscriptions](/billing/subscriptions/overview)

If your integration requires manually listing payment methods, learn how to manually configure WeChat Pay as a payment.

## Disputed payments

WeChat payments have a low risk of fraud or unrecognized payments because the customer must authenticate the payment via the WeChat Pay app. Therefore, there is no dispute process that can result in a chargeback and funds being withdrawn from your Stripe account.

## Refunds

Payments made with WeChat Pay can only be submitted for refund within 180 days from the date of the original charge. After 180 days, it is no longer possible to refund the charge. Refunds for WeChat Pay payments are asynchronous. Stripe notifies you of the final refund status using the charge.refund.updated webhook event. When a refund succeeds, the Refund object’s status transitions to succeeded. In the rare instance that a refund fails, the Refund object’s status transitions to failed and Stripe returns the amount to your Stripe balance. You will then need to arrange an alternative way of providing your customer with a refund.

## Supported currencies

You can create WeChat Pay payments in the currencies that map to your country. The default local currency for WeChat Pay is cny and customers also see their purchase amount in cny.

CurrencyCountry`cny`All countries`aud`Australia`cad`Canada`eur`Austria, Belgium, Denmark, Finland, France, Germany, Ireland, Italy, Luxembourg, Netherlands, Norway, Portugal, Spain, Sweden, Switzerland`gbp`United Kingdom`hkd`Hong Kong`jpy`Japan`sgd`Singapore`usd`United States`dkk`Denmark`nok`Norway`sek`Sweden`chf`SwitzerlandWas this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get started](#get-started)[Disputed payments](#disputed-payments)[Refunds](#refunds)[Supported currencies](#supported-currencies)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`