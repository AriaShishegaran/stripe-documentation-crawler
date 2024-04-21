# Tax for marketplaces

## Tax requirements for platforms and marketplaces

Many countries and US states require marketplace operators to collect sales tax and VAT on their facilitated sales. The US refers to these businesses as marketplace facilitators, while other regions, such as Europe, might refer to them deemed sellers.

As a marketplace operator, your tax collection requirements differ depending on the country or state. However, if your electronic interface enables transactions between buyers and sellers and you directly or indirectly collect customer payments, you might need to fulfill tax collection responsibilities.

If your businesses operates a marketplace or platform, you must first determine whether they qualify as a marketplace facilitator or a deemed seller, then make sure that they maintain tax compliance. If you’re unsure about your business’s tax requirements, consult a tax advisor.

If your business operates a marketplace and wants to collect tax on sales facilitated through this marketplace, refer to details below to enable Stripe Tax for marketplaces.

## Enable Stripe Tax for marketplaces

Stripe Tax enables businesses to calculate, collect, and file indirect taxes in over 40 countries, across hundreds of product categories.

Use this guide if your platform is responsible for collecting, filing, and reporting taxes.

We use the platform’s head office location, preset tax code, and tax registrations to calculate taxes. However, we don’t use the connected account information for tax purposes.

- Configure your platform account for tax collection

[Configure your platform account for tax collection](#set-up)

- (Optional) Assign tax codes to product catalog

[Assign tax codes to product catalog](#assign-product-tax-codes)

- Integrate tax calculation and collection

[Integrate tax calculation and collection](#enable-tax-collection)

- Withhold the collected tax amount

[Withhold the collected tax amount](#tax-withholding)

- Access Stripe Tax reports

[Access Stripe Tax reports](#access-reports)

[Configure your platform account for tax collection](#set-up)

## Configure your platform account for tax collection

To collect taxes, you need the platform account’s tax settings and registrations.

[Assign tax codes to your product catalog](#assign-product-tax-codes)

## Assign tax codes to your product catalog

To calculate taxes, Stripe Tax requires that you classify products into tax codes. You can do so by supplying a preset tax code for the platform account, which might be sufficient if you typically sell a single category of items or services.

[a preset tax code](/tax/products-prices-tax-codes-tax-behavior#preset-tax-codes)

Additionally, you can map tax codes to each product to give you more control over tax categorization. You might have to map each product that a seller sets up on your marketplace. You can find a list of supported tax codes from available tax codes or retrieve it from the Stripe Tax Code API.

[map tax codes to each product](/tax/products-prices-tax-codes-tax-behavior#tax-code-on-product)

[available tax codes](/tax/tax-codes)

[Tax Code API](/api/tax_codes)

[Integrate tax calculation and collection](#enable-tax-collection)

## Integrate tax calculation and collection

You need to integrate with Stripe Tax to estimate taxes as part of your checkout flow.

After you implement it, Stripe automatically starts collecting tax in jurisdictions where you have an active registration.

Independent of the payment APIs, we credit the transaction amount to the connected account. You need to withhold the collected tax amount on the platform because the platform is liable for tax.

[liable for tax](/tax/connect)

[Withhold collected tax amount](#tax-withholding)

## Withhold collected tax amount

You must make sure that the tax collected is transferred to your marketplace account, so that you can then remit the tax to relevant jurisdictions.

[Access Stripe Tax Reports](#access-reports)

## Access Stripe Tax Reports

## See also

- Calculate tax in your custom checkout flow

[Calculate tax in your custom checkout flow](/tax/custom)
