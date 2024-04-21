# Using Treasury to move money

Homebox is a fictitious vertical SaaS that builds software for home services companies like HVAC, cleaners, and plumbers. This integration walks through some basic money movement using the Treasury endpoints of the Stripe API. To see how the company set up a Treasury financial account and issued payment cards, see Using Treasury to set up financial accounts and cards.

[Stripe API](/api)

[Using Treasury to set up financial accounts and cards](/treasury/examples/financial-accounts)

## Using external bank accounts

Stripe Treasury provides platforms with a suite of account creation and money movement API endpoints to help store, manage, and move users’ funds. Platforms can fund a financial account, and move money between Treasury financial accounts and external bank accounts.

The Stripe API offers InboundTransfer and OutboundTransfer to facilitate moving money between users’ external bank accounts and their Treasury financial accounts. The Stripe API also offers OutboundPayment to facilitate moving money from users’ Treasury financial accounts to third-parties’ external bank accounts. All of these objects can leverage PaymentMethods to store external bank account details (such as routing number and account number).

## PaymentMethods explained

Within the Stripe API, you can save payment method information using a PaymentMethod object. For example, Homebox might save their vendors’ accounts as PaymentMethods to send money without having to re-enter and collect their information.

You can attach PaymentMethods that contain external bank account information to a customer (for sending money to a third party) or to a Stripe account (for pulling money from or sending money to an external bank account belonging to the Stripe accountholder). The “customer” refers to the Customer object in the Stripe API, which defines any third party. In Treasury usage, the customer is generally a vendor receiving payments from the Stripe accountholder rather than making payments to the Stripe accountholder. Use the SetupIntent object to set up both customer-attached and account-attached PaymentMethod objects.

The relevant API objects that you can use with a PaymentMethod depend on how they’re attached:

- Customer-attached: Use OutboundPayments.

- Account-attached: Use InboundTransfers and OutboundTransfers.

PaymentMethod flow

## InboundTransfers and OutboundTransfers overview

You can pull funds from a Stripe account’s external bank account using an InboundTransfer and push funds to their external bank account using an OutboundTransfer.

To successfully pull funds into a Treasury financial account with an InboundTransfer, external bank accounts must be verified by the Stripe accountholder. Bank accounts that are used to send funds out of a financial account with an OutboundTransfer don’t need to be verified.

When an external bank account is used for either InboundTransfers or OutboundTransfers, you need to attach the corresponding PaymentMethod to the Stripe account rather than to a customer. You do this by using the attach_to_self=true parameter rather than the customer parameter when creating the PaymentMethod using SetupIntent.

InboundTransfers and OutboundTransfers flow.

## OutboundPayments

Platforms use the OutboundPayment API to send funds from a Treasury financial account to an external bank account owned by a third party.

You must attach PaymentMethods to a customer to use them with OutboundPayments. Bank accounts used for OutboundPayments don’t need to be verified.

OutboundPayments flow

## Adding an external bank account

Homebox wants to link their customers’ own external bank accounts to their Treasury financial accounts. Homebox’s users want to keep all of their business capital in their financial accounts and use inbound transfers to pull money from their external account into their Treasury financial account. To enable their users to transfer money to and from their external account, Homebox creates a SetupIntent with the required parameters and attaches it to an account-attached PaymentMethod:

To send and receive money through OutboundTransfers or InboundTransfers, Homebox must specify an external bank account with the payment_method_data[us_bank_account] parameter. Before creating the live external bank account link, Homebox tests the flow using the test account numbers Stripe provides.

