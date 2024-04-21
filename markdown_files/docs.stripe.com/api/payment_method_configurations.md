htmlPayment Method Configurations | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Payment Method Configurations

PaymentMethodConfigurations control which payment methods are displayed to your customers when you don’t explicitly specify payment method types. You can have multiple configurations with different sets of payment methods for different scenarios.

There are two types of PaymentMethodConfigurations. Which is used depends on the charge type:

Direct configurations apply to payments created on your account, including Connect destination charges, Connect separate charges and transfers, and payments not involving Connect.

Child configurations apply to payments created on your connected accounts using direct charges, and charges with the on_behalf_of parameter.

Child configurations have a parent that sets default values and controls which settings connected accounts may override. You can specify a parent ID at payment time, and Stripe will automatically resolve the connected account’s associated child configuration. Parent configurations are managed in the dashboard and are not available in this API.

Related guides:

- [Payment Method Configurations API](/connect/payment-method-configurations)
- [Multiple configurations on dynamic payment methods](/payments/multiple-payment-method-configs)
- [Multiple configurations for your Connect accounts](/connect/multiple-payment-method-configurations)

Endpoints
# The Payment Method Configuration object

### Attributes

- idstringretrievable with publishable keyUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- activebooleanWhether the configuration can be used for new payments.


- applicationnullablestringFor child configs, the Connect application associated with the configuration.


- is_defaultbooleanThe default configuration is used whenever a payment method configuration is not specified.


- namestringThe configuration’s name.


- parentnullablestringFor child configs, the configuration’s parent configuration.



### More attributesExpand all

- acss_debitnullableobject
- affirmnullableobject
- afterpay_clearpaynullableobject
- alipaynullableobject
- amazon_paynullableobject
- apple_paynullableobject
- au_becs_debitnullableobject
- bacs_debitnullableobject
- bancontactnullableobject
- bliknullableobject
- boletonullableobject
- cardnullableobject
- cartes_bancairesnullableobject
- cashappnullableobject
- customer_balancenullableobject
- epsnullableobject
- fpxnullableobject
- giropaynullableobject
- google_paynullableobject
- grabpaynullableobject
- idealnullableobject
- jcbnullableobject
- klarnanullableobject
- konbininullableobject
- linknullableobject
- livemodeboolean
- oxxonullableobject
- p24nullableobject
- paynownullableobject
- paypalnullableobject
- promptpaynullableobject
- revolut_paynullableobject
- sepa_debitnullableobject
- sofortnullableobject
- swishnullableobject
- us_bank_accountnullableobject
- wechat_paynullableobject
- zipnullableobject

The Payment Method Configuration object`{  "id": "pmc_abcdef",  "object": "payment_method_configuration",  "acss_debit": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "active": true,  "affirm": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "afterpay_clearpay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "alipay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "apple_pay": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "bancontact": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "card": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "cartes_bancaires": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "eps": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "giropay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "google_pay": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "ideal": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "is_default": true,  "klarna": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "link": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "livemode": false,  "name": "Default",  "p24": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "sepa_debit": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "sofort": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "us_bank_account": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "wechat_pay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  }}`# Create a payment method configuration

Creates a payment method configuration

### Parameters

- namestringConfiguration name.


- parentstringConfiguration’s parent configuration. Specify to create a child configuration.



### More parametersExpand all

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

### Returns

Returns the payment method configuration object

POST/v1/payment_method_configurationsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_method_configurations \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d name="Buy Now Pay Laters"`Response`{  "id": "pmc_abcdef",  "object": "payment_method_configuration",  "acss_debit": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "active": true,  "affirm": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "afterpay_clearpay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "alipay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "apple_pay": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "bancontact": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "card": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "cartes_bancaires": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "eps": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "giropay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "google_pay": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "ideal": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "is_default": true,  "klarna": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "link": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "livemode": false,  "name": "Default",  "p24": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "sepa_debit": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "sofort": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "us_bank_account": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "wechat_pay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  }}`# Update payment method configuration

Update payment method configuration

### Parameters

- activebooleanWhether the configuration can be used for new payments.


- namestringConfiguration name.



### More parametersExpand all

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

### Returns

An object with the updated account payment method configuration

POST/v1/payment_method_configurations/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_method_configurations/pmc_abcdef \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "acss_debit[display_preference][preference]"=on`Response`{  "id": "pmc_abcdef",  "object": "payment_method_configuration",  "acss_debit": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "active": true,  "affirm": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "afterpay_clearpay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "alipay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "apple_pay": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "bancontact": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "card": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "cartes_bancaires": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "eps": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "giropay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "google_pay": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "ideal": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "is_default": true,  "klarna": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "link": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "livemode": false,  "name": "Default",  "p24": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "sepa_debit": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "sofort": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "us_bank_account": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "wechat_pay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  }}`# Retrieve payment method configuration

Retrieve payment method configuration

### Parameters

No parameters.

### Returns

A payment method configuration object.

GET/v1/payment_method_configurations/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/payment_method_configurations/pmc_abcdef \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "pmc_abcdef",  "object": "payment_method_configuration",  "acss_debit": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "active": true,  "affirm": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "afterpay_clearpay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "alipay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "apple_pay": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "bancontact": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "card": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "cartes_bancaires": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "eps": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "giropay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "google_pay": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "ideal": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "is_default": true,  "klarna": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "link": {    "available": true,    "display_preference": {      "overridable": null,      "preference": "on",      "value": "on"    }  },  "livemode": false,  "name": "Default",  "p24": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "sepa_debit": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "sofort": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "us_bank_account": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  },  "wechat_pay": {    "available": false,    "display_preference": {      "overridable": null,      "preference": "off",      "value": "off"    }  }}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`