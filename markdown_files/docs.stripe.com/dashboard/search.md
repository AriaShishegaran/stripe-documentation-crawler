htmlPerform searches in the Dashboard | Stripe Documentation[Skip to content](#main-content)Search in the Dashboard[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdashboard%2Fsearch)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdashboard%2Fsearch)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)[Data](#)
[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Data](/docs/stripe-data)# Perform searches in the Dashboard

Use the Dashboard to search for payments, customers, and more.Use the Dashboard’s built-in search feature to find important resources and navigate across different Stripe resources. When you perform a search, the top results appear immediately. View all of the matches by clicking Show all results or by pressing Enter. From the resulting groups of search results, click View all to see an expanded display with column headings, some of which provide sorting options.

### Commonly searched resources

![Dashboard's search suggested filters](https://b.stripecdn.com/docs-statics-srv/assets/dashboard-search.bc1d683e4a7eca1a760873ab03b03aae.png)

Use suggested filters when searching

## Get started

### Advanced searches

Stripe Sigma makes all of your business data available as an interactive SQL environment in the Dashboard. You can write queries for it to perform highly advanced searches and generate customized reports.

Use different pieces of information as search terms:

- The last four digits of a card (4242).
- The payment method type (iDEAL).
- The business name of a connected Stripe account (Rocketship).
- The email receipt number (1817-9523).

For searches that require dates, you can use different formats, like 08/22, 2020-07-12, or last week. Use object identifiers (dispute ID) to take you directly to the object you’re looking for. No additional context is necessary for most searches. The Dashboard automatically looks for the most relevant information based on your search query. You can make use of search filters and operators for more granular control.

## Search filters and operators

By default, the Dashboard looks for values that match your search term in the most logical fields within objects. (For example, it’ll look for an email address in the email field or an object description.) You can use filters and operators to further refine your searches. The more terms you provide in your search query, the fewer the number of results.

FiltersOperatorsUse filters to limit your search terms so that they only apply to specific fields within applicable objects. Preface a search term with one of these filters. If your search term must include a space, wrap it in quotation marks (name:"John Doe"). Many fields are shared across different objects. For instance, the amount field applies to payments, invoices, payouts, and so on.

FilterDescriptionExample`amount:`The amount of an object. For decimal currencies, use a decimal point for both currency units (for example, dollars and cents).amount:149.99`brand:`The brand of card associated with an object.brand:visa`country:`The two-letter[ISO code](https://en.wikipedia.org/wiki/ISO_3166-1)representing the country associated with an object.country:GB`created:`The date an object was created (identical to`date`).created:2020/07/12`currency:`The three-letter[ISO code](https://en.wikipedia.org/wiki/ISO_4217)representing the currency of an object.currency:EUR`date:`The date an object was created (identical to`created`).date:yesterday`email:`The email (either full address or part of one) of an object.email:jenny.rosen@example.com`exp:`The expiration date of the card associated with an object.exp:08/22`flow:`The type of[flow for customer action](/sources#flow-for-customer-action)that applies to a[Sources](/sources)payment.flow:redirect`last4:`The last four digits of the card associated with an object.last4:4080`metadata:`[Metadata](/api#metadata)value on a supported object. Additional[search options](#metadata-searches)for metadata are also available.metadata:555-5555`name:`The cardholder or customer name associated with an object.name:jenny`number:`The unique number identifying an invoice.number:06b2b1a642-0023`postal:`The ZIP or postal code associated with an object.postal:12345`receipt:`The receipt number used in a payment or refund email receipt.receipt:3330-2392`risk_level:`The[risk level](/radar/risk-evaluation)of a payment determined by[Radar](/radar).risk_level:elevated`status:`The status of an object.status:canceled`type:`The type of[PaymentMethod](/payments/payment-methods)or[Source](/sources)used to create a payment.type:ideal`usage:`The[usage](/sources#single-use-or-reusable)availability of a[Sources](/sources)payment method.usage:single_use`zip:`The ZIP or postal code associated with an object.zip:12345### Combine and negate search terms

Use more than one search term to narrow down your search and reduce the number of results. You can also negate any search filter with a hyphen (-) so that matches for it aren’t included.

ExampleDescription`last4:4242 exp:08/22`The last four digits of the card are`4242`and expiration date is`08/22`.`last4:4242 -exp:08/22`The last four digits of the card are`4242`and expiration date isnot`08/22`.`type:ideal status:canceled`iDEAL payments where the source has been canceled and not used to complete a payment.To search for an entire phrase, use quotation marks. For example, “Stripe Shop” provides matches for that full phrase, but Stripe Shop searches the words Stripe and Shop separately.

### Metadata searches

You can search for metadata that you added to objects that support it. Searches automatically include metadata values for any text that doesn’t use a filter. Use the metadata: filter to only look up metadata values. To search for a specific metadata key-value pair, use the metadata key name as a filter, such as order_id:xyn712.

## Search across accounts in an organization

After you add multiple Stripe accounts to an organization, users can search across all accounts they have access to within that organization.

By default, searches display results from all accounts you have access to in the organization. To narrow your search to within your current account, select the account dropdown to the right of the search bar in the Dashboard.

![Search across the organization or current account.](https://b.stripecdn.com/docs-statics-srv/assets/org-search.ad9ff17e4e187a926dd0d12f0dcecda9.png)

Search across the organization by default or narrow your searches to your current account.

When you search within an organization, both the dropdown search results and the full results page display the associated account for each result.

![Organization-wide search results](https://b.stripecdn.com/docs-statics-srv/assets/org-search-results-dropdown.f05bff944bdf38d6ed06e4a4d2e7953a.png)

Search results in the dropdown display the associated account for each result.

## Best practices

Many searches can be performed with a single search term. Use something that would be fairly specific, such as a name or email address. If you’re seeing too few results, make the search term less specific. If there are too many results, include additional terms, one at a time.

Use a wider range of values when using dates or amounts as search terms. Currency conversions and time zone differences between you and your customer are a common source of confusion when looking up information about a payment. In these cases, additional search terms or even different ones altogether can help.

Bookmark searchesAs search terms are included in the URL, you can bookmark the search or share it with other team members as you would any other web page.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Get started](#get-started)[Search filters and operators](#search-filters-operators)[Search across accounts in an organization](#org-search)[Best practices](#best-practices)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`