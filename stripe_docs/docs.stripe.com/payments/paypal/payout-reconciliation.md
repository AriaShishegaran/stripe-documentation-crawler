# PayPal payout reconciliation

Reconciliation is the process of matching and verifying payments that have been received and processed with the corresponding PayPal orders. It only applies to customers receiving their funds on PayPal, and not on Stripe. Stripe automatically reconciles PayPal transactions before the payout, whereas this can’t be done if transactions settle outside of Stripe’s platform. When transactions settle outside of Stripe’s platform, you’ll use PayPal reporting available on your PayPal account or with sFTP for reconciliation.

[reconciles](/reports/payout-reconciliation)

Stripe provides two ways of supporting PayPal transaction reconciliation:

- (Recommended) Using the reference field. This is the preferred option if you have a businesses-generated order or invoice ID, which you can put in the reference field. After the payment is made and processed, my_order_id appears as Invoice ID in the PayPal settlement report.

[reference](#use-reference)

- Using the transaction_id from the Charge object.  When the payment is processed, paypal_capture_id appears as Transaction ID in the PayPal settlement report. This is recommended only if you don’t have a business-generated order ID.

[transaction_id](#use-transaction-id)

[Charge](/api/charges/object#charge_object-payment_method_details-paypal-transaction_id)

## Use Reference

Use the reference field to populate your own reference for an order on a PayPal payment. One example of this is an Order ID from PayPal. This reference is visible to the buyer and also in the settlement report on your PayPal account. To reconcile funds using a reference, you can include it as part of the payment_method_options parameter when creating a PaymentIntent. You can use this reference to match payments made through Stripe with corresponding transactions in the PayPal settlement report. Any subsequent transactions derived from the original Payment transaction, such as refunds and disputes, are associated with the given reference.

[reference](/api/payment_intents/object#payment_intent_object-payment_method_options-paypal-reference)

[settlement report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/)

[payment_method_options](/api/payment_intents/create#create_payment_intent-payment_method_options-paypal)

[PayPal settlement report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/)

The following code sample shows the creation of a PaymentIntent with the reference set in payment_method_options:

After the payment is made and processed, my_order_id is reflected as Invoice ID in the PayPal settlement report.

[PayPal settlement report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/)

## Use the Charge object’s transaction ID

The transaction_id field contains the ID used by PayPal to identify a transaction. To reconcile funds using a transaction_id, retrieve the transaction_id from the payment_method_details field in the Charge object. The transaction_id is present only if the payment has been captured. It’s used to match payments made through Stripe with corresponding transactions in the PayPal settlement report.

[transaction_id](/api/charges/object#charge_object-payment_method_details-paypal-transaction_id)

[payment_method_details](/api/charges/object#charge_object-payment_method_details-paypal)

[PayPal settlement report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/)

For example, here’s how you can retrieve the transaction_id from the Charge object:

When the payment is processed, paypal_capture_id is appears as Transaction ID in the PayPal settlement report.

[PayPal settlement report](https://developer.paypal.com/docs/reports/sftp-reports/settlement-report/)

## Access your PayPal reports

You can download your PayPal Settlement Report and other reports from paypal.com, or you can enable sFTP reporting by contacting PayPal.

The Settlement Report provides an end-to-end view of all balance-impacting transactions within a 24-hour period. This report is used to reconcile money moving events in a PayPal account with monies that are moved to a linked bank account.

To access the Settlement report:

- Log in to your PayPal business account.

[Log in](https://www.paypal.com/signin)

- Under Activity, select All Reports.

- Select Transactions > Settlement.

Read more about PayPal reports and how to download them.

[PayPal reports and how to download them](https://www.paypal.com/us/cshelp/article/how-do-i-view-and-download-statements-and-reports-help145)
