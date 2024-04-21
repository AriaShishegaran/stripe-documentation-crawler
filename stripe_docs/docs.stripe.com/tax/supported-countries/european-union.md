# Collect tax in the European Union

Businesses selling goods and services to customers in the European Union (EU) may need to collect value added tax (VAT). That’s the case even if your business isn’t established (based) in the EU. Although the VAT laws are generally similar across the EU, the tax rates and rules may vary per country.

[OptionalCountries in the EU](#eu-countries)

## OptionalCountries in the EU

## When and how to register

Different rules determine when and how you need to register for VAT, depending on the country your business is located in. After you’ve registered with a country, add your registration to Stripe in the Registrations tab in the Dashboard to start collecting tax on your transactions. Learn more about the different registration schemes in our guide.

[Registrations tab](https://dashboard.stripe.com/tax/registrations)

[in our guide](https://stripe.com/guides/introduction-to-eu-vat-and-vat-oss)

Use the Thresholds tab to get insights about your potential tax registration obligations in each country in the European Union. Stripe also notifies you with email and Dashboard alerts when you need to register to collect tax. Learn more about how the monitoring tool works.

[Thresholds tab](https://dashboard.stripe.com/tax/thresholds)

[monitoring tool works](/tax/monitoring)

[Businesses based in the EU](#eu-businesses)

## Businesses based in the EU

EU countries have different rules and thresholds for when a business established in that country needs to register for VAT and collect tax. You can learn more about how to register on the tax administration websites of each country. Stripe only monitors if you have reached a tax threshold for sales outside of the EU country your business is based in.

If you sell to customers in another EU country you may need to register to collect VAT in that country too, even if your sales volume is small. You can add your domestic registration to Stripe in the Registrations tab in the Dashboard to start collecting tax.

[Registrations tab](https://dashboard.stripe.com/tax/registrations)

You don’t need to register in other EU countries if:

- your total sales are under 10,000 EUR in a calendar year and

- you sell digital products or physical goods and

- your sales are to individuals and not businesses in another EU country

The VAT rate of the EU country your business is based in applies instead. Stripe refers to this simplification rule as the small seller option. We determine whether you’re selling digital products or physical goods using the product tax code you assigned to your product.

[product tax code](/tax/tax-codes)

When you select the ‘domestic registration’ option, you’re asked to indicate if your business is a small seller with sales below the 10,000 EUR threshold. You only see this option for the country that you have set as your origin address. If you choose yes, we monitor your cross-border transactions in the EU and notify you when you exceed that threshold.

[origin address](/tax/set-up#origin-address)

After you exceed the small seller threshold, you’re required to collect tax in the country your customers are located in. You can do so in two ways:

- Register domestically in the EU countries your customers are located in

- Register for the Union One Stop Shop (OSS) scheme in your home EU country.

[Union One Stop Shop (OSS) scheme](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en)

There are three steps to reflect this change in Stripe:

- End your domestic small seller registration in Stripe on the Registrations tab.

[Registrations tab](https://dashboard.stripe.com/tax/registrations)

- Add a new domestic registration for the location your busienss is based and select no when you’re asked if you are a small seller.

- Add any other new domestic or One Stop Shop registrations to start collecting tax in those locations.

If you sell goods or services to individuals (and not to businesses), you can register for the Union One Stop Shop (OSS) scheme in the EU country your business is based in. You won’t have to register with each EU country you sell goods or services to. Instead you’ll be able to register for OSS through your home country VAT website and submit one return for your sales across the EU. You’ll remit all VAT to your local tax authority who will distribute it to the countries where your customers are located.

Learn more about One-Stop Shop. Select the country your business is based in from the table if you need help finding the right links.

[One-Stop Shop](https://stripe.com/guides/introduction-to-eu-vat-and-vat-oss)

[from the table](/tax/supported-countries/european-union#eu-countries)

[Businesses based outside the EU](#outside-eu-businesses)

## Businesses based outside the EU

If your business is based outside the EU, you may need to register to collect VAT from your first sale in an EU country. There are different VAT registration options for businesses based outside the EU.

You can register to collect VAT in each EU country your customers are based in. You may be required to appoint a tax representative, depending on the country you and your customer are located in.

Select the country your customer is based in from the list in the sidebar if you need help finding the right links.

This scheme is for businesses based outside the EU selling services to individuals in the EU. You can choose which EU country you register in. Once you’re registered, you can collect VAT on your sales to customers across the EU without having to register in every country. You’ll also only submit one return for all your EU sales to the country you registered in. You do not need to appoint a tax representative to use the OSS non-Union scheme.

If you sell physical goods to individuals in the EU and the goods are imported in packages (consignments) that are valued at or under 150 EUR,  you can register in the EU country of your choice for Import One Stop Shop. This means your customer will be charged VAT when they buy them. They won’t be charged when the goods arrive at the border in the EU. Once you’re registered, you can collect VAT on your sales of these goods to customers across the EU without having to register in every country. You’ll also only submit one return for all your EU sales to the country you registered in. Businesses based outside the EU normally need to appoint a local intermediary to register for IOSS. Stripe assumes that goods purchased together are shipped together. If a transaction is over 150 EUR, IOSS won’t apply. That means your customers may have to pay taxes and customs duties when the goods arrive at the border in the EU.

## How we calculate taxes

Stripe calculates VAT on a transaction using the following pieces of information:

- the location of your business

- the tax registrations you’ve added to Stripe

- the location of the customer

- the type of the product sold (based on which product tax code you assigned to your product)

[product tax code](/tax/tax-codes)

- the status of the customer (whether or not they’re a VAT-registered business).

[Sales of services](#services)

## Sales of services

When your business is located in the same country as your customer, Stripe calculates VAT by applying that country’s tax rates.

When you and your customer are in different countries (cross-border sales), there are more complicated rules that apply. These rules determine where the services are considered to be delivered and which country is entitled to collect the tax. Here’s a summary of how Stripe applies tax on sales of services:

- Digital goods or electronically supplied services: Generally taxable in the customer’s country. If you’ve indicated your business is a small seller the VAT of the country your business is based in applies.

Digital goods or electronically supplied services: Generally taxable in the customer’s country. If you’ve indicated your business is a small seller the VAT of the country your business is based in applies.

[small seller](/tax/supported-countries/european-union#eu-businesses-domestic-registration-small-sellers)

- Services related to immovable property: Taxable in the country where the property is located. Stripe assumes that the property is located in the customer’s country.

Services related to immovable property: Taxable in the country where the property is located. Stripe assumes that the property is located in the customer’s country.

- Services involving work on movable property: Taxable in the customer’s country as Stripe assumes that the work is performed in the customer’s country.

Services involving work on movable property: Taxable in the customer’s country as Stripe assumes that the work is performed in the customer’s country.

- Services that can be delivered remotely: Taxable in the customer’s country when they’re provided to individuals outside the European Union or other businesses. When they’re provided to individuals in other EU countries, they’re taxable in the seller’s country.

Services that can be delivered remotely: Taxable in the customer’s country when they’re provided to individuals outside the European Union or other businesses. When they’re provided to individuals in other EU countries, they’re taxable in the seller’s country.

- Other services: Taxable in the country your business is based in when provided to individuals. Taxable in the customer’s country when provided to other businesses.

Other services: Taxable in the country your business is based in when provided to individuals. Taxable in the customer’s country when provided to other businesses.

In some cases, when you sell services to a VAT-registered business in another EU country, the customer is responsible for calculating and remitting the VAT. Those transactions are called reverse charges. Your business must provide an invoice that specifies the reverse charge instead of including a tax amount. If your customer is eligible for reverse charges and provides their VAT ID in Stripe, we treat their transactions as reverse charges and don’t calculate tax for them. You can also mark a customer as eligible for reverse charges in the Dashboard or using the API, even if you haven’t collected a tax ID for that customer. For information about which tax IDs Stripe validates, see customer tax IDs.

[reverse charges](/tax/zero-tax#reverse-charges)

[mark a customer as eligible for reverse charges](/tax/zero-tax#reverse-charges)

[customer tax IDs](/invoicing/customer/tax-ids)

Stripe doesn’t support the following types of reverse charges:

- Domestic reverse charge: In some EU countries, a reverse charge can apply to the sale of some goods and services between businesses in that country. Stripe supports reverse charges only for cross-border sales, not for sales within the same country.

- Cross-border conditions: Some EU countries have conditions on which types of services are eligible for reverse charges. For example, a country can require you to have a domestic registration. Stripe assumes that all services sold to customers with a business tax ID are eligible for a reverse charge.

[Sales of physical goods](#physical-goods)

## Sales of physical goods

When your business is located in the same country as your customer and the goods are shipped within that country, Stripe calculates tax by applying that country’s tax rates.

When the goods are shipped to a customer in a different EU country to your business, Stripe calculates the tax based on the type of customer. Different rules apply depending on if your customer is an individual or a VAT registered business.

- Sales to an individual: if the sales are to an individual and your business arranges the delivery (transport) then the goods are taxed using the rules of the country your customer is based in. The exception is if you’re an EU based business and have indicated your business is a small seller in Stripe. The tax of the country your business is based in will apply instead.

[small seller](/tax/supported-countries/european-union#eu-businesses-domestic-registration-small-sellers)

- Sales to a VAT registered business: the sales are taxable in the country your business is based in. Stripe applies the zero rate if the customer provides their VAT ID number.

When the goods are shipped to a customer outside of the EU, Stripe Tax will treat this sale as an export and apply the zero rate. The transaction might still be subject to taxes and customs duties in the country your customer is in. Stripe doesn’t calculate these.

[apply the zero rate](/tax/zero-tax)

## Report and file your taxes

Stripe provides reports of your completed tax transactions in the EU. To access these reports, navigate to the Registrations tab. Learn more about the different types of reports.

[Registrations tab](https://dashboard.stripe.com/tax/registrations)

[the different types of reports](/tax/reports)

The way you file tax returns and pay (remit) your taxes will depend on which types of registrations you have.

- Domestic registration: you’ll file your tax returns in each country you have a registration. Some EU countries may require you to appoint a local tax representative to do this if you are not based in the EU.

- One Stop Shop: you’ll file your tax returns for all your eligible sales across the EU with the country you have a One Stop Shop registration in. If you use different OSS schemes, you need to submit a separate return for each scheme. Learn more about One-Stop Shop.

[One-Stop Shop](https://stripe.com/guides/introduction-to-eu-vat-and-vat-oss#4-file-vat-returns)

Select the country you need to file in from the list in the sidebar if you need help finding the right links. You are responsible for filing and remitting your taxes in the EU. Stripe doesn’t file taxes on your behalf. If you need help, we recommend using our partners our partners Taxually or Marosa who can help manage your filing and remittance.

[Taxually](https://stripe.taxually.com/)

[Marosa](https://marosavat.com/stripe-and-marosa/)
