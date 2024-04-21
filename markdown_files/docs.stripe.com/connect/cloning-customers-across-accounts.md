htmlClone customers across accounts | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcloning-customers-across-accounts)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fcloning-customers-across-accounts)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Clone customers across accounts

With Connect, you can clone your customers' payment information across multiple connected accounts for reuse.CautionThe content of this section refers to a Legacy feature. We recommend that you refer to the guide for cloning PaymentMethods instead. We don’t guarantee continued support for this feature. If you have processes that rely on it, change them.

For some business models, it’s helpful to reuse your customers’ payment information across connected accounts. For example, a customer who makes a purchase from one of your connected sellers shouldn’t need to re-enter their credit card or bank account details to purchase from another seller.

With Connect, you can accomplish this by following three steps:

1. [Storing customers](#storing-customers), with a payment method, on the platform account.
2. [Creating tokens](#creating-tokens)to clone the payment method when it’s time to charge the customer on behalf of a connected account.
3. [Creating charges](#creating-charges)using the new tokens.

[Storing customers](#storing-customers)Cloning saved payment methods is only relevant when creating direct charges on connected accounts. It’s not necessary when making charges on your platform account.

When not cloning payment methods, you save the Stripe Customer objects on each individual connected Stripe account. When cloning payment methods, you instead save them on the platform Stripe account.

This is an API call but be sure to use your own secret and publishable keys instead of the connect account’s.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  --data-urlencode email="paying.user@example.com" \
  -d source=tok_mastercard`[Creating tokens](#creating-tokens)CautionIf your platform uses the Sources API, you must create a Source from that customer rather than creating a token. If your platform uses the Payment Methods API, you must create a PaymentMethod from that customer. After following either of these guides, proceed to Creating charges without creating a token.

When you’re ready to create a charge on a connected account using a customer saved on your platform account, create a new token for that purpose. You’ll need:

- The Stripe account ID of the connected account (for example,`acct_Zu08o4YmfJ28lD7u`) that you’re creating the charge for
- The ID of the customer in your platform account (for example,`cus_CoX5eVI25ysdhn`) being charged
- The card or bank account ID for that customer, if you want to charge a specific card or bank account rather than the default

Command Line[curl](#)`curl https://api.stripe.com/v1/tokens \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d customer={{CUSTOMER_ID}}`[Creating charges](#creating-charges)With the token generated in the previous step, attach this token to a customer on the connected account.

CautionCharges that are made on the cloned customer aren’t reflected on the original customer. This feature is intended for multiple connected accounts that need to charge the same user.

CautionIf your platform uses the Payment Methods API, you must pass the payment method ID as the payment_method parameter instead of passing the source parameter.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d source={{TOKEN_ID}}`Then, use the customer ID (for example, cus_5rzjSBqvmJ6LIU) and the payment method ID (for example, card_P6S9OF1CN48wSo) returned by the customers.create  call to charge the customer.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d amount=999 \
  -d currency=usd \
  -d "payment_method_types[]"=card \
  -d customer={{CUSTOMER_ID}} \
  -d payment_method={{PAYMENT_METHOD_ID}}`## See also

- [Creating charges](/connect/charges)
- [Creating direct charges](/connect/direct-charges)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Storing customers](#storing-customers)[Creating tokens](#creating-tokens)[Creating charges](#creating-charges)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`