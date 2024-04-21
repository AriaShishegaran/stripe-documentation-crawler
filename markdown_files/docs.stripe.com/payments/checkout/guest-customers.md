htmlGuest customers | Stripe Documentation[Skip to content](#main-content)Guest customers[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fguest-customers)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fguest-customers)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Guest customers

Learn how to track the activity of guest customers.The Customer object represents a customer of your business, and it helps tracking subscriptions and payments that belong to the same customer. Checkout Sessions that don’t create Customers are associated with guest customers instead. Stripe automatically groups guest customers in the Dashboard based on them having used the same card, email, or phone to make payments. This unified view helps you review purchasing behavior, refunds, chargebacks, or fraud.

Checkout supports passing in a customer to enable you to prefill customer information on the Checkout page and to associate the payment or subscription with a specific customer.

If you don’t pass in a customer, you can set customer_creation to configure whether or not Checkout automatically creates a Customer object when the session is confirmed.

## Managing and monitoring guest customers

Even though you can’t manage or monitor guest customers in the same way as with Checkout Sessions that create Customers, you can still manage them and monitor their activity.

### Grouping payments under guest customers

We use credit card number as the unique identifier to group credit card payments of your guest customers under the same guest identity. See the guest customer support page for additional details on the matching logic. If the same credit card was used by different guest customers (for example, two spouses using the same credit card to checkout at different times), all guest payments for that credit card show up together under one guest customer. Because we group by credit card, we consider it the same guest customer.

### Updating your privacy policy or other privacy notices

You’re in the best position to know whether this feature is consistent with your privacy policy or other privacy notices. It’s a good practice to review your privacy notices and privacy policy when considering any new feature. Guest customers give you a view of your existing guest data, which can help you better detect fraud and help you manage customer service inquiries.

### Exporting guest customer data from the Dashboard

You can export guest customer data from the Customers tab in the Dashboard. Guest customer information isn’t included in exports from the Payments tab.

### Not seeing any guest customers in the Guests tab

If you don’t see any guest customers under the Guests tab, this is because your Stripe integration is passing a Customer ID when creating Checkout Sessions. We only create guest customers for payments without a specific Customer object associated with them.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`