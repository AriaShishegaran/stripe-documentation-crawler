# Create subscriptions with Stripe Billing

To learn more about Connect, check out the overview. See the create a payments guide to learn more about creating recurring payments on a connected account with subscriptions.

[Connect](/connect)

[overview](/connect)

[create a payments](/connect/creating-a-payments-page#subscriptions)

We base subscription transactions on Stripe Billing pricing.

[subscription](/billing/subscriptions/creating)

[Stripe Billing pricing](https://stripe.com/billing/pricing)

Software as a Service (SaaS) and marketplace businesses use Stripe Connect to route payments between themselves, customers, and connected accounts. You can use Connect to route payments or payouts and use Stripe Billing to support your recurring revenue model.

[payouts](/payouts)

## Use cases

You can create subscriptions for connect accounts, which supports several approaches for collecting payments. You can create subscriptions for your connected account’s customers using direct or destination charges, for your end customers to directly transact with your platform, and to charge your connected accounts a fee for using your platform.

[subscriptions](/billing/subscriptions/overview)

The following use cases describe how to use Stripe Billing to create subscriptions from end customers to connected accounts, to bill platform end customers, and to bill connected accounts.

[Create subscriptions from the end customer to the connected account](#customer-connected-account)

[Prices](/api/prices)

[Create subscriptions to bill platform end customers](#customer-platform)

[Prices](/api/prices)

[Create subscriptions to bill connected accounts](#connected-account-platform)

[Prices](/api/prices)

Using subscriptions with Connect has these restrictions:

- Your platform can’t update or cancel a subscription that it didn’t create.

- Your platform can’t add an application_fee_amount to an invoice that it didn’t create, nor to an invoice that contains invoice items the platform didn’t create.

- Subscriptions aren’t automatically cancelled when you disconnect from the platform. You must cancel the subscription after disconnection. You can use webhooks to monitor connected account activity.

[webhooks to monitor connected account activity](/connect/webhooks)

[Create subscriptions from the end customer to the connected account](#customer-connected-account)

## Create subscriptions from the end customer to the connected account

If you’re building a platform, you can create subscriptions for your connected accounts’ customers, optionally taking a per-payment fee for your platform.

This example builds an online publishing platform that allows customers to subscribe to their favorite authors and pay them a monthly fee to receive premium blog posts from each author.

## Before you begin

Before you can create subscriptions for your customers or connected accounts, you must:

- Create a connected account for each person that receives money on your platform. In our online publishing example, a connected account represents an author.

[connected account](/connect/accounts)

- Create a pricing model. For this example, we create a flat-rate pricing model to charge customers a fee on a recurring basis, but per-seat and usage-based pricing are also supported.

[pricing model](/products-prices/pricing-models#flat-rate)

- Create a customer for each person that subscribes to a connected account. In our online publishing example, you create a customer for each reader that subscribes to an author.

[customer](/billing/customer#manage-customers)

You can use either direct charges or destination charges to split a customer’s payment between the connected account and your platform.

With direct charges, customers won’t be aware of your platform’s existence because the author’s name, rather than your platform’s name, is shown on the statement descriptor. In our online publishing example, readers interact with authors directly.

Direct charges are recommended for connected accounts with access to the full Stripe Dashboard, which includes Standard accounts.

If you want your platform to be responsible for Stripe fees, refunds, and chargebacks, use destination charges. In our online publishing example, customers subscribe to your publishing platform, not directly with specific authors.

Destination charges are recommended for connected accounts with access to the Express Dashboard or connected accounts without access to a Stripe-hosted dashboard, which includes Express and Custom accounts.

For more information about the different types of Connect charges, see Charge types.

[Charge types](/connect/charges#types)

To create a subscription with Charges associated to the connected account, make a create subscription call while authenticated as the connected account. Make sure to define the customer and the Price on the connected account.

[Charges](/api/charges/object)

[create subscription](/api#create_subscription)

[authenticated as the connected account](/connect/authentication#stripe-account-header)

[Price](/api/prices)

Expand latest_invoice.payment_intent to include the Payment Element, which is needed to confirm the payment. Learn more about Payment Elements.

[Payment Elements](/billing/subscriptions/build-subscriptions?ui=elements#add-the-payment-element-to-your-page)

For an end-to-end example of how to implement a subscription signup and payment flow in your application, see the subscriptions integration guide.

[subscriptions integration](/billing/subscriptions/build-subscriptions)

To create a subscription with Charges associated to the platform and automatically create transfers to a connected account, make a create subscription call while providing the connected account ID as the transfer_data[destination] value.

[Charges](/api/charges/object)

[create subscription](/api#create_subscription)

[value](/api/subscriptions/object#subscription_object-transfer_data)

Expand latest_invoice.payment_intent to include the Payment Element, which you need to confirm the payment. Learn more about Payment Elements.

[Payment Elements](/billing/subscriptions/build-subscriptions?ui=elements#add-the-payment-element-to-your-page)

You can optionally specify an application_fee_percent. Learn more about collecting fees.

[application_fee_percent](/api/subscriptions/object#subscription_object-application_fee_percent)

[collecting fees](#collect-fees)

To create a destination charge, define both the customer and the price on the platform account. You must have created a connected account on the platform. The customer must exist within the platform account. When using destination charges, the platform is the merchant of record.

[Create subscriptions to bill platform end customers](#customer-platform)

## Create subscriptions to bill platform end customers

You can use Stripe Billing to create subscriptions for your end customers to directly transact with your platform without involving your connected accounts.

This example builds a marketplace that allows customers to order on-demand delivery from restaurants. This marketplace offers customers a premium monthly subscription that waives their delivery fees. Customers who subscribe to the premium offering pay the marketplace directly and don’t subscribe to any particular delivery service or restaurant.

## Before you begin

Before you create subscriptions for your customers, you must:

You can also create a connected account for each user that receives money from your marketplace. In our on-demand restaurant delivery example, a connected account is a restaurant or a delivery service. However, this step isn’t required for customers to subscribe to your marketplace directly.

[connected account](/connect/accounts)

- Create a pricing model. For this example, we create a flat-rate pricing model to charge customers a fee on a recurring basis, but per-seat and usage-based pricing are also supported.

[pricing model](/products-prices/pricing-models#flat-rate)

- Create a customer record for every customer you want to bill.

[customer](/billing/customer#manage-customers)

To create a subscription where your platform receives the funds, without any money going to connected accounts, follow the Subscriptions guide to create a subscription with Stripe Billing.

[Subscriptions guide](/billing/subscription-resource#create-subscriptions)

If you want to manually transfer a portion of the funds that your platform receives to your connected accounts later, use separate charges and transfers to pay out funds to one or more connected accounts. In our on-demand restaurant delivery example, you can use separate charges and transfers to pay out an affiliate fee to a delivery driver or restaurant who refers a customer to subscribe to the premium delivery service.

[separate charges and transfers](/connect/separate-charges-and-transfers)

[Create subscriptions to bill connected accounts](#connected-account-platform)

## Create subscriptions to bill connected accounts

You can use Stripe Billing to create subscriptions to charge your connected accounts a fee for using your platform.

This example builds a gym management software platform that allows gym businesses to pay a monthly fee to use the software to manage scheduling and appointments for classes. The gym businesses pay the subscription fee, not the gym patrons.

The gym management software also facilitates one-time payments between the gym patron and gym business for each class that the gym patron enrolls in. The monthly subscription is between the connected account and the platform, which doesn’t involve the gym patron in the transaction.

In the diagram above, the gym business is the connected account and the gym patron is the end customer.

## Before you begin

Before you create subscriptions for your customers or connected accounts, you must:

- Create a connected account for each user that receives money on your platform. In this example, the connected account is the gym business.

[connected account](/connect/accounts)

- Create a pricing model. For this example, we create a flat-rate pricing model to charge customers a fee on a recurring basis, but per-seat and usage-based pricing are also supported.

[pricing model](/products-prices/pricing-models#flat-rate)

- Create a customer on the platform with the intended payment method for every connected account you want to bill. In the gym management software example, you create a customer for each gym business:

[customer](/billing/customer#manage-customers)

If your connected accounts use Stripe to process payments for their end customers, they might have already created a Customer object for each end customer.

[Customer](/api/customers)

To successfully create a subscription for the connected account to pay a recurring fee to the platform, you must create a separate Customer object to represent the connected account.

[Customer](/api/customers)

In the gym example, the gym business uses Stripe to process one-time payments for its gym patrons. They already created a Customer object for each gym patron, but you need to create a different Customer object to represent the gym business itself. Create only one Customer to represent each business entity and don’t create a Customer to represent each owner, manager, or operator of the business.

To create a subscription where your platform receives the funds from your connected accounts, follow the Subscriptions guide to create a subscription with Stripe Billing. The Customer object involved in the transaction represents the connected account, not the end customer. In our gym example, the CUSTOMER_ID represents the gym business, not the gym patron.

[Subscriptions guide](/billing/subscription-resource?dashboard-or-api=api)

[Enable your integration to receive event notifications](#subscription-connect-webhooks)

## Enable your integration to receive event notifications

Stripe creates event notifications when changes happen in your account, like when a recurring payment succeeds or when a payout fails. To receive these notifications and use them to automate your integration, set up a webhook endpoint. For example, you could provision access to your service when you receive the invoice.paid event.

[webhook](/webhooks)

Here are the event notifications that Connect integrations typically use.

[Standard accounts](/connect/standard-accounts)

[a bank account or debit card attached to a connected account is updated](/connect/payouts-bank-accounts)

[platform controls](/connect/platform-controls-for-stripe-dashboard-accounts)

[funds you’ve added from your bank account](/connect/add-and-pay-out-guide#add-funds)

[destination](/connect/collect-then-transfer-guide#fulfillment)

[direct](/connect/enable-payment-acceptance-guide)

[a payout fails](/connect/payouts-connected-accounts#webhooks)

[use the Persons API](/connect/handling-api-verification#verification-process)

[platform controls](/connect/platform-controls-for-stripe-dashboard-accounts)

Here are the event notifications that subscriptions integrations typically use.

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

- Create a webhook endpoint

[Create a webhook endpoint](/webhooks#webhook-endpoint-def)

- Listen to events with the Stripe CLI

[Listen to events with the Stripe CLI](/webhooks#local-listener)

- Connect webhooks

[Connect webhooks](/connect/webhooks)

- Subscription webhooks

[Subscription webhooks](/billing/subscriptions/webhooks)

[Test your integration](#test-integration)

## Test your integration

After you create your subscription, thoroughly test your integration before you expose it to customers or use it for any live activity. Learn more about testing Stripe Billing.

[testing Stripe Billing](/billing/testing)

## Additional options

After you create your subscription, you can specify an application_fee_percent, set up the customer portal, charge your customer using the on_behalf_of parameter, and monitor subscriptions with webhooks, in addition to other options.

[application_fee_percent](/api/subscriptions/object#subscription_object-application_fee_percent)

[customer portal](/billing/subscriptions/customer-portal)

## See also

- Creating invoices

[Creating invoices](/invoicing/connect)

- Creating charges

[Creating charges](/connect/charges)

- Share customers across accounts

[Share customers across accounts](/connect/cloning-customers-across-accounts)

- Multiple currencies

[Multiple currencies](/connect/currencies)
