# Payment details

This component is a subset of payments, which provides the detail overlay of a given payment. The UI rendered by the payment details component is equivalent to the overlay that the payments component renders when the user clicks on a payment row.

Use the payment-details component to invoke the payment details overlay without the need to inline the entirety of the payments list in your website. This allows you to invoke the payment detail overlay from your existing UI (for example, your payments list) and integrate with our detail view to enable your customers to view payment details, issue refunds, and manage disputed payments.

By default, the embedded components offer limited information for destination charges and separate charges and transfers. They don’t provide access to customer information, payment methods, and some charge amount details. The destination_on_behalf_of_charge_management feature allows a connected account to see additional information with destination charges, as well as perform refunds and manage disputes.

[destination_on_behalf_of_charge_management](/connect/supported-embedded-components/payment-details#allow-your-connected-accounts-to-manage-destination-charges)

When creating an Account Session, enable payment details by specifying payment_details in the components parameter. You can turn on or off an individual feature of the payment details component by specifying the features parameter under payment_details:

[creating an Account Session](/api/account_sessions/create)

After creating the account session and initializing ConnectJS, you can render the payment details component in the frontend:

[initializing ConnectJS](/connect/get-started-connect-embedded-components#account-sessions)

For destination charges and separate charges and transfers, the connected accounts don’t own the payment intent objects associated with the charges. Pass in the ID of the payment object that belongs to the connected account for these charges.

[destination charges](/connect/destination-charges)

[separate charges and transfers](/connect/separate-charges-and-transfers)

The payment details component shows different information and supports different features for different charge types:

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

This embedded component supports the following parameters:

[charges API](/api/charges)

To enable the dismiss behavior of this component, listen to the close event by calling setOnClose.
