# Embed the payment methods settings componentBeta

After you integrate with dynamic payment methods, you can embed the payment methods settings component into your website to allow your users to manage their payment methods without the need to access the Stripe Dashboard.

[dynamic payment methods](/connect/dynamic-payment-methods)

The component uses the Payment Method Configurations and Account Capabilities APIs to capture your connected accounts’ payment method setting preferences. The component is a low-code, customizable alternative to building a custom payment method settings UI for your connected accounts.

[Payment Method Configurations](/connect/payment-method-configurations)

[Account Capabilities](/connect/account-capabilities)

[Enable dynamic payment methods](#enable-dynamic-payment-methods)

## Enable dynamic payment methods

Follow the steps in upgrading to dynamic payment methods.

[upgrading to dynamic payment methods](/connect/dynamic-payment-methods)

[Integrate with Connect embedded components](#integrate-with-connect-embedded-components)

## Integrate with Connect embedded components

Request access to the embedded component beta and learn how to integrate with Payment Method Configurations.

[Request access](/connect/supported-embedded-components/payment-method-settings#request-access)

[integrate with Payment Method Configurations](/connect/supported-embedded-components/payment-method-settings#integration)

[Have your connected accounts enable payment methods](#have-your-connected-accounts-enable-payment-methods)

## Have your connected accounts enable payment methods

Your connected accounts can use the component to enable payment methods and provide compliance information without the need to access the Stripe Dashboard. If a connected account needs to provide additional compliance information to use a payment method, the component prompts them for the information and collects it up-front.

The embedded payment method settings component is currently available for connected accounts in the US that you (the platform) collect updated information from when requirements change. This includes Custom connected accounts.

[Custom](/connect/custom-accounts)

We support the following payment methods in the embedded component:

Affirm, Afterpay Clearpay, Apple Pay, Bancontact, BLIK, Cards, EPS, giropay, Google Pay, iDEAL, Klarna, Link, P24, Sofort, and Zip.

## See also

- Connect integration guide

[Connect integration guide](/connect/charges)

- Upgrading to dynamic payment methods

[Upgrading to dynamic payment methods](/connect/dynamic-payment-methods)
