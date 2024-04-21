# Error resolution

If you encounter any issues when syncing records from Stripe to NetSuite, you can use the list below to identify and resolve the errors. You might need to modify NetSuite, Stripe, or the connector and then manually sync the record.

You can view all errors in the connector app’s sync records window.

## Data errors

The table below contains errors you might encounter when syncing records to NetSuite.

Please enter value(s) for: [Field Name].

NetSuite

The connector can’t create or update a NetSuite record due to a missing required field on that record. For example, if the connector tries to create an invoice where the Department field is required, NetSuite won’t allow the connector to complete the action until there’s a value for Department in the create invoice request.

Add a default value for the field. To do so, navigate to the App settings > Field mapping > Field defaults page in the connector. The connector uses the default value when creating records of that type. Field defaults use the JSON format.

For example, to add a default value of 2 for Department on your invoices, you add the following:

You have entered an Invalid Field Value [value] for the following field: [field].

NetSuite

The connector can’t create or update a NetSuite record due to one or more invalid field values. This might happen if a field default uses a value that was deleted or made unavailable for any reason.

For example, you might have Class as a required field for deposits. During onboarding, you add a field default of Corporate with an internal ID of 5 to satisfy the requirement. After some time the value for Corporate (ID: 5) is deleted. When the connector attempts to create another bank deposit, it fails with the following error message: You have entered an Invalid Field Value 'Corporate' for the following field: Class

Modify the default value to use a valid field ID. To do so, navigate to the App settings > Field mappings > Field defaults page in the connector.

## Duplicate payments

Stripe and NetSuite handle duplicate payments differently. While Stripe allows overpayment of an invoice, NetSuite returns an error if a customer attempts to make a payment on a fully paid invoice. By default, if a duplicate payment occurs in Stripe, the connector won’t sync the payment because NetSuite doesn’t allow a second payment.

If a duplicate payment causes an error when the connector attempts to reconcile the payout during deposit automation, you can fix the issue by manually removing the first payment from the invoice to allow the second payment.

[deposit automation](/connectors/netsuite/deposit-automation)

Or you can allow the connector to handle duplicate payments for you. If you have a NetSuite invoice that’s fully paid, the connector brings over duplicate payments as unapplied payments in NetSuite. The unapplied payment includes the following memo: Stripe Payment Error: could not apply to invoice XYZ. You can then use these unapplied payments on another invoice, or refund the payments manually in Stripe. To search for duplicate payments in NetSuite, create a saved search using the memo as your criteria.

You can enable the connector to handle duplicate payments in the following ways:

- Allow all duplicate payments in the connector, by default. To do so, go to your connector settings and enable Allow duplicate invoice payments in your Stripe app settings. Contact your implementation partner to understand all accounting and technical implementations before they enable this feature for you.

Allow all duplicate payments in the connector, by default. To do so, go to your connector settings and enable Allow duplicate invoice payments in your Stripe app settings. Contact your implementation partner to understand all accounting and technical implementations before they enable this feature for you.

- Using the Stripe API, add the netsuite_allow_duplicate: true field in the metadata of a duplicate Stripe charge.

Using the Stripe API, add the netsuite_allow_duplicate: true field in the metadata of a duplicate Stripe charge.
