- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# The Session object

[The Session object](/api/checkout/sessions/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- client_reference_idnullable stringA unique string to reference the Checkout Session. This can be a customer ID, a cart ID, or similar, and can be used to reconcile the Session with your internal systems.

A unique string to reference the Checkout Session. This can be a customer ID, a cart ID, or similar, and can be used to reconcile the Session with your internal systems.

- currencynullable enumThree-letter ISO currency code, in lowercase. Must be a supported currency.

Three-letter ISO currency code, in lowercase. Must be a supported currency.

[ISO currency code](https://www.iso.org/iso-4217-currency-codes.html)

[supported currency](https://stripe.com/docs/currencies)

- customernullable stringExpandableThe ID of the customer for this Session. For Checkout Sessions in subscription mode or Checkout Sessions with customer_creation set as always in payment mode, Checkout will create a new customer object based on information provided during the payment flow unless an existing customer was provided when the Session was created.

The ID of the customer for this Session. For Checkout Sessions in subscription mode or Checkout Sessions with customer_creation set as always in payment mode, Checkout will create a new customer object based on information provided during the payment flow unless an existing customer was provided when the Session was created.

- customer_emailnullable stringIf provided, this value will be used when the Customer object is created. If not provided, customers will be asked to enter their email address. Use this parameter to prefill customer data if you already have an email on file. To access information about the customer once the payment flow is complete, use the customer attribute.

If provided, this value will be used when the Customer object is created. If not provided, customers will be asked to enter their email address. Use this parameter to prefill customer data if you already have an email on file. To access information about the customer once the payment flow is complete, use the customer attribute.

- line_itemsnullable objectExpandableThe line items purchased by the customer.Show child attributes

The line items purchased by the customer.

- metadatanullable objectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

[key-value pairs](/api/metadata)

- modeenumThe mode of the Checkout Session.Possible enum valuespaymentAccept one-time payments for cards, iDEAL, and more.setupSave payment details to charge your customers later.subscriptionUse Stripe Billing to set up fixed-price subscriptions.

The mode of the Checkout Session.

Accept one-time payments for cards, iDEAL, and more.

Save payment details to charge your customers later.

Use Stripe Billing to set up fixed-price subscriptions.

- payment_intentnullable stringExpandableThe ID of the PaymentIntent for Checkout Sessions in payment mode.

The ID of the PaymentIntent for Checkout Sessions in payment mode.

- payment_statusenumThe payment status of the Checkout Session, one of paid, unpaid, or no_payment_required. You can use this value to decide when to fulfill your customer’s order.Possible enum valuesno_payment_requiredThe payment is delayed to a future date, or the Checkout Session is in setup mode and doesn’t require a payment at this time.paidThe payment funds are available in your account.unpaidThe payment funds are not yet available in your account.

The payment status of the Checkout Session, one of paid, unpaid, or no_payment_required. You can use this value to decide when to fulfill your customer’s order.

The payment is delayed to a future date, or the Checkout Session is in setup mode and doesn’t require a payment at this time.

The payment funds are available in your account.

The payment funds are not yet available in your account.

- return_urlnullable stringApplies to Checkout Sessions with ui_mode: embedded. The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site.

Applies to Checkout Sessions with ui_mode: embedded. The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site.

- statusnullable enumThe status of the Checkout Session, one of open, complete, or expired.Possible enum valuescompleteThe checkout session is complete. Payment processing may still be in progressexpiredThe checkout session has expired. No further processing will occuropenThe checkout session is still in progress. Payment processing has not started

The status of the Checkout Session, one of open, complete, or expired.

The checkout session is complete. Payment processing may still be in progress

The checkout session has expired. No further processing will occur

The checkout session is still in progress. Payment processing has not started

- success_urlnullable stringThe URL the customer will be directed to after the payment or subscription creation is successful.

The URL the customer will be directed to after the payment or subscription creation is successful.

- urlnullable stringThe URL to the Checkout Session. Redirect customers to this URL to take them to Checkout. If you’re using Custom Domains, the URL will use your subdomain. Otherwise, it’ll use checkout.stripe.com. This value is only present when the session is active.

The URL to the Checkout Session. Redirect customers to this URL to take them to Checkout. If you’re using Custom Domains, the URL will use your subdomain. Otherwise, it’ll use checkout.stripe.com. This value is only present when the session is active.

[Custom Domains](/payments/checkout/custom-domains)

- objectstring

- after_expirationnullable object

- allow_promotion_codesnullable boolean

- amount_subtotalnullable integer

- amount_totalnullable integer

- automatic_taxobject

- billing_address_collectionnullable enum

- cancel_urlnullable string

- client_secretnullable string

- consentnullable object

- consent_collectionnullable object

- createdtimestamp

- currency_conversionnullable object

- custom_fieldsarray of objects

- custom_textobject

- customer_creationnullable enum

- customer_detailsnullable object

- expires_attimestamp

- invoicenullable stringExpandable

- invoice_creationnullable object

- livemodeboolean

- localenullable enum

- payment_linknullable stringExpandable

- payment_method_collectionnullable enum

- payment_method_configuration_detailsnullable object

- payment_method_optionsnullable object

- payment_method_typesarray of strings

- phone_number_collectionnullable object

- recovered_fromnullable string

- redirect_on_completionnullable enum

- saved_payment_method_optionsnullable object

- setup_intentnullable stringExpandable

- shipping_address_collectionnullable object

- shipping_costnullable object

- shipping_detailsnullable object

- shipping_optionsarray of objects

- submit_typenullable enum

- subscriptionnullable stringExpandable

- tax_id_collectionnullable object

- total_detailsnullable object

- ui_modenullable enum

# Create a Session

[Create a Session](/api/checkout/sessions/create)

Creates a Session object.

- client_reference_idstringA unique string to reference the Checkout Session. This can be a customer ID, a cart ID, or similar, and can be used to reconcile the session with your internal systems.

A unique string to reference the Checkout Session. This can be a customer ID, a cart ID, or similar, and can be used to reconcile the session with your internal systems.

- customerstringID of an existing Customer, if one exists. In payment mode, the customer’s most recently saved card payment method will be used to prefill the email, name, card details, and billing address on the Checkout page. In subscription mode, the customer’s default payment method will be used if it’s a card, otherwise the most recently saved card will be used. A valid billing address, billing name and billing email are required on the payment method for Checkout to prefill the customer’s card details.If the Customer already has a valid email set, the email will be prefilled and not editable in Checkout. If the Customer does not have a valid email, Checkout will set the email entered during the session on the Customer.If blank for Checkout Sessions in subscription mode or with customer_creation set as always in payment mode, Checkout will create a new Customer object based on information provided during the payment flow.You can set payment_intent_data.setup_future_usage to have Checkout automatically attach the payment method to the Customer you pass in for future reuse.

ID of an existing Customer, if one exists. In payment mode, the customer’s most recently saved card payment method will be used to prefill the email, name, card details, and billing address on the Checkout page. In subscription mode, the customer’s default payment method will be used if it’s a card, otherwise the most recently saved card will be used. A valid billing address, billing name and billing email are required on the payment method for Checkout to prefill the customer’s card details.

[default payment method](/api/customers/update#update_customer-invoice_settings-default_payment_method)

If the Customer already has a valid email set, the email will be prefilled and not editable in Checkout. If the Customer does not have a valid email, Checkout will set the email entered during the session on the Customer.

[email](/api/customers/object#customer_object-email)

If blank for Checkout Sessions in subscription mode or with customer_creation set as always in payment mode, Checkout will create a new Customer object based on information provided during the payment flow.

You can set payment_intent_data.setup_future_usage to have Checkout automatically attach the payment method to the Customer you pass in for future reuse.

[payment_intent_data.setup_future_usage](/api/checkout/sessions/create#create_checkout_session-payment_intent_data-setup_future_usage)

- customer_emailstringIf provided, this value will be used when the Customer object is created. If not provided, customers will be asked to enter their email address. Use this parameter to prefill customer data if you already have an email on file. To access information about the customer once a session is complete, use the customer field.

If provided, this value will be used when the Customer object is created. If not provided, customers will be asked to enter their email address. Use this parameter to prefill customer data if you already have an email on file. To access information about the customer once a session is complete, use the customer field.

- line_itemsarray of objectsRequired unless setup modeA list of items the customer is purchasing. Use this parameter to pass one-time or recurring Prices.For payment mode, there is a maximum of 100 line items, however it is recommended to consolidate line items if there are more than a few dozen.For subscription mode, there is a maximum of 20 line items with recurring Prices and 20 line items with one-time Prices. Line items with one-time Prices will be on the initial invoice only.Show child parameters

A list of items the customer is purchasing. Use this parameter to pass one-time or recurring Prices.

[Prices](/api/prices)

For payment mode, there is a maximum of 100 line items, however it is recommended to consolidate line items if there are more than a few dozen.

For subscription mode, there is a maximum of 20 line items with recurring Prices and 20 line items with one-time Prices. Line items with one-time Prices will be on the initial invoice only.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- modeenumRequiredThe mode of the Checkout Session. Pass subscription if the Checkout Session includes at least one recurring item.Possible enum valuespaymentAccept one-time payments for cards, iDEAL, and more.setupSave payment details to charge your customers later.subscriptionUse Stripe Billing to set up fixed-price subscriptions.

The mode of the Checkout Session. Pass subscription if the Checkout Session includes at least one recurring item.

Accept one-time payments for cards, iDEAL, and more.

Save payment details to charge your customers later.

Use Stripe Billing to set up fixed-price subscriptions.

- return_urlstringRequired conditionallyThe URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site. This parameter is required if ui_mode is embedded and redirect-based payment methods are enabled on the session.

The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method’s app or site. This parameter is required if ui_mode is embedded and redirect-based payment methods are enabled on the session.

- success_urlstringRequired conditionallyThe URL to which Stripe should send customers when payment or setup is complete. This parameter is not allowed if ui_mode is embedded. If you’d like to use information from the successful Checkout Session on your page, read the guide on customizing your success page.

The URL to which Stripe should send customers when payment or setup is complete. This parameter is not allowed if ui_mode is embedded. If you’d like to use information from the successful Checkout Session on your page, read the guide on customizing your success page.

[customizing your success page](/payments/checkout/custom-success-page)

- after_expirationobject

- allow_promotion_codesboolean

- automatic_taxobject

- billing_address_collectionenum

- cancel_urlstring

- consent_collectionobject

- currencyenumRequired conditionally

- custom_fieldsarray of objects

- custom_textobject

- customer_creationenum

- customer_updateobject

- discountsarray of objects

- expires_attimestamp

- invoice_creationobject

- localeenum

- payment_intent_dataobject

- payment_method_collectionenum

- payment_method_configurationstring

- payment_method_dataobject

- payment_method_optionsobject

- payment_method_typesarray of enums

- phone_number_collectionobject

- redirect_on_completionenum

- saved_payment_method_optionsobject

- setup_intent_dataobject

- shipping_address_collectionobject

- shipping_optionsarray of objects

- submit_typeenum

- subscription_dataobject

- tax_id_collectionobject

- ui_modeenum

Returns a Session object.

# Retrieve a Session

[Retrieve a Session](/api/checkout/sessions/retrieve)

Retrieves a Session object.

No parameters.

Returns a Session object.

# Retrieve a Checkout Session's line items

[Retrieve a Checkout Session's line items](/api/checkout/sessions/line_items)

When retrieving a Checkout Session, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.

No parameters.

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit Checkout Session line items, starting after Line Item starting_after. Each entry in the array is a separate Line Item object. If no more line items are available, the resulting array will be empty.
