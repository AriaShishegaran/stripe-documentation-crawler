htmlRules reference | Stripe Documentation[Skip to content](#main-content)Reference[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fradar%2Frules%2Freference)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fradar%2Frules%2Freference)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)
[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Radar](/radar)·[Home](/docs)[Get started](/docs/get-started)[Protect against fraud](/docs/radar)[Rules](/docs/radar/rules)# Rules reference

Learn more about the structure of rules and the order in which Radar processes them.### Using rules with Connect

To understand how Radar works with Stripe Connect, see Using Radar with Connect.

Before creating a rule, you need to understand how they’re processed and what payment attributes you can use to set evaluation criteria. The Stripe machine-learning fraud systems can block many fraudulent payments for you, but you can also set up rules that are unique to your business using the supported attributes.

## Rule processing and ordering

The action a rule takes determines the order in which it’s processed. Radar evaluates each payment against the rules you create and rules have the following order of priority:

1. Request 3DS: Rules that when used with the[Payment Intents API](/payments/payment-intents)or[Checkout](/payments/checkout),requestthe issuer to do[3D Secure authentication](/payments/3d-secure)if supported. Radar evaluates these before any block, review, or allow rules.
2. Allow: Rules thatallowa payment to be processed. Payments that fall under allow rules aren’t evaluated against any block or review rules.
3. Block: Rules thatblocka payment and reject it. Blocked payments aren’t evaluated against any review rules.
4. Review: Rules that allow payments to be processed but then place them inreview.

If a payment matches the criteria for a rule, Radar takes the appropriate action and the payment isn’t evaluated any further. If a payment matches an allow rule, it’s processed normally–no block or review rules are subsequently evaluated, even if the payment would also meet their criteria. An example set of rules might be as follows:

- Allowpayments less than`$10`
- Allowpayments made within the US and with a risk level of`normal`
- Blockpayments where the risk level is`high`
- Blockpayments`greater than $1,000`
- Reviewpayments made with a card issued`outside the US`

Using the rules above, all payments less than 10 USD would be processed, regardless of their risk level or where the card was issued. This is because the first rule allows the payment, so no further rules are evaluated. Similarly, a 1,500 payment USD made within the US with a normal risk level would also be allowed, despite the rule to block payments over 1,000 USD. This is because of the second rule in the list, allowing payments made within the US and a normal risk level. When a particular rule is triggered, no further rules are evaluated.

## Rule structure

The rule structure has two components—the action it should take and the condition to evaluate:

{action} if {condition}

Together they are referred to as the predicate. In practice, a rule to block all payments over 1,000 USD would appear as:

Block if :amount_in_usd: > 1000.00

- Theactionis`Block`
- Theconditionis`:amount_in_usd: > 1000.00`

### Actions

A rule can perform one of four actions with a payment that meets its criteria, processed in this specific order.

Request 3D SecureWhen used with the Payment Intents API, this rule determines if Stripe requests the issuer to attempt 3D Secure authentication. Requesting 3DS alone doesn’t block all possible 3D Secure outcomes. Whether or not there are matches on this rule, we evaluate rules for allow, block, and review afterward.

AllowThis rule determines when to always allow a payment that meets certain criteria, regardless of Stripe’s evaluation or any other matching rules. When a payment matches the criteria in an allow rule, Stripe processes it normally and it’s not subject to further rules evaluation. Even if Stripe proceeds with a payment, the card issuer may still decline it.

BlockBlock rules specify that Stripe should always block a payment. If a payment matches the criteria in a block rule, Stripe rejects it and it’s not subject to further rules evaluation.

ReviewYou might want to allow certain types of payments but also have the option to examine them more closely. With review rules, you can place payments in review. This is especially useful for payments that don’t fit common patterns, such as larger payments or payments from a country that you don’t often ship to. Stripe still processes these payments and charges the customer, but you have an additional opportunity to review the order and check for signs of fraud.

### Conditions

If a payment matches a rule’s condition, the corresponding action is taken. A basic condition is, itself, made up of three parts:

[attribute] [operator] [value]

- Attribute: The attribute of a payment (for example, theamountortype of card)
- Operator: The arithmetic that compares the attribute to the value (for example,greater thanornot equal to)
- Value: The criteria you want to use (for example,`100.00`or`debit`)

Combining both the action and condition together, the structure of a rule is:

{action} if {[attribute] [operator] [value]}

Four types of conditions exist, depending on the attribute type:

- `[string_attribute] [operator] [string_value]`
- `[country_attribute] [operator] [country_value]`
- `[numeric_attribute] [operator] [numeric_value]`
- `[boolean_attribute]`

You can also use certain attributes as a corresponding value within a condition. For instance, you can create a rule to block payments where the issuing country of the card doesn’t match with the country where the payment was made, using the following attribute and value:

Block if :card_country: != :ip_country:

For a list of all possible conditions, refer to the supported attributes.

String attributes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

These contain any combination of characters. String attributes and values most commonly represent a piece of text, such as a card’s brand (for example, visa, amex) or risk level (for example, elevated). You can use these in rules to allow payments only from a particular country, or block payments made with prepaid cards.

Metadata attributes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

These attributes are derived from the metadata you’ve attached to your payments. Metadata attributes can operate as either strings or numbers. When used as strings, metadata attributes are case-sensitive.

You can use these attributes when creating Stripe Radar rules, enabling you to write rules against any custom business attributes you have passed to Stripe in the metadata field attached to your payments.

Metadata attributes are written in the following structure:

::[metadata attribute name]:: [operator] [metadata_value]

For example, suppose we have payments with the following key-value data stored in the metadata field:

Metadata NameMetadata ValueCustomer Age22Item ID5A381DCategory IDgroceriesYou can write a rule to place payments that match the following criteria into review.

Review if ::Customer Age:: < 30

You can also write rules using both metadata attributes and other supported attributes mentioned in this document. For example, you can write a rule that only places a payment in review if the Item ID matches 5A381D and the payment amount exceeds 1,000 USD.

Review if ::Item ID:: = '5A381D' and :amount_in_usd: > 1000

Metadata attributes also support the IN operator to match against multiple values. For example, you can write a rule that places a payment in review if the Category ID is one of groceries, electronics, or clothing.

Review if ::Category ID:: IN ('groceries', 'electronics', 'clothing')

You can use the INCLUDES operator with rules for metadata attributes and other string attributes to match substrings. For example, you can write a rule that places a payment in review if the Item ID includes the string A381. This matches A381, 5A381D, A381D, 5A381, and so on.

Review if ::Item ID:: INCLUDES 'A381'

CautionMetadata attributes are case-sensitive when used as strings. Make sure that metadata values you specify in rules are exactly the same as the ones attached to your payments.

Metadata on Customer and Destination Objects

You can also access metadata on customer and destination objects (if those are used for a given payment). These attributes use the following structure:

::[customer|destination]:[metadata attribute name]:: [operator] [metadata_value]

For example, suppose you had a customer with the following metadata:

Metadata NameMetadata ValueTrustedtrueYou could write a rule that always allows payments if the customer’s Trusted metadata field is true.

Allow if ::customer:Trusted:: = 'true'

Or if you had a destination with the following metadata:

Metadata NameMetadata ValueCategorynewYou could write a rule that places a payment in review if the destination’s Category metadata field is new.

Review if ::destination:Category:: = 'new'

Country attributes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

These use two-letter country codes to represent a country, such as US for United States, GB for Great Britain, or AR for Argentina. Country attributes operate the same as string attributes, the only difference being that the value must be a country code.

State attributes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

These use ISO codes to represent the state or principal subdivision of a country, such as CA to represent California of the United States, ENG to represent England which is part of Great Britain, or L to represent La Pampa which is part of Argentina. We omit the two-letter country code from the state ISO code, so if you want to block transactions from California, your rule would compare the state attribute to CA.

Block if :ip_state: = 'CA'

State attributes operate the same as string attributes, the only difference being that the value must be an ISO code.

Numeric attributes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

As these contain only numbers, they support more operators than string attributes and values. A payment’s amount is one example of a numeric attribute. You can create a rule to perform an action if the amount is higher, lower, equal, or not equal to the amount you specify.

For numeric attributes that are counts over time windows, the count excludes the payment that you’re currently processing. For example, total_charges_per_customer_hourly represents the number of previous charge attempts from a given customer in the preceding hour. So, for the first charge attempt in a given hour for a customer, total_charges_per_customer_hourly has a value of 0. For a second charge attempt within the same hour, it has a value of 1, and so on.

Time-since-first-seen attributes also don’t take into account the payment you’re currently processing. For example, a payment without an email has a missing value for seconds_since_email_first_seen. So do payments with emails never seen before on your account (since we don’t include the payment currently being processed, this is effectively the same behavior as the first example). See below for more details about missing values. The seconds_since_email_first_seen field is only non-null after a new payment with a given email is processed.

Bounded numeric attributes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Bounded numeric attributes are similar to the numeric attributes described above. For example, they exclude the payment that you’re currently processing. The difference is that the available values for bounded numeric attributes are capped (or bounded) at a specific value.

As an example, take authorized_charges_per_email_hourly which represents the number of previous charges that were authorized for the email in the past hour on your account. For the sake of the example, let’s say it has a bound of 5. For the first charge attempt in the past hour with the email jenny.rosen@example.com the counter has a value of 0. Subsequent charge attempts in the same hour see higher counter values. After authorizing the 6th charge within the hour from jenny.rosen@example.com, the counter stops incrementing and stays at 5 despite actually having 6 charge attempts in the past hour.

If an attempt to increment the counter above the cap occurs, we exclude older values from consideration and replace them with newer values. For example, consider a counter with a cap of 3 that’s been filled up with 3 charges. One way to visualize the counter is by maintaining a list of timestamps representing arrival times of charges: [10, 20, 30] for instance. When a charge arrives at time 50, the counter now looks like [20, 30, 50].

Boolean attributes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

A Boolean attribute represents whether a particular attribute is true. Unlike string and numeric attributes, Boolean attributes have no operators or values. You can use a Boolean attribute to block payments that have been made with a disposable email address, or place payments in review that were made with an anonymous IP address.

Post-authorization attributes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

A post-authorization attribute (for example, :cvc_check:, :address_zip_check:, or :address_line1_check:) requires Stripe to exchange data with card issuers as part of the authorization process. The card issuer verifies this data against the information they have on file for the cardholder and checks for a match. Rules that use post-authorization attributes execute after rules that don’t use post-authorization attributes. (This won’t affect whether a charge is blocked or not, but may impact which rule blocks the charge.)

If you use a post-authorization attribute in a rule, your customer’s statement may temporarily show an authorization even if the charge is ultimately blocked—the authorization generally disappears after a few days.

Address (AVS) and CVC attributes have five possible values:

Attribute valueExplanation`pass`The data provided is correct.`fail`The data provided is incorrect.`unavailable`The customer’s card issuer won’t check the data provided. Not all card issuers or countries support address verification.`unchecked`The data was provided but hasn’t been checked yet. The customer’s card issuer will eventually check the data provided.`not_provided`The data wasn’t provided to Stripe.Some example rules:

- `Block if :address_line1_check: = 'fail'`
- `Block if :cvc_check: != 'pass'`
- `Block if :address_zip_check: in ('fail', 'not_provided')`

Requiring a strict pass on rules can be overly restrictive. For example, wallets usually don’t provide a CVC because they store tokenized card information. Therefore CVC checks, like 3D-Secure checks, aren’t available for payment methods such as Apple Pay. Stripe recommends using Radar’s Built-in rules, which consider these edge cases.

Supported attributes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Refer to the list of all supported attributes for a complete list of attributes you can apply to your rule definitions.

Converted amounts![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

When using amount_in_xyz, Stripe automatically determines the converted amount of any payment when checking if the amount matches your chosen criteria. For example, if you create a rule using amount_in_usd to block all payments greater than 1,000 USD, Stripe would block a payment of a lower nominal amount in a different currency (for example, 900 GBP) if its equivalent converted value exceeds 1,000 USD.

“Takes into account payments from 2020 onwards” in practice![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

The descriptions of some rule attributes include the phrase “takes into account payments from 2020 onwards”. This means that the rule would treat a card that last transacted with your business in 2019 the same as a card that’s new to your business. You should carefully consider what this means in the context of your business and rules as it could result in counterintuitive behavior. For example, if you create a rule to block high-value payments from new cards, you might end up blocking a good customer who hasn’t made a purchase since 2019.

“This attribute only includes live mode Customer objects that interacted with your account in the past <week, year>. This data updates at most every 72 hours.” in practice![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

The descriptions of some rule attributes include the sentences “This attribute only includes live mode Customer objects that interacted with your account in the past <week, year>. This data updates at most every 72 hours.” This means that live mode Customer objects that were created, charged, or updated on your account in the past week or year are included in these counts. However, the count doesn’t update immediately and might take up to 72 hours to propagate through the system, though often times these counters update sooner than 72 hours.

### Operators

A condition’s operator denotes the comparison between the payment’s attribute and the value you provide. Different operators are available, depending on the type of attribute being used.

OperatorStringMetadataCountryStateNumericDescriptionExample=✔︎✔︎✔︎✔︎✔︎Equal to`:card_country: = 'us'`!=✔︎✔︎✔︎✔︎✔︎Not equal to`:card_funding: != 'prepaid'`<✔︎Less than`:amount_in_gbp: < 10.00`>✔︎Greater than`:amount_in_usd: > 500.00`<=︎✔︎Less than or equal to`:amount_in_eur: <= 100.00`>=✔︎Greater than or equal to`:amount_in_cad: >= 10.00`IN✔✔︎✔✔︎✔︎Is in the group`:card_country: IN ('gb', 'ie')`INCLUDES✔✔︎✔✔Contains the string`:ip_address: INCLUDES '192.168'`LIKE✔✔︎✔✔Matches the given pattern. Use the wildcard character`%`to match zero or any number of letters, digits or symbols.`:email: LIKE 'fraud%@stripe.com'`### Lists

You can reference a group of values in your rules through lists. All list aliases referenced in rules must start with @. To construct a rule referencing a list, follow the structure:

{action} [attribute] in [list]

For example, say you have a list of card countries you’d like to block. You could write a rule using several OR clauses:

Block if :card_country: = 'CA' OR :card_country: = 'DE' OR :card_country: = 'AE'

You could also write a rule using an inline list:

Block if :card_country: IN ('CA', 'DE', 'AE')

You could also create a list of card countries you want to block, named card_countries_to_block. You can then add the countries of your choice to the list and reference that list in a rule:

Block if :card_country: in @card_countries_to_block

Referencing a list in a rule allows you to edit a large number of items in one place instead of maintaining many individual rules.

CautionEU merchants should be aware of the Geo-blocking Regulation and its prohibitions on blocking payments from customers based in EU member states. Learn more about this regulation.

### Missing attributes

Typical rule conditions refer to attributes set on every payment, such as :card_country: (which is set on every card-based charge) or a metadata attribute you always send with your payment requests. In some scenarios an attribute might be missing, for example:

- You have different checkout flows on your site, and some of them don’t collect customers’ email addresses


- You’ve only recently started using Stripe.js, and so :ip_country: is available on new payments, but not available on historical payments (which we search when previewing rules)


- For some of your payments, a bug in your integration fails to set an expected metadata key



How rule conditions evaluate missing attributes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Consider the rule Block if :email_domain: = 'definitelyfraud.com'.  If you didn’t collect the customer’s email address, the :email_domain: attribute would be missing, and—as you might expect—the rule condition would not match the payment.

Now consider the rule Review if :email_domain: != 'definitelysafe.com'.  If the :email_domain: attribute is missing, this rule also doesn’t match the payment. This result might seem a bit surprising, as a missing value is not the same as 'definitelysafe.com'. In this case, we interpret != 'definitelysafe.com' to mean “the attribute has some value other than 'definitelysafe.com',” which a missing attribute doesn’t satisfy.

More generally: any comparison (for example, =, !=, >, <) of a missing feature against another static value or feature (missing or present) always returns false.

Explicit handling with the`is_missing`function![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

If you want to explicitly check for the existence of an attribute or metadata attribute, use the is_missing function. Provide this function with the attribute or metadata key that may be missing.

For example, you could write a rule to match all payments where you don’t have access to a customer’s email address:

- `Review if is_missing(:email_domain:)`

Or you might write a rule to match all payments that have a certain metadata attribute set:

- `Review if !(is_missing(::foo::))`

You can also use the is_missing function in OR or AND conjunctions:

- `Review if is_missing(:email_domain:) OR :email_domain: IN ('yopmail.net', 'yandex.ru')`

### Complex conditions

You can build complex conditions by joining together basic conditions using the operators AND, OR, and NOT. You can also use their symbolic equivalents: &&, ||, and ! respectively.

Similar to programming languages such as C, Python, and SQL, Stripe supports standard operator precedence (order of operations). For instance, the complex condition:

{condition_X} OR NOT {condition_Y} AND {condition_Z}

is interpreted as:

{condition_X} OR ((NOT {condition_Y}) AND {condition_Z})

Sub-conditional grouping within complex conditions is also supported using parentheses. For instance, you can amend the prior example to explicitly change the evaluation order of sub-predicates:

({condition_X} OR (NOT {condition_Y})) AND {condition_Z}

{condition_X} OR NOT ({condition_Y} AND {condition_Z})

By using parentheses in different locations, each of these complex conditions lead to different results.

### Valid conditions

The following conditions are examples of correct use of attributes and a supported operator:

- `:card_brand: = 'amex'`
- `:card_country: != 'US'`
- `:amount_in_usd: >= 1000.00`
- `:is_anonymous_ip:`

### Invalid conditions

When creating a rule, Radar provides feedback if you attempt to use an invalid condition. For reference, the following are examples of invalid conditions, where the value for an attribute or the operator used isn’t supported:

- `:risk_level: < 'highest'`(string values can only make use of = or != operators)
- `:ip_country: = 'Canada'`(country values must be expressed in two-letter short code)
- `:amount_in_usd: >= 'one thousand dollars'`(numeric values must be expressed in numbers)
- `:is_anonymous_ip: = 'true'`(Boolean attributes are not used with operators or values)

### Velocity rules

Many supported attributes include invariants for different time scales (for example, the daily in total_charges_per_email_daily). These are called velocity rules.

Attributes are calculated as a rolling window, based on fixed seconds and not on a calendar. For example, daily means that the time between two charges in a rule attribute must be a maximum of 24 hours or 86400 seconds apart to match.

The attributes are defined as:

- `hourly`is 3600 seconds
- `daily`is 86400 seconds
- `weekly`is 604800 seconds
- `yearly`is 31536000 seconds

A common use case for these attributes is to reduce card testing or enumeration attack scenarios, as explained in the Radar 101 guide.

## See also

- [3DS Rule Examples](/radar/rules#request-3d-secure)
- [Continuous Fraud Management Guide](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data)
- [Query Disputes and Fraud Data](/stripe-data/query-disputes-and-fraud-data)
- [Radar 101 Guide](https://stripe.com/guides/radar-rules-101)
- [Rules Overview](/radar/rules)
- [Supported Attributes](/radar/rules/supported-attributes)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Rule processing and ordering](#rule-processing-and-ordering)[Rule structure](#rule-structure)[See also](#see-also)Related Guides[All supported rule attributes](/docs/radar/rules/supported-attributes)[3DS Authentication rules](/docs/radar/rules#request-3d-secure)[Radar 101 Guide](https://stripe.com/guides/radar-rules-101)Products Used[Radar](/radar)[Payments](/payments)[Checkout](/payments/checkout)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`