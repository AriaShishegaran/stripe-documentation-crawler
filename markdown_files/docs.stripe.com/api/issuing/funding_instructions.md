htmlFunding Instructions | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Funding Instructions

Funding Instructions contain reusable bank account and routing information. Push funds to these addresses via bank transfer to top up Issuing Balances.

Endpoints
# The Funding Instruction object

### Attributes

- bank_transferobjectDetails to display instructions for initiating a bank transfer

Show child attributes
- currencystringThree-letter ISO currency code, in lowercase. Must be a supported currency.


- funding_typeenumThe funding_type of the returned instructions

Possible enum values`bank_transfer`Use a bank_transfer hash to define the bank transfer type



### More attributesExpand all

- objectstring
- livemodeboolean

The Funding Instruction object`{  "object": "funding_instructions",  "bank_transfer": {    "country": "DE",    "financial_addresses": [      {        "iban": {          "account_holder_name": "Stripe Technology Europe Limited",          "bic": "SXPYDEHH",          "country": "DE",          "iban": "DE00000000000000000001"        },        "supported_networks": [          "sepa"        ],        "type": "iban"      }    ],    "type": "eu_bank_transfer"  },  "currency": "eur",  "funding_type": "bank_transfer",  "livemode": false}`# Create funding instructions

Create or retrieve funding instructions for an Issuing balance. If funding instructions don’t yet exist for the account, we’ll create new funding instructions. If we’ve already created funding instructions for the account, the same we’ll retrieve the same funding instructions. In other words, we’ll return the same funding instructions each time.

### Parameters

- bank_transferobjectRequiredAdditional parameters for bank_transfer funding types

Show child parameters
- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.


- funding_typeenumRequiredThe funding_type to get the instructions for.

Possible enum values`bank_transfer`Use a bank_transfer hash to define the bank transfer type



### Returns

Returns funding instructions for an Issuing balance

POST/v1/issuing/funding_instructionscURL[](#)[](#)`curl https://api.stripe.com/v1/issuing/funding_instructions \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "bank_transfer[type]"=eu_bank_transfer \  -d currency=eur \  -d funding_type=bank_transfer`Response`{  "object": "funding_instructions",  "bank_transfer": {    "country": "DE",    "financial_addresses": [      {        "iban": {          "account_holder_name": "Stripe Technology Europe Limited",          "bic": "SXPYDEHH",          "country": "DE",          "iban": "DE00000000000000000001"        },        "supported_networks": [          "sepa"        ],        "type": "iban"      }    ],    "type": "eu_bank_transfer"  },  "currency": "eur",  "funding_type": "bank_transfer",  "livemode": false}`# List all funding instructions

Retrieve all applicable funding instructions for an Issuing balance.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

Returns all funding instructions for an Issuing balance

GET/v1/issuing/funding_instructionscURL[](#)[](#)`curl -G https://api.stripe.com/v1/issuing/funding_instructions \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/issuing/funding_instructions",  "has_more": false,  "data": [    {      "object": "funding_instructions",      "bank_transfer": {        "country": "DE",        "financial_addresses": [          {            "iban": {              "account_holder_name": "Stripe Technology Europe Limited",              "bic": "SXPYDEHH",              "country": "DE",              "iban": "DE00000000000000000001"            },            "supported_networks": [              "sepa"            ],            "type": "iban"          }        ],        "type": "eu_bank_transfer"      },      "currency": "eur",      "funding_type": "bank_transfer",      "livemode": false    }  ]}`# Simulate a top upTest helper

Simulates an external bank transfer and adds funds to an Issuing balance. This method can only be called in test mode.

### Parameters

- amountintegerRequiredThe amount to top up


- currencyenumRequiredThe currency to top up



### Returns

Returns testmode funding instructions for an Issuing balance

POST/v1/test_helpers/issuing/fund_balancecURL[](#)[](#)`curl https://api.stripe.com/v1/test_helpers/issuing/fund_balance \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=4242 \  -d currency=eur`Response`{  "object": "funding_instructions",  "bank_transfer": {    "country": "DE",    "financial_addresses": [      {        "iban": {          "account_holder_name": "Stripe Technology Europe Limited",          "bic": "SXPYDEHH",          "country": "DE",          "iban": "DE00000000000000000001"        },        "supported_networks": [          "sepa"        ],        "type": "iban"      }    ],    "type": "eu_bank_transfer"  },  "currency": "eur",  "funding_type": "bank_transfer",  "livemode": false}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`