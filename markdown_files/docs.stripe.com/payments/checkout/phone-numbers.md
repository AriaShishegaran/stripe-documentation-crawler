htmlCollect customer phone numbers with Checkout | Stripe Documentation[Skip to content](#main-content)Collect phone numbers[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fphone-numbers)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcheckout%2Fphone-numbers)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)
[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Checkout](/payments/checkout)·[Home](/docs)[Payments](/docs/payments)[Checkout](/docs/payments/checkout)# Collect customer phone numbers with Checkout

Learn how to collect phone numbers with Checkout.You can enable phone number collection in Checkout if you need  to collect a phone number for shipping or invoicing. Only collect phone numbers if you need them for the transaction. You can enable phone number collection on all payment and subscription mode Sessions (phone number collection isn’t supported in setup mode). This guide assumes that you’ve already integrated Checkout. If you haven’t, see the guide.

[Enable phone number collection](#create-session)To enable phone number collection, set phone_number_collection[enabled] to true when creating a Checkout session.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price_data][unit_amount]"=1000 \
  -d "line_items[0][price_data][product_data][name]"=T-shirt \
  -d "line_items[0][price_data][currency]"=eur \
  -d "line_items[0][quantity]"=2 \
  -d "phone_number_collection[enabled]"=true \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel"`NoteThe above code example creates a Session in payment mode with phone number collection enabled. To enable phone number collection in subscription mode, make the same changes highlighted in green to your subscription mode Session creation request.

With phone number collection enabled, Checkout adds a required phone number field to the payment form. If you’re collecting a shipping address, the phone number field displays under the address fields. Otherwise, Checkout displays the phone number field below the email input. Customers can only enter one phone number per session.

[After the session](#after-session)After the session, you can retrieve customer phone numbers from the resulting Customer, or Checkout Session objects:

### Phone number format

When your customer checks out with third-party wallets like Apple Pay, or Google Pay, the phone number format isn’t guaranteed due to limitations on those platforms. Checkout attempts to save phone numbers from third-party wallets in E.164 format when possible. In all other cases, when a customer doesn’t use Apple Pay, or Google Pay, we guarantee phone numbers in E.164 format.

- [On the Customer](/api/customers): Checkout saves collected phone numbers onto the[phone](/api/customers/object#customer_object-phone)property of the Customer object, which you can access programmatically by either fetching the Customer object directly with the[API](/api/customers/retrieve), or by listening for the[customer.created](/api/events/types#event_types-customer.created)event in a[webhook](/webhooks). You can also view the customer’s phone number in the[dashboard](https://dashboard.stripe.com/customers).

- [On the Checkout Session](/api/checkout/sessions): The customer’s phone number is also saved in the[customer_details](/api/checkout/sessions/object#checkout_session_object-customer_details)hash of the Checkout Session object, under[customer_details.phone](/api/checkout/sessions/object#checkout_session_object-customer_details-phone). After each successful Checkout Session, Stripe emits the[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)event containing the Checkout Session object (and phone number), which you can listen for in a[webhook](/webhooks).

[Collecting phone numbers for existing customers](#existing-customers)Passing in an existing Customer with a populated phone property to the Checkout Session results in the phone number field being prefilled.

If the customer updates their phone number, this updated value persists on the phone property on the Customer object , overwriting any previously saved phone number.

### Phone number updates using the customer portal

You can allow customers to manage their own accounts (which includes updating their phone numbers) in the customer portal.

## See also

- [Integrating the customer portal](/customer-management)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Enable phone number collection](#create-session)[After the session](#after-session)[Collecting phone numbers for existing customers](#existing-customers)[See also](#see-also)Products Used[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`