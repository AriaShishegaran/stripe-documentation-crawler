# Upgrade your onramp integrationBeta

Follow this guide if you integrated with the onramp API before 2023-06-21

We made changes to the Stripe fiat-to-crypto onramp API as part of our public release. If you integrated with onramp before 2023-06-21, you’re integrated with the beta onramp API.

This guide covers the changes made, impact to existing integrations, and instructions for migrating to this latest version.

## Changes from the onramp beta

- Flatted transaction_details into the top-level POST /v1/crypto/onramp_sessions request body

- Renamed the following fields in onramp API requests and resourcessupported_destination_currencies is now destination_currenciessupported_destination_networks is now destination_networkssource_exchange_amount is now source_amountdestination_exchange_amount is now destination_amount

- supported_destination_currencies is now destination_currencies

- supported_destination_networks is now destination_networks

- source_exchange_amount is now source_amount

- destination_exchange_amount is now destination_amount

- Changed the onramp quotes path from /v1/crypto/onramp/quotes to /v1/crypto/onramp_quotes

Examples of what the changes look like in onramp request and responses follow:

Request

Response

Request

Response

## Impact to existing integrations

We released these changes in a way that does not break existing beta integrations. Please get in touch with us if you have any issues with your integration.

[get in touch with us](https://support.stripe.com/)

## Migrating from beta to the latest onramp version

Only follow this section if:

- Your onramp onboarding application was approved before 2023-06-21 OR

- You integrated with onramp before 2023-06-21

Otherwise these instructions don’t apply to you since you’re already on the latest onramp version.

If you want to upgrade your API version, start specifying the crypto_onramp_beta=v2 as part of the Stripe-Version header in your requests.

Beta integrations can now pass a crypto_onramp_beta version as part of the Stripe-Version header to consume either the beta or latest onramp API version. Use the following matrix to determine what behavior to expect based on the Stripe-Version header passed.

If you’d like to upgrade your API version, start specifying the crypto_onramp_beta=v2 as part of the Stripe-Version header in your requests.
