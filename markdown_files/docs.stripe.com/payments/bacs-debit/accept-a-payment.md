htmlBacs Direct Debit payments | Stripe Documentation[Skip to content](#main-content)Accept a payment[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbacs-debit%2Faccept-a-payment)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fbacs-debit%2Faccept-a-payment)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank debits](/docs/payments/bank-debits)[Bacs Direct Debit](/docs/payments/payment-methods/bacs-debit)# Bacs Direct Debit payments

Learn to accept Bacs Direct Debit payments.Prebuilt checkout pagePayment ElementCautionStripe automatically presents your customers payment method options by evaluating their currency, payment method restrictions, and other parameters. We recommend that you configure your payment methods from the Stripe Dashboard using the instructions in Accept a payment.

If you want to continue manually configuring the payment methods you present to your customers with Checkout, use this guide (for example, to accept payments in Subscription mode). Otherwise, migrate to the dashboard.

Stripe users in the UK can use Checkout in payment mode to accept Bacs Direct Debit payments.

A Checkout Session represents the details of your customer’s intent to purchase. You create a Session when your customer wants to pay for something. After redirecting your customer to a Checkout Session, Stripe presents a payment form where your customer can complete their purchase. Once your customer has completed a purchase, they are redirected back to your site.

[Set up StripeServer-side](#set-up-stripe)First, you need a Stripe account. Register now.

Use our official libraries for access to the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create products and prices](#create-products-and-prices)To use Checkout, you first need to create a Product and a Price. Different physical goods or levels of service should be represented by products. Each product’s pricing is represented by one or more prices.

For example, you can create a T-shirt product that has two prices for different currencies, 20 GBP and 25 EUR. This allows you to change and add prices without needing to change the details of your underlying products. You can either create a product and price through the API or in the Dashboard.

If you determine your price at checkout (for example, the customer sets a donation amount) or you prefer not to create prices upfront, you can also create ad-hoc prices at Checkout Session creation using an existing product.

CautionIf you have an existing Checkout integration that doesn’t use Prices, note that the Checkout API has changed since Prices was introduced. You can use this migration guide to upgrade, or keep your existing integration.

DashboardAPINoteProducts created in test mode can be copied to live mode so that you don’t need to re-create them. In the Product detail view in the Dashboard, click Copy to live mode in the upper right corner. You can only do this once for each product created in test mode. Subsequent updates to the test product are not reflected for the live product.

Make sure you are in test mode by toggling the View test data button at the bottom of the Stripe Dashboard. Next, define the items you want to sell. To create a new product and price:

- Navigate to the[Products](https://dashboard.stripe.com/test/products)section in the Dashboard
- ClickAdd product
- SelectOne timewhen setting the price

The product name, description, and image that you supply are displayed to customers in Checkout.

[Create a Checkout SessionClient-sideServer-side](#create-session)Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

index.html`<html>
  <head>
    <title>Checkout</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>`Create a Session with line_items. Line items represent a list of items the customer is purchasing.

When your customer successfully completes their payment, they are redirected to the success_url, a page on your website that informs the customer that their payment details have been successfully collected and their payment is being processed.

When your customer clicks on your logo in a Checkout Session without completing a payment, Checkout redirects them back to your website by navigating to the cancel_url. Typically, this is the page on your website that the customer viewed prior to redirecting to Checkout.

Checkout can accept a payment and save the payment method for future use. Payment methods saved this way can be used for future payments using a PaymentIntent. After creating the Checkout Session, redirect your customer to the URL returned in the response.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "payment_method_types[]"="bacs_debit" \
  -d "line_items[][price]"="{{PRICE_ID}}" \
  -d "line_items[][quantity]"=1 \
  -d "mode"="payment" \
  -d "customer"="{{CUSTOMER_ID}}" \
  -d "payment_intent_data[setup_future_usage]"="off_session" \
  -d "success_url"="https://example.com/success?session_id={CHECKOUT_SESSION_ID}" \
  -d "cancel_url"="https://example.com/cancel"`NoteThe Bacs Direct Debit rules require that customers receive debit notification emails when payment details are initially collected and when their account is debitted. Stripe sends these emails for you by default.

Creating a Checkout Session returns a Session ID. Make the Session ID available on your success page by including the {CHECKOUT_SESSION_ID} template variable in the success_url as in the above example.

CautionDon’t rely on the redirect to the success_url alone for detecting payment initiation, as:

- Malicious users could directly access the`success_url`without paying andgain access to your goods or services.
- Customers may not always reach the`success_url`after a successful payment—they might close their browser tab before the redirect occurs.

[Handle post-payment eventsServer-side](#async)When your customer completes a payment, Stripe redirects them to the URL that you specified in the success_url parameter. Typically, this is a page on your website that informs your customer that their payment was successful.

However, Bacs Direct Debit is a delayed notification payment method, which means that funds are not immediately available. A Bacs Direct Debit payment typically takes 3 business days to make the funds available. Because of this, you’ll want to delay order fulfillment until the funds are available. Once the payment succeeds, the underlying PaymentIntent status changes from processing to succeeded.

The following Checkout events are sent when the payment status changes:

Event NameDescriptionNext steps[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)The customer has successfully authorized the debit payment bysubmitting the Checkout form.Wait for the payment to succeed or fail.[checkout.session.async_payment_succeeded](/api/events/types#event_types-checkout.session.async_payment_succeeded)The customer’s payment succeeded.Fulfill the goods or services that the customer purchased.[checkout.session.async_payment_failed](/api/events/types#event_types-checkout.session.async_payment_failed)The customer’s payment was declined, or failed for some other reason.Contact the customer via email and request that they place a new order.Your webhook code will need to handle all 3 of these Checkout events.

Each Checkout webhook payload includes the Checkout Session object, which contains information about the Customer and PaymentIntent.

The checkout.session.completed webhook is sent to your server before your customer is redirected. Your webhook acknowledgement (any 2xx status code) triggers the customer’s redirect to the success_url. If Stripe doesn’t receive successful acknowledgement within 10 seconds of a successful payment, your customer is automatically redirected to the success_url page.

On your success_url page, you’ll want to show a success message to your customer, and let them know that fulfillment of the order will take a few days as the Bacs Direct Debit payment method is not instant.

When accepting instant payments (such as credit cards) in addition to delayed notification payments, you’ll need to update your webhook endpoint to handle both kinds of payments when receiving a checkout.session.completed event.

[Ruby](#)`# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

# You can find your endpoint's secret in your webhook settings
endpoint_secret = 'whsec_...'

# Using Sinatra
post '/webhook' do
  payload = request.body.read
  event = nil

  # Verify webhook signature and extract the event
  # See https://stripe.com/docs/webhooks#verify-events for more information.
  sig_header = request.env['HTTP_STRIPE_SIGNATURE']
  begin
    event = Stripe::Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  rescue JSON::ParserError => e
    # Invalid payload
    status 400
    return
  rescue Stripe::SignatureVerificationError => e
    # Invalid signature
    status 400
    return
  end

  case event['type']
  when 'checkout.session.completed'
    session = event['data']['object']

    # Check if the order is paid (for example, from a card payment)
    payment_intent = Stripe::PaymentIntent.retrieve(session.payment_intent)
    # A delayed notification payment will have the status 'processing'
    order_paid = payment_intent.status == "succeeded"

    # Save an order in your database, marked as 'awaiting payment'
    create_order(session)

    if order_paid
      fulfill_order(session)
    end
  when 'checkout.session.async_payment_succeeded'
    session = event['data']['object']

    # Fulfill the purchase...
    fulfill_order(session)
  when 'checkout.session.async_payment_failed'
    session = event['data']['object']

    # Send an email to the customer asking them to retry their order
    email_customer_about_failed_payment(session)
  end

  status 200
end`You can get information about the customer and payment by retrieving the Customer or PaymentIntent objects referenced by the customer, payment_intent properties in the webhook payload.

### Testing webhooks locally

To test webhooks locally, you can use Stripe CLI. Once you have it installed, you can forward events to your server:

Command Line`stripe listen --forward-to localhost:4242/webhook
Ready! Your webhook signing secret is '{{WEBHOOK_SIGNING_SECRET}}' (^C to quit)`Learn more about setting up webhooks.

[Test the integration](#testing)By this point you should have a basic Bacs Direct Debit integration that collects bank account details and accepts a payment.

There are several test bank account numbers you can use in test mode to make sure this integration is ready.

Sort codeAccount numberDescription10880000012345The payment succeeds and the PaymentIntent transitions from`processing`to`succeeded`.10880090012345The payment succeeds after three minutes and the PaymentIntent transitions from`processing`to`succeeded`.10880033333335The payment is accepted but then immediately fails with a`debit_not_authorized`failure code and the PaymentIntent transitions from`processing`to`requires_payment_method`. The Mandate becomes`inactive`and the PaymentMethod can not be used again.10880093333335The payment fails after three minutes with a`debit_not_authorized`failure code and the PaymentIntent transitions from`processing`to`requires_payment_method`. The Mandate becomes`inactive`and the PaymentMethod can not be used again.10880022222227The payment fails with an`insufficient_funds`failure code and the PaymentIntent transitions from`processing`to`requires_payment_method`. The Mandate remains`active`and the PaymentMethod can be used again.10880092222227The payment fails after three minutes with an`insufficient_funds`failure code and the PaymentIntent transitions from`processing`to`requires_payment_method`. The Mandate remains`active`and the PaymentMethod can be used again.10880055555559The payment succeeds after three minutes and the PaymentIntent transitions from`processing`to`succeeded`, but a dispute is immediately created.10880000033333Payment Method creation succeeds, but the Mandate is refused by the customer’s bank and immediately transitions to inactive.10880000044444The request to set up Bacs Direct Debit fails immediately due to an invalid account number and the customer is prompted to update their information before submitting. Payment details are not collected.You can test using any of the account numbers provided above. However, because Bacs Direct Debit payments take several days to process, use the test account numbers that operate on a three-minute delay to better simulate the behavior of live payments.

NoteBy default, Stripe automatically sends emails to the customer when payment details are initially collected and each time a debit will be made on their account. These notifications aren’t sent in testmode.

## Payment failures

Payments can fail for a variety of reasons. The reason for a failure is available through charge.failure_code. You can only retry payments with certain failure codes. If you can’t retry a payment, we recommend reaching out to the customer and asking them to pay again using a different bank account or a different payment method.

Below is a list of failure codes we currently send for Bacs Direct Debit. We might add more at any time, so in developing and maintaining your code, don’t assume that only these types exist.

Failure codeDescriptionRetryable`account_closed`The bank account has been closed.No`bank_ownership_changed`The account has been transferred to a new Payment Service Provider (PSP). Check if you have been notified of the new PSP’s details. If not, you must collect a new mandate from the customer.No`debit_not_authorized`The customer has notified their bank that this payment was unauthorized or there is no mandate held by the paying bank.No`generic_could_not_process`This payment could not be processed.Yes`insufficient_funds`The customer’s account has insufficient funds to cover this payment.Yes`invalid_account_number`The account number is not valid. This could mean it is not for a GBP account or that the account cannot process Direct Debit payments.NoTo retry a payment, confirm the PaymentIntent again using the same PaymentMethod.

To ensure success, we recommend reaching out to the payer before retrying a payment.

## See also

- [Payment Intent webhooks](/payments/payment-intents/verifying-status#webhooks)
- [Managing Mandates](/payments/payment-methods/bacs-debit#mandates)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Stripe](#set-up-stripe)[Create products and prices](#create-products-and-prices)[Create a Checkout Session](#create-session)[Handle post-payment events](#async)[Test the integration](#testing)[Payment failures](#payment-failures)[See also](#see-also)Products Used[Payments](/payments)[Checkout](/payments/checkout)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`