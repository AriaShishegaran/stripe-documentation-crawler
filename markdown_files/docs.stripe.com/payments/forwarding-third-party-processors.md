htmlUse Payment Element across multiple processors | Stripe Documentation[Skip to content](#main-content)Use Payment Element across multiple processors[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fforwarding-third-party-processors)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fforwarding-third-party-processors)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)
[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[More payment scenarios](/docs/payments/more-payment-scenarios)[Forward card details to third-party API endpoints](/docs/payments/vault-and-forward)# Use Payment Element across multiple processorsBeta

Learn how to collect card details with Payment Element and use them with a third-party processor.Available in:Use Payment Element to build a custom payment flow that allows you to collect card details, create a PaymentMethod, and forward the payment method to a third-party processor.

Request accessTo gain access to use Stripe’s forwarding service, contact your Stripe representative or Stripe support.

[Create a PaymentMethodClient-side](#create-payment-method)Use a Payment Element to collect payment details. If you’re not integrated with the Payment Element, learn how to get started. After the customer submits your payment form, call stripe.createPaymentMethod to create a PaymentMethod. Pass the PaymentMethod ID to the ForwardingRequest endpoint on your server.

HTML + JSReactcheckout.js`// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');

const options = {
    mode: 'payment',
    amount: 1099,
    currency: 'usd',
    paymentMethodCreation: 'manual',
    // Fully customizable with appearance API.
    appearance: {
        theme: 'stripe'
    }
};

// Set up Stripe.js and Elements to use in checkout form
const elements = stripe.elements(options);

// Create and mount the Payment Element
const paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');

const form = document.getElementById('payment-form');
const submitBtn = document.getElementById('submit');

const handleError = (error) => {
    const messageContainer = document.querySelector('#error-message');
    messageContainer.textContent = error.message;
    submitBtn.disabled = false;
}

form.addEventListener('submit', async (event) => {
    // We don't want to let default form submission happen here,
    // which would refresh the page.
    event.preventDefault();

    // Prevent multiple form submissions
    if (submitBtn.disabled) {
        return;
    }

    // Disable form submission while loading
    submitBtn.disabled = true;

    // Trigger form validation and wallet collection
    const { error: submitError } = await elements.submit();
    if (submitError) {
        handleError(submitError);
        return;
    }

    // Create the PaymentMethod using the details collected by the Payment Element
    const { error, paymentMethod } = await stripe.createPaymentMethod({
        elements,
        params: {
            billing_details: {
                name: 'John Doe',
            }
        }
    });

    if (error) {
        // This point is only reached if there's an immediate error when
        // creating the PaymentMethod. Show the error to your customer (for example, payment details incomplete)
        handleError(error);
        return;
    }

    // Call the ForwardingRequest endpoint on your server
    const res = await fetch("/create-forwarding-request", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            paymentMethodId: paymentMethod.id,
        }),
    });
    const data = await res.json();

    // Handle the response or errors
    handleServerResponse(data);
});`[Create a ForwardingRequest](#create-forwarding-request)Contact your Stripe representative to configure your destination endpoint and begin forwarding transactions. Send the card details to this test endpoint before you connect your integration with your third-party processor.

app.js`const stripe = require("stripe")("sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz");
const express = require('express');
const app = express();

app.set('trust proxy', true);
app.use(express.json());
app.use(express.static("."));

app.post('/create-forwarding-request', async (req, res) => {
    try {
        const forwardedReq = await stripe.forwarding.requests.create(
            {
                payment_method: req.body.paymentMethodId,
                url: '{{DESTINATION_ENDPOINT}}',
                request: {
                    headers: [{
                        name: 'Destination-API-Key',
                        value: '{{DESTINATION_API_KEY}}'
                    },{
                        name: 'Destination-Idempotency-Key',
                        value: '{{DESTINATION_IDEMPOTENCY_KEY}}'
                    }],
                    body: JSON.stringify({
                        "amount": {
                            "currency": "USD",
                            "value": 1099
                        },
                        "reference": "Your order number",
                        "card": {
                            "number": "",
                            "exp_month": "",
                            "exp_year": "",
                            "cvc": "",
                            "name": "",
                        }
                    })
                },
                replacements: ['card_number', 'card_expiry', 'card_cvc', 'cardholder_name'],
            }
        );

        if (forwardedReq.response_details.status != 200) {
            // Return error based on third-party API response code
        } else {
            // Parse and handle the third-party API response
            const forwardedResult = JSON.parse(forwardedReq.response_details.body);
            res.json({
                status: forwardedReq.response_details.status
            });
        }
    } catch (err) {
        res.json({
            error: err
        });
    }
});

app.listen(3000, () => {
    console.log('Running on port 3000');
});`[Handle the ResponseClient-side](#handle-response)After you send the request, you must handle the response.

`const handleServerResponse = async (response) => {
  if (response.error) {
    // Show error on payment form
  } else if (response.status != 200) {
    // Show error based on response code
  } else {
     // Parse the response body to render your payment form
  }
}`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a PaymentMethod](#create-payment-method)[Create a ForwardingRequest](#create-forwarding-request)[Handle the Response](#handle-response)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`