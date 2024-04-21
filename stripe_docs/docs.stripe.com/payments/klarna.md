# Klarna payments

Klarna is a global payment method that gives customers a range of payment options during checkout. These payment options make it convenient for customers to purchase items in all price ranges.

To pay with Klarna, customers are redirected to Klarna’s site, where they select their preferred payment option, then return to your website to complete the order. Klarna presents payment options based on the customer’s billing address and transaction amount. After payment acceptance, the full amount of the order (minus fees) is made available to your Stripe account up front, and Klarna collects the purchase amount from your customer, including any future installment payments, if applicable.

This demo shows the customer experience when using Klarna.

The following tabs capture Klarna’s properties and country availability:

- Supported customer countriesAustralia, Austria, Belgium, Canada, Czechia, Denmark, Finland, France, Greece, Germany, Ireland, Italy, Netherlands, New Zealand, Norway, Poland, Portugal, Spain, Sweden, Switzerland, United Kingdom, and the United States

Supported customer countries

Australia, Austria, Belgium, Canada, Czechia, Denmark, Finland, France, Greece, Germany, Ireland, Italy, Netherlands, New Zealand, Norway, Poland, Portugal, Spain, Sweden, Switzerland, United Kingdom, and the United States

- Presentment currencyAUD, CAD, CHF, CZK, DKK, EUR, GBP, NOK, NZD, PLN, SEK, or USD

Presentment currency

AUD, CAD, CHF, CZK, DKK, EUR, GBP, NOK, NZD, PLN, SEK, or USD

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyBuy Now, Pay Later

Payment method family

Buy Now, Pay Later

- Recurring paymentsNo

Recurring payments

No

- Payout timingStandard payout timing applies

Payout timing

Standard payout timing applies

- Connect supportYes

Connect support

Yes

- Refunds / Partial refundsYes / Yes

Refunds / Partial refunds

Yes / Yes

- Dispute supportYes

Dispute support

Yes

If you’re based in the EEA, UK, or Switzerland, then you can transact with consumers across the EEA, UK, and Switzerland, provided the presentment currency matches the currency of the customer’s country. For example, a Swedish business can present in EUR to accept Klarna from a buyer in Germany.

If you’re based outside of the EEA, UK, or Switzerland, then you can only transact with customers within your country, and the presentment currency must be the currency of your country. For example, an Australian business must present in AUD, and can only transact with buyers in Australia.

Cross-border payments for Klarna beyond the restrictions described above are currently limited to beta users. Sign up for the beta.

