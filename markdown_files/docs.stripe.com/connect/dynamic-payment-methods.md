htmlUpgrading to dynamic payment methods | Stripe Documentation[Skip to content](#main-content)Dynamic payment methods[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fdynamic-payment-methods)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fdynamic-payment-methods)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Upgrading to dynamic payment methods

Increase conversion with dynamic payment methods for existing platforms.This guide provides instructions on how to integrate dynamic payment methods for existing platforms. If you need help setting up a new platform, refer to either the Collect payments then pay out guide or the Enable other businesses to accept payments directly guide.

## Integration instructions for dynamic payment methods

Use the following form to select your integration. If you need help determining your platform setup, including checkout solution, connected account types, and charge types, refer to Create a charge.

Confirm your integrationPayments integration:Stripe CheckoutCheckout is a Stripe-hosted payment form.Payment ElementPayment Element (for web and mobile) is a UI component that you embed into your website or app.Charge type:Direct chargesDestination chargesSeparate charges and transfersDashboard access:StripeExpressNone[Enable payment methods for connected accountsRecommended](#enable-payment-methods-connected-accounts)If necessary, consult the following resources for payment method information:

- [A guide to payment methods](https://stripe.com/payments/payment-methods-guide#choosing-the-right-payment-methods-for-your-business)for help in choosing the right payment methods for your platform.
- [Country availability for payment methods](/connect/payment-method-available-countries)for a list of payment methods and the countries they’re available in.
- [Payment method and product support](/payments/payment-methods/integration-options#payment-method-product-support)table to make sure your chosen payment methods work for your Stripe products and payments flows.

Visit the Manage payment methods for your connected accounts page in your Dashboard to configure which payment methods your connected accounts accept. Changes to default settings apply to all new and existing connected accounts.

For each payment method, you can select one of the following dropdown options:

On by defaultYour connected accounts accept this payment method during checkout. Some payment methods can only be off or blocked, this is because the owners of your platform’s connected accounts must activate them in their Dashboard settings page.Off by defaultYour connected accounts don’t accept this payment method during checkout.If you allow the owners of your platform’s connected accounts to manage their own payment methods in their Dashboard, however, they have the ability to turn it on.BlockedYour connected accounts don’t accept this payment method during checkout.If you allow the owners of your platform’s connected accounts to manage their own payment methods in their Dashboard, they don’t have the option to turn it on.![Dropdown options for payment methods, each showing an available option (blocked, on by default, off by default)](https://b.stripecdn.com/docs-statics-srv/assets/dropdowns.ef651d721d5939d81521dd34dde4577f.png)

Payment method options

If you make a change to a payment method, you must click Review changes in the bottom bar of your screen and Save and apply to update your connected accounts.

![Dialog that shows after clicking Save button with a list of what the user changed](https://b.stripecdn.com/docs-statics-srv/assets/dialog.a56ea7716f60db9778706790320d13be.png)

Save dialog

[Allow your connected accounts to manage their payment methodsRecommended](#allow-connected-accounts-manage)Stripe recommends that you allow the owners of your platform’s connected accounts to customize their own payment methods from the Dashboard. If you enable this option, then each connected account with Stripe Dashboard access can log in to their Dashboard and view their Payment methods page. The Dashboard displays the set of payment method defaults you applied to all new and existing connected accounts. The owners of your platform’s connected accounts can override these defaults, excluding payment methods you have blocked.

Check the Account customization checkbox to enable this option. You must click Review changes in the bottom bar of your screen and then select Save and apply to update this setting.

![Screenshot of the checkbox to select when allowing connected owners to customize payment methods](https://b.stripecdn.com/docs-statics-srv/assets/checkbox.275bd35d2a025272f03af029a144e577.png)

Account customization checkbox

[Integrate Checkout using dynamic payment methodsRequired](#integrate)Previously, you might have used the payment_method_types parameter when defining your Checkout session to accept different payment methods. To begin managing your payment methods in the Dashboard, remove this parameter from your integration.

After you remove the payment_method_types parameter from your integration, some payment methods turn on automatically, including cards and wallets. The currency parameter restricts the payment methods that are shown to the customer during the checkout session.

[Ruby](#)`Stripe::Checkout::Session.create({
mode: 'payment',
# Remove the payment_method_types parameter
# to manage payment methods in the Dashboard
payment_method_types: ['card'],
line_items: [{
  price_data: {
  # The currency parameter determines which
  # payment methods are used in the Checkout Session.
    currency: 'eur',
      product_data: {
        name: 'T-shirt',
      },
      unit_amount: 2000,
    },
    quantity: 1,
  }],
  success_url: 'https://example.com/success',
  cancel_url: 'https://example.com/cancel',
})`[Enable shipping address collection in CheckoutRecommended](#collect-shipping-address)If you collect shipping addresses, you need to define which countries you can ship to when you create the Checkout session.  Specify the two-letter ISO country codes in the shipping_address_collection.allowed_countries parameter.

You can optionally add shipping rates with the shipping_options parameter.

If you use Afterpay or Clearpay, you must collect shipping addresses, but you don’t need to specify shipping rates for those payment methods.

NoteShipping address collection is required to use Afterpay or Clearpay as a payment method in Checkout, but shipping rates aren’t.

[Handle delayed notification payment methods, if applicableRecommended](#delayed)Follow the steps in our Manage payment methods in the Dashboard guide on how to handle delayed notification payment methods.

[Test your integrationRecommended](#test)Test your integration to ensure it performs as you expect. Log in to one of your test accounts and navigate to Payment methods settings to view your settings for your connected accounts. Test your checkout flow with your test API key and a test account. If a payment method you expect to be available is not available, check the payment method product support table to make sure your products and merchants are in a compatible currency and country.

[Have your connected accounts with Stripe Dashboard access enable any payment methods that require setup stepsOptional](#auto-payment)Your connected accounts with Stripe Dashboard access are able to use most payment methods by default; however, some payment methods (such as Alipay and WeChat Pay) require your users to manually activate the payment method in their Dashboard. Confirm which payment methods require manual activation using the payment method capabilities table. If the Available by default column reads no, the payment method requires manual activation.

If you allow the owners of your platform’s connected accounts to manage payment methods, then instruct them to enable these payment methods from their Dashboard.

![Screenshot of connected account payment method customization through Dashboard showing available payment methods as on and available.](https://b.stripecdn.com/docs-statics-srv/assets/turn-on-payments.afef26196ebae8f5564d328d6ba73b92.png)

Payment method customization

If you don’t allow the owners of your platform’s connected accounts to customize payment methods, then instruct them to visit their manual settings page.

![Screenshot of manual settings page with payment methods listed with the option to request access, request invite, or configure.](https://b.stripecdn.com/docs-statics-srv/assets/manual-settings.db0a0c2abebb94e197e1bef683ea7db9.png)

Manual settings for payment methods

BetaThe embedded payment method settings component allows connected accounts to configure the payment methods they offer at checkout without the need to access the Stripe Dashboard. Request access and learn how to integrate with Payment Method Configurations.

## See also

- [Connect integration guide](/connect/charges)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Integration instructions for dynamic payment methods](#integration-instructions-for-dynamic-payment-methods)[Enable payment methods for connected accounts](#enable-payment-methods-connected-accounts)[Allow your connected accounts to manage their payment methods](#allow-connected-accounts-manage)[Integrate Checkout using dynamic payment methods](#integrate)[Enable shipping address collection in Checkout](#collect-shipping-address)[Handle delayed notification payment methods, if applicable](#delayed)[Test your integration](#test)[Have your connected accounts with Stripe Dashboard access enable any payment methods that require setup steps](#auto-payment)[See also](#see-also)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`