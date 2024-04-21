# Bank Debits

With bank debits, you can pull funds directly from your customer’s bank account for both one-time and recurring purchases. Bank debits are often used by:

- Businesses collecting recurring payments from other businesses.

- Retail and services businesses that want a low-cost alternative to cards for large consumer payments, like rent or tuition.

Bank debits might not be a good fit for your business if:

- You deliver goods immediately after checkout because payment confirmation takes 3-7 days.

- Your business is sensitive to disputes—consider other payment methods because some bank debit methods favor the customer during disputes.

## Payment experience

To initiate a bank debit, a customer enters their bank account details during checkout and gives you permission to debit the account. This permission is called a mandate. View a sample mandate.

[sample mandate](https://qry5s.sse.codesandbox.io/?)

To reduce fraud with some bank debits, verify the bank account before the payment by confirming microdeposits or bank login. Verifying bank login can improve the user experience because customers pay by logging into their bank rather than entering bank account details.

## Product support

You can use a single integration for all bank debits that works across Stripe products. With Stripe Checkout, Payment Element, and Payment Links, you can enable bank debits right from the Dashboard with no integration work.

[Stripe Checkout](/payments/checkout)

[Payment Element](/payments/payment-element)

[Payment Links](/payment-links)

[ACH Direct Debit](/payments/ach-debit)

[Bacs Direct Debit](/payments/payment-methods/bacs-debit)

[BECS Debit](/payments/au-becs-debit)

[Pre-authorized debit in Canada](/payments/acss-debit)

[SEPA Direct Debit](/payments/sepa-debit)

1 Subscription mode isn’t supported.

Contact us to request a new bank debit method.

[Contact us](https://support.stripe.com/contact)

## Migrating from the Sources, Tokens, or Charges APIs

If your current bank debit integration uses the Sources, Tokens, or Bank Accounts API, we recommend following the appropriate migration guide to transition to Payment Intents API:

[Payment Intents API](/payments/payment-intents)

- ACH migration guide

[ACH migration guide](/payments/ach-debit/migrations)

- For all other bank debit payment methods, follow the general migration guide

[migration guide](/payments/payment-intents/migration)
