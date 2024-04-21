- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Delete a plan

[Delete a plan](/api/plans/delete)

Deleting plans means new subscribers can’t be added. Existing subscribers aren’t affected.

No parameters.

An object with the deleted plan’s ID and a deleted flag upon success. Otherwise, this call raises an error, such as if the plan has already been deleted.

[an error](#errors)

# Quote

[Quote](/api/quotes)

A Quote is a way to model prices that you’d like to provide to a customer. Once accepted, it will automatically create an invoice, subscription or subscription schedule.

[POST/v1/quotes](/api/quotes/create)

[POST/v1/quotes/:id](/api/quotes/update)

[GET/v1/quotes/:id/line_items](/api/quotes/line_items/list)

[GET/v1/quotes/:id/computed_upfront_line_items](/api/quotes/line_items/upfront/list)

[GET/v1/quotes/:id](/api/quotes/retrieve)

[GET/v1/quotes](/api/quotes/list)

[POST/v1/quotes/:id/accept](/api/quotes/accept)

[POST/v1/quotes/:id/cancel](/api/quotes/cancel)

[GET/v1/quotes/:id/pdf](/api/quotes/pdf)

[POST/v1/quotes/:id/finalize](/api/quotes/finalize)

Show

# Subscriptions

[Subscriptions](/api/subscriptions)

Subscriptions allow you to charge a customer on a recurring basis.

Related guide: Creating subscriptions

[Creating subscriptions](/billing/subscriptions/creating)

[POST/v1/subscriptions](/api/subscriptions/create)

[POST/v1/subscriptions/:id](/api/subscriptions/update)

[GET/v1/subscriptions/:id](/api/subscriptions/retrieve)

[GET/v1/subscriptions](/api/subscriptions/list)

[DELETE/v1/subscriptions/:id](/api/subscriptions/cancel)

[POST/v1/subscriptions/:id/resume](/api/subscriptions/resume)

[GET/v1/subscriptions/search](/api/subscriptions/search)

Show

# Subscription Items

[Subscription Items](/api/subscription_items)

Subscription items allow you to create customer subscriptions with more than one plan, making it easy to represent complex billing relationships.

[POST/v1/subscription_items](/api/subscription_items/create)

[POST/v1/subscription_items/:id](/api/subscription_items/update)

[GET/v1/subscription_items/:id](/api/subscription_items/retrieve)

[GET/v1/subscription_items](/api/subscription_items/list)

[DELETE/v1/subscription_items/:id](/api/subscription_items/delete)

Show

# Subscription Schedule

[Subscription Schedule](/api/subscription_schedules)

A subscription schedule allows you to create and manage the lifecycle of a subscription by predefining expected changes.

Related guide: Subscription schedules

[Subscription schedules](/billing/subscriptions/subscription-schedules)

[POST/v1/subscription_schedules](/api/subscription_schedules/create)

[POST/v1/subscription_schedules/:id](/api/subscription_schedules/update)

[GET/v1/subscription_schedules/:id](/api/subscription_schedules/retrieve)

[GET/v1/subscription_schedules](/api/subscription_schedules/list)

[POST/v1/subscription_schedules/:id/cancel](/api/subscription_schedules/cancel)

[POST/v1/subscription_schedules/:id/release](/api/subscription_schedules/release)

Show

# Tax IDs

[Tax IDs](/api/tax_ids)

You can add one or multiple tax IDs to a customer or account. Customer and account tax IDs get displayed on related invoices and credit notes.

[customer](/api/customers)

Related guides: Customer tax identification numbers, Account tax IDs

[Customer tax identification numbers](/billing/taxes/tax-ids)

[Account tax IDs](/invoicing/connect#account-tax-ids)

[POST/v1/customers/:id/tax_ids](/api/tax_ids/customer_create)

[POST/v1/tax_ids](/api/tax_ids/create)

[GET/v1/customers/:id/tax_ids/:id](/api/tax_ids/customer_retrieve)

[GET/v1/tax_ids/:id](/api/tax_ids/retrieve)

[GET/v1/customers/:id/tax_ids](/api/tax_ids/customer_list)

[GET/v1/tax_ids](/api/tax_ids/list)

[DELETE/v1/customers/:id/tax_ids/:id](/api/tax_ids/customer_delete)

[DELETE/v1/tax_ids/:id](/api/tax_ids/delete)

Show

# Test ClocksTest helper

[Test Clocks](/api/test_clocks)

A test clock enables deterministic control over objects in testmode. With a test clock, you can create objects at a frozen time in the past or future, and advance to a specific future time to observe webhooks and state changes. After the clock advances, you can either validate the current state of your scenario (and test your assumptions), change the current state of your scenario (and test more complex scenarios), or keep advancing forward in time.

[POST/v1/test_helpers/test_clocks](/api/test_clocks/create)

[GET/v1/test_helpers/test_clocks/:id](/api/test_clocks/retrieve)

[GET/v1/test_helpers/test_clocks](/api/test_clocks/list)

[DELETE/v1/test_helpers/test_clocks/:id](/api/test_clocks/delete)

[POST/v1/test_helpers/test_clocks/:id/advance](/api/test_clocks/advance)

Show

# Usage Records

[Usage Records](/api/usage_records)

Usage records allow you to report customer usage and metrics to Stripe for metered billing of subscription prices.

Related guide: Metered billing

[Metered billing](/billing/subscriptions/metered-billing)

This is our legacy usage-based billing API. See the updated usage-based billing docs.

[updated usage-based billing docs](https://docs.stripe.com/billing/subscriptions/usage-based)

[POST/v1/subscription_items/:id/usage_records](/api/usage_records/create)

[GET/v1/subscription_items/:id/usage_record_summaries](/api/usage_records/subscription_item_summary_list)

Show

# Accounts

[Accounts](/api/accounts)

This is an object representing a Stripe account. You can retrieve it to see properties on the account like its current requirements or if the account is enabled to make live charges or receive payouts.

For Custom accounts, the properties below are always returned. For other accounts, some properties are returned until that account has started to go through Connect Onboarding. Once you create an Account Link or Account Session, some properties are only returned for Custom accounts. Learn about the differences between accounts.

[Account Link](/api/account_links)

[Account Session](/api/account_sessions)

[between accounts](/connect/accounts)

[POST/v1/accounts](/api/accounts/create)

[POST/v1/accounts/:id](/api/accounts/update)

[GET/v1/accounts/:id](/api/accounts/retrieve)

[GET/v1/accounts](/api/accounts/list)

[DELETE/v1/accounts/:id](/api/accounts/delete)

[POST/v1/accounts/:id/reject](/api/account/reject)

Show

# Login Links

[Login Links](/api/accounts/login_link)

Login Links are single-use login link for an Express account to access their Stripe dashboard.

[POST/v1/accounts/:id/login_links](/api/accounts/login_link/create)

Show

# Account Links

[Account Links](/api/account_links)

Account Links are the means by which a Connect platform grants a connected account permission to access Stripe-hosted applications, such as Connect Onboarding.

Related guide: Connect Onboarding

[Connect Onboarding](/connect/custom/hosted-onboarding)

[POST/v1/account_links](/api/account_links/create)

Show

# Account Session

[Account Session](/api/account_sessions)

An AccountSession allows a Connect platform to grant access to a connected account in Connect embedded components.

We recommend that you create an AccountSession each time you need to display an embedded component to your user. Do not save AccountSessions to your database as they expire relatively quickly, and cannot be used more than once.

Related guide: Connect embedded components

[Connect embedded components](/connect/get-started-connect-embedded-components)

[POST/v1/account_sessions](/api/account_sessions/create)

Show

# Application Fees

[Application Fees](/api/application_fees)

When you collect a transaction fee on top of a charge made for your user (using Connect), an Application Fee object is created in your account. You can list, retrieve, and refund application fees.

[Connect](/connect)

Related guide: Collecting application fees

[Collecting application fees](/connect/direct-charges#collect-fees)

[GET/v1/application_fees/:id](/api/application_fees/retrieve)

[GET/v1/application_fees](/api/application_fees/list)

Show

# Application Fee Refunds

[Application Fee Refunds](/api/fee_refunds)

Application Fee Refund objects allow you to refund an application fee that has previously been created but not yet refunded. Funds will be refunded to the Stripe account from which the fee was originally collected.

Related guide: Refunding application fees

[Refunding application fees](/connect/destination-charges#refunding-app-fee)

[POST/v1/application_fees/:id/refunds](/api/fee_refunds/create)

[POST/v1/application_fees/:id/refunds/:id](/api/fee_refunds/update)

[GET/v1/application_fees/:id/refunds/:id](/api/fee_refunds/retrieve)

[GET/v1/application_fees/:id/refunds](/api/fee_refunds/list)

Show

# Capabilities

[Capabilities](/api/capabilities)

This is an object representing a capability for a Stripe account.

Related guide: Account capabilities

[Account capabilities](/connect/account-capabilities)

[POST/v1/accounts/:id/capabilities/:id](/api/capabilities/update)

[GET/v1/accounts/:id/capabilities/:id](/api/capabilities/retrieve)

[GET/v1/accounts/:id/capabilities](/api/capabilities/list)

Show

# Country Specs

[Country Specs](/api/country_specs)

Stripe needs to collect certain pieces of information about each account created. These requirements can differ depending on the account’s country. The Country Specs API makes these rules available to your integration.

You can also view the information from this API call as an online guide.

[an online guide](/connect/required-verification-information)

[GET/v1/country_specs/:id](/api/country_specs/retrieve)

[GET/v1/country_specs](/api/country_specs/list)

Show

# External Bank Accounts

[External Bank Accounts](/api/external_accounts)

External bank accounts are financial accounts associated with a Stripe platform’s connected accounts for the purpose of transferring funds to or from the connected account’s Stripe balance.

[POST/v1/accounts/:id/external_accounts](/api/external_account_bank_accounts/create)

[POST/v1/accounts/:id/external_accounts/:id](/api/external_account_bank_accounts/update)

[GET/v1/accounts/:id/external_accounts/:id](/api/external_account_bank_accounts/retrieve)

[GET/v1/accounts/:id/external_accounts](/api/external_account_bank_accounts/list)

[DELETE/v1/accounts/:id/external_accounts/:id](/api/external_account_bank_accounts/delete)

Show

# External Account Cards

[External Account Cards](/api/external_account_cards)

External account cards are debit cards associated with a Stripe platform’s connected accounts for the purpose of transferring funds to or from the connected accounts Stripe balance.

[POST/v1/accounts/:id/external_accounts](/api/external_account_cards/create)

[POST/v1/accounts/:id/external_accounts/:id](/api/external_account_cards/update)

[GET/v1/accounts/:id/external_accounts/:id](/api/external_account_cards/retrieve)

[GET/v1/accounts/:id/external_accounts](/api/external_account_cards/list)

[DELETE/v1/accounts/:id/external_accounts/:id](/api/external_account_cards/delete)

Show

# Person

[Person](/api/persons)

This is an object representing a person associated with a Stripe account.

A platform cannot access a Standard or Express account’s persons after the account starts onboarding, such as after generating an account link for the account. See the Standard onboarding or Express onboarding documentation for information about platform prefilling and account onboarding steps.

[Standard onboarding](/connect/standard-accounts)

[Express onboarding documentation](/connect/express-accounts)

Related guide: Handling identity verification with the API

[Handling identity verification with the API](/connect/handling-api-verification#person-information)

[POST/v1/accounts/:id/persons](/api/persons/create)

[POST/v1/accounts/:id/persons/:id](/api/persons/update)

[GET/v1/accounts/:id/persons/:id](/api/persons/retrieve)

[GET/v1/accounts/:id/persons](/api/persons/list)

[DELETE/v1/accounts/:id/persons/:id](/api/persons/delete)

Show

# Top-ups

[Top-ups](/api/topups)

To top up your Stripe balance, you create a top-up object. You can retrieve individual top-ups, as well as list all top-ups. Top-ups are identified by a unique, random ID.

Related guide: Topping up your platform account

[Topping up your platform account](/connect/top-ups)

[POST/v1/topups](/api/topups/create)

[POST/v1/topups/:id](/api/topups/update)

[GET/v1/topups/:id](/api/topups/retrieve)

[GET/v1/topups](/api/topups/list)

[POST/v1/topups/:id/cancel](/api/topups/cancel)

Show

# Transfers

[Transfers](/api/transfers)

A Transfer object is created when you move funds between Stripe accounts as part of Connect.

Before April 6, 2017, transfers also represented movement of funds from a Stripe account to a card or bank account. This behavior has since been split out into a Payout object, with corresponding payout endpoints. For more information, read about the transfer/payout split.

[Payout](#payout_object)

[transfer/payout split](/transfer-payout-split)

Related guide: Creating separate charges and transfers

[Creating separate charges and transfers](/connect/separate-charges-and-transfers)

[POST/v1/transfers](/api/transfers/create)

[POST/v1/transfers/:id](/api/transfers/update)

[GET/v1/transfers/:id](/api/transfers/retrieve)

[GET/v1/transfers](/api/transfers/list)

Show

# Transfer Reversals

[Transfer Reversals](/api/transfer_reversals)

Stripe Connect platforms can reverse transfers made to a connected account, either entirely or partially, and can also specify whether to refund any related application fees. Transfer reversals add to the platform’s balance and subtract from the destination account’s balance.

[Stripe Connect](/connect)

Reversing a transfer that was made for a destination charge is allowed only up to the amount of the charge. It is possible to reverse a transfer_group transfer only if the destination account has enough balance to cover the reversal.

[destination charge](/connect/destination-charges)

[transfer_group](/connect/separate-charges-and-transfers#transfer-options)

Related guide: Reverse transfers

[Reverse transfers](/connect/separate-charges-and-transfers#reverse-transfers)

[POST/v1/transfers/:id/reversals](/api/transfer_reversals/create)

[POST/v1/transfers/:id/reversals/:id](/api/transfer_reversals/update)

[GET/v1/transfers/:id/reversals/:id](/api/transfer_reversals/retrieve)

[GET/v1/transfers/:id/reversals](/api/transfer_reversals/list)

Show

# Secrets

[Secrets](/api/secret_management)

Secret Store is an API that allows Stripe Apps developers to securely persist secrets for use by UI Extensions and app backends.

The primary resource in Secret Store is a secret. Other apps can’t view secrets created by an app. Additionally, secrets are scoped to provide further permission control.

All Dashboard users and the app backend share account scoped secrets. Use the account scope for secrets that don’t change per-user, like a third-party API key.

A user scoped secret is accessible by the app backend and one specific Dashboard user. Use the user scope for per-user secrets like per-user OAuth tokens, where different users might have different permissions.

Related guide: Store data between page reloads

[Store data between page reloads](/stripe-apps/store-auth-data-custom-objects)

[GET/v1/apps/secrets](/api/apps/secret_store/list)

[POST/v1/apps/secrets/delete](/api/apps/secret_store/delete)

[GET/v1/apps/secrets/find](/api/apps/secret_store/find)

[POST/v1/apps/secrets](/api/apps/secret_store/set)

Show

# Early Fraud Warning

[Early Fraud Warning](/api/radar/early_fraud_warnings)

An early fraud warning indicates that the card issuer has notified us that a charge may be fraudulent.

Related guide: Early fraud warnings

[Early fraud warnings](/disputes/measuring#early-fraud-warnings)

[GET/v1/radar/early_fraud_warnings/:id](/api/radar/early_fraud_warnings/retrieve)

[GET/v1/radar/early_fraud_warnings](/api/radar/early_fraud_warnings/list)

Show

# Reviews

[Reviews](/api/radar/reviews)

Reviews can be used to supplement automated fraud detection with human expertise.

Learn more about Radar and reviewing payments here.

[Radar](/radar)

[here](/radar/reviews)

[GET/v1/reviews/:id](/api/radar/reviews/retrieve)

[GET/v1/reviews](/api/radar/reviews/list)

[POST/v1/reviews/:id/approve](/api/radar/reviews/approve)

Show

# Value Lists

[Value Lists](/api/radar/value_lists)

Value lists allow you to group values together which can then be referenced in rules.

Related guide: Default Stripe lists

[Default Stripe lists](/radar/lists#managing-list-items)

[POST/v1/radar/value_lists](/api/radar/value_lists/create)

[POST/v1/radar/value_lists/:id](/api/radar/value_lists/update)

[GET/v1/radar/value_lists/:id](/api/radar/value_lists/retrieve)

[GET/v1/radar/value_lists](/api/radar/value_lists/list)

[DELETE/v1/radar/value_lists/:id](/api/radar/value_lists/delete)

Show

# Value List Items

[Value List Items](/api/radar/value_list_items)

Value list items allow you to add specific values to a given Radar value list, which can then be used in rules.

Related guide: Managing list items

[Managing list items](/radar/lists#managing-list-items)

[POST/v1/radar/value_list_items](/api/radar/value_list_items/create)

[GET/v1/radar/value_list_items/:id](/api/radar/value_list_items/retrieve)

[GET/v1/radar/value_list_items](/api/radar/value_list_items/list)

[DELETE/v1/radar/value_list_items/:id](/api/radar/value_list_items/delete)

Show

# Authorizations

[Authorizations](/api/issuing/authorizations)

When an issued card is used to make a purchase, an Issuing Authorization object is created. Authorizations must be approved for the purchase to be completed successfully.

[issued card](/issuing)

[Authorizations](/issuing/purchases/authorizations)

Related guide: Issued card authorizations

[Issued card authorizations](/issuing/purchases/authorizations)

[POST/v1/issuing/authorizations/:id](/api/issuing/authorizations/update)

[GET/v1/issuing/authorizations/:id](/api/issuing/authorizations/retrieve)

[GET/v1/issuing/authorizations](/api/issuing/authorizations/list)

[POST/v1/issuing/authorizations/:id/approve](/api/issuing/authorizations/approve)

[POST/v1/issuing/authorizations/:id/decline](/api/issuing/authorizations/decline)

[POST/v1/test_helpers/issuing/authorizations](/api/issuing/authorizations/test_mode_create)

[POST/v1/test_helpers/issuing/authorizations/:id/capture](/api/issuing/authorizations/test_mode_capture)

[POST/v1/test_helpers/issuing/authorizations/:id/expire](/api/issuing/authorizations/test_mode_expire)

[POST/v1/test_helpers/issuing/authorizations/:id/increment](/api/issuing/authorizations/test_mode_increment)

[POST/v1/test_helpers/issuing/authorizations/:id/reverse](/api/issuing/authorizations/test_mode_reverse)

Show

# Cardholders

[Cardholders](/api/issuing/cardholders)

An Issuing Cardholder object represents an individual or business entity who is issued cards.

[issued](/issuing)

Related guide: How to create a cardholder

[How to create a cardholder](/issuing/cards#create-cardholder)

[POST/v1/issuing/cardholders](/api/issuing/cardholders/create)

[POST/v1/issuing/cardholders/:id](/api/issuing/cardholders/update)

[GET/v1/issuing/cardholders/:id](/api/issuing/cardholders/retrieve)

[GET/v1/issuing/cardholders](/api/issuing/cardholders/list)

Show

# Cards

[Cards](/api/issuing/cards)

You can create physical or virtual cards that are issued to cardholders.

[create physical or virtual cards](/issuing/cards)

[POST/v1/issuing/cards](/api/issuing/cards/create)

[POST/v1/issuing/cards/:id](/api/issuing/cards/update)

[GET/v1/issuing/cards/:id](/api/issuing/cards/retrieve)

[GET/v1/issuing/cards](/api/issuing/cards/list)

[POST/v1/test_helpers/issuing/cards/:id/shipping/deliver](/api/issuing/cards/test_mode_deliver)

[POST/v1/test_helpers/issuing/cards/:id/shipping/fail](/api/issuing/cards/test_mode_fail)

[POST/v1/test_helpers/issuing/cards/:id/shipping/return](/api/issuing/cards/test_mode_return)

[POST/v1/test_helpers/issuing/cards/:id/shipping/ship](/api/issuing/cards/test_mode_ship)

Show

# Disputes

[Disputes](/api/issuing/disputes)

As a card issuer, you can dispute transactions that the cardholder does not recognize, suspects to be fraudulent, or has other issues with.

[card issuer](/issuing)

Related guide: Issuing disputes

[Issuing disputes](/issuing/purchases/disputes)

[POST/v1/issuing/disputes](/api/issuing/disputes/create)

[POST/v1/issuing/disputes/:id](/api/issuing/disputes/update)

[GET/v1/issuing/disputes/:id](/api/issuing/disputes/retrieve)

[GET/v1/issuing/disputes](/api/issuing/disputes/list)

[POST/v1/issuing/disputes/:id/submit](/api/issuing/dispute/submit)

Show

# Funding Instructions

[Funding Instructions](/api/issuing/funding_instructions)

Funding Instructions contain reusable bank account and routing information. Push funds to these addresses via bank transfer to top up Issuing Balances.

[top up Issuing Balances](/issuing/funding/balance)

[POST/v1/issuing/funding_instructions](/api/issuing/funding_instructions/create)

[GET/v1/issuing/funding_instructions](/api/issuing/funding_instructions/list)

[POST/v1/test_helpers/issuing/fund_balance](/api/issuing/funding_instructions/fund)

Show

# Personalization Designs

[Personalization Designs](/api/issuing/personalization_designs)

A Personalization Design is a logical grouping of a Physical Bundle, card logo, and carrier text that represents a product line.

[POST/v1/issuing/personalization_designs](/api/issuing/personalization_designs/create)

[POST/v1/issuing/personalization_designs/:id](/api/issuing/personalization_designs/update)

[GET/v1/issuing/personalization_designs/:id](/api/issuing/personalization_designs/retrieve)

[GET/v1/issuing/personalization_designs](/api/issuing/personalization_designs/list)

[POST/v1/test_helpers/issuing/personalization_designs/:id/activate](/api/issuing/personalization_designs/activate_testmode)

[POST/v1/test_helpers/issuing/personalization_designs/:id/deactivate](/api/issuing/personalization_designs/deactivate_testmode)

[POST/v1/test_helpers/issuing/personalization_designs/:id/reject](/api/issuing/personalization_designs/reject_testmode)

Show

# Physical Bundles

[Physical Bundles](/api/issuing/physical_bundles)

A Physical Bundle represents the bundle of physical items - card stock, carrier letter, and envelope - that is shipped to a cardholder when you create a physical card.

[GET/v1/issuing/physical_bundles/:id](/api/issuing/physical_bundles/retrieve)

[GET/v1/issuing/physical_bundles](/api/issuing/physical_bundles/list)

Show

# TokensPreview feature

[Tokens](/api/issuing/tokens)

An issuing token object is created when an issued card is added to a digital wallet. As a card issuer, you can view and manage these tokens through Stripe.

[card issuer](/issuing)

[view and manage these tokens](/issuing/controls/token-management)

[POST/v1/issuing/tokens/:id](/api/issuing/tokens/update)

[GET/v1/issuing/tokens/:id](/api/issuing/tokens/retrieve)

[GET/v1/issuing/tokens](/api/issuing/tokens/list)

Show

# Transactions

[Transactions](/api/issuing/transactions)

Any use of an issued card that results in funds entering or leaving your Stripe account, such as a completed purchase or refund, is represented by an Issuing Transaction object.

[issued card](/issuing)

Related guide: Issued card transactions

[Issued card transactions](/issuing/purchases/transactions)

[POST/v1/issuing/transactions/:id](/api/issuing/transactions/update)

[GET/v1/issuing/transactions/:id](/api/issuing/transactions/retrieve)

[GET/v1/issuing/transactions](/api/issuing/transactions/list)

[POST/v1/test_helpers/issuing/transactions/create_force_capture](/api/issuing/transactions/test_mode_create_force_capture)

[POST/v1/test_helpers/issuing/transactions/create_unlinked_refund](/api/issuing/transactions/test_mode_create_unlinked_refund)

[POST/v1/test_helpers/issuing/transactions/:id/refund](/api/issuing/transactions/test_mode_refund)

Show

# Connection Token

[Connection Token](/api/terminal/connection_tokens)

A Connection Token is used by the Stripe Terminal SDK to connect to a reader.

Related guide: Fleet management

[Fleet management](/terminal/fleet/locations)

[POST/v1/terminal/connection_tokens](/api/terminal/connection_tokens/create)

Show

# Location

[Location](/api/terminal/locations)

A Location represents a grouping of readers.

Related guide: Fleet management

[Fleet management](/terminal/fleet/locations)

[POST/v1/terminal/locations](/api/terminal/locations/create)

[POST/v1/terminal/locations/:id](/api/terminal/locations/update)

[GET/v1/terminal/locations/:id](/api/terminal/locations/retrieve)

[GET/v1/terminal/locations](/api/terminal/locations/list)

[DELETE/v1/terminal/locations/:id](/api/terminal/locations/delete)

Show

# Reader

[Reader](/api/terminal/readers)

A Reader represents a physical device for accepting payment details.

Related guide: Connecting to a reader

[Connecting to a reader](/terminal/payments/connect-reader)

[POST/v1/terminal/readers](/api/terminal/readers/create)

[POST/v1/terminal/readers/:id](/api/terminal/readers/update)

[GET/v1/terminal/readers/:id](/api/terminal/readers/retrieve)

[GET/v1/terminal/readers](/api/terminal/readers/list)

[DELETE/v1/terminal/readers/:id](/api/terminal/readers/delete)

[POST/v1/terminal/readers/:id/cancel_action](/api/terminal/readers/cancel_action)

[POST/v1/terminal/readers/:id/collect_inputs](/api/terminal/readers/collect_inputs)

[POST/v1/terminal/readers/:id/confirm_payment_intent](/api/terminal/readers/confirm_payment_intent)

[POST/v1/terminal/readers/:id/collect_payment_method](/api/terminal/readers/collect_payment_method)

[POST/v1/terminal/readers/:id/process_payment_intent](/api/terminal/readers/process_payment_intent)

[POST/v1/terminal/readers/:id/process_setup_intent](/api/terminal/readers/process_setup_intent)

[POST/v1/terminal/readers/:id/refund_payment](/api/terminal/readers/refund_payment)

[POST/v1/terminal/readers/:id/set_reader_display](/api/terminal/readers/set_reader_display)

[POST/v1/test_helpers/terminal/readers/:id/present_payment_method](/api/terminal/readers/present_payment_method)

Show

# Terminal Hardware OrderPreview feature

[Terminal Hardware Order](/api/terminal/hardware_orders)

A TerminalHardwareOrder represents an order for Terminal hardware, containing information such as the price, shipping information and the items ordered.

[POST/v1/terminal/hardware_orders](/api/terminal/hardware_orders/create)

[GET/v1/terminal/hardware_orders/:id](/api/terminal/hardware_orders/retrieve)

[GET/v1/terminal/hardware_orders](/api/terminal/hardware_orders/list)

[POST/v1/terminal/hardware_orders/:id/cancel](/api/terminal/hardware_orders/cancel)

[GET/v1/terminal/hardware_orders/preview](/api/terminal/hardware_orders/preview)

[POST/v1/test_helpers/terminal/hardware_orders/:id/mark_ready_to_ship](/api/terminal/hardware_orders/test_mode_mark_ready_to_ship)

[POST/v1/test_helpers/terminal/hardware_orders/:id/deliver](/api/terminal/hardware_orders/test_mode_deliver)

[POST/v1/test_helpers/terminal/hardware_orders/:id/ship](/api/terminal/hardware_orders/test_mode_ship)

[POST/v1/test_helpers/terminal/hardware_orders/:id/mark_undeliverable](/api/terminal/hardware_orders/test_mode_mark_undeliverable)

Show

# Terminal Hardware ProductPreview feature

[Terminal Hardware Product](/api/terminal/hardware_products)

A TerminalHardwareProduct is a category of hardware devices that are generally similar, but may have variations depending on the country it’s shipped to.

TerminalHardwareSKUs represent variations within the same Product (for example, a country specific device). For example, WisePOS E is a TerminalHardwareProduct and a WisePOS E - US and WisePOS E - UK are TerminalHardwareSKUs.

[GET/v1/terminal/hardware_products/:id](/api/terminal/hardware_products/retrieve)

[GET/v1/terminal/hardware_products](/api/terminal/hardware_products/list)

Show

# Terminal Hardware SKUPreview feature

[Terminal Hardware SKU](/api/terminal/hardware_skus)

A TerminalHardwareSKU represents a SKU for Terminal hardware. A SKU is a representation of a product available for purchase, containing information such as the name, price, and images.

[GET/v1/terminal/hardware_skus/:id](/api/terminal/hardware_skus/retrieve)

[GET/v1/terminal/hardware_skus](/api/terminal/hardware_skus/list)

Show

# Terminal Hardware Shipping MethodPreview feature

[Terminal Hardware Shipping Method](/api/terminal/hardware_shipping_methods)

A TerminalHardwareShipping represents a Shipping Method for Terminal hardware. A Shipping Method is a country-specific representation of a way to ship hardware, containing information such as the country, name, and expected delivery date.

[GET/v1/terminal/hardware_shipping_methods/:id](/api/terminal/hardware_shipping_methods/retrieve)

[GET/v1/terminal/hardware_shipping_methods](/api/terminal/hardware_shipping_methods/list)

Show

# Configuration

[Configuration](/api/terminal/configuration)

A Configurations object represents how features should be configured for terminal readers.

[POST/v1/terminal/configurations](/api/terminal/configuration/create)

[POST/v1/terminal/configurations/:id](/api/terminal/configuration/update)

[GET/v1/terminal/configurations/:id](/api/terminal/configuration/retrieve)

[GET/v1/terminal/configurations](/api/terminal/configuration/list)

[DELETE/v1/terminal/configurations/:id](/api/terminal/configuration/delete)

Show

# Financial Accounts

[Financial Accounts](/api/treasury/financial_accounts)

Stripe Treasury provides users with a container for money called a FinancialAccount that is separate from their Payments balance. FinancialAccounts serve as the source and destination of Treasury’s money movement APIs.

[POST/v1/treasury/financial_accounts](/api/treasury/financial_accounts/create)

[POST/v1/treasury/financial_accounts/:id](/api/treasury/financial_accounts/update)

[GET/v1/treasury/financial_accounts/:id](/api/treasury/financial_accounts/retrieve)

[GET/v1/treasury/financial_accounts](/api/treasury/financial_accounts/list)

Show

# Financial Account Features

[Financial Account Features](/api/treasury/financial_account_features)

Encodes whether a FinancialAccount has access to a particular Feature, with a status enum and associated status_details. Stripe or the platform can control Features via the requested field.

[POST/v1/treasury/financial_accounts/:id/features](/api/treasury/financial_account_features/update)

[GET/v1/treasury/financial_accounts/:id/features](/api/treasury/financial_account_features/retrieve)

Show

# Transactions

[Transactions](/api/treasury/transactions)

Transactions represent changes to a FinancialAccount’s balance.

[FinancialAccount’s](#financial_accounts)

[GET/v1/treasury/transactions/:id](/api/treasury/transactions/retrieve)

[GET/v1/treasury/transactions](/api/treasury/transactions/list)

Show

# Transaction Entries

[Transaction Entries](/api/treasury/transaction_entries)

TransactionEntries represent individual units of money movements within a single Transaction.

[Transaction](#transactions)

[GET/v1/treasury/transaction_entries/:id](/api/treasury/transaction_entries/retrieve)

[GET/v1/treasury/transaction_entries](/api/treasury/transaction_entries/list)

Show

# Outbound Transfers

[Outbound Transfers](/api/treasury/outbound_transfers)

Use OutboundTransfers to transfer funds from a FinancialAccount to a PaymentMethod belonging to the same entity. To send funds to a different party, use OutboundPayments instead. You can send funds over ACH rails or through a domestic wire transfer to a user’s own external bank account.

[FinancialAccount](#financial_accounts)

[OutboundPayments](#outbound_payments)

Simulate OutboundTransfer state changes with the /v1/test_helpers/treasury/outbound_transfers endpoints. These methods can only be called on test mode objects.

[POST/v1/treasury/outbound_transfers](/api/treasury/outbound_transfers/create)

[GET/v1/treasury/outbound_transfers/:id](/api/treasury/outbound_transfers/retrieve)

[GET/v1/treasury/outbound_transfers](/api/treasury/outbound_transfers/list)

[POST/v1/treasury/outbound_transfers/:id/cancel](/api/treasury/outbound_transfers/cancel)

[POST/v1/test_helpers/treasury/outbound_transfers/:id/fail](/api/treasury/outbound_transfers/test_mode_fail)

[POST/v1/test_helpers/treasury/outbound_transfers/:id/post](/api/treasury/outbound_transfers/test_mode_post)

[POST/v1/test_helpers/treasury/outbound_transfers/:id/return](/api/treasury/outbound_transfers/test_mode_return)

Show

# Outbound Payments

[Outbound Payments](/api/treasury/outbound_payments)

Use OutboundPayments to send funds to another party’s external bank account or FinancialAccount. To send money to an account belonging to the same user, use an OutboundTransfer.

[FinancialAccount](#financial_accounts)

[OutboundTransfer](#outbound_transfers)

Simulate OutboundPayment state changes with the /v1/test_helpers/treasury/outbound_payments endpoints. These methods can only be called on test mode objects.

[POST/v1/treasury/outbound_payments](/api/treasury/outbound_payments/create)

[GET/v1/treasury/outbound_payments/:id](/api/treasury/outbound_payments/retrieve)

[GET/v1/treasury/outbound_payments](/api/treasury/outbound_payments/list)

[POST/v1/treasury/outbound_payments/:id/cancel](/api/treasury/outbound_payments/cancel)

[POST/v1/test_helpers/treasury/outbound_payments/:id/fail](/api/treasury/outbound_payments/test_mode_fail)

[POST/v1/test_helpers/treasury/outbound_payments/:id/post](/api/treasury/outbound_payments/test_mode_post)

[POST/v1/test_helpers/treasury/outbound_payments/:id/return](/api/treasury/outbound_payments/test_mode_return)

Show

# Inbound Transfers

[Inbound Transfers](/api/treasury/inbound_transfers)

Use InboundTransfers to add funds to your FinancialAccount via a PaymentMethod that is owned by you. The funds will be transferred via an ACH debit.

[InboundTransfers](/treasury/moving-money/financial-accounts/into/inbound-transfers)

[FinancialAccount](#financial_accounts)

[POST/v1/treasury/inbound_transfers](/api/treasury/inbound_transfers/create)

[GET/v1/treasury/inbound_transfers/:id](/api/treasury/inbound_transfers/retrieve)

[GET/v1/treasury/inbound_transfers](/api/treasury/inbound_transfers/list)

[POST/v1/treasury/inbound_transfers/:id/cancel](/api/treasury/inbound_transfers/cancel)

[POST/v1/test_helpers/treasury/inbound_transfers/:id/fail](/api/treasury/inbound_transfers/test_mode_fail)

[POST/v1/test_helpers/treasury/inbound_transfers/:id/return](/api/treasury/inbound_transfers/test_mode_return)

[POST/v1/test_helpers/treasury/inbound_transfers/:id/succeed](/api/treasury/inbound_transfers/test_mode_succeed)

Show

# Received Credits

[Received Credits](/api/treasury/received_credits)

ReceivedCredits represent funds sent to a FinancialAccount (for example, via ACH or wire). These money movements are not initiated from the FinancialAccount.

[FinancialAccount](#financial_accounts)

[GET/v1/treasury/received_credits/:id](/api/treasury/received_credits/retrieve)

[GET/v1/treasury/received_credits](/api/treasury/received_credits/list)

[POST/v1/test_helpers/treasury/received_credits](/api/treasury/received_credits/test_mode_create)

Show

# Received Debits

[Received Debits](/api/treasury/received_debits)

ReceivedDebits represent funds pulled from a FinancialAccount. These are not initiated from the FinancialAccount.

[FinancialAccount](#financial_accounts)

[GET/v1/treasury/received_debits/:id](/api/treasury/received_debits/retrieve)

[GET/v1/treasury/received_debits](/api/treasury/received_debits/list)

[POST/v1/test_helpers/treasury/received_debits](/api/treasury/received_debits/test_mode_create)

Show

# Credit Reversals

[Credit Reversals](/api/treasury/credit_reversals)

You can reverse some ReceivedCredits depending on their network and source flow. Reversing a ReceivedCredit leads to the creation of a new object known as a CreditReversal.

[ReceivedCredits](#received_credits)

[POST/v1/treasury/credit_reversals](/api/treasury/credit_reversals/create)

[GET/v1/treasury/credit_reversals/:id](/api/treasury/credit_reversals/retrieve)

[GET/v1/treasury/credit_reversals](/api/treasury/credit_reversals/list)

Show

# Debit Reversals

[Debit Reversals](/api/treasury/debit_reversals)

You can reverse some ReceivedDebits depending on their network and source flow. Reversing a ReceivedDebit leads to the creation of a new object known as a DebitReversal.

[ReceivedDebits](#received_debits)

[POST/v1/treasury/debit_reversals](/api/treasury/debit_reversals/create)

[GET/v1/treasury/debit_reversals/:id](/api/treasury/debit_reversals/retrieve)

[GET/v1/treasury/debit_reversals](/api/treasury/debit_reversals/list)

Show

# Feature

[Feature](/api/entitlements/feature)

A feature represents a monetizable ability or functionality in your system. Features can be assigned to products, and when those products are purchased, Stripe will create an entitlement to the feature for the purchasing customer.

[POST/v1/entitlements/features](/api/entitlements/feature/create)

[GET/v1/entitlements/features](/api/entitlements/feature/list)

[POST/v1/entitlements/features/:id](/api/entitlements/feature/updates)

Show

# Product Feature

[Product Feature](/api/product-feature)

A product_feature represents an attachment between a feature and a product. When a product is purchased that has a feature attached, Stripe will create an entitlement to the feature for the purchasing customer.

[GET/v1/products/:id/features](/api/product-feature/list)

[POST/v1/products/:id/features](/api/product-feature/attach)

[DELETE/v1/products/:id/features/:id](/api/product-feature/remove)

Show

# Active Entitlement

[Active Entitlement](/api/entitlements/active-entitlement)

An active entitlement describes access to a feature for a customer.

[GET/v1/entitlements/active_entitlements](/api/entitlements/active-entitlement/list)

Show

# Scheduled Queries

[Scheduled Queries](/api/sigma/scheduled_queries)

If you have scheduled a Sigma query, you’ll receive a sigma.scheduled_query_run.created webhook each time the query runs. The webhook contains a ScheduledQueryRun object, which you can use to retrieve the query results.

[scheduled a Sigma query](/sigma/scheduled-queries)

[GET/v1/sigma/scheduled_query_runs/:id](/api/sigma/scheduled_queries/retrieve)

[GET/v1/sigma/scheduled_query_runs](/api/sigma/scheduled_queries/list)

Show

# Report Runs

[Report Runs](/api/reporting/report_run)

The Report Run object represents an instance of a report type generated with specific run parameters. Once the object is created, Stripe begins processing the report. When the report has finished running, it will give you a reference to a file where you can retrieve your results. For an overview, see API Access to Reports.

[API Access to Reports](/reporting/statements/api)

Note that certain report types can only be run based on your live-mode data (not test-mode data), and will error when queried without a live-mode API key.

[live-mode API key](/keys#test-live-modes)

[POST/v1/reporting/report_runs](/api/reporting/report_run/create)

[GET/v1/reporting/report_runs/:id](/api/reporting/report_run/retrieve)

[GET/v1/reporting/report_runs](/api/reporting/report_run/list)

Show

# Report Types

[Report Types](/api/reporting/report_type)

The Report Type resource corresponds to a particular type of report, such as the “Activity summary” or “Itemized payouts” reports. These objects are identified by an ID belonging to a set of enumerated values. See API Access to Reports documentation for those Report Type IDs, along with required and optional parameters.

[API Access to Reports documentation](/reporting/statements/api)

Note that certain report types can only be run based on your live-mode data (not test-mode data), and will error when queried without a live-mode API key.

[live-mode API key](/keys#test-live-modes)

[GET/v1/reporting/report_types/:id](/api/reporting/report_type/retrieve)

[GET/v1/reporting/report_types](/api/reporting/report_type/list)

Show

# Accounts

[Accounts](/api/financial_connections/accounts)

A Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.

[GET/v1/financial_connections/accounts/:id](/api/financial_connections/accounts/retrieve)

[GET/v1/financial_connections/accounts](/api/financial_connections/accounts/list)

[POST/v1/financial_connections/accounts/:id/disconnect](/api/financial_connections/accounts/disconnect)

[POST/v1/financial_connections/accounts/:id/refresh](/api/financial_connections/accounts/refresh)

[POST/v1/financial_connections/accounts/:id/subscribe](/api/financial_connections/accounts/subscribe)

[POST/v1/financial_connections/accounts/:id/unsubscribe](/api/financial_connections/accounts/unsubscribe)

Show

# Account Owner

[Account Owner](/api/financial_connections/ownership)

Describes an owner of an account.

[GET/v1/financial_connections/accounts/:id/owners](/api/financial_connections/ownership/list)

Show

# Session

[Session](/api/financial_connections/sessions)

A Financial Connections Session is the secure way to programmatically launch the client-side Stripe.js modal that lets your users link their accounts.

[POST/v1/financial_connections/sessions](/api/financial_connections/sessions/create)

[GET/v1/financial_connections/sessions/:id](/api/financial_connections/sessions/retrieve)

Show

# Transactions

[Transactions](/api/financial_connections/transactions)

A Transaction represents a real transaction that affects a Financial Connections Account balance.

[GET/v1/financial_connections/transactions/:id](/api/financial-connections/transaction/retrieve)

[GET/v1/financial_connections/transactions](/api/financial_connections/transactions/list)

Show

# Tax Calculations

[Tax Calculations](/api/tax/calculations)

A Tax Calculation allows you to calculate the tax to collect from your customer.

Related guide: Calculate tax in your custom payment flow

[Calculate tax in your custom payment flow](/tax/custom)

[GET/v1/tax/calculations/:id/line_items](/api/tax/calculations/line_items)

[POST/v1/tax/calculations](/api/tax/calculations/create)

Show

# Tax Registrations

[Tax Registrations](/api/tax/registrations)

A Tax Registration lets us know that your business is registered to collect tax on payments within a region, enabling you to automatically collect tax.

[automatically collect tax](/tax)

Stripe doesn’t register on your behalf with the relevant authorities when you create a Tax Registration object. For more information on how to register to collect tax, see our guide.

[our guide](/tax/registering)

Related guide: Using the Registrations API

[Using the Registrations API](/tax/registrations-api)

[POST/v1/tax/registrations](/api/tax/registrations/create)

[POST/v1/tax/registrations/:id](/api/tax/registrations/update)

[GET/v1/tax/registrations/:id](/api/tax/registrations/retrieve)

[GET/v1/tax/registrations](/api/tax/registrations/all)

Show

# Tax Transactions

[Tax Transactions](/api/tax/transactions)

A Tax Transaction records the tax collected from or refunded to your customer.

Related guide: Calculate tax in your custom payment flow

[Calculate tax in your custom payment flow](/tax/custom#tax-transaction)

[POST/v1/tax/transactions/create_reversal](/api/tax/transactions/create_reversal)

[POST/v1/tax/transactions/create_from_calculation](/api/tax/transactions/create_from_calculation)

[GET/v1/tax/transactions/:id/line_items](/api/tax/transactions/line_items)

[GET/v1/tax/transactions/:id](/api/tax/transactions/retrieve)

Show

# Tax Settings

[Tax Settings](/api/tax/settings)

You can use Tax Settings to manage configurations used by Stripe Tax calculations.

Related guide: Using the Settings API

[Using the Settings API](/tax/settings-api)

[POST/v1/tax/settings](/api/tax/settings/update)

[GET/v1/tax/settings](/api/tax/settings/retrieve)

Show

# Verification Session

[Verification Session](/api/identity/verification_sessions)

A VerificationSession guides you through the process of collecting and verifying the identities of your users. It contains details about the type of verification, such as what verification check to perform. Only create one VerificationSession for each verification in your system.

[verification check](/identity/verification-checks)

A VerificationSession transitions through multiple statuses throughout its lifetime as it progresses through the verification flow. The VerificationSession contains the user’s verified data after verification checks are complete.

[multiple statuses](/identity/how-sessions-work)

Related guide: The Verification Sessions API

[The Verification Sessions API](/identity/verification-sessions)

[POST/v1/identity/verification_sessions](/api/identity/verification_sessions/create)

[POST/v1/identity/verification_sessions/:id](/api/identity/verification_sessions/update)

[GET/v1/identity/verification_sessions/:id](/api/identity/verification_sessions/retrieve)

[GET/v1/identity/verification_sessions](/api/identity/verification_sessions/list)

[POST/v1/identity/verification_sessions/:id/cancel](/api/identity/verification_sessions/cancel)

[POST/v1/identity/verification_sessions/:id/redact](/api/identity/verification_sessions/redact)

Show

# Verification Report

[Verification Report](/api/identity/verification_reports)

A VerificationReport is the result of an attempt to collect and verify data from a user. The collection of verification checks performed is determined from the type and options parameters used. You can find the result of each verification check performed in the appropriate sub-resource: document, id_number, selfie.

Each VerificationReport contains a copy of any data collected by the user as well as reference IDs which can be used to access collected images through the FileUpload API. To configure and create VerificationReports, use the VerificationSession API.

[FileUpload](/api/files)

[VerificationSession](/api/identity/verification_sessions)

Related guides: Accessing verification results.

[Accessing verification results](/identity/verification-sessions#results)

[GET/v1/identity/verification_reports/:id](/api/identity/verification_reports/retrieve)

[GET/v1/identity/verification_reports](/api/identity/verification_reports/list)

Show

# Crypto Onramp Session

[Crypto Onramp Session](/api/crypto/onramp_sessions)

A Crypto Onramp Session represents your customer’s session as they purchase cryptocurrency through Stripe. Once payment is successful, Stripe will fulfill the delivery of cryptocurrency to your user’s wallet and contain a reference to the crypto transaction ID.

You can create an onramp session on your server and embed the widget on your frontend. Alternatively, you can redirect your users to the standalone hosted onramp.

Related guide: Integrate the onramp

[Integrate the onramp](/crypto/integrate-the-onramp)

[POST/v1/crypto/onramp_sessions](/api/crypto/onramp_sessions/create)

[GET/v1/crypto/onramp_sessions/:id](/api/crypto/onramp_sessions/retrieve)

[GET/v1/crypto/onramp_sessions](/api/crypto/onramp_sessions/list)

Show

# Crypto Onramp Quotes

[Crypto Onramp Quotes](/api/crypto/onramp_quotes)

Crypto Onramp Quotes are estimated quotes for onramp conversions into all the different cryptocurrencies on different networks. The Quotes API allows you to display quotes in your product UI before directing the user to the onramp widget.

Related guide: Quotes API

[Quotes API](/crypto/quotes-api)

[GET/v1/crypto/onramp/quotes](/api/crypto/onramp_quotes/retrieve)

Show

# Climate Order

[Climate Order](/api/climate/order)

Orders represent your intent to purchase a particular Climate product. When you create an order, the payment is deducted from your merchant balance.

[POST/v1/climate/orders](/api/climate/order/create)

[POST/v1/climate/orders/:id](/api/climate/order/update)

[GET/v1/climate/orders/:id](/api/climate/order/retrieve)

[GET/v1/climate/orders](/api/climate/order/list)

[POST/v1/climate/orders/:id/cancel](/api/climate/order/cancel)

Show

# Climate Product

[Climate Product](/api/climate/product)

A Climate product represents a type of carbon removal unit available for reservation. You can retrieve it to see the current price and availability.

[GET/v1/climate/products/:id](/api/climate/product/retrieve)

[GET/v1/climate/products](/api/climate/product/list)

Show

# Climate Supplier

[Climate Supplier](/api/climate/supplier)

A supplier of carbon removal.

[GET/v1/climate/suppliers/:id](/api/climate/supplier/retrieve)

[GET/v1/climate/suppliers](/api/climate/supplier/list)

Show

# Forwarding RequestPreview feature

[Forwarding Request](/api/forwarding/request)

Instructs Stripe to make a request on your behalf using the destination URL. The destination URL is activated by Stripe at the time of onboarding. Stripe verifies requests with your credentials provided during onboarding, and injects card details from the payment_method into the request.

Stripe redacts all sensitive fields and headers, including authentication credentials and card numbers, before storing the request and response data in the forwarding Request object, which are subject to a 30-day retention period.

You can provide a Stripe idempotency key to make sure that requests with the same key result in only one outbound request. The Stripe idempotency key provided should be unique and different from any idempotency keys provided on the underlying third-party request.

Forwarding Requests are synchronous requests that return a response or time out according to Stripe’s limits.

Related guide: Forward card details to third-party API endpoints.

[Forward card details to third-party API endpoints](https://docs.stripe.com/payments/forwarding)

[POST/v1/forwarding/requests](/api/forwarding/forwarding_requests/create)

[GET/v1/forwarding/requests/:id](/api/forwarding/forwarding_requests/retrieve)

[GET/v1/forwarding/requests](/api/forwarding/forwarding_requests/list)

Show

# Webhook Endpoints

[Webhook Endpoints](/api/webhook_endpoints)

You can configure webhook endpoints via the API to be notified about events that happen in your Stripe account or connected accounts.

[webhook endpoints](/webhooks/)

Most users configure webhooks from the dashboard, which provides a user interface for registering and testing your webhook endpoints.

[the dashboard](https://dashboard.stripe.com/webhooks)

Related guide: Setting up webhooks

[Setting up webhooks](/webhooks/configure)

[POST/v1/webhook_endpoints](/api/webhook_endpoints/create)

[POST/v1/webhook_endpoints/:id](/api/webhook_endpoints/update)

[GET/v1/webhook_endpoints/:id](/api/webhook_endpoints/retrieve)

[GET/v1/webhook_endpoints](/api/webhook_endpoints/list)

[DELETE/v1/webhook_endpoints/:id](/api/webhook_endpoints/delete)

Show
