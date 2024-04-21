htmlReconciliation | Stripe Documentation[Skip to content](#main-content)Reconciliation[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcustomer-balance%2Freconciliation)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcustomer-balance%2Freconciliation)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)
[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Add payment methods](/docs/payments/payment-methods/overview)[Bank transfers](/docs/payments/bank-transfers)[Customer balance](/docs/payments/customer-balance)# Reconciliation

Learn about how Stripe reconciles the customer balance to payments and invoices.Stripe offers the automatic or manual reconciliation behavior for funds in the cash balance.

By default, Stripe applies the automatic reconciliation mode to the cash balance of all of your customers. You can use the Bank Transfers reconciliation settings to change the reconciliation behavior for everyone.

![Bank Transfer reconciliation settings](https://b.stripecdn.com/docs-statics-srv/assets/bank-transfer-reconciliation-settings.930a07d8937809fddf187138649fc419.png)

Bank Transfer reconciliation settings

## Override reconciliation behavior

You can use the Dashboard or API to override, for a specific customer, the Bank Transfers reconciliation settings.

To override a customer’s reconciliation behavior in the Dashboard:

1. Select the customer, then findCash Balancein thePayment methodssection.
2. Expand the overflow menu () next to the cash balance details.
3. From the expanded options, selectChange reconciliation mode. This displays a modal that allows you to change the reconciliation behavior for the customer.

![Cash Balance section on the Customer page](https://b.stripecdn.com/docs-statics-srv/assets/cash-balance-settings.fbc9cb0a50beaf42ab1ff6baab7dc09f.png)

The Cash Balance section on the Customer page

To override a customer’s reconciliation behavior using the API, set the customer’s reconciliation mode to manual.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers/{{CUSTOMER_ID}} \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "cash_balance[settings][reconciliation_mode]"=manual`To point the reconciliation mode for an overridden customer back to the user’s default, you can do so in the Dashboard. You can also use the API to set the reconciliation mode on the customer to merchant_default.

## Automatic cash balance reconciliation

USUKEUJPMXBy default, Stripe automatically applies any available cash balance to PaymentIntents and invoices that are awaiting funding. A PaymentIntent is awaiting funding if it’s incomplete. An invoice is awaiting funding if it’s open and either hasn’t passed its due date or became overdue within the last 30 days.

Stripe applies funds in the following order:

1. Stripe initially attempts to match a bank transfer reference with a single invoice that has a matching[invoice number](/api/invoices/object#invoice_object-number).
2. If the first attempt is unsuccessful, Stripe attempts to match the bank transfer reference with a single incomplete PaymentIntent that has a matching reference stored in the PaymentIntent’s[display_bank_transfer_instructions](/api/payment_intents/object#payment_intent_object-next_action-display_bank_transfer_instructions-reference)field.
3. If Stripe doesn’t receive a bank transfer reference or can’t match the reference with a single invoice or PaymentIntent, we search for a group of between one and five invoices and PaymentIntents awaiting the exact amount the user sent. For multiple valid combinations, Stripe prioritizes as follows:  - We filter for the smallest group. If there’s two groups of invoices or PaymentIntents that can both receive the funds, we select the one with fewer objects.
  - If there are multiple smallest-sized groups, we select the smallest group that contains the most invoices.
  - If multiple groups contain the same number of invoices, we select the group with the oldest PaymentIntents.


4. If we can’t find a group that equals the exact funds available, we fund as many invoices that can be fully funded, starting with the oldest finalized ones first.
5. If any funds remain, we apply the remaining funds to incomplete PaymentIntents, starting with the oldest ones first.

## Manual cash balance reconciliation

When manual reconciliation is enabled on a customer, Stripe does not automatically apply any funds from the customer balance.

You can apply funds from the customer balance manually using either the API or the Dashboard.

For both the API and the Dashboard, you can apply funds to an incomplete or partially funded PaymentIntent, or an open Invoice. You can also fund Invoices that are still open but marked overdue with this method.

In the Dashboard, you can apply funds to a PaymentIntent on the Payments page or on the page for the individual payment.

To fund a PaymentIntent from the Payments page, find the payment you want to fund, select the overflow menu (), then click Fund from cash balance.

![The overflow menu for a single Payment on the Stripe Dashboard Payments page](https://b.stripecdn.com/docs-statics-srv/assets/fund-from-cash-balance-payments-list.16be7818811602d966d2ce4f1aadbc0f.png)

To fund a PaymentIntent from the page for the individual payment, click the Fund from cash balance button.

In both cases, selecting the Fund from cash balance button prompts you to confirm the payment. This button doesn’t appear on either page if the customer doesn’t have any funds available on their cash balance.

In order to apply funds to an invoice, navigate to the Invoice page, click the Charge customer button, and then select Cash Balance as the payment method.

Invoices can only be fully funded using the Dashboard, so this option doesn’t appear if the customer doesn’t have sufficient funds on their cash balance to fully pay the invoice.

In order to apply funds using the API:

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents/{{PAYMENT_INTENT_ID}}/apply_customer_balance \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1500 \
  -d currency=usd`The amount is optional. When omitted, the amount defaults to the remaining amount requested on the PaymentIntent.

The following code is an example of a full pass of manual reconciliation. You receive the cash_balance.funds_available webhook, find PaymentIntents that are awaiting funding, and use the funds available to reconcile the open PaymentIntents.

The object sent in the cash_balance.funds_available message always contains a representation of the customer’s full cash balance, regardless of the event triggering the webhook. This means that the cash balance might contain funds that were previously added to the customer’s cash balance, not just those added immediately before the triggering event.

[Ruby](#)`require 'stripe'
require 'sinatra'

Stripe.api_key = 'sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz'

post '/webhook' do
  sig_header = request.env['HTTP_STRIPE_SIGNATURE']
  endpoint_secret = ENV['ENDPOINT_SECRET']
  payload = request.body.read

  begin
    event = Stripe::Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  rescue JSON::ParserError => e
    status 400
    return
  rescue Stripe::SignatureVerificationError => e
    status 400
    return
  end

  case event['type']
    when 'cash_balance.funds_available'
    # The cash_balance.funds_available webhook always contains a complete cash balance,
    # regardless of the event triggering the webhook.
    #
    # This means that the cash balance might contain funds that were previously added to the customer's cash balance,
    # not just those added immediately before the triggering event.
    cash_balance = event['data']['object']
    customer_id = cash_balance['customer']

    # Cash balances might contain multiple currencies.
    currencies_available = cash_balance['available'].keys

    # Getting all payment intents for a customer.
    customer_payment_intents = Stripe::PaymentIntent.list({customer: customer_id})['data']

    # We can order the funding of PaymentIntents in whichever order we like - here we'd
    # like to pay the oldest first.
    customer_payment_intents = customer_payment_intents.sort_by { |payment_intent| payment_intent['created'] }

    # We allow a customer's balance to include multiple currencies.
    #
    # If a customer has balances in multiple currencies, we only allow reconciliation using the balance that matches
    # the currency of the PaymentIntent.
    intents_for_currency = {}
    currencies_available.each do |currency|
      intents_for_currency[currency] = customer_payment_intents.select do |payment_intent|
        allowed_payment_methods = payment_intent['payment_method_types']
        awaiting_further_payment = ['requires_payment_method', 'requires_action'].include? payment_intent['status']
        payment_intent['currency'] == currency.to_s and awaiting_further_payment and allowed_payment_methods.include? 'customer_balance'
      end
    end

    # Here we attempt to fund every fundable PaymentIntent for as long as there are funds available
    # in the customer's Cash Balance for the correct currency. Each time we attempt to fund a
    # PaymentIntent, we repoll the Cash Balance to make sure that we still have funds available for
    # the next PaymentIntent.
    currencies_available.each do |currency|
      payment_intents = intents_for_currency[currency]
      payment_intents.each do |payment_intent|
        if cash_balance['available'][currency] == 0
          break
        end
        Stripe::PaymentIntent.apply_customer_balance(payment_intent['id'])
        cash_balance = Stripe::Customer.retrieve_cash_balance(customer_id, nil)
      end
    end
  end
end`## Unreconciled cash balance funds

Sometimes funds in the customer balance remain unreconciled—for example, when a customer sends too much money and you haven’t created any more PaymentIntents or Invoices for that customer.

To reconcile outstanding funds in the customer cash balance, you can either create a new PaymentIntent or invoice to accept a payment, or return the funds to the customer.

CautionYou’re responsible for making sure that you reconcile customer cash balances promptly and accurately. Reconcile outstanding customer balances quickly, rather than leaving them in your account for an extended period.

Stripe periodically sends a reminder email when you have unreconciled balances in your account to make sure that you can review these unreconciled funds. If a customer balance remains unreconciled for 75 days, Stripe automatically attempts to return the funds to the customer’s bank account. Where Stripe doesn’t have the customer’s account information, Stripe might reach out to the customer directly to initiate a refund of unreconciled funds. If Stripe is unable to determine the customer’s account information, we return the funds to your Stripe account. Coordinate directly with the customer to make sure they receive the returned funds.

You can see the full list of customers who have unreconciled cash balances and the date that we’ll return them to the customer in your Dashboard.

## Credit balance

Credit balance is handled differently from cash balance. Customer credit balance is an Invoices-only feature which represents liability between you and the customer. When an invoice is finalized, the customer’s credit balance is applied to the invoice, decreasing the amount due.

For more information on credit balances, see Customer Credit Balance.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Override reconciliation behavior](#cash-override-reconciliation-behavior)[Automatic cash balance reconciliation](#cash-automatic-reconciliation)[Manual cash balance reconciliation](#cash-manual-reconciliation)[Unreconciled cash balance funds](#cash-unreconciled-funds)[Credit balance](#credit-balance)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`