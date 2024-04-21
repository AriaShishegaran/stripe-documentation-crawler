- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# The Payment Method Configuration object

[The Payment Method Configuration object](/api/payment_method_configurations/object)

- idstringretrievable with publishable keyUnique identifier for the object.

Unique identifier for the object.

- objectstringString representing the object’s type. Objects of the same type share the same value.

String representing the object’s type. Objects of the same type share the same value.

- activebooleanWhether the configuration can be used for new payments.

Whether the configuration can be used for new payments.

- applicationnullable stringFor child configs, the Connect application associated with the configuration.

For child configs, the Connect application associated with the configuration.

- is_defaultbooleanThe default configuration is used whenever a payment method configuration is not specified.

The default configuration is used whenever a payment method configuration is not specified.

- namestringThe configuration’s name.

The configuration’s name.

- parentnullable stringFor child configs, the configuration’s parent configuration.

For child configs, the configuration’s parent configuration.

- acss_debitnullable object

- affirmnullable object

- afterpay_clearpaynullable object

- alipaynullable object

- amazon_paynullable object

- apple_paynullable object

- au_becs_debitnullable object

- bacs_debitnullable object

- bancontactnullable object

- bliknullable object

- boletonullable object

- cardnullable object

- cartes_bancairesnullable object

- cashappnullable object

- customer_balancenullable object

- epsnullable object

- fpxnullable object

- giropaynullable object

- google_paynullable object

- grabpaynullable object

- idealnullable object

- jcbnullable object

- klarnanullable object

- konbininullable object

- linknullable object

- livemodeboolean

- oxxonullable object

- p24nullable object

- paynownullable object

- paypalnullable object

- promptpaynullable object

- revolut_paynullable object

- sepa_debitnullable object

- sofortnullable object

- swishnullable object

- us_bank_accountnullable object

- wechat_paynullable object

- zipnullable object

# Create a payment method configuration

[Create a payment method configuration](/api/payment_method_configurations/create)

Creates a payment method configuration

- namestringConfiguration name.

Configuration name.

- parentstringConfiguration’s parent configuration. Specify to create a child configuration.

Configuration’s parent configuration. Specify to create a child configuration.

- acss_debitobject

- affirmobject

- afterpay_clearpayobject

- alipayobject

- amazon_payobject

- apple_payobject

- apple_pay_laterobject

- au_becs_debitobject

- bacs_debitobject

- bancontactobject

- blikobject

- boletoobject

- cardobject

- cartes_bancairesobject

- cashappobject

- customer_balanceobject

- epsobject

- fpxobject

- giropayobject

- google_payobject

- grabpayobject

- idealobject

- jcbobject

- klarnaobject

- konbiniobject

- linkobject

- oxxoobject

- p24object

- paynowobject

- paypalobject

- promptpayobject

- revolut_payobject

- sepa_debitobject

- sofortobject

- swishobject

- us_bank_accountobject

- wechat_payobject

- zipobject

Returns the payment method configuration object

# Update payment method configuration

[Update payment method configuration](/api/payment_method_configurations/update)

Update payment method configuration

- activebooleanWhether the configuration can be used for new payments.

Whether the configuration can be used for new payments.

- namestringConfiguration name.

Configuration name.

- acss_debitobject

- affirmobject

- afterpay_clearpayobject

- alipayobject

- amazon_payobject

- apple_payobject

- apple_pay_laterobject

- au_becs_debitobject

- bacs_debitobject

- bancontactobject

- blikobject

- boletoobject

- cardobject

- cartes_bancairesobject

- cashappobject

- customer_balanceobject

- epsobject

- fpxobject

- giropayobject

- google_payobject

- grabpayobject

- idealobject

- jcbobject

- klarnaobject

- konbiniobject

- linkobject

- oxxoobject

- p24object

- paynowobject

- paypalobject

- promptpayobject

- revolut_payobject

- sepa_debitobject

- sofortobject

- swishobject

- us_bank_accountobject

- wechat_payobject

- zipobject

An object with the updated account payment method configuration

# Retrieve payment method configuration

[Retrieve payment method configuration](/api/payment_method_configurations/retrieve)

Retrieve payment method configuration

No parameters.

A payment method configuration object.

# List payment method configurations

[List payment method configurations](/api/payment_method_configurations/list)

List payment method configurations

No parameters.

- applicationstring

A list of all payment method configuration objects
