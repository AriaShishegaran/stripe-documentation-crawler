# How subscriptions work

With Subscriptions, customers make recurring payments for access to a product. Subscriptions require you to retain more information about your customers than one-time purchases because you need to charge them in the future.

[Subscription objects](#subscription-objects)

## Subscription objects

Use the following core API resources to build and manage subscriptions:

[Product](/api/products)

[Price](/api/prices)

[Customer](/api/customers)

[PaymentMethod](/api/payment_methods)

[Subscription](/api/subscriptions)

[Invoice](/api/invoices)

[PaymentIntent](/api/payment_intents)

[Integration example](#integration-example)

## Integration example

This section describes our sample integration on GitHub, which illustrates how to build a subscriptions integration. If you’re ready to build your own integration, see the Billing quickstart or integration guide.

[sample integration on GitHub](https://github.com/stripe-samples/subscription-use-cases/tree/master/fixed-price-subscriptions)

[Billing quickstart](/billing/quickstart)

[integration guide](/billing/subscriptions/build-subscriptions)

On your frontend, the landing page collects the email address first. Your application might have other customer-specific information you want to collect like a username or address. Clicking the signup button sends the information collected on the landing page to your backend. This process creates a customer and displays the pricing page on your frontend.

The pricing page displays your subscription options based on the products and prices you create when you first set up your integration, meaning you don’t need to create new ones every time customers sign up. Your pricing page displays the prices you created, and your customers choose the option they want. The example on GitHub displays a payment form when a customer selects an option.

[example on GitHub](https://github.com/stripe-samples/subscription-use-cases/tree/master/fixed-price-subscriptions)

Learn more about products and prices.

[products and prices](/products-prices/how-products-and-prices-work)

The payment form collects a name and card information. Stripe hosts this form if you use Checkout. It’s one of the key features that allows you to collect payments and remain PCI compliant. Clicking Subscribe:

- Creates a new subscription with your customer and price IDs.

- Generates an invoice for your initial subscription cycle.

- Collects payment details and pays your invoice.

- Sets the payment method as the default payment method for the subscription-a requirement for subsequent payments.

You should confirm payment before provisioning access for your customer.

[confirm](/api/payment_intents/confirm)

[provisioning access](#provisioning)

To implement this:

- No code—If you don’t want to write any code, learn how to create a Payment Link and share it with your customers.

[create a Payment Link](/payment-links)

- Low code—If you’re using Checkout, learn how to add a button to your website that creates a Checkout Session.

[add a button to your website that creates a Checkout Session](/billing/subscriptions/build-subscriptions?ui=stripe-hosted#create-session)

- Custom code—If you’re using Elements, learn how to collect payment details and activate the subscription with the Payment Element or Card Element.

[collect payment details and activate the subscription](/billing/subscriptions/build-subscriptions?ui=elements#collect-payment)

Use Entitlements to determine when you can grant or revoke product feature access to your customers.

[Entitlements](/billing/entitlements)

Alternatively, after a successful payment, you can safely provision the product for the customer. This generally means:

- Verifying the status of the subscription is active.

- Granting the customer access to the products and features they subscribed to.

Learn how to use webhooks to:

[webhooks](/webhooks)

- Track active subscriptions

[Track active subscriptions](/billing/subscriptions/webhooks#active-subscriptions)

- Handle payment failures

[Handle payment failures](/billing/subscriptions/webhooks#payment-failures)

- Check event objects

[Check event objects](/webhooks#events-overview)

[privacy policy](https://stripe.com/privacy)

[How payments work with subscriptions](#how-payments-work-subscriptions)

## How payments work with subscriptions

To simplify the handling of failed payments and to create subscriptions before attempting payment:

- Pass payment_behavior=default_incomplete when creating a subscription. If your subscription requires payment, it’s created with an incomplete status, otherwise your subscription immediately becomes active.

[payment_behavior=default_incomplete](/api/subscriptions/create#create_subscription-payment_behavior)

- Activate an incomplete subscription by paying the first invoice.

- Pass the payment intent identifier from the invoice to your user interface to collect payment information and confirm the payment intent. You can use Elements, the Android SDK, or the iOS SDK.

[Elements](/js/elements_object)

[Android SDK](https://stripe.dev/stripe-android/)

[iOS SDK](https://stripe.dev/stripe-ios/)

The payment process differs across payment methods and geographical locations. Payments can also fail initially (for example, a customer might enter the wrong card number or have insufficient funds), so various payment outcomes are possible.

A PaymentIntent tracks the lifecycle of every payment. Whenever a payment is due for a subscription, Stripe generates an invoice and a PaymentIntent. The PaymentIntent ID attaches to the invoice and you can access it from the Invoice and Subscription objects. The state of the PaymentIntent affects the state of the invoice and the subscription. Here’s how the different outcomes of a payment map to the different statuses:

[PaymentIntent](/payments/payment-intents)

The following sections explain these statuses and the actions to take for each.

When your payment succeeds, the status of the PaymentIntent is succeeded, and the subscription becomes active. For payment methods with longer processing periods, subscriptions are immediately activated. In these cases, the status of the PaymentIntent may be processing for an active subscription until the payment succeeds.

[payment methods](/payments/payment-methods/integration-options)

With your subscription now activated, provision access to your product. Read the guide to learn more about the subscription lifecycle and best practices for provisioning.

[the subscription lifecycle](/billing/subscriptions/overview#subscription-lifecycle)

If payment fails because of a card error, such as a decline, the status of the PaymentIntent is requires_payment_method and the subscription is incomplete.

[card error](/api/errors#errors-card_error)

[decline](/declines#issuer-declines)

To resolve these scenarios:

- Notify the customer.

- Collect new payment information and confirm the payment intent.

[confirm the payment intent](/api/payment_intents/confirm)

- Update the default payment method on the subscription.

[default payment method](/api/subscriptions/object#subscription_object-default_payment_method)

Learn how to handle payment failures for subscriptions.

[handle payment failures for subscriptions](/billing/subscriptions/webhooks#payment-failures)

Some payment methods require customer authentication with 3D Secure (3DS) to complete the payment process. If you use the Payment Intents API, the value of latest_invoice.payment_intent.status is requires_action when a customer needs to authenticate a payment. 3DS completes the authentication process. Whether a payment method requires authentication depends on your Radar rules and the issuing bank for the card.

[3D Secure](/payments/3d-secure)

[Payment Intents API](/api/payment_intents)

[Radar rules](/payments/3d-secure/authentication-flow#three-ds-radar)

Regulations in Europe often require 3D Secure. See Strong Customer Authentication to determine whether handling this status is important for your business. If you have an existing billing integration and want to add support for this flow, also see the Billing SCA Migration guide.

[Strong Customer Authentication](/strong-customer-authentication)

[Billing SCA Migration guide](/billing/migration/strong-customer-authentication)

To handle these scenarios:

- Monitor for the invoice.payment_action_required event notification with webhooks. This indicates that authentication is required.

[webhooks](/billing/subscriptions/webhooks)

- Notify your customer that they must authenticate.

- Retrieve the client secret for the payment intent and pass it in a call to stripe.ConfirmCardPayment. This displays an authentication modal to your customers, attempts payment, then closes the modal and returns context to your application.

[stripe.ConfirmCardPayment](/js/payment_intents/confirm_card_payment)

- Monitor the invoice.paid event on your webhook endpoint to verify that the payment succeeded. Users can leave your application before confirmCardPayment() finishes. Verifying whether the payment succeeded allows you to correctly provision your product.

Stripe handles recurring charges for you automatically. This includes:

- Automatically invoicing customers and attempting payments when new billing cycles start.

[Automatically invoicing](/billing/invoices/subscription#subscription-renewal)

- When payments fail, Stripe retries them using the Smart Retries feature. This automatically re-attempts payment when cards are declined according to your Dashboard settings.

[Smart Retries](/invoicing/automatic-collection#smart-retries)

You can send a dunning email to customers for overdue payments to increase recovery chances. For payments that require 3D Secure, you can configure your billing settings to send a hosted link to customers so they can complete the flow.

[dunning email](/invoicing/integration/send-email)

[configure your billing settings](https://dashboard.stripe.com/account/billing/automatic)

[hosted link](/invoicing/hosted-invoice-page)

If you don’t want to use Stripe’s tooling to manage failures, you can build your own. If a payment fails or if it requires customer authentication, the subscription’s status is set to past_due and the PaymentIntent status is either requires_payment_method or requires_action.

To manage these scenarios, set up a webhook and listen to the customer.subscription.updated event so that you’re notified when subscriptions enter a past_due state:

[webhook](/webhooks)

[customer.subscription.updated](/api/events/types#event_types-customer.subscription.updated)

For these subscriptions, you need to get your customers back into your application to collect a different payment method so they can complete the payment. You can use an email or a mobile push notification. Stripe provides built-in reminder emails to handle this case, which you can configure in your billing settings.

[billing settings](https://dashboard.stripe.com/account/billing/automatic)

When your customer is back in your application, reuse either your payment failure flow or customer action flow depending on the status of the associated PaymentIntent. After the payment succeeds, the status of the subscription is active and the invoice is paid.

[payment failure flow](/billing/subscriptions/overview#requires-payment-method)

[customer action flow](/billing/subscriptions/overview#requires-action)

Subscriptions that include free trials, usage-based billing, invoices with coupons, or applied customer credit balances often result in non-payment invoices. This means you don’t immediately charge your customer when you create the subscription.

[free trials](/billing/subscriptions/trials)

[usage-based billing](/products-prices/pricing-models#usage-based-pricing)

Even though you don’t charge customers for the first invoice, authenticating and authorizing their card is often beneficial as it can increase the chance that the first non-zero payment completes successfully. Payments made this way are known as off-session payments. To manage these scenarios, Stripe created SetupIntents.

You can use SetupIntents to:

- Collect payment information.

- Authenticate your customer’s card to claim exemptions later.

[exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication)

- Authorize your customer’s card without charging it.

Authenticating payments allows your customer to grant permissions to charge their card. Strong Customer Authentication requires this, and 3DS is a common way to complete it. Collecting payment method information and authorizing it ensures that you can successfully charge the payment method.

[Strong Customer Authentication](/strong-customer-authentication)

[3DS](/payments/3d-secure)

In off-session scenarios, SetupIntents enable you to charge customers for their first non-zero payment without having to bring them back to your website or app for authentication. This reduces the friction on your customers.

The pending_setup_intent field on a subscription doesn’t cancel automatically when the subscription ends. Listen for customer.subscription.deleted webhooks and manually cancel a subscription SetupIntent if needed.

[cancel a subscription SetupIntent](/api/setup_intents/cancel)

Stripe automatically creates SetupIntents for subscriptions that don’t require an initial payment. The authentication and authorization process also completes at this point, if required. If both succeed or aren’t required, no action is necessary, and the subscription.pending_setup_intent field is null. If either step fails, Stripe recommends using the SetupIntent on your frontend to resolve the issue while your customer is on-session. The next two sections explain in detail how to manage scenarios where authentication or authorization fail.

Authentication failures occur when Stripe is unable to authenticate your customer with their card issuer. When this happens, the status of the SetupIntent is set to requires_action.

To resolve these scenarios, call confirmCardSetup on your frontend so that your customer can complete the authentication flow manually. The code example below expands the pending_setup_intent to complete the flow.

[confirmCardSetup](/js#stripe-confirm-card-setup)

[expands](/api/expanding_objects)

After completing this flow, authorization executes if it’s required. If authorization succeeds, or if it’s not required, pending_setup_intent is updated to null upon completion.

Payment authorization failures occur when Stripe can’t verify that a card can be charged. When this happens, the status of the SetupIntent is set to requires_payment_method. This generally means that subsequent charges with that card fail.

To resolve these scenarios, collect a new payment method, then update the default payment method for your customer or the subscription. The code example below expands the pending_setup_intent to complete the flow.

[collect a new payment method](/billing/subscriptions/overview#requires-payment-method)

[expands](/api/expanding_objects)

[The subscription lifecycle](#subscription-lifecycle)

## The subscription lifecycle

This is what the recommended subscription flow looks like:

If you set payment_behavior to default_incomplete, the subscription status is incomplete. Learn more about why we recommend using this type of payment behavior for subscriptions.

[payment behavior](#subscription-payment-behavior)

- You create the subscription. The status of the subscription is incomplete (if you follow the recommended flow—if you create a subscription without specifying the payment_behavior, the default status is active).

- An invoice is created for the subscription. The status of the invoice is open.

- The customer pays the first invoice.

- When the payment succeeds:The subscription status moves to activeThe invoice status is set to paidStripe sends an invoice.paid event webhook event.

- The subscription status moves to active

- The invoice status is set to paid

- Stripe sends an invoice.paid event webhook event.

- You provision access to your product. You can confirm whether the invoice has been paid by:Setting up a webhook endpoint and listening for the invoice.paid event.Manually checking the subscription object and looking for subscription.status=active. The status becomes active when the invoice has been paid either through an automatic charge or having the customer pay manually.

- Setting up a webhook endpoint and listening for the invoice.paid event.

- Manually checking the subscription object and looking for subscription.status=active. The status becomes active when the invoice has been paid either through an automatic charge or having the customer pay manually.

The status can also become trialing if you offer trials that don’t require payments. When the trial is over, the subscription moves to active and the subscribed customer starts to be charged.

To simplify handling failed payments, create subscriptions with payment_behavior set to default_incomplete. This creates subscriptions with status incomplete, which allows you to collect and confirm payment information in a single user interface. When using allow_incomplete or error_if_incomplete, Stripe immediately attempts to pay the invoice. If the payment fails, the subscription’s status changes to incomplete or the creation fails.

[default_incomplete](/api/subscriptions/create#create_subscription-payment_behavior)

When your customer successfully pays the invoice, the subscription updates to active and the invoice to paid. At this point, you can provision access to your product.

Customers have about 23 hours to make a successful payment. The subscription remains in status incomplete and the invoice is open during this time. If your customer pays the invoice, the subscription updates to active and the invoice to paid. If they don’t make a payment, the subscription updates to incomplete_expired and the invoice becomes void.

This window exists because your customer usually makes the first payment for a subscription while on-session. If the customer returns to your application after 23 hours, create a new subscription for them.

The subscription’s status remains active as long as automatic payments succeed. If automatic payment fails, the subscription updates to past_due and Stripe attempts to recover payment based on your retry rules. If payment recovery fails, you can set the subscription status to canceled, unpaid, or leave it past_due.

[retry rules](https://dashboard.stripe.com/account/billing/automatic)

For unpaid subscriptions, the latest invoice remains open but payments aren’t attempted. The subscription continues to generate invoices each billing cycle and remains in draft state. To reactivate the subscription, you need to:

- Collect new payment information.

- Turn automatic collection back on by setting auto advance to true on draft invoices.

[auto advance](/api/invoices/update#update_invoice-auto_advance)

- Finalize, then pay the open invoices. Pay the most recent invoice before its due date to update the status of the subscription to active.

[Finalize](/api/invoices/finalize)

Setting past_due subscriptions to unpaid is the default behavior because it gives you the most options for reactivating subscriptions.

Canceling subscriptions disables creating new invoices for the subscription and stops automatic collection of all invoices from the subscription by setting auto_advance to false. It also deletes the subscription. If your customer wants to resubscribe, you need to collect new payment information from them and create a new subscription.

If the subscription is incomplete and you void the first invoice that’s generated, the subscription updates to incomplete_expired. If you void the most recent invoice for an active subscription and it’s not the first one, the following logic is applied to each invoice (from most recent to oldest) until it meets one of these conditions:

- If the invoice is in a paid or uncollectible state, the subscription state is set to active.

- If the collection_method is set to charge_automatically on the invoice and Stripe stopped dunning on the invoice because of retry limits, the subscription state is set to canceled , unpaid, or past_due based on your automatic collection settings.

[collection_method](/api/invoices/object#invoice_object-collection_method)

[automatic collection settings](https://dashboard.stripe.com/settings/billing/automatic)

- If the collection_method is set to send_invoice, and the invoice is past its due date, the state of the subscription is set to past_due.

[collection_method](/api/invoices/object#invoice_object-collection_method)

- If the invoice is in none of these states, the same steps execute on the next most recent invoice.

If no invoices match any of the above criteria, the subscription state is set to active.

[requires action](#requires-action)

[subscription settings](/billing/subscriptions/overview#settings)

[Smart Retries](/billing/revenue-recovery/smart-retries)

[trial_settings.end_behavior.missing_payment_method](/billing/subscriptions/trials#create-free-trials-without-payment)

[resume the subscription](/billing/subscriptions/trials#resume-a-paused-subscription)

[Subscription events](#subscription-events)

## Subscription events

Events are triggered every time a subscription is created or changed. We send some events immediately when a subscription is created, while others recur on regular billing intervals. We recommend listening for events with a webhook endpoint.

[Events](/api#event_types)

[webhook endpoint](/billing/subscriptions/webhooks)

Make sure that your integration properly handles the events. For example, you might want to email a customer if a payment fails or revoke a customer’s access when a subscription is canceled.

The following table describes the most common events related to subscriptions and, where applicable, suggests actions for handling the events.

[Customer](/api/customers/object)

[subscription payment behavior](/billing/subscriptions/overview#subscription-payment-behavior)

[configured](/api/subscriptions/create#create_subscription-trial_settings-end_behavior-missing_payment_method)

[free trial ends without a payment method](/billing/subscriptions/trials#create-free-trials-without-payment)

[resumed](/api/subscriptions/resume)

[payment collection is paused](/billing/subscriptions/pause-payment)

[payment collection is unpaused](/billing/subscriptions/pause-payment#unpausing)

[trial period ends](/billing/subscriptions/trials)

[changes](/billing/subscriptions/change)

[integrating with entitlements](/billing/entitlements)

[automatic collection](/invoicing/integration/automatic-advancement-collection)

[finalizing invoices](/invoicing/integration/workflow-transitions#finalized)

- Respond to the notification by sending a request to the Finalize an invoice API.

[Finalize an invoice](/api/invoices/finalize)

- You can send the invoice to the customer. View invoice finalization to learn more.

[invoice finalization](/invoicing/integration/workflow-transitions#finalized)

- Depending on your settings, we automatically charge the default payment method or attempt collection. View emails after finalization to learn more.

[emails after finalization](/invoicing/integration/workflow-transitions#emails)

[handle invoice finalization failures](/tax/customer-locations#finalizing-invoices-with-finalization-failures)

[invoice finalization](/invoicing/integration/workflow-transitions#finalized)

- Inspect the Invoice’s last_finalization_error to determine the cause of the error.

[last_finalization_error](/api/invoices/object#invoice_object-last_finalization_error)

- If you’re using Stripe Tax, check the Invoice object’s automatic_tax field.

[automatic_tax](/api/invoices/object#invoice_object-last_finalization_error)

- If automatic_tax[status]=requires_location_inputs, the invoice can’t be finalized and payments can’t be collected. Notify your customer and collect the required customer location.

[customer location](/tax/customer-locations)

- If automatic_tax[status]=failed, retry the request later.

[requires action](/billing/subscriptions/overview#requires-action)

invoice.payment_failed

A payment for an invoice failed. The PaymentIntent status changes to requires_action. The status of the subscription continues to be incomplete only for the subscription’s first invoice. If a payment fails, there are several possible actions to take:

- Notify the customer. Read about how you can configure subscription settings to enable Smart Retries and other revenue recovery features.

[subscription settings](/billing/subscriptions/overview#settings)

[Smart Retries](/billing/revenue-recovery/smart-retries)

- If you’re using PaymentIntents, collect new payment information and confirm the PaymentIntent.

[confirm the PaymentIntent](/api/payment_intents/confirm)

- Update the default payment method on the subscription.

[default payment method](/api/subscriptions/object#subscription_object-default_payment_method)

[Dashboard](https://dashboard.stripe.com/settings/billing/automatic)

[extra invoice items](/billing/invoices/subscription#adding-upcoming-invoice-items)

[PaymentIntent](/api/payment_intents)

[phases](/billing/subscriptions/subscription-schedules#subscription-schedule-phases)

[released](/api/subscription_schedules/release)

[Invoice lifecycle](#invoice-lifecycle)

## Invoice lifecycle

The invoices overview provides a more detailed explanation of how invoices work, but for invoices generated by subscriptions, the basic lifecycle looks like this:

[invoices overview](/invoicing/overview)

- The subscription generates a new invoice in draft state.

- About one hour after creation, the invoice finalizes (changes are no longer permitted).

[one hour](/billing/invoices/subscription#adding-draft-invoice-items)

- The status is set to open and Stripe automatically attempts to pay it using the default payment method.

- If payment succeeds, the status updates to paid.

- If payment fails, the invoice remains open and the subscription becomes past_due.

In this flow, Stripe doesn’t notify your customer about the invoice. Payment is automatically attempted on the invoice shortly after it’s generated. However, if customer emails are enabled, we send an email receipt.

[customer emails](https://dashboard.stripe.com/account/emails)

[Subscription settings and recovery](#settings)

## Subscription settings and recovery

Your subscription settings determine how Stripe responds when payments fail or when subscriptions become past due.

[subscription settings](https://dashboard.stripe.com/settings/billing/automatic)

After creating a subscription, payment failure is the most important event that can happen. Failures occur for many reasons:

- Lack of a payment method on the customer.

- The payment method is expired.

- The payment is declined.

You can configure Stripe to retry failed payments. Smart Retries use Stripe’s machine learning to pick the optimal time to retry, over a configurable time period up to one month after the initial payment fails.

[Smart Retries](https://dashboard.stripe.com/settings/billing/automatic)

You can also modify the retry schedule with custom rules. You can configure up to three retries, each with a specific number of days after the previous attempt.

If recovery fails, the subscription transitions according to your settings. The options are:

After the final payment attempt, we make no further payment attempts until you add a new payment method to the customer. Changing your subscription settings only affects future retries. After a payment attempt on an invoice, its next_payment_attempt value is set using the current subscription settings in your Dashboard.

[next_payment_attempt](/api#invoice_object-next_payment_attempt)

Stripe can optionally send different emails to customers, using the email addresses associated with the Customer object:

[Customer](/api#customers)

- An upcoming renewal reminder at the same time that we send the invoice.upcoming event.

- A failed payment notification prompting customers to update their payment information. Learn how to turn on failed payment notifications.

[how to turn on failed payment notifications](/billing/revenue-recovery/customer-emails#failed-payment-notifications)

- An expiring card notification when a customer’s default_source card is due to expire.

You can customize your URL to update a card and your logo and colors used in the email, as outlined in the receipts documentation.

[receipts](/receipts#customizing-receipts)

You can configure the due date for invoices that use the send_invoice collection method to receive manual payments. You can also configure up to three reminders, starting at 10 days before the due date and ending at 60 days after.

[collection method](/billing/collection-method#set-collection-method-invoice)

You can also take additional action on the subscription 30, 60, or 90 days after an invoice becomes past due. The options are:

Learn more about subscription statuses.

[subscription statuses](#subscription-statuses)

For payments that require 3D Secure, Stripe can send a confirmation email to your customer at the same time that we send the invoice.payment_action_required. You can also configure sending up to three reminders, from 1 to 7 days after the payment was initiated.

If a payment is still incomplete after the set number of days, you can choose to:

Card networks require you to inform your customers about their trials. Stripe can manage this communication for you. In the Stripe Dashboard, you can configure the cancellation URL that’s included on both the reminder emails and on the receipt for the first invoice after a trial ends. You can also configure the statement descriptor for the first charge after a trial. Learn more about these requirements and settings on the trials page.

[Stripe Dashboard](https://dashboard.stripe.com/settings/billing/automatic)

[trials](/billing/subscriptions/trials#compliance)

[Changing subscriptions](#changing-subscriptions)

## Changing subscriptions

Stripe supports changing existing subscriptions without having to cancel and recreate them. Some of the most significant changes you might make are upgrading or downgrading the subscription price, or canceling or pausing payment collection for an active subscription. Learn more about how to change existing subscriptions.

[upgrading or downgrading](/billing/subscriptions/upgrade-downgrade)

[canceling](/billing/subscriptions/cancel)

[pausing payment collection for](/billing/subscriptions/pause-payment)

[change existing subscriptions](/billing/subscriptions/change)
