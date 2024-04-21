# Test Financial Connections

[Get started with test mode](#get-started)

## Get started with test mode

Refer to the testing documentation to learn more about testing your Stripe integration.

[testing](/testing)

To use the test mode features of Financial Connections, follow the relevant use case guide using a test API key. Accounts and customers that you make in test mode are invisible to your live mode integration.

[use case guide](/financial-connections/use-cases)

The Financial Connections authentication flow is subject to change, so we don’t recommend automated client-side testing. Stripe’s test mode API is also strictly rate limited, which you must account for in your tests.

[authentication flow](/financial-connections/fundamentals#authentication-flow)

[rate limited](/testing#rate-limits)

[How to use test accounts and institutionsServer-side](#web-how-to-use-test-accounts)

## How to use test accounts and institutionsServer-side

When you provide Stripe.js with a Financial Connections Session token created using test keys, the authentication flow exclusively shows a selection of test institutions managed by Stripe. The client can link accounts from any of these institutions without providing credentials.

[Stripe.js](/js)

[authentication flow](/financial-connections/fundamentals#authentication-flow)

Features like balances, account ownership, and transactions work the same way as they do in live mode, except they return testing data instead of real account data.

[balances](/financial-connections/balances)

[account ownership](/financial-connections/ownership)

[transactions](/financial-connections/transactions)

Test mode webhooks are separate from live webhooks. Learn about testing your webhook integrations.

[webhooks](/webhooks)

[testing your webhook integrations](/webhooks#test-webhook)

[Testing different user authentication scenariosClient-side](#web-test-institutions)

## Testing different user authentication scenariosClient-side

Stripe provides a set of test institutions exercising different success and failure scenarios, each represented as a bank in the list of featured institutions.

- Test Institution: Simulates the user successfully logging into their institution and contains a basic set of test accounts.

- Test OAuth Institution: Contains the same test accounts as Test Institution, but instead of authenticating directly with the modal, it opens an OAuth popup for authentication.

- Ownership Accounts: Contains test accounts representing different ownership states.

- Invalid Payment Accounts: Contains test accounts that are unusable for ACH payments.

- Down bank (scheduled): The institution’s login API is unavailable for a known time period that the institution communicated to Stripe.

- Down bank (unscheduled): The institution’s login API is unavailable without any information about the downtime communicated to Stripe.

- Down bank (error): Stripe is experiencing an unknown error communicating with the institution.

We recommend manually testing OAuth and non-OAuth institutions to make sure that both UI flows work within the context your application. See additional documentation about the differences between OAuth and non-OAuth connections.

[additional documentation](/financial-connections/fundamentals#how-stripe-links-financial-accounts)
