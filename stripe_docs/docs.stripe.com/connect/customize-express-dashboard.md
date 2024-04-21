# Customize the Express Dashboard

The Express Dashboard allows a platform’s users (connected accounts) to view their available balance, see upcoming payouts, and track their earnings in real time. It displays an Activity feed, an Earnings chart, and your platform’s brand name and icon. Learn how to customize the Express Dashboard for your users in this guide.

[payouts](/payouts)

To learn more about each feature in the Express Dashboard, see Express Dashboard.

[Express Dashboard](/connect/express-dashboard)

[Add your platform's brand name and icon](#add-platform-branding)

## Add your platform's brand name and icon

You can display your platform’s brand name and icon in the Express Dashboard.

Access your Connect settings, enter your platform’s business_name, upload your platform’s icon, and save your changes. If you already saved your brand information before reading this guide, you can skip this step.

[Connect settings](https://dashboard.stripe.com/settings/connect)

[Set custom descriptions for charges and transfers](#set-custom-descriptions)

## Set custom descriptions for charges and transfers

By default, the Transactions list on the Express Dashboard displays generic descriptions for charges and transfers (for example: Payment on {YOUR_PLATFORM}).

First, determine which type of charge your platform uses. The two recommended charge types for Express connected accounts are Destination Charges and Separate Charges and Transfers.

[Destination Charges](/connect/charges#destination)

[Separate Charges and Transfers](/connect/charges#separate-charges-transfers)

After you determine the charge type, use the following instructions to update your integration.

To update the description on a payment object that’s visible to your platform’s users, you need to use the Stripe API. This applies to all platforms that use destination charges.

[description](/api/charges/object#charge_object-description)

[destination charges](/connect/destination-charges)

- Find the existing transfer object you created for an account by finding the latest charge created on the PaymentIntent.

[charge](/api/payment_intents/object#payment_intent_object-charges)

[PaymentIntent](/api/payment_intents/object)

- Use the charge object to find the transfer object associated with the charge.

[transfer](/api/charges/object#charge_object-transfer)

- Use the transfer object to find the destination_payment ID that exists on the transfer.

[destination_payment](/api/transfers/object#transfer_object-destination_payment)

- Call the Update Charge API to update the description on the destination payment using the destination_payment ID.

[Update Charge](/api/charges/update)

[description](/api/charges/update#update_charge-description)

The destination_payment object belongs to the connected account, so you’ll need to set the Stripe-Account header to the connected account’s ID to make this call.

[destination_payment](/api/transfers/object#transfer_object-destination_payment)

[the Stripe-Account header](/connect/authentication)

This description becomes visible on the charge after you’ve written this field.

Learn more about creating destination charges on your platform.

[creating destination charges on your platform](/connect/destination-charges)

To update the description on a payment object that’s visible to your platform’s users, you need to use the Stripe API. This applies to platforms that use separate charges and transfers.

[description](/api/charges/object#charge_object-description)

[separate charges and transfers](/connect/separate-charges-and-transfers)

- Use the transfer object to find the destination_payment ID that exists on the transfer.

[destination_payment](/api/transfers/object#transfer_object-destination_payment)

- Call the Update Charge API to update the description on the destination payment using the destination_payment ID found in the previous step.

[Update Charge](/api/charges/update)

[description](/api/charges/update#update_charge-description)

The destination_payment object belongs to the connected account, so you’ll need to set the Stripe-Account header to the connected account’s ID to make this call.

[destination_payment](/api/transfers/object#transfer_object-destination_payment)

[the Stripe-Account header](/connect/authentication)

This description becomes visible on the charge after you’ve written this field.

Learn more about creating separate charges and transfers.

[creating separate charges and transfers](/connect/separate-charges-and-transfers)

## See also

- Collect payments and then pay out (if you process payments with Stripe)

[Collect payments and then pay out](/connect/collect-then-transfer-guide)

- Pay out money (if you add money from a bank account to pay out)

[Pay out money](/connect/add-and-pay-out-guide)
