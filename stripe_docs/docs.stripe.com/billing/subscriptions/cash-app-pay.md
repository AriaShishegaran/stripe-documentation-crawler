# Set up a subscription with Cash App Pay

Use this guide to set up a subscription using Cash App Pay as a payment method.

[subscription](/billing/subscriptions/creating)

[Cash App Pay](/payments/cash-app-pay)

Create and confirm a subscription using two API calls. The first API call uses the Setup Intents API to set Cash App Pay as a payment method. The second API call sends customer, product, and payment method information to the Subscriptions API to create a Subscription and confirm a payment in one call.

[first API call](/billing/subscriptions/cash-app-pay#create-setup-intent)

[Setup Intents API](/api/setup_intents)

[second API call](/billing/subscriptions/cash-app-pay#create-subscription)

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

[Create a SetupIntentServer-side](#create-setup-intent)

## Create a SetupIntentServer-side

Create a SetupIntent to save a customer’s payment method for future payments. The SetupIntent tracks the steps of this setup process.

[SetupIntent](/api/setup_intents)

[https://www.stripe.com](https://www.stripe.com)

The returned SetupIntent includes a client secret, which the client side uses to securely complete the setup instead of passing the entire SetupIntent object. You can use different approaches to pass the client secret to the client side. The SetupIntent response also includes a payment method ID that you need to use in the next step to confirm a PaymentIntent.

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

[pass the client secret to the client side](/payments/payment-intents#passing-to-client)

The SetupIntent response includes the status requires_action, which means your users must perform another action to complete the SetupIntent. Use the next_action.cashapp_handle_redirect_or_display_qr_code object from the SetupIntent response to redirect your users to a Stripe hosted page that displays the QR code, or render the QR code directly. To authenticate users, follow the instructions to confirm SetupIntent and save a payment method. After they authenticate, the Cash App mobile application redirects users to the return_url on their mobile device, and the SetupIntent moves to a succeeded state.

[confirm SetupIntent and save a payment method](/payments/cash-app-pay/set-up-payment?platform=web&ui=direct-api#web-create-setup-intent)

[Create a subscriptionServer-side](#create-subscription)

## Create a subscriptionServer-side

Create a subscription that has a price and customer. Set the value of the default_payment_method parameter to the PaymentMethod ID from the SetupIntent response.

Included in the response is the subscription’s first PaymentIntent, containing the client secret, which you use on the client side to securely complete the payment process instead of passing the entire PaymentIntent object. Return the client_secret to the frontend to complete payment.

[PaymentIntent](/payments/payment-intents)

[client secret](/api/payment_intents/object#payment_intent_object-client_secret)

To create a subscription with a free trial period, see Subscription trials.

[subscription](/billing/subscriptions/creating)

[Subscription trials](#trial-periods)
