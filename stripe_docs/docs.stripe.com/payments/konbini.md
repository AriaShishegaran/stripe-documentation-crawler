# Konbini payments

Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash.

To complete a transaction, customers receive payment codes for specific convenience stores along with a confirmation number. Customers then bring the information to a convenience store to make a cash payment. You will receive payment confirmation instantly, while funds will be available for payout after 4 business days.

[payout](/payouts)

Customers can pay at FamilyMart, Lawson, Ministop and Seicomart stores across Japan.

- Customer locationsJapan

Customer locations

Japan

- Payment method familyCash-based payment method

Payment method family

Cash-based payment method

- Connect supportPartial: request an invite to create charges on behalf of other accounts

Connect support

Partial: request an invite to create charges on behalf of other accounts

[request an invite](https://support.stripe.com/contact/email?topic=payment_apis)

[on behalf of](/connect/charges#on_behalf_of)

- Billing supportYes

Billing support

Yes

- Presentment currencyJPY

Presentment currency

JPY

- Dispute supportNo

Dispute support

No

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payout timingStandard payout timing applies

Payout timing

Standard payout timing applies

- Refunds / Partial refundsYes/yes

Refunds / Partial refunds

Yes/yes

- Minimum charge amount¥120

Minimum charge amount

¥120

- Maximum charge amount¥300,000

Maximum charge amount

¥300,000

## Payment flow

1. Selects Konbini at checkout

2. Receives payment codes and a confirmation number

3. Makes a cash payment with the appropriate payment code and confirmation number at a convenience store

4. Receives notification that payment is complete

## Get started

You don’t actually have to integrate Konbini and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding Konbini from the Dashboard:

- Invoicing

[Invoicing](/invoicing/quickstart-guide)

- Payment Links

[Payment Links](/payment-links)

- Subscriptions

[Subscriptions](/billing/subscriptions/overview)

If you prefer to manually list payment methods, learn how to manually configure Konbini as a payment.

[manually configure Konbini as a payment](/payments/konbini/accept-a-payment)

## Disputed payments

Konbini payments have a low risk of fraud or unrecognized payments because the customer must provide cash payment in person at a convenience store. Generally Konbini payments cannot be disputed by the customer. However, in rare instances irregularities similar in nature to disputes (by the convenience store) might arise, (for example, due to mishandling). Stripe will need to reach out to you in such cases and ask for your cooperation.

## Refunds

Konbini payments can be refunded either through the Dashboard or API. To complete a refund, your customer must provide account information where funds should be returned to. Stripe automatically contacts the customer at the email address provided at time of PaymentIntent confirmation and requests this information from them, after which the refund is processed automatically.

[Dashboard](https://dashboard.stripe.com/payments)

[API](/api#create_refund)

## Billing

Use Stripe Billing to create Konbini supported subscriptions and invoices.

[Stripe Billing](https://stripe.com/billing)

[subscriptions](/billing/subscriptions/creating)

[invoices](/api/invoices)

Due to the in-person nature of Konbini payments, automatically charged invoices are not supported.

[automatically charged](/invoicing/automatic-charging)

Invoices and subscriptions need to be configured with a collection_method of send_invoice.

[collection_method](/api/invoices/object#invoice_object-collection_method)

## Prohibited business categories

On top of the categories of businesses restricted from using Stripe overall, the following categories are specifically prohibited from using Konbini.

[businesses restricted from using Stripe overall](https://stripe.com/restricted-businesses)

- Sole proprietors who have been doing business for less than 3 years

- Real Money Trading (RMT), that is, sale of virtual (in-game) characters, currency, and so on.

- Gambling

- Information selling, in particular:Money making schemesInvestment related informationGambling strategies for horse racing, pachinko, slot machines, and so on

- Money making schemes

- Investment related information

- Gambling strategies for horse racing, pachinko, slot machines, and so on

- Multi-level marketing and pyramid schemes

- Gore content or products

- Unscientific and superstition-based content or products

- Prohibited medical products (per the Japanese Pharmaceutical Affairs Act)

- Content or products offensive to public order or moral

- Personal import facilitation (forwarding)

- Foreign money transfer

- Loans

- Dating sites

- E-cigarettes (vaping), waterpipes (shisha, hookah), and so on

- Fortune-telling

Please keep in mind that our financial partner and convenience store chains may reject businesses at their discretion regardless of category.
