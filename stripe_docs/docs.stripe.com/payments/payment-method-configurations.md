# Payment method configurations

Payment method configurations allows dynamic payment method users to display different sets of payment methods to customers for specific checkout scenarios.

[dynamic payment method](/payments/payment-methods/dynamic-payment-methods)

You can create a configuration to:

- Display a unique set of payment methods for certain products

- Enable a set of payment methods for your one-time payment checkout flow and a different set of payment methods for your subscription checkout flow

- Connect Offer connected accounts access to additional payment methods for a different subscription fee

After you create a payment method configuration, you can toggle each payment method on or off for a given scenario directly in Dashboard—no code required. Then at checkout, select which configuration you want to use. Stripe ranks the payment methods that are enabled within that configuration to optimize for conversion.

## Before you begin

- You must use either the Stripe Payment Element or Checkout.

[Payment Element](/payments/payment-element)

[Checkout](/payments/checkout)

- You must use Dynamic payment methods to enable additional payment methods from the Stripe Dashboard, which won’t require any code changes.To set up dynamic payment methods for direct users, see the payment method integration guide.Connect To set up dynamic payment methods for Connect platforms, see Upgrading to dynamic payment methods.

[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods)

- To set up dynamic payment methods for direct users, see the payment method integration guide.

[payment method integration](/payments/payment-methods/dynamic-payment-methods)

- Connect To set up dynamic payment methods for Connect platforms, see Upgrading to dynamic payment methods.

[Upgrading to dynamic payment methods](/connect/dynamic-payment-methods)

[Create a payment method configuration](#create-payment-method-configuration)

## Create a payment method configuration

By default, you have one payment method configuration called Default Config. You can create additional payment method configurations using both the Stripe Dashboard and the API.

- In your Dashboard, go to Payment methods settings.

[Payment methods settings](https://dashboard.stripe.com/test/settings/payment_methods)

- In the Configuration Management section, click the overflow menu (), then select Create a configuration.

- Give your new configuration a name.

- Click Save configuration.

The page displays your new configuration. It has a default set of enabled payment methods.

To switch between configurations, use the Select configuration dropdown near the top of the page.

[Enable payment methods](#enable-payment-methods)

## Enable payment methods

In the Dashboard, open the configuration and turn on the payment methods that you want to make available to buyers when using that configuration. A buyer sees only payment methods that are turned on and compatible with the payment location and currency.

Some payment methods don’t show edit controls until you expand them.

[Display available payment methods in checkout](#section-4)

## Display available payment methods in checkout

Copy the configuration ID in the Dashboard from the configuration you want to use in your checkout flow.

If you’re using the deferred intent creation integration path, pass the payment_method_configuration ID when you create your Payment Element component. The Payment Element automatically pulls the payment methods associated with that configuration and ranks them to best convert buyers.

[deferred intent creation integration path](/payments/accept-a-payment-deferred)

If you aren’t using a Payment Element, pass the payment_method_configuration ID when you create a Checkout session.

[create a Checkout session](/api/checkout/sessions/create)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

To see how your payment methods appear to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

[Dashboard](https://dashboard.stripe.com/settings/payment_methods/review)

[Create a PaymentIntent with the configuration](#create-payment-intent)

## Create a PaymentIntent with the configuration

Create a PaymentIntent on your server using the payment method configuration.

In the latest version of the API, the automatic_payment_methods parameter is optional because it’s enabled by default.
