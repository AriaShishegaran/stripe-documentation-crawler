# Authorization signalsBeta

## Verification data

For every authorization that takes place, we compare the values provided during checkout with the ones on file. We notify you if we detect a mismatch on:

- CVV2 (or security code)

- Card expiration date

- Billing address

- Billing zip code

- PIN number (when entered)

Identifying a mismatch between the card details on file and those entered at checkout may help you identify fraudulent activity. For example:

- A mismatch between the billing zip code and the one provided at checkout might represent a card that’s been stolen by a bad actor who’s unaware of the cardholder’s zip code and attempts to use the card to make a purchase.

- A mismatch between the CVV2 on file and the one entered at checkout might represent a bad actor cycling through card numbers to find one that works, without knowledge of the CVV associated with it.

Depending on your risk tolerance and the characteristics of the authorization, such as whether it’s in person or online, you can reject authorizations if any mismatches are identified in the verification data values.

## Fraud disputability assessment

Stripe’s fraud disputability assessment evaluates whether an authorization can be disputed in the event of fraud.

Having the confidence to determine whether or not you can dispute an authorization in the event of fraud at the time of authorization allows you to make informed decisions. For example, consider an authorization that is otherwise classified as “medium risk”:

- If you know that you can dispute the authorization if fraud occurs, you can approve it

- If you know that you can’t dispute the authorization (if fraud occurs), you can decline it or only approve a lower amount than what’s requested

Stripe assesses disputability likelihood by comparing the characteristics of the authorization (such as whether 3DS was used or if the card was present with a chip). We make this assessment against network rules for disputes to proactively determine what would happen in the event of a dispute.

To determine the disputability likelihood of an authorization in the event of fraud, examine the fraud_disputability_likelihood field on the Authorization object. This field will populate with various enums that inform you about whether the authorization can be disputed. We label every authorization as very_likely, neutral, or very_unlikely, or unknown:

[fraud_disputability_likelihood](/api/issuing/authorizations/object#issuing_authorization_object-fraud_disputability_likelihood)

- When authorizations receive a score of very_likely, it’s highly probable that disputes filed based on these authorizations are accepted by the card network. The card network rarely rejects very_likely authorization disputes. When they do, it’s typically due to exceptional circumstances. These circumstances might include a card filing a fraud dispute for the second time or exceeding the allowable number of disputes for a card within a specific timeframe defined by Visa.

- When authorizations receive a score of very_unlikely, disputes are almost always automatically rejected by the card network.

- When authorizations receive a score of neutral, Stripe assesses that the dispute outcome depends on various factors. Historically, these disputes are more likely to be accepted by the card network. However, this behavior might change at any given point.

Learn more about fraud disputability likelihood.

[fraud disputability likelihood](/api/issuing/authorizations/object#issuing_authorization_object-fraud_disputability_likelihood)

## High-risk merchant alerts

Use webhook notifications to receive detailed risk assessments of the acquiring merchant involved in an authorization.

If you have data on the risk level of a merchant and the likelihood of a dispute, you can make more informed decisions about which authorizations you approve or reject. To make this assessment, Stripe evaluates all of the acquiring transaction activity for a merchant on Stripe Issuing, including data such as its historical dispute rate.

To determine the risk level, examine the risk_assessment.merchant_dispute_risk hash field on the Authorization object. The following example demonstrates how to use each value.

[risk_assessment.merchant_dispute_risk](/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-merchant_risk)

A low (normal) risk transaction

A high-risk transaction

Learn more about merchant dispute risk.

[merchant dispute risk](/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-merchant_dispute_risk)

## Card testing risk

Card testing is a prevalent form of fraud where malicious actors test stolen card numbers or cycle through Primary Account Numbers (PANs) until they find a valid one. They use this valid PAN at a business with weak verification controls. To counteract this, Stripe assesses the likelihood of your involvement in a card testing attack, takes action on your behalf, and notifies you through the API about the severity of the incident. Additionally, we assess if any cards may have been compromised during the attack.

Stripe automatically intervenes in the most obvious card testing scenarios. We offer a balanced approach in medium-risk situations to avoid being overly conservative. These cases require careful consideration of various factors, including the authorization and cardholder details. As a result, we recommend the careful evaluation of all relevant considerations before making a decision on whether to block an authorization.

We assess card testing risk by, among other things, evaluating the frequency and intensity of “card does not exist” declines associated with a specific Bank Identification Number (BIN) and/or merchant. These declines are the most definitive significant indicator because they often exhibit a noticeable increase in speed and frequency compared to regular card declines.

To determine card testing risk, examine the risk_assessment.card_testing_risk field on the Authorization object. The following example demonstrates how to use each value.  We also provide the following fields:

[risk_assessment.card_testing_risk](/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-card_testing_risk)

- invalid_account_number_decline_rate_past_hour: Stripe calculates and returns this value when a decline contains a non-existent PAN.

- invalid_credentials_decline_rate_past_hour: Stripe calculates and returns this value on declines where the PAN exists (or existed in the past), but other verifications such as the CVV, expiration, and postal code are failing.

A low risk transaction

A high-risk transaction

Learn more about card testing risk.

[card testing risk](/api/issuing/authorizations/object#issuing_authorization_object-risk_assessment-card_testing_risk)

## Recommended settings

To get started, enable the following settings that align with your business needs. While these settings might not be customized to your business model, geography, or cardholder behavior, you can use them as a source of directional guidance when using Stripe’s tools. Contact us for support in adjusting these thresholds.

Authorization signals are currently limited to beta users. You must be an Issuing customer to join the beta. To request access to the beta, log in to your Stripe account and refresh the page. Contact Stripe for more information.

[Contact Stripe](https://stripe.com/contact/sales)
