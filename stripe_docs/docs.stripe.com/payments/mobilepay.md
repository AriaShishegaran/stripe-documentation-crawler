# MobilePay payments

MobilePay is a single-use card wallet payment method used in Denmark and Finland. It allows customers to authenticate and approve payments using the MobilePay app.

[single-use](/payments/payment-methods#usage)

[authenticate and approve](/payments/payment-methods#customer-actions)

During the processing of a MobilePay payment, Stripe performs a card transaction using the card data we receive from MobilePay. The processing of the card transaction is invisible to your integration, and you can only see the outcome of the transaction.

Stripe immediately notifies you when the payment succeeded or failed.

[immediately notifies you](/payments/payment-methods#payment-notification)

- Customer locationsDenmark and Finland

Customer locations

Denmark and Finland

- Presentment currencyDKK, EUR, NOK, SEK

Presentment currency

DKK, EUR, NOK, SEK

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyDigital wallet

Payment method family

Digital wallet

- Recurring paymentsNo

Recurring payments

No

- Payout timingStandard payout timing applies

Payout timing

Standard payout timing applies

[Standard payout timing](/payouts#payout-speed)

- Connect supportYes

Connect support

Yes

- Refunds / Partial refundsYes / yes

Refunds / Partial refunds

Yes / yes

- Dispute supportYes

Dispute support

Yes

## Payment flows

The customer follows a mobile redirect flow to pay with MobilePay.

Customers pay with MobilePay by using one of the following methods:

- Mobile: Customers follow a mobile redirect from your website or mobile app to the MobilePay app, where they authorize the payment, then return to your website or mobile app.

Mobile: Customers follow a mobile redirect from your website or mobile app to the MobilePay app, where they authorize the payment, then return to your website or mobile app.

- Desktop: Customers enter their phone number linked with MobilePay which initiates a push notification on their MobilePay app, this allows them to authorize the payment.

Desktop: Customers enter their phone number linked with MobilePay which initiates a push notification on their MobilePay app, this allows them to authorize the payment.

## Get started

Learn how to manually configure MobilePay as a payment method.

[manually configure MobilePay as a payment method](/payments/mobilepay/accept-a-payment)

You don’t actually have to integrate MobilePay and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding MobilePay from the Dashboard:

- Payment Links

[Payment Links](/payment-links)

## MobilePay with Connect

You can use Stripe Connect with MobilePay to process payments on behalf of a connected account. Connect users can use MobilePay with the following charge types:

[Stripe Connect](/connect/overview)

- Direct

[Direct](/connect/direct-charges)

- Destination

[Destination](/connect/destination-charges)

- Separate charges and transfers

[Separate charges and transfers](/connect/separate-charges-and-transfers)

Connected accounts that use the Stripe dashboard can enable MobilePay in their Payment methods settings in the Dashboard. To check which accounts have enabled MobilePay, use the capabilities hash in our accounts webhooks or APIs to see if the mobilepay_payments capability is set to active.

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

[accounts webhooks or APIs](/api/accounts/object#account_object-capabilities-mobilepay_payments)

Follow the instructions to enable payment methods for your connected accounts. The name of your connected account is the name customers see during checkout and in the MobilePay app.

[enable payment methods for your connected accounts](/connect/account-capabilities)

## Refunds

MobilePay supports full and partial refunds. You can also issue multiple partial refunds up to the amount of the original charge.

## Disputed payments

MobilePay allows transaction disputes. Customers can open disputes directly with their cards issuer for cases of suspected fraud, double payments, or a difference between an order and a transaction amount. You can submit evidence to contest a dispute directly. The dispute process is the same as that for card payments. Learn how to manage disputes.

[manage disputes](/disputes/responding)

## Card transaction retries

MobilePay allows customers to retry payments in-app before marking a payment as failed and redirecting to your website. When a card transaction fails, the customer can retry a payment using a different card, which might result in a successful payment.

## 3D-Secure authentication

Certain cards or banks might require the need for an additional card authentication step during the processing of the MobilePay transaction.

When this occurs, the customer is presented with a WebView dialog in the MobilePay application, prompting them to authorize the payment. The need to perform a 3D-Secure challenge is invisible to your integration and there are no extra integration steps required for you to handle.

[3D-Secure challenge](/payments/3d-secure)

The expected impact varies, depending on customer country and card network:

## Liability shift

Liability shift doesn’t apply to MobilePay payments unless 3D-Secure authentication has taken place. MobilePay doesn’t allow you the option to enforce 3D-Secure authentication on the underlying card payment.

[Liability shift](/payments/3d-secure/authentication-flow#disputed-payments)

[3D-Secure authentication](/payments/3d-secure)

## Prohibited business categories

In addition to the categories of businesses restricted from using Stripe overall, the following categories are specifically prohibited from using MobilePay:

[businesses restricted from using Stripe overall](https://stripe.com/restricted-businesses)

- Bitcoins

- Stock trade

- Gambling

- Betting

- Bonds

- Money transfers

- Debt collection

- Multi-level marketing and pyramid schemes

For more information about MobilePay eligibility for your account, review your Payment methods settings in the Dashboard.

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

## Current limitations

At this time, the MobilePay transaction confirmation page displays the default merchant account icon instead of a configurable custom logo. Stripe will notify you as feature improvements become available so you can update your account configuration as needed.

An example confirmation page is presented below:

A screenshot of a successful MobilePay payment.

At this time, MobilePay only supports automatic captures and manual captures of the full amount. Stripe will notify you as feature improvements become available for manual captures of partial amounts.

[manual captures of the full amount](/payments/place-a-hold-on-a-payment-method)

Stripe currently doesn’t have support for the Dankort card network. If a customer chooses to pay with a Dankort-branded card, Stripe processes the payment on the Visa and Mastercard networks instead.

## Fees

To process MobilePay payments, Stripe receives card data from MobilePay to process card transactions using Stripe’s Visa and Mastercard integrations. As MobilePay payments are card transactions, you incur the following fees for each successful transaction:

- Stripe processing fees associated with the card transaction

- Applicable taxes

- MobilePay transaction processing fee

- An additional monthly membership fee (applicable only to Denmark registered businesses)

The MobilePay transaction fee isn’t subtracted immediately from the transaction. Instead, Stripe bills them once a day.

After a successful transaction, Stripe automatically deducts the Stripe transaction fees and applicable taxes from the original transaction amount and provides the remaining amount on your Stripe balance. These fees are identical to a standard card transaction.

MobilePay is subject to the standard payout schedule applicable to your country.

[standard payout schedule applicable to your country](/payouts)

The MobilePay processing fee isn’t presented within the net amount of a successful transaction. Instead, Stripe bills the MobilePay processing fee once a day, at which point we automatically deduct the sum that you owe from your Stripe balance.

[Stripe balance](https://dashboard.stripe.com/balance)

MobilePay charges a fixed 35 DKK monthly membership fee to all Denmark registered businesses using its services. Stripe bills this fee once a month (if applicable), at which point we automatically deduct the sum that you owe from your Stripe balance.

[Stripe balance](https://dashboard.stripe.com/balance)

The incurred MobilePay fees are listed as a separate entry on your monthly tax invoice. You can find your monthly invoices in your Dashboard.

[Dashboard](https://dashboard.stripe.com/settings/documents)
