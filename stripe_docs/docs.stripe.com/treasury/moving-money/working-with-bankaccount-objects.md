# Working with SetupIntents, PaymentMethods, and BankAccounts

You can use PaymentMethod objects to save account credentials for a US-based bank account for future use. After creating the PaymentMethod, you can use the same object repeatedly to move funds into and out of a financial account. Depending on your use case, you can attach the PaymentMethod to either a Customer object or the Stripe account.

[PaymentMethod](/payments/payment-methods#payment-method-object)

[Customer](/api/customers)

- Attach the PaymentMethod to a Customer object if you intend to use the payment method for an outbound payment to a third party.

- Attach the PaymentMethod to a connected account or platform account if you intend to use the payment method for an inbound transfer or outbound transfer between an external account that belongs to the same business as the Stripe account.

The Customer object defines a third-party entity that represents the owner of an external bank account.

If you previously collected customer payment details with Stripe using the BankAccounts object, you can substitute the BankAccount for a PaymentMethod in those requests. For InboundTransfers, the BankAccount status value in this case must be verified. We recommend using PaymentMethods where possible to get the full suite of features.

[BankAccounts](/ach-deprecated)

In some cases, banks on the receiving end of ACH money movements notify Stripe that account information (such as account number or routing number) has changed. If we receive such a notification for an account associated with a PaymentMethod or BankAccount object, we automatically update the object. See the ACH Notification of Change handling guide for more information.

[ACH Notification of Change handling](/treasury/moving-money/notification-of-change)

## Create a SetupIntent to save us_bank_account details

SetupIntents enable you to set up a payment method to use with money movement endpoints of the Stripe API. Use SetupIntents to save customer or account credentials as a payment method and optimize them for the objects you intend to use it with. For example, when setting up a US bank account, it’s necessary to verify the bank account if you intend to debit that external account with an inbound transfer. Stripe updates the SetupIntent object throughout the setup process.

[SetupIntents](/payments/setup-intents)

The following example demonstrates using a SetupIntent with a bank account that allows for bidirectional fund transfers. For complete details on how to set up a payment method for creating payments and bank account verification, see the Save details for future payments with ACH Direct Debit guide. When setting up payment methods for managing financial account funds with SetupIntents, the following fields are the most relevant:

[Save details for future payments with ACH Direct Debit](/payments/ach-debit/set-up-payment)

- flow_directions: this array defines the directionality of the flows for a payment method. It’s possible values are inbound and outbound, denoting if the payment method can move funds into, out of, or both into and out of a financial account. You can also configure an existing payment method to become bidirectional.

[flow_directions](/api/setup_intents/create#create_setup_intent-flow_directions)

- attach_to_self: a Boolean flag to indicate whether you want to attach this payment method to the in-context Account object. Set this as true to create an account-attached payment method for managing this account’s own money movement flows like inbound transfers and outbound transfers.

[attach_to_self](/api/setup_intents/create#create_setup_intent-attach_to_self)

- customer: ID of the Customer object the payment method is attached to on successful setup. You can use Customer-attached payment methods with outbound payments to send money to third parties and customers. You can also use them with Stripe Payments PaymentIntents to receive money. You must set the attach_to_self attribute to false or leave it blank when creating a customer-attached payment method.

[customer](/api/setup_intents/create#create_setup_intent-confirm)

To use a payment method for ‘inbound’ flow directions (such as InboundTransfers), you need permission from the user. Creating this agreement (Mandate object) up front and associating it with the payment method allows you to charge the payment method later.

[permission from the user](/payments/setup-intents#mandates)

Add terms to your website or app that state how you plan to debit funds from external accounts, and let users opt in. At a minimum, ensure that your terms cover the following:

- User permission for you to initiate a debit or a series of debits on their behalf

- The anticipated frequency of debits (one-time or recurring)

- How the debit amount is determined

While you need user permission with a mandate for debiting an external bank account in the US with inbound transfers, that permission isn’t needed for sending money to a bank account with outbound transfers or outbound payments.

To create a SetupIntent, you must either use an existing payment method with the payment_method parameter, or provide new credentials using the inline payment_method_data parameter.

Use POST /v1/setup_intents to create a SetupIntent.

If successful, the response returns the newly created SetupIntent object.

The SetupIntent has one of the following statuses:

After successfully confirming the SetupIntent, Stripe sends an email confirmation of the mandate and collected bank account details to your user. The default email references Stripe Payments, so if you use Stripe Treasury without Stripe Payments you might want to turn off Stripe emails and send custom messages instead.

[custom messages](/payments/ach-debit#mandate-and-microdeposit-emails)
