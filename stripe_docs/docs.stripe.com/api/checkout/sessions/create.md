- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

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

# List all Checkout Sessions

[List all Checkout Sessions](/api/checkout/sessions/list)

Returns a list of Checkout Sessions.

- payment_intentstringOnly return the Checkout Session for the PaymentIntent specified.

Only return the Checkout Session for the PaymentIntent specified.

- subscriptionstringOnly return the Checkout Session for the subscription specified.

Only return the Checkout Session for the subscription specified.

- createdobject

- customerstring

- customer_detailsobject

- ending_beforestring

- limitinteger

- payment_linkstring

- starting_afterstring

- statusenum

A dictionary with a data property that contains an array of up to limit Checkout Sessions, starting after Checkout Session starting_after. Each entry in the array is a separate Checkout Session object. If no more Checkout Sessions are available, the resulting array will be empty.

# Expire a Session

[Expire a Session](/api/checkout/sessions/expire)

A Session can be expired when it is in one of these statuses: open

After it expires, a customer can’t complete a Session and customers loading the Session see a message saying the Session is expired.

No parameters.

Returns a Session object if the expiration succeeded. Returns an error if the Session has already expired or isn’t in an expireable state.
