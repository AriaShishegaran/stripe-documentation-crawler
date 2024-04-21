htmlSet up a subscription with PayPal | Stripe Documentation[Skip to content](#main-content)PayPal[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fpaypal)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Fpaypal)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)[Manage subscription cycles](/docs/billing/subscriptions/change)[Set payment methods for subscriptions](/docs/billing/subscriptions/payment-methods-setting)# Set up a subscription with PayPal

Learn how to create and charge for a subscription with PayPal.CautionTo start accepting PayPal subscriptions on Stripe, you need to enable PayPal recurring payments from the Dashboard.

[Create a product and priceDashboard](#create-product-plan-code)Products represent the item or service you’re selling. Prices define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 EUR monthly subscription. To model this:

1. Navigate to the[Add a product](https://dashboard.stripe.com/test/products/create)page.
2. Enter aNamefor the product.
3. Enter15for the price.
4. SelectEURas the currency.
5. ClickSave product.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: price_G0FvDp6vZvdwRZ.

[Create or retrieve a Customer before setupServer-side](#web-create-a-customer)To reuse a PayPal payment method for future payments, it must be attached to a Customer.

You should create a Customer object when your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer will enable you to retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

Command Line[curl](#)`curl -X POST https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`[Create a SetupIntentServer-side](#web-create-setup-intent)A SetupIntent is an object that represents your intent and tracks the steps to set up your customer’s payment method for future payments.

Create a SetupIntent on your server with payment_method_types set to paypal and specify the Customer’s id.

Command Line[curl](#)`curl https://api.stripe.com/v1/setup_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d "payment_method_types[]"=paypal \
  -d "payment_method_data[type]"=paypal`The SetupIntent object contains a client_secret, a unique key that you need to pass to Stripe on the client side to redirect your buyer to PayPal and authorize the mandate.

[Redirect your customerClient-side](#web-confirm-setup-intent)When a customer attempts to set up their PayPal account for future payments, we recommend you use Stripe.js to confirm the SetupIntent. Stripe.js is our foundational JavaScript library for building payment flows. It will automatically handle complexities like the redirect described below, and enables you to easily extend your integration to other payment methods in the future.

Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

checkout.html`<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/v3/"></script>
</head>`Create an instance of Stripe.js with the following JavaScript on your checkout page.

`// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY',
  {}
);`To confirm the setup on the client side, pass the client secret of the SetupIntent object that you created in Step 3.

The client secret is different from your API keys that authenticate Stripe API requests. It should still be handled carefully because it can complete the charge. Do not log it, embed it in URLs, or expose it to anyone but the customer.

### Confirm PayPal Setup

To authorize you to use their PayPal account for future payments, your customer will be redirected to a PayPal billing agreement page, which they will need to approve before being redirected back to your website. Use stripe.confirmPayPalSetup to handle the redirect away from your page and to complete the setup. Add a return_url to this function to indicate where Stripe should redirect the user to after they approve the billing agreement on PayPal’s website.

client.js`// Redirects away from the client
const {error} = await stripe.confirmPayPalSetup(
  '{{SETUP_INTENT_CLIENT_SECRET}}',
  {
    return_url: 'https://example.com/setup/complete',
    mandate_data: {
      customer_acceptance: {
        type: 'online',
        online: {
            infer_from_client: true
        }
      }
    },
  }
);

if (error) {
  // Inform the customer that there was an error.
}`You can find the Payment Method owner’s email, payer ID, and Billing Agreement ID on the resulting Mandate under the payment_method_details property. You can also find the buyer’s email and payer ID in  the paypal property on the PaymentMethod.

FieldValue`verified_email`The email address of the payer on their PayPal account.`payer_id`A unique ID of the payer’s PayPal account.`billing_agreement_id`The PayPal Billing Agreement ID (BAID). This is an ID generated by PayPal which represents the mandate between the business and the customer.[Monitor webhooksServer-side](#web-monitor-webhooks)Use a method such as webhooks to confirm the billing agreement was authorized successfully by your customer, instead of relying on your customer to return to the payment status page. When a customer successfully authorizes the billing agreement, the SetupIntent emits the setup_intent.succeeded webhook event. If a customer doesn’t successfully authorize the billing agreement, the SetupIntent will emit the setup_intent.setup_failed webhook event and returns to a status of requires_payment_method. When a customer revokes the billing agreement from their PayPal account, the mandate.updated is emitted.

[Create the subscriptionServer-side](#create-subscription-code)Create a subscription with the price and customer:

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer=cus_Gk0uVzT2M4xOKD \
  -d default_payment_method=pm_1F0c9v2eZvKYlo2CJDeTrB4n \
  -d "items[0][price]"=price_F52b2UdntfQsfR \
  -d "expand[0]"="latest_invoice.payment_intent" \
  -d off_session=true`Creating subscriptions automatically charges customers because the default payment method is set. After a successful payment, the status in the Stripe Dashboard changes to Active. The price you created earlier determines subsequent billings.

[Manage subscription statusClient-side](#manage-sub-status)Assuming the initial payment succeeds, the state of the subscription is active and no further action is needed. When payments fail, the status is changed to the Subscription status configured in your automatic collection settings. You should notify the customer on failure and charge them with a different payment method.

[Update a subscriptionServer-side](#update-subscription)When you update a subscription, you need to specify off_session=true. Otherwise, any new payment will require a user redirection to PayPal for confirmation. For example, if you want to change the quantity of an item included in the subscription you can use:

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer=cus_Gk0uVzT2M4xOKD \
  -d default_payment_method=pm_1F0c9v2eZvKYlo2CJDeTrB4n \
  -d "items[0][price]"=price_F52b2UdntfQsfR \
  -d "items[0][quantity]"=2 \
  -d off_session=true`[Test the integration](#test-integration)Test your PayPal integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from requires_action to succeeded.

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click Fail test payment. The PaymentIntent will transition from requires_action to requires_payment_method.

[OptionalSetting the billing cycle](#billing-cycle)[OptionalSubscription trials](#trial-periods)[OptionalRemove a saved PayPal account](#payment-method-detatch)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a product and price](#create-product-plan-code)[Create or retrieve a Customer before setup](#web-create-a-customer)[Create a SetupIntent](#web-create-setup-intent)[Redirect your customer](#web-confirm-setup-intent)[Monitor webhooks](#web-monitor-webhooks)[Create the subscription](#create-subscription-code)[Manage subscription status](#manage-sub-status)[Update a subscription](#update-subscription)[Test the integration](#test-integration)Products Used[Billing](/billing)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`