# Payment method settingsBeta

Render a connected account’s Payment Method Configuration to enable customization of payment methods displayed at checkout. Connected accounts can customize their checkout payment methods and provide the necessary compliance details for their usage.

[Payment Method Configuration](/api/payment_method_configurations)

This Connect embedded component is in beta. Request access below.

[Request access](/connect/supported-embedded-components/payment-method-settings#request-access)

The embedded payment method settings component is currently available for connected accounts in the US that you (the platform) collect updated information from when requirements change. This includes Custom connected accounts.

[Custom](/connect/custom-accounts)

We support the following payment methods in the embedded component:

Affirm, Afterpay Clearpay, Apple Pay, Bancontact, BLIK, Cards, EPS, giropay, Google Pay, iDEAL, Klarna, Link, P24, Sofort, and Zip.

The embedded payment method settings uses the Payment Method Configurations and Account Capabilities APIs to display a list of customizable payment methods to your connected accounts. If a connected account requires additional compliance data prior to requesting the payment method capability, the component indicates this and collects the necessary information in advance.

[Payment Method Configurations](/connect/payment-method-configurations)

[Account Capabilities](/connect/account-capabilities)

[capability](/api/capabilities/object)

## Requirements

Your integration must use dynamic payment methods to automatically apply the connected account’s preferences during checkout. In prebuilt payment UIs such as Payment Element and Checkout, Stripe handles the logic for displaying eligible payment methods for each transaction.

[dynamic payment methods](/connect/dynamic-payment-methods)

[Payment Element](https://stripe.com/payments/elements)

[Checkout](https://stripe.com/payments/checkout)

## Integrate with Payment Method Configurations

When creating an Account Session, enable payment method settings by specifying payment_method_settings in the components parameter.

[creating an Account Session](/api/account_sessions/create)

After creating the account session and initializing ConnectJS, you can render the payment method settings component in the frontend:

[initializing ConnectJS](/connect/get-started-connect-embedded-components#account-sessions)

The embedded payment method settings component respects the platform-level defaults that you configure in the Dashboard or the Payment Method Configurations API.

[Dashboard](/connect/payment-methods)

[Payment Method Configurations API](/connect/payment-method-configurations)

For payment methods that you configure as On by default or Off by default, the connected account can override that preference in the component. If you have set a payment method to Blocked, it’s completely hidden in the component.

The embedded payment method settings component currently shows the connected account’s default payment method configuration. During the beta, the component supports multiple configurations with a component attribute that accepts a configuration ID.

[multiple configurations](/connect/multiple-payment-method-configurations)

## Request early access  Beta

Sign in to request access to this Connect embedded component in beta.

[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fsupported-embedded-components%2Fpayment-method-settings)

If you don’t have a Stripe account, you can register here.

[register here](https://dashboard.stripe.com/register)

## See also

- Connect integration guide

[Connect integration guide](/connect/charges)

- Upgrading to dynamic payment methods

[Upgrading to dynamic payment methods](/connect/dynamic-payment-methods)

- Payment Method Configurations API

[Payment Method Configurations API](/connect/payment-method-configurations)

- Account Capabilities API

[Account Capabilities API](/connect/account-capabilities)
