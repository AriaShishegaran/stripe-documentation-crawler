htmlStripe Checkout | Stripe Documentation[Skip to content](#main-content)Overview[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)# Stripe Checkout

Build a low-code payment form and embed it on your site or host it on Stripe.Checkout is a low-code payment integration that creates a customizable form for collecting payments. You can embed Checkout directly in your website or redirect customers to a Stripe-hosted payment page. It supports one-time payments and subscriptions and accepts over 40 local payment methods. For a full list of Checkout features, see Built-in features and customizable features.

Explore Stripe Checkout

Don’t see your use case? Let us know how you’d like to use Checkout.

## Get started

[How Checkout worksLearn how to add a checkout page to your website and collect payments.](/payments/checkout/how-checkout-works)[Watch a video tutorialLearn how to implement Stripe Checkout features.](/videos/checkout-101?video=payment-link)[QuickstartExplore a code sample of an integration with Stripe Checkout.](/checkout/quickstart)[Enable global payment methodsTurn on different Checkout payment methods through the Dashboard.](/payments/dashboard-payment-methods)[Fulfill your ordersLearn how to fulfill orders after a customer completes their purchase.](/payments/checkout/fulfill-orders)## Customize Checkout

[Customize your integrationCustomize branding, language support, fonts, store policies, and so on.](/payments/checkout/customization)[Use custom domainsLearn how to bring your own custom domain to Stripe Checkout.](/payments/checkout/custom-domains)[Customize your success pageDisplay a custom confirmation page with your customer’s order information.](/payments/checkout/custom-success-page)[Collect taxesCollect taxes for one-time payments and Subscriptions.](/payments/checkout/taxes)[Collect tax IDsCollect VAT and other customer tax IDs in Checkout.](/tax/checkout/tax-ids)[Collect phone numbersCollect phone numbers in Checkout.](/payments/checkout/phone-numbers)[Post-payment invoicesSend invoices to customers with Stripe Checkout.](/receipts?payment-ui=checkout)[Set up future paymentsSave payment details and charge your customers later.](/payments/save-and-reuse)## Boost revenue

[Subscription upsellsEnable customers to upgrade their subscription plan at checkout by using upsells.](/payments/checkout/upsells)[Cross-sellsEnable customers to purchase complementary products at checkout by using cross-sells.](/payments/checkout/cross-sells)[Recover abandoned cartsRecover abandoned Checkout pages and boost revenue.](/payments/checkout/abandoned-carts)[Automatically convert currencies with Adaptive PricingAutomatically convert prices for selected international shoppers to increase conversion.](/payments/checkout/adaptive-pricing)[Define multi-currency pricesPresent prices in your customers’ local currencies during checkout.](/payments/checkout/multi-currency-prices)[Analyzing your conversion funnelLearn how to analyze the conversion funnel of your Stripe Checkout page.](/payments/checkout/analyze-conversion-funnel)## No-code options

[Pricing tableDisplay a pricing table on your website and take customers directly to Stripe Checkout.](/payments/checkout/pricing-table)[Payment linksEmbed or share a link to a Stripe payment page to accept payments without a website.](/payment-links)## Additional features

[Add discountsReduce the amount charged to a customer by discounting their subtotal with coupons and promotion codes.](/payments/checkout/discounts)[Charge shippingUse shipping rates and collect shipping addresses from your customers.](/payments/during-payment/charge-shipping?payment-ui=checkout)[Manage limited inventory with CheckoutLearn how to manage inventory with time-limited purchase windows.](/payments/checkout/managing-limited-inventory)## Try a sample project

[One-time paymentsWeb · Mobile web](https://github.com/stripe-samples/checkout-one-time-payments)[SubscriptionsWeb · Mobile web · Stripe Billing](https://github.com/stripe-samples/checkout-single-subscription)[Browse our samples](/samples)## Built-in and customizable features

Stripe Checkout has the following built-in and customizable features:

### Built-in features

- PayPal, Google Pay, Apple Pay, and Link
- Responsive mobile design
- SCA-ready
- CAPTCHAs
- PCI compliance
- Card validation
- Error messaging
- [Adjustable quantities](/payments/checkout/adjustable-quantity)
- [Automatic tax collection](/tax/checkout)
- International language support
- [Adaptive Pricing](/payments/checkout/adaptive-pricing)

### Customizable features

- [Collect taxes](/payments/checkout/taxes)
- [Custom branding with colors, buttons, and font](/payments/checkout/customization)
- [Cross-sells](/payments/checkout/cross-sells)
- [Global payment methods](/payments/dashboard-payment-methods)
- [Subscription upsells](/payments/checkout/upsells)
- [Custom domains](/payments/checkout/custom-domains)(Stripe-hosted page only)
- [Email receipts](/receipts)
- [Apply discounts](/payments/checkout/discounts)
- [Custom success page](/payments/checkout/custom-success-page)
- [Recover abandoned carts](/payments/checkout/abandoned-carts)
- [Autofill payment details with Link](/payments/checkout/customization#link)
- [Collect Tax IDs](/tax/checkout/tax-ids)
- [Collect shipping information](/payments/collect-addresses?payment-ui=checkout)
- [Collect phone numbers](/payments/checkout/phone-numbers)
- [Set the subscription billing cycle date](/payments/checkout/billing-cycle)

Sign up to be notified of new features and updates.Provide your email to receive updates on new features and support for more use cases.Get updatesRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`