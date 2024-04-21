# Risk insights

Stripe Radar’s adaptive machine learning system determines the risk score and risk level for a payment and uses them to decide when to block or mark payments for review. The system evaluates hundreds of signals about each payment, using data from Stripe’s network across millions of businesses. The risk insights feature, available with Stripe Radar for Fraud Teams, provides a sneak peek into some of the signals that power Radar’s machine learning system.

[machine learning system](https://stripe.com/radar/guide)

Risk insights for payments

If you’re not seeing the customer information or locations that you expect, check that your integration follows Radar’s best practices.

[best practices](/radar/integration)

If your integration doesn’t provide important details like the cardholder’s email address, IP address, or shipping address, Radar can’t compute all of the data it needs to accurately evaluate each payment.

Risk insights also includes information about the customer, such as matching the cardholder’s name with the provided email, and the success rate of transactions on the Stripe network associated with the email address. A low authorization rate may indicate suspicious behavior, because previous declines sometimes suggest past attempts at fraudulent transactions.

We also highlight geography-based information, including the billing, shipping, and, IP address locations associated with this payment.

## Risk insights

If you want to see more Radar’s signals, click the Show all insights button from the risk insights section. This opens a dialog with a list of signals to Radar’s machine learning engine.

Radar’s risk insights dialog

The data used to populate fraud factor numbers and top fraud factors is only populated for charges made within the last 6 months. This feature isn’t supported for payments in test mode.

Some of the signals in the risk insights dialog have badges with numbers next to them. These badges show the fraud factor for a signal on this payment. A fraud factor represents the likelihood of fraud for charges with a value similar to this signal when compared to the average transaction on Stripe. A fraud factor of 3.5x means that charges with a similar value for this signal are 3.5 times more likely to be fraudulent than average. In a higher risk payment, we expect to see some fraud factors greater than 1, and in a lower risk payment we expect to see some fraud factors less than 1.

Fraud factors

Hover over a fraud factor to see more information about the possible values for it. These factors will change over time as the data in our network changes. This data provides context for the distribution of fraud factors for a signal. This dialog also provides the network distribution of values for a signal, letting you know whether the current payment has a value that’s common or if it’s rare or unique in the Stripe network.

Top fraud factors

The Top Fraud Factors section outside the risk insights dialog notifies you with fraud signals when the payment has values that commonly indicate fraud. Because Radar’s machine learning detects complex patterns across hundreds of signals, it’s still possible for a charge to be correctly identified as fraud, even if none of the signals appear suspicious on an individual level.

## Related payments

You can also view the network of related payments, which includes any other payments made to your business using the same customer ID, IP address, or card number as the payment you’re currently viewing. This can help identify common fraud patterns, such as card testing (many different cards sharing a single IP address) or trial abuse (many “customers” share the same card).

[card testing](/disputes/prevention/fraud-types#card-testing)

Related payments

## See also

- Review

[Review](/radar/reviews)

- Integration checklist

[Integration checklist](/radar/integration)