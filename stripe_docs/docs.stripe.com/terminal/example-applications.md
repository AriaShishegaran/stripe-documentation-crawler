# Example applications

For a more immersive guide, check out the sample integration.

[sample integration](/terminal/quickstart)

A Stripe Terminal integration starts with your point of sale application running at a physical location. Your point of sale application communicates with a reader through the Terminal SDK to collect in-person payments from your customers. Your backend works with your point of sale application to authenticate the Terminal SDK and finalize payments.

Before starting your own integration, we recommend setting up one of the Terminal example applications. This will give you a better feel for how the components of a Terminal integration fit together and show you the interactions between the SDK, the reader, your point of sale application, and your backend code.

[Deploy the example backend](#set-up-backend)

## Deploy the example backend

To get started with the example applications, set up the Sinatra-based example backend by following the instructions in the README. You can either run the backend locally or deploy it to Render with a free account. The example backend works with the example application to authenticate the Terminal SDK and finalize payments.

[example backend](https://github.com/stripe/example-terminal-backend)

[README](https://github.com/stripe/example-terminal-backend)

[Run the example application](#run-example-app)

## Run the example application

Build and run one of the example applications:

- Clone the example from GitHub:

[GitHub](https://github.com/stripe/stripe-terminal-js-demo)

[https://github.com/stripe/stripe-terminal-js-demo.git](https://github.com/stripe/stripe-terminal-js-demo.git)

- Run the following commands to run the example:

- In the running example, enter the URL of the example backend that you deployed in step 1.

[step 1](#set-up-backend)

[Connect to a simulated reader](#connect-simulated-reader)

## Connect to a simulated reader

After you have the example running, select Use simulator to connect to a simulated reader.

[simulated reader](/terminal/references/testing#simulated-reader)

The JavaScript example app connected to a simulated reader

The simulated reader handles events just like a physical reader, so you can continue to collecting your first payment.

The simulated reader functionality is built into the SDK, so you can use it to develop and test your own point of sale application without connecting to a physical device.

[Collect your first payment](#collect-payment)

## Collect your first payment

Collect your first payment using the example application and a simulated reader. Each of the examples features an event log for you to reference as you integrate Terminal in your own application. As you collect your first payment, you’ll see the following sequence:

- Create payment: The example application collects a payment method using the SDK.

- Collect payment method: The simulated reader receives a card.

- Process and capture: The example application and backend finalize the payment.

(Optional) Use separate authorization and capture to add a reconciliation step before finalizing the transaction. You can also automatically capture Terminal transactions.

[separate authorization and capture](/payments/place-a-hold-on-a-payment-method)

[automatically capture](/api/payment_intents/create#create_payment_intent-capture_method)

Collecting a payment, using the JavaScript example app and a simulated reader

## Next steps

- Design an integration

[Design an integration](/terminal/designing-integration)
