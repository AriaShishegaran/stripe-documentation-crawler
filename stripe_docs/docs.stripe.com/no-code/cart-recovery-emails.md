# Cart Recovery EmailsBeta

Customers might leave a Payment Link or Checkout session before completing their purchase—also known as cart abandonment. Enable no-code automated cart recovery emails, directly from the Dashboard, to email customers to complete their purchase and boost your revenue and conversion.

[cart abandonment](/payments/checkout/compliant-promotional-emails)

Cart Recovery Emails is currently in invite only beta for US businesses. To request early access for your Stripe account, sign up here.

[here](https://forms.gle/wNkyKBSirJj6GFXv6)

## Get started

If you don’t have a Stripe account, sign up now.

[sign up now](https://dashboard.stripe.com/register/payment_links)

Stripe sends Cart Recovery Emails from the marketing email domain (marketing@marketing.stripe.com) but we encourage you to onboard your own Custom Email Domain. This allows customers to receive these emails from your own domain resulting in better deliverability and conversion rates.

[Custom Email Domain](https://dashboard.stripe.com/settings/emails)

## Enable Cart Recovery Emails

Sample cart recovery email

- Go to your Stripe Dashboard.

- Navigate to Settings and click Checkout and Payment Links. You can see and send a preview of the cart recovery email there and customize it if necessary.

[Checkout and Payment Links](https://dashboard.stripe.com/settings/checkout#cart-recovery-emails)

- Review and, if acceptable, accept the Cart Recovery Emails terms and conditions.

- (Optional) Configure a custom reply-to address; this allows you to receive replies from customers. The default address is no-reply@stripe.com, and customer replies aren’t sent to you.

## Collect consent for promotional emails

To send cart recovery emails, you need to collect consent from customers. Depending on how you create your Payment Link or Checkout session, you might need to take additional actions.

[collect consent from customers](/payments/checkout/promotional-emails-consent)

[“consent_collection[promotions]”=auto](/api/checkout/sessions/create#create_checkout_session-consent_collection-promotions)

[“consent_collection[promotions]”=auto](/api/checkout/sessions/create#create_checkout_session-consent_collection-promotions)

After consent_collection is set, the customer sees a checkbox below the email address field on the checkout page asking them to consent to receiving promotional emails.

## Sending Cart Recovery Emails

Emails are automatically sent on your behalf to the customer when the checkout session expires (defaults to 24 hours). Checkout sessions created with the API can change this using the expires_at field. The following requirements must also be satisfied:

- The checkout session isn’t testmode.

- The customer consented to receiving promotional emails on the checkout page and provided a complete email address.

- The customer doesn’t have a later checkout session with you. For example, if the customer created checkout sessions A and B (in that order) and both expire, only B will have a recovery email sent. If B had been completed successfully, no emails would be sent.

## Finding recovered payments

We display a Recovered badge on the Payment details page in the Dashboard if the payment is recovered using a cart recovery email.

[Payment](https://dashboard.stripe.com/payments)



## Recover abandoned carts using the API

If you’re a developer and want to further customize your cart recovery emails, consider recovering abandoned carts using the API.

[recovering abandoned carts using the API](/payments/checkout/abandoned-carts)

## Sync customer promotional subscriptions with other services

Because your business might use various platforms to send promotional emails, make sure that you synchronize these emails across all systems when customers subscribe or unsubscribe to them.

In the Stripe Dashboard, you can synchronize recipient promotional subscriptions with other systems:

- Download a CSV file containing the promotional email subscriptions for each email address that Stripe has ever collected promotional consent from.

- Upload CSV files containing updated promotional subscription data per email address, which updates the subscription statuses that Stripe has on record for each recipient.

Sync subscriptions settings section

To download the subscriptions, go to the Email settings page in the Dashboard and click Download customer marketing email subscriptions.

[Email settings page](https://dashboard.stripe.com/settings/emails)

This initiates a download of a CSV file containing the promotional email subscription statuses of all email addresses Stripe has a subscription status for. It also includes the date when that change was made.

- Email address

- Subscription statusEither Subscribed or Unsubscribed

- Either Subscribed or Unsubscribed

- Updated atA date and time, in UTC, which conveys when the update time

- A date and time, in UTC, which conveys when the update time

To synchronize Stripe’s subscription status with other systems, you can upload subscription statuses per email address.

In the Email settings page in the Dashboard, you can upload a CSV file containing subscription statuses per email address. You can also include a date field for the updated at status to Stripe’s system. If a date field isn’t specified, the system defaults to the uploaded status.

[Email settings page](https://dashboard.stripe.com/settings/emails)

- Email address

- Subscription statusEither Subscribed or Unsubscribed

- Either Subscribed or Unsubscribed

- Updated at (optional)Date and time in ISO 8601 format or Unix timestamp.

- Date and time in ISO 8601 format or Unix timestamp.

## View marketing email subscription for a customer

You can view the marketing subscription for a customer on the Customers page in the Dashboard.

[Customers page](https://dashboard.stripe.com/customers)

Marketing email preferences in customer details page

This table describes the customer’s overall subscription, as well as their granular marketing email preferences.
