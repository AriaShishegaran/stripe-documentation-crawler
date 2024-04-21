# Payments

Renders a transaction list for direct charges, destination charges, and separate charges and transfers on the connected account.

[direct charges](/connect/direct-charges)

[destination charges](/connect/destination-charges)

[separate charges and transfers](/connect/separate-charges-and-transfers)

By default, the embedded components offer limited information for destination charges and separate charges and transfers. They don’t provide access to customer information, payment methods, and some charge amount details. The destination_on_behalf_of_charge_management feature allows a connected account to see additional information with destination charges, as well as perform refunds and manage disputes.

[destination_on_behalf_of_charge_management](/connect/supported-embedded-components/payments#allow-your-connected-accounts-to-manage-destination-charges)

## Creating an Account Session

When creating an Account Session, enable the payments embedded component by specifying payments in the components parameter. You can turn on or off an individual feature of the payments component by specifying the features parameter under payments:

[creating an Account Session](/api/account_sessions/create)

The payments component shows different information and supports different features for different charge types:

- For direct charges, your connected accounts can view the complete set of information. They can also manage refunds, manage disputes, and capture payments if you enable the corresponding features when creating an account session.

- For destination charges and separate charges and transfers, your connected accounts can only see the transfer object associated with the selected charge, which contains limited information.

[destination charges](/connect/destination-charges)

[separate charges and transfers](/connect/separate-charges-and-transfers)

- For destination charges with the on_behalf_of attribute, your connected accounts can view the complete set of information when the destination_on_behalf_of_charge_management feature is enabled. When this feature is turned on, you can also enable refund and disputes management by enabling the corresponding features.

[on_behalf_of](/api/payment_intents/object#payment_intent_object-on_behalf_of)

When you set the destination_on_behalf_of_charge_management feature to true, your connected accounts can use the payments component to view and manage destination charges that have the on_behalf_of attribute. If you also turn on the dispute_management feature, your connected accounts can participate directly in handling their disputes.

[destination charges](/connect/destination-charges)

[on_behalf_of](/api/payment_intents/object#payment_intent_object-on_behalf_of)

[participate directly in handling their disputes](/connect/supported-embedded-components/payments#dispute-management-for-destination-charges)

Enabling the destination_on_behalf_of_charge_management feature has the following limitations:

- You can’t filter by charge status or payment methods.

- You can’t export certain data columns.

## Rendering the payments component

After creating the account session and initializing ConnectJS, you can render the payments component in the front end:

[initializing ConnectJS](/connect/get-started-connect-embedded-components#account-sessions)

## Dispute management for destination charges

When a dispute occurs on destination charges or separate charges and transfers, the platform is debited the disputed amount and a dispute fee. Connect embedded components don’t reverse the transfer to the connected account regardless of the Account Session features. We recommend setting up webhooks to listen to dispute events. When a dispute is created, you can create an account debit or a transfer reversal on the transfer to your connected account. You can also reverse the transfer to your connected account through the Dashboard. When a dispute is closed, you can then update the balance on your connected account depending on the result of the dispute. If your connected account won the dispute, you can create a transfer to reverse the effect of the account debit or transfer reversal.

[dispute](/disputes/connect)

[destination charges](/connect/destination-charges)

[separate charges and transfers](/connect/separate-charges-and-transfers)

[webhooks](/api/webhook_endpoints)

[dispute events](/api/events/types#event_types-charge.dispute.created)

[account debit](/connect/account-debits#charging-a-connected-account)

[transfer reversal](/api#create_transfer_reversal)

[Dashboard](https://dashboard.stripe.com/test/transfers)

[create a transfer](/api#create_transfer)

When both dispute_management and destination_on_behalf_of_charge_management are enabled, the connected accounts can update and modify dispute evidence, counter disputes, and accept disputes for destination charges with the on_behalf_of attribute set to them.

## Customizing description

To display a custom description within the payment component for destination charges and separate charges and transfers, follow these steps:

[destination charges](/connect/destination-charges)

[separate charges and transfers](/connect/separate-charges-and-transfers)

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
