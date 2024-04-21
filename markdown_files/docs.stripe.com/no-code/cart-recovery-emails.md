htmlCart Recovery Emails | Stripe Documentation[Skip to content](#main-content)Cart Recovery Emails[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Fcart-recovery-emails)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Fcart-recovery-emails)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/no-code)[Find your use case](/docs/no-code/get-started)[No-code payments](#)[Customer experience](#)
NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[No-code](/docs/no-code)Customer experience# Cart Recovery EmailsBeta

Automatically send emails to remind customers to complete their purchase.Customers might leave a Payment Link or Checkout session before completing their purchase—also known as cart abandonment. Enable no-code automated cart recovery emails, directly from the Dashboard, to email customers to complete their purchase and boost your revenue and conversion.

Cart Recovery Emails is currently in invite only beta for US businesses. To request early access for your Stripe account, sign up here.

### Available in Beta

United States## Get started

If you don’t have a Stripe account, sign up now.

Stripe sends Cart Recovery Emails from the marketing email domain (marketing@marketing.stripe.com) but we encourage you to onboard your own Custom Email Domain. This allows customers to receive these emails from your own domain resulting in better deliverability and conversion rates.

## Enable Cart Recovery Emails

![sample email](https://b.stripecdn.com/docs-statics-srv/assets/cart-recovery-email.fad5422a229cebffff9984b45ca62974.png)

Sample cart recovery email

1. Go to your Stripe Dashboard.
2. Navigate to Settings and click[Checkout and Payment Links](https://dashboard.stripe.com/settings/checkout#cart-recovery-emails). You can see and send a preview of the cart recovery email there and customize it if necessary.![cart recovery email settings](https://b.stripecdn.com/docs-statics-srv/assets/checkout-settings-cart-recovery.2d64419f339e7c71d5f115b1d747279b.png)


3. Review and, if acceptable, accept the Cart Recovery Emails terms and conditions.
4. (Optional) Configure a custom reply-to address; this allows you to receive replies from customers. The default address is no-reply@stripe.com, and customer replies aren’t sent to you.

## Collect consent for promotional emails

To send cart recovery emails, you need to collect consent from customers. Depending on how you create your Payment Link or Checkout session, you might need to take additional actions.

Additional actionsPayment Link created in the Dashboard (No-code)No additional action is required.`consent_collection`is automatically set and your customers receive recovery emails. You’ll also receive events if you’ve configured a webhook endpoint.Payment Link created with the APIPass[“consent_collection[promotions]”=auto](/api/checkout/sessions/create#create_checkout_session-consent_collection-promotions)when you create the Payment Link.Checkout created with the APIPass[“consent_collection[promotions]”=auto](/api/checkout/sessions/create#create_checkout_session-consent_collection-promotions)when you create the Checkout session.After consent_collection is set, the customer sees a checkbox below the email address field on the checkout page asking them to consent to receiving promotional emails.

## Sending Cart Recovery Emails

Emails are automatically sent on your behalf to the customer when the checkout session expires (defaults to 24 hours). Checkout sessions created with the API can change this using the expires_at field. The following requirements must also be satisfied:

- The checkout session isn’t testmode.
- The customer consented to receiving promotional emails on the checkout page and provided a complete email address.
- The customer doesn’t have a later checkout session with you. For example, if the customer created checkout sessions A and B (in that order) and both expire, only B will have a recovery email sent. If B had been completed successfully, no emails would be sent.

## Finding recovered payments

We display a Recovered badge on the Payment details page in the Dashboard if the payment is recovered using a cart recovery email.



## Recover abandoned carts using the API

If you’re a developer and want to further customize your cart recovery emails, consider recovering abandoned carts using the API.

## Sync customer promotional subscriptions with other services

Because your business might use various platforms to send promotional emails, make sure that you synchronize these emails across all systems when customers subscribe or unsubscribe to them.

In the Stripe Dashboard, you can synchronize recipient promotional subscriptions with other systems:

- Download a CSV file containing the promotional email subscriptions for each email address that Stripe has ever collected promotional consent from.
- Upload CSV files containing updated promotional subscription data per email address, which updates the subscription statuses that Stripe has on record for each recipient.

![](https://b.stripecdn.com/docs-statics-srv/assets/sync-subscriptions-settings.fb75370f685c42b1197be4dd4b320e24.png)

Sync subscriptions settings section

### Download recipient promotional email subscriptions

To download the subscriptions, go to the Email settings page in the Dashboard and click Download customer marketing email subscriptions.

This initiates a download of a CSV file containing the promotional email subscription statuses of all email addresses Stripe has a subscription status for. It also includes the date when that change was made.

CSV format headers![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Email address
- Subscription status  - Either`Subscribed`or`Unsubscribed`


- Updated at  - A date and time, in UTC, which conveys when the update time



Sample CSV![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Email addressSubscription statusUpdated atexample@gmail.comSubscribed2023-10-23T20:58:02+00:00jonathan@hotmail.comUnsubscribed2023-10-23T20:58:02+00:00### Upload promotional email subscriptions

To synchronize Stripe’s subscription status with other systems, you can upload subscription statuses per email address.

In the Email settings page in the Dashboard, you can upload a CSV file containing subscription statuses per email address. You can also include a date field for the updated at status to Stripe’s system. If a date field isn’t specified, the system defaults to the uploaded status.

CSV format headers![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

- Email address
- Subscription status  - Either`Subscribed`or`Unsubscribed`


- Updated at (optional)  - Date and time in ISO 8601 format or Unix timestamp.



Sample CSV![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Email addressSubscription statusUpdated atadrian@gmail.comSubscribed2023-10-23T20:58:02+00:00jonathan@hotmail.comUnsubscribedexample@gmail.comSubscribed1698094682## View marketing email subscription for a customer

You can view the marketing subscription for a customer on the Customers page in the Dashboard.

![](https://b.stripecdn.com/docs-statics-srv/assets/customer-detail-page-marketing-prefs.030fda62a655721b1a5371bbc450876e.png)

Marketing email preferences in customer details page

This table describes the customer’s overall subscription, as well as their granular marketing email preferences.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get started](#get-started)[Enable Cart Recovery Emails](#enable-cart-recovery-emails)[Collect consent for promotional emails](#collect-consent-for-promotional-emails)[Sending Cart Recovery Emails](#sending-cart-recovery-emails)[Finding recovered payments](#finding-recovered-payments)[Recover abandoned carts using the API](#recover-abandoned-carts-using-the-api)[Sync customer promotional subscriptions with other services](#sync-customer-promotional-subscriptions-with-other-services)[View marketing email subscription for a customer](#view-marketing-email-subscription-for-a-customer)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`