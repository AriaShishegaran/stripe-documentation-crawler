# Create separate charges and transfers

Create separate charges and transfers to transfer funds from one payment to multiple connected accounts, or when a specific user isn’t known at the time of the payment. The charge on your platform account is decoupled from the transfer(s) to your connected accounts. With this charge type:

- You create a charge on your platform’s account and also transfer funds to your connected accounts. The payment appears as a charge on your account and there are also transfers to connected accounts (amount determined by you), which are withdrawn from your account balance.

- You can transfer funds to multiple connected accounts.

- Your account balance is debited for the cost of the Stripe fees, refunds, and chargebacks.

This charge type is most optimal for marketplaces that need to split payments between multiple parties, such as DoorDash, a restaurant delivery platform.

Stripe supports separate charges and transfers in the following regions:

In most scenarios, your platform and any connected account must be in the same region. Attempting to transfer funds across a disallowed border returns an error. For information about cross-region support, see cross-border transfers. You must only use transfers in combination with the permitted use cases for charges, tops-ups and fees.

[cross-border transfers](/connect/account-capabilities#transfers-cross-border)

[charges](/connect/charges)

[tops-ups](/connect/top-ups)

[fees](#collect-fees)

Redirect to a Stripe-hosted payment page using Stripe Checkout. See how this integration compares to Stripe’s other integration types.

[Stripe Checkout](/payments/checkout)

[compares to Stripe’s other integration types](/payments/accept-a-payment/web/compare-integrations)

[](https://checkout.stripe.dev/)

Redirect to Stripe-hosted payment page

Try it out

[Try it out](https://checkout.stripe.dev/)

[Set up StripeServer-side](#set-up-stripe)

## Set up StripeServer-side

First, register for a Stripe account.

[register](https://dashboard.stripe.com/register)

Use our official libraries to access the Stripe API from your application:

[Create a Checkout SessionClient-sideServer-side](#create-checkout-session)

## Create a Checkout SessionClient-sideServer-side

A Checkout Session controls what your customer sees in the payment form such as line items, the order amount and currency, and acceptable payment methods. Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

[Checkout Session](/api/checkout/sessions)

On your server, create a Checkout Session and redirect your customer to the URL returned in the response.

[URL](/api/checkout/sessions/object#checkout_session_object-url)

[https://example.com/success?session_id={CHECKOUT_SESSION_ID}](https://example.com/success?session_id={CHECKOUT_SESSION_ID})

- line_items - This attribute represents the items the customer is purchasing. The items are displayed in the Stripe-hosted checkout page.

- payment_intent_data[transfer_group] - Use a unique string as the transfer_group to identify objects that are associated with each other. When Stripe automatically creates a charge for a PaymentIntent with a transfer_group value, it assigns the same value to the charge’s transfer_group.

- success_url - Stripe redirects the customer to the success URL after they complete a payment and replaces the {CHECKOUT_SESSION_ID} string with the Checkout Session ID. Use this to retrieve the Checkout Session and inspect the status to decide what to show your customer. You can also append your own query parameters, which persist through the redirect process. See customize redirect behavior with a Stripe-hosted page for more information.

[customize redirect behavior with a Stripe-hosted page](/payments/checkout/custom-success-page)

[Handle post-payment eventsServer-side](#handle-post-payment-events)

## Handle post-payment eventsServer-side

Stripe sends a checkout.session.completed event when the payment completes. Use a webhook to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[Use a webhook to receive these events](/webhooks/quickstart)

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes. Some payment methods also take 2-14 days for payment confirmation. Setting up your integration to listen for asynchronous events enables you to accept multiple payment methods with a single integration.

[payment methods](https://stripe.com/payments/payment-methods-guide)

Stripe recommends handling all of the following events when collecting payments with Checkout:

[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)

[checkout.session.async_payment_succeeded](/api/events/types#event_types-checkout.session.async_payment_succeeded)

[checkout.session.async_payment_failed](/api/events/types#event_types-checkout.session.async_payment_failed)

These events all include the Checkout Session object. After the payment succeeds, the underlying PaymentIntent status changes from processing to succeeded or a failure status.

[Checkout Session](/api/checkout/sessions)

[PaymentIntent](/payments/payment-intents)

[status](/payments/paymentintents/lifecycle)

[Create a TransferServer-side](#create-transfer)

## Create a TransferServer-side

On your server, send funds from your account to a connected account by creating a Transfer and specifying the transfer_group used.

[Transfer](/api/transfers/create)

Transfer and charge amounts don’t have to match. You can split a single charge between multiple transfers or include multiple charges in a single transfer. The following example creates an additional transfer associated with the same transfer_group.

[Test the integration](#test-the-integration)

## Test the integration

[authentication](/strong-customer-authentication)

See Testing for additional information to test your integration.

[Testing](/testing)

[OptionalEnable additional payment methods](#enable-payment-methods)

## OptionalEnable additional payment methods

## Specify the settlement merchant

The settlement merchant is dependent on the capabilities set on an account and how a charge is created. The settlement merchant determines whose information is used to make the charge. This includes the statement descriptor (either the platform’s or the connected account’s) that’s displayed on the customer’s credit card or bank statement for that charge.

[capabilities](/connect/account-capabilities)

Specifying the settlement merchant allows you to be more explicit about who to create charges for. For example, some platforms prefer to be the settlement merchant because the end customer interacts directly with their platform (such as on-demand platforms). However, some platforms have connected accounts that interact directly with end customers instead (such as a storefront on an e-commerce platform). In these scenarios, it might make more sense for the connected account to be the settlement merchant.

You can set the on_behalf_of parameter to the ID of a connected account to make that account the settlement merchant for the payment. When using on_behalf_of:

- Charges settle in the connected account’s country and settlement currency.

- The fee structure for the connected account’s country is used.

- The connected account’s statement descriptor is displayed on the customer’s credit card statement.

- If the connected account is in a different country than the platform, the connected account’s address and phone number are displayed on the customer’s credit card statement.

- The number of days that a pending balance is held before being paid out depends on the delay_days setting on the connected account.

[pending balance](/connect/account-balances)

[delay_days](/api/accounts/create#create_account-settings-payouts-schedule-delay_days)

If on_behalf_of is omitted, the platform is the business of record for the payment.

The on_behalf_of parameter is supported only for connected accounts with the card_payments capability. Accounts under the recipient service agreement can’t request card_payments.

[card_payments](/connect/account-capabilities#card-payments)

[recipient service agreement](/connect/service-agreement-types#recipient)

[https://example.com/success](https://example.com/success)

## Collect fees

When using separate charges and transfers, the platform can collect fees on a charge by reducing the amount it transfers to the destination accounts. For example, consider a restaurant delivery service transaction that involves payments to the restaurant and to the driver:

- The customer pays a 100 USD charge.

- Stripe collects a 3.20 USD fee and adds the remaining 96.80 USD to the platform account’s pending balance.

- The platform transfers 70 USD to the restaurant’s connected account and 20 USD to the driver’s connected account.

- A platform fee of 6.80 USD remains in the platform account.

To learn about processing payments in multiple currencies with Connect, see working with multiple currencies.

[working with multiple currencies](/connect/currencies)

## Transfer availability

The default behavior is to transfer funds from the platform account’s available balance. Attempting a transfer that exceeds the available balance fails with an error. To avoid this problem, when creating a transfer, tie it to an existing charge by specifying the charge ID as the source_transaction parameter. With a source_transaction, the transfer request returns success regardless of your available balance. However, the funds don’t become available in the destination account until the funds from the associated charge are available to transfer from the platform account.

[charge](/api/charges)

If the source charge has a transfer_group value, Stripe assigns the same value to the transfer’s transfer_group. If it doesn’t, then Stripe generates a string in the format group_ plus the associated PaymentIntent ID, for example: group_pi_2NHDDD589O8KAxCG0179Du2s. It assigns that string as the transfer_group for both the charge and the transfer.

You must specify the source_transaction when you create a transfer. You can’t update that attribute later.

You can get the charge ID from the PaymentIntent:

[PaymentIntent](/payments/payment-intents)

- Get the PaymentIntent’s latest_charge attribute. This attribute is the ID of the most recent charge associated with the PaymentIntent.

[latest_charge attribute](/api/payment_intents/object#payment_intent_object-latest_charge)

- Request a list of charges, specifying the payment_intent in the request. This method returns full data for all charges associated with the PaymentIntent.

[Request a list of charges](/api/charges/list)

When using this parameter:

- The amount of the transfer must not exceed the amount of the source charge

- You can create multiple transfers with the same source_transaction, as long as the sum of the transfers doesn’t exceed the source charge

- The transfer takes on the pending status of the associated charge: if the funds from the charge become available in N days, the payment that the destination Stripe account receives from the transfer also becomes available in N days

- Stripe automatically creates a transfer_group for you

- The currency of the balance transaction associated with the charge must match the currency of the transfer

Asynchronous payment methods, like ACH, can fail after a subsequent transfer request is made. For these payments, avoid using source_transaction. Instead, wait until a charge.succeeded event is triggered before transferring the funds. If you have to use source_transaction with these payments, you must implement functionality to manage payment failures.

[charge.succeeded](/api/events/types#event_types-charge.succeeded)

When a payment used as a source_transaction fails, funds from your platform’s account balance are transferred to the connected account to cover the payment. To recover these funds, reverse the transfer associated with the failed source_transaction.

[reverse](/connect/separate-charges-and-transfers#reverse-transfers)

## Transfer options

You can assign any value to the transfer_group string, but it must represent a single business action. You can also make a transfer with neither an associated charge nor a transfer_group—for example, when you must pay a provider but there’s no associated customer payment.

The transfer_group only identifies associated objects. It doesn’t affect any standard functionality. To prevent a transfer from executing before the funds from the associated charge are available, use the transfer’s source_transaction attribute.

Transfer and charge amounts don’t have to match. You can split a single charge between multiple transfers or include multiple charges in a single transfer. You can perform transfers and charges in any order.

By default, a transfer request fails when the amount exceeds the platform’s available account balance. You can instead validate the transfer amount against its associated charge by specifying that charge as the transfer’s source_transaction. In that case, the transfer request automatically succeeds but isn’t executed until the funds from that charge are available in the platform account.

[available account balance](/connect/account-balances)

[by specifying that charge as the transfer’s source_transaction](#transfer-availability)

If you use separate charges and transfers, take that into account when planning your payout schedule. Automatic payouts can interfere with transfers that don’t have a defined source_transaction.

[payout](/payouts)

## Issue refunds

You can refund charges created on your platform using its secret key. However, refunding a charge has no impact on any associated transfers. It’s up to your platform to reconcile any amount owed back to it by reducing subsequent transfer amounts or by reversing transfers.

[reversing transfers](#reversing-transfers)

## Reverse transfers

Connect supports the ability to reverse transfers made to connected accounts, either entirely or partially (by setting an amount value):

[reverse transfers](/api#create_transfer_reversal)

Transfer reversals add the specified (or entire) amount back to the platform’s available balance, reducing the connected account’s available balance accordingly. It is only possible to reverse a transfer if the connected account’s available balance is greater than the reversal amount or has connected reserves enabled.

[connected reserves](/connect/account-balances#understanding-connected-reserve-balances)

If the transfer reversal requires a currency conversion, and the reversal amount would result in a zero balance after the conversion, it returns an error.

## See also

- Working with multiple currencies

[Working with multiple currencies](/connect/currencies)

- Statement descriptors with Connect

[Statement descriptors with Connect](/connect/statement-descriptors)

- Understanding Connect account balances

[Understanding Connect account balances](/connect/account-balances)
