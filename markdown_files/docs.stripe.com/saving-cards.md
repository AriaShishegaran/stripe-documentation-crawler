htmlSaving cards with the Charges API | Stripe Documentation[Skip to content](#main-content)Save a card[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsaving-cards)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsaving-cards)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)[Older APIs](/docs/payments/older-apis)[Charges](/docs/payments/charges-api)# Saving cards with the Charges API

Learn how to save and update card details to charge customers later.Legacy APIThe content of this section refers to a Legacy feature. Use the PaymentIntents API instead.

The Charges API doesn’t support the following features, many of which are required for credit card compliance:

- Merchants in India
- [Bank requests for card authentication](/payments/cards/overview)
- [Strong Customer Authentication](/strong-customer-authentication)

When you collect a customer’s payment information, a Stripe token is created. This token can only be used once, but that doesn’t mean you have to request your customer’s card details for every payment.

Stripe provides a Customer object so you can save this—and other—information for later use. You can use Customer objects for creating subscriptions or future one-off charges.

## Saving credit card details for later

### Saving cards with Payment Intents?

This page covers saving cards with the Charges API. To avoid an increase in declined payments due to SCA, save and reuse cards with Stripe’s SCA-ready payments APIs.

To make a card available for later charging, including subscriptions, create a new Customer instead of a Charge by providing their email address and tokenized card information.

Be certain to store the customer ID on your side for later use. You can subsequently charge that customer by passing the customer ID—instead of a card representation—in the charge request.

Command Line[curl](#)`# Create a Customer:
curl https://api.stripe.com/v1/customers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d source=tok_mastercard \
  -d email="paying.user@example.com"

# Charge the Customer instead of the card:
curl https://api.stripe.com/v1/charges \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d amount=1000 \
  -d currency=usd \
  -d customer=cus_7sqFSKcBzzYEAf

# YOUR CODE: Save the customer ID and other info in a database for later.

# When it's time to charge the customer again, retrieve the customer ID.
curl https://api.stripe.com/v1/charges \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d amount=1500 \
  -d currency=usd \
  -d customer=cus_7sqFSKcBzzYEAf`Charges using saved card details can be customized in the same ways as one-time charges.

NoteStripe typically validates card information when it is saved. For more details on when this happens, see Check if a card is valid without a charge.  As a result of this process, customers may see a temporary authorization for a small charge in their local currency on their statement. This doesn’t guarantee that any future charges succeed (for example, the card no longer has sufficient funds, is reported lost or stolen, or if the account is closed). This process also updates the results of any checks, including traditional bank checks by Radar (for example, CVC or postal code), that may have been performed.

## Automatic card updates

Saved payment method details can continue to work even if the issuing bank replaces the physical card. Stripe works with card networks and automatically attempts to update saved card details whenever a customer receives a new card (for example, replacing an expired card or one that was reported lost or stolen). This allows your customers to continue using your service without interruption and reduces the need for you to collect new card details whenever a card is replaced.

Automatic card updates require card issuers to participate with the network and provide this information. It is widely supported in the United States, allowing Stripe to automatically update most American Express, Visa, Mastercard, and Discover cards issued there. International support varies from country to country. It isn’t possible to identify cards that support automatic updates.

You can listen for Stripe webhooks to learn of card update activity:

- The`payment_method.updated`event notifies you of updates to a card through an API call
- The`payment_method.automatically_updated`event notifies you of automatic card updates from the network

These events include the card’s new expiration date and last four digits, so you can update your own records as needed.

## Changing the default payment method

### Updating a stored card

Beyond replacing the payment method entirely, you can only update a saved card’s billing address or expiration date.

Although many of the cards you save can be automatically updated, you should still adopt a process that allows customers to update or replace the cards on file (for example, a customer wants to change the card being billed or their card can’t be automatically updated). The end of the process requires an update customer call, providing a new token for the source parameter.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers/cus_V9T7vofUbZMqpv \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d source=tok_visa`This sets the new card as the default payment method for future payments. It also deletes the previously saved card.

## Multiple payment methods

Customers can also store multiple payment methods. The first one saved to a customer is set as the default_source. This is used for subscription payments and whenever a charge request is made with just a customer ID.

You can manage the payment methods saved to a customer (for example, create or remove cards) and you can update the customer to change default_source to another stored payment method at any time.

## See also

- [Guide to Payment Methods](https://stripe.com/payments/payment-methods-guide)
- [Creating Charges](/payments/charges-api)
- [Billing](/billing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Saving credit card details for later](#saving-credit-card-details-for-later)[Automatic card updates](#automatic-card-updates)[Changing the default payment method](#changing-default-payment-method)[Multiple payment methods](#multiple-payment-methods)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`