htmlIntegrate India e-mandates | Stripe Documentation[Skip to content](#main-content)India e-Mandates[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Findia-emandate-guide)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/invoicing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Finvoicing%2Findia-emandate-guide)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Invoicing](/docs/invoicing)[Global invoicing](/docs/invoicing/global-invoicing)# Integrate India e-mandates

Learn how to integrate India e-mandates with Stripe Invoicing.### India recurring payments

For a deeper dive on India recurring payments, see our comprehensive guide.

This guide provides an overview of how to generate and use India e-mandates with Stripe Invoicing for one-time payments. Currently, you can only integrate with India e-mandates through the API.

We use the term off-session to describe payments that occur without the customer’s direct involvement. These types of payments use previously collected customer payment information. In contrast, on-session payments occur when a customer is directly involved in making a payment. This can be either through the user-interface or to complete a two-factor authentication flow like 3D Secure (3DS).

[Generate a mandate](#generate-mandate)To generate a mandate, while your customer is signed in, make a call to create a SetupIntent that includes the payment method ID and mandate details.

NoteWhen you submit a request to create a SetupIntent, the start date must be a timestamp and within 1 day of today.

Command Line[curl](#)`curl https://api.stripe.com/v1/setup_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer={{CUSTOMER_ID}} \
  -d "payment_method_types[]"=card \
  -d "payment_method_options[card][mandate_options][reference]"={{REFRENCE}} \
  -d "payment_method_options[card][mandate_options][description]"={{DESCRIPTION}} \
  -d "payment_method_options[card][mandate_options][amount]"=2000 \
  -d "payment_method_options[card][mandate_options][currency]"=inr \
  -d "payment_method_options[card][mandate_options][amount_type]"=fixed \
  -d "payment_method_options[card][mandate_options][start_date]"=1672549767 \
  -d "payment_method_options[card][mandate_options][end_date]"=1685592567 \
  -d "payment_method_options[card][mandate_options][interval]"=month \
  -d "payment_method_options[card][mandate_options][interval_count]"=1`After creating the SetupIntent, use the Payment Element to collect the customer’s payment details and set up future payments. Use stripe.confirmSetup to complete the setup using details collected by the Payment Element.

`stripe.confirmSetup({
  elements,
  confirmParams: {
    // Return URL where the customer should be redirected after the SetupIntent is confirmed.
    return_url: 'https://example.com',
  },
})
.then(function(result) {
  if (result.error) {
    // Inform the customer that there was an error.
  }
});`Confirming the SetupIntent transitions it to requires_action state, along with the next_action property describing what action needs to be taken for completing the payment.

`{
  "payment_method_options": {
    "card" : {
      "mandate_options" : {
        "reference" : "{{REFRENCE}}",
        "description" : "{{DESCRIPTION}}",
        "amount" : "{{AMOUNT}}",
        "currency" : "inr",
        "type" : "{{AMOUNT_TYPE}}",
        "start_date" : "{{START_DATE}}",
        "end_date" : "{{END_DATE}}",
        "interval" : "{{INTERVAL}}",
        "interval_count" : "{{INTERVAL_COUNT}}"
      }
    }
  },
  "status": "requires_action",
  "next_action": {
    "type": "use_stripe_sdk",
    "use_stripe_sdk": {
      "type": "three_d_secure_redirect",
      "stripe_js": "https://hooks.stripe.com/redirect/authenticate/src_xxxxxxxxxxx",
      "source": "src_xxxxxxxx"
    }
  },
  // Other existing SetupIntent params
}`Upon successful completion of AFA (3DS) by the cardholder, the SetupIntent transitions to a succeeded state and Stripe creates a mandate. The mandate is available on the SetupIntent object.

`{
  "mandate": "{{MANDATE_ID}}",
  "payment_method_options": {
    "card" : {
      "mandate_options" : {
        "reference" : "{{REFRENCE}}",
        "description" : "{{DESCRIPTION}}",
        "amount" : "{{AMOUNT}}",
        "currency" : "inr",
        "type" : "{{AMOUNT_TYPE}}",
        "start_date" : "{{START_DATE}}",
        "end_date" : "{{END_DATE}}",
        "interval" : "{{INTERVAL}}",
        "interval_count" : "{{INTERVAL_COUNT}}"
      }
    }
  },
  status: "succeeded",
  // Other existing SetupIntent params
}`NoteYou can pass the payment_method_options[card][mandate_options] parameter for all subscription registrations requests. Stripe ignores these parameters if your customer is using a non-Indian card for their subscription as the regulation doesn’t apply to them.

[Use a mandate to create an invoice](#use-mandate-invoice)When you create an invoice, you can set the default mandate for any of the invoice’s off-session payments. When you use default mandates, we recommend that you set the corresponding payment method and the default_payment_method:

Command Line`# Request to create an Invoice with a default mandate
curl https://api.stripe.com/v1/invoices \
  -u sk_test_123: \
  -d customer=cus_xyz \
  -d default_payment_method=pm_xxx \
  -d payment_settings[default_mandate]=mandate_xyz`Eventually, this invoice might attempt an off-session charge of the payment method. This is because you’ve either configured the invoice to automatically advance, have manually advanced it using the Invoice Pay endpoint, or confirmed the invoice’s payment intent. If the invoice attempts to charge your customer, the default_mandate and default_payment_method parameters work together to pay the invoice off-session.

As long as the mandate remains active—and the charge falls within the mandate’s initial parameters in terms of the amount and frequency—the charge is successfully processed. It’s also possible to set the default_mandate and default_payment_method parameters on the invoice using the Invoice Update endpoint.

[Use a mandate to charge an invoice](#use-mandate-charge)If you don’t want to set the mandate on the invoice during creation (for example, you haven’t collected the mandate), you can provide it at two later points during the mandate life cycle. The route you take depends on how you set up your existing invoicing integration.

Alternatively, if you’re using the Invoice Pay endpoint, you can provide the mandate as a top-level mandate parameter. As with setting the default mandate, explicitly provide the payment method you want to use with the mandate:

Command Line`# Request to attempt payment on an open invoice with a mandate
curl https://api.stripe.com/v1/invoices/in_aaa/pay \
  -u sk_test_123: \
  -d payment_method=pm_xxx \
  -d mandate=mandate_xyz`Similarly, you can use the mandate to confirm the payment intent associated with the invoice:

Command Line`# Request to retrieve the invoice's PaymentIntent ID
curl https://api.stripe.com/v1/invoices/in_aaa \
  -u sk_test_123:


# Response to GET /v1/invoices/in_aaa
{
  "id": "in_abc789",
  "status": "open",
  "payment_intent": "pi_zyx",
  # ... more fields
}

# Request to attempt invoice payment with a mandate by confirming the payment intent
curl https://api.stripe.com/v1/payment_intents/pi_zyc012/confirm \
  -u sk_test_123: \
  -d mandate=mandate_xyz`[Notification and waiting period](#customer-notification)Before the charge finally goes through, customers receive a notification that informs them of the charge. Customers are also given the chance to modify or cancel the mandate. After 26 hours pass, the amount is charged to the customer’s card and the invoice is moved into a paid state.

## See also

- [India recurring payments](/india-recurring-payments)
- [Invoicing API](/api/invoices)
- [How Invoicing works](/invoicing/overview)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Generate a mandate](#generate-mandate)[Use a mandate to create an invoice](#use-mandate-invoice)[Use a mandate to charge an invoice](#use-mandate-charge)[Notification and waiting period](#customer-notification)[See also](#see-also)Products Used[Invoicing](/invoicing)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`