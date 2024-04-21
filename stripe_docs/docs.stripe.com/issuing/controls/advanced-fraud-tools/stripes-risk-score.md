# Stripe's risk scoreBeta

Incorporate Stripe’s risk assessment into your business needs when deciding whether to approve or reject an authorization. The following statistics provide directional guidance on the performance of our tools, dependent on what you’re optimizing for: approval rate or fraud prevention. While these settings might not be customized to your business model, geography, or cardholder behavior, you can use them as a source of directional guidance when using Stripe’s tools. Contact us for support in adjusting these thresholds.

Stripe provides a composite score and risk categorization to help you assess the risk level of an authorization. The values exist on a 0-99 scale, with higher values representing higher risk. In addition to the risk score, Stripe provides an assessment of the authorization’s riskiness in an enum value. We label every authorization as ‘normal’ or ’high’.

We recommend backtesting your data against the score to assess opportunities to use the score to drive down fraud rates. For example, you might find that fraud_score > 20 and risk_level = normal equates to particularly risky authorizations for your portfolio and opt to block authorizations that satisfy those conditions.

Precision and recall are inversely related. When you block more transactions, the false positive rate increases while the likelihood of allowing fraud decreases. When you block fewer transactions, the false positive rate decreases. Set your blocking thresholds accordingly based on rigorous backtesting of your data and your own risk tolerance.

Learn more about the Stripe’s risk score.

[Stripe’s risk score](/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-fraud_risk)

## Fraud classification

While our model is reliable, it inevitably flags:

- False positives: Non-fraudulent transactions as high risk

- False negatives: Fraudulent transactions as non-high risk

As Stripe refines the performance of its risk models, you can actively contribute to our refinement process by flagging both fraudulent transactions that we might not accurately identify and non-fraudulent transactions. You’ll also be strengthening the fraud prevention capabilities of the industry as a whole: when you flag a false negative, we send a fraud report to card networks, telling them about the fraudulent activity.

You can report false positives and false negatives while validating correct assessments (true positives and true negatives) through the Fraud Classification API. Using this API is optional for accessing Stripe’s risk score. However, your contributions  improve the model over time. Due to this, we recommend automating reporting with this API in the early stages of your implementation

[Fraud Classification API](/api/issuing/fraud_classification/create)

Learn more about the Fraud Classification API.

[Fraud Classification API](/api/issuing/fraud_classification/create)

Stripe’s risk score is currently limited to beta users. You must be an Issuing customer to join the beta. To request access to the beta, log in to your Stripe account and refresh the page. Contact Stripe for more information.

[Contact Stripe](https://stripe.com/contact/sales)