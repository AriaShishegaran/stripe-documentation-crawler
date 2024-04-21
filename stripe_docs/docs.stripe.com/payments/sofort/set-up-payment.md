# Use Sofort to set up future SEPA Direct Debit payments

Our financial partners are in the process of deprecating Sofort. New businesses can’t accept Sofort payments. For more information read our support page.

[support page](https://support.stripe.com/questions/sofort-is-being-deprecated-as-a-standalone-payment-method)

We recommend that you follow the Set up future payments guide. If you’ve already integrated with Elements, see the Payment Element migration guide.

[Set up future payments](/payments/save-and-reuse)

[Payment Element migration guide](/payments/payment-element/migration)

See Save bank details during payment if you need to accept a payment and save IBAN details.

[Save bank details during payment](/payments/sofort/save-during-payment)

Sofort is a single use payment method where customers are required to authenticate each payment. With this integration, Stripe charges your customer 1 EUR through Sofort in order to collect their bank details. After your customer authenticates the payment, Stripe refunds the payment and store your customer’s IBAN in a SEPA Direct Debit payment method. You can then use the SEPA Direct Debit PaymentMethod to accept payments or set up a subscription.

[single use](/payments/payment-methods#usage)

[authenticate](/payments/payment-methods#customer-actions)

[IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)

[SEPA Direct Debit](/payments/sepa-debit)

[PaymentMethod](/api/payment_methods)

[accept payments](/payments/sepa-debit/accept-a-payment)

[set up a subscription](/billing/subscriptions/sepa-debit)

To use Sofort to set up SEPA Direct Debit payments, you must SEPA Direct Debit in the Dashboard. You must also comply with our Sofort Terms of Service and SEPA Direct Debit Terms of Service.

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

[Sofort Terms of Service](https://stripe.com/sofort/legal)

[SEPA Direct Debit Terms of Service](https://stripe.com/sepa-direct-debit/legal)

You can use Checkout in setup mode to collect payment details and set up future SEPA Direct Debit payments using Sofort.

[Checkout in setup mode](/payments/save-and-reuse?platform=checkout)

[Create or retrieve a CustomerServer-side](#create-retrieve-customer)

## Create or retrieve a CustomerServer-side

To set up future SEPA Direct Debit payments using Sofort, you must attach the SEPA Direct Debit payment method to a Customer.

[Customer](/api/customers)

Create a Customer object when your customer creates an account with your business. You can retrieve and use a customer’s stored payment method details later, if you associate the ID of the Customer object with your own internal representation of the customer.

[Set up future payments](#setup-a-payment)

## Set up future payments

This guide builds on the foundational set up future payments Checkout integration and describes how to enable Sofort—it shows the differences between setting up future payments for cards and using Sofort.

[set up future payments](/payments/save-and-reuse?platform=checkout)

When creating a new Checkout Session, you need to add sofort to the list of payment_method_types.

[Checkout Session](/api/checkout/sessions)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

[Charge the SEPA Direct Debit PaymentMethod laterServer-side](#charge-sepa-pm)

## Charge the SEPA Direct Debit PaymentMethod laterServer-side

When you need to charge your customer again, create a new PaymentIntent. Find the ID of the SEPA Direct Debit payment method by retrieving the SetupIntent and expanding the latest_attempt field where you will find the generated_sepa_debit ID inside of payment_method_details.

[retrieving](/api/setup_intents/retrieve)

[expanding](/api/expanding_objects)

Create a PaymentIntent with the SEPA Direct Debit and Customer IDs.

[Test your integration](#testing)

## Test your integration

When testing your Checkout integration, select Sofort as the payment method and click the Pay button.

## See also

- Accept a SEPA Direct Debit payment

[Accept a SEPA Direct Debit payment](/payments/sepa-debit/accept-a-payment)

- Set up a subscription with SEPA Direct Debit in the EU

[Set up a subscription with SEPA Direct Debit in the EU](/billing/subscriptions/sepa-debit)
