htmlWork with payment authentication data in the Dashboard | Stripe Documentation[Skip to content](#main-content)Using the Dashboard[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayment-authentication%2Fdashboard)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayment-authentication%2Fdashboard)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)
[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[More payment scenarios](/docs/payments/more-payment-scenarios)[3D Secure authentication](/docs/payments/3d-secure)[Payment authentication reporting](/docs/payment-authentication)# Work with payment authentication data in the Dashboard

Use the Dashboard to download reports and inspect data sources.[Data availability and date range](#data-availability)When loading the page, the report defaults to displaying the previous 6 months. You can select previous months in the dropdown menu, or choose the trailing 4-week, 3-month, or 6-month periods. All charts and tables adjust to reflect the date selection.

[Downloading report data](#downloading-report-data)![](https://b.stripecdn.com/docs-statics-srv/assets/download-report.764901ac6d68f7903fef403e75dcdab9.png)

You can use the Download report link displayed on each chart to download the data used to generate the chart as a CSV file.

### Downloading summary report data

![](https://b.stripecdn.com/docs-statics-srv/assets/summary-report.52d113402ce8ee836fc2ccbc4739ec19.png)

When you click Download report you might be prompted for the type of report you want. The summary report downloads a CSV report containing the main columns for the underlying data.

### Downloading itemized report data

![](https://b.stripecdn.com/docs-statics-srv/assets/itemized-report.298342f0a96ab6dcb9c5c8cb3aa80e6b.png)

When you click Download report you might be prompted for the type of report you want. The itemized report downloads a CSV report based on the columns you select. You can choose what columns to include from the dropdown: Default, All, or Custom.

![](https://b.stripecdn.com/docs-statics-srv/assets/itemized-report-1.8500af94be59b732ac200c1d89c3e5d0.png)

Use the Show button to view the columns that will be included in the report.

[Inspecting report data with Sigma](#inspecting-data-with-sigma)![](https://b.stripecdn.com/docs-statics-srv/assets/view-in-sigma.f39682979ac5305f17f5580cb3b892c6.png)

Users with access to Sigma can further analyze their data by using the View in Sigma link, also on the top right of every chart. By default, Sigma opens the SQL query that generates the data included in the chart or the CSV report file. You can modify the query to dig deeper into any trends that you want to better understand. See Writing queries for more information on this Sigma dataset.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Data availability and date range](#data-availability)[Downloading report data](#downloading-report-data)[Inspecting report data with Sigma](#inspecting-data-with-sigma)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`