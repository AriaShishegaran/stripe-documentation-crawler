- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# List all charges

[List all charges](/api/charges/list)

Returns a list of charges you’ve previously created. The charges are returned in sorted order, with the most recent charges appearing first.

- customerstringOnly return charges for the customer specified by this customer ID.

Only return charges for the customer specified by this customer ID.

- createdobject

- ending_beforestring

- limitinteger

- payment_intentstring

- starting_afterstring

- transfer_groupstringConnect only

A dictionary with a data property that contains an array of up to limit charges, starting after charge starting_after. Each entry in the array is a separate charge object. If no more charges are available, the resulting array will be empty. If you provide a non-existent customer ID, this call raises an error.

[an error](#errors)

# Capture a charge

[Capture a charge](/api/charges/capture)

Capture the payment of an existing, uncaptured charge that was created with the capture option set to false.

Uncaptured payments expire a set number of days after they are created (7 by default), after which they are marked as refunded and capture attempts will fail.

[7 by default](/charges/placing-a-hold)

Don’t use this method to capture a PaymentIntent-initiated charge. Use Capture a PaymentIntent.

[Capture a PaymentIntent](/api/payment_intents/capture)

- amountintegerThe amount to capture, which must be less than or equal to the original amount. Any additional amount will be automatically refunded.

The amount to capture, which must be less than or equal to the original amount. Any additional amount will be automatically refunded.

- receipt_emailstringThe email address to send this charge’s receipt to. This will override the previously-specified email address for this charge, if one was set. Receipts will not be sent in test mode.

The email address to send this charge’s receipt to. This will override the previously-specified email address for this charge, if one was set. Receipts will not be sent in test mode.

- statement_descriptorstringFor card charges, use statement_descriptor_suffix instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters.

For card charges, use statement_descriptor_suffix instead. Otherwise, you can use this value as the complete description of a charge on your customers’ statements. Must contain at least one letter, maximum 22 characters.

- statement_descriptor_suffixstringProvides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.

Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that’s set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.

- application_fee_amountintegerConnect only

- transfer_dataobjectConnect only

- transfer_groupstringConnect only

Returns the charge object, with an updated captured property (set to true). Capturing a charge will always succeed, unless the charge is already refunded, expired, captured, or an invalid capture amount is specified, in which case this method will raise an error.

[an error](#errors)

# Search charges

[Search charges](/api/charges/search)

Search for charges you’ve previously created using Stripe’s Search Query Language. Don’t use search in read-after-write flows where strict consistency is necessary. Under normal operating conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up to an hour behind during outages. Search functionality is not available to merchants in India.

[Search Query Language](/search#search-query-language)

- querystringRequiredThe search query string. See search query language and the list of supported query fields for charges.

The search query string. See search query language and the list of supported query fields for charges.

[search query language](/search#search-query-language)

[query fields for charges](/search#query-fields-for-charges)

- limitintegerA limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.

- pagestringA cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

A cursor for pagination across multiple pages of results. Don’t include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.

A dictionary with a data property that contains an array of up to limit charges. If no objects match the query, the resulting array will be empty. See the related guide on expanding properties in lists.

[expanding properties in lists](/expand#lists)

# Customers

[Customers](/api/customers)

This object represents a customer of your business. Use it to create recurring charges and track payments that belong to the same customer.

Related guide: Save a card during payment

[Save a card during payment](/payments/save-during-payment)

[POST/v1/customers](/api/customers/create)

[POST/v1/customers/:id](/api/customers/update)

[GET/v1/customers/:id](/api/customers/retrieve)

[GET/v1/customers](/api/customers/list)

[DELETE/v1/customers/:id](/api/customers/delete)

[GET/v1/customers/search](/api/customers/search)

Show

# Customer Session

[Customer Session](/api/customer_sessions)

A customer session allows you to grant client access to Stripe’s frontend SDKs (like StripeJs) control over a customer.

[POST/v1/customer_sessions](/api/customer_sessions/create)

Show

# Disputes

[Disputes](/api/disputes)

A dispute occurs when a customer questions your charge with their card issuer. When this happens, you have the opportunity to respond to the dispute with evidence that shows that the charge is legitimate.

Related guide: Disputes and fraud

[Disputes and fraud](/disputes)

[POST/v1/disputes/:id](/api/disputes/update)

[GET/v1/disputes/:id](/api/disputes/retrieve)

[GET/v1/disputes](/api/disputes/list)

[POST/v1/disputes/:id/close](/api/disputes/close)

Show

# Events

[Events](/api/events)

Events are our way of letting you know when something interesting happens in your account. When an interesting event occurs, we create a new Event object. For example, when a charge succeeds, we create a charge.succeeded event, and when an invoice payment attempt fails, we create an invoice.payment_failed event. Certain API requests might create multiple events. For example, if you create a new subscription for a customer, you receive both a customer.subscription.created event and a charge.succeeded event.

Events occur when the state of another API resource changes. The event’s data field embeds the resource’s state at the time of the change. For example, a charge.succeeded event contains a charge, and an invoice.payment_failed event contains an invoice.

As with other API resources, you can use endpoints to retrieve an individual event or a list of events from the API. We also have a separate webhooks system for sending the Event objects directly to an endpoint on your server. You can manage webhooks in your account settings. Learn how to listen for events so that your integration can automatically trigger reactions.

[individual event](#retrieve_event)

[list of events](#list_events)

[webhooks](http://en.wikipedia.org/wiki/Webhook)

[account settings](https://dashboard.stripe.com/account/webhooks)

[listen for events](/webhooks)

When using Connect, you can also receive event notifications that occur in connected accounts. For these events, there’s an additional account attribute in the received Event object.

[Connect](/connect)

We only guarantee access to events through the Retrieve Event API for 30 days.

[Retrieve Event API](#retrieve_event)

[GET/v1/events/:id](/api/events/retrieve)

[GET/v1/events](/api/events/list)

Show

# Files

[Files](/api/files)

This object represents files hosted on Stripe’s servers. You can upload files with the create file request (for example, when uploading dispute evidence). Stripe also creates files independently (for example, the results of a Sigma scheduled query).

[create file](#create_file)

[Sigma scheduled query](#scheduled_queries)

Related guide: File upload guide

[File upload guide](/file-upload)

[POST/v1/files](/api/files/create)

[GET/v1/files/:id](/api/files/retrieve)

[GET/v1/files](/api/files/list)

Show

# File Links

[File Links](/api/file_links)

To share the contents of a File object with non-Stripe users, you can create a FileLink. FileLinks contain a URL that you can use to retrieve the contents of the file without authentication.

[POST/v1/file_links](/api/file_links/create)

[POST/v1/file_links/:id](/api/file_links/update)

[GET/v1/file_links/:id](/api/file_links/retrieve)

[GET/v1/file_links](/api/file_links/list)

Show

# Mandates

[Mandates](/api/mandates)

A Mandate is a record of the permission that your customer gives you to debit their payment method.

[GET/v1/mandates/:id](/api/mandates/retrieve)

Show

# Payment Intents

[Payment Intents](/api/payment_intents)

A PaymentIntent guides you through the process of collecting a payment from your customer. We recommend that you create exactly one PaymentIntent for each order or customer session in your system. You can reference the PaymentIntent later to see the history of payment attempts for a particular session.

A PaymentIntent transitions through multiple statuses throughout its lifetime as it interfaces with Stripe.js to perform authentication flows and ultimately creates at most one successful charge.

[multiple statuses](/payments/intents#intent-statuses)

Related guide: Payment Intents API

[Payment Intents API](/payments/payment-intents)

[POST/v1/payment_intents](/api/payment_intents/create)

[POST/v1/payment_intents/:id](/api/payment_intents/update)

[GET/v1/payment_intents/:id](/api/payment_intents/retrieve)

[GET/v1/payment_intents](/api/payment_intents/list)

[POST/v1/payment_intents/:id/cancel](/api/payment_intents/cancel)

[POST/v1/payment_intents/:id/capture](/api/payment_intents/capture)

[POST/v1/payment_intents/:id/confirm](/api/payment_intents/confirm)

[POST/v1/payment_intents/:id/increment_authorization](/api/payment_intents/increment_authorization)

[POST/v1/payment_intents/:id/apply_customer_balance](/api/payment_intents/apply_customer_balance)

[GET/v1/payment_intents/search](/api/payment_intents/search)

[POST/v1/payment_intents/:id/verify_microdeposits](/api/payment_intents/verify_microdeposits)

Show

# Setup Intents

[Setup Intents](/api/setup_intents)

A SetupIntent guides you through the process of setting up and saving a customer’s payment credentials for future payments. For example, you can use a SetupIntent to set up and save your customer’s card without immediately collecting a payment. Later, you can use PaymentIntents to drive the payment flow.

[PaymentIntents](#payment_intents)

Create a SetupIntent when you’re ready to collect your customer’s payment credentials. Don’t maintain long-lived, unconfirmed SetupIntents because they might not be valid. The SetupIntent transitions through multiple statuses as it guides you through the setup process.

[statuses](https://docs.stripe.com/payments/intents#intent-statuses)

Successful SetupIntents result in payment credentials that are optimized for future payments. For example, cardholders in certain regions might need to be run through Strong Customer Authentication during payment method collection to streamline later off-session payments. If you use the SetupIntent with a Customer, it automatically attaches the resulting payment method to that Customer after successful setup. We recommend using SetupIntents or setup_future_usage on PaymentIntents to save payment methods to prevent saving invalid or unoptimized payment methods.

[certain regions](https://stripe.com/guides/strong-customer-authentication)

[Strong Customer Authentication](https://docs.stripe.com/strong-customer-authentication)

[off-session payments](https://docs.stripe.com/payments/setup-intents)

[Customer](#setup_intent_object-customer)

[setup_future_usage](#payment_intent_object-setup_future_usage)

By using SetupIntents, you can reduce friction for your customers, even as regulations change over time.

Related guide: Setup Intents API

[Setup Intents API](https://docs.stripe.com/payments/setup-intents)

[POST/v1/setup_intents](/api/setup_intents/create)

[POST/v1/setup_intents/:id](/api/setup_intents/update)

[GET/v1/setup_intents/:id](/api/setup_intents/retrieve)

[GET/v1/setup_intents](/api/setup_intents/list)

[POST/v1/setup_intents/:id/cancel](/api/setup_intents/cancel)

[POST/v1/setup_intents/:id/confirm](/api/setup_intents/confirm)

[POST/v1/setup_intents/:id/verify_microdeposits](/api/setup_intents/verify_microdeposits)

Show

# Setup Attempts

[Setup Attempts](/api/setup_attempts)

A SetupAttempt describes one attempted confirmation of a SetupIntent, whether that confirmation is successful or unsuccessful. You can use SetupAttempts to inspect details of a specific attempt at setting up a payment method using a SetupIntent.

[GET/v1/setup_attempts](/api/setup_attempts/list)

Show

# Payouts

[Payouts](/api/payouts)

A Payout object is created when you receive funds from Stripe, or when you initiate a payout to either a bank account or debit card of a connected Stripe account. You can retrieve individual payouts, and list all payouts. Payouts are made on varying schedules, depending on your country and industry.

[connected Stripe account](/connect/bank-debit-card-payouts)

[varying schedules](/connect/manage-payout-schedule)

Related guide: Receiving payouts

[Receiving payouts](/payouts)

[POST/v1/payouts](/api/payouts/create)

[POST/v1/payouts/:id](/api/payouts/update)

[GET/v1/payouts/:id](/api/payouts/retrieve)

[GET/v1/payouts](/api/payouts/list)

[POST/v1/payouts/:id/cancel](/api/payouts/cancel)

[POST/v1/payouts/:id/reverse](/api/payouts/reverse)

Show

# Refunds

[Refunds](/api/refunds)

Refund objects allow you to refund a previously created charge that isn’t refunded yet. Funds are refunded to the credit or debit card that’s initially charged.

Related guide: Refunds

[Refunds](/refunds)

[POST/v1/refunds](/api/refunds/create)

[POST/v1/refunds/:id](/api/refunds/update)

[GET/v1/refunds/:id](/api/refunds/retrieve)

[GET/v1/refunds](/api/refunds/list)

[POST/v1/refunds/:id/cancel](/api/refunds/cancel)

Show

# Confirmation Token

[Confirmation Token](/api/confirmation_tokens)

ConfirmationTokens help transport client side data collected by Stripe JS over to your server for confirming a PaymentIntent or SetupIntent. If the confirmation is successful, values present on the ConfirmationToken are written onto the Intent.

To learn more about how to use ConfirmationToken, visit the related guides:

- Finalize payments on the server

[Finalize payments on the server](/payments/finalize-payments-on-the-server)

- Build two-step confirmation.

[Build two-step confirmation](/payments/build-a-two-step-confirmation)

[GET/v1/confirmation_tokens/:id](/api/confirmation_tokens/retrieve)

[POST/v1/test_helpers/confirmation_tokens](/api/confirmation_tokens/test_create)

Show

# Tokens

[Tokens](/api/tokens)

Tokenization is the process Stripe uses to collect sensitive card or bank account details, or personally identifiable information (PII), directly from your customers in a secure manner. A token representing this information is returned to your server to use. Use our recommended payments integrations to perform this process on the client-side. This guarantees that no sensitive card data touches your server, and allows your integration to operate in a PCI-compliant way.

[recommended payments integrations](/payments)

If you can’t use client-side tokenization, you can also create tokens using the API with either your publishable or secret API key. If your integration uses this method, you’re responsible for any PCI compliance that it might require, and you must keep your secret API key safe. Unlike with client-side tokenization, your customer’s information isn’t sent directly to Stripe, so we can’t determine how it’s handled or stored.

You can’t store or use tokens more than once. To store card or bank account information for later use, create Customer objects or Custom accounts. Radar, our integrated solution for automatic fraud protection, performs best with integrations that use client-side tokenization.

[Customer](/api#customers)

[Custom accounts](/api#external_accounts)

[Radar](/radar)

[POST/v1/tokens](/api/tokens/create_account)

[POST/v1/tokens](/api/tokens/create_bank_account)

[POST/v1/tokens](/api/tokens/create_card)

[POST/v1/tokens](/api/tokens/create_cvc_update)

[POST/v1/tokens](/api/tokens/create_person)

[POST/v1/tokens](/api/tokens/create_pii)

[GET/v1/tokens/:id](/api/tokens/retrieve)

Show

# Payment Methods

[Payment Methods](/api/payment_methods)

PaymentMethod objects represent your customer’s payment instruments. You can use them with PaymentIntents to collect payments or save them to Customer objects to store instrument details for future payments.

[PaymentIntents](/payments/payment-intents)

Related guides: Payment Methods and More Payment Scenarios.

[Payment Methods](/payments/payment-methods)

[More Payment Scenarios](/payments/more-payment-scenarios)

[POST/v1/payment_methods](/api/payment_methods/create)

[POST/v1/payment_methods/:id](/api/payment_methods/update)

[GET/v1/customers/:id/payment_methods/:id](/api/payment_methods/customer)

[GET/v1/payment_methods/:id](/api/payment_methods/retrieve)

[GET/v1/customers/:id/payment_methods](/api/payment_methods/customer_list)

[GET/v1/payment_methods](/api/payment_methods/list)

[POST/v1/payment_methods/:id/attach](/api/payment_methods/attach)

[POST/v1/payment_methods/:id/detach](/api/payment_methods/detach)

Show

# Payment Method Configurations

[Payment Method Configurations](/api/payment_method_configurations)

PaymentMethodConfigurations control which payment methods are displayed to your customers when you don’t explicitly specify payment method types. You can have multiple configurations with different sets of payment methods for different scenarios.

There are two types of PaymentMethodConfigurations. Which is used depends on the charge type:

[charge type](/connect/charges)

Direct configurations apply to payments created on your account, including Connect destination charges, Connect separate charges and transfers, and payments not involving Connect.

Child configurations apply to payments created on your connected accounts using direct charges, and charges with the on_behalf_of parameter.

Child configurations have a parent that sets default values and controls which settings connected accounts may override. You can specify a parent ID at payment time, and Stripe will automatically resolve the connected account’s associated child configuration. Parent configurations are managed in the dashboard and are not available in this API.

[managed in the dashboard](https://dashboard.stripe.com/settings/payment_methods/connected_accounts)

Related guides:

- Payment Method Configurations API

[Payment Method Configurations API](/connect/payment-method-configurations)

- Multiple configurations on dynamic payment methods

[Multiple configurations on dynamic payment methods](/payments/multiple-payment-method-configs)

- Multiple configurations for your Connect accounts

[Multiple configurations for your Connect accounts](/connect/multiple-payment-method-configurations)

[POST/v1/payment_method_configurations](/api/payment_method_configurations/create)

[POST/v1/payment_method_configurations/:id](/api/payment_method_configurations/update)

[GET/v1/payment_method_configurations/:id](/api/payment_method_configurations/retrieve)

[GET/v1/payment_method_configurations](/api/payment_method_configurations/list)

Show

# Payment Method Domains

[Payment Method Domains](/api/payment_method_domains)

A payment method domain represents a web domain that you have registered with Stripe. Stripe Elements use registered payment method domains to control where certain payment methods are shown.

Related guides: Payment method domains.

[Payment method domains](/payments/payment-methods/pmd-registration)

[POST/v1/payment_method_domains](/api/payment_method_domains/create)

[POST/v1/payment_method_domains/:id](/api/payment_method_domains/update)

[GET/v1/payment_method_domains/:id](/api/payment_method_domains/retrieve)

[GET/v1/payment_method_domains](/api/payment_method_domains/list)

[POST/v1/payment_method_domains/:id/validate](/api/payment_method_domains/validate)

Show

# Bank Accounts

[Bank Accounts](/api/customer_bank_accounts)

These bank accounts are payment methods on Customer objects.

On the other hand External Accounts are transfer destinations on Account objects for Custom accounts. They can be bank accounts or debit cards as well, and are documented in the links above.

[External Accounts](/api#external_accounts)

[Custom accounts](/connect/custom-accounts)

Related guide: Bank debits and transfers

[Bank debits and transfers](/payments/bank-debits-transfers)

[POST/v1/customers/:id/sources](/api/customer_bank_accounts/create)

[POST/v1/customers/:id/sources/:id](/api/customer_bank_accounts/update)

[GET/v1/customers/:id/bank_accounts/:id](/api/customer_bank_accounts/retrieve)

[GET/v1/customers/:id/bank_accounts](/api/customer_bank_accounts/list)

[DELETE/v1/customers/:id/sources/:id](/api/customer_bank_accounts/delete)

[POST/v1/customers/:id/sources/:id/verify](/api/customer_bank_accounts/verify)

Show

# Cash Balance

[Cash Balance](/api/cash_balance)

A customer’s Cash balance represents real funds. Customers can add funds to their cash balance by sending a bank transfer. These funds can be used for payment and can eventually be paid out to your bank account.

[POST/v1/customers/:id/cash_balance](/api/cash_balance/update)

[GET/v1/customers/:id/cash_balance](/api/cash_balance/retrieve)

Show

# Cash Balance Transaction

[Cash Balance Transaction](/api/cash_balance_transactions)

Customers with certain payments enabled have a cash balance, representing funds that were paid by the customer to a merchant, but have not yet been allocated to a payment. Cash Balance Transactions represent when funds are moved into or out of this balance. This includes funding by the customer, allocation to payments, and refunds to the customer.

[GET/v1/customers/:id/cash_balance_transactions/:id](/api/cash_balance_transactions/retrieve)

[GET/v1/customers/:id/cash_balance_transactions](/api/cash_balance_transactions/list)

[POST/v1/test_helpers/customers/:id/fund_cash_balance](/api/cash_balance_transactions/fund_cash_balance)

Show

# Cards

[Cards](/api/cards)

You can store multiple cards on a customer in order to charge the customer later. You can also store multiple debit cards on a recipient in order to transfer to those cards later.

Related guide: Card payments with Sources

[Card payments with Sources](/sources/cards)

[POST/v1/customers/:id/sources](/api/cards/create)

[POST/v1/customers/:id/sources/:id](/api/cards/update)

[GET/v1/customers/:id/cards/:id](/api/cards/retrieve)

[GET/v1/customers/:id/cards](/api/cards/list)

[DELETE/v1/customers/:id/sources/:id](/api/cards/delete)

Show

# SourcesDeprecated

[Sources](/api/sources)

Source objects allow you to accept a variety of payment methods. They represent a customer’s payment instrument, and can be used with the Stripe API just like a Card object: once chargeable, they can be charged, or can be attached to customers.

Stripe doesn’t recommend using the deprecated Sources API. We recommend that you adopt the PaymentMethods API. This newer API provides access to our latest features and payment method types.

[Sources API](/api/sources)

[PaymentMethods API](/api/payment_methods)

Related guides: Sources API and Sources & Customers.

[Sources API](/sources)

[Sources & Customers](/sources/customers)

[POST/v1/sources](/api/sources/create)

[POST/v1/sources/:id](/api/sources/update)

[GET/v1/sources/:id](/api/sources/retrieve)

[POST/v1/customers/:id/sources](/api/sources/attach)

[DELETE/v1/customers/:id/sources/:id](/api/sources/detach)

Show

# Products

[Products](/api/products)

Products describe the specific goods or services you offer to your customers. For example, you might offer a Standard and Premium version of your goods or service; each version would be a separate Product. They can be used in conjunction with Prices to configure pricing in Payment Links, Checkout, and Subscriptions.

[Prices](#prices)

Related guides: Set up a subscription, share a Payment Link, accept payments with Checkout, and more about Products and Prices

[Set up a subscription](/billing/subscriptions/set-up-subscription)

[share a Payment Link](/payment-links)

[accept payments with Checkout](/payments/accept-a-payment#create-product-prices-upfront)

[Products and Prices](/products-prices/overview)

[POST/v1/products](/api/products/create)

[POST/v1/products/:id](/api/products/update)

[GET/v1/products/:id](/api/products/retrieve)

[GET/v1/products](/api/products/list)

[DELETE/v1/products/:id](/api/products/delete)

[GET/v1/products/search](/api/products/search)

Show

# Prices

[Prices](/api/prices)

Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products. Products help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.

[Products](#products)

For example, you might have a single “gold” product that has prices for $10/month, $100/year, and €9 once.

Related guides: Set up a subscription, create an invoice, and more about products and prices.

[Set up a subscription](/billing/subscriptions/set-up-subscription)

[create an invoice](/billing/invoices/create)

[products and prices](/products-prices/overview)

[POST/v1/prices](/api/prices/create)

[POST/v1/prices/:id](/api/prices/update)

[GET/v1/prices/:id](/api/prices/retrieve)

[GET/v1/prices](/api/prices/list)

[GET/v1/prices/search](/api/prices/search)

Show

# Coupons

[Coupons](/api/coupons)

A coupon contains information about a percent-off or amount-off discount you might want to apply to a customer. Coupons may be applied to subscriptions, invoices, checkout sessions, quotes, and more. Coupons do not work with conventional one-off charges or payment intents.

[subscriptions](#subscriptions)

[invoices](#invoices)

[checkout sessions](/api/checkout/sessions)

[quotes](#quotes)

[charges](#create_charge)

[payment intents](/api/payment_intents)

[POST/v1/coupons](/api/coupons/create)

[POST/v1/coupons/:id](/api/coupons/update)

[GET/v1/coupons/:id](/api/coupons/retrieve)

[GET/v1/coupons](/api/coupons/list)

[DELETE/v1/coupons/:id](/api/coupons/delete)

Show

# Promotion Code

[Promotion Code](/api/promotion_codes)

A Promotion Code represents a customer-redeemable code for a coupon. It can be used to create multiple codes for a single coupon.

[coupon](#coupons)

[POST/v1/promotion_codes](/api/promotion_codes/create)

[POST/v1/promotion_codes/:id](/api/promotion_codes/update)

[GET/v1/promotion_codes/:id](/api/promotion_codes/retrieve)

[GET/v1/promotion_codes](/api/promotion_codes/list)

Show

# Discounts

[Discounts](/api/discounts)

A discount represents the actual application of a coupon or promotion code. It contains information about when the discount began, when it will end, and what it is applied to.

[coupon](#coupons)

[promotion code](#promotion_codes)

Related guide: Applying discounts to subscriptions

[Applying discounts to subscriptions](/billing/subscriptions/discounts)

[DELETE/v1/customers/:id/discount](/api/discounts/delete)

[DELETE/v1/subscriptions/:id/discount](/api/discounts/subscription_delete)

Show

# Tax Code

[Tax Code](/api/tax_codes)

Tax codes classify goods and services for tax purposes.

[Tax codes](https://stripe.com/docs/tax/tax-categories)

[GET/v1/tax_codes/:id](/api/tax_codes/retrieve)

[GET/v1/tax_codes](/api/tax_codes/list)

Show

# Tax Rate

[Tax Rate](/api/tax_rates)

Tax rates can be applied to invoices, subscriptions and Checkout Sessions to collect tax.

[invoices](/billing/invoices/tax-rates)

[subscriptions](/billing/subscriptions/taxes)

[Checkout Sessions](/payments/checkout/set-up-a-subscription#tax-rates)

Related guide: Tax rates

[Tax rates](/billing/taxes/tax-rates)

[POST/v1/tax_rates](/api/tax_rates/create)

[POST/v1/tax_rates/:id](/api/tax_rates/update)

[GET/v1/tax_rates](/api/tax_rates/list)

[GET/v1/tax_rates/:id](/api/tax_rates/retrieve)

Show

# Shipping Rates

[Shipping Rates](/api/shipping_rates)

Shipping rates describe the price of shipping presented to your customers and applied to a purchase. For more information, see Charge for shipping.

[Charge for shipping](/payments/during-payment/charge-shipping)

[POST/v1/shipping_rates](/api/shipping_rates/create)

[POST/v1/shipping_rates/:id](/api/shipping_rates/update)

[GET/v1/shipping_rates/:id](/api/shipping_rates/retrieve)

[GET/v1/shipping_rates](/api/shipping_rates/list)

Show

# Sessions

[Sessions](/api/checkout/sessions)

A Checkout Session represents your customer’s session as they pay for one-time purchases or subscriptions through Checkout or Payment Links. We recommend creating a new Session each time your customer attempts to pay.

[Checkout](/payments/checkout)

[Payment Links](/payments/payment-links)

Once payment is successful, the Checkout Session will contain a reference to the Customer, and either the successful PaymentIntent or an active Subscription.

[Customer](/api/customers)

[PaymentIntent](/api/payment_intents)

[Subscription](/api/subscriptions)

You can create a Checkout Session on your server and redirect to its URL to begin Checkout.

Related guide: Checkout quickstart

[Checkout quickstart](/checkout/quickstart)

[POST/v1/checkout/sessions](/api/checkout/sessions/create)

[GET/v1/checkout/sessions/:id](/api/checkout/sessions/retrieve)

[GET/v1/checkout/sessions/:id/line_items](/api/checkout/sessions/line_items)

[GET/v1/checkout/sessions](/api/checkout/sessions/list)

[POST/v1/checkout/sessions/:id/expire](/api/checkout/sessions/expire)

Show

# Payment Link

[Payment Link](/api/payment_links/payment_links)

A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times.

When a customer opens a payment link it will open a new checkout session to render the payment page. You can use checkout session events to track payments through payment links.

[checkout session](/api/checkout/sessions)

[checkout session events](/api/events/types#event_types-checkout.session.completed)

Related guide: Payment Links API

[Payment Links API](/payment-links)

[POST/v1/payment_links](/api/payment_links/payment_links/create)

[POST/v1/payment_links/:id](/api/payment_links/payment_links/update)

[GET/v1/payment_links/:id/line_items](/api/payment_links/line_items)

[GET/v1/payment_links/:id](/api/payment_links/payment_links/retrieve)

[GET/v1/payment_links](/api/payment_links/payment_links/list)

Show

# Credit Note

[Credit Note](/api/credit_notes)

Issue a credit note to adjust an invoice’s amount after the invoice is finalized.

Related guide: Credit notes

[Credit notes](/billing/invoices/credit-notes)

[POST/v1/credit_notes](/api/credit_notes/create)

[POST/v1/credit_notes/:id](/api/credit_notes/update)

[GET/v1/credit_notes/:id/lines](/api/credit_notes/lines)

[GET/v1/credit_notes/preview/lines](/api/credit_notes/preview_lines)

[GET/v1/credit_notes/:id](/api/credit_notes/retrieve)

[GET/v1/credit_notes](/api/credit_notes/list)

[GET/v1/credit_notes/preview](/api/credit_notes/preview)

[POST/v1/credit_notes/:id/void](/api/credit_notes/void)

Show

# Customer Balance Transaction

[Customer Balance Transaction](/api/customer_balance_transactions)

Each customer has a Balance value, which denotes a debit or credit that’s automatically applied to their next invoice upon finalization. You may modify the value directly by using the update customer API, or by creating a Customer Balance Transaction, which increments or decrements the customer’s balance by the specified amount.

[Balance](/api/customers/object#customer_object-balance)

[update customer API](/api/customers/update)

Related guide: Customer balance

[Customer balance](/billing/customer/balance)

[POST/v1/customers/:id/balance_transactions](/api/customer_balance_transactions/create)

[POST/v1/customers/:id/balance_transactions/:id](/api/customer_balance_transactions/update)

[GET/v1/customers/:id/balance_transactions/:id](/api/customer_balance_transactions/retrieve)

[GET/v1/customers/:id/balance_transactions](/api/customer_balance_transactions/list)

Show

# Customer Portal Session

[Customer Portal Session](/api/customer_portal/sessions)

The Billing customer portal is a Stripe-hosted UI for subscription and billing management.

A portal configuration describes the functionality and features that you want to provide to your customers through the portal.

A portal session describes the instantiation of the customer portal for a particular customer. By visiting the session’s URL, the customer can manage their subscriptions and billing details. For security reasons, sessions are short-lived and will expire if the customer does not visit the URL. Create sessions on-demand when customers intend to manage their subscriptions and billing details.

Learn more in the integration guide.

[integration guide](/billing/subscriptions/integrating-customer-portal)

[POST/v1/billing_portal/sessions](/api/customer_portal/sessions/create)

Show

# Customer Portal Configuration

[Customer Portal Configuration](/api/customer_portal/configurations)

A portal configuration describes the functionality and behavior of a portal session.

[POST/v1/billing_portal/configurations](/api/customer_portal/configurations/create)

[POST/v1/billing_portal/configurations/:id](/api/customer_portal/configurations/update)

[GET/v1/billing_portal/configurations/:id](/api/customer_portal/configurations/retrieve)

[GET/v1/billing_portal/configurations](/api/customer_portal/configurations/list)

Show

# Invoices

[Invoices](/api/invoices)

Invoices are statements of amounts owed by a customer, and are either generated one-off, or generated periodically from a subscription.

They contain invoice items, and proration adjustments that may be caused by subscription upgrades/downgrades (if necessary).

[invoice items](#invoiceitems)

If your invoice is configured to be billed through automatic charges, Stripe automatically finalizes your invoice and attempts payment.  Note that finalizing the invoice, when automatic, does not happen immediately as the invoice is created. Stripe waits until one hour after the last webhook was successfully sent (or the last webhook timed out after failing). If you (and the platforms you may have connected to) have no webhooks configured, Stripe waits one hour after creation to finalize the invoice.

[when automatic](/invoicing/integration/automatic-advancement-collection)

If your invoice is configured to be billed by sending an email, then based on your email settings, Stripe will email the invoice to your customer and await payment. These emails can contain a link to a hosted page to pay the invoice.

[email settings](https://dashboard.stripe.com/account/billing/automatic)

Stripe applies any customer credit on the account before determining the amount due for the invoice (i.e., the amount that will be actually charged). If the amount due for the invoice is less than Stripe’s minimum allowed charge per currency, the invoice is automatically marked paid, and we add the amount due to the customer’s credit balance which is applied to the next invoice.

[minimum allowed charge per currency](/currencies#minimum-and-maximum-charge-amounts)

More details on the customer’s credit balance are here.

[here](/billing/customer/balance)

Related guide: Send invoices to customers

[Send invoices to customers](/billing/invoices/sending)

[POST/v1/invoices](/api/invoices/create)

[POST/v1/invoices/create_preview](/api/invoices/create_preview)

[POST/v1/invoices/:id](/api/invoices/update)

[POST/v1/invoices/:id/lines/:id](/api/invoices/update_line)

[GET/v1/invoices/:id](/api/invoices/retrieve)

[GET/v1/invoices/upcoming](/api/invoices/upcoming)

[GET/v1/invoices/:id/lines](/api/invoices/invoice_lines)

[GET/v1/invoices/upcoming/lines](/api/invoices/upcoming_invoice_lines)

[GET/v1/invoices](/api/invoices/list)

[DELETE/v1/invoices/:id](/api/invoices/delete)

[POST/v1/invoices/:id/finalize](/api/invoices/finalize)

[POST/v1/invoices/:id/mark_uncollectible](/api/invoices/mark_uncollectible)

[POST/v1/invoices/:id/pay](/api/invoices/pay)

[GET/v1/invoices/search](/api/invoices/search)

[POST/v1/invoices/:id/send](/api/invoices/send)

[POST/v1/invoices/:id/void](/api/invoices/void)

Show

# Invoice Items

[Invoice Items](/api/invoiceitems)

Invoice Items represent the component lines of an invoice. An invoice item is added to an invoice by creating or updating it with an invoice field, at which point it will be included as an invoice line item within invoice.lines.

[invoice](/api/invoices)

[an invoice line item](/api/invoices/line_item)

[invoice.lines](/api/invoices/object#invoice_object-lines)

Invoice Items can be created before you are ready to actually send the invoice. This can be particularly useful when combined with a subscription. Sometimes you want to add a charge or credit to a customer, but actually charge or credit the customer’s card only at the end of a regular billing cycle. This is useful for combining several charges (to minimize per-transaction fees), or for having Stripe tabulate your usage-based billing totals.

[subscription](/api/subscriptions)

Related guides: Integrate with the Invoicing API, Subscription Invoices.

[Integrate with the Invoicing API](/invoicing/integration)

[Subscription Invoices](/billing/invoices/subscription#adding-upcoming-invoice-items)

[POST/v1/invoiceitems](/api/invoiceitems/create)

[POST/v1/invoiceitems/:id](/api/invoiceitems/update)

[GET/v1/invoiceitems/:id](/api/invoiceitems/retrieve)

[GET/v1/invoiceitems](/api/invoiceitems/list)

[DELETE/v1/invoiceitems/:id](/api/invoiceitems/delete)

Show

# Meters

[Meters](/api/billing/meter)

A billing meter is a resource that allows you to track usage of a particular event. For example, you might create a billing meter to track the number of API calls made by a particular user. You can then attach the billing meter to a price and attach the price to a subscription to charge the user for the number of API calls they make.

[POST/v1/billing/meters](/api/billing/meter/create)

[POST/v1/billing/meters/:id](/api/billing/meter/update)

[GET/v1/billing/meters/:id](/api/billing/meter/retrieve)

[GET/v1/billing/meters](/api/billing/meter/list)

[POST/v1/billing/meters/:id/deactivate](/api/billing/meter/deactivate)

[POST/v1/billing/meters/:id/reactivate](/api/billing/meter/reactivate)

Show

# Meter Events

[Meter Events](/api/billing/meter-event)

A billing meter event represents a customer’s usage of a product. Meter events are used to bill a customer based on their usage. Meter events are associated with billing meters, which define the shape of the event’s payload and how those events are aggregated for billing.

[POST/v1/billing/meter_events](/api/billing/meter-event/create)

Show

# Meter Event Adjustment

[Meter Event Adjustment](/api/billing/meter-event_adjustment)

A billing meter event adjustment is a resource that allows you to cancel a meter event. For example, you might create a billing meter event adjustment to cancel a meter event that was created in error or attached to the wrong customer.

[POST/v1/billing/meter_event_adjustments](/api/billing/meter-event_adjustment/create)

Show

# Meter Event Summary

[Meter Event Summary](/api/billing/meter-event_summary)

A billing meter event summary represents an aggregated view of a customer’s billing meter events within a specified timeframe. It indicates how much usage was accrued by a customer for that period.

[GET/v1/billing/meters/:id/event_summaries](/api/billing/meter-event_summary/list)

Show

# Plans

[Plans](/api/plans)

You can now model subscriptions more flexibly using the Prices API. It replaces the Plans API and is backwards compatible to simplify your migration.

[Prices API](#prices)

Plans define the base price, currency, and billing cycle for recurring purchases of products. Products help you track inventory or provisioning, and plans help you track pricing. Different physical goods or levels of service should be represented by products, and pricing options should be represented by plans. This approach lets you change prices without having to change your provisioning scheme.

[Products](#products)

For example, you might have a single “gold” product that has plans for $10/month, $100/year, €9/month, and €90/year.

Related guides: Set up a subscription and more about products and prices.

[Set up a subscription](/billing/subscriptions/set-up-subscription)

[products and prices](/products-prices/overview)

[POST/v1/plans](/api/plans/create)

[POST/v1/plans/:id](/api/plans/update)

[GET/v1/plans/:id](/api/plans/retrieve)

[GET/v1/plans](/api/plans/list)

[DELETE/v1/plans/:id](/api/plans/delete)

Show

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
