htmlChoose settlement preference | Stripe Documentation[Skip to content](#main-content)Choose settlement preference[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpaypal%2Fchoose-settlement-preference)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpaypal%2Fchoose-settlement-preference)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Wallets](/docs/payments/wallets)[PayPal](/docs/payments/paypal)# Choose settlement preference

Learn about settlement modes for PayPal payments.Settlement choice determines how you access and manage funds, use the Dashboard, perform reconciliation, and so on.

## Getting started

If you’re a Connect user, your funds always settle on Stripe, similar to other payment methods. If you operate as a direct business, when you connect your PayPal and Stripe accounts you can set the funds settlement preference for your PayPal payments. Read this guide to learn more about differences between PayPal and Stripe settlement options.

If you already use PayPal through Stripe, you can check your current settlement preference on the Payment Methods Settings page in the Stripe Dashboard.

## Money flow and payouts

If you settle funds from the PayPal payments on Stripe, you can access the money from your Stripe balance according to your payouts schedule, similar to other payment methods at Stripe. The funds from the payments you receive are immediately transferred from PayPal to your Stripe balance, without the need for you to take any action.

If you settle PayPal payments to PayPal, you’ll need to manage payouts on PayPal.

## Refunds and disputes

Settlement on Stripe uses the funds available in your Stripe account if you want to refund a payment or need to cover the funds from a dispute, similarly to other payment methods on Stripe. If PayPal charges a fee when a dispute closes, it’s withdrawn from your Stripe balance through a Balance Transaction of type adjustment.

For settlement on PayPal, you can still manage refunds and disputes from your Stripe Dashboard, but the relevant funds are the funds on your PayPal account. If settle on PayPal, Stripe doesn’t transfer any funds from your PayPal account to your Stripe account or vice-versa. For that reason, make sure that you always have a positive balance in both accounts to cover expected refund amounts or disputes, and fees that PayPal might charge when the dispute closes.

## Dashboard experience

If you settle your funds from PayPal payments on Stripe, the Stripe Dashboard is the same as with other payment methods on Stripe.

If you settle your PayPal funds on a PayPal account, the balance transaction linked to the corresponding payment has a zero amount regardless of the payment, because funds settle in your PayPal balance, and no money goes to your Stripe balance.

Additionally, the Gross and Net volume charts won’t reflect your sales volume from PayPal if you settle your funds on a PayPal account. In this case, we recommend using the Payment methods report to track the volume from PayPal sales.

The payment details view is also different if you settle your PayPal funds to your PayPal account. The Net value reflects the change on the net volume of your Stripe balance. This is a negative value of the fee amount that Stripe takes for the payment.

## Reconciliation impact

Reconciliation is the process of matching and verifying payments that have been received and processed with the corresponding PayPal orders.

When settling your funds on Stripe, you get automatic transactions reconciliation.

If you settle on PayPal, you need to manually reconcile the transactions. Learn about how Stripe provides support for PayPal transaction reconciliation.

## Changing your settlement preference

If for any reason you need to change your current settlement mode, you can initiate the process from the Stripe Dashboard.

1. Go to the[Payment Methods Settings page](https://dashboard.stripe.com/settings/payment_methods).
2. Find PayPal settings.
3. ClickContact Support to change. You’ll be redirected to the FAQ page where you can file a support ticket.
4. File a support ticket to request a change.

The change shows up in the PayPal settings accordingly.

## Currency conversions

A currency conversion occurs when the presentment currency differs from the settlement currency. See currency conversions for additional detail. Prevent currency conversions by adding a settlement currency for every currency you present to your customers.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Getting started](#getting-started)[Money flow and payouts](#money-flow-and-payouts)[Refunds and disputes](#refunds-and-disputes)[Dashboard experience](#dashboard-experience)[Reconciliation impact](#reconciliation-impact)[Changing your settlement preference](#chaning-your-settlement-preference)[Currency conversions](#currency-conversions)Products Used[Payments](/payments)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`