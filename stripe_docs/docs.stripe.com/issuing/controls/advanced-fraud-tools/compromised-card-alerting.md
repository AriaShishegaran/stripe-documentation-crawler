# Compromised card alertingBeta

Canceling a card suspected to be compromised can help you prevent subsequent abuse of PANs that have been compromised after the initial fraudulent activity. You can use these indicators to initiate communications and a reissuance workflow for cardholders. If Stripe observes a valid PAN successfully used in a card testing attack through an approved authorization, we flag the card as possibly compromised.

## Mitigate risk and take action

When Stripe observes a successful authorization during a severe card testing attack (defined as risk_assessment.card_testing_risk.risk_level set to elevated or highest), the fraud_warning.type field in the card’s object populates as card_testing_exposure. The started_at value corresponds to the date that the successful authorization in card testing attack took place. When a card has been impacted multiple times in a card testing attack, the value defaults to the first time stamp of the first incident.

After Stripe populates the type field with card_testing_exposure, we recommend contacting the cardholder, canceling the card, and issuing a new one. This mitigates the risk of subsequent authorizations on what a fraudulent actor likely assumes is a valid PAN that they can abuse.

Learn more about compromised card alerting

[compromised card alerting](/api/issuing/cards/object#issuing_card_object-fraud_warning)

Compromised card alerting is currently limited to beta users. You must be an Issuing customer to join the beta. To request access to the beta, log in to your Stripe account and refresh the page. Contact Stripe for more information.

[Contact Stripe](https://stripe.com/contact/sales)
