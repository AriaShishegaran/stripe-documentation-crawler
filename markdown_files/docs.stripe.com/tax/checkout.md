htmlAutomatically collect tax on Checkout sessions | Stripe Documentation[Skip to content](#main-content)Checkout[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fcheckout)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fcheckout)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)# Automatically collect tax on Checkout sessions

Learn how to automatically calculate taxes in Checkout.Stripe Tax automatically calculates the taxes on all purchases and subscriptions accumulated during a Checkout session. If you haven’t integrated with Checkout, you must complete the integration using the Accept a Payment guide.

NoteLog in or sign up for Stripe to activate Stripe Tax.

[Update your products and prices](#product-and-price-setup)Stripe Tax uses information stored on the Products and Prices APIs to determine the right rates and rules to apply when calculating tax. Update the products and prices you use to include:

1. Tax behavior: The tax behavior on a price can be either inclusive or exclusive. This determines how the buyer sees the tax. When you set tax behavior to exclusive, it adds tax onto the subtotal amount you specify on your price. This is common in US markets and for B2B sales. When set to inclusive, the amount your buyer pays never changes, even if the tax rate varies. This is common practice for B2C buyers in many markets outside the US.

Setting the tax behavior explicitly on a price is optional, if you set up the default tax behavior in the Stripe Tax settings. You can override the default tax behavior setting by setting a tax behavior on a price.


2. (Optional) Tax code: A tax code is a classification of your product or service for Stripe Tax that makes sure we apply the correct tax rate to your transactions. Some examples include “Audio book,” “Gift card,” or “Software as a service.” If you don’t set the tax code, Stripe Tax uses the preset tax settings.



CautionYou can’t change tax_behavior after you set it to one of “exclusive” or “inclusive.” You can create a new price and archive the current one instead.

If you don’t want to create your products and prices upfront, you can pass price_data.tax_behavior and product_data.tax_code when creating Checkout sessions.

Learn more about Products, prices, tax codes, and tax behavior.

[Create a Checkout Session](#create-session)After updating your products and prices, you’re ready to start calculating tax on your Checkout sessions. You can create sessions for one time and recurring purchases.

A customer’s tax rates come from their location, which Checkout assesses from the customer’s address. The address that Checkout uses to calculate taxes depends on whether the customer is new or existing, and whether you collect shipping addresses during the Checkout Session:

New CustomerExisting CustomerCollect a billing address onlyCheckout calculates taxes based on the customer’s billing address entered into the Checkout SessionIf the customer has a previously saved shipping address, Checkout calculates taxes based on that address. Otherwise, you can calculate taxes based on billing address entered during Checkout (by specifying[customer_update[address]=auto](/api/checkout/sessions/create#create_checkout_session-customer_update-address)) or the billing address saved to the customer (the default behavior).Collect a shipping addressCheckout calculates taxes based on the customer’s shipping address entered into the Checkout SessionCheckout calculates taxes based on the customer’s shipping address entered into the Checkout Session.Existing addresses on the customer won’t apply in this case.NoteIf you wish to ensure that Google Pay is offered as a payment method while using Stripe Tax in Checkout, you must require collecting a shipping address. Apple Pay with Stripe Tax displays only when the customer’s browser supports Apple Pay version 12.

[Calculating tax for new customers](#new-customers)If you don’t pass in an existing customer when creating a Checkout session, Checkout creates a new customer and automatically saves billing address and shipping information. For tax collection purposes, Checkout uses billing and shipping addresses to determine the customer’s location.

Checkout uses the shipping address entered during the session to determine the customer’s location for calculating tax. If you don’t collect shipping information, Checkout uses the billing address.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=2 \
  -d "automatic_tax[enabled]"=true \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel"`[Calculating tax for existing customersOptional](#existing-customers)To calculate tax on Checkout sessions created for existing customers, you can set the automatic_tax[enabled] parameter to true when creating the session. You can either base tax calculations on the customer’s existing addresses or new addresses collected during the session:

### Use the existing addresses on the customer for taxes

If you’ve already collected the addresses of existing customers, you can base tax calculations on those addresses rather than the addresses collected during checkout:

- The customer address that Checkout uses for taxes: If available, Checkout uses the customer’s saved shipping address to calculate taxes. Otherwise, Checkout uses the customer’s saved billing address to calculate taxes.


- Customer address requirements: When using existing addresses for taxes, the customer must either have a valid shipping address or billing address saved. You can see whether or not a customer’s saved addresses are valid by checking the customer’s customer.tax.automatic_tax property. If the property is supported or not_collecting, it means the customer’s saved addresses are valid, and you can enable Stripe Tax on Checkout sessions for that customer.



Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=2 \
  -d "automatic_tax[enabled]"=true \
  -d customer={{CUSTOMER_ID}} \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel"`### Use the addresses collected during Checkout for taxes

You can configure Checkout to save new billing or shipping addresses to a customer. In this case, Checkout calculates tax using the address entered during checkout.

- The address that Checkout uses for taxes: If you collect shipping addresses, Checkout uses the shipping address entered during the session to calculate taxes. Otherwise, Checkout uses the billing address entered during the session to calculate taxes.


- Where Checkout saves the addresses collected during checkout: If you collect shipping addresses, Checkout saves the shipping address entered during the session to the customer’s customer.shipping.address property. Otherwise, Checkout saves the billing address entered during the session to the customer’s customer.address property. In both cases, the address used for taxes overrides any existing addresses.



If you collect shipping addresses with Checkout, set the customer_update[shipping] property to auto so that you copy the shipping information from Checkout to the customer.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=2 \
  -d "automatic_tax[enabled]"=true \
  -d customer={{CUSTOMER_ID}} \
  -d "customer_update[shipping]"=auto \
  -d "shipping_address_collection[allowed_countries][0]"=US \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel"`If you don’t collect shipping addresses with Checkout, and you want to use billing addresses entered during checkout for taxes, you must save the billing address to the customer. Set the customer_update[address] property to auto so that you copy the newly-entered address onto the provided customer.

Stripe-hosted pageEmbedded formCommand Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price]"={{PRICE_ID}} \
  -d "line_items[0][quantity]"=2 \
  -d "automatic_tax[enabled]"=true \
  -d customer={{CUSTOMER_ID}} \
  -d "customer_update[address]"=auto \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success" \
  --data-urlencode cancel_url="https://example.com/cancel"`[Check the responseOptional](#check-the-response)To inspect the results of the latest tax calculation, you can read the tax amount calculated by Checkout from the total_details.amount_tax on the Checkout Session resource. Additionally, the tax outcome for each payment is available when viewing a payment in the Dashboard.

## See also

- [Determining customer locations](/tax/customer-locations)
- [Checkout and tax IDs](/tax/checkout/tax-ids)
- [Reporting and filing](/tax/reports)
- [Use Stripe Tax with Connect](/tax/connect)
- [Calculate tax in your custom checkout flow](/tax/custom)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Update your products and prices](#product-and-price-setup)[Create a Checkout Session](#create-session)[Calculating tax for new customers](#new-customers)[Calculating tax for existing customers](#existing-customers)[Check the response](#check-the-response)[See also](#see-also)Products Used[Tax](/tax)[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`