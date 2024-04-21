- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Create a PaymentMethod

[Create a PaymentMethod](/api/payment_methods/create)

Creates a PaymentMethod object. Read the Stripe.js reference to learn how to create PaymentMethods via Stripe.js.

[Stripe.js reference](/stripe-js/reference#stripe-create-payment-method)

Instead of creating a PaymentMethod directly, we recommend using the PaymentIntents API to accept a payment immediately or the SetupIntent API to collect payment method details ahead of a future payment.

[PaymentIntents](/payments/accept-a-payment)

[SetupIntent](/payments/save-and-reuse)

- typeenumRequiredThe type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.Possible enum valuesacss_debitPre-authorized debit payments are used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).affirmAffirm is a buy now, pay later payment method in the US.afterpay_clearpayAfterpay / Clearpay is a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.alipayAlipay is a digital wallet payment method used in China.amazon_payAmazon Pay is a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.au_becs_debitBECS Direct Debit is used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).bacs_debitBacs Direct Debit is used to debit UK bank accounts.bancontactBancontact is a bank redirect payment method used in Belgium.blikBLIK is a single-use payment method common in Poland.boletoBoleto is a voucher-based payment method used in Brazil.Show 55 more

The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.

Pre-authorized debit payments are used to debit Canadian bank accounts through the Automated Clearing Settlement System (ACSS).

[Pre-authorized debit payments](/payments/acss-debit)

Affirm is a buy now, pay later payment method in the US.

[Affirm](/payments/affirm)

Afterpay / Clearpay is a buy now, pay later payment method used in Australia, Canada, France, New Zealand, Spain, the UK, and the US.

[Afterpay / Clearpay](/payments/afterpay-clearpay)

Alipay is a digital wallet payment method used in China.

[Alipay](/payments/alipay)

Amazon Pay is a Wallet payment method that lets hundreds of millions of Amazon customers pay their way, every day.

[Amazon Pay](/payments/amazon-pay)

BECS Direct Debit is used to debit Australian bank accounts through the Bulk Electronic Clearing System (BECS).

[BECS Direct Debit](/payments/au-becs-debit)

Bacs Direct Debit is used to debit UK bank accounts.

[Bacs Direct Debit](/payments/payment-methods/bacs-debit)

Bancontact is a bank redirect payment method used in Belgium.

[Bancontact](/payments/bancontact)

BLIK is a single-use payment method common in Poland.

[BLIK](/payments/blik)

Boleto is a voucher-based payment method used in Brazil.

[Boleto](/payments/boleto)

- billing_detailsobjectBilling information associated with the PaymentMethod that may be used or required by particular types of payment methods.Show child parameters

Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- acss_debitobject

- affirmobject

- afterpay_clearpayobject

- alipayobject

- allow_redisplayenum

- amazon_payobject

- au_becs_debitobject

- bacs_debitobject

- bancontactobject

- blikobject

- boletoobject

- cardobject

- cashappobject

- customer_balanceobject

- epsobject

- fpxobject

- giropayobject

- grabpayobject

- idealobject

- interac_presentobjectPreview feature

- klarnaobject

- konbiniobject

- linkobject

- mobilepayobjectPreview feature

- oxxoobject

- p24object

- paynowobject

- paypalobject

- pixobject

- promptpayobject

- radar_optionsobject

- revolut_payobject

- sepa_debitobject

- sofortobject

- swishobject

- us_bank_accountobject

- wechat_payobject

- zipobject

Returns a PaymentMethod object.

# Update a PaymentMethod

[Update a PaymentMethod](/api/payment_methods/update)

Updates a PaymentMethod object. A PaymentMethod must be attached a customer to be updated.

- billing_detailsobjectBilling information associated with the PaymentMethod that may be used or required by particular types of payment methods.Show child parameters

Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.

- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.

[key-value pairs](/api/metadata)

- allow_redisplayenum

- cardobject

- linkobject

- us_bank_accountobject

Returns a PaymentMethod object.

# Retrieve a Customer's PaymentMethod

[Retrieve a Customer's PaymentMethod](/api/payment_methods/customer)

Retrieves a PaymentMethod object for a given Customer.

No parameters.

Returns a PaymentMethod object.

# Retrieve a PaymentMethod

[Retrieve a PaymentMethod](/api/payment_methods/retrieve)

Retrieves a PaymentMethod object attached to the StripeAccount. To retrieve a payment method attached to a Customer, you should use Retrieve a Customer’s PaymentMethods

[Retrieve a Customer’s PaymentMethods](/api/payment_methods/customer)

No parameters.

Returns a PaymentMethod object.

# List a Customer's PaymentMethods

[List a Customer's PaymentMethods](/api/payment_methods/customer_list)

Returns a list of PaymentMethods for a given Customer

- typeenumAn optional filter on the list, based on the object type field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.

An optional filter on the list, based on the object type field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.

- allow_redisplayenum

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit PaymentMethods of type type, starting after PaymentMethods starting_after. Each entry in the array is a separate PaymentMethod object. If no more PaymentMethods are available, the resulting array will be empty.
