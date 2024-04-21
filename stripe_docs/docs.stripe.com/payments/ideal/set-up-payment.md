# Use iDEAL to set up future SEPA Direct Debit payments

See Save bank details during payment if you need to accept a payment and save IBAN details.

[Save bank details during payment](/payments/ideal/save-during-payment)

We recommend that you follow the Set up future payments guide. If you’ve already integrated with Elements, see the Payment Element migration guide.

[Set up future payments](/payments/save-and-reuse)

[Payment Element migration guide](/payments/payment-element/migration)

iDEAL is a single use payment method where customers are required to authenticate each payment. With this integration, Stripe charges your customer 0.01 EUR through iDEAL to collect their bank details. After your customer authenticates the payment, Stripe refunds the payment and stores your customer’s IBAN in a SEPA Direct Debit payment method. You can then use the SEPA Direct Debit PaymentMethod to accept payments or set up a subscription.

[single use](/payments/payment-methods#usage)

[authenticate](/payments/payment-methods#customer-actions)

[IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)

[SEPA Direct Debit](/payments/sepa-debit)

[PaymentMethod](/api/payment_methods)

[accept payments](/payments/sepa-debit/accept-a-payment)

[set up a subscription](/billing/subscriptions/sepa-debit)

To use iDEAL to set up SEPA Direct Debit payments, you must activate SEPA Direct Debit in the Dashboard. You must also comply with the iDEAL Terms of Service and SEPA Direct Debit Terms of Service.

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

[iDEAL Terms of Service](https://stripe.com/ideal/legal)

[SEPA Direct Debit Terms of Service](https://stripe.com/sepa-direct-debit/legal)

You can use Checkout in setup mode to collect payment details and set up future SEPA Direct Debit payments using iDEAL.

[Checkout in setup mode](/payments/save-and-reuse?platform=checkout)

[Create or retrieve a CustomerServer-side](#create-retrieve-customer)

## Create or retrieve a CustomerServer-side

To set up future SEPA Direct Debit payments using iDEAL, you must attach the SEPA Direct Debit payment method to a Customer.

[Customer](/api/customers)

Create a Customer object when your customer creates an account with your business. You can retrieve and use a customer’s stored payment method details later, if you associate the ID of the Customer object with your own internal representation of the customer.

[Set up future payments](#setup-a-payment)

## Set up future payments

This guide builds on the foundational set up future payments Checkout integration and describes how to enable iDEAL—it shows the differences between setting up future payments for cards and using iDEAL.

[set up future payments](/payments/save-and-reuse?platform=checkout)

When creating a new Checkout Session, you need to add ideal to the list of payment_method_types.

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

Using your test API keys, select any bank from the list. After confirming, you’re redirected to a test page with options to authorize or fail the payment method setup.

[test API keys](/keys#test-live-modes)

- Click Authorize test payment to test the case when the setup is successful.

- Click Fail test payment to test the case when the customer fails to authenticate.

## See also

- Accept a SEPA Direct Debit payment

[Accept a SEPA Direct Debit payment](/payments/sepa-debit/accept-a-payment)

- Set up a subscription with SEPA Direct Debit in the EU

[Set up a subscription with SEPA Direct Debit in the EU](/billing/subscriptions/sepa-debit)
