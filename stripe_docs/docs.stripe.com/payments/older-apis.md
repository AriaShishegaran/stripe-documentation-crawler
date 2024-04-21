# Older payment APIs

We’ve replaced some of our older APIs and no longer update their documentation.

## Migrate to current APIs

The older APIs are limited. To get the latest Stripe features, migrate to the Payment Intents, Setup Intents, and Payment Methods APIs. See each individual API’s docs for specifics on migrating.

[Payment Intents](/payments/payment-intents)

[Setup Intents](/payments/setup-intents)

[Payment Methods](/payments/payment-methods)

## Deprecation of the Sources API

We’ve deprecated support for local payment methods in the Sources API and plan to turn it off. If you currently handle any local payment methods using the Sources API, you must migrate them to the current APIs. We’ll communicate more information about this end of support via email.

[Sources API](/sources)

[migrate them to the current APIs](/payments/payment-methods/transitioning)

We’ve also deprecated support for card payments in the Sources API, but don’t currently plan to turn it off.

## Older APIs that remain available

Although unsupported, these APIs aren’t going away. Until you upgrade your integration, you can still use these APIs:

- Charges

[Charges](/payments/charges-api)

- ACH

[ACH](/ach-deprecated)

## Comparing the APIs

[Cards, digital wallets, bank transfers, and so on](/payments/payment-methods/overview)

[SCA-ready](/strong-customer-authentication)

[Terminal](/terminal)
