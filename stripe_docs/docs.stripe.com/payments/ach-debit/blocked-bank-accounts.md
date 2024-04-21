# Blocked bank accounts

Bank accounts can become blocked for reasons other than insufficient funds, and can become blocked for legitimate reasons or because of an error. You can minimize the chances of an account being blocked, and you can take actions to unblock accounts if you understand the underlying reasons.

## Reasons for blocked bank accounts

When ACH Debits are returned for reasons other than insufficient funds (for example, an account is closed or frozen), NACHA rules require originators of an ACH Debit to review and confirm the bank account or take other action before reinitiating a debit. To comply with these Rules, Stripe blocks certain bank accounts until we can confirm that the issue causing the returns has been resolved. In addition to ensuring compliance with the NACHA rules, this process helps businesses reduce fraud and avoid repeated dispute and return fees. We don’t block bank accounts because of past insufficient funds returns.

## Minimizing blocked customer bank accounts

You can minimize the risk of dealing with blocked customer bank accounts by taking a few preventative steps. To minimize this risk, we recommend that you:

- Verify accounts using Financial Connections Instant Verification—This helps confirm accurate account details and verify account ownership.

- Prevent accidental disputes—Use clear statement descriptors for your business name that customers can easily recognize on their bank statements, which minimizes the chance that a confused customer unintentionally disputes your payments.

[statement descriptors](https://support.stripe.com/questions/update-business-name-shown-on-customer-bank-statements)

- Reduce bank auto-blocks—Some banks and business accounts automatically reject ACH Debits attempts from unknown entities. To prevent this, have your customer provide Stripe Company IDs to their bank to enable debits initiated by Stripe.

[Stripe Company IDs](https://support.stripe.com/questions/ach-direct-debit-company-ids-for-stripe)

## Identifying blocked accounts

In the Dashboard, ACH Debits that failed because blocked accounts are labeled blocked with an error message. When attempting to confirm a Payment Intent or Setup Intent, these blocked requests return an HTTP 402 status and contain the bank_account_unusable error code. Payment Intents also generate a failed charge, while Setup Intents create a failed Setup Attempt instead.

[Payment Intents](/api/payment_intents)

[Setup Intents](/api/setup_intents)

After creating a US bank account payment method, the us_bank_account.status_details.blocked field renders if the account is blocked. You must make requests using a secret key for the field to appear.

[us_bank_account.status_details.blocked](/api/payment_methods/object#payment_method_object-us_bank_account-status_details-blocked)

You can access the network_code and reason properties inside the PaymentMethod object to understand the details behind each block. The network_code contains the raw ACH return code associated with a previous failed payment or dispute made with this account, while the reason is a summary category that corresponds with the code’s semantic meaning.

[network_code](/api/payment_methods/object#payment_method_object-us_bank_account-status_details-blocked-network_code)

[reason properties](/api/payment_methods/object#payment_method_object-us_bank_account-status_details-blocked-reason)

For more information on removing blocks, consult the section on handling blocked bank accounts below for each reason value. When Stripe removes the block, the us_bank_account.status_details.blocked field stops rendering on all previously affected payment methods.

[handling blocked bank accounts](/payments/ach-debit/blocked-bank-accounts#block-category-table)

Stripe sends the payment_method.automatically_updated event for all saved payment methods when a blockable ACH return is received. This also includes any verified customer bank accounts that were created using the Stripe legacy ACH integration.

[payment_method.automatically_updated](/api/events/types#event_types-payment_method.automatically_updated)

[legacy ACH integration](/payments/ach-debit/migrations)

Consuming these events can provide advance notice if your business model relies on recurring payments that need to be processed before a certain date. Inspect the event data for the us_bank_account.status_details.blocked field, then work with your customer to unblock or switch bank accounts before initiating future payments.

You receive equivalent events when the block is removed, indicating that payment methods can be reused immediately, if an active mandate exists or you recollect one.

## Handling blocked bank accounts

If a customer’s account becomes blocked, the action you take depends on the reason the account was blocked. You can identify the reason code on the blocked payment method.

Bank-initiated failures

- bank_account_closed

- bank_account_frozen

- bank_account_invalid_details

- bank_account_restricted

Contact the customer to make sure their bank account is still valid, and that other information associated with the account is current and correct. If the customer’s bank account is no longer valid or active, ask them to update their payment method for future debits.

If, after contacting the customer, you believe the bank account was blocked in error, please contact Stripe Support. We’ll request additional information (proof that the account is open and debitable) to verify that the issue that caused the account to be blocked has been resolved. After we confirm this information, we can unblock the account for future use.

[Stripe Support](https://support.stripe.com/contact)

Customer-initiated disputes

- debit_not_authorized

When a customer disputes a payment as unauthorized, contact them before attempting any additional debits. After their first dispute, Stripe revokes the associated mandate and requires them to accept a new mandate authorization before additional debits can be attempted.  If they dispute a second payment, the bank account is blocked.

Some bank accounts have anti-fraud tools that automatically reject debit attempts from unknown entities. You can typically identify these blocks with an R29 network_code. If you see an R29, contact your customer and confirm that they’ve asked their bank to allow ACH Debits from the Stripe Company IDs before attempting additional debits.

[Stripe Company IDs](https://support.stripe.com/questions/ach-direct-debit-company-ids-for-stripe)

If, after contacting the customer, you believe they unintentionally disputed these payments, contact Stripe Support. We’ll request additional information to verify that the accountholder authorized the payment and that the issue causing prior disputes has been resolved. After we confirm this information, we can unblock the account for future use.

[Stripe Support](https://support.stripe.com/contact)

- bank_account_unusable

[Stripe Support](https://support.stripe.com/contact)
