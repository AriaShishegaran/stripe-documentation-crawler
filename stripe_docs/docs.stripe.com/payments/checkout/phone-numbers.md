# Collect customer phone numbers with Checkout

You can enable phone number collection in Checkout if you need  to collect a phone number for shipping or invoicing. Only collect phone numbers if you need them for the transaction. You can enable phone number collection on all payment and subscription mode Sessions (phone number collection isn’t supported in setup mode). This guide assumes that you’ve already integrated Checkout. If you haven’t, see the guide.

[mode](/api/checkout/sessions/create#create_checkout_session-mode)

[guide](/payments/checkout)

[Enable phone number collection](#create-session)

## Enable phone number collection

To enable phone number collection, set phone_number_collection[enabled] to true when creating a Checkout session.

[phone_number_collection[enabled]](/api/checkout/sessions/create#create_checkout_session-phone_number_collection-enabled)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

The above code example creates a Session in payment mode with phone number collection enabled. To enable phone number collection in subscription mode, make the same changes highlighted in green to your subscription mode Session creation request.

With phone number collection enabled, Checkout adds a required phone number field to the payment form. If you’re collecting a shipping address, the phone number field displays under the address fields. Otherwise, Checkout displays the phone number field below the email input. Customers can only enter one phone number per session.

[After the session](#after-session)

## After the session

After the session, you can retrieve customer phone numbers from the resulting Customer, or Checkout Session objects:

[Customer](/api/customers)

[Checkout Session](/api/checkout/sessions)

When your customer checks out with third-party wallets like Apple Pay, or Google Pay, the phone number format isn’t guaranteed due to limitations on those platforms. Checkout attempts to save phone numbers from third-party wallets in E.164 format when possible. In all other cases, when a customer doesn’t use Apple Pay, or Google Pay, we guarantee phone numbers in E.164 format.

[Apple Pay](/apple-pay)

[Google Pay](/google-pay)

[E.164](https://en.wikipedia.org/wiki/E.164)

[Apple Pay](/apple-pay)

[Google Pay](/google-pay)

[E.164](https://en.wikipedia.org/wiki/E.164)

- On the Customer: Checkout saves collected phone numbers onto the phone property of the Customer object, which you can access programmatically by either fetching the Customer object directly with the API, or by listening for the customer.created event in a webhook. You can also view the customer’s phone number in the dashboard.

[On the Customer](/api/customers)

[phone](/api/customers/object#customer_object-phone)

[API](/api/customers/retrieve)

[customer.created](/api/events/types#event_types-customer.created)

[webhook](/webhooks)

[dashboard](https://dashboard.stripe.com/customers)

- On the Checkout Session: The customer’s phone number is also saved in the customer_details hash of the Checkout Session object, under customer_details.phone. After each successful Checkout Session, Stripe emits the checkout.session.completed event containing the Checkout Session object (and phone number), which you can listen for in a webhook.

[On the Checkout Session](/api/checkout/sessions)

[customer_details](/api/checkout/sessions/object#checkout_session_object-customer_details)

[customer_details.phone](/api/checkout/sessions/object#checkout_session_object-customer_details-phone)

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[webhook](/webhooks)

[Collecting phone numbers for existing customers](#existing-customers)

## Collecting phone numbers for existing customers

Passing in an existing Customer with a populated phone property to the Checkout Session results in the phone number field being prefilled.

[Customer](/api/customers)

[phone](/api/customers/object#customer_object-phone)

[Checkout Session](/api/checkout/sessions)

If the customer updates their phone number, this updated value persists on the phone property on the Customer object , overwriting any previously saved phone number.

[phone](/api/checkout/sessions/object#checkout_session_object-phone)

[Customer object](/api/customers)

You can allow customers to manage their own accounts (which includes updating their phone numbers) in the customer portal.

[updating their phone numbers](/api/customer_portal/configurations/create#create_portal_configuration-features-customer_update-allowed_updates)

## See also

- Integrating the customer portal

[Integrating the customer portal](/customer-management)
