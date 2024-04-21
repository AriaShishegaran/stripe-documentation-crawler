htmlPermissions reference | Stripe Documentation[Skip to content](#main-content)Permissions[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Freference%2Fpermissions)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Freference%2Fpermissions)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# Permissions reference

A list of available events and their required permissions.A Stripe App needs permission to read or write user data. This includes these situations:

- Accessing Stripe API objects—see[Object permissions](#object)
- Subscribing to events—see[Event permissions](#event)

To request permissions, list them in the permissions array in your app manifest file. You can also manage this array from the CLI. Account administrators that install your app must accept the permissions that you list before using it.

If your app performs an action it lacks permissions for, Stripe might raise an invalid request error.

## Manage permissions

You can add a permission to the permissions array in your stripe-app.json app manifest file using the following command:

Command Line`stripe apps grant permission "PERMISSION_NAME" "EXPLANATION"`Replace:

- `PERMISSION_NAME`: The name of the permission you’d like to add. See[possible permission names](/security/permissions).
- `EXPLANATION`: Explanation for enabling access. Users see this explanation when they install your app.

Repeat this step for each new permission that you want to add to your application.

### After you add your permission, your app manifest file should look like this:

To remove a permission, you can also use the CLI:

Command Line`stripe apps revoke permission "PERMISSION_NAME"`## Object permissions

For each API object your app reads or writes, it must request at least one of the corresponding permissions.

If you are expanding objects in the responses of your API requests, you must also request at least one corresponding permission for each API object you expand.

ResourcePermissionDescriptionAccount`connected_account_read`Grants access to read[Accounts](/api/accounts)Account link`account_link_write`Grants access to[Account Links](/api/account_links)Apple Pay Domain`apple_pay_domain_read`,`apple_pay_domain_write`Grants access to Apple Pay Domain resources. To use Apple Pay, you need to register your web domains with Apple. See[domain registration](/payments/payment-methods/pmd-registration)for more information.Application Fee`application_fee_read`,`application_fee_write`Grants access to[Application Fees](/api/application_fees)Balance`balance_read`Grants access to[Balance](/api/balance)Balance transaction source

balance_transaction_source_read

Grants access to expand the source attribute when retrieving Balance Transactions

This permission also implies the following permissions: application_fee_read, balance_read, transfer_read

Billing clock`billing_clock_read`,`billing_clock_write`Grants access to[Test clocks](/billing/testing/test-clocks)Charge`charge_read`,`charge_write`Grants access to[Charges](/api/charges)Checkout Session

checkout_session_read, checkout_session_write

Grants access to Sessions

This permission also implies the following permissions: mandate_read, payment_intent_read, payment_links_read, product_read, setup_intent_read, sku_read

Configuration`terminal_configuration_read`,`terminal_configuration_write`Grants access to[Configurations](/api/terminal/configuration)Connection Token`terminal_connection_token_write`Grants access to[Connection Tokens](/api/terminal/connection_tokens)Coupon`coupon_read`,`coupon_write`Grants access to[Coupons](/api/coupons)Credit note

credit_note_read, credit_note_write

Grants access to Credit Notes

This permission also implies the following permissions: invoice_read,

Customer portal

customer_portal_read, customer_portal_write

Grants access to the customer portal

If you’re using the customer portal to manage subscriptions or payment methods, you must also request elements_write.

Customer

customer_read, customer_write

Grants access to Customers

This permission also implies the following permission: billing_clock_read.

Dispute`dispute_read`,`dispute_write`Grants access to[Disputes](/api/disputes)Edit link`edit_link_write`Grants access to[Login Links](/api/account/login_link)Elements`elements_write`Grants access to[Stripe.js Elements](/js/elements_object)Event`event_read`Grants access to[Events](/api/events)File`file_read`,`file_write`Grants access to[Files](/api/files)Invoice

invoice_read, invoice_write

Grants access to Invoices

This permission also implies the following permission: credit_note_read

If you’re using the hosted invoice page to manage invoices or payment methods, you must also request elements_write.

Issuing authorization`issuing_authorization_read`,`issuing_authorization_write`Grants access to[Authorizations](/api/issuing/authorizations)Issuing card`issuing_card_read`,`issuing_card_write`Grants access to[Cards](/api/issuing/cardholders)Issuing cardholder`issuing_cardholder_read`,`issuing_cardholder_write`Grants access to[Cardholders](/api/issuing/cardholders)Issuing dispute`issuing_dispute_read`,`issuing_dispute_write`Grants access to[Issuing Disputes](/api/issuing/disputes)Issuing transaction`issuing_transaction_read, issuing_transaction_write`Grants access to[Transactions](/api/issuing/transactions)Location`terminal_location_read`,`terminal_location_write`Grants access to[Locations](/api/terminal/locations)Mandate`mandate_read`,`mandate_write`Grants access to[Mandates](/api/mandates)Order`order_read`,`order_write`Grants access to[Orders](/api/orders_legacy)Payment intent

payment_intent_read, payment_intent_write

Grants access to PaymentIntents

If you’re managing PaymentIntents with Stripe.js Elements, you must also request elements_write.

This permission also implies the following permissions: product_read, sku_read

Payment links

payment_links_read, payment_links_write

Grants access to Payment Links

This permission also implies the following permissions: mandate_read, product_read, sku_read

Payment method

payment_method_read, payment_method_write

Grants access to PaymentMethods

This permission also implies the following permission: source_read

Payout`payout_read`,`payout_write`Grants access to[Payouts](/api/payouts)Plan`plan_read`,`plan_write`Grants access to[Plans](/api/plans)and[Prices](/api/prices)Product`product_read`,`product_write`Grants access to[Products](/api/products)Promotion Code`promotion_code_read`,`promotion_code_write`Grants access to[Promotion Codes](/api/promotion_codes)Quote

quote_read, quote_write

Grants access to Quotes

This permission also implies the following permissions: sku_read, product_read

Reader`terminal_reader_read`,`terminal_reader_write`Grants access to[Readers](/api/terminal/readers)Report Runs and Report Types`report_runs_and_report_types_read`Grants read access to[Report Types](/api/reporting/report_type)and allows creation of[Report Runs](/api/reporting/report_run)Review`review_read`,`review_write`Grants access to[Reviews](/api/radar/reviews)Secret`secret_write`Grants access to[Secrets](/api/secret_management)Setup Intent

setup_intent_read, setup_intent_write

Grants access to SetupIntents

If you’re managing SetupIntents with Stripe.js Elements, you must also request elements_write.

This permission also implies the following permission: mandate_read

Shipping rate`shipping_rate_read`,`shipping_rate_write`Grants access to[Shipping Rates](/api/shipping_rates)SKU`sku_read`,`sku_write`Grants access to[SKUs](/api/skus)Source`source_read`,`source_write`Grants access to[Sources](/api/sources)Subscription`subscription_read`,`subscription_write`Grants access to[Subscriptions](/api/subscriptions)Tax rate`tax_rate_read`,`tax_rate_write`Grants access to[Tax Rates](/api/tax_rates)Token`token_read`,`token_write`Grants access to[Tokens](/api/tokens)Top up`top_up_read`,`top_up_write`Grants access to[Top-ups](/api/topups)Transfer

transfer_read, transfer_write

Grants access to Transfers

This permission also implies the following permission: payout_read

Usage record`usage_record_read`,`usage_record_write`Grants access to[Usage Records](/api/usage_records)User Email`user_email_read`Grants access to user emailsWebhook`webhook_read`Grants access to[Webhook Endpoints](/api/webhook_endpoints)## Event permissions

For each Event your  app subscribes to, it must request at least one of the corresponding permissions.

Loading...## See also

- [App manifest reference](/stripe-apps/reference/app-manifest)
- [How UI extensions work](/stripe-apps/how-ui-extensions-work)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Manage permissions](#manage)[Object permissions](#object)[Event permissions](#event)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`