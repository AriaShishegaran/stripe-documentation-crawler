# Collect consent for promotional emailsUS only

Promotional emails are often sent to inform customers of new products and to share coupons and discounts. For example, you can use them to subscribe customers to company newsletters or send cart abandonment emails.

[send cart abandonment emails](/payments/checkout/abandoned-carts)

Collect consent from customers to send them promotional emails

To protect consumers from unwanted spam, customers must agree to receiving promotional emails before you can contact them. Checkout helps you collect the necessary consent, where applicable, to send promotional emails. Learn more about promotional email requirements.

[Learn more](/payments/checkout/compliant-promotional-emails)

[Collect consent](#collect-consent)

## Collect consent

You can collect promotional email consent with Stripe Checkout when you create the session:

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

When consent_collection.promotions='auto', Checkout dynamically displays a checkbox for collecting the customer’s consent to promotional content.

When the checkbox is shown, the default state depends on the customer’s country and the country your business is based in. Data privacy laws vary by jurisdiction, so Checkout disables or limits this feature when local regulations prohibit it.

[Store consent and email address](#store-consent)

## Store consent and email address

The Checkout Session’s consent attribute records whether or not the session collected promotional consent from the customer.

[consent](/api/checkout/sessions/object#checkout_session_object-consent)

As customers complete purchases, keep track of which customers consent to promotional content. You can create or update an existing webhook handler to do this. Listen to the checkout.session.completed event, check for the consent.promotions status, and then store email addresses for customers who give consent.

[webhook](/webhooks)

## See also

After you’ve configured Checkout to collect consent for sending customers promotional content, you can recover abandoned carts by following up with leads who left Checkout before completing payment.

[recover abandoned carts](/payments/checkout/abandoned-carts)
