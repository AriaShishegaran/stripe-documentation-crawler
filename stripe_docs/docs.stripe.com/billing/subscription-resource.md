# Subscriptions

Read the integration guide to learn how to build a complete subscription integration.

[build a complete subscription integration](/billing/subscriptions/build-subscriptions)

For a more immersive experience, follow the quickstart to build a simple, working subscriptions integration.

[quickstart](/billing/quickstart)

Subscriptions are a core resource in Stripe. They represent what your customer is paying for and how much and how often you’re charging them for the product. You build and manage subscriptions by using other core Stripe resources, like Customers, Products, Prices, and Invoices, and PaymentIntents.

[Subscriptions](/billing/subscriptions/creating)

[Customers](/api/customers)

[Products](/api/products)

[Prices](/api/prices)

[Invoices](/api/invoices)

[PaymentIntents](/payments/payment-intents)

Subscriptions abstractions

You can create and update subscriptions from the Dashboard or the API. Use the API if you have a large number of subscriptions to manage, or if you want to manage them programmatically.

You can subscribe customers:

- Manually through the Dashboard

[Manually through the Dashboard](#dashboard)

- With Payment Links

[Payment Links](/payment-links)

- Programmatically through the API

[Programmatically through the API](#api)

- Through your website by embedding pricing tables and linking to a Checkout session

[embedding pricing tables](/payments/checkout/pricing-table)

[Checkout session](/checkout/quickstart)

Manage how you notify customers about different subscription events in the subscriptions email settings page of the Dashboard.

[subscriptions email settings page](https://dashboard.stripe.com/settings/billing/automatic)

## Create a subscription

To create a subscription:

- In the Stripe Dashboard, go to the subscriptions page.

In the Stripe Dashboard, go to the subscriptions page.

[subscriptions](https://dashboard.stripe.com/test/subscriptions)

- Click +Create subscription.

Click +Create subscription.

- Find or add a customer.

Find or add a customer.

- Enter the pricing and product information. You can add multiple products.

Enter the pricing and product information. You can add multiple products.

- Set the start and end date of the subscription.

Set the start and end date of the subscription.

- Set the starting date for the billing cycle. This defines when the next invoice is generated. Depending on your settings, the saved payment method on file might also be charged automatically on the billing cycle date. Learn more about the billing cycle date.

Set the starting date for the billing cycle. This defines when the next invoice is generated. Depending on your settings, the saved payment method on file might also be charged automatically on the billing cycle date. Learn more about the billing cycle date.

[billing cycle date](/billing/subscriptions/billing-cycle)

- (Optional) Add the default tax behavior, a coupon, a free trial, or metadata.

(Optional) Add the default tax behavior, a coupon, a free trial, or metadata.

- (Optional) Maximize revenue for your business by enabling revenue recovery features in the Dashboard. You can automatically retry failed payments, build custom automations, configure customer emails, and more.

(Optional) Maximize revenue for your business by enabling revenue recovery features in the Dashboard. You can automatically retry failed payments, build custom automations, configure customer emails, and more.

[revenue recovery](/billing/revenue-recovery)

Here are two other ways to create subscriptions:

- Click Create >  Subscription in the upper right hand corner of the Dashboard.

- Type c s anywhere in the Dashboard to open the subscription editor.

## Edit a subscription

To edit a subscription:

- Go to the subscriptions page.

Go to the subscriptions page.

[subscriptions](https://dashboard.stripe.com/test/subscriptions)

- Find the subscription you want to modify, click the overflow menu (), then click Update subscription. You can also click the  next to the subscription name. From this menu, you can also:Cancel the subscription. In the modal that opens, select the date to cancel the subscription—immediately, at the end of the current period, or on a custom date. You can also select the option to refund the last payment for this subscription and create a credit note for your records.Pause payment collection. In the modal that opens, select the duration of the pause—indefinite or ending on a custom date—and how invoices should behave during the pause.Share payment update link. In the modal that opens, you can share a link with the customer to update their payment details. For more information, see Share payment update link.

Find the subscription you want to modify, click the overflow menu (), then click Update subscription. You can also click the  next to the subscription name. From this menu, you can also:

- Cancel the subscription. In the modal that opens, select the date to cancel the subscription—immediately, at the end of the current period, or on a custom date. You can also select the option to refund the last payment for this subscription and create a credit note for your records.

Cancel the subscription. In the modal that opens, select the date to cancel the subscription—immediately, at the end of the current period, or on a custom date. You can also select the option to refund the last payment for this subscription and create a credit note for your records.

[credit note](/invoicing/dashboard/credit-notes)

- Pause payment collection. In the modal that opens, select the duration of the pause—indefinite or ending on a custom date—and how invoices should behave during the pause.

Pause payment collection. In the modal that opens, select the duration of the pause—indefinite or ending on a custom date—and how invoices should behave during the pause.

- Share payment update link. In the modal that opens, you can share a link with the customer to update their payment details. For more information, see Share payment update link.

Share payment update link. In the modal that opens, you can share a link with the customer to update their payment details. For more information, see Share payment update link.

[Share payment update link](/billing/subscriptions/update-payment-method)

- Make your changes to the subscription.

Make your changes to the subscription.

- Click Update subscription.

Click Update subscription.

## Delete a subscription

You can’t delete a subscription. But you can cancel it or pause payment collection. See editing a subscription for those details.

[editing a subscription](#edit-susbscription)

## See also

- Change subscriptions

[Change subscriptions](/billing/subscriptions/change)

- Upgrade and downgrade subscriptions

[Upgrade and downgrade subscriptions](/billing/subscriptions/upgrade-downgrade)

- Cancel subscriptions

[Cancel subscriptions](/billing/subscriptions/cancel)
