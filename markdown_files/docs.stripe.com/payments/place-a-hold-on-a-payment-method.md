htmlPlace a hold on a payment method | Stripe Documentation[Skip to content](#main-content)Place a hold on a payment method[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fplace-a-hold-on-a-payment-method)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fplace-a-hold-on-a-payment-method)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)
[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[More payment scenarios](/docs/payments/more-payment-scenarios)# Place a hold on a payment method

Separate payment authorization and capture to create a charge now, but capture funds later.When you create a payment, you can place a hold on an eligible payment method to reserve funds that you can capture later. For example, hotels often authorize a payment in full before a guest arrives, then capture the money when the guest checks out.

Authorizing a payment guarantees the amount by holding it on the customer’s payment method. If you’re using the API, the payment_method_details.card.capture_before attribute on the charge indicates when the authorization expires.

You need to capture the funds before the authorization expires. If the authorization expires before you capture the funds, the funds are released and the payment status changes to canceled. By default, the authorization expires in 7 days. Learn more about statuses for asynchronous payments.

### Example code

Check out the sample app on GitHub.

Before implementing, understand the following limitations for authorizing and capturing separately.

### Limitations

[Use the Dashboard to authorize and capture](#use-dashboard)You can authorize a payment and capture funds separately without writing code.

1. In the Dashboard,[create a new payment](https://dashboard.stripe.com/test/payments/new). SelectOne-time.
2. When you enter or select the payment method, selectMore optionsthenCapture funds later.

The payment appears in your payments page as Uncaptured.

To capture the funds, go to the payment details page and click Capture.

[Tell Stripe to authorize only](#authorize-only)To indicate that you want separate authorization and capture, specify capture_method as manual when creating the PaymentIntent. This parameter instructs Stripe to authorize the amount but not capture it on the customer’s payment method.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d currency=usd \
  -d "payment_method_types[]"=card \
  -d capture_method=manual`With the above approach, you tell Stripe that you can only use “capture after” for a PaymentIntent with eligible payment methods. For example, you can’t accept card payments and Giropay (which doesn’t support capture after) for a single PaymentIntent. To accept payment methods that might not all support capture after, you can configure capture-after-per-payment-method by configuring capture_method=manual on the payment_method_options[<payment_method_type>] object. For example, by configuring payment_method_options[card][capture_method]=manual, you’re placing only card payments on hold. You can manage payment methods from the Dashboard. Stripe handles the return of eligible payment methods based on factors such as the transaction’s amount, currency, and payment flow.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d currency=usd \
  -d "automatic_payment_methods[enabled]"=true \
  -d "payment_method_options[card][capture_method]"=manual`Alternatively, you can list card and giropay using payment method types like in the example below.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d currency=eur \
  -d "payment_method_types[]"=card \
  -d "payment_method_types[]"=giropay \
  -d "payment_method_options[card][capture_method]"=manual`Before continuing to capture, attach a payment method with card details to the PaymentIntent, and authorize the card by confirming the PaymentIntent. You can do this by setting the payment_method and confirm fields on the PaymentIntent.

Extended AuthorizationsBy default, an authorization for an online card payment is valid for 7 days. To increase the validity period, see how to place an extended hold on an online card payment.

[Capture the funds](#capture-funds)After the payment method is authorized, the PaymentIntent status transitions to requires_capture. To capture the authorized funds, make a PaymentIntent capture request. This captures the total authorized amount by default. To capture less or (for certain online card payments) more than the initial amount, pass the amount_to_capture option. A partial capture automatically releases the remaining amount. If attempting to capture more than the initial amount for an online card payment, refer to the overcapture documentation.

The following example demonstrates how to capture 7.50 USD of the authorized 10.99 USD payment:

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents/pi_ANipwO3zNfjeWODtRPIg/capture \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d amount_to_capture=750`While some card payments are eligible for multicapture, you can only perform one capture on an authorized payment for most payments. If you partially capture a payment, you can’t perform another capture for the difference. (Instead, consider saving the customer’s payment method details for later and creating future payments as needed.)

Card statements from some issuers and interfaces from payment methods don’t always distinguish between authorizations and captured (settled) payments, which can sometimes confuse customers.

Additionally, when a customer completes the payment process on a PaymentIntent with manual capture, it triggers the payment_intent.amount_capturable_updated event. You can inspect the PaymentIntent’s amount_capturable property to see the total amount that you can capture from the PaymentIntent.

[OptionalCancel the authorization](#cancel-authorization)## See also

- [Separate authorization and capture with Checkout](/payments/accept-a-payment?platform=web&ui=stripe-hosted#auth-and-capture)
- [Place an extended hold on an online card payment](/payments/extended-authorization)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Use the Dashboard to authorize and capture](#use-dashboard)[Tell Stripe to authorize only](#authorize-only)[Capture the funds](#capture-funds)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`