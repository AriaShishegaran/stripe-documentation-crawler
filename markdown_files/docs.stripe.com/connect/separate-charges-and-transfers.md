htmlCreate separate charges and transfers | Stripe Documentation[Skip to content](#main-content)Separate charges and transfers[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fseparate-charges-and-transfers)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fseparate-charges-and-transfers)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)[Create a charge](/docs/connect/charges)# Create separate charges and transfers

Create charges on your platform account and transfer funds to multiple connected accounts.Create separate charges and transfers to transfer funds from one payment to multiple connected accounts, or when a specific user isn’t known at the time of the payment. The charge on your platform account is decoupled from the transfer(s) to your connected accounts. With this charge type:

- You create a charge on your platform’s account and also transfer funds to your connected accounts. The payment appears as a charge on your account and there are also transfers to connected accounts (amount determined by you), which are withdrawn from your account balance.
- You can transfer funds to multiple connected accounts.
- Your account balance is debited for the cost of the Stripe fees, refunds, and chargebacks.

This charge type is most optimal for marketplaces that need to split payments between multiple parties, such as DoorDash, a restaurant delivery platform.

Stripe supports separate charges and transfers in the following regions:

AustraliaAustriaBelgiumBrazilBulgariaCanadaCroatiaCyprusCzech RepublicDenmarkEstoniaFinlandFranceGermanyGreeceHungaryIrelandItalyJapanLatviaLiechtensteinLithuaniaLuxembourgMalaysiaMaltaMexicoNetherlandsNew ZealandNorwayPolandPortugalRomaniaSingaporeSlovakiaSloveniaSpainSwedenSwitzerlandUnited KingdomUnited StatesIn most scenarios, your platform and any connected account must be in the same region. Attempting to transfer funds across a disallowed border returns an error. For information about cross-region support, see cross-border transfers. You must only use transfers in combination with the permitted use cases for charges, tops-ups and fees.

WebiOSAndroidReact NativeStripe-hosted pageEmbedded formCustom flowRedirect to a Stripe-hosted payment page using Stripe Checkout. See how this integration compares to Stripe’s other integration types.

[](https://checkout.stripe.dev/)### Integration effort

Low code### Integration type

Redirect to Stripe-hosted payment page

### UI customization

[Limited customization](#)Try it out

[Set up StripeServer-side](#set-up-stripe)First, register for a Stripe account.

Use our official libraries to access the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Create a Checkout SessionClient-sideServer-side](#create-checkout-session)A Checkout Session controls what your customer sees in the payment form such as line items, the order amount and currency, and acceptable payment methods. Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

checkout.html`<html>
  <head>
    <title>Checkout</title>
  </head>
  <body>
    <form action="/create-checkout-session" method="POST">
      <button type="submit">Checkout</button>
    </form>
  </body>
</html>`On your server, create a Checkout Session and redirect your customer to the URL returned in the response.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price_data][currency]"=usd \
  -d "line_items[0][price_data][product_data][name]"="Restaurant delivery service" \
  -d "line_items[0][price_data][unit_amount]"=10000 \
  -d "line_items[0][quantity]"=1 \
  -d "payment_intent_data[transfer_group]"=ORDER100 \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success?session_id={CHECKOUT_SESSION_ID}"`- `line_items`- This attribute represents the items the customer is purchasing. The items are displayed in the Stripe-hosted checkout page.
- `payment_intent_data[transfer_group]`- Use a unique string as the`transfer_group`to identify objects that are associated with each other. When Stripe automatically creates a charge for a PaymentIntent with a`transfer_group`value, it assigns the same value to the charge’s`transfer_group`.
- `success_url`- Stripe redirects the customer to the success URL after they complete a payment and replaces the`{CHECKOUT_SESSION_ID}`string with the Checkout Session ID. Use this to retrieve the Checkout Session and inspect the status to decide what to show your customer. You can also append your own query parameters, which persist through the redirect process. See[customize redirect behavior with a Stripe-hosted page](/payments/checkout/custom-success-page)for more information.

[Handle post-payment eventsServer-side](#handle-post-payment-events)Stripe sends a checkout.session.completed event when the payment completes. Use a webhook to receive these events and run actions, like sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes. Some payment methods also take 2-14 days for payment confirmation. Setting up your integration to listen for asynchronous events enables you to accept multiple payment methods with a single integration.

Stripe recommends handling all of the following events when collecting payments with Checkout:

EventDescriptionNext steps[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)The customer has successfully authorized the payment by submitting the Checkout form.Wait for the payment to succeed or fail.[checkout.session.async_payment_succeeded](/api/events/types#event_types-checkout.session.async_payment_succeeded)The customer’s payment succeeded.Fulfill the purchased goods or services.[checkout.session.async_payment_failed](/api/events/types#event_types-checkout.session.async_payment_failed)The payment was declined, or failed for some other reason.Contact the customer through email and request that they place a new order.These events all include the Checkout Session object. After the payment succeeds, the underlying PaymentIntent status changes from processing to succeeded or a failure status.

[Create a TransferServer-side](#create-transfer)On your server, send funds from your account to a connected account by creating a Transfer and specifying the transfer_group used.

Command Line[curl](#)`curl https://api.stripe.com/v1/transfers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=7000 \
  -d currency=usd \
  -d destination={{CONNECTED_ACCOUNT_ID}} \
  -d transfer_group=ORDER100`Transfer and charge amounts don’t have to match. You can split a single charge between multiple transfers or include multiple charges in a single transfer. The following example creates an additional transfer associated with the same transfer_group.

Command Line[curl](#)`curl https://api.stripe.com/v1/transfers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=2000 \
  -d currency=usd \
  -d destination={{OTHER_CONNECTED_ACCOUNT_ID}} \
  -d transfer_group=ORDER100`[Test the integration](#test-the-integration)CardsWalletsBank redirectsBank debitsVouchersCard numberScenarioHow to test4242424242424242The card payment succeeds and doesn’t require authentication.Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.4000002500003155The card payment requires[authentication](/strong-customer-authentication).Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.4000000000009995The card is declined with a decline code like`insufficient_funds`.Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.6205500000000000004The UnionPay card has a variable length of 13-19 digits.Fill out the credit card form using the credit card number with any expiration, CVC, and postal code.See Testing for additional information to test your integration.

[OptionalEnable additional payment methods](#enable-payment-methods)## Specify the settlement merchant

The settlement merchant is dependent on the capabilities set on an account and how a charge is created. The settlement merchant determines whose information is used to make the charge. This includes the statement descriptor (either the platform’s or the connected account’s) that’s displayed on the customer’s credit card or bank statement for that charge.

Specifying the settlement merchant allows you to be more explicit about who to create charges for. For example, some platforms prefer to be the settlement merchant because the end customer interacts directly with their platform (such as on-demand platforms). However, some platforms have connected accounts that interact directly with end customers instead (such as a storefront on an e-commerce platform). In these scenarios, it might make more sense for the connected account to be the settlement merchant.

You can set the on_behalf_of parameter to the ID of a connected account to make that account the settlement merchant for the payment. When using on_behalf_of:

- Chargessettlein the connected account’s country andsettlement currency.
- The fee structure for the connected account’s country is used.
- The connected account’s statement descriptor is displayed on the customer’s credit card statement.
- If the connected account is in a different country than the platform, the connected account’s address and phone number are displayed on the customer’s credit card statement.
- The number of days that a[pending balance](/connect/account-balances)is held before being paid out depends on the[delay_days](/api/accounts/create#create_account-settings-payouts-schedule-delay_days)setting on the connected account.

If on_behalf_of is omitted, the platform is the business of record for the payment.

CautionThe on_behalf_of parameter is supported only for connected accounts with the card_payments capability. Accounts under the recipient service agreement can’t request card_payments.

Command Line[curl](#)`curl https://api.stripe.com/v1/checkout/sessions \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "line_items[0][price_data][currency]"=usd \
  -d "line_items[0][price_data][product_data][name]"="Restaurant delivery service" \
  -d "line_items[0][price_data][unit_amount]"=10000 \
  -d "line_items[0][quantity]"=1 \
  -d "payment_intent_data[on_behalf_of]"={{CONNECTED_ACCOUNT_ID}} \
  -d "payment_intent_data[transfer_group]"=ORDER100 \
  -d mode=payment \
  --data-urlencode success_url="https://example.com/success"`## Collect fees

When using separate charges and transfers, the platform can collect fees on a charge by reducing the amount it transfers to the destination accounts. For example, consider a restaurant delivery service transaction that involves payments to the restaurant and to the driver:

1. The customer pays a 100 USD charge.
2. Stripe collects a 3.20 USD fee and adds the remaining 96.80 USD to the platform account’s pending balance.
3. The platform transfers 70 USD to the restaurant’s connected account and 20 USD to the driver’s connected account.
4. A platform fee of 6.80 USD remains in the platform account.

![How a charge is divided into fees for the platform account and transfers for the connected accounts](https://b.stripecdn.com/docs-statics-srv/assets/charges_transfers.c54b814c7e6f88993bf259c8a53f03e8.png)

To learn about processing payments in multiple currencies with Connect, see working with multiple currencies.

## Transfer availability

The default behavior is to transfer funds from the platform account’s available balance. Attempting a transfer that exceeds the available balance fails with an error. To avoid this problem, when creating a transfer, tie it to an existing charge by specifying the charge ID as the source_transaction parameter. With a source_transaction, the transfer request returns success regardless of your available balance. However, the funds don’t become available in the destination account until the funds from the associated charge are available to transfer from the platform account.

If the source charge has a transfer_group value, Stripe assigns the same value to the transfer’s transfer_group. If it doesn’t, then Stripe generates a string in the format group_ plus the associated PaymentIntent ID, for example: group_pi_2NHDDD589O8KAxCG0179Du2s. It assigns that string as the transfer_group for both the charge and the transfer.

NoteYou must specify the source_transaction when you create a transfer. You can’t update that attribute later.

Command Line[curl](#)`curl https://api.stripe.com/v1/transfers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=7000 \
  -d currency=usd \
  -d source_transaction={{CHARGE_ID}} \
  -d destination={{CONNECTED_ACCOUNT_ID}}`You can get the charge ID from the PaymentIntent:

- Get the PaymentIntent’s[latest_charge attribute](/api/payment_intents/object#payment_intent_object-latest_charge). This attribute is the ID of the most recent charge associated with the PaymentIntent.
- [Request a list of charges](/api/charges/list), specifying the`payment_intent`in the request. This method returns full data for all charges associated with the PaymentIntent.

When using this parameter:

- The amount of the transfer must not exceed the amount of the source charge
- You can create multiple transfers with the same`source_transaction`, as long as the sum of the transfers doesn’t exceed the source charge
- The transfer takes on the pending status of the associated charge: if the funds from the charge become available in N days, the payment that the destination Stripe account receives from the transfer also becomes available in N days
- Stripe automatically creates a`transfer_group`for you
- The currency of the balance transaction associated with the charge must match the currency of the transfer

Asynchronous payment methods, like ACH, can fail after a subsequent transfer request is made. For these payments, avoid using source_transaction. Instead, wait until a charge.succeeded event is triggered before transferring the funds. If you have to use source_transaction with these payments, you must implement functionality to manage payment failures.

When a payment used as a source_transaction fails, funds from your platform’s account balance are transferred to the connected account to cover the payment. To recover these funds, reverse the transfer associated with the failed source_transaction.

## Transfer options

You can assign any value to the transfer_group string, but it must represent a single business action. You can also make a transfer with neither an associated charge nor a transfer_group—for example, when you must pay a provider but there’s no associated customer payment.

NoteThe transfer_group only identifies associated objects. It doesn’t affect any standard functionality. To prevent a transfer from executing before the funds from the associated charge are available, use the transfer’s source_transaction attribute.

Transfer and charge amounts don’t have to match. You can split a single charge between multiple transfers or include multiple charges in a single transfer. You can perform transfers and charges in any order.

By default, a transfer request fails when the amount exceeds the platform’s available account balance. You can instead validate the transfer amount against its associated charge by specifying that charge as the transfer’s source_transaction. In that case, the transfer request automatically succeeds but isn’t executed until the funds from that charge are available in the platform account.

NoteIf you use separate charges and transfers, take that into account when planning your payout schedule. Automatic payouts can interfere with transfers that don’t have a defined source_transaction.

## Issue refunds

You can refund charges created on your platform using its secret key. However, refunding a charge has no impact on any associated transfers. It’s up to your platform to reconcile any amount owed back to it by reducing subsequent transfer amounts or by reversing transfers.

Command Line[curl](#)`curl https://api.stripe.com/v1/refunds \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d charge={{CHARGE_ID}}`## Reverse transfers

Connect supports the ability to reverse transfers made to connected accounts, either entirely or partially (by setting an amount value):

Command Line[curl](#)`curl https://api.stripe.com/v1/transfers/{{TRANSFER_ID}}/reversals \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=7000`Transfer reversals add the specified (or entire) amount back to the platform’s available balance, reducing the connected account’s available balance accordingly. It is only possible to reverse a transfer if the connected account’s available balance is greater than the reversal amount or has connected reserves enabled.

If the transfer reversal requires a currency conversion, and the reversal amount would result in a zero balance after the conversion, it returns an error.

## See also

- [Working with multiple currencies](/connect/currencies)
- [Statement descriptors with Connect](/connect/statement-descriptors)
- [Understanding Connect account balances](/connect/account-balances)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Stripe](#set-up-stripe)[Create a Checkout Session](#create-checkout-session)[Handle post-payment events](#handle-post-payment-events)[Create a Transfer](#create-transfer)[Test the integration](#test-the-integration)[Specify the settlement merchant](#settlement-merchant)[Collect fees](#collect-fees)[Transfer availability](#transfer-availability)[Transfer options](#transfer-options)[Issue refunds](#issue-refunds)[Reverse transfers](#reverse-transfers)[See also](#see-also)Products Used[Connect](/connect)[Checkout](/payments/checkout)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`