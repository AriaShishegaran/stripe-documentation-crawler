htmlMigrate to Confirmation Tokens | Stripe Documentation[Skip to content](#main-content)Migrate to Confirmation Tokens[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-element%2Fmigration-ct)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fpayment-element%2Fmigration-ct)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)
[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Elements](/payments/elements)·[Home](/docs)[Payments](/docs/payments)[Web Elements](/docs/payments/elements)[Payment Element](/docs/payments/payment-element)# Migrate to Confirmation Tokens

Learn how to migrate your existing "create payment method" integration to a "create confirmation token" integration.Use this guide to learn how to finalize payments on the server by using a ConfirmationToken instead of a PaymentMethod to send data collected from your client to your server.

A ConfirmationToken holds a superset of the data found on a PaymentMethod, such as shipping information, and enables new features as we build them.

[Create the Confirmation Tokenclient-side](#client-side)Instead of calling stripe.createPaymentMethod, call stripe.createConfirmationToken to create a ConfirmationToken object. Pass this ConfirmationToken to the server to confirm the PaymentIntent.

The stripe.createConfirmationToken method accepts the same parameters as stripe.createPaymentMethod (through params.payment_method_data), plus additional shipping and return_url parameters.

BeforeAftercheckout.js`// Create the PaymentMethod using the details collected by the Payment Element.
const {error, paymentMethod} = await stripe.createPaymentMethod({
  elements,
  params: {
    billing_details: {
      name: 'Jenny Rosen',
    }
  }
});


if (error) {
  // This point is only reached if there's an immediate error when creating the PaymentMethod.
  // Show the error to your customer (for example, payment details incomplete)
  handleError(error);
  return;
}

// Create the PaymentIntent
const res = await fetch("/create-confirm-intent", {
  method: "POST",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify({
    paymentMethodId: paymentMethod.id,
  }),
});`checkout.js`// Create the ConfirmationToken using the details collected by the Payment Element and additional shipping information. Provide shipping and return_url if you don't want to provide it when confirming the intent on the server
const {error, confirmationToken} = await stripe.createConfirmationToken({
  elements,
  params: {
    payment_method_data: {
       billing_details: {
         name: 'Jenny Rosen',
       }
    },
    // Remove shipping if you're collecting it using Address Element or don't require it
    shipping: {
      name: 'Jenny Rosen',
      address: {
        line1: '1234 Main Street',
        city: 'San Francisco',
        state: 'CA',
        country: 'US',
        postal_code: '94111',
      },
    },
    return_url: 'https://example.com/order/123/complete',
  }
});

if (error) {
  // This point is only reached if there's an immediate error when creating the ConfirmationToken.
  // Show the error to your customer (for example, payment details incomplete)
  handleError(error);
  return;
}

// Create the PaymentIntent
const res = await fetch("/create-confirm-intent", {
  method: "POST",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify({
    confirmationTokenId: confirmationToken.id,
  }),
});`[Create and submit the payment to Stripeserver-side](#server-side)You pass the ConfirmationToken to the server to confirm the PaymentIntent, rather than passing a PaymentMethod as you did before. The properties stored on the ConfirmationToken are applied to the Intent when its ID is provided to the confirmation_token parameter at confirmation time.

NoteIf you already provide shipping and return_url on the ConfirmationToken, you don’t need to provide those fields again when confirming the PaymentIntent.

BeforeAfterserver.js`app.post('/create-confirm-intent', async (req, res) => {
  try {
    const intent = await stripe.paymentIntents.create({
      confirm: true,
      amount: 1099,
      currency: 'usd',
      // In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
      automatic_payment_methods: {enabled: true},
      use_stripe_sdk: true,
      // the PaymentMethod ID sent by your client
      payment_method: req.body.paymentMethodId,
      return_url: 'https://example.com/order/123/complete',
      mandate_data: {
        customer_acceptance: {
          type: "online",
          online: {
            ip_address: req.ip,
            user_agent: req.get("user-agent"),
          },
        },
      },
      shipping: {
        name: 'Jenny Rosen',
        address: {
          line1: '1234 Main Street',
          city: 'San Francisco',
          state: 'CA',
          country: 'US',
          postal_code: '94111',
        },
      }
    });
    res.json({
      client_secret: intent.client_secret,
      status: intent.status
    });
  } catch (err) {
    res.json({
      error: err
    })
  }
});`server.js`app.post('/create-confirm-intent', async (req, res) => {
  try {
    const intent = await stripe.paymentIntents.create({
      confirm: true,
      amount: 1099,
      currency: 'usd',
      // In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
      automatic_payment_methods: {enabled: true},
      use_stripe_sdk: true,
      // the ConfirmationToken ID sent by your client that already has the shipping, mandate_data, and return_url data
      confirmation_token: req.body.confirmationTokenId,
    });
    res.json({
      client_secret: intent.client_secret,
      status: intent.status
    });
  } catch (err) {
    res.json({
      error: err
    })
  }
});`Any parameters provided directly to the PaymentIntent or SetupIntent at confirmation time, such as shipping override corresponding properties on the ConfirmationToken.

[OptionalSetting conditional parameters setup_future_usage or capture_method based on payment method](#conditional-options)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create the Confirmation Token](#client-side)[Create and submit the payment to Stripe](#server-side)Products Used[Elements](/payments/elements)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`