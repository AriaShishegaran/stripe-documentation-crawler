# Migrating to new APIs

The ACH Direct Debit payment method allows you to use bank accounts collected with Stripe’s older Bank Accounts API or migrate verified bank accounts from another payment processor to use with the Payment Intents API.

[Bank Accounts API](/ach-deprecated)

[Payment Intents API](/payments/payment-intents)

[Compatibility with the Bank Accounts API](#bank-accounts-api)

## Compatibility with the Bank Accounts API

If you have previously collected customer payment details with Stripe using the Bank Accounts API, you can start using the Payment Intents API immediately without migrating any payment information for ACH Direct Debit. Using customer bank accounts with PaymentIntents is a two-step process:

[Bank Accounts API](/ach-deprecated)

[Payment Intents API](/payments/payment-intents)

[bank accounts](/api/customer_bank_accounts)

- Create a payment with a verified bank account.

- Collect authorization to debit the customer’s bank account via a mandate.

Bank Accounts that are already verified and have been attached to a Customer are usable in any API that accepts a PaymentMethod object. You can use a saved BankAccount as a PaymentMethod when creating a PaymentIntent.

[Bank Accounts](/api/customer_bank_accounts)

[verified](/ach-deprecated#verifying)

[Customer](/api/customers)

[PaymentMethod](/api/payment_methods)

Similarly, you can use a saved BankAccount as a PaymentMethod when creating a SetupIntent.

Confirming a PaymentIntent or SetupIntent requires having your customer authorize a mandate to debit the account. Learn more about SEC codes to understand which authorization type is right for your business.

[mandate](/api/setup_intents/create#create_setup_intent-mandate_data)

[SEC codes](/payments/ach-debit/sec-codes)

In some cases, you might have pre-authorization from your customer from an earlier purchase or SetupIntent that you can use to create an off-session payment. For example:

- If you previously collected an online mandate from the customer, you can use both the IP address and user agent information to create a mandate object.

- If you previously collected payment and mandate information offline on paper, you can create a PPD mandate.

[PPD mandate](/payments/ach-debit/sec-codes#ppd-sec-code)

To create an off-session payment, you can use offline mandate acceptance to provide a record of your customer’s original authorization.

Authorization is only required the first time you use a BankAccount object with the PaymentIntents API. After that, you can use the BankAccount object as a PaymentMethod to accept future payments.

[accept future payments](/payments/ach-debit/set-up-payment#web-future-payments)

You can retrieve saved BankAccounts through the Payment Methods API.

[Payment Methods API](/api/payment_methods)

When using a BankAccount as a PaymentMethod, no new objects are created. The Payment Methods API simply provides a different view of the same underlying object.

[Migrating bank accounts from another payment processor](#migrate-payment-processor)

## Migrating bank accounts from another payment processor

If you have a store of saved bank accounts that you verified and used to process ACH Direct Debit payments on another processor, you can migrate them to Stripe to begin accepting payments.

Both your business and Stripe are responsible for maintaining proof of authorization to debit, as well as proof of bank account verification. Please contact us with details, including:

[contact us](https://support.stripe.com/contact)

- How your business collects authorization from customers.

- How your business verifies customer bank accounts.

Stripe can temporarily give you the ability to skip bank account verification. Request this temporary capability from Stripe Support. Once enabled, process each bank account and create a SetupIntent for each.

[Stripe Support](https://support.stripe.com/contact)

[SetupIntent](/api/setup_intents)

Create a new Customer object or retrieve an existing one to associate with this bank account.

[Customer object](/api/customers)

Then create and confirm a SetupIntent with your saved bank account details and the date of your customer’s original authorization to debit the account.

Retrieve and store the PaymentMethod ID from the response to use for future payments. You can also retrieve it by listing all PaymentMethods for the customer.

[PaymentMethod ID](/api/setup_intents/object#setup_intent_object-payment_method)

[future payments](/payments/ach-debit/set-up-payment#web-future-payments)

[listing](/api/payment_methods/list)