[test account numbers](/payments/ach-debit/set-up-payment?platform=web&payment-ui=stripe-hosted#test-account-numbers)

As shown in the preceding example, Homebox has defined the external bank account (payment_method_data[us_bank_account]) and set attach_to_self as true, which enables the bank account information to be associated with the Stripe accountholder (rather than a third party). When the platform sends the request, the Treasury API responds with a SetupIntent:

[https://payments.stripe.com/microdeposit/sacs_test_xxx](https://payments.stripe.com/microdeposit/sacs_test_xxx)

## Verifying an external bank account

Homebox linked an external bank account in the previous section. The bank account must be verified, though, before Homebox can use it for InboundTransfers. Bank account verification enables the account owner to confirm ownership of the external bank account. To verify, Homebox can use Stripe Financial Connections for instant verification, or microdeposits (which take more time).

[Stripe Financial Connections](#connections)

[microdeposits](#microdeposits)

Stripe offers Financial Connections to instantly verify an owned bank account. Financial Connections is a Stripe hosted flow integrated on the application’s client- and server-side.

[Financial Connections](/financial-connections)

There are three steps necessary for Homebox to collect and verify bank account information with Financial Connections:

- Create a SetupIntent with the property attach_to_self (replacing the customer_id property), and the value instant for the verification_method property.

Create a SetupIntent with the property attach_to_self (replacing the customer_id property), and the value instant for the verification_method property.

- Provide the client_secret to the frontend application to use stripe.collectBankAccountForSetup to collect bank account details, create a PaymentMethod, and attach that PaymentMethod to the SetupIntent.NoteThe account holder’s name in the billing_details parameter is required to create a US bank account PaymentMethod.

Provide the client_secret to the frontend application to use stripe.collectBankAccountForSetup to collect bank account details, create a PaymentMethod, and attach that PaymentMethod to the SetupIntent.

The account holder’s name in the billing_details parameter is required to create a US bank account PaymentMethod.

- Display the mandate terms to collect the authorization for the PaymentMethod usage.

Display the mandate terms to collect the authorization for the PaymentMethod usage.

For step 1, Homebox develops the following code to create a SetupIntent server-side and pass the information to a handlebars.js template. This code assumes that an application has a user logged in to Stripe and that it passes the Stripe Account ID as part of the Session object (req.session.accountId).

[Session object](/api/financial_connections/sessions/object)

Step 2 begins when Homebox passes the following data to the render function:

- The Stripe account ID.

- The client secret obtained from the SetupIntent that’s used as the identifier.

- The platform’s publishable API key.

In this example, the client-side page renders with a button for the user to validate their bank account through Financial Connections.

Modal to add a bank account

Homebox creates the following code to drive the logic behind the preceding button.

In this code example, the script calls the collectUsBankAccountForSetup method and passes the client_secret from the SetupIntent. An application dialog walks the user through linking their bank account.

Workflow for adding a bank account

Step 3 begins with the successful completion of the preceding workflow, as the SetupIntent status changes to requires_confirmation and a modal displays an authorization message for the user to confirm.

[authorization message](/payments/ach-debit/set-up-payment?platform=web#web-collect-mandate-and-submit)

Authorization message

After the user clicks Accept, the code calls the confirmUsBankAccountSetup method and the bank account is stored as verified. The bank account can now be used for InboundTransfers.

Microdeposits are small sums of money, typically a fraction of a US dollar, that Stripe deposits into an external bank account. Owners of the account can verify ownership of the account by confirming the exact amount of those deposits.

The SetupIntent object that Homebox created in the previous section includes a PaymentMethod ID.

The SetupIntent also includes a next_action object with a URL defined in the hosted_verification_url value.

[https://payments.stripe.com/microdeposit/sacs_test_xxx](https://payments.stripe.com/microdeposit/sacs_test_xxx)

Homebox provides the URL to the connected account owner to complete verification. The owner must follow the URL to verify receipt by entering the associated descriptor code of the microdeposit (in test mode, use the value SM11AA).

[test mode](/test-mode)

Microdeposit verification

## Using PaymentMethods with InboundTransfers

Homebox can begin creating InboundTransfers using a bank account verified with one of the previously described methods.

The following request transfers 200 USD using an account-attached payment method into the financial account with the provided ID. The Stripe-Account header value identifies the Stripe account that owns both the financial account and the payment method.

If successful, the response provides the InboundTransfer object. The object includes a hosted_regulatory_receipt_url that provides access to details of the transaction for the account holder on the Homebox platform.

## Using PaymentMethods with OutboundPayments

You can also use a PaymentMethod to send funds to an external bank account owned by a third party using OutboundPayment objects.

Homebox wants to send funds to one of its connected account’s vendors on a recurring basis to pay for supplies. To do so, the platform needs to first get the customer ID using the Customers endpoint.

The response provides the customers for the associated connected account. Homebox identifies the correct customer and records their ID.

Homebox then creates a SetupIntent using the ID. Because OutboundPayments are used for outbound money flows to third parties, Homebox makes sure to set flow_directions to outbound and doesn’t use attach_to_self, instead specifying a customer.

A successful call returns the following object to indicate the PaymentMethod is successfully attached to the customer.

## Creating an OutboundPayment without a PaymentMethod

PaymentMethods aren’t required when sending or using OutboundPayments if you don’t have a need to store the recipient’s bank account, as in the case of one-off payments.

Homebox needed to pay a vendor 50 USD to cover the cost of supplies. To pay the vendor, the platform calls OutboundPayments with the external bank account information.

The successful call returns the following object:

## See also

- Using Treasury to set up financial accounts and cards

[Using Treasury to set up financial accounts and cards](/treasury/examples/financial-accounts)

- API reference

[API reference](/api/treasury/financial_accounts)
