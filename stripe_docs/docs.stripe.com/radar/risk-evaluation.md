# Risk evaluation

While Stripe Radar offers a greater ability to monitor your payments and protect your business from disputes, you’re ultimately responsible for payments you choose to accept, including those that are later disputed or found to be fraudulent.

[ultimately responsible](https://stripe.com/us/legal#processing-transactions-disputes)

At the core of Stripe Radar is an adaptive machine learning system that evaluates the risk level for each payment in real time. It uses hundreds of signals about each payment, and taps into data across our network of millions of businesses, to predict whether a payment is likely to be fraudulent.

Our machine learning system is flexible and responsive, continuously learns from new customer purchase patterns and transaction features, and incorporates feedback from you whenever payments are indicated as fraudulent.

[machine learning system](https://stripe.com/radar/guide)

When a business using Stripe sees a card for the first time, there’s a 91% chance that we’ve seen the card elsewhere on the Stripe network in the past.

## When to use Radar

The following information also applies to transactions created through Stripe Checkout and Stripe Billing. To provide a seamless experience for your subscription customers, Radar’s fraud models only score the initial transaction of a recurring Stripe Billing subscription, but evaluates rules for all transactions.

[subscription](/billing/subscriptions/creating)

Radar evaluates risk and runs rules for three different types of Stripe API objects: Charges, PaymentIntents and SetupIntents. Stripe designed the Radar rules to take four different actions:

[Charges](/api/charges)

[PaymentIntents](/api/payment_intents)

[SetupIntents](/api/setup_intents)

- Request 3DS authentication

- Allow the creation of the object

- Block the creation of the object

- Review the creation of a Charge

The following table illustrates which rules Radar runs for each type of API object:

You can enable Radar for SetupIntents in your Radar settings.

[Radar settings](https://dashboard.stripe.com/test/radar/settings)

## Risk outcomes

With Stripe Radar for Fraud Teams, each payment also includes a risk score that ranges from 0–99 to indicate the risk level on a more granular level. By default, a score of 65 or above indicates elevated risk, while a score of 75 or above indicates high risk. You can adjust the thresholds at Risk Settings.

[Risk Settings](/radar/risk-settings)

The Stripe machine learning models evaluate the likelihood that a payment is fraudulent. This judgment can take one of five values:

- High risk

[High risk](#high-risk)

- Elevated risk

[Elevated risk](#elevated-risk)

- Normal risk

[Normal risk](#normal-risk)

- Not evaluated

[Not evaluated](#not-evaluated)

- Unknown risk

[Unknown risk](#unknown-risk)

Each payment includes information on the outcome of our risk evaluation.

Radar for fraud teams users will see a risk insights section on the payment page that provides more details about why we assigned a payment a particular risk level and score.

[risk insights](/radar/reviews/risk-insights)

If a card issuer declines a payment, Stripe also includes any information we receive from them as part of the outcome.

[declines](/declines)

The outcome for each payment is available when viewing a payment in the Dashboard or through the API as part of the Outcome attribute of the Charge object.

[Dashboard](https://dashboard.stripe.com/)

[Outcome](/api#charge_object-outcome)

[Charge](/api#charge_object)

Stripe reports payments as high risk when we believe they’re likely to be fraudulent. Payments of this risk level are blocked by default.

[blocked](/radar/rules#built-in-rules)

On the Charge object of a high risk payment, the risk_level is set to highest.

If Stripe Radar ever blocks a payment that you know is legitimate, you can remove the block using the Dashboard. To do this, view the payment in the Dashboard and click Add to allow list. Adding a payment to the allow list doesn’t retry the payment, but it does prevent Stripe Radar from blocking future payment attempts with that card or email address.

Don’t see Add to allow list? Contact Stripe to have this feature added to your Radar account.

[Contact Stripe](https://support.stripe.com/email)

Elevated risk payments have an increased chance of being fraudulent. Stripe Radar allows payments of this risk level by default. Stripe Radar for Fraud Teams automatically places elevated risk payments into your review queue so you can take a closer look.

[review](/radar/reviews)

On the Charge object of an elevated risk payment, the risk_level is set to elevated.

Payments with a normal risk evaluation have fewer characteristics that are strongly indicative of fraud than payments with elevated or high risk levels. However, we recommend that you continue to be vigilant when fulfilling these orders. Payments that have normal risk can still turn out to be fraudulent and there are other possible types of fraud that can occur later on in the order process.

[types of fraud](/disputes/prevention/identifying-fraud)

On the Charge object of a successful payment with normal risk, the risk_level is set to normal.

The Risk level is set to not_assessed for non-card payments, card-based payments predating the public assignment of risk levels, and for payments where the merchant opts out of Radar fraud risk assessment.

On the Charge object of an unevaluated payment, the risk_level is set to not_assessed.

In unusual cases, an error might cause risk evaluation to fail. In this case, Stripe reports the payment as having unknown risk.

On the Charge object of an unknown risk payment, the risk_level is set to unknown.

## Searching for a specific risk level in the Dashboard

You can search for payments of a specific risk level using the risk_level search term and the desired risk level. For example, a search for risk_level:highest returns a list of all payments with a high risk level. Likewise, a search for risk_level:elevated returns a list of all payments with an elevated risk level.

[risk_level:highest](https://dashboard.stripe.com/test/search?query=risk_level%3Ahighest)

[risk_level:elevated](https://dashboard.stripe.com/test/search?query=risk_level%3Aelevated)

## Feedback on risk evaluations

While we use information across our network to evaluate a payment, you might have additional information about a payment as a result of a customer interaction. The Stripe machine learning models respond to feedback you share with us, and you can help improve our fraud detection algorithms by refunding and reporting payments that you believe are fraudulent.

[refunding](/refunds)

Refunding fraudulent payments helps improve our fraud detection algorithms and the accuracy of our risk evaluations for this payment, and similar ones in the future.

To refund a payment and mark it as fraudulent, view the payment in the Dashboard and then:

- Click Refund.

- Select Fraudulent as the Reason.

- Provide a brief explanation.

You can also indicate that a payment is fraudulent when you create a refund using the API by providing fraudulent as the value for reason. This adds the email address and card fingerprint associated with the payment to the default email address and card fingerprint block lists.

[create a refund](/api#create_refund)

[block lists](/radar/lists#default-lists)

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

For a small subset of charges, Stripe modifies the reported risk score so we can measure the performance of our models and obtain data for subsequent model development. This allows Stripe to ensure key metrics like false positive rate and recall remain within desirable ranges, and that model performance continues to improve.

If you don’t want the protection of the Stripe Radar machine learning models, you can opt out by contacting our Support team.

[contacting](https://stripe.com/contact)
