# Making API calls for connected accounts

You can make API calls for your connected accounts:

- Server-side with the Stripe-Account header and the connected account ID, per request

[Stripe-Account header](#stripe-account-header)

- Client-side by passing the connected account ID as an argument to the client library

To optimize performance and reliability, Stripe has established rate limits and allocations for API endpoints.

[rate limits and allocations](/rate-limits)

## Adding the Stripe-Account header server-side

For server-side API calls, you can make requests as connected accounts using the special header Stripe-Account with the Stripe account identifier (it starts with the prefix acct_) of your platform user. Here’s an example that shows how to Create a PaymentIntent with your platform’s API secret key and your user’s Account identifier.

[Create a PaymentIntent](/api/payment_intents/create)

[API secret key](/keys)

[Account](/api/accounts)

In the latest version of the API, specifying the automatic_payment_methods parameter is optional because Stripe enables its functionality by default.

The Stripe-Account header approach is implied in any API request that includes the Stripe account ID in the URL. Here’s an example that shows how to Retrieve an account with your user’s Account identifier in the URL.

[Retrieve an account](/api/accounts/retrieve)

[Account](/api/accounts)

All of Stripe’s server-side libraries support this approach on a per-request basis:

## Adding the connected account ID to a client-side application

Client-side libraries set the connected account ID as an argument to the client application:

The JavaScript code for passing the connected account ID client-side is the same for plain JS and for ESNext.

## See also

- Creating charges

[Creating charges](/connect/charges)

- Using subscriptions

[Using subscriptions](/connect/subscriptions)
