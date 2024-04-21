# Insights

Stripe Identity’s machine learning system considers a variety of signals when verifying a user’s identity. It examines a number of factors to produce insights that can give further clarity into Stripe’s decision.

These insights are more nuanced than the top-level verification decisions, and you can use them to assist with manual reviews or customer support processes.

- Insights: The name Stripe uses to refer to the collection of all insights.

- Insight: The specific attribute scored (for example, blur, authenticity). It’s of either type Level or Label.Level: These insights provide a computed level, which is a score that translates to low, elevated, or high. Insights of this type evaluate the potential risk to verification.Label: These insights provide a binary value of being either present or absent. Some of these insights evaluate a potential risk to verification, but others might be neutral, with no inherent risk associated with them.

- Level: These insights provide a computed level, which is a score that translates to low, elevated, or high. Insights of this type evaluate the potential risk to verification.

- Label: These insights provide a binary value of being either present or absent. Some of these insights evaluate a potential risk to verification, but others might be neutral, with no inherent risk associated with them.

## Document insights

These are the insights produced on document checks:

[document checks](/identity/verification-checks?type=document)

## Selfie insights

These are the insights produced on selfie checks:

[selfie checks](/identity/verification-checks?type=selfie)

## Dashboard usage

The Dashboard page for a submitted VerificationSession contains a panel showing the insights generated for this session.
