htmlVirtual bank account numbers | Stripe Documentation[Skip to content](#main-content)Virtual bank account numbers[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcustomer-balance%2Fvirtual-bank-account-numbers)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcustomer-balance%2Fvirtual-bank-account-numbers)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank transfers](/docs/payments/bank-transfers)[Customer balance](/docs/payments/customer-balance)# Virtual bank account numbers

Learn best practices for using Virtual Bank Account Numbers (VBANs) for reconciliation on Stripe.Virtual Bank Account Numbers (VBANs) are an important part of the bank transfers payment method. To accept funds from a bank transfer, Stripe issues a VBAN to your customer. When the customer transfers money to that VBAN, Stripe automatically allocates the funds to the customer’s cash balance. After these funds arrive on the customer’s cash balance, Stripe carries out further reconciliation steps to associate the funds with the correct PaymentIntent or Invoice.

After a customer has been allocated a VBAN, it belongs to them forever. Any additional funds that are sent to that VBAN are automatically added to customer’s cash balance. Because VBANs are permanent, it’s important to understand their limits and best practices for using them.

## Allocation

There are several ways to allocate a VBAN to a customer.

- When you create and confirm a PaymentIntent with the customer balance payment method, Stripe looks for an existing VBAN that is assigned to the customer and for the country specified in the request. If the customer does not have an appropriate VBAN, Stripe generates a new VBAN for the customer.


- When you create a new Invoice with the customer balance payment method, Stripe looks for an existing VBAN that matches the country and is assigned to the customer specified in the request. If the customer does not have an appropriate VBAN, Stripe generates a new VBAN for the customer.


- The Funding Instructions API creates VBANs without requiring an existing PaymentIntent or Invoice. You can use this API when you don’t expect payment from a customer yet but still want to create a new VBAN for them.



## Limits and Best Practices

When you integrate with bank transfers, only request a VBAN for a customer if they’re likely to make a payment using a bank transfer. In these cases, you only generate a VBAN when creating a PaymentIntent or a Invoice.

Don’t assign VBANs to inactive customers or make VBAN allocation part of your registration flow.

Due to regional differences in VBAN availability, Stripe enforces different limits per region. If you need more VBANs than the limits allow, please reach out to our support team.

RegionLimitsUSWe allow up to5,000new VBANs every 24 hours.UKWe allow up to2,000new VBANs every 24 hours.EUWe allow up to5,000new VBANs every 24 hours and enforce a lifetime limit of50,000VBANs per account. Stripe also charges[a fee](https://stripe.com/pricing/local-payment-methods)for every new VBAN allocation over 1,000 allocations made in the EU.JPWe allow up to1,000new VBANs every 24 hours.MXWe allow up to1,000new VBANs every 24 hours.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Allocation](#allocation)[Limits and Best Practices](#limits-and-best-practices)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`