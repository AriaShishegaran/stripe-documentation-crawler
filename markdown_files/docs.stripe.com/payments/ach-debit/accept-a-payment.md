htmlAccept an ACH Direct Debit payment | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fach-debit%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fach-debit%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank debits](/docs/payments/bank-debits)[ACH Direct Debit](/docs/payments/ach-debit)# Accept an ACH Direct Debit payment

Build a custom payment form or use Stripe Checkout to accept payments with ACH Direct Debit.WebMobilePrebuilt checkout pageDirect APICautionStripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

Stripe users in the US can use Checkout in payment mode to accept ACH Direct Debit payments.

A Checkout Session represents the details of your customer’s intent to purchase. You create a Session when your customer wants to pay for something. After redirecting your customer to a Checkout Session, Stripe presents a payment form where your customer can complete their purchase. After your customer has completed a purchase, they are redirected back to your site.

With Checkout, you can create a Checkout Session with us_bank_account as a payment method type to track and handle the states of the payment until the payment completes.

NoteACH Direct Debit is a delayed notification payment method, which means that funds aren’t immediately available after payment. A payment typically takes 4 business days to arrive in your account.

[Determine compatibility](#compatibility)Supported business locations: US

Supported currencies: usd

Presentment currencies: usd

Payment mode: Yes

Setup mode: Yes

Subscription mode: Yes

A Checkout Session must satisfy all of the following conditions to support ACH Direct Debit payments:

- Express all[Prices](/api/prices)for all line items in US dollars (currency code`usd`).

[Create or retrieve a customerRecommendedServer-side](#create-customer)Create a Customer object when your user creates an account with your business, or retrieve an existing Customer associated with this user. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the stored payment method details later. Include an email address on the Customer to enable Financial Connections’ return user optimization.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d email={{CUSTOMER_EMAIL}}`[Accept a payment](#accept-a-payment)NoteBuild an integration to accept a payment with Checkout before using this guide.

This guides you through enabling ACH Direct Debit and shows the differences between accepting a card payment and using this payment method.

### Enable ACH Direct Debit as a payment method

When creating a new Checkout Session, you need to:

1. Add`us_bank_account`to the list of`payment_method_types`.
2. Make sure all your`line_items`use the`usd`currency.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d mode=payment \
  -d customer={{CUSTOMER_ID}} \
  -d "payment_method_types[0]"=card \
  -d "payment_method_types[1]"=us_bank_account \
  -d "line_items[0][price_data][currency]"=usd \
  -d "line_items[0][price_data][unit_amount]"=2000 \
  -d "line_items[0][price_data][product_data][name]"=T-shirt \
  -d "line_items[0][quantity]"=1 \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel"`For more information on Financial Connections fees, see pricing details.

By default, collecting bank account payment information uses Financial Connections to instantly verify your customer’s account, with a fallback option of manual account number entry and microdeposit verification. See the Financial Connections docs to learn how to configure Financial Connections and access additional account data to optimize your ACH integration. For example, you can use Financial Connections to check an account’s balance before initiating the ACH payment.

NoteTo expand access to additional data after a customer authenticates their account, they must re-link their account with expanded permissions.

If the customer opts for microdeposit verification instead of Financial Connections, Stripe automatically sends two small deposits to the provided bank account. These deposits can take 1-2 business days to appear on the customer’s online bank statement. When the deposits are expected to arrive, the customer receives an email with a link to confirm these amounts and verify the bank account with Stripe. After verification is complete, the payment begins processing.

We recommend including the payment_intent_data.setup_future_usage parameter with a value of off_session when creating a payment mode Session for ACH Direct Debit so you can save payment method details.

### Fulfill your orders

After accepting a payment, learn how to fulfill orders.

Because ACH Direct Debit is a delayed notification payment method, you must also complete the handle delayed notification payment methods step of the guide.

[Test your integration](#test-integration)Learn how to test scenarios with instant verifications using Financial Connections.

### Send transaction emails in test mode

After you collect the bank account details and accept a mandate, send the mandate confirmation and microdeposit verification emails in test mode. To do this, provide an email in the payment_method_data.billing_details[email] field in the form of {any-prefix}+test_email@{any_domain} when you collect the payment method details.

Common mistakeYou need to activate your Stripe account before you can trigger these emails in Test mode.

### Test account numbers

Stripe provides several test account numbers and corresponding tokens you can use to make sure your integration for manually-entered bank accounts is ready for production.

Account numberTokenRouting numberBehavior`000123456789``pm_usBankAccount_success``110000000`The payment succeeds.`000111111113``pm_usBankAccount_accountClosed``110000000`The payment fails because the account is closed.`000111111116``pm_usBankAccount_noAccount``110000000`The payment fails because no account is found.`000222222227``pm_usBankAccount_insufficientFunds``110000000`The payment fails due to insufficient funds.`000333333335``pm_usBankAccount_debitNotAuthorized``110000000`The payment fails because debits aren’t authorized.`000444444440``pm_usBankAccount_invalidCurrency``110000000`The payment fails due to invalid currency.`000666666661``pm_usBankAccount_failMicrodeposits``110000000`The payment fails to send microdeposits.`000555555559``pm_usBankAccount_dispute``110000000`The payment triggers a dispute.`000000000009``pm_usBankAccount_processing``110000000`The payment stays in processing indefinitely. Useful for testing[PaymentIntent cancellation](/api/payment_intents/cancel).Before test transactions can complete, you need to verify all test accounts that automatically succeed or fail the payment. To do so, use the test microdeposit amounts or descriptor codes below.

### Test microdeposit amounts and descriptor codes

To mimic different scenarios, use these microdeposit amounts or 0.01 descriptor code values.

Microdeposit values0.01 descriptor code valuesScenario`32`and`45`SM11AASimulates verifying the account.`10`and`11`SM33CCSimulates exceeding the number of allowed verification attempts.`40`and`41`SM44DDSimulates a microdeposit timeout.[Additional considerations](#additional-considerations)### Microdeposit verification failure

When a bank account is pending verification with microdeposits, the customer can fail to verify for three reasons:

- The microdeposits failed to send to the customer’s bank account (this usually indicates a closed or unavailable bank account or incorrect bank account number).
- The customer made 10 failed verification attempts for the account. Exceeding this limit means the bank account can no longer be verified or reused.
- The customer failed to verify the bank account within 10 days.

If the bank account fails verification for one of these reasons, you can handle the checkout.session.async_payment_failed event to contact the customer about placing a new order.

[OptionalInstant only verification](#instant-only-verification)[OptionalAccess data on a Financial Connections bank account](#access-data-on-a-financial-connections-bank-account)[OptionalResolve disputesServer-side](#resolving-disputes)[OptionalPayment Reference](#payment-reference)## See also

- [Save ACH Direct Debit pre-authorized debit details for future payments](/payments/ach-debit/set-up-payment)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Determine compatibility](#compatibility)[Create or retrieve a customer](#create-customer)[Accept a payment](#accept-a-payment)[Test your integration](#test-integration)[Additional considerations](#additional-considerations)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`