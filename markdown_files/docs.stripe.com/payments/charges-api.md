htmlCard payments on the Charges API | Stripe Documentation[Skip to content](#main-content)Charges[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcharges-api)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Fcharges-api)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)[Older APIs](/docs/payments/older-apis)# Card payments on the Charges APIDeprecated

Learn how to charge, save, and authenticate cards with Stripe's legacy APIs.Legacy APIThe content of this section refers to a Legacy feature. Use the PaymentIntents API instead.

The Charges API doesn’t support the following features, many of which are required for credit card compliance:

- Merchants in India
- [Bank requests for card authentication](/payments/cards/overview)
- [Strong Customer Authentication](/strong-customer-authentication)

The Charges and Tokens APIs are legacy APIs used in older Stripe integrations to accept debit and credit card payments. Use PaymentIntents for new integrations.

The Charges API limits your ability to take advantage of Stripe features. To get the latest features, use Stripe Checkout or migrate to the Payment Intents API.

## Payment flow

In most cases, the PaymentIntents API offers more flexibility and integration options.

Charges APIPayment Intents API1. Collect the customer’s payment information in the browser with Elements.
2. Tokenize the payment information with Stripe.js.
3. Perform a request to send the token to your server.
4. Use the token to create a charge on your server with the desired amount and currency.
5. Fulfill the customer’s order if payment is successful.

1. Create a PaymentIntent on your server with the desired amount and currency.
2. Send the PaymentIntent’s client secret to the client side.
3. Collect the customer’s payment information in the browser with Elements.
4. Use Stripe.js or the mobile SDKs to handle[3D Secure](/payments/3d-secure/authentication-flow#three-ds-radar)and complete the payment on the client.
5. Use webhooks to fulfill the customer’s order if the payment is successful.

## Refunds

To refund a payment via the API, create a Refund and provide the ID of the charge to be refunded.

Command Line[curl](#)`curl https://api.stripe.com/v1/refunds \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d charge={{CHARGE_ID}}`To refund part of a payment, provide an amount parameter, as an integer in cents (or the charge currency’s smallest currency unit).

Command Line[curl](#)`curl https://api.stripe.com/v1/refunds \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d charge={{CHARGE_ID}} \
  -d amount=1000`## Apple Pay

When your customer approves the payment, your app receives a PKPayment instance containing their encrypted card details by implementing the PKPaymentAuthorizationViewControllerDelegate methods.

1. Use the[createTokenWithPayment](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPAPIClient.html#/c:@CM@StripePayments@StripeCore@objc(cs)STPAPIClient(im)createTokenWithPayment:completion:)SDK method to turn the`PKPayment`into a Stripe`Token`
2. Use this`Token`to[create a charge](/payments/accept-a-payment-charges#ios-create-charge).

CheckoutViewController.swift[Swift](#)`extension CheckoutViewController: PKPaymentAuthorizationViewControllerDelegate {

    func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didAuthorizePayment payment: PKPayment, handler: @escaping (PKPaymentAuthorizationResult) -> Void) {
        // Convert the PKPayment into a Token
        STPAPIClient.shared.createToken(withPayment: payment) { token, error in
              guard let token = token else {
                  // Handle the error
                  return
              }
            let tokenID = token.tokenId
            // Send the token identifier to your server to create a Charge...
            // If the server responds successfully, set self.paymentSucceeded to YES
        }
    }

    func paymentAuthorizationViewControllerDidFinish(_ controller: PKPaymentAuthorizationViewController) {`See all 26 lines## Dynamic statement descriptor

By default, your Stripe account’s statement descriptor appears on customer statements whenever you charge their card. Additionally, you can set the statement descriptor dynamically on every charge request with the statement_descriptor argument on the Charge object.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "amount"=999 \
  -d "currency"="usd" \
  -d "description"="Example charge" \
  -d "source"="tok_visa" \
  -d "statement_descriptor"="Custom descriptor"`Statement descriptors are limited to 22 characters, can’t use the special characters <, >, ', ", or *, and must not consist solely of numbers.

When setting the statement descriptor dynamically on credit and debit card charges, the dynamic portion is appended to the settlement merchant’s statement descriptor (separated by an * and an empty space). For example, a statement descriptor for a business, named FreeCookies, that includes the kind of cookie purchased might look like FREECOOKIES* SUGAR.

The * and empty space count towards the 22 character limit and Stripe automatically allots 10 characters for the dynamic statement descriptor. This means that the settlement merchant’s descriptor might be truncated if it’s longer than 10 characters (assuming the dynamic statement descriptor is also greater than 10 characters). If the dynamic statement descriptor is also greater than 10 characters, both descriptors are truncated at 10 characters.

If you’re having issues with the character limits, you can set a shortened descriptor in the Stripe Dashboard to shorten the settlement merchant’s descriptor. This allows more room for the dynamic statement descriptor. The shortened descriptor:

- Replaces the settlement merchant’s statement descriptor when using dynamic descriptors.
- Can be between 2 and 10 characters.

NoteIf your account’s statement descriptor is longer than 10 characters, set a shortened descriptor in the Dashboard or use statement_descriptor_prefix. This prevents your statement descriptor from being truncated in unpredictable ways.

If you’re not sure what the statement descriptors look like when they’re combined, you can check them in the Stripe Dashboard.

## Storing information in metadata

### Using Payment Intents

If using the Payment Intents API, only retrieve and update the metadata and description fields on the Payment Intent object. If using both the Payment Intent and Charge objects, you’re not guaranteed to see consistent values for these fields.

Stripe supports adding metadata to the most common requests you make, such as processing charges. Metadata isn’t shown to customers or factored into whether or not a charge is declined or blocked by our fraud prevention system.

Through metadata, you can associate other information—meaningful to you—with Stripe activity. Any metadata you include is viewable in the Dashboard (for example, when looking at the page for an individual charge), and is also available in common reports and exports. As an example, your store’s order ID can be attached to the charge used to pay for that order. Doing so allows you, your accountant, or your finance team to easily reconcile charges in Stripe to orders in your system.

If you are using Radar, consider passing any additional customer information and order information as metadata. By doing so, you can write Radar rules using metadata attributes and have more information about the payment available within the Dashboard which can expedite your review process.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "amount"=999 \
  -d "currency"="usd" \
  -d "description"="Example charge" \
  -d "source"="tok_visa" \
  -d "metadata[order_id]"=6735`CautionDon’t store any sensitive information (personally identifiable information, card details, and so on) as metadata or in the charge’s description parameter.

## Declines

If you want your integration to respond to payment failures automatically, you can access a charge’s outcome in two ways.

- [Handle the API error](/api#error_handling)that’s returned when a payment fails. For blocked and card issuer-declined payments, the error includes the charge’s ID, which you can then use to[retrieve](/api#retrieve_charge)the charge.
- Use[webhooks](/webhooks)to monitor status updates. For example, the`charge.failed`event triggers when a payment is unsuccessful.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Payment flow](#payment-flow)[Refunds](#refunds)[Apple Pay](#apple-pay)[Dynamic statement descriptor](#dynamic-statement-descriptor)[Storing information in metadata](#storing-information-in-metadata)[Declines](#declines)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`