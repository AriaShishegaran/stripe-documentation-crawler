htmlRevenue Recognition rules | Stripe Documentation[Skip to content](#main-content)Revenue recognition rules[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Frules)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Frules)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Revenue recognition](/docs/revenue-recognition)# Revenue Recognition rules

Learn about Revenue Recognition rules.Configure Revenue Recognition rules to define revenue treatments specific to your business.

Stripe Revenue Recognition allows you to configure custom rules to handle revenue treatments specific to your business needs. For example, you can configure a rule to:

- Categorizean[invoice](/api/invoices)line item as a tax or fee
- Booka transaction amount or invoice line item as a passthrough fee
- Excludetransactions from specific customers or test invoices
- Amortizerevenue over a specified time period relative to payment or invoice finalization date
- Recognizerevenue after a specific time period to model a futurefulfillmentschedule
- Allocatemultiple revenue treatments to a single transaction amount

Rules are typically applied to reports 24-48 hours after setting them. Rules that you apply to a report have an active status. Rules that you haven’t applied to a report remain in a processing status.

## Default rules

Stripe Revenue Recognition provides a set of default rules to model the methodology for handling common Stripe resources.

- For invoice line items with service periods, the line item amount amortizes evenly over its service period. If a period isn’t set on an invoice line item, the amount is recognized entirely when the invoice finalizes.
- Other payments not made through an invoice are recognized immediately upon payment if no service period or fulfillment information exists, or by the[imported](/revenue-recognition/data-import)service period or fulfillment data.

![Default rules](https://b.stripecdn.com/docs-statics-srv/assets/default-rules.1cdaa035a358fec4294971ba23bddaa1.png)

## Custom rules

Custom rules override Stripe’s default revenue treatment behaviors where applicable and you can add or modify them on the Stripe Dashboard.

You can apply rules to:

- [Products](/api/products)
- [Customers](/api/customers)
- [Invoice line items](/api/invoices/line_item)
- [Other payments](/api/charges)(that is, payments that aren’t associated with invoices)

See how to create a rule and define revenue treatments. You can also explore sample rules on tax treatment, pass-through fees, exclusion, and custom time periods.

## Rule ordering and hierarchy

Each transaction can only have one rule applied to it when processing revenue reports. In situations where a single transaction fits the “Apply-to” criteria for multiple rules, rule hierarchy determines which rule to apply to the transaction. The higher a rule is ranked on the list, the higher the priority it’s assigned.

You can rearrange the order of the rules by clicking Change rule order as shown below:

![Rules](https://b.stripecdn.com/docs-statics-srv/assets/rules.076bd00821d7a78ec4d541afe8c9b669.png)

After clicking Change rule order, you can reorder the rules to adjust their priorities.

![Rule order](https://b.stripecdn.com/docs-statics-srv/assets/rule-order.6232b5130188f7e9b253d7f9d197e3f0.png)

## Best practices for effectively maintaining your rules

As your business grows, it’s important to make sure you regularly maintain your rules to ensure the accuracy of your revenue reports. The following are some best practices to keep rules correct for your Revenue Recognition reports.

Know when to create a rule

When applied correctly, Stripe’s default rules and revenue treatment methodology for handling subscription events accurately recognize and defer revenue for businesses who require more control over their unique use.

Regularly monitor rules to ensure they’re up-to-date

Billing models, customer types and edge cases can regularly change, and you should evolve your rules accordingly. To make sure that revenue treatments remain predictable, periodically check your rules so they’re up-to-date in terms of hierarchy and effective period.

Check if your accounting period is open or closed when new rules are applied

If the effective period for a new rule overlaps with a closed accounting period, it generates corrections if the rules are retroactively applied to transactions from past (closed) accounting periods. If you want to avoid this, reopen your books by opening your accounting period prior to adding the rule.

## See also

- [Create a rule](/revenue-recognition/rules/create-a-rule)
- [Examples](/revenue-recognition/rules/examples)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Default rules](#default-rules)[Custom rules](#custom-rules)[Rule ordering and hierarchy](#rule-ordering-and-hierarchy)[Best practices for effectively maintaining your rules](#best-practices-for-effectively-maintaining-your-rules)[See also](#see-also)Products Used[Revenue Recognition](/billing/revenue-recognition)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`