htmlCollect on-receipt tips | Stripe Documentation[Skip to content](#main-content)Collect on-receipt tips[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fcollecting-tips%2Fon-receipt)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffeatures%2Fcollecting-tips%2Fon-receipt)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)[Collect tips](/docs/terminal/features/collecting-tips/overview)# Collect on-receipt tips

Learn how to allow customers to add tips to receipts.Available in:Some business types allow customers to add a tip to a transaction after authorizing the card. This is most common for businesses in the dining and hospitality space (for example, a restaurant or bar), where a customer can add a tip onto the receipt.

In the US, after you confirm a PaymentIntent, you can collect a tip by capturing more than the authorized amount. This is known as over-capture. After you capture the PaymentIntent, your customer sees the full captured amount reflected on their statement.

To collect a tip, you must create and confirm a PaymentIntent following the steps outlined in collecting in-person payments. You can verify that a given PaymentIntent is eligible for over-capture by accessing overcapture_supported.

Next, capture more than the authorized amount by providing an amount_to_capture that’s equal to the sum of the confirmed PaymentIntent and tip amount.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/capture \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount_to_capture=1800`Over-capturing updates the PaymentIntent amount to reflect the new total, inclusive of the tip. This doesn’t result in an additional authorization, so your customer won’t see any immediate updates on their credit card statement. To see the original amount authorized, use the amount_authorized field in the PaymentIntent’s underlying Charge object.

## Limits

You can over-capture up to 50% of the PaymentIntent’s authorized amount, or 50 USD, whichever is greater. For example, if your PaymentIntent’s authorized amount is 40 USD, you can capture up to 90 USD; if your PaymentIntent’s amount is 100 USD, you can capture up to 150 USD.

If you need to capture more than these limits allow, there are two options:

- If yourMCCis eligible, you can use[incremental authorization](/terminal/features/incremental-authorizations)to increase the PaymentIntent’s`amount`.
- You can create a new PaymentIntent to capture the tip amount using the[generated_card](/api/payment_intents/object#payment_intent_object-last_payment_error-payment_method-card-generated_from-payment_method_details-card_present-generated_card)payment method from the first PaymentIntent.

## Availability

On-receipt tipping is available for United States businesses with eligible merchant category codes (MCCs), for payments using Visa, Mastercard, Discover, and American Express card brands.

Businesses in the following categories are eligible to collect tips using over-capture:

- Taxicabs and limousines
- Eating places and restaurants
- Drinking places (alcoholic beverages)
- Fast food restaurants
- Beauty and barber shops
- Health and beauty spas

Merchant category codes (MCCs)If you’re not sure about the eligibility of your merchant category, you can contact support. If you’re a Connect user, set the merchant category codes for your connected accounts to match their businesses.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Limits](#limits)[Availability](#availability)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`