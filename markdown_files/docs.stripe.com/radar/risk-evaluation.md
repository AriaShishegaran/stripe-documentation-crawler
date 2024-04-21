htmlRisk evaluation | Stripe Documentation[Skip to content](#main-content)Risk evaluation[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fradar%2Frisk-evaluation)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fradar%2Frisk-evaluation)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)
[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Radar](/radar)·[Home](/docs)[Get started](/docs/get-started)[Protect against fraud](/docs/radar)# Risk evaluation

Access the Stripe Radar risk evaluations in the Dashboard and the API.### Dispute liability

While Stripe Radar offers a greater ability to monitor your payments and protect your business from disputes, you’re ultimately responsible for payments you choose to accept, including those that are later disputed or found to be fraudulent.

At the core of Stripe Radar is an adaptive machine learning system that evaluates the risk level for each payment in real time. It uses hundreds of signals about each payment, and taps into data across our network of millions of businesses, to predict whether a payment is likely to be fraudulent.

Our machine learning system is flexible and responsive, continuously learns from new customer purchase patterns and transaction features, and incorporates feedback from you whenever payments are indicated as fraudulent.

NoteWhen a business using Stripe sees a card for the first time, there’s a 91% chance that we’ve seen the card elsewhere on the Stripe network in the past.

## When to use Radar

### Using Radar with Stripe Checkout or Stripe Billing

The following information also applies to transactions created through Stripe Checkout and Stripe Billing. To provide a seamless experience for your subscription customers, Radar’s fraud models only score the initial transaction of a recurring Stripe Billing subscription, but evaluates rules for all transactions.

Radar evaluates risk and runs rules for three different types of Stripe API objects: Charges, PaymentIntents and SetupIntents. Stripe designed the Radar rules to take four different actions:

- Request 3DS authentication
- Allow the creation of the object
- Block the creation of the object
- Review the creation of a Charge

The following table illustrates which rules Radar runs for each type of API object:

Transaction typeRequest 3DSAllow & BlockReviewCharge✔✔PaymentIntent✔✔✔SetupIntent✔✔You can enable Radar for SetupIntents in your Radar settings.

## Risk outcomes

### Risk score (Stripe Radar for Fraud Teams only)

With Stripe Radar for Fraud Teams, each payment also includes a risk score that ranges from 0–99 to indicate the risk level on a more granular level. By default, a score of 65 or above indicates elevated risk, while a score of 75 or above indicates high risk. You can adjust the thresholds at Risk Settings.

The Stripe machine learning models evaluate the likelihood that a payment is fraudulent. This judgment can take one of five values:

- [High risk](#high-risk)
- [Elevated risk](#elevated-risk)
- [Normal risk](#normal-risk)
- [Not evaluated](#not-evaluated)
- [Unknown risk](#unknown-risk)

Each payment includes information on the outcome of our risk evaluation.

Radar for fraud teams users will see a risk insights section on the payment page that provides more details about why we assigned a payment a particular risk level and score.

If a card issuer declines a payment, Stripe also includes any information we receive from them as part of the outcome.

The outcome for each payment is available when viewing a payment in the Dashboard or through the API as part of the Outcome attribute of the Charge object.

### High risk payments

Stripe reports payments as high risk when we believe they’re likely to be fraudulent. Payments of this risk level are blocked by default.

On the Charge object of a high risk payment, the risk_level is set to highest.

`...
"outcome":
{
  "network_status": "not_sent_to_network",
  "reason": "highest_risk_level",
  "risk_level": "highest",
  "risk_score": 92, // Provided only with Stripe Radar for Fraud Teams
  "seller_message": "Stripe blocked this charge as too risky.",
  "type": "blocked",
}
...`If Stripe Radar ever blocks a payment that you know is legitimate, you can remove the block using the Dashboard. To do this, view the payment in the Dashboard and click Add to allow list. Adding a payment to the allow list doesn’t retry the payment, but it does prevent Stripe Radar from blocking future payment attempts with that card or email address.

NoteDon’t see Add to allow list? Contact Stripe to have this feature added to your Radar account.

### Elevated risk payments

Elevated risk payments have an increased chance of being fraudulent. Stripe Radar allows payments of this risk level by default. Stripe Radar for Fraud Teams automatically places elevated risk payments into your review queue so you can take a closer look.

On the Charge object of an elevated risk payment, the risk_level is set to elevated.

`...
"outcome": {
  "network_status": "approved_by_network",
  "reason": "elevated_risk_level",
  "risk_level": "elevated",
  "risk_score": 56, // Provided only with Stripe Radar for Fraud Teams
  "seller_message": "Stripe evaluated this charge as having elevated risk, and placed it in your manual review queue.",
  "type": "manual_review"
}
...`### Normal risk payments

Payments with a normal risk evaluation have fewer characteristics that are strongly indicative of fraud than payments with elevated or high risk levels. However, we recommend that you continue to be vigilant when fulfilling these orders. Payments that have normal risk can still turn out to be fraudulent and there are other possible types of fraud that can occur later on in the order process.

On the Charge object of a successful payment with normal risk, the risk_level is set to normal.

`...
"outcome":
{
  "network_status": "approved_by_network",
  "reason": null,
  "seller_message": "The charge was authorized.",
  "risk_level": "normal",
  "risk_score": 23, // Provided only with Stripe Radar for Fraud Teams
  "type": "authorized",
}
...`### Not evaluated

The Risk level is set to not_assessed for non-card payments, card-based payments predating the public assignment of risk levels, and for payments where the merchant opts out of Radar fraud risk assessment.

On the Charge object of an unevaluated payment, the risk_level is set to not_assessed.

`...
"outcome": {
  "network_status": "approved_by_network",
  "reason": "not_assessed_risk_level",
  "risk_level": "not_assessed",
  "seller_message": "Your business has opted out of Radar fraud risk assessments.",
  "type": "authorized"
}
...`### Unknown risk payments

In unusual cases, an error might cause risk evaluation to fail. In this case, Stripe reports the payment as having unknown risk.

On the Charge object of an unknown risk payment, the risk_level is set to unknown.

`...
"outcome": {
  "network_status": "approved_by_network",
  "reason": "unknown_risk_level",
  "risk_level": "unknown",
  "seller_message": "Something went wrong while evaluating this payment. Our engineers have been notified and we’ll look into this as soon as possible.",
  "type": "authorized"
}
...`## Searching for a specific risk level in the Dashboard

You can search for payments of a specific risk level using the risk_level search term and the desired risk level. For example, a search for risk_level:highest returns a list of all payments with a high risk level. Likewise, a search for risk_level:elevated returns a list of all payments with an elevated risk level.

## Feedback on risk evaluations

While we use information across our network to evaluate a payment, you might have additional information about a payment as a result of a customer interaction. The Stripe machine learning models respond to feedback you share with us, and you can help improve our fraud detection algorithms by refunding and reporting payments that you believe are fraudulent.

Refunding fraudulent payments helps improve our fraud detection algorithms and the accuracy of our risk evaluations for this payment, and similar ones in the future.

To refund a payment and mark it as fraudulent, view the payment in the Dashboard and then:

1. ClickRefund.
2. SelectFraudulentas theReason.
3. Provide a brief explanation.

You can also indicate that a payment is fraudulent when you create a refund using the API by providing fraudulent as the value for reason. This adds the email address and card fingerprint associated with the payment to the default email address and card fingerprint block lists.

[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

# If you haven't refunded the charge, you can do so and let Stripe
# know it was fraudulent in one step.
Stripe::Refund.create({
  charge: '{{CHARGE_ID}}',
  reason: 'fraudulent',
})

# If you already refunded the charge (without specifying the
# 'fraudulent' reason), you can still let us know it was fraudulent.
Stripe::Charge.update(
  '{{CHARGE_ID}}',
  {
    fraud_details: {
      user_report: 'fraudulent',
    },
  }
)`For a small subset of charges, Stripe modifies the reported risk score so we can measure the performance of our models and obtain data for subsequent model development. This allows Stripe to ensure key metrics like false positive rate and recall remain within desirable ranges, and that model performance continues to improve.

If you don’t want the protection of the Stripe Radar machine learning models, you can opt out by contacting our Support team.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[When to use Radar](#when-to-use-radar)[Risk outcomes](#risk-outcomes)[Searching for a specific risk level in the Dashboard](#searching-for-a-specific-risk-level-in-the-dashboard)[Feedback on risk evaluations](#feedback-on-risk-evaluations)Products Used[Radar](/radar)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`