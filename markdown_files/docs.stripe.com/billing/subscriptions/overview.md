htmlHow subscriptions work | Stripe Documentation[Skip to content](#main-content)How subscriptions work[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Foverview)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Foverview)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)# How subscriptions work

Learn how subscriptions work within Stripe.With Subscriptions, customers make recurring payments for access to a product. Subscriptions require you to retain more information about your customers than one-time purchases because you need to charge them in the future.

[Subscription objects](#subscription-objects)Use the following core API resources to build and manage subscriptions:

ResourceDefinition[Product](/api/products)What your business offers — whether that’s a good or a service.[Price](/api/prices)How much and how often to charge for products, including how much the product costs, what currency to use, and the interval if the price is for subscriptions.[Customer](/api/customers)Stripe Customer objects allow you to perform recurring charges for the same customer, and to track multiple charges. If you create subscriptions, the customer ID is passed to the subscription object.[PaymentMethod](/api/payment_methods)Your customer’s payment instruments–how they pay for your service. For example, you may store a credit card on the customer object for recurring use. Typically used with the Payment Intents or Setup Intents APIs.[Subscription](/api/subscriptions)The product details associated with the plan that your customer subscribes to, which allow you to charge the customer on a recurring basis.[Invoice](/api/invoices)A statement of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices. You can also manually create one-off invoices.[PaymentIntent](/api/payment_intents)A way to build dynamic payment flows. A Payment Intent tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods. Invoices create payment intents automatically.![How Stripe objects work in a subscription lifecycle.](https://b.stripecdn.com/docs-statics-srv/assets/abstractions.c0365799e62eac96eed3e9e746e3b65b.svg)

[Integration example](#integration-example)This section describes our sample integration on GitHub, which illustrates how to build a subscriptions integration. If you’re ready to build your own integration, see the Billing quickstart or integration guide.

### Landing page

On your frontend, the landing page collects the email address first. Your application might have other customer-specific information you want to collect like a username or address. Clicking the signup button sends the information collected on the landing page to your backend. This process creates a customer and displays the pricing page on your frontend.

### Pricing page

The pricing page displays your subscription options based on the products and prices you create when you first set up your integration, meaning you don’t need to create new ones every time customers sign up. Your pricing page displays the prices you created, and your customers choose the option they want. The example on GitHub displays a payment form when a customer selects an option.

Learn more about products and prices.

### Payment

The payment form collects a name and card information. Stripe hosts this form if you use Checkout. It’s one of the key features that allows you to collect payments and remain PCI compliant. Clicking Subscribe:

1. Creates a new subscription with your customer and price IDs.
2. Generates an invoice for your initial subscription cycle.
3. Collects payment details and pays your invoice.
4. Sets the payment method as the default payment method for the subscription-a requirement for subsequent payments.

NoteYou should confirm payment before provisioning access for your customer.

To implement this:

- No code—If you don’t want to write any code, learn how to[create a Payment Link](/payment-links)and share it with your customers.
- Low code—If you’re using Checkout, learn how to[add a button to your website that creates a Checkout Session](/billing/subscriptions/build-subscriptions?ui=stripe-hosted#create-session).
- Custom code—If you’re using Elements, learn how to[collect payment details and activate the subscription](/billing/subscriptions/build-subscriptions?ui=elements#collect-payment)with the Payment Element or Card Element.

### Provisioning

Use Entitlements to determine when you can grant or revoke product feature access to your customers.

Alternatively, after a successful payment, you can safely provision the product for the customer. This generally means:

1. Verifying the status of the subscription is`active`.
2. Granting the customer access to the products and features they subscribed to.

Learn how to use webhooks to:

- [Track active subscriptions](/billing/subscriptions/webhooks#active-subscriptions)
- [Handle payment failures](/billing/subscriptions/webhooks#payment-failures)
- [Check event objects](/webhooks#events-overview)

Interested in getting early access to Entitlements?Please provide your email address below and our team will contact you soon.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.[How payments work with subscriptions](#how-payments-work-subscriptions)To simplify the handling of failed payments and to create subscriptions before attempting payment:

1. Pass[payment_behavior=default_incomplete](/api/subscriptions/create#create_subscription-payment_behavior)when creating a subscription. If your subscription requires payment, it’s created with an`incomplete`status, otherwise your subscription immediately becomes`active`.
2. Activate an incomplete subscription by paying the first invoice.
3. Pass the payment intent identifier from the invoice to your user interface to collect payment information andconfirmthe payment intent. You can use[Elements](/js/elements_object), the[Android SDK](https://stripe.dev/stripe-android/), or the[iOS SDK](https://stripe.dev/stripe-ios/).

### Payment status

The payment process differs across payment methods and geographical locations. Payments can also fail initially (for example, a customer might enter the wrong card number or have insufficient funds), so various payment outcomes are possible.

A PaymentIntent tracks the lifecycle of every payment. Whenever a payment is due for a subscription, Stripe generates an invoice and a PaymentIntent. The PaymentIntent ID attaches to the invoice and you can access it from the Invoice and Subscription objects. The state of the PaymentIntent affects the state of the invoice and the subscription. Here’s how the different outcomes of a payment map to the different statuses:

Payment outcomePaymentIntent statusInvoice statusSubscription statusSuccess`succeeded``paid``active`Fails because of a card error`requires_payment_method``open``incomplete`Fails because of authentication`requires_action``open``incomplete`The following sections explain these statuses and the actions to take for each.

### Payment succeeded

When your payment succeeds, the status of the PaymentIntent is succeeded, and the subscription becomes active. For payment methods with longer processing periods, subscriptions are immediately activated. In these cases, the status of the PaymentIntent may be processing for an active subscription until the payment succeeds.

With your subscription now activated, provision access to your product. Read the guide to learn more about the subscription lifecycle and best practices for provisioning.

ResponseSubscriptionPaymentIntent`{
  "id": "sub_1ELI8bClCIKljWvsvK36TXlC",
  "object": "subscription",
  "status": "active",
  ...
  "latest_invoice": {
    "id": "in_EmGqfJMYy3Nt9M",
    "status": "paid",
    ...
    "payment_intent": {
      "status": "succeeded",
      ...
    }
  }
}`activesucceeded![Subscription payment network flow.](https://b.stripecdn.com/docs-statics-srv/assets/payment-flow-succeeds.ac7343c9ec9a77e6efa1a84c02bb597d.svg)

### Requires payment method

If payment fails because of a card error, such as a decline, the status of the PaymentIntent is requires_payment_method and the subscription is incomplete.

ResponseSubscriptionPaymentIntent`{
  "id": "sub_1ELI8bClCIKljWvsvK36TXlC",
  "object": "subscription",
  "status": "incomplete",
  ...
  "latest_invoice": {
    "id": "in_EmGqfJMYy3Nt9M",
    "status": "open",
    ...
    "payment_intent": {
      "status": "requires_payment_method",
      ...
    }
  }
}`incompleterequires_payment_methodTo resolve these scenarios:

- Notify the customer.
- Collect new payment information and[confirm the payment intent](/api/payment_intents/confirm).
- Update the[default payment method](/api/subscriptions/object#subscription_object-default_payment_method)on the subscription.

Learn how to handle payment failures for subscriptions.

![How to handle subscription payment failures.](https://b.stripecdn.com/docs-statics-srv/assets/payment-flow-requires-payment-method.8305917aa91650ba7f7e9b6e5999ce32.svg)

### Requires action

Some payment methods require customer authentication with 3D Secure (3DS) to complete the payment process. If you use the Payment Intents API, the value of latest_invoice.payment_intent.status is requires_action when a customer needs to authenticate a payment. 3DS completes the authentication process. Whether a payment method requires authentication depends on your Radar rules and the issuing bank for the card.

Regulations in Europe often require 3D Secure. See Strong Customer Authentication to determine whether handling this status is important for your business. If you have an existing billing integration and want to add support for this flow, also see the Billing SCA Migration guide.

ResponseSubscriptionPaymentIntent`{
  "id": "sub_1ELI8bClCIKljWvsvK36TXlC",
  "object": "subscription",
  "status": "incomplete",
  ...
  "latest_invoice": {
    "id": "in_EmGqfJMYy3Nt9M",
    "status": "open",
    ...
    "payment_intent": {
      "status": "requires_action",
      "client_secret": "pi_91_secret_W9",
      "next_action": {
        "type": "use_stripe_sdk",
        ...
      },
      ...
    }
  }
}`incompleterequires_actionTo handle these scenarios:

- Monitor for the`invoice.payment_action_required`event notification with[webhooks](/billing/subscriptions/webhooks). This indicates that authentication is required.
- Notify your customer that they must authenticate.
- Retrieve the client secret for the payment intent and pass it in a call to[stripe.ConfirmCardPayment](/js/payment_intents/confirm_card_payment). This displays an authentication modal to your customers, attempts payment, then closes the modal and returns context to your application.
- Monitor the`invoice.paid`event on your webhook endpoint to verify that the payment succeeded. Users can leave your application before`confirmCardPayment()`finishes. Verifying whether the payment succeeded allows you to correctly provision your product.

![How to handle subscription payments that require additional action from the customer.](https://b.stripecdn.com/docs-statics-srv/assets/payment-flow-requires-action.ac57889e9bccdb6ec4f5ea47fba194ec.svg)

### Recurring charges

Stripe handles recurring charges for you automatically. This includes:

- [Automatically invoicing](/billing/invoices/subscription#subscription-renewal)customers and attempting payments when new billing cycles start.
- When payments fail, Stripe retries them using the[Smart Retries](/invoicing/automatic-collection#smart-retries)feature. This automatically re-attempts payment when cards are declined according to your Dashboard settings.

You can send a dunning email to customers for overdue payments to increase recovery chances. For payments that require 3D Secure, you can configure your billing settings to send a hosted link to customers so they can complete the flow.

Build your own handling for recurring charge failures![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If you don’t want to use Stripe’s tooling to manage failures, you can build your own. If a payment fails or if it requires customer authentication, the subscription’s status is set to past_due and the PaymentIntent status is either requires_payment_method or requires_action.

![Objects involved when handling failed or action required subscription payments.](https://b.stripecdn.com/docs-statics-srv/assets/recurring-charge-failure.f0db8a9b3a90000f3df0b98f7aacfa36.svg)

To manage these scenarios, set up a webhook and listen to the customer.subscription.updated event so that you’re notified when subscriptions enter a past_due state:

`{
  "id": "sub_E8uXk63MAbZbto",
  "object": "subscription",
  ...
  "status": "past_due",
  "latest_invoice": "in_1EMLu1ClCIKljWvsfTjRFAxa"
}`For these subscriptions, you need to get your customers back into your application to collect a different payment method so they can complete the payment. You can use an email or a mobile push notification. Stripe provides built-in reminder emails to handle this case, which you can configure in your billing settings.

When your customer is back in your application, reuse either your payment failure flow or customer action flow depending on the status of the associated PaymentIntent. After the payment succeeds, the status of the subscription is active and the invoice is paid.

### Handle non-payment invoices

Subscriptions that include free trials, usage-based billing, invoices with coupons, or applied customer credit balances often result in non-payment invoices. This means you don’t immediately charge your customer when you create the subscription.

Even though you don’t charge customers for the first invoice, authenticating and authorizing their card is often beneficial as it can increase the chance that the first non-zero payment completes successfully. Payments made this way are known as off-session payments. To manage these scenarios, Stripe created SetupIntents.

Using SetupIntents![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You can use SetupIntents to:

- Collect payment information.
- Authenticate your customer’s card to claim[exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication)later.
- Authorize your customer’s card without charging it.

Authenticating payments allows your customer to grant permissions to charge their card. Strong Customer Authentication requires this, and 3DS is a common way to complete it. Collecting payment method information and authorizing it ensures that you can successfully charge the payment method.

In off-session scenarios, SetupIntents enable you to charge customers for their first non-zero payment without having to bring them back to your website or app for authentication. This reduces the friction on your customers.

The pending_setup_intent field on a subscription doesn’t cancel automatically when the subscription ends. Listen for customer.subscription.deleted webhooks and manually cancel a subscription SetupIntent if needed.

Stripe automatically creates SetupIntents for subscriptions that don’t require an initial payment. The authentication and authorization process also completes at this point, if required. If both succeed or aren’t required, no action is necessary, and the subscription.pending_setup_intent field is null. If either step fails, Stripe recommends using the SetupIntent on your frontend to resolve the issue while your customer is on-session. The next two sections explain in detail how to manage scenarios where authentication or authorization fail.

Managing authentication failuresClient-side![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Authentication failures occur when Stripe is unable to authenticate your customer with their card issuer. When this happens, the status of the SetupIntent is set to requires_action.

![How to handle subscription payment authentication failures.](https://b.stripecdn.com/docs-statics-srv/assets/authentication_failure.2eaec43cac8c688f0ff3438fbe3b50e4.svg)

To resolve these scenarios, call confirmCardSetup on your frontend so that your customer can complete the authentication flow manually. The code example below expands the pending_setup_intent to complete the flow.

`const {pending_setup_intent} = subscription;

if (pending_setup_intent) {
  const {client_secret, status} = subscription.pending_setup_intent;

  if (status === "requires_action") {
    const {setupIntent, error} = await stripe.confirmCardSetup(client_secret);

    if (error) {
      // Display error.message in your UI.
    } else {
      // The setup has succeeded. Display a success message.
    }
  }
}`After completing this flow, authorization executes if it’s required. If authorization succeeds, or if it’s not required, pending_setup_intent is updated to null upon completion.

Managing authorization failuresClient-side![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Payment authorization failures occur when Stripe can’t verify that a card can be charged. When this happens, the status of the SetupIntent is set to requires_payment_method. This generally means that subsequent charges with that card fail.

![How to handle subscription payment authorization failures.](https://b.stripecdn.com/docs-statics-srv/assets/authorization_failure.0b6ca4a2e2bbeba11710bf22fb0a5d00.svg)

To resolve these scenarios, collect a new payment method, then update the default payment method for your customer or the subscription. The code example below expands the pending_setup_intent to complete the flow.

`const {pending_setup_intent, latest_invoice} = subscription;

if (pending_setup_intent) {
  const {client_secret, status} = subscription.pending_setup_intent;

  if (status === "requires_action") {
    const {setupIntent, error} = await stripe.confirmCardSetup(client_secret);

    if (error) {
      // Display error.message in your UI.
    } else {
      // The setup has succeeded. Display a success message.
    }
  } else if (status === "requires_payment_method") {
    // Collect new payment method
  }
}`[The subscription lifecycle](#subscription-lifecycle)This is what the recommended subscription flow looks like:

### Payment behavior

If you set payment_behavior to default_incomplete, the subscription status is incomplete. Learn more about why we recommend using this type of payment behavior for subscriptions.

1. You create the subscription. The`status`of the subscription is`incomplete`(if you follow the recommended flow—if you create a subscription without specifying the`payment_behavior`, the default`status`is`active`).
2. An invoice is created for the subscription. The`status`of the invoice is`open`.
3. The customer pays the first invoice.
4. When the payment succeeds:  - The subscription`status`moves to`active`
  - The invoice`status`is set to`paid`
  - Stripe sends an`invoice.paid`event webhook event.


5. You provision access to your product. You can confirm whether the invoice has been paid by:  - Setting up a webhook endpoint and listening for the`invoice.paid`event.
  - Manually checking the subscription object and looking for`subscription.status=active`. The`status`becomes`active`when the invoice has been paid either through an automatic charge or having the customer pay manually.



The status can also become trialing if you offer trials that don’t require payments. When the trial is over, the subscription moves to active and the subscribed customer starts to be charged.

![Subscription creation and expiration workflow](https://b.stripecdn.com/docs-statics-srv/assets/lifecycle-default-incomplete.a6ba5c1779f0f9b8601166f41bbc6d88.svg)

### Subscription payment behavior

To simplify handling failed payments, create subscriptions with payment_behavior set to default_incomplete. This creates subscriptions with status incomplete, which allows you to collect and confirm payment information in a single user interface. When using allow_incomplete or error_if_incomplete, Stripe immediately attempts to pay the invoice. If the payment fails, the subscription’s status changes to incomplete or the creation fails.

### Successful payments

When your customer successfully pays the invoice, the subscription updates to active and the invoice to paid. At this point, you can provision access to your product.

Payment window![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Customers have about 23 hours to make a successful payment. The subscription remains in status incomplete and the invoice is open during this time. If your customer pays the invoice, the subscription updates to active and the invoice to paid. If they don’t make a payment, the subscription updates to incomplete_expired and the invoice becomes void.

This window exists because your customer usually makes the first payment for a subscription while on-session. If the customer returns to your application after 23 hours, create a new subscription for them.

### Failed payments

The subscription’s status remains active as long as automatic payments succeed. If automatic payment fails, the subscription updates to past_due and Stripe attempts to recover payment based on your retry rules. If payment recovery fails, you can set the subscription status to canceled, unpaid, or leave it past_due.

### Unpaid subscriptions

For unpaid subscriptions, the latest invoice remains open but payments aren’t attempted. The subscription continues to generate invoices each billing cycle and remains in draft state. To reactivate the subscription, you need to:

- Collect new payment information.
- Turn automatic collection back on by setting[auto advance](/api/invoices/update#update_invoice-auto_advance)to`true`on draft invoices.
- [Finalize](/api/invoices/finalize), then pay the open invoices. Pay the most recent invoice before its due date to update the status of the subscription to`active`.

Setting past_due subscriptions to unpaid is the default behavior because it gives you the most options for reactivating subscriptions.

### Cancel subscriptions

Canceling subscriptions disables creating new invoices for the subscription and stops automatic collection of all invoices from the subscription by setting auto_advance to false. It also deletes the subscription. If your customer wants to resubscribe, you need to collect new payment information from them and create a new subscription.

### Voiding an invoice generated by a subscription

If the subscription is incomplete and you void the first invoice that’s generated, the subscription updates to incomplete_expired. If you void the most recent invoice for an active subscription and it’s not the first one, the following logic is applied to each invoice (from most recent to oldest) until it meets one of these conditions:

- If the invoice is in a`paid`or`uncollectible`state, the subscription state is set to`active`.
- If the[collection_method](/api/invoices/object#invoice_object-collection_method)is set to`charge_automatically`on the invoice and Stripe stopped dunning on the invoice because of retry limits, the subscription state is set to`canceled`,`unpaid`, or`past_due`based on your[automatic collection settings](https://dashboard.stripe.com/settings/billing/automatic).
- If the[collection_method](/api/invoices/object#invoice_object-collection_method)is set to`send_invoice`, and the invoice is past its due date, the state of the subscription is set to`past_due`.
- If the invoice is in none of these states, the same steps execute on the next most recent invoice.

If no invoices match any of the above criteria, the subscription state is set to active.

### Subscription statuses

StatusDescription`trialing`The subscription is currently in a trial period and it’s safe to provision your product for your customer. The subscription transitions automatically to`active`when the first payment is made.`active`The subscription is in good standing and the most recent payment is successful. It’s safe to provision your product for your customer.`incomplete`A successful payment needs to be made within 23 hours to activate the subscription. Or the payment[requires action](#requires-action), like customer authentication. Subscriptions can also be`incomplete`if there’s a pending payment and the PaymentIntent status would be`processing`.`incomplete_expired`The initial payment on the subscription failed and no successful payment was made within 23 hours of creating the subscription. These subscriptions don’t bill customers. This status exists so you can track customers that failed to activate their subscriptions.`past_due`Payment on the latestfinalizedinvoice either failed or wasn’t attempted. The subscription continues to create invoices. Your[subscription settings](/billing/subscriptions/overview#settings)determine the subscription’s next state. If the invoice is still unpaid after all[Smart Retries](/billing/revenue-recovery/smart-retries)have been attempted, you can configure the subscription to move to`canceled`,`unpaid`, or leave it as`past_due`. To move the subscription to`active`, pay the most recent invoice before its due date.`canceled`The subscription has been canceled. During cancellation, automatic collection for all unpaid invoices is disabled (`auto_advance=false`). This is a terminal state that can’t be updated.`unpaid`The latest invoice hasn’t been paid but the subscription remains in place. The latest invoice remains open and invoices continue to be generated but payments aren’t attempted. You should revoke access to your product when the subscription is`unpaid`since payments were already attempted and retried when it was`past_due`. To move the subscription to`active`, pay the most recent invoice before its due date.`paused`The subscription has ended its trial period without a default payment method and the[trial_settings.end_behavior.missing_payment_method](/billing/subscriptions/trials#create-free-trials-without-payment)is set to`pause`. Invoices will no longer be created for the subscription. After a default payment method has been attached to the customer, you can[resume the subscription](/billing/subscriptions/trials#resume-a-paused-subscription).[Subscription events](#subscription-events)Events are triggered every time a subscription is created or changed. We send some events immediately when a subscription is created, while others recur on regular billing intervals. We recommend listening for events with a webhook endpoint.

Make sure that your integration properly handles the events. For example, you might want to email a customer if a payment fails or revoke a customer’s access when a subscription is canceled.

The following table describes the most common events related to subscriptions and, where applicable, suggests actions for handling the events.

EventDescription`customer.created`Sent when a[Customer](/api/customers/object)is successfully created.`customer.subscription.created`Sent when the subscription is created. The subscription`status`might be`incomplete`if customer authentication is required to complete the payment or if you set`payment_behavior`to`default_incomplete`. View[subscription payment behavior](/billing/subscriptions/overview#subscription-payment-behavior)to learn more.`customer.subscription.deleted`Sent when a customer’s subscription ends.`customer.subscription.paused`Sent when a subscription’s`status`changes to`paused`.For example, this is sent when a subscription is[configured](/api/subscriptions/create#create_subscription-trial_settings-end_behavior-missing_payment_method)to pause when a[free trial ends without a payment method](/billing/subscriptions/trials#create-free-trials-without-payment).Invoicing won’t occur until the subscription is[resumed](/api/subscriptions/resume).We don’t send this event if[payment collection is paused](/billing/subscriptions/pause-payment)because invoices continue to be created during that time period.`customer.subscription.resumed`Sent when a subscription previously in a`paused`status is resumed. This doesn’t apply when[payment collection is unpaused](/billing/subscriptions/pause-payment#unpausing).`customer.subscription.trial_will_end`Sent three days before the[trial period ends](/billing/subscriptions/trials). If the trial is less than three days, this event is triggered.`customer.subscription.updated`Sent when a subscription starts or[changes](/billing/subscriptions/change). For example, renewing a subscription, adding a coupon, applying a discount, adding an invoice item, and changing plans all trigger this event.`entitlements.active_entitlement_summary.updated`Sent when a customer’s active entitlements are updated. When you receive this event, you can provision or de-provision access to your product’s features. Read more about[integrating with entitlements](/billing/entitlements).`invoice.created`Sent when an invoice is created for a new or renewing subscription. If Stripe fails to receive a successful response to`invoice.created`, then finalizing all invoices with[automatic collection](/invoicing/integration/automatic-advancement-collection)is delayed for up to 72 hours. Read more about[finalizing invoices](/invoicing/integration/workflow-transitions#finalized).- Respond to the notification by sending a request to the[Finalize an invoice](/api/invoices/finalize)API.

`invoice.finalized`Sent when an invoice is successfully finalized and ready to be paid.- You can send the invoice to the customer. View[invoice finalization](/invoicing/integration/workflow-transitions#finalized)to learn more.
- Depending on your settings, we automatically charge the default payment method or attempt collection. View[emails after finalization](/invoicing/integration/workflow-transitions#emails)to learn more.

`invoice.finalization_failed`The invoice couldn’t be finalized. Learn how to[handle invoice finalization failures](/tax/customer-locations#finalizing-invoices-with-finalization-failures)by reading the guide. Learn more about[invoice finalization](/invoicing/integration/workflow-transitions#finalized)in the invoices overview guide.- Inspect the Invoice’s[last_finalization_error](/api/invoices/object#invoice_object-last_finalization_error)to determine the cause of the error.
- If you’re using Stripe Tax, check the Invoice object’s[automatic_tax](/api/invoices/object#invoice_object-last_finalization_error)field.
- If`automatic_tax[status]=requires_location_inputs`, the invoice can’t be finalized and payments can’t be collected. Notify your customer and collect the required[customer location](/tax/customer-locations).
- If`automatic_tax[status]=failed`, retry the request later.

`invoice.paid`Sent when the invoice is successfully paid. You can provision access to your product when you receive this event and the subscription`status`is`active`.`invoice.payment_action_required`Sent when the invoice requires customer authentication. Learn how to handle the subscription when the invoice[requires action](/billing/subscriptions/overview#requires-action).invoice.payment_failed

A payment for an invoice failed. The PaymentIntent status changes to requires_action. The status of the subscription continues to be incomplete only for the subscription’s first invoice. If a payment fails, there are several possible actions to take:

- Notify the customer. Read about how you can configure[subscription settings](/billing/subscriptions/overview#settings)to enable[Smart Retries](/billing/revenue-recovery/smart-retries)and other revenue recovery features.
- If you’re using PaymentIntents, collect new payment information and[confirm the PaymentIntent](/api/payment_intents/confirm).
- Update the[default payment method](/api/subscriptions/object#subscription_object-default_payment_method)on the subscription.

`invoice.upcoming`Sent a few days prior to the renewal of the subscription. The number of days is based on the number set forUpcoming renewal eventsin the[Dashboard](https://dashboard.stripe.com/settings/billing/automatic). For existing subscriptions, changing the number of days takes effect on the next billing period. You can still add[extra invoice items](/billing/invoices/subscription#adding-upcoming-invoice-items), if needed.`invoice.updated`Sent when a payment succeeds or fails. If payment is successful the`paid`attribute is set to`true`and the`status`is`paid`. If payment fails,`paid`is set to`false`and the`status`remains`open`. Payment failures also trigger  a`invoice.payment_failed`event.`payment_intent.created`Sent when a[PaymentIntent](/api/payment_intents)is created.`payment_intent.succeeded`Sent when a PaymentIntent has successfully completed payment.`subscription_schedule.aborted`Sent when a subscription schedule is canceled because payment delinquency terminated the related subscription.`subscription_schedule.canceled`Sent when a subscription schedule is canceled, which also cancels any active associated subscription.`subscription_schedule.completed`Sent when all[phases](/billing/subscriptions/subscription-schedules#subscription-schedule-phases)of a subscription schedule complete.`subscription_schedule.created`Sent when a new subscription schedule is created.`subscription_schedule.expiring`Sent 7 days before a subscription schedule is set to expire.`subscription_schedule.released`Sent when a subscription schedule is[released](/api/subscription_schedules/release), or stopped and disassociated from the subscription, which remains.`subscription_schedule.updated`Sent when a subscription schedule is updated.[Invoice lifecycle](#invoice-lifecycle)The invoices overview provides a more detailed explanation of how invoices work, but for invoices generated by subscriptions, the basic lifecycle looks like this:

1. The subscription generates a new invoice in`draft`state.
2. About[one hour](/billing/invoices/subscription#adding-draft-invoice-items)after creation, the invoice finalizes (changes are no longer permitted).
3. The status is set to`open`and Stripe automatically attempts to pay it using the default payment method.
4. If payment succeeds, the status updates to`paid`.
5. If payment fails, the invoice remains`open`and the subscription becomes`past_due`.

In this flow, Stripe doesn’t notify your customer about the invoice. Payment is automatically attempted on the invoice shortly after it’s generated. However, if customer emails are enabled, we send an email receipt.

[Subscription settings and recovery](#settings)Your subscription settings determine how Stripe responds when payments fail or when subscriptions become past due.

### Smart Retries

After creating a subscription, payment failure is the most important event that can happen. Failures occur for many reasons:

- Lack of a payment method on the customer.
- The payment method is expired.
- The payment is declined.

You can configure Stripe to retry failed payments. Smart Retries use Stripe’s machine learning to pick the optimal time to retry, over a configurable time period up to one month after the initial payment fails.

You can also modify the retry schedule with custom rules. You can configure up to three retries, each with a specific number of days after the previous attempt.

If recovery fails, the subscription transitions according to your settings. The options are:

SettingDescriptionCancel the subscriptionThe subscription changes to a`canceled`state after the maximum number of days defined in the retry schedule.Mark the subscription as unpaidThe subscription changes to an`unpaid`state after the maximum number of days defined in the retry schedule. Invoices continue to be generated and stay in a draft state.Leave the subscription past-dueThe subscription remains in a`past_due`state after the maximum number of days defined in the retry schedule. Invoices continue to be generated and charge customer based on retry settings.After the final payment attempt, we make no further payment attempts until you add a new payment method to the customer. Changing your subscription settings only affects future retries. After a payment attempt on an invoice, its next_payment_attempt value is set using the current subscription settings in your Dashboard.

Emails![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Stripe can optionally send different emails to customers, using the email addresses associated with the Customer object:

- An upcoming renewal reminder at the same time that we send the`invoice.upcoming`event.
- A failed payment notification prompting customers to update their payment information. Learn[how to turn on failed payment notifications](/billing/revenue-recovery/customer-emails#failed-payment-notifications).
- An expiring card notification when a customer’s`default_source`card is due to expire.

You can customize your URL to update a card and your logo and colors used in the email, as outlined in the receipts documentation.

### Manual payment

You can configure the due date for invoices that use the send_invoice collection method to receive manual payments. You can also configure up to three reminders, starting at 10 days before the due date and ending at 60 days after.

You can also take additional action on the subscription 30, 60, or 90 days after an invoice becomes past due. The options are:

SettingDescriptionCancel the subscriptionThe subscription changes to a`canceled`state after the maximum number of days defined in the retry schedule.Mark the subscription as unpaidThe subscription changes to an`unpaid`state after the maximum number of days defined in the retry schedule. Invoices continue to generate and either stay in a`draft`state or transition to a state specified in your invoice settings.Leave the subscription past-dueThe subscription remains in a`past_due`state after the maximum number of days defined in the retry schedule. Invoices continue to be generated into an`open`state.Learn more about subscription statuses.

### Payments requiring 3D Secure

For payments that require 3D Secure, Stripe can send a confirmation email to your customer at the same time that we send the invoice.payment_action_required. You can also configure sending up to three reminders, from 1 to 7 days after the payment was initiated.

If a payment is still incomplete after the set number of days, you can choose to:

SettingDescriptionCancel the subscriptionThe subscription changes to a`canceled`state after the maximum number of days defined in the retry schedule.Mark the subscription as unpaidThe subscription changes to an`unpaid`state after the maximum number of days defined in the retry schedule. Invoices continue to be generated and stay in a draft state.Leave the subscription past-dueThe subscription remains in a`past_due`state after the maximum number of days defined in the retry schedule. Invoices continue to be generated and charge customer based on retry settings.### Trials

Card networks require you to inform your customers about their trials. Stripe can manage this communication for you. In the Stripe Dashboard, you can configure the cancellation URL that’s included on both the reminder emails and on the receipt for the first invoice after a trial ends. You can also configure the statement descriptor for the first charge after a trial. Learn more about these requirements and settings on the trials page.

[Changing subscriptions](#changing-subscriptions)Stripe supports changing existing subscriptions without having to cancel and recreate them. Some of the most significant changes you might make are upgrading or downgrading the subscription price, or canceling or pausing payment collection for an active subscription. Learn more about how to change existing subscriptions.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Subscription objects](#subscription-objects)[Integration example](#integration-example)[How payments work with subscriptions](#how-payments-work-subscriptions)[The subscription lifecycle](#subscription-lifecycle)[Subscription events](#subscription-events)[Invoice lifecycle](#invoice-lifecycle)[Subscription settings and recovery](#settings)[Changing subscriptions](#changing-subscriptions)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`