# Set up Stripe Tax

If you’re a platform that wants to set up Stripe Tax for your connected accounts that are responsible for collecting, filing, and reporting taxes, see Tax for software platforms.

[Tax for software platforms](/tax/tax-for-platforms)

To set up Stripe Tax you need to configure your tax settings within the Dashboard and, depending on your integration, add one line of code.

[Dashboard](https://dashboard.stripe.com/settings/tax)

- Confirm your origin address. Review and confirm that your details are correct.

[Confirm your origin address](#origin-address)

- Select a preset tax code. We use it to apply the correct tax rate.

[Select a preset tax code](#preset-tax-code)

- Select whether prices include tax to have a tax behavior on every price for products.

[Select whether prices include tax](#default-tax-behavior)

- Add tax registrations. Add an active tax registration when you’ve exceeded a tax threshold.

[Add tax registrations](#add-registrations)

- Enable Tax in your Stripe integration or use the Stripe Tax API to start collecting tax.

[Enable Tax in your Stripe integration or use the Stripe Tax API](#integrate)

Log in or sign up for Stripe to activate Stripe Tax.

[Log in](https://dashboard.stripe.com/settings/tax)

[sign up](https://dashboard.stripe.com/register)

[Confirm your origin addressOptional](#origin-address)

## Confirm your origin addressOptional

The origin address is where your business is located or, if you sell physical goods, the address where you’re shipping goods from. We use your Stripe business address here so you only need to review and confirm that your details are correct.

[Select a preset tax code](#preset-tax-code)

## Select a preset tax code

- Preset product tax code: A product tax code is a classification of your product or service for Stripe Tax. We use this to make sure that the correct tax rate is applied to your transactions.You must select the correct product tax code for your product or service. We use this if you don’t explicitly specify a tax_code, which maps to tax codes, on your products or in product_data on your transactions. Learn about products, prices, and tax codes.

Preset product tax code: A product tax code is a classification of your product or service for Stripe Tax. We use this to make sure that the correct tax rate is applied to your transactions.

You must select the correct product tax code for your product or service. We use this if you don’t explicitly specify a tax_code, which maps to tax codes, on your products or in product_data on your transactions. Learn about products, prices, and tax codes.

[tax_code](/api/products/create#create_product-tax_code)

[product_data](/api/prices/create#create_price-product_data)

[products, prices, and tax codes](/tax/products-prices-tax-codes-tax-behavior)

- Default shipping tax code: A shipping tax code determines what type of tax treatment to apply when shipping (delivery) fees are added to the price that you charge. In some countries, the tax rate used to calculate the correct amount of tax on your product is the same rate that’s applied to the shipping fees. Some countries have a unique tax rate for shipping fees.If you’re selling digital goods or services, or if you’re located in the EU, you don’t need to select anything. Otherwise, select the most appropriate tax treatment for your business. We use this if you don’t explicitly specify a tax code on a shipping rate.

Default shipping tax code: A shipping tax code determines what type of tax treatment to apply when shipping (delivery) fees are added to the price that you charge. In some countries, the tax rate used to calculate the correct amount of tax on your product is the same rate that’s applied to the shipping fees. Some countries have a unique tax rate for shipping fees.

If you’re selling digital goods or services, or if you’re located in the EU, you don’t need to select anything. Otherwise, select the most appropriate tax treatment for your business. We use this if you don’t explicitly specify a tax code on a shipping rate.

[Select whether prices include tax](#default-tax-behavior)

## Select whether prices include tax

To calculate tax, you need to know the tax behavior of a price. The default tax behavior dictates that all prices for products have a tax behavior, in case it isn’t defined on the price itself.

You have three options:

- Exclusive: Tax is excluded from the price and is added on top of the price defined on the product.

- Inclusive: Tax is included in the price and already included in the price defined on the product.

- Automatic: Use currency to determine if tax is included or excluded. Stripe uses the currency of the price to define whether the tax is added on top of the price (excluded) or included in the price. Tax is excluded in USD and CAD, but included in all other currencies.

Learn about tax behavior for products and prices.

[tax behavior for products and prices](/tax/products-prices-tax-codes-tax-behavior#tax-behavior)

[Add registrations](#add-registrations)

## Add registrations

When your business exceeds a tax threshold (the sales volume or number of transactions where you’re required to start collecting tax), you have to register with the local tax authority before you can add tax to your transactions. If you have existing transactions on Stripe, you’ll see our monitoring tool which helps you understand where you might be registered or need to register.

You need to add any active tax registrations you have in tax settings within the Stripe Dashboard. You can either add a registration manually, or through the Monitor tax thresholds section. Additionally, you can schedule a registration to begin at a date in the future if you’re planning to register. Stripe Tax only calculates and collects tax on transactions in these locations.

We have more information on how to register in different markets. Check our guide.

[Check our guide](/tax/supported-countries)

[Enable Tax in your Stripe integration or use the Stripe Tax API](#integrate)

## Enable Tax in your Stripe integration or use the Stripe Tax API

The final step in setting up Stripe Tax is to enable automatic tax on your Stripe integration. Here’s how:

- No-code: If you’re using the Dashboard to create payments, Stripe Tax is enabled automatically unless you switch off the toggle at the bottom of the tax settings page. You can try it out by creating an invoice, subscription, quote, or payment link in the Dashboard.

[invoice](https://dashboard.stripe.com/invoices/create)

[subscription](https://dashboard.stripe.com/subscriptions/create)

[quote](https://dashboard.stripe.com/quotes/create)

[payment link](https://dashboard.stripe.com/payment-links/create)

- Low-code: If you’re using any low-code products that are currently integrated with Stripe Tax, you need to add automatic_tax[enabled]=true to each integration. Read our guides for more information:InvoicingBillingCheckout

Low-code: If you’re using any low-code products that are currently integrated with Stripe Tax, you need to add automatic_tax[enabled]=true to each integration. Read our guides for more information:

- Invoicing

[Invoicing](/tax/invoicing)

- Billing

[Billing](/tax/subscriptions)

- Checkout

[Checkout](/tax/checkout)

- Custom flows: To use Tax with PaymentIntents, or to collect tax on payments received outside of Stripe, see our integration guide for Custom Payment Flows.

Custom flows: To use Tax with PaymentIntents, or to collect tax on payments received outside of Stripe, see our integration guide for Custom Payment Flows.

[Custom Payment Flows](/tax/custom)

We also have integration builders for Checkout.

[Checkout](/checkout/quickstart)
