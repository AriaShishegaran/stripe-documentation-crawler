htmlTax overrides | Stripe Documentation[Skip to content](#main-content)Tax overrides[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Ftax-overrides)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Ftax-overrides)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Calculate tax](/docs/tax/calculating)# Tax overridesBeta

Learn how to override tax behavior using Stripe Tax.Set up Stripe Tax to fit your business needs with tax overrides. Create rules that apply to a product tax code in any supported location.

For example, you can:

- Change the[Software as a service (SaaS) - personal use](/tax/tax-codes?tax_code=txcd_10103000)tax code from taxable to non-taxable in Louisiana to reflect the uncertainty of how SaaS might be taxed.
- Apply a 5% tax rate to the[Newspapers](/tax/tax-codes?tax_code=txcd_35020100%09)tax code in Poland, instead of the applied rate of 8%, to reflect that your product is a regional newspaper and not a national one.
- Treat the[Food for non-immediate consumption](/tax/tax-codes?tax_code=txcd_40040000)tax code as taxable at the standard rate in New York, to reflect that you sell a bagels with cream cheese.

After you create a tax override, you’re responsible for keeping the rate and taxability up to date with any changes in tax law. When you remove a tax override, Stripe manages the updates.

## Create a tax override

To create a tax override rule, you must enable tax collection in Stripe by adding a tax registration for a jurisdiction. We recommend that you create your first tax override in a sandbox to make sure that you get the tax outcome you expect:

1. In the Dashboard, navigate to the[Overrides tab](https://dashboard.stripe.com/tax/overrides)in the Tax page.
2. Click+ Create override.
3. In the sectionProduct tax code, choose the product tax code your override applies to.
4. (Optional)Specify the date and time for the override rule to become effective underEffective date. For example, you can set the override rule to start from the first day of the month. If you don’t set a date, the rule takes effect immediately.
5. In the sectionRule location, choose a jurisdiction where your override applies.  - You can create a rule that applies to a country or state.
  - For US jurisdictions, you can also create a rule that only applies to a specific city, county, or district.


6. ForTax type, choose the type of tax your override applies to.
7. Click the Tax behavior you want to apply. We indicate whether the product tax code you chose is taxable or non-taxable in that specific location and for the particular tax type (for example, sales tax or VAT).  - If you chooseTaxable, you have two options:    - Apply the standard rate. This means that your rule always uses the standard rate that Stripe has determined for that product tax code, tax, and location. If the standard rate changes, that change also applies to your products.
    - Apply a custom rate. This means that your rule uses the tax rate that you set. If the standard rate changes for that product, your custom rate still applies.

Regional considerationsUnited StatesYou can’t apply a custom rate in the US when creating a rule for a state that applies to all jurisdictions in a state because several cities and counties have different tax rates. To determine a custom rate for these jurisdictions, select a specific city, county, or district in the jurisdiction dropdown.




8. Verify that all of the details in theSummarypanel are correct. TheRate previewdisplays the expected tax rate that applies for a location within the jurisdiction you chose.  - The calculated tax might vary for other addresses within the same jurisdiction.
  - In some cases, the tax code, tax, and location you select might be taxed at the location of your business, rather than the destination of the customer. In these cases, the preview displays how tax applies in your business location. We don’t use your tax override rule in these cases.


9. ClickCreate ruleto apply your rule immediately, or at the time and date you chose.

## View and maintain your tax overrides

View all your override rules in the Overrides tab. Click an override to view the following information:

- When the rule was created or edited.
- Who created or edited the rule.
- The taxability and rate that’s applied.
- The tax code, location, and tax the rule applies to.

If you have an override in place, Stripe won’t automatically update the taxability or custom rate of your product if something changes. It’s your responsibility to maintain your tax overrides to make sure they reflect what’s needed for your business.

## Edit a tax override

If your override is scheduled to start in the future, you can edit the start or end time of your override rule. If your rule is already active, you can edit the end date and time. To change the tax code, location, or tax rate, you must archive the rule and create a new one in its place.

To edit your tax rule:

1. In the Dashboard, navigate to the[Overrides tab](https://dashboard.stripe.com/tax/overrides)in the Tax page.
2. Find the override rule you want to edit.
3. Click the overflow menu () next to the rule and chooseEdit rule.
4. Make your changes to the time and date.
5. ClickSave.

## Archive a tax override

You can archive an override that you created. After you archive an override rule, it no longer applies to your tax transactions and Stripe’s default behavior applies instead. Rules can’t be unarchived, but you can create a new rule instead.

To archive your tax override:

1. In the Dashboard, navigate to the[Overrides tab](https://dashboard.stripe.com/tax/overrides)in the Tax page.
2. Find the tax override you want to archive.
3. Click the overflow menu () next to the rule and chooseArchive rule.
4. Confirm your changes, then clickArchive.

## Verify which transactions have a tax override rule applied

To verify which tax override applies to a transaction, view the customizations_applied_ids column of the itemized export.

We don’t include transactions that contain tax overrides in the US-specific location reports or summarized reports. Learn more about the different tax reports.

## How we pick which override applies

When two rules apply to the same product in the same jurisdiction, Stripe only applies the more specific rule.

For example, this might apply if Stripe treats your product as taxable in the state of Colorado, but you want to treat it as non-taxable in all of Colorado except for the city of Boulder, where it should be taxed at the standard rate.

To change this, you can create a rule for the tax code that you apply to your product for the state of Colorado:

1. Navigate to the[Overrides tab](https://dashboard.stripe.com/tax/overrides)in the Tax page, then chooseColoradofrom theRule locationdropdown.
2. EnableInclude all jurisdictions.
3. ChooseSales Taxfrom theTax typedropdown.
4. SetNon-taxableas theTax behavior.

Additionally, you can create a second rule for the same tax code to apply tax in Boulder, but not elsewhere in Colorado:

1. Navigate to the[Overrides tab](https://dashboard.stripe.com/tax/overrides)in the Tax page, then chooseColoradofrom theChoose locationdropdown underRule location.
2. DisableInclude all jurisdictions.
3. ChooseBoulderfrom theChoose a jurisdiction* dropdown.
4. ChooseSales Taxfrom theTax typedropdown.
5. SetStandard rateas theTax behavior.

You can’t create a tax override that applies to the same specific jurisdiction (for example, Boulder) for the same tax code, during the same time period.

## When you can’t use overrides

Some parts of a tax calculation can’t be overridden. The following things will continue to affect the final tax calculation:

- Sourcing rules: These rules determine whether tax is calculated using the destination of the buyer or the origin of the seller. If you create an override that applies to a jurisdiction, but your product is sourced to the origin instead, your override rule won’t apply.
- Tiers, thresholds, and taxable basis apply in some jurisdictions:  - Taxable basis: In certain locations, only a specific portion of the tax code is taxable. For example, in Texas, only 80% of the cost of Software as a service is subject to tax.
  - Treatment based on price: Products might be treated differently based on their price. For example, in New York, clothing is exempt from tax if it costs under 110 USD, but taxable if it exceeds that amount. Even if you create a rule for New York City with a custom rate, sales of clothing in New York under 110 USD is still considered exempt.



Regional considerationsUnited StatesTax overrides in Stripe don’t transfer to TaxJar. When using TaxJar for filing, these overrides aren’t taken into account when TaxJar recalculates the tax you’re expected to file. As a result, tax overrides might not be suitable for your specific use case.

Interested in using Tax overrides?Please provide your email address below and we'll get in touch when it's ready!Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll let you know when it's ready.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a tax override](#create-a-tax-override)[View and maintain your tax overrides](#view-and-maintain-your-tax-overrides)[Edit a tax override](#edit-a-tax-override)[Archive a tax override](#archive-a-tax-override)[Verify which transactions have a tax override rule applied](#verify-which-transactions-have-a-tax-override-rule-applied)[How we pick which override applies](#how-we-pick-which-override-applies)[When you can’t use overrides](#when-you-can’t-use-overrides)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`