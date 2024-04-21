# NetSuite invoice payment page

The Stripe Connector for NetSuite creates a payment page for each of your NetSuite invoices, allowing your customers to pay their invoices using a Stripe payment flow. Customers can pay with any of the payment methods that you enable. Every accepted payment includes automated payment processing, cash application, deposit automation, and fee calculation.

[payment methods](https://dashboard.stripe.com/test/settings/payment_methods)

## Save payment methods for future use

You can use the payment page to optionally save a customer’s payment method for future use. For example, a connector add-on, such as AutoPay, might use the saved payment method to charge a customer for future invoices. Stripe saves the customer’s payment method to a new or existing Customer object.

[AutoPay](http://autopay-docs.com)

[Customer](/api/customers)

You’re responsible for your compliance with all applicable laws, regulations, and network rules when saving a customer’s payment details. For example, if you want to save a customer’s payment method for future use, you need their agreement to be billed outside of the connector’s payment flow. Getting that agreement up front allows you to save the customer’s payment details, and potentially even charge the customer for future invoices.

If you plan to charge the customer while they’re offline, then at a minimum, make sure that your terms also cover the following:

- The customer’s agreement to your initiating a payment or a series of payments on their behalf for specified transactions.

- The anticipated timing and frequency of payments (for example, whether charges are for scheduled installment or subscription payments, or for unscheduled top-ups).

- How the payment amount is determined.

- Your cancellation policy, if you’re setting up the payment method for a subscription service.

Make sure you keep a record of your customer’s written agreement to these terms.

## Customize the payment page

You can customize the look and feel of the payment page to match the design of your site. Modify the payment page color and design on the Branding settings page in the Stripe Dashboard. Modify your name and statement descriptor on the Public details page.

[Branding settings](https://dashboard.stripe.com/settings/branding)

[Public details](https://dashboard.stripe.com/settings/public)

## Add the payment page to your communications

You can integrate the payment page into your customer communications in NetSuite. For example, you might choose to map the payment page’s unique link to a Pay Now button in your NetSuite email templates, invoice PDF templates, or manual outreach.

## Send email receipts for payments

You have two options for sending email receipts to your customers:

- Use Stripe to automatically send email receipts. The connector provides the invoice ID and NetSuite customer email. To use this option, enable Successful payments on the Customer emails settings page in the Stripe Dashboard. You can also customize your receipts.

Use Stripe to automatically send email receipts. The connector provides the invoice ID and NetSuite customer email. To use this option, enable Successful payments on the Customer emails settings page in the Stripe Dashboard. You can also customize your receipts.

[Customer emails settings](https://dashboard.stripe.com/settings/emails)

[customize your receipts](/receipts?payment-ui=payment-links#customizing-receipts)

- Use NetSuite to send email receipts for payments. You must disable email receipts in the Stripe Dashboard and then set up a workflow to send customized email receipts from NetSuite.

Use NetSuite to send email receipts for payments. You must disable email receipts in the Stripe Dashboard and then set up a workflow to send customized email receipts from NetSuite.

## Support multiple currencies and payment methods

Accept payments in the supported presentment currencies in your region. The payment page displays the currency that’s specified on the NetSuite invoice. Stripe then creates a payment based on that currency.

[supported presentment currencies](/currencies#presentment-currencies)

You can enable the payment methods you want to accept on the Payment methods page. Stripe supports many categories of payment methods based on your region and business need.

[Payment methods](https://dashboard.stripe.com/settings/payment_methods)

[payment methods](/payments/payment-methods/overview)

## Automate bank reconciliation

The payment page includes deposit automation, which automates the bank reconciliation process for all payments, refunds, and disputes from a Stripe payout to a NetSuite bank deposit.

[deposit automation](/connectors/netsuite/deposit-automation)

## See also

- Customer payment page

[Customer payment page](/connectors/netsuite/customer-payment-page)

- Deposit automation

[Deposit automation](/connectors/netsuite/deposit-automation)
