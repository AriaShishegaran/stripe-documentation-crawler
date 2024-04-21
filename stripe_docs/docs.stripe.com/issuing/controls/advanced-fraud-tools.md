# Advanced fraud toolsBeta

Stripe Issuing’s advanced fraud tools help you identify and prevent transaction fraud. Use our real-time webhook functionality to approve or reject authorizations with the API.

This guide helps you understand how to use these signals and features to drive down transaction fraud while minimizing impact on legitimate transactions.

## Overview

Use Issuing’s fraud tools to gain unrestricted access to the following API-based signals on a per-authorization or per-card basis:

[3D Secure (3DS)](/issuing/3d-secure)

[Stripe Defense Layer](#stripe-defense-layer)

[Fraud challenges](#fraud-challenges)

- Verification data

[Verification data](/issuing/controls/advanced-fraud-tools/authorization-signals#verification-data)

- Fraud disputability likelihood

[Fraud disputability likelihood](/issuing/controls/advanced-fraud-tools/authorization-signals#fraud-disputability-assessment)

- High risk merchant alerts

[High risk merchant alerts](/issuing/controls/advanced-fraud-tools/authorization-signals#high-risk-merchant-alerts)

- Card testing risk

[Card testing risk](/issuing/controls/advanced-fraud-tools/authorization-signals#card-testing-risk)

[Compromised card alerting](#compromised-alerting)

## Integration

To make informed decisions during authorization, update your real-time webhook authorization logic to incorporate these signals. Learn more about our recommended settings.

[real-time webhook authorization logic](/issuing/controls/real-time-authorizations/quickstart)

[our recommended settings](#recommended-settings)

## Full suite of fraud controls

Stripe provides access to fraud-adjacent features such as spending controls, dispute filing, token management, and card management tools. Learn how to manage fraud with Stripe Issuing’s full suite of controls and tools.

[manage fraud with Stripe Issuing’s full suite of controls and tools](/issuing/manage-fraud)

## 3D Secure (3DS)

3DS uses multi-factor authentication to reduce fraud for online transactions where a card isn’t physically present. It’s triggered by businesses in online checkout flows, and requires multi-factor authentication (usually through SMS or email-based one-time passcode that Stripe sends) to complete.

In most cases, merchants are responsible for online fraud losses in card-not-present transactions. To protect themselves, businesses can trigger 3DS verification to reduce the chances of accepting a fraudulent transaction. If a merchant triggers 3DS verification, the cardholder needs to complete the verification step if your Stripe cards are enrolled in 3DS. In the UK and EU, 3DS is the standard for implementing the regulatory requirements of Strong Customer Authentication (SCA).

You must request enrollment of your Issuing account through Support to use 3DS. Once enrolled, your cards will be set up to trigger additional verification on authorizations in which a merchant requests 3DS.

Learn more about Cardholder authentication using 3D Secure.

[Cardholder authentication using 3D Secure](/issuing/3d-secure)

## Stripe Defense Layer

Stripe’s proprietary monitoring can help identify transactions that are very likely to be high risk and decline them before they can impact your bottom line. All Issuing users are enabled on the Stripe Defense Layer, which provides several automatic controls to help reduce your fraud exposure without changing loss liability. Among other considerations, Stripe attempts to block authorizations that:

- Appear to be card testing

- Seem extremely high risk based on our risk modeling

These defenses typically impact a very small subset (less than 0.5%) of authorizations.

## Fraud challenges

Fraud challenges provide you with the ability to request additional, SMS-based verification in situations where you prefer not to outright decline a potentially risky authorization.

False positive declines can occur in the practice of fraud protection. To allow for cardholders to override potential false-positive declines and limit card disruption for them, you can trigger SMS based verification.

SMS verification functions as an override option to a decline. For cardholders, the workflow consists of the following steps:

- Attempt an authorization, but receive a decline.

- Successfully complete an SMS verification prompt (sent to the cardholder’s phone number on file with Stripe).

- Try the authorization again and receive approval.

To enable this workflow, use either Stripe-managed SMS prompts or user-managed SMS prompts:

Stripe automatically triggers SMS verification for authorizations that we consider high risk. If the cardholder successfully completes the verification within 60 minutes, the merchant cardholder combination is allow-listed for 7 days to complete subsequent authorizations and override risk-specific declines. We recommend using this option if you’re an Issuing user who’s comfortable with Stripe’s risk thresholds and would prefer if Stripe managed the process of reconciling post-verification authorization against the status of the SMS alert.

You can respond to an authorization webhook with a decline decision and a request for SMS verification. In these scenarios, you can define your own logic to trigger SMS prompts. We recommend using this option if you’re an Issuing user who prefers to own the logic that triggers SMS prompts.

Learn more about the Fraud challenge flow and how to define your own logic.

[Fraud challenge flow](/issuing/controls/fraud-challenges)

[define your own logic](/issuing/controls/fraud-challenges)

## Authorization signals

At authorization, we provide a comprehensive set of signals which you can use to make informed decisions via real-time webhooks.

Learn more about Authorization signals.

[Authorization signals](/issuing/controls/advanced-fraud-tools/authorization-signals)

## Stripe’s risk score

Stripe uses a variety of risk signals to assess the risk level of an authorization then makes this assessment available to you via API. You can incorporate Stripe’s assessment into your decision logic when determining whether to approve or reject an authorization.

Learn more about Stripe’s risk score.

[Stripe’s risk score](/issuing/controls/advanced-fraud-tools/stripes-risk-score)

## Compromised card alerting

Stripe notifies you through the API when we believe a card may have been compromised. This allows you to cancel and reissue a card, file disputes, or notify a cardholder.

Canceling a card suspected to be compromised can help you prevent subsequent fraudulent use of PANs that have been compromised after the initial fraudulent activity. You can use these indicators to initiate communications and a reissuance workflow for cardholders. If Stripe observes a valid PAN successfully used in a card testing attack through an approved authorization, we flag the card as possibly compromised.

When Stripe observes a successful authorization during a severe card testing attack (defined as risk_assessment.card_testing_risk.risk_level set to elevated or highest), the fraud_warning.type field in the card’s object populates as card_testing_exposure. The started_at value corresponds to the date that the successful authorization in card testing attack took place. When a card has been impacted multiple times in a card testing attack, the value defaults to the first time stamp of the first incident. After Stripe populates the type field with card_testing_exposure, we recommend contacting the cardholder, canceling the card, and issuing a new one. This mitigates the risk of subsequent authorizations on what a fraudulent actor likely assumes is a valid PAN that they can fraudulently use.

Learn more about Compromised card alerting.

[Compromised card alerting](/issuing/controls/advanced-fraud-tools/compromised-card-alerting)

To get started, enable the following settings that align with your business needs. While these settings might not be customized to your business model, geography, or cardholder behavior, you can use them as a source of directional guidance when using Stripe’s tools. Contact us for support in adjusting these thresholds.

[3D Secure (3DS)](/issuing/3d-secure)

[Real-time webhook](/issuing/controls/real-time-authorizations)

[Stripe Defense Layer](#stripe-defense-layer)

[Fraud challenges](/issuing/controls/fraud-challenges)

[Stripe’s risk score](/issuing/controls/advanced-fraud-tools/stripes-risk-score)

[Compromised card alerting](/issuing/controls/advanced-fraud-tools/compromised-card-alerting)

Issuing advanced fraud tools are currently limited to beta users. You must be an Issuing customer to join the beta. To request access to the beta, log in to your Stripe account and refresh the page. Contact Stripe for more information.

[Contact Stripe](https://stripe.com/contact/sales)
