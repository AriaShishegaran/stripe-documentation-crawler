htmlCollect tax in the United States | Stripe Documentation[Skip to content](#main-content)United States[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Funited-states)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsupported-countries%2Funited-states)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Supported countries](/docs/tax/supported-countries)# Collect tax in the United States

Learn how to use Stripe Tax to calculate, collect, and report tax in the US.Businesses selling goods and services to customers in the United States (US) might need to collect sales tax. That’s the case even if your business isn’t established (based) in the US. Tax rates and rules vary by state.

[OptionalStates in the US](#us-states)## When to register for tax collection

Different rules determine when and how you need to register to collect tax depending on the state. States can choose which level and type of activity in the state means a business needs to collect tax there. This is called nexus. A business can have nexus in a state if they have:

- Physical activity, such as having remote employees based there or storing inventory in a warehouse.
- Economic activity, such as an amount or total value of transactions within a time period.

If you have nexus in a state, you need to register for a license to collect tax on sales to customers in that state.

To understand the economic nexus thresholds in each state use the links above. Stripe only monitors if you have reached an economic nexus tax threshold for sales outside of the state your business is based in. Learn more about economic nexus.

Use the Thresholds tab to get insights about your potential tax registration obligations. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

## Register to collect tax

Each state has its own sales tax authority. You need to individually register to collect sales tax in each state where you have met the registration requirements. Start by going to the state tax authority website. If you need help finding the right links to register for tax, select a state from the list above.

Learn more about the sales tax registration process in the United States.

### Streamlined Sales and Use Tax Agreement (SSUTA)

The Streamlined Sales and Use Tax Agreement (SSUTA) was created by a coalition of states to help businesses manage their sales and use tax obligations across the United States. Twenty-four US states are members of the SSUTA agreement. However, individual states can still decide which products and services are taxable in their state. You can learn more and register for sales and use tax permits in all SSUTA member states on the streamlined sales tax registration website.

After you’ve registered with a state, add your registration to Stripe in the Registrations tab in the Dashboard to start collecting tax on your transactions in that location.

## How we calculate taxes

What you sell and where you sell impacts how tax is calculated on your sales. Different rules apply when your customer is located in the same state as your business or located somewhere else.

Stripe calculates tax on a transaction taking into account the following factors:

- the location of your business
- the tax registrations you’ve added to Stripe
- the location of the buyer
- the type of the product sold (based on which[product tax code](/tax/tax-codes)you assigned to your product)
- the status of the customer (whether they’re an individual or a business)

### Sales to a customer located outside the state your business is based in

If your origin address is in the US and is different from the state your customer is located in, Stripe always calculates tax based on your customer’s location.

### Sales to a customer located within the same state as your business

If your origin address is in the US and in the same state as your customer’s state, Stripe generally calculates sales tax based on your customer’s location.

However some states use your origin address instead of the customers location depending on the type of product or service you sell:

- In Arizona, Illinois, Missouri,Pennsylvania, Tennessee, and Virginia, Stripe applies tax based on your business location.
- In California, state, county, and city taxes are based on the origin address, while district taxes are based on the customer’s location.
- In Mississippi, Ohio, Texas, and Utah, Stripe applies tax based on the origin address for physical and digital goods. Sales of services are taxed at the destination address.

[OptionalSales tax holidays](#us-sales-tax-holidays)## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab of the Dashboard. Learn more about the different types of reports.

You’re responsible for filing and remitting your taxes in the US. Stripe doesn’t file taxes on your behalf. You can find where to file your return for each state in our tax returns guide.

For automating filing in the US, we recommend using TaxJar’s AutoFile solution.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to register for tax collection](#when-to-register-for-tax-collection)[Register to collect tax](#register-to-collect-tax)[How we calculate taxes](#how-we-calculate-taxes)[Report and file your taxes](#report-and-file-your-taxes)Related Guides[Introduction to US sales tax and economic nexus](https://stripe.com/guides/introduction-to-us-sales-tax-and-economic-nexus)[Navigate the sales tax registration process in the US](https://stripe.com/guides/sales-tax-registration-process-us)[How to file sales tax returns in the US](https://stripe.com/guides/how-to-file-sales-tax-us)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`