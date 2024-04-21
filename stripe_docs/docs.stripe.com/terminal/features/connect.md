# Use Terminal with Connect

Get notified when Stripe Reader S700 is available in your country.

[Get notified](https://dashboard.stripe.com/terminal/s700_notify)

Stripe Terminal is fully compatible with Connect, enabling your platform or marketplace to accept in-person payments.

[Connect](/connect)

The way Terminal creates API objects depends on whether you use direct charges or destination charges. If you use direct charges, all Terminal API objects belong to connected accounts. If you use destination charges, all Terminal API objects are created on your platform account. In both cases, use Locations to group readers as you see fit.

[direct charges](/connect/direct-charges)

[destination charges](/connect/destination-charges)

[Locations](/api/terminal/locations)

Terminal Connect Accounts must have the card_payments capability to perform transactions.

## Direct charges

With direct charges, API objects belong to the connected account rather than the platform. The connected account is responsible for the cost of Stripe fees, refunds, and chargebacks.

[direct charges](/connect/direct-charges)

In the Dashboard, you can view your Terminal data by logging in as the connected account.

With direct charges, you must create payment objects that belong to the connected account. You must create other Terminal API objects like Locations and Readers that belong to the same connected account.

[direct charges](/connect/direct-charges)

[Locations](/api/terminal/locations)

[Readers](/api/terminal/readers)

To create a Location belonging to a connected account, use the Stripe-Account header.

[create a Location](/terminal/fleet/locations)

Before you can connect your application to a smart reader, you must register the reader to a Stripe account. To register a reader to a connected account, use the Stripe-Account header.

[smart reader](/terminal/payments/connect-reader?reader-type=internet)

When using Connect OAuth authentication, the connected account needs to be authorized for live mode and test mode separately, using the respective application Client ID for each mode.

[Connect OAuth](/connect/oauth-reference)

When creating a ConnectionToken for the Terminal SDK, set the Stripe-Account header to the connected account accepting payments. You may also provide a location parameter to control access to readers. If you provide a location, the ConnectionToken is only usable with readers assigned to that location. If you don’t provide a location, the ConnectionToken is usable with all readers.

[ConnectionToken](/api/terminal/connection_tokens)

With the iOS, Android, and React Native SDKs, you can create a PaymentIntent on the client or server. The JavaScript SDK only supports server-side creation.

When creating a PaymentIntent client-side for direct charges, you don’t need to specify any additional parameters for the PaymentIntent. Instead, when creating a ConnectionToken, set the Stripe-Account header to the connected account accepting payments. The iOS, Android, and React Native SDKs create the PaymentIntent on the same connected account the ConnectionToken belongs to. For more information, see Create Payment Intents Client-side.

[Create Payment Intents Client-side](/terminal/payments/collect-payment#create-client-side)

The JavaScript SDK requires you to create the PaymentIntent on your server. For iOS or Android, you might want to create the PaymentIntent on your server if the information required to start a payment isn’t readily available in your app. For more information, see Create Payment Intents Server-side.

[Create Payment Intents Server-side](/terminal/payments/collect-payment?terminal-sdk-platform=js#create-payment)

When creating a PaymentIntent server-side for direct charges, set the Stripe-Account header to the connected account.

## Destination charges

When using destination charges, API objects like Payment Intents and Locations belong to your platform account. Each payment creates a transfer to a connected account automatically.

[destination charges](/connect/destination-charges)

In the Dashboard, you can view your Terminal data directly when logged into your platform account.

The best way to group Reader objects by connected account is by assigning them to Locations. On your platform account, create a Location for a connected account using a display name that identifies the account.

[create a Location](/terminal/fleet/locations)

Before you can connect your application to a smart reader, you must register the reader to your platform account.

[smart reader](/terminal/payments/connect-reader?reader-type=internet)

When creating a ConnectionToken for the Terminal SDK, use your platform account’s secret key. Don’t set the Stripe-Account header. Provide a location parameter to control access to readers. If you provide a location, the ConnectionToken is only usable with readers assigned to that location. If you don’t provide a location, the ConnectionToken is usable with all readers.

When creating a PaymentIntent using destination charges, provide the on_behalf_of and transfer_data[destination], and application_fee_amount parameters.

[on_behalf_of](/api/payment_intents/create#create_payment_intent-on_behalf_of)

[transfer_data[destination]](/api/payment_intents/create#create_payment_intent-transfer_data-destination)

[application_fee_amount](/api/payment_intents/create#create_payment_intent-application_fee_amount)

The on_behalf_of parameter is the ID of the connected account that will become the settlement merchant for the payment.  For Terminal transactions, this parameter must be set in cases where the platform country isn’t the same as the Connect account country. When on_behalf_of is set, Stripe automatically:

- Settles charges in the country of the specified account, thereby minimizing declines and avoiding currency conversions.

- Uses the fee structure for the connected account’s country.

- Lists the connected account’s address and phone number on the customer’s credit card statement, as opposed to the platform’s address and phone number (only occurs if the account and platform are in different countries).

For transfer_data[destination], set the ID of the connected account that receives the transfer.

Finally, you may withhold an application fee for your platform by providing the application_fee_amount parameter.

[application_fee_amount](/api/payment_intents/create#create_payment_intent-application_fee_amount)

With the iOS, Android, and React Native SDKs, you can create a PaymentIntent client-side and provide the onBehalfOf, transferDataDestination, and applicationFeeAmount parameters.

Client-side PaymentIntent creation is possible with the iOS or Android SDKs. If you’re using the JavaScript SDK for Stripe Terminal, create a PaymentIntent server-side.

The JavaScript SDK requires you to create the PaymentIntent on your server. For iOS or Android, you want to create the PaymentIntent on your server if the information required to start a payment isn’t readily available in your app. For more information, see Create Payment Intents Server-side.

[Create Payment Intents Server-side](/terminal/payments/collect-payment?terminal-sdk-platform=js#create-payment)

## See also

- Cart display

[Cart display](/terminal/features/display)

- Receipts

[Receipts](/terminal/features/receipts)
