# Link with Checkout

You can also use Link with Payment Links.

[Payment Links](/payment-links)

Checkout is a prebuilt payment form that you can embed on your site or use as a Stripe-hosted payment page. Use Link with Checkout to allow your customers to securely save and reuse their payment information. For logged-in customers already using Link, it autofills this information regardless of whether they initially saved it on a different business’s checkout page.

[prebuilt payment form](/payments/checkout)

Checkout supports Link with no additional fees, and the same pricing applies as for other card payments.  Turn Link on and off in your payment method settings.  Learn more about what Link is and how it works.

[pricing](https://stripe.com/pricing)

[payment method settings](https://dashboard.stripe.com/settings/payment_methods)

[what Link is](/payments/link/what-is-link)

Add Link to your prebuilt checkout page

## Before you begin

Build an integration to accept a payment using Checkout.

[accept a payment](/payments/accept-a-payment?integration=checkout)

[Enable Link in Checkout](#accept-a-payment)

## Enable Link in Checkout

Accept payments with Link using information your customer stores in the Link app. When you receive a payment from a customer using Link in Checkout, the payment_method.type listed for the payment is link. To add Link to your Checkout integration, create a Checkout Session with link as a payment method type.

[Link app](https://link.com/)

[Checkout integration](/payments/accept-a-payment?integration=checkout)

Use dynamic payment methods to increase conversion by showing the most relevant payment methods to your customers. If you collect card details for future usage with Setup Intents, list payment methods manually instead of using dynamic payment methods.

[dynamic payment methods](/connect/dynamic-payment-methods)

[future usage with Setup Intents](/payments/save-and-reuse)

To enable dynamic payment methods for your Checkout integration:

- Remove the payment_method_types parameter from your integration.

[payment_method_types](/api/payment_intents/object#payment_intent_object-payment_method_types)

- Add Link by enabling the Link payment method from your payment method settings.

[payment method settings](https://dashboard.stripe.com/settings/payment_methods)

Link enabled as a payment method in the Stripe Dashboard

After you remove the payment_method_types parameter from your integration, some payment methods turn on automatically, including cards and wallets. The currency parameter restricts the payment methods that the customer sees during the checkout session.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

[Test the integration](#web-test-the-integration)

## Test the integration

Don’t store real user data in test mode Link accounts. Treat them as if they’re publicly available, because these test accounts are associated with your publishable key.

[test mode](/test-mode)

Currently, Link only works with credit cards, debit cards, and qualified US bank account purchases. Link requires domain registration.

[domain registration](/payments/payment-methods/pmd-registration)

You can create test mode accounts for Link using any valid email address. The following table shows the fixed one-time passcode values that Stripe accepts for authenticating test mode accounts:

As Stripe adds additional funding source support, you don’t need to update your integration. Stripe automatically supports them with the same transaction settlement time and guarantees as card and bank account payments.

## Link for Connect platforms

Link is automatically available to any connected account that uses Checkout through a Connect platform integration.

- If you’re a Connect platform, you can manage Link for your platform account through Link settings in your Dashboard. Your connected accounts manage Link from within their own Dashboard settings.

[Link settings](https://dashboard.stripe.com/settings/link)

- If you’re a connected account processing payments through a Connect platform, you can manage Link for both payments processed through a platform and payments processed without a platform in your Link settings in the Dashboard.

## See also

- Stripe Checkout

[Stripe Checkout](/payments/checkout)

- How Checkout works

[How Checkout works](/payments/checkout/how-checkout-works)

- Quickstart

[Quickstart](/checkout/quickstart)
