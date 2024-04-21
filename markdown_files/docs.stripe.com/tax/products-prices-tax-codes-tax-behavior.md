htmlSpecify product tax codes and tax behavior | Stripe Documentation[Skip to content](#main-content)Specify product tax codes and tax behavior[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fproducts-prices-tax-codes-tax-behavior)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fproducts-prices-tax-codes-tax-behavior)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Calculate tax](/docs/tax/calculating)# Specify product tax codes and tax behavior

Learn how to add tax codes and tax behavior to your products and prices to automatically calculate tax.NoteLog in or sign up for Stripe to activate Stripe Tax.

Stripe Tax uses product tax codes (PTCs) to associate products with their applicable tax rates, which might be lower or higher in different cities or countries. Assign each of your products a tax code to automatically apply the rate and other taxability rules.

If a product doesn’t fit any of the specific codes, use one of the codes with “General” in its name to apply the standard rate of the jurisdiction. See our list of available tax codes.

### Preset tax codes

When activating Stripe Tax you can set two types of preset tax codes: one for products and one for shipping. You can set both in the Tax settings in the Dashboard.

![The tax settings showing the preset tax codes, and the default shipping tax code.](https://b.stripecdn.com/docs-statics-srv/assets/pp_settings_v2.b1d3f908cebf1292d37b0d2f7c5cf4c0.png)

The tax settings showing the preset tax codes, and the default shipping tax code.

![Preset tax code setting in the Stripe Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/pp_settings.9b418a4caa814152a80f66c7afffd059.png)

Preset product tax code![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

The preset product tax code represents your product or service in Stripe Tax. We use the preset if you don’t explicitly specify a tax_code on your products or in product_data on your transactions. As you process payments, we also use the preset tax code to display the tax thresholds you might be approaching or have exceeded, under the Monitor tax thresholds section in your tax settings.

If you sell multiple different product types (for example, SaaS and e-books), you could use test mode to change your preset tax code and review the impact of different product types on the Monitor tab.

Preset shipping tax code![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

The preset shipping tax code  represents the tax treatment for shipping fees when charged. We use this if you don’t explicitly specify a tax_code on a shipping rate. Stripe Tax allows you to change the default shipping treatment to Nontaxable if you don’t want to charge any tax on shipping fees. We recommend you leave the default as “Shipping” to ensure the correct tax is always charged.

To charge tax on shipping for recurring payments, you can create a Product or pass product_data for a line item called “shipping” and select the shipping tax_code.

The taxability of shipping can vary by US state and country.

![Map of the United States showing states where shipping is taxable, not taxable, or have no sales tax.](https://b.stripecdn.com/docs-statics-srv/assets/pp_shipping_us_taxability.e90be097aec68286cbc6a83a4e5bfc13.png)

## Tax behavior

You must specify a tax_behavior on a price, or a default tax behavior in the tax settings in the Dashboard, which determines how tax is presented to the buyer. This allows you to localize your checkout depending on the market. When you set tax behavior to exclusive, it adds tax onto the subtotal amount you specify on your price. This is common in US markets and for B2B sales. When set to inclusive, the amount your buyer pays never changes, even if the tax rate varies. This is common practice for B2C buyers in many markets outside the US.

### Setting a default tax behavior (recommended)

You can define a default tax behavior that applies to every price that has no tax behavior defined. You can setup the default tax behavior under the Stripe Tax settings.

After you set the default tax behavior, all prices that don’t have a tax_behavior defined, use this setting and are ready for Stripe Tax. The options for the default tax behavior are:

- Inclusive:Inclusive taxis already included in the price. For example, a product has the price defined as 5.00 USD. The final price the customer pays is 5.00 USD.
- Exclusive:Exclusive taxis added on top of the price. For example, a product has the price defined as 5.00 USD. The tax charged on this product could be 10% and would result in a final price of 5.50 USD. (Tax rates might differ—this is only an explanatory example.)
- Inferred by currency: The tax behavior is based on the price that’s chosen for a product. For the currencies`USD`and`CAD`the tax behavior is exclusive. For all other currencies the tax behavior is inclusive. This also works with[multi-currency Prices](/products-prices/pricing-models#multicurrency).

To override this setting for an individual price, set a tax behavior on a price.

## Setting tax behavior on a price (optional)

You can set the tax behavior for a Price when creating it with the Dashboard or the API. When creating a Price in the Dashboard, you can inspect the impact of your pricing model on your revenue.

CautionYou can’t change tax_behavior after it’s been set to one of “exclusive” or “inclusive”.

![Tax behavior for a Price object in the Stripe Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/pp_pricing.c4124697874540947a451121f0c73c4d.png)

To create a Price with tax_behavior through the API, it might look like this:

Command Line[curl](#)`curl https://api.stripe.com/v1/prices \
 -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
 -d unit_amount=10000 \
 -d currency=usd \
 -d product=prod_q23fxaHasd \
 -d tax_behavior=exclusive \
 -d "recurring[interval]"=month`For a multi-currency Price, use the currency_options.<currency>.tax_behavior parameter to set different tax behaviors for different currencies.

In some cases, you might want to use a custom price that hasn’t been pre-configured. You can pass in price_data instead of a price ID. For example, accepting a one time payment for a custom price might look like this:

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
 -d success_url="https://example.com/success" \
 -d cancel_url="https://example.com/cancel" \
 -d "payment_method_types[0]"=card \
 -d "line_items[0][price_data][currency]"="usd" \
 -d "line_items[0][price_data][unit_amount]"=10000 \
 -d "line_items[0][price_data][tax_behavior]"="exclusive" \
 -d "line_items[0][price_data][product]"="prod_Jb3wOhvaIOZZTM" \
 -d "line_items[0][quantity]"=2 \
 -d mode=payment`## Setting a tax code on a product (recommended)

When creating Products in the Dashboard you can set your tax_code in the dropdown by searching for any available tax code. If you don’t, Stripe Tax uses the preset tax code defined on the Dashboard. If a product could fit multiple codes, for example, a SaaS product used for personal or business use depending on the type of customer, we recommend creating two separate products in Stripe and assigning the appropriate code to each.

![Tax codes for a product in the Stripe Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/pp_product_tax_category.e6ad090b235a41108b8843420db18330.png)

To create a Product with tax_code using the API, it might look like this:

Command Line[curl](#)`curl https://api.stripe.com/v1/products \
 -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
 -d name="Test Product" \
 -d tax_code=txcd_10000000`In some cases, you might want to use a custom product that hasn’t been pre-configured. You can pass in product_data instead of a product ID. For example, accepting a one time payment for a custom product might look like this:

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
 -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
 -d success_url="https://example.com/success" \
 -d cancel_url="https://example.com/cancel" \
 -d "payment_method_types[0]"=card \
 -d "line_items[0][price_data][currency]"="usd" \
 -d "line_items[0][price_data][unit_amount]"=10000 \
 -d "line_items[0][price_data][tax_behavior]"="exclusive" \
 -d "line_items[0][price_data][product_data][name]"="Product name" \
 -d "line_items[0][price_data][product_data][tax_code]"=txcd_10000000 \
 -d "line_items[0][quantity]"=2 \
 -d mode=payment`## Creating a shipping rate with tax code (optional)

Checkout payment mode allows you to set shipping rates and charge tax on shipping. You can automatically calculate tax on shipping charges by setting the tax code on the shipping rate in the Dashboard or API.

![Shipping rate with a tax code in the Stripe Dashboard](https://b.stripecdn.com/docs-statics-srv/assets/pp_shipping_rate_v3.a204f73ab02310683aace14717d960f4.png)

Command Line[curl](#)`curl https://api.stripe.com/v1/shipping_rates \
 -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
 -d display_name="Ground shipping" \
 -d type="fixed_amount" \
 -d "fixed_amount[amount]"=500 \
 -d "fixed_amount[currency]"=usd \
 -d tax_behavior="inclusive" \
 -d tax_code="txcd_92010001"`## See also

- [Checkout and Tax](/tax/checkout)
- [Invoicing and Tax](/tax/invoicing)
- [Determining customer locations](/tax/customer-locations)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Tax behavior](#tax-behavior)[Setting tax behavior on a price (optional)](#setting-tax-behavior-on-a-price-(optional))[Setting a tax code on a product (recommended)](#tax-code-on-product)[Creating a shipping rate with tax code (optional)](#shipping-rate)[See also](#see-also)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`