[Sign up for the beta.](#)

## Get started

You don’t actually have to integrate Klarna and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

You can also manually list Klarna as a payment method and use it with Payment Links or the Payment Method Messaging Element.

[manually list](/payments/klarna/accept-a-payment)

[Payment Links](/payment-links)

[Payment Method Messaging Element](/payments/payment-method-messaging)

To create recurring or off-session payments with Klarna, sign up for the beta.

[sign up for the beta.](#)

## Payment options

Depending on the customer’s billing country and the transaction amount, Klarna can present customers with various payment options. Regardless of the underlying payment option selected, Stripe makes the full amount of the funds (minus fees) available to you upfront and Klarna collects the purchase amount from your customer, who repays Klarna directly. These options include:

- Pay in 3 or 4 (also known as Installments): Customers pay for the purchase in three or four interest-free payments. The total transaction amount is typically spread equally across the installments, but Klarna might occasionally charge your customer more in the first installment based on the customer’s purchase power and other credit factors.

- Monthly installments (also known as Financing): Customers pay for the purchase over a longer term of up to 36 months, which might include interest.

- Pay later: Customers pay for the purchase in a single payment in 30 days.

- Pay now: Customers pay for the purchase immediately using a linked card, bank debit, or bank transfer.

1 See the Klarna FAQ for more information about Klarna Financing availability in the United Kingdom.

[Klarna FAQ](https://support.stripe.com/questions/klarna-faq#klarna-financing-us-uk-payers)

2 Puerto Rico is the only US territory supported by Klarna.

3 Supported in all states except New Mexico (NM) and Hawaii (HI).

4 Supported in all states except Montana (MT), New Mexico (NM) and Hawaii (HI). Accessible by request only, Contact us for access..

[Contact us for access.](#)

5 Supported in all states except Iowa (IA), West Virginia (WV) and Massachusetts (MA).

## Prohibited business categories

In addition to the industry and business categories listed in Prohibited and restricted business, the following categories aren’t allowed to use Klarna:

[Prohibited and restricted business](https://stripe.com/restricted-businesses)

- Charities

- Political organizations, parties, or initiatives

- B2B

For more information about Klarna eligibility for your account, navigate to your Payment methods settings.

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

## Klarna branding

Let your customers know you accept payments with Klarna by including the Payment Method Messaging Element on your product and cart pages. You must comply with Klarna’s marketing compliance guides.

[Payment Method Messaging Element](/payments/payment-method-messaging)

[marketing compliance guides](https://docs.klarna.com/marketing/solutions/grab-and-go)

If you’re in the UK, there are FCA regulatory requirements in the UK regarding advertising Klarna’s BNPL payment methods. Failure to comply can result in criminal charges. Per these requirements, you must only advertise Klarna with messaging approved by Klarna. You can find Klarna approved messaging in Klarna’s UK Financial Promotion Rules.

[FCA](https://www.fca.org.uk/)

[UK Financial Promotion Rules](https://docs.klarna.com/marketing/solutions/grab-and-go/gb/Klarna-Financial-Promotion-Rules/)

## Disputed payments

Klarna covers disputes driven by customer fraud or inability to repay installments provided you follow Klarna’s shipping policy. Merchants aren’t involved in these disputes.

[Klarna’s shipping policy](https://www.klarna.com/international/shipping-policies/)

Customers can open a dispute within 180 days of the original transaction. Communicate directly with your customer to try and solve the issue together. If you can’t reach a solution, Klarna intervenes to help solve the dispute. You can manage disputes in the Stripe Dashboard and with APIs.

Prior to November 15, 2023, you could only manage Klarna disputes through emails. Now, all new Klarna disputes are managed in the Stripe Dashboard and with APIs. As you transition from managing disputes through email to handling them in the Dashboard or with the API, you must continue to respond to existing email disputes by email.

To learn how to use the Dashboard or API to manage disputes, see Respond to disputes.

[Respond to disputes](/payments/klarna/disputes)

Klarna reaches out to both you and the customer, requesting convincing evidence that you fulfilled the purchase order. Klarna emails the support email address that you list in your Dashboard settings when you activate Klarna. If you haven’t provided a support email address, Klarna defaults to your primary Stripe account email address. Contact us to modify the email address Klarna uses.

[Dashboard settings](https://dashboard.stripe.com/settings/public)

[Contact us](https://support.stripe.com/contact)

Klarna might request evidence such as:

- Received return confirmation (for shipped goods returned from the customer to you).

- Tracking ID.

- Shipping date.

- Record of purchase for intangible goods, such as IP address or email receipt.

- Record of purchase for services or physical goods, such as phone number or proof of receipt.

This information helps Klarna determine if a dispute is valid or if they’ll reject it. Make sure the evidence you provide contains as much detail as possible from what the customer provided at checkout. You must submit the requested information within 7 days. If Klarna rules in favor of the customer, they might initiate a dispute, with funds withdrawn from your Stripe account. Klarna dispute decisions are final, and they have no appeal process.

## Refunds

You can refund Klarna charges up to 180 days after the payment completes. Klarna cancels any remaining payments on a refunded charge and returns the already-paid amount to the customer. Refunds usually take 5-7 business days to complete, but may take longer depending on the customer’s financial institution and the type of purchase. Klarna supports full and partial refunds. You can also issue multiple partial refunds up to the amount of the original charge. Partial refunds update the Klarna order to reflect the new total amount.

- If the partial refund is greater than the remaining balance of the order, Klarna deducts the refund amount from the outstanding balance and returns the difference.

- If the partial refund is less than the remaining balance of the order, Klarna deducts the amount from the outstanding balance and spreads refunds evenly across the remaining payments.

## Klarna with Connect

You can use Stripe Connect with Klarna to process payments on behalf of a connected account. Connect users can use Klarna with the following charge types:

[Stripe Connect](/connect/overview)

- Direct

[Direct](/connect/direct-charges)

- Destination

[Destination](/connect/destination-charges)

- Separate Charges and Transfers

[Separate Charges and Transfers](/connect/separate-charges-and-transfers)

Connected accounts that use the Stripe Dashboard can enable Klarna through their Dashboard. To check which accounts have enabled Klarna, use the capabilities hash in our accounts webhooks or APIs to see if the klarna_payments capability is set to active.

[accounts webhooks or APIs](/api/accounts/object#account_object-capabilities-klarna_payments)

Request the klarna_payments capability on any connected account you want to enable Klarna for. See this guide to learn more about requesting capabilities for your connected accounts. The name of your connected account is the name customers see during checkout and in the Klarna app.

[this guide](/connect/account-capabilities)

## Termination rights

In addition to the termination and suspension rights included in the Stripe Services Agreement, Klarna has certain additional rights to suspend or terminate your use of Klarna, such as for breach of the prohibited business categories listed above or for high dispute rates that aren’t promptly remedied.

[Stripe Services Agreement](https://stripe.com/klarna/legal)

## Additional requirements

You acknowledge that:

- Klarna decides if customers can use Klarna for purchases and has the sole right to receive payment from Klarna customers. Stripe acquires those purchases for you and settles the funds to you.

- You must provide customers with any required or requested payment instructions or documents (such as VAT). These documents must refer to Klarna as the payee and not contain any of your bank details.

- You can’t impose fees or higher prices for Klarna purchases or act unfairly towards Klarna.

- You must promptly follow Stripe’s instructions to stop an order process or shipping to help reduce the risk of fraudulent transactions.

- You can’t use any design that’s confusingly similar to Klarna’s trademarks (see Klarna’s branding guidelines).

[Klarna’s branding guidelines](https://docs.klarna.com/marketing/)

- You must not permit use of Klarna for purchases by a person who might reasonably be considered to share a financial interest with you, including owners, directors, and employees of your business or any affiliated company.

If you’re in Australia, Klarna provides guidance on how to comply with the Design and Distribution Obligations (DDO) when accepting Klarna in Australia. Most Stripe users don’t need to do anything to comply. If you actively promote or recommend Klarna’s Pay in 4 product in Australia, you may be considered a “distributor” under the DDO and may have to:

[Design and Distribution Obligations (DDO)](https://docs.klarna.com/marketing/au/advertising-legal-guidelines/design-and-distribution-obligations-ddo/)

- Help Klarna as needed to comply with the DDO, including only promoting Pay in 4 consistent with Klarna’s Target Market Determination (TMD)

[Target Market Determination (TMD)](https://www.klarna.com/au/legal/target-market-determinations/)

- Promptly advise Klarna of any “significant adverse dealing” such as:a major complaint or large number of complaints that Pay in 4 causes a customer harm ora customer under 18 makes a purchase using Pay in 4

- a major complaint or large number of complaints that Pay in 4 causes a customer harm or

- a customer under 18 makes a purchase using Pay in 4

- If requested, provide Klarna with reports about any Pay in 4 complaints you receive

- Keep and, if requested, provide Klarna information relating to any reported significant adverse dealings
