htmlCollect taxes for recurring payments | Stripe Documentation[Skip to content](#main-content)Collect taxes[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Ftaxes%2Fcollect-taxes)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Ftaxes%2Fcollect-taxes)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)[Subscriptions](/docs/subscriptions)[Tax](/docs/billing/taxes)# Collect taxes for recurring payments

Learn how to collect and report taxes for recurring payments.To calculate tax for recurring payments, Stripe offers Stripe Tax and Tax Rates.

- Stripe Tax—a paid product that automatically calculates the tax on your transactions without the need to define the rates and rules. Fees only apply after you’ve added at least one location where you’re registered to calculate and remit tax. For more information, see Stripe Tax.


- Tax Rates—a free feature that allows you to define any number of tax rates for invoices, subscriptions, and one-time payments that use Checkout. Stripe won’t create or maintain any tax rates on your behalf. For more information, see Tax Rates and how to use them.



Stripe TaxTax RatesStripe Tax allows you to calculate the tax to collect on your recurring payments when using Stripe Billing. You can create new subscriptions or add Stripe Tax to existing subscriptions, and examine any potential impact to the amount on your customer’s upcoming invoice. Stripe Tax is natively integrated with Stripe Billing and automatically handles tax calculation with your pricing model (for example, sub-cent, package), prorations, discounts, trials, and more. This guide assumes you’re setting up Stripe Tax and Billing for the first time.

To update existing subscriptions, reference the Update existing subscriptions guide.

NoteLog in or sign up for Stripe to activate Stripe Tax.

[Update your products and prices](#product-and-price-setup)Stripe Tax uses information stored on the Products and Prices APIs to determine the right rates and rules to apply when calculating tax. Update the products and prices you use to include:

1. Tax behavior: The tax behavior on a price can be either inclusive or exclusive. This determines how the buyer sees the tax. When you set tax behavior to exclusive, it adds tax onto the subtotal amount you specify on your price. This is common in US markets and for B2B sales. When set to inclusive, the amount your buyer pays never changes, even if the tax rate varies. This is common practice for B2C buyers in many markets outside the US.

Setting the tax behavior explicitly on a price is optional, if you set up the default tax behavior in the Stripe Tax settings. You can override the default tax behavior setting by setting a tax behavior on a price.


2. (Optional) Tax code: A tax code is a classification of your product or service for Stripe Tax that makes sure we apply the correct tax rate to your transactions. Some examples include “Audio book,” “Gift card,” or “Software as a service.” If you don’t set the tax code, Stripe Tax uses the preset tax settings.



CautionYou can’t change tax_behavior after you set it to one of “exclusive” or “inclusive.” You can create a new price and archive the current one instead.

If you don’t want to create your products and prices upfront, you can pass price_data.tax_behavior and product_data.tax_code when creating subscriptions.

Learn more about Products, prices, tax codes, and tax behavior.

This guide uses an e-magazine as an example of a product with a recurring payment.

First, create a Price on your server with a monthly charge for a new Product named “My Product”. For tax purposes you add two extra fields:

- `tax_behavior`on the Price object. Set to`inclusive`or`exclusive`. This is a required field if you’re using Stripe Tax with Subscriptions.
- `tax_code`on the Product object. A Stripe[tax code](/api/tax_codes), which maps to a product tax code. Consult our[list of tax codes](/tax/tax-codes)for more information.

Command Line[curl](#)`curl https://api.stripe.com/v1/products \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d name="My Product" \
  -d tax_code=txcd_10000000`Record the product ID for the product. It looks like this:

`{
  "id": "prod_H94k5odtwJXMtQ",`See all 22 linesUse the product ID to create a price.

Command Line[curl](#)`curl https://api.stripe.com/v1/prices \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d unit_amount=1000 \
  -d currency=usd \
  -d "recurring[interval]"=month \
  -d product=prod_H94k5odtwJXMtQ \
  -d tax_behavior=exclusive`NoteWhen price_data.tax_behavior is set to exclusive, tax is added onto the subtotal amount you specify. This is common in US markets and for B2B sales. When set to inclusive, the amount your buyer pays will never change, even if the tax rate varies. This is common practice for B2C buyers in many markets outside the US.

Record the price ID so you can use it in subsequent steps. It looks like this:

`{
  "id": "price_HGd7M3DV3IMXkC",`See all 28 lines[Create a customerServer-side](#create-a-customer)When a user subscribes to your website, create a Customer on your server.

When creating a customer, you can send us a description and the payment method only. However, the more information you send us, the better the tax calculation can identify the location of your customer and tax them accordingly. We recommend populating the customer.address field. Expand the tax field to confirm the location Stripe Tax has identified for your customer.

You can either add a country and a postal code:

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d description="a new user" \
  --data-urlencode email="franklin@example.com" \
  -d payment_method=pm_1FU2bgBF6ERF9jhEQvwnA7sX \
  -d "address[country]"=US \
  -d "address[postal_code]"=94103 \
  -d "expand[]"=tax`Or, ideally, add a complete billing address:

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d description="a new user" \
  --data-urlencode email="franklin@example.com" \
  -d payment_method=pm_1FU2bgBF6ERF9jhEQvwnA7sX \
  -d "address[line1]"="510 Townsend St" \
  -d "address[city]"="San Francisco" \
  -d "address[state]"=CA \
  -d "address[country]"=US \
  -d "address[postal_code]"=94103 \
  -d "expand[]"=tax`Or, only an IP address:

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d description="a new user" \
  --data-urlencode email="franklin@example.com" \
  -d payment_method=pm_1FU2bgBF6ERF9jhEQvwnA7sX \
  -d "tax[ip_address]"="127.0.0.1" \
  -d "expand[]"=tax`The expanded tax field indicates the computed tax location (using the address first, falling back on the given IP address) and if the customer is compatible with automatic tax calculation:

`{
   "id": "cus_13729he8947269",
   "object": "customer",
   // ... other fields omitted
   "tax": {
    "location": {"country": "US", "state": "CA", "source": "billing_address"},
    "ip_address": null,
    "automatic_tax": "supported",
  }
}`The value of automatic_tax has four possible states:

StatusDescriptionPossible Action`supported`Automatic tax fully supported.No further action needed.`unrecognized_location`The address isn’t valid for determining a tax location.Ask customer for an updated address and set`customer.address`to the new value.`not_collecting`The address is resolvable to a location for which you haven’t set up a registration.Depending on your tax obligations, you can either proceed and Stripe Tax won’t assess any taxes, or you might want to[add a new registration](/tax/registering)for the jurisdiction in which the customer is based.`failed`An error occurred with Stripe’s servers. This is rare.Try the request again, or contact Stripe support for additional assistance.[Create a subscriptionServer-side](#create-a-subscription)Now that the Customer is set up for tax calculation, you can create a Subscription on your server with the customer and their selected plan. To enable automatic tax calculation on subscriptions, set the automatic_tax[enabled] parameter to true:

Command Line[curl](#)`curl https://api.stripe.com/v1/subscriptions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer=cus_13729he8947269 \
  -d "items[0][price]"=price_HGd7M3DV3IMXkC \
  -d "items[0][quantity]"=1 \
  -d "automatic_tax[enabled]"=true \
  -d payment_behavior=default_incomplete \
  -d "expand[0]"=latest_invoice`Setting this parameter causes all subsequent Invoices to be created with automatic tax calculations activated.

To inspect the results of the latest tax calculation, retrieve the latest Invoice of a Subscription. You can do this by expanding the latest_invoice field on any Subscription request, as in the examples above. You can retrieve the tax amounts from the tax and total_tax_amounts fields on the latest invoice, and also from the per-line item tax_amounts fields.

If Stripe Tax does not have enough information to determine the customer’s location, a customer_tax_location_invalid error is returned.

[Collect payment information to activate the subscriptionClient-side](#collect-payment)To complete payment of the first invoice and activate the subscription, use stripe.confirmCardPayment when your customer submits the form.

`const btn = document.querySelector('#submit-payment-btn');
btn.addEventListener('click', async (e) => {
  e.preventDefault();
  const nameInput = document.getElementById('name');

  // Create payment method and confirm payment intent.
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: cardElement,
      billing_details: {
        name: nameInput.value,
      },
    }
  }).then((result) => {
    if(result.error) {
      alert(result.error.message);
    } else {
      // Successful subscription payment
    }
  });
});`The subscription automatically becomes active upon payment. See our Subscriptions with Elements guide for more details on setting up your checkout page.

[Handling location validation](#handling-location-validation)Stripe Tax requires a recognized customer location to calculate tax.

We recommend validating a customer’s automatic_tax status before attempting to create or update a subscription or one-off draft invoice with automatic_tax[enabled]=true.

Creating or updating a subscription or invoice behaves the following way when the customer location is unrecognized:

- Creating or updating a subscription thatcauses an immediateinvoice and payment attempt errors with an HTTP status 400 response.
- Updating a subscription thatdoes not cause an immediateinvoice or payment attempt returns an HTTP status 200 response. However, the customer location validation happens later asynchronously when the invoice is finalized. If the customer location is invalid during invoice finalization, Stripe sends a`invoice.finalization_failed`webhook. If you don’t take any action, the invoice remains in a`draft`state, regardless of the value of`auto_advance`.
- Creating or updating a draft invoice (either within the short window after a subscription cycle, or for a one-off invoice) updates the invoice’s`automatic_tax.status`to`requires_location_inputs`. You can then either update the customer object to correct the address, and then update or finalize the invoice, or turn off automatic tax calculation. If you don’t take any action, the invoice remains in a`draft`state, regardless of the value of`auto_advance`.

If tax calculation fails due to an unrecognized customer location on a recurring Subscription Invoice, Stripe sends a invoice.finalization_failed webhook when attempting to finalize the invoice. Keep this in mind when updating the location details of your customer.

We recommend listening for Subscription-related events (for example, invoice finalization failures) with webhooks because most activity happens asynchronously.

[Previewing a price before creating a customer or subscriptionOptional](#preview-price)Stripe also provides an endpoint for previewing an upcoming invoice for a subscription. You can use this endpoint to preview the initial invoice for a new subscription:

Command Line[curl](#)`curl -G https://api.stripe.com/v1/invoices/upcoming \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer=cus_13729he8947269 \
  -d "subscription_items[0][price]"=price_HGd7M3DV3IMXkC \
  -d "subscription_items[0][quantity]"=1 \
  -d "automatic_tax[enabled]"=true`If you haven’t created a Customer yet, but you’ve collected your customer’s billing information, you can use the customer_details parameter in the place of a Customer ID:

Command Line[curl](#)`curl -G https://api.stripe.com/v1/invoices/upcoming \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "customer_details[address][line1]"="510 Townsend St" \
  -d "customer_details[address][city]"="San Francisco" \
  -d "customer_details[address][state]"=CA \
  -d "customer_details[address][country]"=US \
  -d "customer_details[address][postal_code]"=94103 \
  -d "subscription_items[0][price]"=price_HGd7M3DV3IMXkC \
  -d "subscription_items[0][quantity]"=1 \
  -d "automatic_tax[enabled]"=true`When previewing the first invoice for a subscription, the subscription ID in the response won’t point to a valid subscription.

You can also use this endpoint if you have an ongoing subscription without taxes enabled and would like to preview what the upcoming invoice would look like if you were to enable automatic tax.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/invoices/upcoming \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d customer=cus_13729he8947269 \
  -d subscription=sub_1JebWO2eZvKYlo2C1WYmWFd3 \
  -d "automatic_tax[enabled]"=true`## See also

- [Determining customer locations](/tax/customer-locations)
- [Customer tax IDs](/billing/customer/tax-ids)
- [Reporting and filing](/tax/reports)
- [Tax Rates](/billing/taxes/tax-rates)
- [Tax Rates on Invoices](/invoicing/taxes/tax-rates)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Update your products and prices](#product-and-price-setup)[Create a customer](#create-a-customer)[Create a subscription](#create-a-subscription)[Collect payment information to activate the subscription](#collect-payment)[Handling location validation](#handling-location-validation)[Previewing a price before creating a customer or subscription](#preview-price)[See also](#see-also)Products Used[Tax](/tax)[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`