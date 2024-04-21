htmlRisk insights | Stripe Documentation[Skip to content](#main-content)Risk insights[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fradar%2Freviews%2Frisk-insights)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fradar%2Freviews%2Frisk-insights)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)
[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Radar](/radar)·[Home](/docs)[Get started](/docs/get-started)[Protect against fraud](/docs/radar)[Reviews](/docs/radar/reviews)# Risk insights

Understand risk factors and details about a particular payment.Stripe Radar’s adaptive machine learning system determines the risk score and risk level for a payment and uses them to decide when to block or mark payments for review. The system evaluates hundreds of signals about each payment, using data from Stripe’s network across millions of businesses. The risk insights feature, available with Stripe Radar for Fraud Teams, provides a sneak peek into some of the signals that power Radar’s machine learning system.

![](https://b.stripecdn.com/docs-statics-srv/assets/risk-insights-card.ef788006b7b5d6acbb4d237386a3c4ed.png)

Risk insights for payments

### Why are certain fields unavailable?

If you’re not seeing the customer information or locations that you expect, check that your integration follows Radar’s best practices.

If your integration doesn’t provide important details like the cardholder’s email address, IP address, or shipping address, Radar can’t compute all of the data it needs to accurately evaluate each payment.

Risk insights also includes information about the customer, such as matching the cardholder’s name with the provided email, and the success rate of transactions on the Stripe network associated with the email address. A low authorization rate may indicate suspicious behavior, because previous declines sometimes suggest past attempts at fraudulent transactions.

We also highlight geography-based information, including the billing, shipping, and, IP address locations associated with this payment.

## Risk insights

If you want to see more Radar’s signals, click the Show all insights button from the risk insights section. This opens a dialog with a list of signals to Radar’s machine learning engine.

![](https://b.stripecdn.com/docs-statics-srv/assets/risk-insights-dialog.90d9ff8cc321c3e9bab7423b07ec97c6.png)

Radar’s risk insights dialog

### Understand fraud factors

### Why don't I see any fraud factors?

The data used to populate fraud factor numbers and top fraud factors is only populated for charges made within the last 6 months. This feature isn’t supported for payments in test mode.

Fraud factor numbers![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Some of the signals in the risk insights dialog have badges with numbers next to them. These badges show the fraud factor for a signal on this payment. A fraud factor represents the likelihood of fraud for charges with a value similar to this signal when compared to the average transaction on Stripe. A fraud factor of 3.5x means that charges with a similar value for this signal are 3.5 times more likely to be fraudulent than average. In a higher risk payment, we expect to see some fraud factors greater than 1, and in a lower risk payment we expect to see some fraud factors less than 1.

![](https://b.stripecdn.com/docs-statics-srv/assets/risk-insights-fraud-factor.3bd00f6b09999ef71f6d258c2cc20be6.png)

Fraud factors

Hover over a fraud factor to see more information about the possible values for it. These factors will change over time as the data in our network changes. This data provides context for the distribution of fraud factors for a signal. This dialog also provides the network distribution of values for a signal, letting you know whether the current payment has a value that’s common or if it’s rare or unique in the Stripe network.

Top fraud factors![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

![](https://b.stripecdn.com/docs-statics-srv/assets/risk-insights-top-fraud-factors.ef27de20a842cb7d411261e9e7757fc6.png)

Top fraud factors

The Top Fraud Factors section outside the risk insights dialog notifies you with fraud signals when the payment has values that commonly indicate fraud. Because Radar’s machine learning detects complex patterns across hundreds of signals, it’s still possible for a charge to be correctly identified as fraud, even if none of the signals appear suspicious on an individual level.

## Related payments

You can also view the network of related payments, which includes any other payments made to your business using the same customer ID, IP address, or card number as the payment you’re currently viewing. This can help identify common fraud patterns, such as card testing (many different cards sharing a single IP address) or trial abuse (many “customers” share the same card).

![](https://b.stripecdn.com/docs-statics-srv/assets/related-payments-highlight.f0668ec4db4273e04eb4f8f3b8910e08.png)

Related payments

## See also

- [Review](/radar/reviews)
- [Integration checklist](/radar/integration)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Risk insights](#risk-insights-dialog)[Related payments](#related-payments)[See also](#see-also)Products Used[Radar](/radar)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`