htmlStripe Tax FAQ | Stripe Documentation[Skip to content](#main-content)FAQ[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Ffaq)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Ffaq)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)# Stripe Tax FAQ

Read the frequently asked questions about Stripe Tax.NoteFor additional help navigating indirect tax compliance, check out our Stripe Tax guides.

[Set up](#set-up)### What tax code should I choose?

Stripe has a proprietary tax code system that maps our tax codes to tax codes globally. Choose the category that best represents your business and products, and we’ll correctly determine the tax amounts and rules based on customer location. Consult with your tax advisor to determine the best tax codes for your business.

Learn more

### Do tax codes vary by country?

Tax codes, and tax code objects (for example, txcd_xxx) within Stripe are always the same across different jurisdictions. However, individual products might have tax treatments that differ by location, and Stripe maintains current rate and taxability information for you, while staying up to date with any changing regulations.

### What is the difference between inclusive and exclusive tax?

Inclusive tax means you include the tax in the final price, and is common for B2C purchases outside the US. Exclusive tax is when you add tax on top of the price you defined, and is common for B2B transactions or B2C transactions in the US.

[Calculating Tax](#calculating-tax)### Where does Stripe Tax support full “rooftop-accurate” address lookup?

Stripe Tax supports full rooftop-accurate address lookup for US customer addresses, with addresses matched to the USPS address database.

Rooftop-accurate address lookup means that you can attribute your customer’s location to a specific house or building. This provides greater accuracy in the US, where two houses located side-by-side on the same street might be subject to different tax rates, due to complex jurisdiction boundaries.

Outside the US, we use the country, state, and postal code fields as necessary but we don’t compare the addresses against an address database. See “Special jurisdictions and excluded territories” for more about when the state and postal code are used.

### Do you support PO Box addresses?

In general, PO Boxes aren’t part of our US address database. If we can’t find the address for a PO Box or other address in the address database, we approximate the location using the rest of the address details, such as the postal code (for example, ZIP5).

### What is ZIP5 and ZIP+4 (ZIP9)?

In the US, postal codes are called “ZIP codes." A ZIP5 is a 5-digit basic ZIP code (for example, 94103) which represents an area for mail delivery. A ZIP+4 or ZIP9 is a 9-digit extended ZIP code (for example, 94103-4918) which typically represents a smaller area or a single high-volume mail recipient (such as a company campus).

### How do I know which address was used as my Customer’s tax location?

When you enable automatic tax calculation on an invoice or Checkout session, the Dashboard shows an Automatic tax section. This section shows where your customer was located for tax purposes and which address we used as the source of this location. This is also returned in the Customer API if you expand the tax field.

### How do I check how precisely my customer’s location was determined?

When you enable automatic tax calculation on an invoice or Checkout session, the Dashboard shows an Automatic tax section. This section shows how precisely we determined your customer’s location. Customer API also provides relevant location resolution information if you expand the tax field.

The table below lists the supported precisions and whether tax can be calculated:

PrecisionTax calculatedDescriptionAddressEverywhereThe address placed the customer at a known postal address (such as a house or business in the USPS address database).StreetEverywhereThe address placed the customer on a known street but didn’t identify a specific postal address.Postal codeEverywhereThe address placed the customer within a postal code area (for example, a ZIP5 or ZIP+4), but didn’t identify a particular street or address.CityOutside the USThe address placed the customer within a particular city, but didn’t identify a postal code area (for example, a ZIP5) or street.StateOutside the USThe address had a valid ISO 3166-1 country code and ISO 3166-2 state code.CountryOutside the USThe address had a valid ISO 3166-1 country code.### How reliable and accurate is using an IP address to determine my customer’s location?

We can geolocate an IP address to a specific location in almost all cases. This doesn’t mean that it’s a good reflection of your customer’s actual location. We don’t recommend relying on your customer’s IP address in locations that impose local taxes (such as the US)—the IP address location might represent your customer’s ISP (internet service provider) location, which can be some distance away. In Europe and other regions where countries have a tax authority that imposes a single tax, the IP address is more likely to accurately reflect your customer’s location.

### When are tax calculations recorded in the Stripe Tax exports?

Stripe Tax calculates taxes and maintains a record of the total tax collected. You can access the record of total tax collected through Stripe Tax exports.

Stripe Tax exports include transactions committed with the Stripe Tax API and operations on Stripe objects with automatic_tax[enabled]=true.

Stripe Tax exports record the following operations, which increase the balance of total tax collected:

- Customer completes a payment in a Checkout Session. This also applies to Checkout Sessions created through[Payment Links](/api/payment_links/payment_links).
- Finalizing an Invoice. This applies to one-off Invoices and Subscription renewal Invoices.[Invoice finalization](/invoicing/integration/workflow-transitions)happens when the Invoice’s state transitions from`draft`to`open`state. This transition happensbeforethe Invoice is paid.
- Transitioning an Invoice’s state from`uncollectible`to`paid`through the[Pay Invoices API](/api/invoices/pay).
- [Voiding](/api/credit_notes/void)a Credit Note.
- [Creating](/api/tax/transactions/create_from_calculation)a tax transaction with the Stripe Tax API.

Stripe Tax exports record the following operations, which decrease the balance of total tax collected:

- [Voiding](/api/invoices/void)an Invoice.
- Marking an Invoice as[uncollectible](/api/invoices/mark_uncollectible).
- [Creating](/api/credit_notes/create)a Credit Note.
- A[Refund](/api/refunds)of a Charge associated with an Invoice or a Checkout Session.
- Creating a[reversal](/api/tax/transactions/create_reversal)(refund) tax transaction with the Stripe Tax API.

Stripe Tax doesn’t record the following operation in Tax exports:

- [Disputes](/disputes)that are upheld by the cardholder’s bank. Stripe Tax doesn’t decrease the balance of the collected total tax.
- Refunds of[uncaptured amounts](/api/payment_intents/capture#capture_payment_intent-amount_to_capture)of a payment. This can happen when performing a[partial capture](/api/payment_intents/capture#capture_payment_intent-amount_to_capture)for payments of Checkout sessions using[capture_method=manual](/api/checkout/sessions/create#create_checkout_session-payment_intent_data-capture_method). When the capture amount is lower than the original amount, Stripe Tax doesn’t reduce the total balance of the collected tax.

### If I create a draft invoice today, but it’s set to finalize in the future, and the tax rates change in between, which tax rate is used?

Stripe calculates the tax at the published rate on the date that an invoice is finalized. For example, if an invoice draft is initialized on December 20th and set to finalize on January 15th but a new tax rate is introduced on January 1st, the tax on the invoice will be calculated at the new rate.

- December 1st: Tax Rate: 6%
- December 20th: Invoice draft initialized set to finalize January 15th
- January 1st: Tax Rate 5%
- January 15th: Invoice finalized with a tax rate of 5%

### How do chargebacks work?

A chargeback doesn’t reduce the balance of total tax collected.

Stripe Tax calculates taxes and maintains a record of the total tax collected. You can access the record of total tax collected through Stripe Tax exports.

For example, for a transaction with an amount of 100 USD and exclusive tax of 10 USD, the total tax collected is 10 USD. In the event of a chargeback, we won’t reduce Stripe Tax reporting total tax collected from 10 USD to 0 USD.

### How do you handle credit notes?

A credit note reduces the balance of total tax collected.

Stripe Tax calculates taxes and maintains a record of the total tax collected. You can access the record of total tax collected through Stripe Tax exports.

For example, for an invoice with an amount of 100 USD and exclusive tax of 10 USD, the total tax collected is 10 USD. Issuing a credit note that fully refunds the invoice shows as a negative amount in your Stripe Tax reporting, reducing your liability from 10 USD to 0 USD.

### How is tax liability calculated when using credit notes?

Applying credit notes reduces the tax liability of a transaction proportionately across all the items in a basket.

For example, applying a credit note of 33 USD to an order of 2 items costing 66 USD and 33 USD with a 10% tax rate (total 108.90 USD) reduces tax liability by 2.20 USD and 1.10 USD respectively.

### How is tax liability determined in the case of partial refunds?

If an order’s total amount is > 0 after a refund, then the remaining amount will keep at least 0.01 USD in tax liability. This is because it uses a cumulative remainder approach to deal with rounding.

### How do you handle discounts?

We apply discounts before tax.

For example, for an exclusive price of 100 USD, a tax rate of 10%, and a discount of 10 USD, the resulting values are:

- Amount: 100 USD
- Discount: 10 USD
- Post discount amount:  90 USD
- Tax: 9 USD
- Total: 99 USD (90 USD + 9 USD)

For example, for a inclusive price of 100 USD, a tax rate of 10%, and a discount of 10 USD the resulting values are:

- Amount: 100 USD
- Discount: 10 USD
- Post discount amount: 90 USD
- Tax: 8.18 USD
- Total: 90 USD

### Do you mandate two pieces of non conflicting evidence for B2C transactions in Europe?

No, we don’t mandate two pieces of non conflicting evidence for business to consumer transactions in the EU. However, we do store and retain the evidence used on the Customer object that you can review before requesting additional information from a customer after the transaction.

### Are Apple Pay and Google Pay available to use with Stripe Tax?

Stripe Tax supports Apple Pay and Google Pay if your customer enters their shipping or billing address during the payment process.

If you enable Apple Pay or Google Pay on your account and enable Stripe Tax on your integration, Stripe:

- Automatically calculates the tax of the customer’s subtotal before they submit payment.
- Enables Apple Pay as a payment option if the user’s browser supports Apple Pay version 12 and above.
- Enables Google Pay as a payment option to customers only when the user collects the customer’s shipping address information.

### Where does Stripe get its tax rates from?

We have a team of tax researchers focused on monitoring tax laws and tax authority publications for changes. We make the updates directly to Stripe Tax when the change is effective.

### In which currency are tax calculations recorded?

Tax calculation amounts are recorded in the presentment currency, which can differ from both the settlement currency and the tax authority’s local filing currency.

You have the option to view amounts in both the presentment and filing currencies through Stripe Tax exports.

### When do conversions to other currencies occur?

Stripe converts tax amounts from the presentment currency to the tax authority’s local filing currency when we record the tax calculations.

[Reporting and filing](#reporting-and-filing)### Does Stripe Tax handle remitting and reporting tax, or filing tax returns?

Stripe Tax doesn’t handle remitting and reporting tax, or filing tax returns. Stripe Tax provides itemized and summarized exports to help users prepare, file, and remit the tax that was automatically calculated and collected. To automate filing in the US, we recommend using TaxJar’s AutoFile solution. In Europe, we recommend using Taxually or Marosa. To get started, visit Taxually’s partner page or Marosa’s partner page.

### How frequently do I need to file returns?

Each jurisdiction determines the required information and frequency for reporting and filing taxes. If you’re a business collecting taxes, you must report, file, and remit the taxes collected in every jurisdiction that you’re registered in. Make sure you understand the obligations of each jurisdiction and consult your tax advisor if you need help.

Learn more about reporting and filing.

### How can I complete my returns myself or with my accountant?

Stripe Tax provides itemized and summarized exports to help you complete your returns. Consult with your tax advisor if you need help understanding the filing or reporting requirements for the jurisdictions where you’re registered.

### How can I remit the funds I collected to each jurisdiction?

Each jurisdiction mandates its own method and timing of remittance (direct debits, bank transfers, and so on). Make sure you understand the rules for each jurisdiction and consult your tax advisor if you need help. For automating remittance in the US, we recommend using TaxJar’s AutoFile solution. In Europe, we recommend using Taxually or Marosa. To get started, visit Taxually’s partner page or Marosa’s partner page.

[Pricing](#pricing)Stripe Tax pricing is usage-based and determined by the number of transactions or the sales volume that you process through Stripe Tax for tax calculation and collection. The pricing varies based on the type of integration you use. No matter which integration you use, you only incur fees for transactions in jurisdictions where you have an active tax registration. To learn more, visit the support page on Stripe Tax pricing.

Custom pricing is available for companies with large payments volume, high transaction volume, or unique business models. Contact our sales team to learn more.

Pay a fixed amount per month for Stripe Tax?Interested in getting early access to subscription pricing? Instead of paying per transaction, you can pay a fixed amount for a set of transactions. Share your email address to learn more.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.### When do you charge a fee for Stripe Tax?

You’re only charged for using Stripe Tax on transactions or calculations to customers in states or countries where you’re registered to collect tax. If the registration options you have selected are either VAT OSS - European Union or Small Seller - European Union, you’re charged on all EU transactions.

As Stripe Tax is a tax calculation product, we charge a fee when Stripe Tax calculates the tax for a live-mode transaction. It is important to note that this fee is distinct from when a payments transaction is completed, as that fee relates to payments and not calculation. The Stripe Tax fee might apply in cases in which the applicable payment isn’t collected or processed, or if a credit card charge is disputed.

Below are the details of what qualifies as a transaction that triggers a fee for Stripe Tax.

No-code/low-code integrationsTax API integrationsConnectSituationStripe Tax fees chargedOrigin address and active tax registrations configured in[Stripe Tax Settings](https://dashboard.stripe.com/settings/tax).No fee charged on Checkout Sessions, Subscriptions, and Invoices without`automatic_tax`enabled.Subscription created with[automatic_tax enabled](/api/subscriptions/create#create_subscription-automatic_tax-enabled).Fee charged each time the subscription renews and the renewal invoice is finalized, if there’s an active tax registration covering the customer jurisdiction at the time.Checkout Session created with[automatic_tax enabled](/api/checkout/sessions/create#create_checkout_session-automatic_tax-enabled), in subscription[mode](/api/checkout/sessions/create#create_checkout_session-mode).Fee charged each time the subscription renews and the renewal invoice is finalized, if there’s an active tax registration covering the customer jurisdiction at the time.Checkout Session created with[automatic_tax enabled](/api/checkout/sessions/create#create_checkout_session-automatic_tax-enabled), in payment[mode](/api/checkout/sessions/create#create_checkout_session-mode).Fee charged when the Checkout Session is completed, if there’s an active tax registration covering the customer jurisdiction at the time.One-off invoice created with[automatic_tax enabled](/api/invoices/create#create_invoice-automatic_tax), and[finalized](/api/invoices/finalize)even if not paid by the customer.Fee charged when the invoice is finalized, if there’s an active tax registration covering the customer jurisdiction at the time.A payment is refunded, a credit note is issued, an invoice is voided, or a chargeback is received.Fee is charged for the initial transaction. No additional fee is charged for refund, credit note, voided invoice, or chargeback.Payment Link Session created with[automatic_tax enabled](/api/payment_links/payment_links/create#create_payment_link-automatic_tax), in payment mode.Fee is charged when the Payment Link Session is completed, if there’s an active tax registration covering the customer jurisdiction at the time.### Do you charge a fee when the tax collected is zero?

Yes, we charge the Stripe Tax fee even if the tax amount calculated is zero, for example, if:

- You have an active registration covering the customer jurisdiction
- The products sold are exempt (from sales tax) or out of scope (of VAT)
- The customer is tax exempt or a reverse charge applies
- The country or state has no sales tax (for example, Montana in the US)

The Stripe Tax fee is only charged on that volume where you have an active registration configured in live mode.

### Do you calculate taxes on transactions in markets where I’m not registered?

No, we don’t charge a fee on transactions in markets where you’re not registered. For markets where you’re not registered to collect tax, the resulting tax amount is zero.

### Do you charge a fee for functionality other than calculating tax?

We don’t charge a fee to:

- Configure your Stripe Tax settings, such as your origin address, preset tax code, or tax registrations
- Calculate tax on transactions that aren’t completed, such as abandoned Checkout Sessions or draft invoices that are never finalized
- Calculate tax on credit notes
- Monitor tax thresholds based on your past Stripe payments

To turn off Stripe Tax calculation (and thus any fees associated), make sure your integration has automatic_tax[enabled]=false.

### Do you charge a Stripe Tax fee for credit notes?

We don’t charge a fee to calculate the tax to refund on credit notes.

### Do you refund the Stripe Tax fee when a payment is refunded or an invoice is voided?

No, we don’t refund the Stripe Tax fee in these situations.

### Do you charge the Stripe Tax fee on the entire payments volume or only on the payments volume in markets where I’m registered to collect taxes?

We charge a fee only on transaction volume in locations where you’re registered to collect taxes. That means you incur a fee if we calculate tax to be 0 in a location where you have an active tax registration. We don’t charge you for volume where you’ve no active registration.

We assess the fee based on the transaction volume including the calculated tax. Therefore, the transaction volume includes the calculated exclusive tax.

### Do you charge a fee when there is a 100% off discount or coupon?

For low-code or no-code integrations, such as Stripe Tax on Billing, Invoices, Subscriptions, Payment Links, and Checkout, we charge a fee based on volume. We don’t charge a fee if the transaction’s volume is zero.

For the Stripe Tax API, the fee applies to calls to the API, so that does include a charge even if the transaction volume is zero.

### Do you charge a fee for Subscription trials?

Creating a Subscription with a trial period creates an immediate zero-amount Invoice. We don’t charge a fee for these Invoices because the Invoice’s amount is zero.

When the Subscription trial ends, it starts a new billing cycle for the Customer and generates a new Invoice. After this Invoice finalizes, we charge a fee if the Invoice’s amount is greater than zero.

Invoice finalization happens when the Invoice’s state transitions from draft to open. This transition happens before the Invoice is paid.

### Where can I see my Stripe Tax fees?

You can find Stripe fees under Reports > Stripe fees.

If you have a low code or no code integration, you can find your Stripe Tax fees under Product usage fees as Automatic Taxes - Automatic tax.

If you have an API integration, you can find your Stripe Tax fees under Other fees as either Tax Api Calculation or Tax Api Transaction, depending on your usage.

[Integrations](#integrations)### How to turn off Stripe Tax

You can stop using Stripe Tax for tax calculations by turning off automatic tax calculation in Tax Settings and setting automatic_tax[enabled]=false for API transactions.

### How to stop calculating taxes automatically on a subscription

You can use the Dashboard UI to remove the automatic calculation of taxes on a subscription. Alternatively, you can update the subscription with the API to have automatic_tax[enabled]=false.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up](#set-up)[Calculating Tax](#calculating-tax)[Reporting and filing](#reporting-and-filing)[Pricing](#pricing)[Integrations](#integrations)Products Used[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`