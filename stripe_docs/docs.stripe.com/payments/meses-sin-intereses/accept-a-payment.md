# Accept meses sin intereses card payments

Installments (meses sin intereses) is a feature of consumer credit cards in Mexico that allows customers to split purchases over multiple billing statements. You receive payment as if it were a normal one-time charge, with fees deducted, and the customer’s bank handles collecting the money over time.

Some restrictions apply to which transactions and cards can use installments. Review the compatibility requirements.

[compatibility requirements](/payments/mx-installments#requirements)

Accepting an installment payment incurs an additional fee to the standard credit card transaction fee.

[an additional fee](/payments/mx-installments#fees)

You can enable installments across a variety of Stripe products. Choose the instructions below matching your implementation.

## Integrate with Checkout

You can accept installments with Checkout.

[Checkout](/payments/checkout)

Checkout creates a secure, Stripe-hosted payment page that lets you collect payments quickly. It works across devices and can help increase your conversion. Checkout provides a low-code way to get started accepting payments.

Your customers use Checkout to pay with cards (with or without installments) and other payment methods that support Checkout.

## Enable installments with the Checkout Sessions API

Stripe Checkout allows you to collect installment payments. You can use this integration guide to set up Checkout. After you set up Checkout, you can use it to enable installments by following the instructions below.

[integration guide](/checkout/quickstart)

- Review Checkout documentation

[Review Checkout documentation](#review-checkout-docs)

- Create a new Checkout session

[Create a new Checkout session](#create-new-session)

- Select an Installment plan on the client

[Select an Installment plan on the client](#select-plan)

- Retrieve the selected Installment plan

[Retrieve the selected Installment plan](#retrieve-plan)

[Review Checkout documentation](#review-checkout-docs)

## Review Checkout documentation

Review the Checkout Sessions API integration guide and Checkout Sessions API docs to familiarize yourself with how to create a Checkout page.

[Checkout Sessions API integration guide](/checkout/quickstart)

[Checkout Sessions API docs](/api/checkout/sessions)

[Create a new Checkout session](#create-new-session)

## Create a new Checkout session

Create a new Checkout session with installments enabled as shown in the example below. You need to substitute your own API key and price object.

Installments only works with payment mode, not setup or subscription mode.

[Select an Installment plan on the client](#select-plan)

## Select an Installment plan on the client

The hosted Checkout page displays the available installment options based on the credit card number provided by the customer.

If a customer clicks on Pay in installments (meses sin intereses), the installment plan option selected by default is the first plan on the list.

The customer can select their desired installment option using the Checkout interface.

Installment plans only show up for credit cards that support them and for transactions that have a total amount greater than or equal to 300.00 MXN.

In test mode, you can use test card numbers to test different behaviors.

[test mode](/test-mode)

[use test card numbers](#testing)

[Retrieve the selected Installment plan](#retrieve-plan)

## Retrieve the selected Installment plan

The selected installment plan is available through both Dashboard and API. In the Dashboard, click on a payment and scroll down to Payment details. If the transaction used installments, you’ll see the length of the plan…

The selected installment plan is also available on the Payment Intent. After the user has completed payment, get the payment intent ID from the Checkout Session object (for example, "payment_intent": "pi_...") and then use that payment intent ID to retrieve the PaymentIntent object to see which installment plan the customer selected.

With the payment intent ID, retrieve the PaymentIntent object:

The PaymentIntent object then shows the selected installment plan:

At this point, you’ve successfully used the Checkout Sessions API to accept payments using installments. For more information on setting up Checkout, review the Checkout integration guide. For more information on the installments API setup, review the instructions for integrating with the Payment Intents API. You might also find useful information in the Checkout Sessions and Payment Intents API docs.

[Checkout integration guide](/checkout/quickstart)

[Payment Intents API](/payments/payment-intents)

[Checkout Sessions](/api/checkout/sessions)

[Payment Intents](/api/payment_intents/object)

## Custom settings

You can customize your installments configuration using the Stripe Dashboard payment methods settings page.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

You can find the option to enable or disable installments in your payment methods settings page. This setting allows you to enable installments for no-code payment methods, including Payment Links and Checkout.

[payment methods settings page](https://dashboard.stripe.com/settings/payment_methods)

Separately, on the payment methods settings page, you can also configure the specific monthly plans you want to offer and the minimum and maximum transaction amounts for each plan. These plan configurations apply to all of your existing installments integrations.

## Test the integration

You can use the following cards to test your integration:
