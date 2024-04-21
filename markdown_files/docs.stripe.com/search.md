htmlSearch | Stripe Documentation[Skip to content](#main-content)Search[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsearch)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsearch)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)
[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)API# Search

Look up objects in your Stripe data.Some top level API resources support retrieval with search API methods. You can use the search APIs to retrieve your Stripe objects in a flexible manner. Using search is a faster alternative to paginating through all resources. To create a search query, review the Search query language and reference the query fields of the resource:

- [Query fields for charges](/search#query-fields-for-charges)
- [Query fields for customers](/search#query-fields-for-customers)
- [Query fields for invoices](/search#query-fields-for-invoices)
- [Query fields for PaymentIntents](/search#query-fields-for-payment-intents)
- [Query fields for prices](/search#query-fields-for-prices)
- [Query fields for products](/search#query-fields-for-products)
- [Query fields for subscriptions](/search#query-fields-for-subscriptions)

## Examples

Here are some examples of what you can do with the Search charges API and Search PaymentIntents API:

### Charges metadata search

Look up charges matching a custom metadata value.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/charges/search \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  --data-urlencode query="metadata['key']:'value'"`### Charges last4 search

Look up charges matching the last 4 digits of the card used for the payment.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/charges/search \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  --data-urlencode query="payment_method_details.card.last4:4242"`### Customers email search

Look up customers matching an email.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/customers/search \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  --data-urlencode query="email:'sally@rocketrides.io'"`### Negation filter

Look up PaymentIntents not in the USD currency.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/payment_intents/search \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  --data-urlencode query="-currency:'usd'"`### Numeric filter

Filter invoice objects with a total greater than 1000.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/invoices/search \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d query="total>1000"`### Combining multiple filters

Look up charges matching a combination of metadata and currency.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/charges/search \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  --data-urlencode query="metadata['key']:'value' AND currency:'usd'"`## Search query language

### Query structure and terminology

A query clause consists of a field followed by an operator followed by a value:

clause`email:"amy@rocketrides.io"`field`email`operator`:`value`amy@rocketrides.io`You can combine multiple query clauses in a search by either separating them with a space, or using the AND or OR keywords (case insensitive). By default, the API combines clauses with AND logic. AND and OR operators are mutually exclusive.

The example query email:"amy@rocketrides.io" metadata["key"]:"value" matches records where both the email address is amy@rocketrides.io, and the metadata in the record includes key with a value of value.

### Creating a query which does not match a clause

You can negate query clauses using a - character. For example, the following search returns records that don’t match the email amy@rocketrides.io.

-email:"amy@rocketrides.io"

### Field types, substring matching, and numeric comparators

Every search field supports exact matching with a :. Certain fields such as email and name support substring matching. Certain other fields such as amount support numeric comparators like > and <.

Each field includes a type that defines the operations you can use in the field. For a full list of available fields, see supported query fields for each resource.

Using an unsupported operator, such as specifying greater than (>) on a string, returns an error.

typeoperatorstokenexact match (case insensitive)string

exact match, substring (case insensitive)

An exact match on a string type returns any record where that record contains all of the words from the query in the same order. For example the query name:"one two three" would match both a result with the name “one two three” and a result with the name “one two three four”.

numericexact match, greater than and less than### Quotes

You must use quotation marks around string values. Quotation marks are optional for numeric values. For example:

- `currency:"usd"`means quotes are required.
- `payment_method_details.card.last4:1234`means quotes are optional.

You can escape quotes inside of quotes with a backslash (\).

description:"the story called \"The Sky and the Sea.\""

### Metadata

You can perform searches on metadata that you’ve added to objects that support it.

Use the following format to construct a clause for a metadata search: metadata["<field>"]:"<value>".

The following clause demonstrates how to create a clause that queries for records with a donation ID of “asdf-jkl”: metadata["donation-id"]:"asdf-jkl".

You can query for the presence of a metadata key on an object. The following clause would match all records where donation-id is a metadata key. -metadata["donation-id"]:null

### Search Syntax

The following table lists the syntax that you can use to construct a query.

SyntaxUsageDescriptionExamples`:``field:value`Exact match operator (case insensitive)`currency:"eur"`returns records where the currency is exactly “EUR” in a case-insensitive comparison`AND`,`and``field:value1 AND field:value2`The query returns only records that match both clauses (case insensitive)`status:"active" AND amount:500``OR`,`or``field:value1 OR field:value2`The query returns records that match either of the clauses (case insensitive)`currency:"usd" OR currency:"eur"``-``-field:value`Returns records that don’t match the clause`-currency:"jpy"`returns records that aren’t in JPY`NULL`,`null``field:null`A special token used for field presence (case insensitive)`url:null`returns records where a URL field is empty`\``" \"\""`Escape quotes within quotes`description:"the story called \"The Sky and the Sea.\""``~``field~value`Substring match operator (substrings must be a minimum of 3 characters)`email~"amy"`returns matches for amy@rocketrides.io and xamy`>`,`<`,`=`- `field<value`
- `field>value`
- `field>=value`
- `field<=value`

Greater than/less than operators`amount>="10"`brings up objects where the amount is 10 or greater## Supported query fields for each resource

### Query fields for charges

FieldusageType (token, string, numeric)amount`amount>1000`numericbilling_details.address.postal_code`billing_details.address.postal_code:12345`tokencreated`created>1620310503`numericcurrency`currency:"usd"`tokencustomer`customer:"cus_123"`tokendisputed`disputed:"true"`tokenmetadata`metadata["key"]:"value"`tokenpayment_method_details.{{SOURCE}}.last4`payment_method_details.card.last4:1234`tokenpayment_method_details.{{SOURCE}}.exp_month`payment_method_details.card_present.exp_month:12`tokenpayment_method_details.{{SOURCE}}.exp_year`payment_method_details.interac_present.exp_year:2022`tokenpayment_method_details.{{SOURCE}}.brand`payment_method_details.card.brand:"visa"`tokenpayment_method_details.{{SOURCE}}.fingerprint`payment_method_details.card.fingerprint:"fp"`tokenrefunded`refunded:"true"`tokenstatus`status:"succeeded"`tokenFor SOURCE, use card, card_present, or interac_present. Use card for online charges, interac_present for Terminal card present charges for the Interac network, and card_present for other Terminal card present charges.

The disputed field accepts only the tokens “true” and “false”, indicating the presence of disputes.

refunded:"true" filters for fully-refunded charges, refunded:"false" filters for partially-refunded charges, and refunded:null filters for non-refunded charges.

### Query fields for customers

FieldusageType (token, string, numeric)created`created>1620310503`numericemail`email~"amyt"`stringmetadata`metadata["key"]:"value"`tokenname`name~"amy"`stringphone`phone:"+19999999999"`string### Query fields for invoices

FieldusageType (token, string, numeric)created`created>1620310503`numericcurrency`currency:"usd"`tokencustomer`customer:"cus_123"`tokenmetadata`metadata["key"]:"value"`tokennumber`number:"MYSHOP-123"`stringreceipt_number`receipt_number:"RECEIPT-123"`stringstatus`status:"open"`stringsubscription`subscription:"SUBS-123"`stringtotal`total>1000`numeric### Query fields for payment intents

FieldusageType (token, string, numeric)amount`amount>1000`numericcreated`created>1620310503`numericcurrency`currency:"usd"`tokencustomer`customer:"cus_123"`tokenmetadata`metadata["key"]:"value"`tokenstatus`status:"succeeded"`token### Query fields for prices

FieldusageType (token, string, numeric)active`active:"true"`tokencurrency`currency:"usd"`tokenlookup_key`lookup_key:"standard_monthly"`stringmetadata`metadata["key"]:"value"`tokenproduct`product:"prod_123"`stringtype`type:"recurring"`token### Query fields for products

FieldusageType (token, string, numeric)active`active:"true"`tokendescription`description~"t-shirts"`stringmetadata`metadata["key"]:"value"`tokenname`name~"amy"`stringshippable`shippable:"true"`tokenurl`url~"/dinosaur_swag"`string### Query fields for subscriptions

FieldusageType (token, string, numeric)created`created>1620310503`numericmetadata`metadata["key"]:"value"`tokenstatus`status:"active"`token## Limitations

### Minimum API version

The minimum supported API Version to use search is 2020-08-27. Read our API upgrades guide to learn more about upgrades. To use search without upgrading your account API version, you can override the API version on a single request by setting the Stripe-Version request header:

Command Line`-H "Stripe-Version: 2024-04-10"`Read our server-side libraries guide on how to override an API version when using a library.

### Data freshness

Don’t use search for read-after-write flows (for example, searching immediately after a charge is made) because the data won’t be immediately available to search. Under normal operating conditions, data is searchable in under 1 minute. Propagation of new or updated data could be delayed during an outage.

### Rate limits

We apply a rate limit of up to 20 read operations per second which applies for all search endpoints in both live mode and test mode. Live mode and test mode limits are separate. Keeping the rate limit in mind, for workloads where you need to run analytics on one or more API resource(s), Sigma is much more efficient. For workloads where you need to export a large portion of your API resource, our Data Pipeline product is more efficient.

### Regional availability

Search isn’t available to merchants in India.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Examples](#examples)[Search query language](#search-query-language)[Supported query fields for each resource](#supported-query-fields-for-each-resource)[Limitations](#limitations)Products Used[Payments](/payments)[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`