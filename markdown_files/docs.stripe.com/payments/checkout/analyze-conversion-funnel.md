htmlAnalyze your conversion funnel | Stripe Documentation[Skip to content](#main-content)Analyze conversion funnel[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fanalyze-conversion-funnel)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fanalyze-conversion-funnel)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Analyze your conversion funnel

Analyze your Stripe Checkout conversion funnel with Google Analytics 4.Use Google Analytics 4 (GA4) to track users as they progress through your Stripe Checkout purchase funnel. Before you begin, set up a GA4 account and add a GA4 property.

[Set up your site](#setup)1. Create a product page with a Checkout button:

product.html`<html>
  <head>
    <title>Buy cool new product</title>
  </head>
  <body>
    <script>
      window.addEventListener("load", function () {
        document
          .getElementById("submit")
          .addEventListener("click", function (event) {
            event.preventDefault();
            fetch("/create-checkout-session", {
              method: "POST",
            })
              .then((response) => response.json())
              .then((checkoutSession) => {
                window.location.href = checkoutSession.url;
              });
          });
      });
    </script>
    <form>
      <button id="submit">Checkout</button>
    </form>
  </body>
</html>`
2. Create a server-side endpoint that creates a Checkout Session and serves the pages:

index.js`// This example sets up endpoints using the Express framework.
// Watch this video to get started: https://youtu.be/rPR2aJ6XnAc.

const express = require("express");
require("dotenv").config();

const app = express();

// Set your secret key. Remember to switch to your live key in production!
// See your keys here: https://dashboard.stripe.com/apikeys

const stripe = require('stripe')('sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz');

const request = require("request");

app.post(
  "/create-checkout-session",
  express.urlencoded({ extended: false }),
  async (req, res) => {
    const session = await stripe.checkout.sessions.create({
      payment_method_types: ["card"],
      line_items: [
        {
          price_data: {
            currency: "usd",
            product_data: {
              name: "T-shirt",
            },
            unit_amount: 2000,
          },
          quantity: 1,
        },
      ],
      mode: "payment",
      success_url: req.get("origin") + "/success",
      cancel_url: req.get("origin") + "/cancel",
    });

    res.json({ url: session.url });
  }
);

app.get("/product", function (req, res) {
  res.sendFile(__dirname + "/product.html");
});

app.get("/success", function (req, res) {
  res.sendFile(__dirname + "/success.html");
});

app.get("/cancel", function (req, res) {
  res.sendFile(__dirname + "/cancel.html");
});

app.listen(4242, () => console.log(`Listening on port ${4242}!`));`
3. Create a success page:

success.html`<html>
  <head>
    <title>Thanks for your order!</title>
  </head>
  <body>
    <h1>Thanks for your order!</h1>
    <p>
      We appreciate your business! If you have any questions, please email
      <a href="mailto:orders@example.com">orders@example.com</a>.
    </p>
  </body>
</html>`
4. Create a canceled page:

canceled.html`<html>
  <head>
    <title>Order Canceled!</title>
  </head>
  <body>
    <p>
      <a href="/product">Start another order</a>.
    </p>
  </body>
</html>`

[Instrumentation walkthrough](#instrumentation-using-google-analytics)In the following example, we assume your customer has:

- Viewed your product page.
- Clicked theBuybutton and was redirected to Stripe Checkout.
- Completed the payment and was redirected to the success page.

### Quick summary

### Add instrumentation

1. Add checkout.stripe.com to your referral exclusion list.


2. Add Google Analytics tags to your product, success, and canceled pages. Tags automatically fire an event on page load.

product.html`<html>
  <head>
    <!-- START GOOGLE ANALYTICS -->
    <script
      async
      src="https://www.googletagmanager.com/gtag/js?id=<GOOGLE_ANALYTICS_CLIENT_ID>"
    ></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        window.dataLayer.push(arguments);
      }
      gtag("js", new Date());
      gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");
    </script>
    <!-- END GOOGLE ANALYTICS -->
    <title>Buy cool new product</title>
  </head>
  <body>
    <script>
      window.addEventListener("load", function () {
        document
          .getElementById("submit")
          .addEventListener("click", function (event) {
            event.preventDefault();
            fetch("/create-checkout-session", {
              method: "POST",
            })
              .then((response) => response.json())
              .then((checkoutSession) => {
                window.location.href = checkoutSession.url;
              });
          });
      });
    </script>
    <form>
      <button id="submit">Checkout</button>
    </form>
  </body>
</html>`success.html`<html>
  <head>
    <!-- START GOOGLE ANALYTICS -->
    <script
      async
      src="https://www.googletagmanager.com/gtag/js?id=<GOOGLE_ANALYTICS_CLIENT_ID>"
    ></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        window.dataLayer.push(arguments);
      }
      gtag("js", new Date());
      gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");
    </script>
    <!-- END GOOGLE ANALYTICS -->
    <title>Thanks for your order!</title>
  </head>
  <body>
    <h1>Thanks for your order!</h1>
    <p>
      We appreciate your business! If you have any questions, please email
      <a href="mailto:orders@example.com">orders@example.com</a>.
    </p>
  </body>
</html>`canceled.html`<html>
  <head>
    <!-- START GOOGLE ANALYTICS -->
    <script
      async
      src="https://www.googletagmanager.com/gtag/js?id=<GOOGLE_ANALYTICS_CLIENT_ID>"
    ></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        window.dataLayer.push(arguments);
      }
      gtag("js", new Date());
      gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");
    </script>
    <!-- END GOOGLE ANALYTICS -->
    <title>Order Canceled!</title>
  </head>
  <body>
    <p>
      <a href="/product">Start another order</a>.
    </p>
  </body>
</html>`
3. Fire an event just before redirecting to Stripe Checkout:

product.html`<html>
  <head>
    <!-- START GOOGLE ANALYTICS -->
    <script
      async
      src="https://www.googletagmanager.com/gtag/js?id=<GOOGLE_ANALYTICS_CLIENT_ID>"
    ></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        window.dataLayer.push(arguments);
      }
      gtag("js", new Date());
      gtag("config", "<GOOGLE_ANALYTICS_CLIENT_ID>");
    </script>
    <!-- END GOOGLE ANALYTICS -->
    <title>Buy cool new product</title>
  </head>
  <body>
    <script>
      window.addEventListener("load", function () {
        document
          .getElementById("submit")
          .addEventListener("click", function (event) {
            event.preventDefault();
            fetch("/create-checkout-session", {
              method: "POST",
            })
              .then((response) => response.json())
              .then((checkoutSession) => {
                window.location.href = checkoutSession.url;
                gtag("event", "begin_checkout", {
                  event_callback: function () {
                    window.location.href = checkoutSession.url;
                  },
                });
              });
          });
      });
    </script>
    <form>
      <button id="submit">Checkout</button>
    </form>
  </body>
</html>`

### Analyze your conversion funnel metrics

After you add the proper instrumentation, you can see the metrics corresponding to each step defined in your conversion funnel:

- product page views:The number of page visitors who viewed the product page.
- begin_checkout event count:The number of page visitors who clicked theBuybutton and were redirected to Stripe Checkout.
- success page views:The number of page visitors who completed the purchase and were redirected to the success page.

Using these numbers, you can see where visitors are dropping off in your conversion funnel.

[OptionalServer-side event recording](#server-side-event-recording)[OptionalLinking client and server-side events](#link-client-and-server-side-events)[OptionalServer-side redirects](#server-side-redirect)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up your site](#setup)[Instrumentation walkthrough](#instrumentation-using-google-analytics)Products Used[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`