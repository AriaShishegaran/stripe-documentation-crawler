htmlIndia recurring payments | Stripe Documentation[Skip to content](#main-content)India recurring payments[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Findia-recurring-payments)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Findia-recurring-payments)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)
[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)Regulation support# India recurring payments

Learn how to update an integration to support RBI e-mandates.The Reserve Bank of India (RBI) issued a directive (amended subsequently in December 2020 and March 2021) that introduces additional security measures for recurring payments on India issued cards. These measures include:

- Banks need to register cardholders and create ane-mandatethrough a one-time process, using additional factor authentication (AFA) like[3D Secure (3DS)](/payments/3d-secure).
- Banks must alert cardholders at least 24 hours before charges take place and give them the ability to opt out of transactions.
- Recurring transactions over 15,000 INR (or equivalent in other currencies) must go through AFA each time.

If you’re an India-based Stripe user or an international (non-IN) Stripe user, your business is impacted if you have customers who use India cards for:

- Off-sessionpayments
- Subscriptions or Invoices where the`collection_method`is set to`charge_automatically`

## How payments work with an e-mandate

Stripe has worked with a partner platform to support registering e-mandates and issuing pre-debit notifications to customers.

NoteWe don’t currently offer the use of e-mandates to Stripe users in Mexico and Japan.

Depending on how you’ve integrated with Stripe, you might need to send Stripe additional information to set up a mandate. The customer must go through AFA (3DS) to register the mandate.

Subsequent off-session payments or auto-debits for a Subscription undergo a significant change. Customers need to receive a pre-debit notification at least 24 hours before the actual payment with the exact debit amount mentioned. The pre-debit notification contains information about the payment and an option to cancel the mandate. If the payment amount is above 15,000 INR or the mandate’s maximum amount, the pre-debit notification contains a link to perform AFA (3DS) to authorize the payment.

Because Stripe is integrating with a partner platform, we wait 26 hours before charging the customer after receiving a payment request (we add a buffer for possible downstream issues, which necessitates the 26 hours advance notification). This means that Stripe delays collecting payment by 26 hours.

Without a mandate for an off-session payment, the card issuer will likely decline the payment.

## Integration



SubscriptionsPaymentIntents & SetupIntentsThe RBI regulations impact Subscriptions that use collection_method=charge_automatically to charge India issued cards.

### Subscription creation

Custom codePrebuilt checkout pageWhen creating a new Subscription with the API,

- If you have a default payment method set, the Subscription uses the latest SetupIntent on the payment method, and attempts to find a corresponding mandate.
- If no mandate is in place, Stripe automatically attempts to create one even if you don’t pass in the relevant parameters in[mandate_options](/api/subscriptions/create#create_subscription-payment_settings-payment_method_options-card-mandate_options). The customer then needs to authenticate the payment.

To learn how to create a new Subscription, see Build a subscriptions integration.

### Subscription Revenue Recovery

Stripe provides a number of automated recovery features to help collect payments that might’ve been unsuccessful. If you want to handle these payment failures on your own, refer to Build your own handling for recurring charge failures for guidance. Otherwise, some recommendations are listed below.

NotePayments from India issued cards are attempted only once. This behavior is independent of your payment retry settings. If the payment from an India issued card fails, your Subscription and Invoice status will still be updated based on what you configured in your Subscriptions and emails settings for “If all retries for a payment fail”.

3D Secure emails![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If a mandate doesn’t exist on the default payment method during Subscription renewals or updates, Stripe attempts to create a new one. To register the mandate, the customer needs to complete AFA (3DS). Enable the Subscriptions and emails settings to Send a Stripe-hosted link for customers to confirm their payments when required so that customers can be brought back on-session to complete authentication if required.

NoteStripe doesn’t attempt to create a new mandate if the current mandate used by the Subscription is inactive.

Manage failed payments![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

We recommend enabling notifications to your customers if their Subscription payments fail and their Subscription is paused. Stripe can send emails to customers to update failed card payment methods if you enable it in the Subscriptions and emails settings.

### Mandate webhooks

If you rely on Stripe to automatically create the mandate, the mandate details are returned in the Invoice’s underlying PaymentIntent and corresponding Charge, or the SetupIntent if you’re creating the Subscription with a trial.

Stripe doesn’t return a mandate ID if any of the following is true:

- A card isn’t an India issued card.
- The currency for the mandate isn’t supported by either the issuer or for the Stripe account’s country.
- The India issued card is neither Visa nor Mastercard. Stripe only supports mandates for these two card brands.

Stripe supports INR mandates for all businesses. The following currencies are supported only for international (non-IN) businesses:

- USD
- EUR
- GBP
- SGD
- CAD
- CHF
- SEK
- AED
- JPY
- NOK
- MYR
- HKD

There are over 100 issuing banks in India and the process of fully adapting to the new requirements is expected to take some time. An issuer might not support e-mandates for a particular currency yet. If so, Stripe doesn’t return a mandate ID.

PaymentIntentSetupIntentYou can find the mandate_options in the PaymentIntent.

`{
  "object": {
    "id": "pi_xxxxxxxxxxxxxxxxxxxxxxxx",
    "object": "payment_intent",
    ...
    "payment_method": "pm_xxxxxxxxxxxxxxxxxxxxxxxx",
    "payment_method_options": {
      "card": {
        "installments": null,
        "mandate_options": {
          "amount": 2000000,
          "amount_type": "maximum",
          "description": "{{DESCRIPTION}}",
          "end_date": null,
          "interval": "month",
          "interval_count": 1,
          "reference": "{{REFERENCE}}",
          "start_date": 1675238400,
          "supported_types": [
            "india"
          ]
        },
        ...
      }
    },
    ...
  }
}`The mandate ID is in the PaymentIntent’s corresponding Charge object. See Identifying charges on a PaymentIntent to learn more about how to retrieve the Charge.

`{
  "id": "ch_xxxxxxxxxxxxxxxxxxxxxxxx",
  "object": "charge",
  "payment_intent": "pi_xxxxxxxxxxxxxxxxxxxxxxxx",
  "payment_method": "pm_xxxxxxxxxxxxxxxxxxxxxxxx",
  "payment_method_details": {
    "card": {
      "brand": "visa",
      "country": "IN",
      "mandate": "mandate_xxxxxxxxxxxxxxxxxxxxxxxx", // id of the mandate created
      ...
  },
  ...
  "status": "succeeded",
  ...
}`Even though the PaymentIntent or SetupIntent might have transitioned into status=succeeded, the mandate might not yet be active. Stripe creates the Mandate object in the pending state. When the mandate transitions to an active state, we send a mandate.updated event. In rare cases, a mandate can take up to 30 minutes to transition to active in live mode. If the mandate doesn’t become active after 30 minutes, assume that you can’t use the mandate.

`{
  "object": {
    "id": "mandate_xxxxxxxxxxxxxxxxxxxxxxxx",
    "object": "mandate",
    "customer_acceptance": {
      "accepted_at": 1677301688,
      "online": {
        "ip_address": "xx.xxx.xx.xxx",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
      },
      "type": "online"
    },
    "livemode": false,
    "multi_use": {
    },
    "payment_method": "pm_xxxxxxxxxxxxxxxxxxxxxxxx",
    "payment_method_details": {
      "card": {
      },
      "type": "card"
    },
    "status": "active",
    "type": "multi_use"
  },
  "previous_attributes": {
    "status": "pending"
  }
}`If Stripe can’t create a mandate, you can suggest using a different card, or you can offer alternative options such as setting collection_method as send_invoice for the Subscription instead.

Also, a previously active mandate can become inactive, for instance if the customer cancels it. In that case, the mandate becomes inactive and Stripe sends a mandate.updated event.

For more information on receiving webhooks, see Steps to receive webhooks.

### Subscription updates

The pre-debit notification that the bank sends tells the cardholder, at minimum, about the name of the business, the transaction amount, the date or time of the debit, the reference number of the mandate, and the reason for debit. Make sure that your mandate details match what you’re actually debiting the customer for to avoid confusion or declines.

If you depend on Stripe to automatically create mandates for your Subscription and want to update a Subscription, we recommend that you bring the customer back on-session to cancel the original Subscription. Doing so creates a new subscription in the following scenarios, and creates a new mandate that reflects the Subscription details accurately:

- Changes to the billing interval of a Subscription
- Upgrades to a Subscription where the customer wants to avoid having to authorize the payment each renewal. For context, Stripe creates the mandate with`amount_type=maximum`by default. A customer can still be charged more than the maximum amount with`amount_type=maximum`. However, the customer must authorize payments for amounts more than the`mandate_options[amount]`or 15,000 INR (whichever is less).

Examples:

- If you have`amount_type=maximum`,`amount=100000`, the customer would need to authenticate for amounts over 1,000 INR.
- If you have`amount=2000000`, the customer would need to authenticate for amounts over 15,000 INR.

### Pre-debit notification

When the off-session PaymentIntent is confirmed, the issuing bank sends the customer the pre-debit notification. The PaymentIntent transitions to a processing state for the entire duration of the pre-debit notification period (26 hours) and can’t be canceled.

`{
  "object": "payment_intent",
  ...
  "processing": {
    "card": {
      "customer_notification": {
        "approval_requested": true,
        "completes_at": 1677307005
      }
    },
    "type": "card"
  },
  ...
  "status": "processing",
  ...
}`If processing.card.customer_notification.approval_requested is true, the customer needs to authenticate the payment using the pre-debit notification sent to them by the issuing bank.

The processing.card.customer_notification.completes_at attribute specifies the time that the Stripe attempts to charge the card. If successfully processing the payment requires customer approval, they need to authenticate the payment by the specified time.

### Error and decline codes

We return error codes for the following scenarios:

Error codeDescription`payment_intent_mandate_invalid`Attempting a recurring payment using an inactive mandate returns this code. You can prevent this by checking the mandate status before attempting to charge.`india_recurring_payment_mandate_canceled`Attempting a recurring payment using a canceled mandate returns this code. This can happen when we only learn that a mandate has been canceled at this point.`processing_error`Discovery of a (usually transient) processing error returns this code.In the context of e-mandates, certain decline codes have potentially more specific explanations than in general scenarios:

Decline codeDescription`transaction_not_approved`Attempting a subsequent payment when the customer has paused permissions to auto-debit, or doesn’t authenticate the payment when it’s required returns this code.## Testing

You can use these test card numbers to simulate different scenarios.

In test mode, it takes approximately 15 minutes for an off-session PaymentIntent to transition out of the processing state. The on-session PaymentIntent for an initial payment never enters the processing state.

Test card numberScenario4000003560000123Simulates successful mandate setup and renewals.4000003560000297Simulates a cardholder receiving a pre-debit notification for an off-session payment either canceling or pausing the payment for a mandate of any amount.4000003560000248Simulates the issuing bank’s failure to send a pre-debit notification to the cardholder during off-session payment for a mandate of any amount.4000003560000263Simulates a cardholder canceling a mandate of any amount.## Limitations

Keep in mind the following limitations:

- Stripe attempts to automatically create mandates only on Subscriptions created after October 1, 2021. If you have a Subscription created before then, cancel and create a new Subscription to make sure a mandate is created.
- You can’t create a mandate using the[Charges](/api/charges)and[Sources](/api/sources)APIs. If you want to create a mandate, you must use the PaymentIntent or SetupIntent APIs.
- You can’t pass an existing mandate to a Subscription.
- You can’t cancel or update a mandate.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[How payments work with an e-mandate](#how-payments-work-with-an-e-mandate)[Integration](#integration)[Subscription creation](#subscription-creation)[Subscription Revenue Recovery](#subscription-revenue-recovery)[Mandate webhooks](#webhooks)[Subscription updates](#subscription-updates)[Pre-debit notification](#predebit-notification)[Error and decline codes](#error-and-decline-codes)[Testing](#testing)[Limitations](#limitations)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`