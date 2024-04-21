# Test Stripe Invoicing

To learn more about testing an integration, see Stripe’s general-purpose testing page. For a Subscriptions integration, go to Testing Stripe Billing.

[testing page](/testing)

[Testing Stripe Billing](/billing/testing)

Use these common scenarios to test your invoicing integration before taking it live.

## Test webhook notifications

Stripe triggers event notifications when an invoice’s status changes. After you set up the Stripe CLI and link to your Stripe account, you can test webhooks by:

[invoice’s](/api/invoices)

[status changes](/invoicing/integration/workflow-transitions#status-transitions-endpoints)

- Triggering event notifications with the Stripe CLI.

Triggering event notifications with the Stripe CLI.

[Stripe CLI](/stripe-cli)

- Using the Dashboard to create invoices in test mode.

Using the Dashboard to create invoices in test mode.

[create invoices](https://dashboard.stripe.com/test/invoices/create)

[test mode](/test-mode)

You can add an endpoint and see its received events by going to Webhooks in the Dashboard.

[Webhooks](https://dashboard.stripe.com/test/webhooks)

By using the Stripe CLI to trigger events, you can see event notifications on your server as they come in. This means that you can check your webhook integration directly without complicating factors such as network tunnels or firewalls. When you use the Stripe CLI, the event your webhook receives contains fake data that doesn’t correlate to invoice information.

The most reliable way to test webhook notifications is to create test invoices for existing customers and handle the corresponding events.

## Test payment failures

To trigger payment failures for invoices, you can use the test credit card numbers in Declined payments. If you want to simulate a declined payment for a card that’s been successfully attached to a customer, use 4000 0000 0000 0341 as their default payment method.

[Declined payments](/testing#declined-payments)

Depending on your retry settings, you might have to wait a day or more to see the first retry attempt. To see what happens for a successful retry, you can use this waiting period to update the customer’s payment method to a working test card.

[retry settings](/invoicing/automatic-collection)

## Test payments that require 3D Secure

Use the 4000 0000 0000 3063 card to simulate 3D Secure triggering for invoices. (You can also write custom Radar rules in test mode to trigger authentication.) When Stripe triggers a 3D Secure authentication, you can test authenticating or failing the payment attempt in the 3DS dialog that opens. If the payment is authenticated successfully, the invoice is paid. When a payment attempt fails, the authentication attempt is unsuccessful and the invoice remains open.

[4000 0000 0000 3063](/testing#regulatory-cards)

[custom Radar rules](https://dashboard.stripe.com/test/radar/rules)

## Test bank transfer payments

To test manual payments on invoices through bank transfers:

- Create a testmode invoice with the collection method set to send_invoice and payment_settings[payment_method_types] array set to [customer_balance].

Create a testmode invoice with the collection method set to send_invoice and payment_settings[payment_method_types] array set to [customer_balance].

- Find the invoice in the Dashboard and click Send. This generates a unique virtual bank account number for your customer.

Find the invoice in the Dashboard and click Send. This generates a unique virtual bank account number for your customer.

- Retrieve your customer’s unique virtual bank account number using the [Customer Balance Funding Instructions API)(/docs/payments/customer-balance/funding-instructions#create-funding-instructions). You can also find your customer’s virtual banking details in the Hosted Invoice Page and PDF.

Retrieve your customer’s unique virtual bank account number using the [Customer Balance Funding Instructions API)(/docs/payments/customer-balance/funding-instructions#create-funding-instructions). You can also find your customer’s virtual banking details in the Hosted Invoice Page and PDF.

## Test customer tax ID verification

Use these magic tax IDs to trigger certain verification conditions in test mode. The tax ID type must be either the EU VAT Number or Australian Business Number (ABN).
