htmlHow cards work | Stripe Documentation[Skip to content](#main-content)How cards work[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcards%2Foverview)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcards%2Foverview)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)
[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[About Stripe payments](/docs/payments/online-payments)# How cards work

See how a credit or debit card payment works online, step by step.### Card fees

For information on payment method transaction fees, see local payment method pricing.

Cards are one of the most popular ways to pay online, with broad global reach. There are different types of cards and several steps in the process. To build a Stripe integration that supports all of your customers, see what goes on behind the scenes of a card payment.

![](https://b.stripecdn.com/docs-statics-srv/assets/1ab45e9a3dd360cdbbe998626aaa5ca1.svg)

Checking card detailsStripe checks that the details provided are formatted correctly (for example, the expiry date isn’t in the past). There’s no guarantee that the card itself is valid yet.

![](https://b.stripecdn.com/docs-statics-srv/assets/collect-card-details.2a81817764a4adc86c6d37e7efbb53cf.svg)

![](https://b.stripecdn.com/docs-statics-srv/assets/b7c1464dd02fdcfd323588c65e417322.svg)

Customer authenticationSome banks, especially in regulated regions like Europe and India, may prompt the customer to authenticate a purchase (for example, by texting the customer a code to enter on the bank’s website). Watch our video to learn more.

![](https://b.stripecdn.com/docs-statics-srv/assets/requires-action.a062dfa0d428b32132566ba7ef1d7243.svg)

![](https://b.stripecdn.com/docs-statics-srv/assets/e7ac3b4c7ee721fbac555ab73ac53443.svg)

AuthorizationThe bank checks for sufficient funds and, if successful, holds the amount on the customer’s account to guarantee it for the Stripe user.

![](https://b.stripecdn.com/docs-statics-srv/assets/Card-statement-pending.8c8594ba68e57f92be51bea871cd51de.svg)

![](https://b.stripecdn.com/docs-statics-srv/assets/6423ea22ac10bfa6996c6f9db9b0ad1d.svg)

CaptureThe money moves from the issuing bank to the Stripe user’s account.

![](https://b.stripecdn.com/docs-statics-srv/assets/Card-statement-succeeded.25905919ede8f790dec2989ab3111f04.svg)

## Card updates

Updating a saved card can only change its name, billing address, expiration date, or metadata. To make any other changes, you must delete the card and create a new one.

To let your customers manage their own payment methods, implement processes that allow them to manually update and replace their saved cards.

To change a customer’s default payment method for invoices and subscriptions, make an API call to update customer and provide a new value for the invoice_settings.default_payment_method property.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers/cus_V9T7vofUbZMqpv \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "invoice_settings[default_payment_method]"=pm_1Msy7wLkdIwHu7ixsxmFvcz7`For information on how Checkout handles saved payment methods, see the create session API reference. To consider default payment methods in other scenarios, use custom code.

## Automatic card updates

Saved payment method details can continue to work even if the issuing bank replaces the physical card. Stripe works with card networks and automatically attempts to update saved card details whenever a customer receives a new card (for example, replacing an expired card or one that was reported lost or stolen). This allows your customers to continue using your service without interruption and reduces the need for you to collect new card details whenever a card is replaced.

Automatic card updates require card issuers to participate with the network and provide this information. It is widely supported in the United States, allowing Stripe to automatically update most American Express, Visa, Mastercard, and Discover cards issued there. International support varies from country to country. It isn’t possible to identify cards that support automatic updates.

You can listen for Stripe webhooks to learn of card update activity:

- The`payment_method.updated`event notifies you of updates to a card through an API call
- The`payment_method.automatically_updated`event notifies you of automatic card updates from the network

These events include the card’s new expiration date and last four digits, so you can update your own records as needed.

## See also

- [Cards](/payments/cards)
- [Co-badged cards compliance](/co-badged-cards-compliance)
- [Payment method integration options](/payments/payment-methods/integration-options)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Card updates](#card-updates)[Automatic card updates](#automatic-card-updates)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`