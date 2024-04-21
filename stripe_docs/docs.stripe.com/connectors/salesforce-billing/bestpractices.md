# Best practices for using Stripe with Salesforce Billing

Use the the information in this guide to learn how to import data, use payment center, test cards in payment center, and set batch size for optimal performance.

## Data import options

You can add payment methods using the quick action on the Payment Methods related list, which you can access from the Account record. If you need additional help, refer to the Installation and Configuration guide.

## Data import scenarios

You can also add Stripe customer data in other ways, such as with a data import using information from Stripe or by using a custom script. If you use these options, you need to make sure that you have certain values present in the Salesforce records.

See the following data import scenarios, and use whichever one best fits your use case for importing data.

[Import customers and payment methods](#section-1)

## Import customers and payment methods

To import customers and payment methods, the Salesforce Admin needs to do the following:

- Import Customer records (required fields).Account NameStripe Customer ID

- Account Name

- Stripe Customer ID

[Customer](/api/customers/retrieve)

- Import payment method records (required fields).Payment Gateway record IDActive checkbox set to TruePayment Gateway Token

- Payment Gateway record ID

- Active checkbox set to True

- Payment Gateway Token

[Import existing customer and payment methods](#section-2)

## Import existing customer and payment methods

To import existing customers and payment methods, the Salesforce Admin needs to do the following:

- Insert the Account record:Because the Account records already exist in Salesforce, Account records updated with the Stripe Customer ID. There are multiple ways to match to an existing Account (such as an ID or Account Name).

- Because the Account records already exist in Salesforce, Account records updated with the Stripe Customer ID. There are multiple ways to match to an existing Account (such as an ID or Account Name).

[Customer](/api/customers/retrieve)

- Import payment methods required fields.Payment Gateway record IDActive checkbox set to TruePayment Gateway TokenStripe Customer ID

- Payment Gateway record ID

- Active checkbox set to True

- Payment Gateway Token

- Stripe Customer ID

[Customer](/api/customers/retrieve)

[Import only payment methods](#section-3)

## Import only payment methods

To import only payment methods, the Salesforce Admin needs to do the following:

- Import the required fields for payment methods.Payment Gateway record IDActive checkbox set to TruePayment Gateway Token

- Payment Gateway record ID

- Active checkbox set to True

- Payment Gateway Token

[Create a Payment Method from the Payment Center](#section-4)

## Create a Payment Method from the Payment Center

From Salesforce a user can create a payment in the payment center. The connector doesn’t support creating and charging Payment Methods simultaneously from the Payment Center.

This problem occurs when a new payment is entered, and save this payment for later use is selected.

[Increase Salesforce throughput for batch payments in Salesforce Billing](#section-5)

## Increase Salesforce throughput for batch payments in Salesforce Billing

Stripe recommends setting the Payment creation batch size in Salesforce Billing to the upper limit, which is currently 70.

- Navigate to Salesforce Setup and search for installed packages.

- Click Configure next to the Salesforce Billing package.

- Navigate to the Payment tab.

- Adjust the Payment creation batch size as needed.
