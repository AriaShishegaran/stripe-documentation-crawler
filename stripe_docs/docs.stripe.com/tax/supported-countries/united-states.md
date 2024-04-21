# Collect tax in the United States

Businesses selling goods and services to customers in the United States (US) might need to collect sales tax. That’s the case even if your business isn’t established (based) in the US. Tax rates and rules vary by state.

[OptionalStates in the US](#us-states)

## OptionalStates in the US

## When to register for tax collection

Different rules determine when and how you need to register to collect tax depending on the state. States can choose which level and type of activity in the state means a business needs to collect tax there. This is called nexus. A business can have nexus in a state if they have:

- Physical activity, such as having remote employees based there or storing inventory in a warehouse.

- Economic activity, such as an amount or total value of transactions within a time period.

If you have nexus in a state, you need to register for a license to collect tax on sales to customers in that state.

To understand the economic nexus thresholds in each state use the links above. Stripe only monitors if you have reached an economic nexus tax threshold for sales outside of the state your business is based in. Learn more about economic nexus.

[links above](/tax/supported-countries/united-states#us-states)

[economic nexus](https://stripe.com/guides/introduction-to-us-sales-tax-and-economic-nexus)

Use the Thresholds tab to get insights about your potential tax registration obligations. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

[Thresholds tab](https://dashboard.stripe.com/tax/thresholds)

[monitoring tool works](/tax/monitoring)

## Register to collect tax

Each state has its own sales tax authority. You need to individually register to collect sales tax in each state where you have met the registration requirements. Start by going to the state tax authority website. If you need help finding the right links to register for tax, select a state from the list above.

[list above](/tax/supported-countries/united-states#us-states)

Learn more about the sales tax registration process in the United States.

[the sales tax registration process in the United States](https://stripe.com/guides/sales-tax-registration-process-us)

The Streamlined Sales and Use Tax Agreement (SSUTA) was created by a coalition of states to help businesses manage their sales and use tax obligations across the United States. Twenty-four US states are members of the SSUTA agreement. However, individual states can still decide which products and services are taxable in their state. You can learn more and register for sales and use tax permits in all SSUTA member states on the streamlined sales tax registration website.

[streamlined sales tax registration website](https://www.streamlinedsalestax.org/)

After you’ve registered with a state, add your registration to Stripe in the Registrations tab in the Dashboard to start collecting tax on your transactions in that location.

[Registrations tab](https://dashboard.stripe.com/tax/registrations?location=us)

## How we calculate taxes

What you sell and where you sell impacts how tax is calculated on your sales. Different rules apply when your customer is located in the same state as your business or located somewhere else.

Stripe calculates tax on a transaction taking into account the following factors:

- the location of your business

- the tax registrations you’ve added to Stripe

- the location of the buyer

- the type of the product sold (based on which product tax code you assigned to your product)

[product tax code](/tax/tax-codes)

- the status of the customer (whether they’re an individual or a business)

If your origin address is in the US and is different from the state your customer is located in, Stripe always calculates tax based on your customer’s location.

[origin address](/tax/set-up#origin-address)

If your origin address is in the US and in the same state as your customer’s state, Stripe generally calculates sales tax based on your customer’s location.

[origin address](/tax/set-up#origin-address)

However some states use your origin address instead of the customers location depending on the type of product or service you sell:

- In Arizona, Illinois, Missouri,Pennsylvania, Tennessee, and Virginia, Stripe applies tax based on your business location.

- In California, state, county, and city taxes are based on the origin address, while district taxes are based on the customer’s location.

- In Mississippi, Ohio, Texas, and Utah, Stripe applies tax based on the origin address for physical and digital goods. Sales of services are taxed at the destination address.

[OptionalSales tax holidays](#us-sales-tax-holidays)

## OptionalSales tax holidays

## Report and file your taxes

Stripe provides reports of your completed tax transactions. To access these reports, navigate to the Registrations tab of the Dashboard. Learn more about the different types of reports.

[Registrations tab](https://dashboard.stripe.com/tax/registrations)

[the different types of reports](/tax/reports)

You’re responsible for filing and remitting your taxes in the US. Stripe doesn’t file taxes on your behalf. You can find where to file your return for each state in our tax returns guide.

[our tax returns guide](https://stripe.com/guides/how-to-file-sales-tax-us)

For automating filing in the US, we recommend using TaxJar’s AutoFile solution.

[TaxJar’s AutoFile solution](https://go.taxjar.com/2021StripeTaxInquiry_LP-01-Request.html)
