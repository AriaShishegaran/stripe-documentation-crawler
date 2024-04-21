# Request permissionsBeta

Application developers can request permissions for their applications. These permissions grant granular access to the Stripe API.

[Accounts](/api/accounts)

[Account Links](/api/account_links)

[domain registration](/payments/payment-methods/pmd-registration)

[Application Fees](/api/application_fees)

[Balance](/api/balance)

Balance transaction source

balance_transaction_source_read

Grants access to expand the source attribute when retrieving Balance Transactions

[Balance Transactions](/api/balance_transactions)

This permission also implies the following permissions: application_fee_read, balance_read, transfer_read

[Test clocks](/billing/testing/test-clocks)

[Charges](/api/charges)

Checkout Session

checkout_session_read, checkout_session_write

Grants access to Sessions

[Sessions](/api/checkout/sessions)

This permission also implies the following permissions: mandate_read, payment_intent_read, payment_links_read, product_read, setup_intent_read, sku_read

[Configurations](/api/terminal/configuration)

[Connection Tokens](/api/terminal/connection_tokens)

[Coupons](/api/coupons)

Credit note

credit_note_read, credit_note_write

Grants access to Credit Notes

[Credit Notes](/api/credit_notes)

This permission also implies the following permissions: invoice_read,

Customer portal

customer_portal_read, customer_portal_write

Grants access to the customer portal

[customer portal](/api/customer_portal)

If you’re using the customer portal to manage subscriptions or payment methods, you must also request elements_write.

Customer

customer_read, customer_write

Grants access to Customers

[Customers](/api/customers)

This permission also implies the following permission: billing_clock_read.

[Disputes](/api/disputes)

[Login Links](/api/account/login_link)

[Stripe.js Elements](/js/elements_object)

[Events](/api/events)

[Files](/api/files)

Invoice

invoice_read, invoice_write

Grants access to Invoices

[Invoices](/api/invoices)

This permission also implies the following permission: credit_note_read

If you’re using the hosted invoice page to manage invoices or payment methods, you must also request elements_write.

[hosted invoice page](/invoicing/hosted-invoice-page)

[Authorizations](/api/issuing/authorizations)

[Cards](/api/issuing/cardholders)

[Cardholders](/api/issuing/cardholders)

[Issuing Disputes](/api/issuing/disputes)

[Transactions](/api/issuing/transactions)

[Locations](/api/terminal/locations)

[Mandates](/api/mandates)

[Orders](/api/orders_legacy)

Payment intent

payment_intent_read, payment_intent_write

Grants access to PaymentIntents

[PaymentIntents](/api/payment_intents)

If you’re managing PaymentIntents with Stripe.js Elements, you must also request elements_write.

[Stripe.js Elements](/js/elements_object)

This permission also implies the following permissions: product_read, sku_read

Payment links

payment_links_read, payment_links_write

Grants access to Payment Links

[Payment Links](/payment-links)

This permission also implies the following permissions: mandate_read, product_read, sku_read

Payment method

payment_method_read, payment_method_write

Grants access to PaymentMethods

[PaymentMethods](/api/payment_methods)

This permission also implies the following permission: source_read

[Payouts](/api/payouts)

[Plans](/api/plans)

[Prices](/api/prices)

[Products](/api/products)

[Promotion Codes](/api/promotion_codes)

Quote

quote_read, quote_write

Grants access to Quotes

[Quotes](/api/quotes)

This permission also implies the following permissions: sku_read, product_read

[Readers](/api/terminal/readers)

[Report Types](/api/reporting/report_type)

[Report Runs](/api/reporting/report_run)

[Reviews](/api/radar/reviews)

[Secrets](/api/secret_management)

Setup Intent

setup_intent_read, setup_intent_write

Grants access to SetupIntents

[SetupIntents](/api/setup_intents)

If you’re managing SetupIntents with Stripe.js Elements, you must also request elements_write.

[Stripe.js Elements](/js/elements_object)

This permission also implies the following permission: mandate_read

[Shipping Rates](/api/shipping_rates)

[SKUs](/api/skus)

[Sources](/api/sources)

[Subscriptions](/api/subscriptions)

[Tax Rates](/api/tax_rates)

[Tokens](/api/tokens)

[Top-ups](/api/topups)

Transfer

transfer_read, transfer_write

Grants access to Transfers

[Transfers](/api/transfers)

This permission also implies the following permission: payout_read

[Usage Records](/api/usage_records)

[Webhook Endpoints](/api/webhook_endpoints)
