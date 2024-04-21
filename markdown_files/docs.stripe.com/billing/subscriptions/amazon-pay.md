htmlSet up a subscription with Amazon Pay | Stripe Documentation[Skip to content](#main-content)Amazon Pay[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Famazon-pay)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Fsubscriptions%2Famazon-pay)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)[Manage subscription cycles](/docs/billing/subscriptions/change)[Set payment methods for subscriptions](/docs/billing/subscriptions/payment-methods-setting)# Set up a subscription with Amazon PayBeta

Learn how to create and charge for a subscription with Amazon Pay.Use this guide to set up a subscription using Amazon Pay as a payment method.

NoteCurrently, only gated businesses have access to use this payment method. Email us at amazonpay-beta@stripe.com to gain access.

SetupIntents APISubscriptions APIPrebuilt checkout pageCreate and confirm a subscription using two API calls. The first API call uses the Setup Intents API to set Amazon Pay as a payment method. The second API call sends customer, product, and payment method information to the Subscriptions API to create a Subscription and confirm a payment in one call.

[Create a product and priceDashboard](#create-product-plan-code)Products represent the item or service you’re selling. Prices define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

This guide uses a stock photo service as an example and charges customers a 15 USD monthly subscription. To model this:

1. Navigate to the[Add a product](https://dashboard.stripe.com/test/products/create)page.
2. Enter aNamefor the product.
3. Enter15for the price.
4. SelectUSDas the currency.
5. ClickSave product.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: price_G0FvDp6vZvdwRZ.

[Create or retrieve a CustomerServer-side](#web-create-customer)To save an Amazon Pay payment method for future payments, you must attach it to a Customer.

Create a Customer object after your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the payment method details that you store later. If your customer hasn’t created an account, you can still create a Customer object and associate it with your internal representation of their account at a later point.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  --data-urlencode description="My First Test Customer (created for API docs)"`[Create a SetupIntentServer-side](#create-setup-intent)Create a SetupIntent to save a customer’s payment method for future payments. A SetupIntent is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this set up process. Create a SetupIntent on your server with payment_method_types set to amazon_pay and specify the Customer’s ID and usage=off_session or usage=on_session.

Command Line[curl](#)`curl https://api.stripe.com/v1/setup_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d confirm=true \
  --data-urlencode return_url="https://www.stripe.com" \
  -d usage=off_session \
  -d customer=cus_ODQluYFNl44ODI \
  -d "payment_method_data[type]"=amazon_pay \
  -d "payment_method_types[]"=amazon_pay \
  -d "mandate_data[customer_acceptance][type]"=online \
  -d "mandate_data[customer_acceptance][online][ip_address]"="127.0.0.0" \
  -d "mandate_data[customer_acceptance][online][user_agent]"=device`The SetupIntent object contains a client_secret, which is a unique key that you must pass to Stripe.js on the client side to redirect your buyer to Amazon Pay and authorize the mandate.

### Retrieve the client secret

The SetupIntent includes a client secret that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

Single-page applicationServer-side renderingRetrieve the client secret from an endpoint on your server, using the browser’s fetch function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

main.rb[Ruby](#)`get '/secret' do
  intent = # ... Create or retrieve the SetupIntent
  {client_secret: intent.client_secret}.to_json
end`And then fetch the client secret with JavaScript on the client side:

`(async () => {
  const response = await fetch('/secret');
  const {client_secret: clientSecret} = await response.json();
  // Render the form using the clientSecret
})();`Next, you save Amazon Pay on the client with Stripe.js.

Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

checkout.html`<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/v3/"></script>
</head>`When a customer clicks to pay with Amazon Pay, use Stripe.js to submit the payment to Stripe. Stripe.js is the foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and enables you to extend your integration to other payment methods. Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

checkout.html`<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/v3/"></script>
</head>`Create an instance of Stripe.js with the following JavaScript on your checkout page.

You also need to specify the beta flag, amazon_pay_pm_beta_1, to use Amazon Pay with Stripe.js.

client.js`// Set your publishable key. Remember to change this to your live publishable key in production!
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY',
  {betas: ['amazon_pay_pm_beta_1']}
);`Use stripe.confirmAmazonPaySetup to confirm the setupIntent on the client side, with a return_url and mandate_data. Use the return_url to redirect customers to a specific page after the SetupIntent succeeds.

client.js`// Redirects away from the client
 const {error} = await stripe.confirmAmazonPaySetup(
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
 }`[Create a subscriptionServer-side](#create-subscription)Create a subscription that has a price and a customer. Set the value of the default_payment_method parameter to the PaymentMethod ID from the SetupIntent response.

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d "items[0][price]"={{PRICE_ID}} \
  -d default_payment_method={{PAYMENT_METHOD_ID}} \
  -d off_session=true`Creating subscriptions automatically charges customers due to the pre-set default payment method. After a successful payment, the status in the Stripe Dashboard changes to Active. The price that you previously set up determines the amount for future billings. Learn how to create a subscription with a free trial period.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a product and price](#create-product-plan-code)[Create or retrieve a Customer](#web-create-customer)[Create a SetupIntent](#create-setup-intent)[Create a subscription](#create-subscription)Products Used[Billing](/billing)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`