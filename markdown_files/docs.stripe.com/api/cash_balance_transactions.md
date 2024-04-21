htmlCash Balance Transaction | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Cash Balance Transaction

Customers with certain payments enabled have a cash balance, representing funds that were paid by the customer to a merchant, but have not yet been allocated to a payment. Cash Balance Transactions represent when funds are moved into or out of this balance. This includes funding by the customer, allocation to payments, and refunds to the customer.

Endpoints
# The Cash Balance Transaction object

### Attributes

- idstringUnique identifier for the object.


- objectstringString representing the object’s type. Objects of the same type share the same value.


- adjusted_for_overdraftnullableobjectIf this is a type=adjusted_for_overdraft transaction, contains information about what caused the overdraft, which triggered this transaction.

Show child attributes
- applied_to_paymentnullableobjectIf this is a type=applied_to_payment transaction, contains information about how funds were applied.

Show child attributes
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.


- currencystringThree-letter ISO currency code, in lowercase. Must be a supported currency.


- customerstringExpandableThe customer whose available cash balance changed as a result of this transaction.


- ending_balanceintegerThe total available cash balance for the specified currency after this transaction was applied. Represented in the smallest currency unit.


- fundednullableobjectIf this is a type=funded transaction, contains information about the funding.

Show child attributes
- livemodebooleanHas the value true if the object exists in live mode or the value false if the object exists in test mode.


- net_amountintegerThe amount by which the cash balance changed, represented in the smallest currency unit. A positive value represents funds being added to the cash balance, a negative value represents funds being removed from the cash balance.


- refunded_from_paymentnullableobjectIf this is a type=refunded_from_payment transaction, contains information about the source of the refund.

Show child attributes
- transferred_to_balancenullableobjectIf this is a type=transferred_to_balance transaction, contains the balance transaction linked to the transfer.

Show child attributes
- typeenumThe type of the cash balance transaction. New types may be added in future. See Customer Balance to learn more about these types.

Possible enum values`adjusted_for_overdraft`A cash balance transaction type: adjusted_for_overdraft

`applied_to_payment`A cash balance transaction type: applied_to_payment

`funded`A cash balance transaction type: funded

`funding_reversed`A cash balance transaction type: funding_reversed

`refunded_from_payment`A cash balance transaction type: refunded_from_payment

`return_canceled`A cash balance transaction type: return_canceled

`return_initiated`A cash balance transaction type: return_initiated

`transferred_to_balance`A cash balance transaction type: transferred_to_balance

`unapplied_from_payment`A cash balance transaction type: unapplied_from_payment


- unapplied_from_paymentnullableobjectIf this is a type=unapplied_from_payment transaction, contains information about how funds were unapplied.

Show child attributes

The Cash Balance Transaction object`{  "id": "ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF",  "object": "customer_cash_balance_transaction",  "created": 1690829143,  "currency": "eur",  "customer": "cus_9s6XKzkNRiz8i3",  "ending_balance": 10000,  "funded": {    "bank_transfer": {      "eu_bank_transfer": {        "bic": "BANKDEAAXXX",        "iban_last4": "7089",        "sender_name": "Sample Business GmbH"      },      "reference": "Payment for Invoice 28278FC-155",      "type": "eu_bank_transfer"    }  },  "livemode": false,  "net_amount": 5000,  "type": "funded"}`# Retrieve a cash balance transaction

Retrieves a specific cash balance transaction, which updated the customer’s cash balance.

### Parameters

No parameters.

### Returns

Returns a cash balance transaction object if a valid identifier was provided.

GET/v1/customers/:id/cash_balance_transactions/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions/ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF",  "object": "customer_cash_balance_transaction",  "created": 1690829143,  "currency": "eur",  "customer": "cus_9s6XKzkNRiz8i3",  "ending_balance": 10000,  "funded": {    "bank_transfer": {      "eu_bank_transfer": {        "bic": "BANKDEAAXXX",        "iban_last4": "7089",        "sender_name": "Sample Business GmbH"      },      "reference": "Payment for Invoice 28278FC-155",      "type": "eu_bank_transfer"    }  },  "livemode": false,  "net_amount": 5000,  "type": "funded"}`# List cash balance transactions

Returns a list of transactions that modified the customer’s cash balance.

### Parameters

No parameters.

### More parametersExpand all

- ending_beforestring
- limitinteger
- starting_afterstring

### Returns

A dictionary with a data property that contains an array of up to limit cash balance transactions, starting after item starting_after. Each entry in the array is a separate cash balance transaction object. If no more items are available, the resulting array will be empty.

GET/v1/customers/:id/cash_balance_transactionsServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -G https://api.stripe.com/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d limit=3`Response`{  "object": "list",  "url": "/v1/customers/cus_9s6XKzkNRiz8i3/cash_balance_transactions",  "has_more": false,  "data": [    {      "id": "ccsbtxn_1Na16B2eZvKYlo2CUhyw3dsF",      "object": "customer_cash_balance_transaction",      "created": 1690829143,      "currency": "eur",      "customer": "cus_9s6XKzkNRiz8i3",      "ending_balance": 10000,      "funded": {        "bank_transfer": {          "eu_bank_transfer": {            "bic": "BANKDEAAXXX",            "iban_last4": "7089",            "sender_name": "Sample Business GmbH"          },          "reference": "Payment for Invoice 28278FC-155",          "type": "eu_bank_transfer"        }      },      "livemode": false,      "net_amount": 5000,      "type": "funded"    }    {...}    {...}  ],}`# Fund a test mode cash balanceTest helper

Create an incoming testmode bank transfer

### Parameters

- amountintegerRequiredAmount to be used for this test cash balance transaction. A positive integer representing how much to fund in the smallest currency unit (e.g., 100 cents to fund $1.00 or 100 to fund ¥100, a zero-decimal currency).


- currencyenumRequiredThree-letter ISO currency code, in lowercase. Must be a supported currency.



### More parametersExpand all

- referencestring

### Returns

Returns a specific cash balance transaction, which funded the customer’s cash balance.

POST/v1/test_helpers/customers/:id/fund_cash_balanceServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl https://api.stripe.com/v1/test_helpers/customers/cus_9s6XKzkNRiz8i3/fund_cash_balance \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d amount=5000 \  -d currency=eur`Response`{  "id": "ccsbtxn_1NlhIV2eZvKYlo2CKwRcXkii",  "object": "customer_cash_balance_transaction",  "created": 1693612963,  "currency": "eur",  "customer": "cus_9s6XKzkNRiz8i3",  "ending_balance": 10000,  "funded": {    "bank_transfer": {      "eu_bank_transfer": {        "bic": "BANKDEAAXXX",        "iban_last4": "7089",        "sender_name": "Sample Business GmbH"      },      "reference": "Payment for Invoice 28278FC-155",      "type": "eu_bank_transfer"    }  },  "livemode": false,  "net_amount": 5000,  "type": "funded"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`