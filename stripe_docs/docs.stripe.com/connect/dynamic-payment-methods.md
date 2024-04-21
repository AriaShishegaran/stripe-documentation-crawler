# Upgrading to dynamic payment methods

This guide provides instructions on how to integrate dynamic payment methods for existing platforms. If you need help setting up a new platform, refer to either the Collect payments then pay out guide or the Enable other businesses to accept payments directly guide.

[Collect payments then pay out](/connect/collect-then-transfer-guide)

[Enable other businesses to accept payments directly](/connect/enable-payment-acceptance-guide)

## Integration instructions for dynamic payment methods

Use the following form to select your integration. If you need help determining your platform setup, including checkout solution, connected account types, and charge types, refer to Create a charge.

[Create a charge](/connect/charges)

[Enable payment methods for connected accountsRecommended](#enable-payment-methods-connected-accounts)

## Enable payment methods for connected accountsRecommended

If necessary, consult the following resources for payment method information:

- A guide to payment methods for help in choosing the right payment methods for your platform.

[A guide to payment methods](https://stripe.com/payments/payment-methods-guide#choosing-the-right-payment-methods-for-your-business)

- Country availability for payment methods for a list of payment methods and the countries they’re available in.

[Country availability for payment methods](/connect/payment-method-available-countries)

- Payment method and product support table to make sure your chosen payment methods work for your Stripe products and payments flows.

[Payment method and product support](/payments/payment-methods/integration-options#payment-method-product-support)

Visit the Manage payment methods for your connected accounts page in your Dashboard to configure which payment methods your connected accounts accept. Changes to default settings apply to all new and existing connected accounts.

[Manage payment methods for your connected accounts](https://dashboard.stripe.com/settings/payment_methods/connected_accounts)

For each payment method, you can select one of the following dropdown options:

Payment method options

If you make a change to a payment method, you must click Review changes in the bottom bar of your screen and Save and apply to update your connected accounts.

Save dialog

[Allow your connected accounts to manage their payment methodsRecommended](#allow-connected-accounts-manage)

## Allow your connected accounts to manage their payment methodsRecommended

Stripe recommends that you allow the owners of your platform’s connected accounts to customize their own payment methods from the Dashboard. If you enable this option, then each connected account with Stripe Dashboard access can log in to their Dashboard and view their Payment methods page. The Dashboard displays the set of payment method defaults you applied to all new and existing connected accounts. The owners of your platform’s connected accounts can override these defaults, excluding payment methods you have blocked.

[Payment methods](https://dashboard.stripe.com/settings/payment_methods)

Check the Account customization checkbox to enable this option. You must click Review changes in the bottom bar of your screen and then select Save and apply to update this setting.

Account customization checkbox

[Integrate Checkout using dynamic payment methodsRequired](#integrate)

## Integrate Checkout using dynamic payment methodsRequired

Previously, you might have used the payment_method_types parameter when defining your Checkout session to accept different payment methods. To begin managing your payment methods in the Dashboard, remove this parameter from your integration.

After you remove the payment_method_types parameter from your integration, some payment methods turn on automatically, including cards and wallets. The currency parameter restricts the payment methods that are shown to the customer during the checkout session.

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

[Enable shipping address collection in CheckoutRecommended](#collect-shipping-address)

## Enable shipping address collection in CheckoutRecommended

If you collect shipping addresses, you need to define which countries you can ship to when you create the Checkout session.  Specify the two-letter ISO country codes in the shipping_address_collection.allowed_countries parameter.

[shipping addresses](/payments/collect-addresses?payment-ui=checkout)

[parameter](/api/checkout/sessions/create#create_checkout_session-shipping_address_collection-allowed_countries)

You can optionally add shipping rates with the shipping_options parameter.

[parameter](/api/checkout/sessions/create#create_checkout_session-shipping_options)

If you use Afterpay or Clearpay, you must collect shipping addresses, but you don’t need to specify shipping rates for those payment methods.

Shipping address collection is required to use Afterpay or Clearpay as a payment method in Checkout, but shipping rates aren’t.

[Handle delayed notification payment methods, if applicableRecommended](#delayed)

## Handle delayed notification payment methods, if applicableRecommended

Follow the steps in our Manage payment methods in the Dashboard guide on how to handle delayed notification payment methods.

[Manage payment methods in the Dashboard](/payments/dashboard-payment-methods#delayed-notifications)

[handle delayed notification payment methods](/payments/dashboard-payment-methods#delayed-notifications)

[Test your integrationRecommended](#test)

## Test your integrationRecommended

Test your integration to ensure it performs as you expect. Log in to one of your test accounts and navigate to Payment methods settings to view your settings for your connected accounts. Test your checkout flow with your test API key and a test account. If a payment method you expect to be available is not available, check the payment method product support table to make sure your products and merchants are in a compatible currency and country.

[Test your integration](/payments/dashboard-payment-methods#testing)

[payment method product support table](/connect/account-capabilities#payment-methods)

[Have your connected accounts with Stripe Dashboard access enable any payment methods that require setup stepsOptional](#auto-payment)

## Have your connected accounts with Stripe Dashboard access enable any payment methods that require setup stepsOptional

Your connected accounts with Stripe Dashboard access are able to use most payment methods by default; however, some payment methods (such as Alipay and WeChat Pay) require your users to manually activate the payment method in their Dashboard. Confirm which payment methods require manual activation using the payment method capabilities table. If the Available by default column reads no, the payment method requires manual activation.

[payment method capabilities](/connect/account-capabilities#payment-methods)

If you allow the owners of your platform’s connected accounts to manage payment methods, then instruct them to enable these payment methods from their Dashboard.

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

Payment method customization

If you don’t allow the owners of your platform’s connected accounts to customize payment methods, then instruct them to visit their manual settings page.

[manual settings page](https://dashboard.stripe.com/settings/payment_methods)

Manual settings for payment methods

The embedded payment method settings component allows connected accounts to configure the payment methods they offer at checkout without the need to access the Stripe Dashboard. Request access and learn how to integrate with Payment Method Configurations.

[Request access](/connect/supported-embedded-components/payment-method-settings#request-access)

[integrate with Payment Method Configurations](/connect/supported-embedded-components/payment-method-settings#integration)

## See also

- Connect integration guide

[Connect integration guide](/connect/charges)
