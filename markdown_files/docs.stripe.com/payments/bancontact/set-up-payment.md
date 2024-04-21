htmlUse Bancontact to set up future SEPA Direct Debit payments | Stripe Documentation[Skip to content](#main-content)Set up future payments[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbancontact%2Fset-up-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbancontact%2Fset-up-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank redirects](/docs/payments/bank-redirects)[Bancontact](/docs/payments/bancontact)# Use Bancontact to set up future SEPA Direct Debit payments

Learn how to save bank details from a Bancontact payment and charge your customers later with SEPA Direct Debit.CautionWe recommend that you follow the Set up future payments guide. If you’ve already integrated with Elements, see the Payment Element migration guide.

### Bancontact payments

See Save bank details during payment if you need to accept a payment and save IBAN details.

Bancontact is a single use payment method where customers are required to authenticate each payment. With this integration, Stripe charges your customer 0.02 EUR through Bancontact to collect their bank details. After your customer authenticates the payment, Stripe refunds the payment and stores your customer’s IBAN in a SEPA Direct Debit payment method. You can then use the SEPA Direct Debit PaymentMethod to accept payments or set up a subscription.

CautionTo use Bancontact to set up SEPA Direct Debit payments, you must activate SEPA Direct Debit in the Dashboard. You must also comply with the Bancontact Terms of Service and SEPA Direct Debit Terms of Service.

Prebuilt checkout pageWebiOSAndroidReact NativeYou can use Checkout in setup mode to collect payment details and set up future SEPA Direct Debit payments using Bancontact.

[Create or retrieve a CustomerServer-side](#create-retrieve-customer)To set up future SEPA Direct Debit payments using Bancontact, you must attach the SEPA Direct Debit payment method to a Customer.

Create a Customer object when your customer creates an account with your business. You can retrieve and use a customer’s stored payment method details later if you associate the ID of the Customer object with your own internal representation of the customer.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`[Set up future payments](#setup-a-payment)This guide builds on the foundational set up future payments Checkout integration and describes how to enable Bancontact—it shows the differences between setting up future payments for cards and using Bancontact.

### Enable Bancontact as a payment method

When creating a new Checkout Session, you need to add bancontact to the list of payment_method_types.

[Ruby](#)`Stripe::Checkout::Session.create({
  mode: 'setup',
  payment_method_types: ['card'],
  payment_method_types: ['card', 'bancontact'],
  customer: customer.id,
  success_url: 'https://example.com/success',
  cancel_url: 'https://example.com/cancel',
})`[Charge the SEPA Direct Debit PaymentMethod laterServer-side](#charge-sepa-pm)When you need to charge your customer again, create a new PaymentIntent. Find the ID of the SEPA Direct Debit payment method by retrieving the SetupIntent and expanding the latest_attempt field where you will find the generated_sepa_debit ID inside of payment_method_details.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/setup_intents/{{SETUP_INTENT_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "expand[]"=latest_attempt`Create a PaymentIntent with the SEPA Direct Debit and Customer IDs.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "payment_method_types[]"=sepa_debit \
  -d amount=1099 \
  -d currency=eur \
  -d customer={{CUSTOMER_ID}} \
  -d payment_method={{SEPA_DEBIT_PAYMENT_METHOD_ID}} \
  -d confirm=true`[Test your integration](#testing)When testing your Checkout integration, select Bancontact as the payment method and click the Pay button.

## See also

- [Accept a SEPA Direct Debit payment](/payments/sepa-debit/accept-a-payment)
- [Set up a subscription with SEPA Direct Debit in the EU](/billing/subscriptions/sepa-debit)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create or retrieve a Customer](#create-retrieve-customer)[Set up future payments](#setup-a-payment)[Charge the SEPA Direct Debit PaymentMethod later](#charge-sepa-pm)[Test your integration](#testing)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`