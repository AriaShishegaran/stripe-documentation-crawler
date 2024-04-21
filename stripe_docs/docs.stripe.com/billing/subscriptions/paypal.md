# Set up a subscription with PayPal

To start accepting PayPal subscriptions on Stripe, you need to enable PayPal recurring payments from the Dashboard.

[enable PayPal recurring payments](/payments/paypal/set-up-future-payments?platform=web#enable-recurring-payments-support-from-stripe-dashboard)

[Create a product and priceDashboard](#create-product-plan-code)

## Create a product and priceDashboard

Products represent the item or service you’re selling. Prices define how much and how frequently you charge for a product. This includes how much the product costs, what currency you accept, and whether it’s a one-time or recurring charge. If you only have a few products and prices, create and manage them in the Dashboard.

[Products](/api/products)

[Prices](/api/prices)

This guide uses a stock photo service as an example and charges customers a 15 EUR monthly subscription. To model this:

- Navigate to the Add a product page.

[Add a product](https://dashboard.stripe.com/test/products/create)

- Enter a Name for the product.

- Enter 15 for the price.

- Select EUR as the currency.

- Click Save product.

After you create the product and the price, record the price ID so you can use it in subsequent steps. The pricing page displays the ID and it looks similar to this: price_G0FvDp6vZvdwRZ.

[Create or retrieve a Customer before setupServer-side](#web-create-a-customer)

## Create or retrieve a Customer before setupServer-side

To reuse a PayPal payment method for future payments, it must be attached to a Customer.

[Customer](/api/customers)

You should create a Customer object when your customer creates an account on your business. Associating the ID of the Customer object with your own internal representation of a customer will enable you to retrieve and use the stored payment method details later. If your customer hasn’t created an account, you can still create a Customer object now and associate it with your internal representation of the customer’s account later.

[Create a SetupIntentServer-side](#web-create-setup-intent)

## Create a SetupIntentServer-side

A SetupIntent is an object that represents your intent and tracks the steps to set up your customer’s payment method for future payments.

[SetupIntent](/api/setup_intents)

Create a SetupIntent on your server with payment_method_types set to paypal and specify the Customer’s id.

[SetupIntent](/api/setup_intents)

[payment_method_types](/api/setup_intents/create#create_setup_intent-payment_method_types)

[Customer](/api/customers)

[id](/api/customers/object#customer_object-id)

The SetupIntent object contains a client_secret, a unique key that you need to pass to Stripe on the client side to redirect your buyer to PayPal and authorize the mandate.

[client_secret](/api/setup_intents/object#setup_intent_object-client_secret)

[Redirect your customerClient-side](#web-confirm-setup-intent)

## Redirect your customerClient-side

When a customer attempts to set up their PayPal account for future payments, we recommend you use Stripe.js to confirm the SetupIntent. Stripe.js is our foundational JavaScript library for building payment flows. It will automatically handle complexities like the redirect described below, and enables you to easily extend your integration to other payment methods in the future.

[Stripe.js](/js)

Include the Stripe.js script on your checkout page by adding it to the head of your HTML file.

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

Create an instance of Stripe.js with the following JavaScript on your checkout page.

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

To confirm the setup on the client side, pass the client secret of the SetupIntent object that you created in Step 3.

The client secret is different from your API keys that authenticate Stripe API requests. It should still be handled carefully because it can complete the charge. Do not log it, embed it in URLs, or expose it to anyone but the customer.

To authorize you to use their PayPal account for future payments, your customer will be redirected to a PayPal billing agreement page, which they will need to approve before being redirected back to your website. Use stripe.confirmPayPalSetup to handle the redirect away from your page and to complete the setup. Add a return_url to this function to indicate where Stripe should redirect the user to after they approve the billing agreement on PayPal’s website.

[stripe.confirmPayPalSetup](/js/setup_intents/confirm_paypal_setup)

You can find the Payment Method owner’s email, payer ID, and Billing Agreement ID on the resulting Mandate under the payment_method_details property. You can also find the buyer’s email and payer ID in  the paypal property on the PaymentMethod.

[Mandate](/api/mandates/)

[payment_method_details](/api/mandates/object#mandate_object-payment_method_details-paypal)

[paypal](/api/payment_methods/object#payment_method_object-paypal)

[PaymentMethod](/api/payment_methods)

[Monitor webhooksServer-side](#web-monitor-webhooks)

## Monitor webhooksServer-side

Use a method such as webhooks to confirm the billing agreement was authorized successfully by your customer, instead of relying on your customer to return to the payment status page. When a customer successfully authorizes the billing agreement, the SetupIntent emits the setup_intent.succeeded webhook event. If a customer doesn’t successfully authorize the billing agreement, the SetupIntent will emit the setup_intent.setup_failed webhook event and returns to a status of requires_payment_method. When a customer revokes the billing agreement from their PayPal account, the mandate.updated is emitted.

[webhooks](/payments/payment-intents/verifying-status#webhooks)

[setup_intent.succeeded](/api/events/types#event_types-setup_intent.succeeded)

[webhook](/webhooks)

[setup_intent.setup_failed](/api/events/types#event_types-setup_intent.setup_failed)

[mandate.updated](/api/events/types#event_types-mandate.updated)

[Create the subscriptionServer-side](#create-subscription-code)

## Create the subscriptionServer-side

Create a subscription with the price and customer:

[subscription](/api/subscriptions)

Creating subscriptions automatically charges customers because the default payment method is set. After a successful payment, the status in the Stripe Dashboard changes to Active. The price you created earlier determines subsequent billings.

[subscriptions](/billing/subscriptions/creating)

[default payment method](/api/customers/create#create_customer-invoice_settings-default_payment_method)

[Stripe Dashboard](https://dashboard.stripe.com/test/subscriptions)

[Manage subscription statusClient-side](#manage-sub-status)

## Manage subscription statusClient-side

Assuming the initial payment succeeds, the state of the subscription is active and no further action is needed. When payments fail, the status is changed to the Subscription status configured in your automatic collection settings. You should notify the customer on failure and charge them with a different payment method.

[automatic collection settings](/invoicing/automatic-collection)

[charge them with a different payment method](/billing/subscriptions/overview#requires-payment-method)

[Update a subscriptionServer-side](#update-subscription)

## Update a subscriptionServer-side

When you update a subscription, you need to specify off_session=true. Otherwise, any new payment will require a user redirection to PayPal for confirmation. For example, if you want to change the quantity of an item included in the subscription you can use:

[Test the integration](#test-integration)

## Test the integration

Test your PayPal integration with your test API keys by viewing the redirect page. You can test the successful payment case by authenticating the payment on the redirect page. The PaymentIntent will transition from requires_action to succeeded.

[test API keys](/keys#test-live-modes)

To test the case where the user fails to authenticate, use your test API keys and view the redirect page. On the redirect page, click Fail test payment. The PaymentIntent will transition from requires_action to requires_payment_method.

[OptionalSetting the billing cycle](#billing-cycle)

## OptionalSetting the billing cycle

[OptionalSubscription trials](#trial-periods)

## OptionalSubscription trials

[OptionalRemove a saved PayPal account](#payment-method-detatch)

## OptionalRemove a saved PayPal account
