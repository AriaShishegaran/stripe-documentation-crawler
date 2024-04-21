htmlCustomize redirect behavior with an embedded form | Stripe Documentation[Skip to content](#main-content)Customize redirect behavior (Embedded form)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-redirect-behavior)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fcustom-redirect-behavior)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Customize redirect behavior with an embedded form

For embedded forms, redirect your customers to a return page or prompt them to retry.If you have a Checkout integration that uses an embedded form, you can customize how and whether Stripe redirects your customers after they complete payment. You can have Stripe always redirect customers, only redirect for some payment methods, or completely disable redirects.

Common mistakeIf you’ve integrated with a Stripe-hosted payment page, you can’t use the return_url parameter. You must use success_url. Learn more about customizing a success page for integrations with a Stripe-hosted page.

To set up redirects, specify the return page in the return_url parameter.

You can also optionally:

- [Only redirect customers if the payment method requires it](#redirect-if-required)(for example, a bank authorization page for a debit-based method).
- Not use a return page and[disable redirect-based payment methods](#disable-redirects).

## Redirect customers to a return page

When you create the Checkout Session, you specify the URL of the return page in the return_url parameter. Include the {CHECKOUT_SESSION_ID} template variable in the URL. When Checkout redirects a customer, it replaces the variable with the actual Checkout Session ID.

When rendering your return page, retrieve the Checkout Session status using the Checkout Session ID in the URL. Handle the result according to the session status as follows:

- `complete`: The payment succeeded. Use the information from the Checkout Session to render a success page.
- `open`: The payment failed or was canceled. Remount Checkout so that your customer can try again.

server.js`app.get('/session_status', async (req, res) => {
  const session = await stripe.checkout.sessions.retrieve(req.query.session_id);
  const customer = await stripe.customers.retrieve(session.customer);

  res.send({
    status: session.status,
    payment_status: session.payment_status,
    customer_email: customer.email
  });
});`client.js`const session = await fetch(`/session_status?session_id=${session_id}`)
if (session.status == 'open') {
  // Remount embedded Checkout
else if (session.status == 'complete') {
  // Show success page
  // Optionally use session.payment_status or session.customer_email
  // to customize the success page
}`## Redirect-based payment methods

During payment, some payment methods redirect the customer to an intermediate page, such as a bank authorization page. When they complete that page, Stripe redirects them to your return page.

### Only redirect for redirect-based payment methods

If you don’t want to redirect customers after payments that don’t require a redirect, set redirect_on_completion to if_required. That redirects only customers who check out with redirect-based payment methods.

For card payments, Checkout renders a default success state instead of redirecting. To use your own success state, pass an onComplete callback that destroys the Checkout instance and renders your custom success state.

onComplete is called when the Checkout Session completes successfully, or when the checkout.session.completed webhook event is sent.

HTML + JSReactreturn.js`const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');

initialize();

async function initialize() {
  const fetchClientSecret = async () => {
    const response = await fetch("/create-checkout-session", {
      method: "POST",
    });
    const { clientSecret } = await response.json();
    return clientSecret;
  };

  // Example `onComplete` callback
  const handleComplete = async function() {
    // Destroy Checkout instance
    checkout.destroy()

    // Retrieve details from server (which loads Checkout Session)
    const details = await retrievePurchaseDetails();

    // Show custom purchase summary
    showPurchaseSummary(details);
  }

  const checkout = await stripe.initEmbeddedCheckout({
    fetchClientSecret,
    onComplete: handleComplete
  });

  checkout.mount('#checkout');
}`### Disable redirect-based payment methods

If you don’t want to create a return page, create your Checkout Session with redirect_on_completion set to never.

This disables redirect-based payment methods:

- If you use[Dynamic payment methods](/payments/payment-methods/dynamic-payment-methods), you can still manage payment methods from the Dashboard, but payment methods that require redirects aren’t eligible.
- If you manually specify payment methods with[payment_method_types](/api/checkout/sessions/object#checkout_session_object-payment_method_types), you can’t include any redirect-based payment methods.

Setting redirect_on_completion: never removes the return_url requirement. For these sessions, Checkout renders a default success state instead of redirecting. You can use your own success state by passing an onComplete callback which destroys the Checkout instance and renders your custom success state.

onComplete is called when the Checkout Session completes successfully, or when the checkout.session.completed webhook event is sent.

HTML + JSReactreturn.js`const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');

initialize();

async function initialize() {
  const fetchClientSecret = async () => {
    const response = await fetch("/create-checkout-session", {
      method: "POST",
    });
    const { clientSecret } = await response.json();
    return clientSecret;
  };

  // Example `onComplete` callback
  const handleComplete = async function() {
    // Destroy Checkout instance
    checkout.destroy()

    // Retrieve details from server (which loads Checkout Session)
    const details = await retrievePurchaseDetails();

    // Show custom purchase summary
    showPurchaseSummary(details);
  }

  const checkout = await stripe.initEmbeddedCheckout({
    fetchClientSecret,
    onComplete: handleComplete
  });

  checkout.mount('#checkout');
}`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Redirect customers to a return page](#return-url)[Redirect-based payment methods](#redirect-based-payment-methods)Products Used[Checkout](/payments/checkout)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`