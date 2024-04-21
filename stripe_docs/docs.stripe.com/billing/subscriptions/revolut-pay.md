# Set up a subscription with Revolut PayBeta

Use this guide to set up a subscription using Revolut Pay as a payment method.

[subscription](/billing/subscriptions/creating)

[Revolut Pay](/payments/revolut-pay)

Currently, only gated businesses have access to use this payment method. Email us at revolutpay-beta@stripe.com to gain access.

[revolutpay-beta@stripe.com](mailto:revolutpay-beta@stripe.com)

Create and confirm a subscription using two API calls. The first API call uses the Setup Intents API to set Revolut Pay as a payment method. The second API call sends customer, product, and payment method information to the Subscriptions API to create a Subscription and confirm a payment in one call.

[first API call](/billing/subscriptions/revolut-pay#create-setup-intent)

[Setup Intents API](/api/setup_intents)

[second API call](/billing/subscriptions/revolut-pay#create-subscription)

[Subscriptions API](/api/subscriptions)

[Create a product and priceDashboard](#create-product-plan-code)

## Create a product and priceDashboard

Products represent the item or service you’re selling. Prices define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

[Products](/api/products)

[Prices](/api/prices)

This guide uses a stock photo service as an example and charges customers a 15 GBP monthly subscription. To model this:

- Navigate to the Add a product page.

[Add a product](https://dashboard.stripe.com/test/products/create)

- Enter a Name for the product.

- Enter 15 for the price.

- Select GBP as the currency.

- Click Save product.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: price_G0FvDp6vZvdwRZ.

[Create a SetupIntentServer-side](#create-setup-intent)

## Create a SetupIntentServer-side

Create a SetupIntent to save a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process.

[SetupIntent](/api/setup_intents)

[https://www.stripe.com](https://www.stripe.com)

The SetupIntent object contains a client_secret, which is a unique key that you must pass to Stripe.js on the client side to redirect your buyer to Revolut Pay and authorize the mandate.

[Create a subscriptionServer-side](#create-subscription)

## Create a subscriptionServer-side

Create a subscription that has a price and a customer. Set the value of the default_payment_method parameter to the PaymentMethod ID from the SetupIntent response.

Creating subscriptions automatically charges customers due to the pre-set default payment method. After a successful payment, the status in the Stripe Dashboard changes to Active. The price that you previously set up determines the amount for future billings. Learn how to create a subscription with a free trial period.

[create a subscription with a free trial period](#trial-periods)
