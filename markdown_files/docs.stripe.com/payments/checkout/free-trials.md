htmlConfigure a free trial without collecting payment details | Stripe Documentation[Skip to content](#main-content)Start a free trial without collecting payment details[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Ffree-trials)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Ffree-trials)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Configure a free trial without collecting payment details

Use Stripe Checkout to collect a customer's information for a free trial without collecting their payment details.Stripe Checkout lets you sign up customers for a free trial of a subscription service without collecting their payment details. At the end of the trial period you specify, use Stripe to configure a reminder email to collect a customer’s payment details.

[Configure Checkout session](#section-1)Create a Checkout Session with the following:

- A`subscription_data`parameter with:  - `trial_period_days`set to the length (in days) of your free trial. In this example, the trial period is 30 days.
  - `trial_settings[end_behavior][missing_payment_method]`set to`cancel`(or`pause`) if the trial ends without a payment method attached. View[Use trial periods](/billing/subscriptions/trials#create-free-trials-without-payment)to learn more.


- The`payment_method_collection`parameter set to`if_required`. This tells Stripe that collecting payment information at checkout is optional.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d mode=subscription \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel" \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=1 \
  -d "subscription_data[trial_settings][end_behavior][missing_payment_method]"=cancel \
  -d "subscription_data[trial_period_days]"=30 \
  -d payment_method_collection=if_required`![](https://b.stripecdn.com/docs-statics-srv/assets/skip-payment-method-collection.44ef515675b659555a1d80475114f89f.png)

[Collect payment details when the trial is about to expire](#collect-payment)Before the trial expires, collect payment details from your customer.

Under Manage free trial messaging in your Subscriptions and emails settings, you can choose to automatically send a reminder email when a customer’s trial is about to expire.

Next, select the Link to a Stripe-hosted page option so the reminder email contains a link for the customer to add or update their payment details. We don’t send free trial reminder emails in test mode. Learn more about how to set up free trial reminders.

You must comply with card network requirements when offering trials. Learn more about compliance requirements for trials and promotion.

[OptionalCollect payment details in the Billing customer portal](#customer-portal)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Configure Checkout session](#section-1)[Collect payment details when the trial is about to expire](#collect-payment)Products Used[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`