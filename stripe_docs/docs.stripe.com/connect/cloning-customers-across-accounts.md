# Clone customers across accounts

The content of this section refers to a Legacy feature. We recommend that you refer to the guide for cloning PaymentMethods instead. We don’t guarantee continued support for this feature. If you have processes that rely on it, change them.

[cloning PaymentMethods](/payments/payment-methods/connect#cloning-payment-methods)

For some business models, it’s helpful to reuse your customers’ payment information across connected accounts. For example, a customer who makes a purchase from one of your connected sellers shouldn’t need to re-enter their credit card or bank account details to purchase from another seller.

With Connect, you can accomplish this by following three steps:

[Connect](/connect)

- Storing customers, with a payment method, on the platform account.

[Storing customers](#storing-customers)

- Creating tokens to clone the payment method when it’s time to charge the customer on behalf of a connected account.

[Creating tokens](#creating-tokens)

- Creating charges using the new tokens.

[Creating charges](#creating-charges)

[Storing customers](#storing-customers)

## Storing customers

Cloning saved payment methods is only relevant when creating direct charges on connected accounts. It’s not necessary when making charges on your platform account.

[creating direct charges on connected accounts](/connect/direct-charges)

When not cloning payment methods, you save the Stripe Customer objects on each individual connected Stripe account. When cloning payment methods, you instead save them on the platform Stripe account.

[Customer objects](/api#customers)

This is an API call but be sure to use your own secret and publishable keys instead of the connect account’s.

[API call](/api#create_customer)

[Creating tokens](#creating-tokens)

## Creating tokens

If your platform uses the Sources API, you must create a Source from that customer rather than creating a token. If your platform uses the Payment Methods API, you must create a PaymentMethod from that customer. After following either of these guides, proceed to Creating charges without creating a token.

[create a Source from that customer](/sources/connect#cloning-card-sources)

[Payment Methods API](/payments/payment-methods)

[create a PaymentMethod from that customer](/payments/payment-methods/connect#cloning-payment-methods)

[Creating charges](/connect/cloning-customers-across-accounts#creating-charges)

When you’re ready to create a charge on a connected account using a customer saved on your platform account, create a new token for that purpose. You’ll need:

[create a new token](/api#create_card_token)

- The Stripe account ID of the connected account (for example, acct_RyA2sudTCTA7dfWZ) that you’re creating the charge for

- The ID of the customer in your platform account (for example, cus_Pu2VfAQCb6PxzD) being charged

- The card or bank account ID for that customer, if you want to charge a specific card or bank account rather than the default

[Creating charges](#creating-charges)

## Creating charges

With the token generated in the previous step, attach this token to a customer on the connected account.

[attach this token to a customer](/api#create_customer)

Charges that are made on the cloned customer aren’t reflected on the original customer. This feature is intended for multiple connected accounts that need to charge the same user.

If your platform uses the Payment Methods API, you must pass the payment method ID as the payment_method parameter instead of passing the source parameter.

[Payment Methods API](/payments/payment-methods)

Then, use the customer ID (for example, cus_Wf6gQJkMEPH1hO) and the payment method ID (for example, card_lyZWxYajoY6Jex) returned by the customers.create  call to charge the customer.

## See also

- Creating charges

[Creating charges](/connect/charges)

- Creating direct charges

[Creating direct charges](/connect/direct-charges)
