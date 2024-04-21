# OXXO payments

OXXO is a Mexican chain of convenience stores with thousands of locations across Latin America and represents nearly 20% of online transactions in Mexico. OXXO allows customers to pay bills and online purchases in-store with cash.

To complete a transaction, customers receive a voucher that includes a reference number for the transaction. Customers then bring their voucher to an OXXO store to make a cash payment. You will receive payment confirmation by the next business day along with the settled funds.

[Customers](/api/customers)

- Customer locationsMexico

Customer locations

Mexico

- Presentment currencyMXN

Presentment currency

MXN

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyCash-based payment method

Payment method family

Cash-based payment method

- Recurring paymentsNo

Recurring payments

No

- Payout timingStandard payout timing applies

Payout timing

Standard payout timing applies

- Connect supportYes

Connect support

Yes

- Dispute supportNo

Dispute support

No

- Refunds / Partial refundsNo / no

Refunds / Partial refunds

No / no

## Payment flow

Step 1. Selects OXXO at checkout

Step 2. Receives voucher with transaction reference

Step 3. Provides voucher and cash payment at OXXO store

Step 4. Receives notification that payment is complete

## Get started

You don’t actually have to integrate OXXO and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

Payment Links also supports adding OXXO from the Dashboard.

[Payment Links](/payment-links)

If your integration requires manually listing payment methods, learn how to manually configure OXXO as a payment.

[manually configure OXXO as a payment](/payments/oxxo/accept-a-payment)

Check out the OXXO sample on GitHub.

[sample on GitHub](https://github.com/stripe-samples/accept-a-payment)

## Disputed payments

OXXO payments have a low risk of fraud or unrecognized payments because the customer must provide cash payment in person at an OXXO convenience store. Customers can’t dispute OXXO payments.

## Refunds

OXXO payments can’t be refunded. Some merchants have created a separate process to credit their customers who reach out directly.

## Amount limits

The amount for a single OXXO must be at least 10.00 MXN and no more than 10,000.00 MXN.
