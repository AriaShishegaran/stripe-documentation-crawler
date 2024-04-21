# Cross-border payoutsUS only

Cross-border payouts enable you to pay sellers, freelancers, content creators, and service providers in their local currencies. You can transfer funds to connected accounts in other countries with your existing platform account and charge configuration.

[payouts](/payouts)

## Fund flow restrictions

The following fund flows are generally supported in countries for cross-border payouts:

- Separate charges and transfers without the on_behalf_of parameter

[Separate charges and transfers](/connect/separate-charges-and-transfers)

- Top-ups and transfers

[Top-ups and transfers](/connect/top-ups)

- Destination charges

[Destination charges](/connect/destination-charges)

Direct charges and destination charges with the on_behalf_of parameter aren’t supported. However, some countries have additional limitations.

For Brazil, India, and Thailand, only the following fund flows are supported:

[India](https://support.stripe.com/questions/stripe-india-support-for-marketplaces)

[Thailand](https://support.stripe.com/questions/stripe-thailand-support-for-marketplaces)

- Separate charges and transfers without the on_behalf_of parameter

[Separate charges and transfers](/connect/separate-charges-and-transfers)

- Top-up and transfers

## Supported countries

Cross-border payouts enable US platforms using separate charges and transfers, destination charges, or top-ups to pay out to connected accounts in the following countries:

* Bank accounts in countries with an asterisk (*) can only receive Euro (EUR) payouts.

Stripe might pause payouts to countries in the preview program while any issues are resolved. We don’t provide advance notice to you as the owner of the platform or to the owners of your connected accounts.

Some countries have special requirements for payments received from outside their country’s borders, or limitations on the supported fund flows. Those countries might also have higher minimum payout amounts.

[special requirements](/connect/cross-border-payouts/special-requirements)

[minimum payout amounts](/payouts#cbp-minimum-payout-amounts)

Stripe isn’t responsible for providing direct support for accounts on the recipient service agreement. However, the platform can reach out to Stripe for support for these accounts.

[recipient service agreement](/connect/service-agreement-types#recipient)

## Restrictions and requirements

- The platform must be in the US.

- Funds must come from separate charges and transfers, destination charges without on_behalf_of (OBO), or top-ups.

- The platform must be the business of record. Consequently, destination charges with on_behalf_of (OBO) aren’t supported.

[destination charges with on_behalf_of (OBO)](/connect/destination-charges#settlement-merchant)

- Connected accounts must onboard under the recipient service agreement. That means transfers to recipient accounts take an extra 24 hours to become available in the connected account’s balance.

[recipient service agreement](/connect/service-agreement-types#recipient)

- US connected accounts don’t support cross-border payouts; onboard US connected accounts using the full terms of service.

[terms of service](/connect/service-agreement-types)

- You can’t make cross-border instant payouts.

[instant payouts](/connect/instant-payouts)

The onboarding specifications for cross-border payouts vary by destination country. To learn more, see:

- Required verification information

[Required verification information](/connect/required-verification-information)

- Supported settlement currencies

[Supported settlement currencies](/connect/payouts-connected-accounts#supported-settlement)

- Bank account formats

[Bank account formats](/connect/payouts-bank-accounts)

## Get started

Existing Connect platforms - Select the recipient service agreement at account creation.

[Select the recipient service agreement](/connect/service-agreement-types#choosing-type)

New Connect platforms - Follow one of the guides below that best fits your use case, and make sure to specify the recipient service agreement in the account creation step.

[specify the recipient service agreement](/connect/service-agreement-types#choosing-type)

- Collect payments and then pay out

[Collect payments and then pay out](/connect/collect-then-transfer-guide)

- Pay out money

[Pay out money](/connect/add-and-pay-out-guide)
