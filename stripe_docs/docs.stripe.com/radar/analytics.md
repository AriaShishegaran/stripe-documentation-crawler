# Radar Analytics

The Radar analytics dashboard helps you analyze and understand the state of fraud for your business. The dashboard contains several reports with information about how much fraud Radar is blocking for your business in addition to information about important indicators of changing fraud patterns.

[Radar analytics dashboard](https://dashboard.stripe.com/radar)

[Radar](/radar)

Using Sigma or Data Pipeline, you can use Radar rule attributes alongside your own dataset to continuously improve your fraud management, identify fraudulent payments, create a deeper understanding of your customers, and analyze data in an environment that works best for you.

[Sigma](https://stripe.com/sigma)

[Data Pipeline](https://stripe.com/data-pipeline)

[Radar rule attributes](/radar/rules/reference#supported-attributes)

[continuously improve your fraud management](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data)

[Overview Chart](#overview-chart)

## Overview Chart

When fighting fraud, it’s important to see what Radar is doing during the flow of attempted payments. The Overview Chart shows you how Radar helps reduce fraud. From left-to-right, you can see payments flow through a few steps in their lifecycle. First, you can see the Authenticated column, showing you how many payment attempts went through a 3DS challenge, and how many completed and failed. The second column, Screened by Radar, shows how often Radar’s risk score and your Radar Rules blocked suspicious payments, sent others to your review queue, and allowed the rest to continue the payment attempt. Finally, the Disputed column shows the disputes on your account.

Below the chart, a table shows the numeric values for each column. Hover over a value to see its detailed information, with subcategories, counts, and subtotals.

[Benchmarking](#benchmarking)

## Benchmarking

Without a comparison, it’s hard to tell what a particular fraud rate means. Is a 0.02% dispute rate good or bad? The answer depends on your business model, your region, and many other factors. Radar provides merchants with a comparison to similar businesses on key fraud metrics to help inform actions you can take to improve the performance of Radar.

Radar has a tool specifically for this—aggregated benchmarks for businesses in your region, and businesses that are similar to your own.

You can view benchmarks for:

- Block rate — The percentage of payments that are blocked by your Radar Rules, high risk scores, or otherwise blocked by Stripe.

- Fraudulent dispute rate — The percentage of payments that customers dispute as fraud.

- Estimated false positive rate — The estimated percentage of non-fraudulent payments that your Radar settings block. (A high value means that you may be blocking too many valid payments.)

You’ll see these benchmarks embedded in the charts and tables throughout Radar’s analytics page—hover your mouse over these icons to view their details.

[Radar’s analytics page](https://stripe.com/radar)

We’ve taken steps to ensure that other merchants can’t identify your benchmarks:

- We aggregate regional benchmarks across many businesses in your region, so it’s not possible to discern an individual competitor in such a large pool of businesses.

- Benchmarks for similar businesses only display if you have many dozens of businesses in your cohort. (If you don’t see any similar-business benchmarks, this is the reason. You’ll still see regional benchmarks, though, since those are large cohorts.)

- For a given benchmark rate, the value for each business gets one “vote," so even if a single company dominates your industry, that company is only a small weight in the benchmark.

- We only include businesses with a significant number of payments, since some of these fraud events are generally rare.

If you want to opt-out of benchmarking, contact us. If you opt out, your business won’t be included in benchmark calculations, though you can continue to see benchmarks in Radar’s analytics page.

[contact us](https://support.stripe.com/)

[Fraud prevention](#fraud-prevention)

## Fraud prevention

Radar’s algorithms evaluate payments for suspected fraud risk and take action accordingly. Radar blocks high risk payments by default and provides additional fraud tools (if you have Radar for Fraud Teams) so that you can specify your own criteria to block suspicious payments.

[Radar for Fraud Teams](https://stripe.com/radar/fraud-teams)

Attempted payments account for all card payment requests screened by Radar, including retried payment attempts on the same purchase.

Card-present payments made through Stripe Terminal or recurring payments made through Stripe Billing aren’t screened by Radar.

[Stripe Terminal](https://stripe.com/terminal)

[Stripe Billing](https://stripe.com/billing)

Blocked payments represents the number of attempted payments that Radar blocked. Payments are broadly blocked by Radar for two reasons:

- Radar’s machine learning model evaluates the payment as high risk and blocks it by applying the default high risk block rule. Radar sets the blocking threshold at 75 by default and Radar for Fraud Teams users can adjust it in the risk settings.

[high risk block rule](/radar/rules#built-in-rules)

[Radar for Fraud Teams](https://stripe.com/radar/fraud-teams)

[risk settings](/radar/risk-settings)

- The payment matches one of your other block rules.

[block rules](https://dashboard.stripe.com/settings/radar/rules)

Block rate is the percentage of attempted payments that were blocked by Radar.

Volume, blocked payments is the monetary value of attempted payments that Radar blocked. (The volume shown is in your default currency, using estimated conversion rates for payments from other currencies.)

Stripe may block a payment for other reasons not included here (e.g., payments initiated by cards on deny-lists that are globally known to be fraudulent or payments made from sanctioned countries).

Additionally, SetupIntents—which let you save customer credentials for future payments—aren’t accounted for here even though they’re screened by Radar.

[SetupIntents](/payments/setup-intents)

The following section contains two views that help you understand changes to your block rate over the selected time period, along with the proportion of payments blocked by both Radar’s machine learning model and your block rules.

Radar — High risk score accounts for the number of blocked payments that were blocked due to high risk, their total monetary volume, and the corresponding block rate (out of all attempted payments). These are payments that received a Radar risk score greater than your high risk threshold and were consequently blocked by the default high risk block rule.

[high risk block rule](/radar/rules#built-in-rules)

The estimated false positive rate is the estimated probability that a non-fraudulent payment was incorrectly blocked by Radar’s machine learning. This is derived using a combination of the Radar risk level of these payments and global experiments across all payments on the Stripe network.

Radar — Rules similarly, accounts for the number of blocked payments that were blocked by one of your other block rules, their total monetary volume, and the corresponding block rate (out of all attempted payments).

[block rules](https://dashboard.stripe.com/settings/radar/rules)

Depending on your business needs, your block rate or false positive rate, you may want to adjust the amount of fraud blocked by Radar’s machine learning. Radar for Fraud Teams users can adjust the risk threshold (75 by default) at which payments are blocked in their risk settings. As you increase the risk score at which you block, you’ll allow more overall payments through but you may also allow more fraud. As you decrease the risk score where you block, you’ll probably block more fraud but also block more overall payments.

[Radar for Fraud Teams](https://stripe.com/radar/fraud-teams)

[risk settings](/radar/risk-settings)

Closely monitor your fraudulent dispute rate and disputes activity to understand the impact of changing risk thresholds. In general, follow Radar’s best practices to ensure your integration makes the most of Radar’s machine learning models.

[best practices](/radar/integration)

[Fraudulent disputes](#fraudulent-disputes)

## Fraudulent disputes

Use the fraudulent disputes section to analyze fraudulent dispute activity for your business over time. Fraudulent disputes are those that were opened with fraud as the specified reason.

[specified reason](/disputes/categories)

This chart displays fraudulent dispute rate (in solid line) as a percentage of payments in the selected time period that have been disputed for fraud.

Cardholders may take some time to dispute a payment, but almost all disputes arrive within 120 days after the payment. Therefore, for the trailing 120 days, this chart displays:

- A partial dispute rate (in solid line) for payments that have already been disputed.

- An estimated projection of the maximum dispute rate (in dashed line) after all disputes for these more recent payments have arrived.

The final dispute rate is likely to fall somewhere between the partial dispute rate and the projected maximum dispute rate, which is based on historical dispute statistics across the Stripe network and dispute activity on your account.

The fraudulent dispute rate chart tracks the rate of fraudulent disputes on payments based on when the payment was created and not when it was disputed. This is a more accurate representation of fraud for your business, because it shows which specific payments were disputed for fraud. For example, you could use the fraud rate chart to see if payments made during a particular holiday sale resulted in more fraudulent disputes than usual.

The average time to dispute metric measures the amount of time, on average, it took for payments in the selected time range to be disputed for fraud. The expected range is 1–120 days.

[Disputes](#disputes)

## Disputes

This section helps you identify trends in payments that were disputed by the cardholder for any specified reason. Look for unexpected changes to disputes activity to identify changes to fraud patterns in your business and take action to prevent disputes and fraud.

[specified reason](/disputes/categories)

[prevent disputes and fraud](/disputes/prevention)

Aggregated totals at the top of this section account for the total number of disputes received, the number of currently open disputes that you must decide to accept or challenge, and the associated disputed volume (the total monetary volume of payments disputed, not including any dispute fees). The win rate is the percentage of disputes received that you won.

[decide](/disputes/responding#decide)

This data only includes inquiries (which can act as early warnings of fraudulent payments) when they escalate into real disputes.

[inquiries](/disputes/how-disputes-work#inquiries)

The disputes received chart represents dispute activity, plotting disputes opened by dispute creation date for successful payments in the specified time period. A tabular breakdown of disputes received by dispute reason accompanies this chart, along with information about how many disputes you responded to with supporting evidence, and how many you won. The breakdown only displays the top three most frequently observed dispute types; you can download the dispute report for a more granular view into all dispute reasons.

[dispute reason](/disputes/categories)

[download](/radar/analytics#downloading-and-inspecting-data-sources)

[Manual reviews](#manual-reviews)

## Manual reviews

Radar for Fraud Teams users can use this section to analyze the current state and outcomes of payments that were placed in review.

[placed in review](/radar/reviews)

Check out these best practices to get the most out of reviews and perform them efficiently.

[best practices](/radar/reviews#best-practices)

The sent to manual review chart on the left displays the number of payments sent to your review queue within the specified time period. As you review payments and take action, the tabular breakdown on the right updates to display how many reviews were approved, refunded, disputed or are currently in review.

If a customer disputes a payment that’s currently in review, the review automatically closes.

[disputes](/disputes)

The dispute rate of approved reviews represents the percentage of reviews that were approved after investigation but eventually disputed by the cardholder. While cardholders dispute payments for several reasons, you should carefully review payments before approving them to make sure this percentage stays reasonably low.

[Using the dashboard](#using-the-dashboard)

## Using the dashboard

To give you a comprehensive view of fraud trends for your entire business, this dashboard aggregates your fraud data across all currencies and uses daily foreign exchange rates to convert all monetary amounts into your default currency.

Stripe computes all of your data daily, beginning at 12:00am UTC. Data for each day includes all account activity that takes place between 12:00am UTC and 11:59pm UTC. Radar Analytics data is available in this dashboard within 24 hours.

When loading the page, the report defaults to displaying the previous six months. You can select previous months in the dropdown menu, or choose the trailing 4-week, 3-month, 6-month, or 1-year periods. All charts and tables adjust to reflect the date selection.

Each chart has a download link in the top right corner that you can use to download a CSV of the data in the chart. Users with access to Sigma can further analyze their data by using the View in Sigma link, also on the top right of every chart. By default, Sigma opens the SQL query that generates the data included in the chart and the CSV file. You can modify the query to dig deeper into any trends that you want to better understand.

[Sigma](https://stripe.com/sigma)
