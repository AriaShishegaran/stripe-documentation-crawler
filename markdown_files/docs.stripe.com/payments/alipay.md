htmlAlipay payments | Stripe Documentation[Skip to content](#main-content)Alipay[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Falipay)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Falipay)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)# Alipay payments

Learn about Alipay, a digital wallet popular with customers from China.Alipay is a digital wallet in China that has more than a billion active users worldwide. Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer’s login credentials.

Payment method propertiesCountry availability- Customer locations

Chinese consumers, overseas Chinese, and Chinese travelers


- Presentment currency

CNY, AUD, CAD, EUR, GBP, HKD, JPY, SGD, MYR, NZD, USD (depending on business locations)


- Payment confirmation

Customer-initiated


- Payment method family

Wallets


- Recurring payments

Requires approval


- Payout timing

Standard payout timing applies


- Connect support

Partial (request an invite to create charges on behalf of other accounts)


- Dispute support

No


- Refunds / Partial refunds

Yes / yes



## Prohibited business categories

For more information about Alipay eligibility for your account, navigate to your Payment methods settings.

Both Stripe and Alipay maintain a list of prohibited businesses that aren’t allowed to use their services. To use Alipay on Stripe, your business can’t be restricted from using Stripe or appear on Alipay’s prohibited business list. If you’re not sure if your business is a prohibited business, or have questions about how these requirements apply to you, please contact support.

## Get started

You don’t actually have to integrate Alipay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- [Checkout](/checkout/quickstart): Our prebuilt, hosted checkout page.
- [Elements](/payments/quickstart): Our drop-in UI components.

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

Payment Links also supports adding Alipay from the Dashboard.

If you prefer to manually list payment methods, learn how to manually configure Alipay as a payment.

## Disputed payments

Alipay payments have a low risk of fraud or unrecognized payments because the customer must authenticate the payment, so no dispute process exists that could create chargebacks and withdraw funds from your Stripe account. If an Alipay user contacts them about a problem with a transaction, they might direct that user to you for a resolution.

## Refunds

You can refund Alipay payments up to 90 days after the original payment. Refunds for Alipay payments are asynchronous and take up to 5 minutes to complete. Stripe notifies you of the final refund status using the charge.refund.updated webhook event. When a refund succeeds, the status of the Refund object transitions to succeeded. If a refund fails, the status of the Refund object transitions to failed and Stripe returns the amount to your Stripe balance. At this point, you need to arrange an alternative way of providing your customer with a refund.

## Supported currencies

You can create Alipay payments in the currencies that map to your country. The default local currency for Alipay is cny and customers also see their purchase amount in cny.

CurrencyCountry`cny`Any country`aud`Australia`cad`Canada`eur`Austria, Belgium, Bulgaria, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Norway, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden, Switzerland`gbp`United Kingdom`hkd`Hong Kong`jpy`Japan`myr`Malaysia`nzd`New Zealand`sgd`Singapore`usd`United StatesIf you have a bank account in another currency and would like to create an Alipay payment in that currency, you can contact support. Support for additional currencies is provided on a case-by-case basis.

## See also

Accepting Alipay payments

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Prohibited business categories](#prohibited-business-categories)[Get started](#get-started)[Disputed payments](#disputed-payments)[Refunds](#refunds)[Supported currencies](#supported-currencies)[See also](#see-also)Products Used[Payments](/payments)[Payment Links](/payments/payment-links)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`