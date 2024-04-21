# Swish payments

Swish is a single-use payment method used in Sweden. It allows customers to authenticate and approve payments using the Swish mobile app and the Swedish BankID mobile app.

[single-use](/payments/payment-methods#usage)

[authenticate and approve](/payments/payment-methods#customer-actions)

You get immediate notification on whether the payment succeeded or failed.

[immediate notification](/payments/payment-methods#payment-notification)

- Customer locationsSweden

Customer locations

Sweden

- Presentment currencySEK

Presentment currency

SEK

- Payment confirmationCustomer-initiated

Payment confirmation

Customer-initiated

- Payment method familyReal-time payments

Payment method family

Real-time payments

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

- Refunds/Partial refundsYes/yes

Refunds/Partial refunds

Yes/yes

- Dispute supportNo

Dispute support

No

## Payment flows

The customer follows a mobile redirect flow to pay with Swish.

Customers pay with Swish by using one of the following methods:

- Mobile: Customers follow a mobile redirect from your website or mobile app to the Swish app, where they authorize the payment, then return to your website or mobile app.

Mobile: Customers follow a mobile redirect from your website or mobile app to the Swish app, where they authorize the payment, then return to your website or mobile app.

- Desktop: Customers scan a QR code you present on your website using the Swish app, which allows them to authorize the payment.

Desktop: Customers scan a QR code you present on your website using the Swish app, which allows them to authorize the payment.

## Get started

Learn how to manually configure Swish as a payment method.

[manually configure Swish as a payment method](/payments/swish/accept-a-payment)

You don’t actually have to integrate Swish and other payment methods individually. If you use our front-end products, Stripe automatically determines the most relevant payment methods to display. Follow a quickstart for one of our hosted UIs:

- Checkout: Our prebuilt, hosted checkout page.

[Checkout](/checkout/quickstart)

- Elements: Our drop-in UI components.

[Elements](/payments/quickstart)

After setting up your payment form, activate the payment methods you want using the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)

The following Stripe products also support adding Swish from the Dashboard:

- Payment Links

[Payment Links](/payment-links)

## Merchant of record

For Swish payments, Stripe operates as the merchant of record. Therefore, Stripe’s name appears as the recipient of payments in the Swish app and as the statement descriptor in the customer’s bank statements. Your business name appears in the message field in the Swish app.

## Prohibited business categories

In addition to the industry and business categories listed in Prohibited and Restricted Businesses, the following categories aren’t allowed to use Swish:

[Prohibited and Restricted Businesses](https://stripe.com/restricted-businesses)

- Precious stones and metals, watches and jewelry

- Digital wallet top-ups

## Refunds

You can refund Swish charges up to 365 days after the payment completes. Refunds usually take a few minutes to complete. Swish supports full and partial refunds. You can also issue multiple partial refunds up to the amount of the original charge.

## Swish with Connect

You can use Stripe Connect with Swish to process payments on behalf of a connected account. Connect users can use Swish with the following charge types:

[Stripe Connect](/connect/overview)

- Direct

[Direct](/connect/direct-charges)

- Destination

[Destination](/connect/destination-charges)

- Separate charges and transfers

[Separate charges and transfers](/connect/separate-charges-and-transfers)

Connected accounts that use the Stripe dashboard can enable Swish in their Payment methods settings in the Dashboard. To check which accounts have enabled Swish, use the capabilities hash in our accounts webhooks or APIs to see if the swish_payments capability is set to active.

[Payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

[accounts webhooks or APIs](/api/accounts/object#account_object-capabilities-swish_payments)

Follow the instructions to enable payment methods for your connected accounts. The name of your connected account is the name customers see during checkout and in the Swish app.

[enable payment methods for your connected accounts](/connect/account-capabilities)
