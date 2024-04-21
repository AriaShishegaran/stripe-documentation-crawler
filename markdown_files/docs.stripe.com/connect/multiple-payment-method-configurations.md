htmlMultiple configurations for your Connect accounts | Stripe Documentation[Skip to content](#main-content)Multiple payment method configurations[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fmultiple-payment-method-configurations)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fmultiple-payment-method-configurations)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Multiple configurations for your Connect accounts

Learn how to allow your connected accounts to display different sets of payment methods to their buyers in different scenarios.Use this feature if your platform is using dynamic payment methods and supports setting different types of payment methods for different types of transactions (for example, subscriptions versus one-time checkout) or for different invoice amounts (for example, invoices more than a certain dollar amount can be paid using BNPL).

[Create a new payment method configuration in your Dashboard](#section-1)Navigate to the Payment methods settings for your connected accounts in the Stripe Dashboard. This is where you control your platform level “parent” configurations. Your connected accounts receive a “child” configuration for each parent that they can customize within the constraints you set below.

You start with one parent configuration by default. To create an additional configuration, click Add new configuration, and give it a name.

![Payment method configuration page](https://b.stripecdn.com/docs-statics-srv/assets/ppc-dashboard-demo-connect.93d78670fd3582900915ab57e3e219ec.png)

[Set the platform level default state](#section-2)You can apply the default setting for each payment method to your new parent configuration, and control what customizations your connected accounts can make. Use the dropdown to select the desired setting:

- On by defaultthe payment method is on by default. Connected accounts can turn it on and off.
- Off by defaultthe payment method is off by default. Connected accounts can turn it on and off.
- Blockedturns the payment method off for all connected accounts. Connected accounts can’t turn it on.

![Configure settings for each payment method](https://b.stripecdn.com/docs-statics-srv/assets/settings-api-wallets.956b27fd0756e064d433aaa5999130fe.png)

[Allow your connected accounts to customize](#section-3)Standard Connected accounts can visit the Dashboard to turn payment methods on or off if the payment method has been set to either On by default or Off by default. Your connected accounts see the newly created child configuration in their Payment methods settings. Your connected accounts can use the dropdown menu at the top of the page to choose a configuration to edit.

If you want your connected accounts to customize their Payment methods settings from your platform dashboard instead of the Stripe Dashboard, or if you have connected accounts who don’t have  Stripe Dashboard access, you can integrate with the Payment Method Configurations API.

Use the Payment Method Configurations API with the connected account ID and child configuration ID to read the current state of a payment method for a specific connected account on that configuration.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_method_configurations/{{PAYMENT_METHOD_CONFIGURATION_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"``{
  "object": "list",
  "data": [
    {
      "id": "{{PAYMENT_METHOD_CONFIGURATION_ID}}",
      "object": "payment_method_configuration",
      "name": "My Custom Configuration",
      "active": true,
      "is_default": true,
      "livemode": false,
      "parent": "{{PAYMENT_METHOD_CONFIGURATION_ID}}",
      "acss_debit": {
        "available": false,
        "display_preference": {
          "overridable": true,
          "preference": "off",
          "value": "off"
        }
      },
      "affirm": {
        "available": false,
        "display_preference": {
          "overridable": true,
          "preference": "off",
          "value": "off"
        }
      },
      "afterpay_clearpay": {
        "available": false,
        "display_preference": {
          "overridable": true,
          "preference": "off",
          "value": "off"
        }
      },
      ... additional payment methods
    }
  ],
  "has_more": false,
  "url": "/v1/payment_method_configurations"
}`If successful, the return list displays each payment method and includes two parameters outlining availability and display preference.

- available is the combination of capability value (active, inactive, pending, or unrequested) and display_preference value.

You can use the available field to know whether or not a buyer sees this payment method at checkout time. If available is true, that payment method’s capability is active and display_preference is on. If available is false, the payment method either doesn’t have an active capability or the display_preference value is off, and buyers won’t see it at checkout time. To simplify your integration and take advantage of other features, use payment methods that you manage from the Dashboard at checkout, which automatically reads this parameter and shows the right payment methods to buyers.


- display_preference has three components: overridable, preference, and value.

  - `overridable`is read-only, and indicates whether the connected account’s preference can override the default set above.
  - `preference`is writable, and stores the connected account’s preference.
  - `value`is read-only, and reflects the effective`display_preference`value.



NoteOnly payment methods that are relevant in the connected account’s country are shown in the API response and are configurable. Check country support.

When a connected account owner takes action to turn on or off a payment method, you can update the display_preference preference attribute. This stores the connected account owner’s preference for that payment method and is used to determine whether buyers see the payment method.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_method_configurations/{{PAYMENT_METHOD_CONFIGURATION_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "affirm[display_preference][preference]"=on``{
  "id": "{{PAYMENT_METHOD_CONFIGURATION_ID}}",
  "object": "payment_method_configuration",
  "name": "My Custom Configuration",
  "active": true,
  "is_default": true,
  "livemode": false,
  "acss_debit": {
    "available": false,
    "display_preference": {
      "overridable": true,
      "preference": "off",
      "value": "off"
    }
  },
  "affirm": {
    "available": true,
    "display_preference": {
      "overridable": true,
      "preference": "on",
      "value": "on"
    }
  },
  "afterpay_clearpay": {
    "available": false,
    "display_preference": {
      "overridable": true,
      "preference": "off",
      "value": "off"
    }
  },
  ... additional payment methods
}`When your connected accounts turn on payment methods with the API, Stripe intelligently ranks the payment methods based on the buyer’s location, order size, and other factors to always show the highest converting payment methods first.

[Display available payment methods on checkout](#section-4)Pass the parent configuration ID when rendering your checkout flow to use your new configuration. Stripe automatically looks up the child configuration for the associated connected account and uses their customized settings.

If you’re using the Payment Element and creating a PaymentIntent before rendering the Payment Element, you can pass the parent ID into your PaymentIntent.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d amount=1099 \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]"=true \
  -d payment_method_configuration={{PAYMENT_METHOD_CONFIGURATION_ID}}`If you’re using the Payment Element with the deferred intent creation integration path, you can pass the parent ID in to your elements session options.

`const options = {
   mode: 'payment',
   amount: 1099,
   currency: 'usd',
   payment_method_configuration: '{{PAYMENT_METHOD_CONFIGURATION_ID}}'
}`If you’re creating a Checkout session, you can pass the parent ID in to your checkout session options.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d mode=payment \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=1 \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel" \
  -d currency=usd \
  -d payment_method_configuration={{PAYMENT_METHOD_CONFIGURATION_ID}}`[(Optional)—Apple Pay, Google Pay, and Link](#section-5)Some payment methods, such as Apple Pay, Google Pay and Link, aren’t included as separate payment method types on a PaymentIntent and are confirmed only when supplying card. With the Payment Method Configurations API, you can let connected account owners opt in or opt out of these specific payment methods and prevent them from showing up in the UI.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a new payment method configuration in your Dashboard](#section-1)[Set the platform level default state](#section-2)[Allow your connected accounts to customize](#section-3)[Display available payment methods on checkout](#section-4)[(Optional)—Apple Pay, Google Pay, and Link](#section-5)Products Used[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`