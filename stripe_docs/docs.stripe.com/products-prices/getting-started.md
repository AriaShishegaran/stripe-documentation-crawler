# Get started with products and prices

Products and Prices are core resources for several Stripe integrations, including Checkout Sessions, Payment Links, Subscriptions and Invoices.

[Products](/api/products)

[Prices](/api/prices)

[Checkout Sessions](/api/checkout/sessions)

[Payment Links](/payment-links)

[Subscriptions](/billing)

[Invoices](/invoicing)

First, make sure you understand the overall goals of your integration project-make your design decisions before you start building it. For example, if you’re building a Subscription integration, read designing an integration to learn more about design decisions and pricing models to understand how to translate your business model on Stripe.

[Subscription](/billing/subscriptions/creating)

[designing an integration](/billing/subscriptions/designing-integration)

[pricing models](/products-prices/pricing-models)

Next, decide whether you need to create new products and prices in Stripe or import an existing product catalog from another system into Stripe. Create new products and prices in the Dashboard if your product catalog is small or you don’t want to use code. If you have a very large product catalog, use the Products API to import your catalog programmatically.

[Create new products and prices](#create-products-prices)

[Products](/api/products)

[import](#import-products-prices)

## Multiple products and prices

You can create as many products as you need to represent your product catalog. You can also create multiple prices for each product. Whether you should create multiple products as opposed to multiple prices depends on several factors. Generally, however, you want to:

- Create multiple prices for a single product if you’re selling the same item at different price points. For example, if you offer a subscription tier at monthly and yearly rates, create one product for the tier and one price for the monthly rate and another for the yearly rate. See an example of this for a good-better-best flat rate pricing model. (If you’re selling the same item in different currencies, then instead of creating multiple prices, create a single multi-currency Price.)

Create multiple prices for a single product if you’re selling the same item at different price points. For example, if you offer a subscription tier at monthly and yearly rates, create one product for the tier and one price for the monthly rate and another for the yearly rate. See an example of this for a good-better-best flat rate pricing model. (If you’re selling the same item in different currencies, then instead of creating multiple prices, create a single multi-currency Price.)

[good-better-best flat rate pricing model](/products-prices/pricing-models#flat-rate)

[multi-currency Price](/products-prices/pricing-models#multicurrency)

- Create multiple products if the items require different provisioning or fulfillment in your application. In the good-better-best model, for example, you would create a different product for each tier. Similarly, if you have different versions of a product, like different colors or sizes of a t-shirt, you would create a product for each version.

Create multiple products if the items require different provisioning or fulfillment in your application. In the good-better-best model, for example, you would create a different product for each tier. Similarly, if you have different versions of a product, like different colors or sizes of a t-shirt, you would create a product for each version.

[good-better-best](/products-prices/pricing-models#flat-rate)

You can copy products from test mode to live mode so that you don’t need to recreate them. Prices associated with the product are also copied over. In the Product detail view in the Dashboard, click Copy to live mode in the upper right corner.

You can only copy test products to live mode once. If you make updates to the test product after the copy, the live product won’t reflect the changes.

## Create products and prices

Using the Dashboard is the easiest way to create new products and prices. If you want to use the API, see the guide for managing products and prices; this section only describes the Dashboard steps.

[Dashboard](https://dashboard.stripe.com/products)

[managing products and prices](/products-prices/manage-prices)

To create a product in the Dashboard:

- Go to More > Product catalog.

- Click +Add product.

- Enter the Name of your product.

- (Optional) Add a Description. The description appears at checkout, on the customer portal, and in quotes.

[customer portal](/customer-management)

[quotes](/quotes)

- (Optional) Add an Image of your product. Use a JPEG or PNG file that’s smaller than 2MB. The image appears at checkout.

- (Optional) If you’re using Stripe Tax, select a Tax code for your product. See tax codes for more information about the appropriate category for your product.

[Stripe Tax](/tax)

[tax codes](/tax/tax-codes)

- (Optional) Enter a Statement descriptor. This descriptor overrides any account descriptors for recurring payments. Choose something that your customers would recognize on a bank statement.

- (Optional) Enter a Unit label. This describes how you sell your product. For example, if you charge by the seat, enter “seat” so the line item includes “per seat” for the price. Unit labels appear at checkout, and in invoices, receipts, and the customer portal.

[customer portal](/billing/subscriptions/customer-portal)

To save a product in the Dashboard, you must also add at least one price. You can also create multiple prices for a product. See create a price to learn more.

[create a price](#create-price)

To create a price in the Dashboard, you have to create a product first. You can create multiple prices for a product.

[create a product](#create-product)

- Select a Pricing model. For more details about recurring pricing models, read the pricing model guide.Flat-rate pricing: Charge the same price for each unit. If you use this option, select One time or Recurring.Package pricing: Charge by the package, or group of units, such as charging 25 EUR for every 5 units. Purchases are rounded up by default, so a customer buying 8 units pays 50 EUR.Graduated pricing: Use pricing tiers that might result in a different price for some units in an order. For example, you might charge 10 EUR per unit for the first 100 units and then 5 EUR per unit for the next 50. If you use this option, select the currency for the price and fill in the tier table.Volume pricing: Charge the same price for each unit based on the total number of units sold. For example, you might charge 10 EUR per unit for 50 units, and 7 EUR per unit for 100 units. If you use this option, select the currency for the price and fill in the tier table.Customer chooses price: Let the payer decide on the amount to pay for your product, service, or cause. Customer chooses price is only compatible with Checkout and Payment Links.Usage-based pricing: Charge your customers based on how much of your service they use during the billing cycle.

Select a Pricing model. For more details about recurring pricing models, read the pricing model guide.

[pricing model guide](/products-prices/pricing-models)

- Flat-rate pricing: Charge the same price for each unit. If you use this option, select One time or Recurring.

- Package pricing: Charge by the package, or group of units, such as charging 25 EUR for every 5 units. Purchases are rounded up by default, so a customer buying 8 units pays 50 EUR.

- Graduated pricing: Use pricing tiers that might result in a different price for some units in an order. For example, you might charge 10 EUR per unit for the first 100 units and then 5 EUR per unit for the next 50. If you use this option, select the currency for the price and fill in the tier table.

- Volume pricing: Charge the same price for each unit based on the total number of units sold. For example, you might charge 10 EUR per unit for 50 units, and 7 EUR per unit for 100 units. If you use this option, select the currency for the price and fill in the tier table.

- Customer chooses price: Let the payer decide on the amount to pay for your product, service, or cause. Customer chooses price is only compatible with Checkout and Payment Links.

- Usage-based pricing: Charge your customers based on how much of your service they use during the billing cycle.

- (Optional) If you’re selling in multiple currencies, click Add another currency to set how much to charge in each currency.

(Optional) If you’re selling in multiple currencies, click Add another currency to set how much to charge in each currency.

- Select a Billing period for recurring prices. You can add a custom period if none of the drop-down options are what you want.

Select a Billing period for recurring prices. You can add a custom period if none of the drop-down options are what you want.

- Select whether to Include tax in price. Learn more about taxes and subscriptions.

Select whether to Include tax in price. Learn more about taxes and subscriptions.

[taxes and subscriptions](/billing/taxes)

- (Optional) Enter a Price description. Customers don’t see this description.

(Optional) Enter a Price description. Customers don’t see this description.

- Click Create price to save the price. You can edit the price later.

[edit the price](#edit-price)

## Import products and prices

If you have a very large product catalog, use the Products API to import your catalog programmatically. If you’re importing your product catalog to Stripe, you can use anything as your starting data source, like a product management system or CSV file.

[Products](/api/products)

Use the Products API to create a product in Stripe for each product in your system. To map products in your system to products in Stripe, assign each product that you import a unique id. For each product, use the Prices API to make a corresponding price. Make sure to store the id of the newly created price. You’ll need to pass this id when you use the products and prices in your integration.

[Products](/api/products)

[id](/api/products/create#create_product-id)

[Prices](/api/prices)

[use the products and prices](#use-products-and-prices)

Confirm the import by checking the Dashboard or using the API to list all products.

[Dashboard](https://dashboard.stripe.com/products)

[list all products](/api/products/list)

During development, you might need to run this script multiple times for testing. If you use the same Product ID, you’ll see an error stating that a Product with that ID already exists. If you haven’t used the Product yet, you can delete it using the Stripe Dashboard:

- Go to the Products Dashboard and find your Product.

Go to the Products Dashboard and find your Product.

[Dashboard](https://dashboard.stripe.com/products)

- In the Pricing section, click the overflow menu () next to the Price and select Delete Price.

In the Pricing section, click the overflow menu () next to the Price and select Delete Price.

- Click the the overflow menu () at the top of the page, and select Delete Product.

Click the the overflow menu () at the top of the page, and select Delete Product.

You’ll likely need to run through an import more than once. You can create a script to test the import and, if you want to, synch your original data source with Stripe. To make your script idempotent and resilient to errors, you can safely try to create the product first, then update it if the product already exists.

To keep your product catalog synchronized with Stripe, use webhooks or other mechanisms to trigger product updates in Stripe. To update a product programmatically, use the following pattern.

[update a product](/api/products/update)

First, find the existing price associated with the product with list all prices API to make sure the price still matches your data source. Each product should have exactly one active price.

[list all prices](/api/prices/list)

Next, check whether the decimal amount of the price has changed. The unit_amount_decimal field displays the unit amount in cents.

[field](/api/prices/object#price_object-unit_amount_decimal)

If the amount doesn’t match, you have to create a new price. When you create a new price, specify the product ID of the original product, the currency, and the updated unit_amount price.

[create a new price](/api/prices/create)

Finally, update the old price to mark it as active=false.

[update the old price](/api/prices/update)

## Use products and prices

Now that you have products and prices in Stripe, you can use them in an integration.

Specify the Price ID when you create a Checkout Session.

- If you’re using one-time prices, see how to create a Checkout Session when accepting a payment.

If you’re using one-time prices, see how to create a Checkout Session when accepting a payment.

[how to create a Checkout Session](/payments/accept-a-payment?platform=web&ui=stripe-hosted#redirect-customers)

- If you’re creating Subscriptions, see how to Checkout Session when building a subscription integration.

If you’re creating Subscriptions, see how to Checkout Session when building a subscription integration.

[how to Checkout Session](/billing/subscriptions/build-subscriptions?ui=stripe-hosted#create-session)
