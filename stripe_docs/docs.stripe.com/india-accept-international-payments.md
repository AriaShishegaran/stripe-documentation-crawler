# Accept International Payments from IndiaBeta

You can increase your success rates by presenting your international payments in your customer’s local currency. We support 135+ currencies on Visa and Mastercard, as well as USD on American Express. In order to do so, these transactions will have to be declared as “exports”.

When your customer is based outside India, it’s a good idea to localize your presentment currency to match that of the customer’s card (for example, USD, EUR, JPY, and so on). This ensures a higher likelihood of a successful charge by the customer’s card issuing bank, as opposed to presenting in INR, which in some cases may be declined with a generic decline code, due to a mistaken perception of a fraudulent charge.

[presentment currency](/currencies#presentment-currencies)

Stripe supports presentment in 135+ currencies. In order to present in a non-INR currency, you’ll need to provide additional information in onboarding and in API requests, since these transactions are considered exports from India.

See our India FAQ for more information.

[India FAQ](https://support.stripe.com/questions/india-faq)

## Requirements

Stripe supports both INR and non-INR presentment for customers located outside India, provided:

- The Stripe account must be a registered Indian business (sole proprietorship, limited liability partnership, or company.

- The Stripe business can’t be an individual.

- If you sell physical goods, you must provide a valid Importer Exporter Code (IEC).

- If you sell services, providing an IEC is optional, unless:you accept AMEX payments from international customersyou take any benefits under India’s Foreign Trade Policy

- you accept AMEX payments from international customers

- you take any benefits under India’s Foreign Trade Policy

- The transaction is a maximum of 30,000 USD. This is the regulatory limit.

## Onboarding

To enable export transactions, you must do the following when submitting your account application:

- Opt in to exports: In the account application, check the applicable box under the ‘I am exporting products to customers located outside India’ section. If you don’t opt in, you’ll only be able to make export charges in test mode. This option is only available for users with legal entity sole proprietorship, company, and LLC. (individuals are excluded)

Opt in to exports: In the account application, check the applicable box under the ‘I am exporting products to customers located outside India’ section. If you don’t opt in, you’ll only be able to make export charges in test mode. This option is only available for users with legal entity sole proprietorship, company, and LLC. (individuals are excluded)

[(individuals are excluded)](https://support.stripe.com/questions/how-can-i-open-a-stripe-account-in-india)

- Submit your importer/exporter code (IEC) The IEC is a code issued by the Indian Director General of Foreign Trade (DGFT) to Indian companies that intend to export from India. You can apply for an IEC at the DGFT website. An IEC is required under certain conditions.If you plan to accept Visa or Mastercard, an IEC is required only if you sell physical goods.If you plan to accept AMEX international payments for all export transactions, including selling physical goods and services. This is described by India’s Foreign Trade Policy

Submit your importer/exporter code (IEC) The IEC is a code issued by the Indian Director General of Foreign Trade (DGFT) to Indian companies that intend to export from India. You can apply for an IEC at the DGFT website. An IEC is required under certain conditions.

[DGFT website](https://dgft.gov.in/CP/)

- If you plan to accept Visa or Mastercard, an IEC is required only if you sell physical goods.

- If you plan to accept AMEX international payments for all export transactions, including selling physical goods and services. This is described by India’s Foreign Trade Policy

[AMEX international payments](https://support.stripe.com/questions/american-express-card-support-for-india-based-businesses)

- Specify a transaction purpose code. The transaction purpose code describes the nature of a payment received in foreign currency. The list of valid transaction purpose codes is maintained by the Reserve Bank of India (RBI). You must select the code which is closest to your product from the drop-down on the account application.

Specify a transaction purpose code. The transaction purpose code describes the nature of a payment received in foreign currency. The list of valid transaction purpose codes is maintained by the Reserve Bank of India (RBI). You must select the code which is closest to your product from the drop-down on the account application.

The list of transaction purpose codes supported by Stripe is copied below.

[copied below](#TransactionPurposeCode)

You can opt into the ability to enable exports, change your IEC (if applicable), or change your transaction purpose code at any time through the Dashboard. Also, if needed, you may use the same IEC if you have multiple export businesses, as long as the IEC is in the name of a common beneficial owner of both businesses.

[Dashboard](https://dashboard.stripe.com/settings/update)

A Stripe account can only have a single transaction purpose code.

You must send Stripe these additional fields for every international payment presented to a customer holding a non-India issued card. Regulatory reporting requires this.

- The buyer’s name

- Their billing address with a valid 2-alphabet ISO-3166 country code

[2-alphabet ISO-3166 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

- The charge description

- If you sell physical goods (not services), a shipping address is also mandatory, with a valid 2-alphabet ISO-3166 code

[2-alphabet ISO-3166 code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

Please see the code samples below to understand in which fields these items must be sent to Stripe.

Funds collected from both domestic and international payments are paid out to you in INR separately by Stripe.

If you process both domestic and international payments, you may have two payouts on the same day, with an International label for the relevant payouts in your dashboard.

[payouts in your dashboard](https://dashboard.stripe.com/test/payouts)

## International payments for services

Every international payment for services is required to have the buyer’s name, billing address and a description of the service being exported.

This information is required by our financial partners.

If the buyer’s name, billing address or description isn’t provided, the payment will fail.

Pass the description of service in the Payment Intents API as shown below

Pass the customer name and billing address in Customer Creation API as shown below

[Customer](/api/customers)

That’s it! This payment has been declared as an export transaction.

## International payments for goods

Every international payment for goods is required to have the buyer’s name, billing address, description and shipping address. This information is required by our financial partners.

This information is required by our financial partners.

If the buyer’s name,  billing address, shipping address or description isn’t provided, the payment will fail.

Pass the description of the item and a shipping address in the Payment Intents API as shown below

Pass the customer name and billing address in Customer Creation API as shown below

That’s it! This payment has been declared as an export transaction.

## Fighting fraud

International card payments require 2-factor authentication via 3D Secure (3DS).

Learn more about the requirement for 3D Secure.

[3D Secure](https://support.stripe.com/questions/3d-secure-authentication-for-international-card-payments-to-indian-businesses)

## Accepting recurring international payments (Stripe Billing)

You can use Stripe Billing to bill your international customers via Subscriptions and Invoices.

[Billing](/billing)

[Subscriptions](/billing/subscriptions/creating)

[Invoices](/api/invoices)

For recurring international payments related to services, the only change you need is to provide a buyer’s name and an address.

You don’t have to provide a description, because Stripe will generate one from the description on your invoice items. Therefore, you should ensure that the description on your invoice items accurately reflects your product:

For recurring international payments related to physical goods, please also provide a shipping address in the Customer Creation API.

When selling to international customers, 3D Secure isn’t mandatory. You may notice a higher dispute rate than when you were selling to Indian customers.

We often see disputes from customers claiming that they were charged even after they canceled their subscription. Here are some best practices to avoid these disputes:

- Make it clear on your signup page that your customers are agreeing to a recurring payment and include information about whether or not you plan to notify the customer before each payment. Make sure cancellation procedures are clearly communicated to your customers, and clearly state the window in which a subscription can be canceled. Include copies of these procedures in a visible terms of service page.

- If offering a free or discounted trial period, be sure to clearly communicate the length of the trial and the date full price billing will occur. You should also clearly display the amount of the standard pricing above the payment button on your checkout page.

- Cancel subscriptions within two business days of initial request, making sure to pass the cancellation along to Stripe if you use our subscription functionality. Per card network rules, you may also only make eight attempts per card after an initial decline, so be sure to close out any subscriptions that have already reached this limit. Provide your customer with a confirmation of the cancellation.

- Have a clear way for customers to contact you if requesting cancellation. If customers have questions about their subscription, they’re more likely to submit a dispute if you’re difficult to reach. You can track your overall dispute activity under the Analytics section in your Dashboard.

Learn more about dispute prevention and common reasons why cardholders file disputes.

[disputes](/disputes)

## Monthly payment advice for export transactions

Standard Chartered Bank (SCB) will issue payment advice directly to your registered Stripe email address the same day your export payout is being processed. This will include a list of export charges that are part of the specific export payout.

## Transaction Purpose Code Listing

Below is a list of the supported Transaction Purpose Codes that you can currently select in onboarding. We can’t support other Transaction Purpose Codes due to the requirements from our financial partner.
