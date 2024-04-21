# Set up a subscription with Amazon PayBeta

Use this guide to set up a subscription using Amazon Pay as a payment method.

[subscription](/billing/subscriptions/creating)

[Amazon Pay](/payments/amazon-pay)

Currently, only gated businesses have access to use this payment method. Email us at amazonpay-beta@stripe.com to gain access.

[amazonpay-beta@stripe.com](mailto:amazonpay-beta@stripe.com)

Create and confirm a subscription using two API calls. The first API call uses the Setup Intents API to set Amazon Pay as a payment method. The second API call sends customer, product, and payment method information to the Subscriptions API to create a Subscription and confirm a payment in one call.

[first API call](/billing/subscriptions/amazon-pay#create-setup-intent)

[Setup Intents API](/api/setup_intents)

[second API call](/billing/subscriptions/amazon-pay#create-subscription)

[Subscriptions API](/api/subscriptions)

[Create a product and priceDashboard](#create-product-plan-code)

## Create a product and priceDashboard

Products represent the item or service you’re selling. Prices define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

[Products](/api/products)

[Prices](/api/prices)

This guide uses a stock photo service as an example and charges customers a 15 USD monthly subscription. To model this:

- Navigate to the Add a product page.

[Add a product](https://dashboard.stripe.com/test/products/create)

- Enter a Name for the product.

- Enter 15 for the price.

- Select USD as the currency.

- Click Save product.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: price_G0FvDp6vZvdwRZ.

[Create or retrieve a CustomerServer-side](#web-create-customer)

## Create or retrieve a CustomerServer-side

To save an Amazon Pay payment method for future payments, you must attach it to a Customer.

[Customer](/api/customers)

Create a Customer object after your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer enables you to retrieve and use the payment method details that you store later. If your customer hasn’t created an account, you can still create a Customer object and associate it with your internal representation of their account at a later point.

[Create a SetupIntentServer-side](#create-setup-intent)

## Create a SetupIntentServer-side

Create a SetupIntent to save a customer’s payment method for future payments. A SetupIntent is an object that represents your intent to set up a customer’s payment method for future payments. The SetupIntent tracks the steps of this set up process. Create a SetupIntent on your server with payment_method_types set to amazon_pay and specify the Customer’s ID and usage=off_session or usage=on_session.

[SetupIntent](/api/setup_intents)

[SetupIntent](/api/setup_intents)

[payment_method_types](/api/setup_intents/create#create_setup_intent-payment_method_types)

[usage=off_session](/api/setup_intents/create#create_setup_intent-usage)

[https://www.stripe.com](https://www.stripe.com)

The SetupIntent object contains a client_secret, which is a unique key that you must pass to Stripe.js on the client side to redirect your buyer to Amazon Pay and authorize the mandate.

The SetupIntent includes a client secret that the client side uses to securely complete the payment process. You can use different approaches to pass the client secret to the client side.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

Retrieve the client secret from an endpoint on your server, using the browser’s fetch function. This approach is best if your client side is a single-page application, particularly one built with a modern frontend framework like React. Create the server endpoint that serves the client secret:

And then fetch the client secret with JavaScript on the client side:

Next, you save Amazon Pay on the client with Stripe.js.

[Stripe.js](/payments/elements)

Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

When a customer clicks to pay with Amazon Pay, use Stripe.js to submit the payment to Stripe. Stripe.js is the foundational JavaScript library for building payment flows. It automatically handles complexities like the redirect described below, and enables you to extend your integration to other payment methods. Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

[Stripe.js](/payments/elements)

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Create an instance of Stripe.js with the following JavaScript on your checkout page.

You also need to specify the beta flag, amazon_pay_pm_beta_1, to use Amazon Pay with Stripe.js.

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

Use stripe.confirmAmazonPaySetup to confirm the setupIntent on the client side, with a return_url and mandate_data. Use the return_url to redirect customers to a specific page after the SetupIntent succeeds.

[return_url](/api/setup_intents/create#create_setup_intent-return_url)

[mandate_data](/api/setup_intents/create#create_setup_intent-mandate_data)

[return_url](/api/setup_intents/create#create_setup_intent-return_url)

[Create a subscriptionServer-side](#create-subscription)

## Create a subscriptionServer-side

Create a subscription that has a price and a customer. Set the value of the default_payment_method parameter to the PaymentMethod ID from the SetupIntent response.

Creating subscriptions automatically charges customers due to the pre-set default payment method. After a successful payment, the status in the Stripe Dashboard changes to Active. The price that you previously set up determines the amount for future billings. Learn how to create a subscription with a free trial period.

[create a subscription with a free trial period](#trial-periods)
