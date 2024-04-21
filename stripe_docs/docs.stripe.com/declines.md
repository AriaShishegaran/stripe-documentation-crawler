# Declines

Track your decline rate over time to identify potential fraud or integration issues. For a clearer overview of your authorization rates, analyze unique declines and exclude failed retries from your analysis.

Payments can fail for a variety of reasons, including some that help prevent fraudulent transactions. Stripe works to reduce decline rates across all supported payment methods. We work with issuers and networks to improve acceptance rates, often without affecting your integration.

There are three reasons why a payment might fail:

- Issuer declines

[Issuer declines](/declines#issuer-declines)

- Blocked payments

[Blocked payments](/declines#blocked-payments)

- Invalid API calls

[Invalid API calls](/declines#invalid-api-calls)

You need to handle each type of payment failure differently. For every failure, you can use the Dashboard or API to review a payment’s details. When using the API, look at the Charge object’s outcome. This attribute covers the payment failure type and provides information about its cause.

[Dashboard](https://dashboard.stripe.com/payments)

[outcome](/api/charges/object#charge_object-outcome)

Stripe handles non-card payment method declines similarly to card declines. Stripe sends you a response code that includes information about the decline, for example, if it’s due to insufficient funds, a lost or stolen card, or another reason.

## Issuer declines

When your customer’s card issuer receives a charge, their automated systems and models decide whether to authorize it. These tools analyze signals such as spending habits, account balance, and card data (expiration date, address information, and CVC).

If the card issuer declines a payment, Stripe shares with you all of the decline information we receive. This information is available in the Dashboard and through the API. When issuers provide specific explanations, such as an incorrect card number or low funds, these explanations return to Stripe through decline codes.

[decline codes](/declines/codes)

## Blocked payments

Stripe Radar blocks high risk payments, such as those with mismatched CVC or postal code values. This automated fraud prevention product evaluates each payment, without requiring any action from you.

[Stripe Radar](/radar)

A payment that Radar declined

When Stripe blocks a payment, it obtains initial authorization from the card issuer but refrains from charging the card. This precaution helps prevent potential fraudulent payments that might lead to disputes.

For some card types, customers might see the card issuer’s authorization for the payment amount on their statement. However, Stripe hasn’t charged this amount or withdrawn funds. The card issuer typically removes this authorization from the customer’s statement within a few days.

If you recognize a blocked payment as legitimate, you can lift the block by locating the payment in the Dashboard and clicking Add to allow list. This action doesn’t retry the payment but prevents Stripe Radar from blocking future payment attempts using the same card or email address.

[Dashboard](https://dashboard.stripe.com/payments)

Don’t see the Add to allow list button on the payment details page? Contact Stripe to add this feature to your Radar account.

[Contact Stripe](https://support.stripe.com/email)

When using the API, the outcome of a blocked payment reflects the type of payment failure and the reason for it, along with the evaluated risk level.

## Invalid API calls

In the API, you might see an invalid API call like the following:

The invalid API call generates an error response that might look like this:

[https://stripe.com/docs/error-codes/invalid-number](https://stripe.com/docs/error-codes/invalid-number)

The outcome of a declined payment includes the type of payment failure and the reason, based on the card issuer’s decline code. The reason might contain information other than the issuer’s response code, for example, if a Radar rule evaluation blocked the charge.

[outcome](/api#charge_object-outcome)

[reason](/api#charge_object-outcome-reason)

As you develop your Stripe integration, continuously test it to identify any potential bugs that might lead to invalid API calls. Invalid API calls typically don’t result in a payment appearing in your Dashboard. However, you might see the payment appear in a few cases.

[test](/testing)

## See also

- Card declines

[Card declines](/declines/card)

- Test declined payments

[Test declined payments](/testing?testing-method=card-numbers#declined-payments)

- Refund and cancel payments

[Refund and cancel payments](/refunds)
