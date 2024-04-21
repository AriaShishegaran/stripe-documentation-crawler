# Alipay payments

Alipay is a digital wallet in China that has more than a billion active users worldwide. Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer’s login credentials.

- Customer locationsChinese consumers, overseas Chinese, and Chinese travelers

Customer locations

Chinese consumers, overseas Chinese, and Chinese travelers

- Presentment currencyCNY, AUD, CAD, EUR, GBP, HKD, JPY, SGD, MYR, NZD, USD (depending on business locations)

Presentment currency

CNY, AUD, CAD, EUR, GBP, HKD, JPY, SGD, MYR, NZD, USD (depending on business locations)

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyWallets

Payment method family

Wallets

- Recurring paymentsRequires approval

Recurring payments

Requires approval

[Requires approval](https://support.stripe.com/contact)

- Payout timingStandard payout timing applies

Payout timing

Standard payout timing applies

- Connect supportPartial (request an invite to create charges on behalf of other accounts)

Connect support

Partial (request an invite to create charges on behalf of other accounts)

[on behalf of](/connect/charges#on_behalf_of)

- Dispute supportNo

Dispute support

No

- Refunds / Partial refundsYes / yes

Refunds / Partial refunds

Yes / yes

## Prohibited business categories

For more information about Alipay eligibility for your account, navigate to your Payment methods settings.

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

Both Stripe and Alipay maintain a list of prohibited businesses that aren’t allowed to use their services. To use Alipay on Stripe, your business can’t be restricted from using Stripe or appear on Alipay’s prohibited business list. If you’re not sure if your business is a prohibited business, or have questions about how these requirements apply to you, please contact support.

[restricted from using Stripe](https://stripe.com/restricted-businesses)

[prohibited business list](https://stripe.com/legal/alipay)

[contact support](https://support.stripe.com/contact/login)

## Get started

You don’t actually have to integrate Alipay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

Payment Links also supports adding Alipay from the Dashboard.

[Payment Links](/payment-links)

If you prefer to manually list payment methods, learn how to manually configure Alipay as a payment.

[manually configure Alipay as a payment](/payments/alipay/accept-a-payment)

## Disputed payments

Alipay payments have a low risk of fraud or unrecognized payments because the customer must authenticate the payment, so no dispute process exists that could create chargebacks and withdraw funds from your Stripe account. If an Alipay user contacts them about a problem with a transaction, they might direct that user to you for a resolution.

## Refunds

You can refund Alipay payments up to 90 days after the original payment. Refunds for Alipay payments are asynchronous and take up to 5 minutes to complete. Stripe notifies you of the final refund status using the charge.refund.updated webhook event. When a refund succeeds, the status of the Refund object transitions to succeeded. If a refund fails, the status of the Refund object transitions to failed and Stripe returns the amount to your Stripe balance. At this point, you need to arrange an alternative way of providing your customer with a refund.

[webhook](/webhooks)

[Refund](/api/refunds/object)

## Supported currencies

You can create Alipay payments in the currencies that map to your country. The default local currency for Alipay is cny and customers also see their purchase amount in cny.

If you have a bank account in another currency and would like to create an Alipay payment in that currency, you can contact support. Support for additional currencies is provided on a case-by-case basis.

[contact support](https://support.stripe.com/email)

## See also

Accepting Alipay payments

[Accepting Alipay payments](/payments/alipay/accept-a-payment)
