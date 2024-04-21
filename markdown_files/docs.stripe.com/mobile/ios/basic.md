htmliOS basic integration | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fmobile%2Fios%2Fbasic)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fmobile%2Fios%2Fbasic)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# iOS basic integrationDeprecated

Accept cards and Apple Pay with the iOS SDK's prebuilt UI.NoteWe created an improved payments UI for mobile apps with features such as additional payment methods and SwiftUI support. We recommend using it for your integration instead of this one.

If you want to migrate but are unable to, please let us know.

Use this integration if you want a prebuilt UI that:

- Accepts credit cards and Apple Pay
- Saves and displays cards for reuse
- Supports[limited customization](#theming)of fonts and colors
- Displays full-screen view controllers to collect payment details, shipping address, and shipping method:

![STPPaymentOptionsViewController](https://b.stripecdn.com/docs-statics-srv/assets/payment-options.2b2fc48bc62666a77af952501ae6e014.png)

STPPaymentOptionsViewController

![STPAddCardViewController](https://b.stripecdn.com/docs-statics-srv/assets/add-card-vc.b44c275bc80072cf98eb0658bb8f5c51.png)

STPAddCardViewController

![STPShippingAddressViewController](https://b.stripecdn.com/docs-statics-srv/assets/shipping-address.13f3a4bed7bcf89f36dd74e43b78986f.png)

STPShippingAddressViewController

These view controllers are also available to use individually—see the steps below for more details. This integration requires both server and client-side steps to implement.

NoteCheck out the example Basic Integration app and backend for a full implementation of this guide.

[Set up StripeClient-sideServer-side](#setup-ios)First, you need a Stripe account. Register now.

### Server-side

This integration requires endpoints on your server that talk to the Stripe API. Use our official libraries for access to the Stripe API from your server:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`### Client-side

The Stripe iOS SDK is open source, fully documented, and compatible with apps supporting iOS 13 or above.

Swift Package ManagerCocoaPodsCarthageManual FrameworkTo install the SDK, follow these steps:

1. In Xcode, selectFile>Add Packages…and enter`https://github.com/stripe/stripe-ios-spm`as the repository URL.
2. Select the latest version number from our[releases page](https://github.com/stripe/stripe-ios/releases).
3. Add theStripeproduct to the[target of your app](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app).

NoteFor details on the latest SDK release and past versions, see the Releases page on GitHub. To receive notifications when a new release is published, watch releases for the repository.

Configure the SDK with your Stripe publishable key on app start. This enables your app to make requests to the Stripe API.

AppDelegate.swift[Swift](#)`import UIKit
import Stripe

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        StripeAPI.defaultPublishableKey = "pk_test_VOOyyYjgzqdm8I3SrBqmh9qY"
        // do any other necessary launch configuration
        return true
    }
}`NoteUse your test mode keys while you test and develop, and your live mode keys when you publish your app.

[Set up an ephemeral keyClient-sideServer-side](#ephemeral-key)In order for the SDK to save and retrieve credit cards for later use, create a single Stripe Customer object for each of your users. When you create a new user or account on your server, create a corresponding Customer object at the same time, even if you don’t collect payment information from your users when they sign up. This ensures that your application has a matching Customer for each user.

For security, the Customer API is not directly accessible from the client. Instead, your server provides the SDK with an ephemeral key—a short-lived API key with restricted access to the Customer API. You can think of an ephemeral key as a session, authorizing the SDK to retrieve and update a specific Customer object for the duration of the session.

### Server-side

To provide an ephemeral key to the SDK, you’ll need to expose a new API endpoint on your backend. This endpoint should create an ephemeral key for the current Stripe customer, and return the key’s unmodified response as JSON. When the SDK requests an ephemeral key, it will specify the version of the Stripe API that it expects the response to come from. Your endpoint must accept an api_version parameter, and use the specified API version when creating the ephemeral key. This ensures that the SDK always receives the correct ephemeral key response from your backend. Consult our Example Backend to see this in practice.

Command Line[curl](#)`curl https://api.stripe.com/v1/ephemeral_keys \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "customer"="{{CUSTOMER_ID}}" \
  -H "Stripe-Version: {{API_VERSION}}"`### Client-side

In your app, conform to the STPCustomerEphemeralKeyProvider protocol by implementing its createCustomerKeyWithAPIVersion method. This method requests an ephemeral key from the endpoint you created on the backend.

When implementing this method, be sure to pass the apiVersion parameter along to your ephemeral keys endpoint. Consult the API client in our example app to see this in practice.

MyAPIClient.swift[Swift](#)[View full sample](https://github.com/stripe/stripe-ios/blob/21.4.0/Example/Basic%20Integration/Basic%20Integration/MyAPIClient.swift#L77-L101)`import Stripe

class MyAPIClient: NSObject, STPCustomerEphemeralKeyProvider {

    func createCustomerKey(withAPIVersion apiVersion: String, completion: @escaping STPJSONResponseCompletionBlock) {
        let url = self.baseURL.appendingPathComponent("ephemeral_keys")
        var urlComponents = URLComponents(url: url, resolvingAgainstBaseURL: false)!
        urlComponents.queryItems = [URLQueryItem(name: "api_version", value: apiVersion)]
        var request = URLRequest(url: urlComponents.url!)
        request.httpMethod = "POST"
        let task = URLSession.shared.dataTask(with: request, completionHandler: { (data, response, error) in
            guard let response = response as? HTTPURLResponse,
                response.statusCode == 200,
                let data = data,
                let json = ((try? JSONSerialization.jsonObject(with: data, options: []) as? [String : Any]) as [String : Any]??) else {
                completion(nil, error)
                return
            }
            completion(json, nil)
        })
        task.resume()
    }
}`[Set up an STPCustomerContextClient-side](#set-up-customer-context)Next, initialize an STPCustomerContext with the STPCustomerEphemeralKeyProvider you created in the previous step.

A CustomerSession talks to your backend to retrieve an ephemeral key for your Customer with its STPCustomerEphemeralKeyProvider, and uses that key to manage retrieving and updating the Customer’s payment methods on your behalf.

ViewController.swift[Swift](#)`// MyAPIClient implements STPCustomerEphemeralKeyProvider (see above)
let customerContext = STPCustomerContext(keyProvider: MyAPIClient())`To reduce load times, preload your customer’s information by initializing STPCustomerContext before they enter your payment flow.

If your current user logs out of the app and a new user logs in, create a new instance of STPCustomerContext or clear the cached customer using the provided clearCachedCustomer method. On your backend, create and return a new ephemeral key for the Customer object associated with the new user.

[Set up an STPPaymentContextClient-side](#initialize-payment-context)Once you’ve set up your customer context, you can use it to initialize STPPaymentContext, the core class of the integration. Conform a class to STPPaymentContextDelegate and assign it to the payment context’s delegate and hostViewController properties. We recommend using your app’s checkout screen UIViewController. In the next steps, you will implement the STPPaymentContext delegate methods.

You should also set the payment context’s paymentAmount property, which will be displayed to your user in the Apple Pay dialog (you can change this later, if the amount of the user’s purchase changes).

ViewController.swift[Swift](#)`init() {
    self.paymentContext = STPPaymentContext(customerContext: customerContext)
    super.init(nibName: nil, bundle: nil)
    self.paymentContext.delegate = self
    self.paymentContext.hostViewController = self
    self.paymentContext.paymentAmount = 5000 // This is in cents, that is, 50 USD
}`[Handle the user's payment methodClient-side](#handle-payment-method)In your checkout screen, add a button to let the customer enter or change their payment method. When tapped, use STPPaymentContext to push or present an STPPaymentOptionsViewController on the payment context’s hostViewController.

ViewController.swift[Swift](#)`// If you prefer a modal presentation
func choosePaymentButtonTapped() {
    self.paymentContext.presentPaymentOptionsViewController()
}

// If you prefer a navigation transition
func choosePaymentButtonTapped() {
    self.paymentContext.pushPaymentOptionsViewController()
}`![STPPaymentOptionsViewController](https://b.stripecdn.com/docs-statics-srv/assets/payment-options.2b2fc48bc62666a77af952501ae6e014.png)

STPPaymentOptionsViewController

![STPAddCardViewController](https://b.stripecdn.com/docs-statics-srv/assets/add-card-vc.b44c275bc80072cf98eb0658bb8f5c51.png)

STPAddCardViewController

STPPaymentOptionsViewController uses STPCustomerContext to display a Customer’s payment methods. If there are no stored payment methods or the Add New Card button is tapped, STPAddCardViewController is displayed. You can also initialize and display these view controllers without using STPPaymentContext.

### - paymentContextDidChange:

This STPPaymentContext delegate method triggers when the content of the payment context changes, like when the user selects a new payment method or enters shipping information. This is a good place to update your UI:

ViewController.swift[Swift](#)`func paymentContextDidChange(_ paymentContext: STPPaymentContext) {
    self.activityIndicator.animating = paymentContext.loading
    self.paymentButton.enabled = paymentContext.selectedPaymentOption != nil
    self.paymentLabel.text = paymentContext.selectedPaymentOption?.label
    self.paymentIcon.image = paymentContext.selectedPaymentOption?.image
}`[Handle the user's shipping infoClient-side](#handle-shipping-info)If your user needs to enter or change their shipping address and shipping method, STPPaymentContext can do this for you automatically. STPPaymentContext will save shipping info to the Stripe customer when your user updates their information, and automatically prefill the shipping view controller for future purchases. Note that you should not rely on the shipping information stored on the Stripe customer for order fulfillment, as your user may change this information if they make multiple purchases. We recommend adding shipping information when you create a PaymentIntent object (which can also help prevent fraud), or when saving it to your own database. When presenting the shipping view controller, you can specify whether you’d like it presented modally, or pushed onto a UINavigationController stack:

ViewController.swift[Swift](#)`// If you prefer a modal presentation
func shippingButtonTapped() {
    self.paymentContext.presentShippingViewController()
}

// If you prefer a navigation transition
func shippingButtonTapped() {
    self.paymentContext.pushShippingViewController()
}`This sets up and presents an STPShippingAddressViewController on the payment context’s hostViewController. Once the user enters a valid shipping address, they’re taken to an STPShippingMethodsViewController. After they select a shipping method, both view controllers are dismissed or popped off the hostViewController’s stack.

![STPShippingAddressViewController](https://b.stripecdn.com/docs-statics-srv/assets/shipping-address.13f3a4bed7bcf89f36dd74e43b78986f.png)

STPShippingAddressViewController

![STPShippingMethodsController](https://b.stripecdn.com/docs-statics-srv/assets/shipping-methods.ee65a7f2daf86eb501224bce0a8034ad.png)

STPShippingMethodsViewController

### - paymentContext:didUpdateShippingAddress:completion:

This method is called after your user enters a shipping address. Validate the returned address and determine the shipping methods available for that address.

If the address is valid, call the provided completion block with a status of STPShippingStatusValid, nil for the error argument, an array of shipping methods, and a selected shipping method. If you don’t need to collect a shipping method, pass nil for the shipping methods and selected shipping method. If the address is invalid, call the completion block with a status of STPShippingStatusInvalid, an error object describing the issue with the address, and nil for the shipping methods and selected shipping method. Note that providing an error object is optional—if you omit it, the user sees an alert with the message “Invalid Shipping Address.”

ViewController.swift[Swift](#)`func paymentContext(_ paymentContext: STPPaymentContext, didUpdateShippingAddress address: STPAddress, completion: @escaping STPShippingMethodsCompletionBlock) {
    let upsGround = PKShippingMethod()
    upsGround.amount = 0
    upsGround.label = "UPS Ground"
    upsGround.detail = "Arrives in 3-5 days"
    upsGround.identifier = "ups_ground"
    let fedEx = PKShippingMethod()
    fedEx.amount = 5.99
    fedEx.label = "FedEx"
    fedEx.detail = "Arrives tomorrow"
    fedEx.identifier = "fedex"

    if address.country == "US" {
        completion(.valid, nil, [upsGround, fedEx], upsGround)
    }
    else {
        completion(.invalid, nil, nil, nil)
    }
}`[Submit the paymentClient-sideServer-side](#submit-payment)When your user is ready to pay (for example, they tap the Buy button) call requestPayment on your payment context. It displays any required UI (such as the Apple Pay dialog) and calls the appropriate methods on its delegate as your user finishes their payment.

ViewController.swift[Swift](#)`func payButtonTapped() {
    self.paymentContext.requestPayment()
}`### - paymentContext:didCreatePaymentResult:completion:

This method is called when the customer has successfully selected a payment method. Submit the payment to Stripe using a Payment Intent. Stripe uses this payment object to track and handle all the states of the payment until the payment completes.

### Server-side

On your server, make an endpoint that creates a PaymentIntent with an amount and currency and returns its client secret to your client.

Always decide how much to charge on the server side, a trusted environment, as opposed to the client. This prevents malicious customers from being able to choose their own prices.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "amount"=1099 \
  -d "currency"="usd"`### Client-side

On the client, implement this delegate method to:

1. Request a`PaymentIntent`from your server.
2. Assemble a[STPPaymentIntentParams](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentIntentParams.html)object with the`PaymentIntent`client secret from your server and the[paymentMethod](https://stripe.dev/stripe-ios/docs/Classes/STPPaymentResult.html#/c:objc(cs)STPPaymentResult(py)paymentMethod)provided by the delegate method.
3. Call the[STPPaymentHandler confirmPayment](https://stripe.dev/stripe-ios/stripe-payments/Classes/STPPaymentHandler.html#/c:@M@StripePayments@objc(cs)STPPaymentHandler(im)confirmPayment:withAuthenticationContext:completion:)method to[confirm](/api/payment_intents/confirm)the payment, passing the`STPPaymentContext`as the[authenticationContext](https://stripe.dev/stripe-ios/stripe-payments/Protocols/STPAuthenticationContext.html).

ViewController.swift[Swift](#)`func paymentContext(_ paymentContext: STPPaymentContext,
  didCreatePaymentResult paymentResult: STPPaymentResult,
  completion: @escaping STPErrorBlock) {
    // Request a PaymentIntent from your backend
    MyAPIClient.sharedClient.createPaymentIntent(products: self.products, shippingMethod: paymentContext.selectedShippingMethod) { result in
        switch result {
        case .success(let clientSecret):
            // Assemble the PaymentIntent parameters
            let paymentIntentParams = STPPaymentIntentParams(clientSecret: clientSecret)
            paymentIntentParams.paymentMethodId = paymentResult.paymentMethod.stripeId

            // Confirm the PaymentIntent
            STPPaymentHandler.shared().confirmPayment(paymentIntentParams, with: paymentContext) { status, paymentIntent, error in
                switch status {
                case .succeeded:
                    // Your backend asynchronously fulfills the customer's order, for example, via webhook
                    completion(.success, nil)
                case .failed:
                    completion(.error, error) // Report error
                case .canceled:
                    completion(.userCancellation, nil) // Customer canceled
                @unknown default:
                    completion(.error, nil)
                }
            }
        case .failure(let error):
            completion(.error, error) // Report error from your API
            break
        }
    }
}`You must call the provided completion block with the appropriate STPPaymentStatus (.success, .error, or .userCancellation) when the customer’s payment is finished.

### - paymentContext:didFinishWithStatus:error:

This method is called after the previous method, when any auxiliary UI that has been displayed (such as the Apple Pay dialog) has been dismissed. You should inspect the returned status and show an appropriate message to your user. For example:

ViewController.swift[Swift](#)`func paymentContext(_ paymentContext: STPPaymentContext,
  didFinishWithStatus status: STPPaymentStatus,
  error: Error?) {

    switch status {
    case .error:
        self.showError(error)
    case .success:
        self.showReceipt()
    case .userCancellation:
        return // Do nothing
    }
}`### - paymentContext:didFailToLoadWithError:

This method is called in the rare case that the payment context’s initial loading call fails, usually due to lack of internet connectivity. You should dismiss your checkout page when this occurs and invite the user to try again. You can also optionally attempt to try again by calling retryLoading on the payment context.

ViewController.swift[Swift](#)`func paymentContext(_ paymentContext: STPPaymentContext,
  didFailToLoadWithError error: Error) {
    self.navigationController?.popViewController(animated: true)
    // Show the error to your user, and so on
}`[Test the integration](#test)​​Several test cards are available for you to use in test mode to make sure this integration is ready. Use them with any CVC and an expiration date in the future.

NumberDescription4242424242424242Succeeds and immediately processes the payment.4000002500003155Requires authentication. Stripe triggers a modal asking for the customer to authenticate.4000000000009995Always fails with a decline code of`insufficient_funds`.For the full list of test cards see our guide on testing.

[OptionalHandle post-payment events](#fulfillment)[OptionalSet up Apple PayClient-side](#set-up-apple-pay)[OptionalCustomize the UIClient-side](#theming)## See also

- [After the payment](/payments/after-the-payment)
- [The Payment Intents API](/payments/payment-intents)
- [Stripe iOS SDK Reference](https://stripe.dev/stripe-ios/)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Stripe](#setup-ios)[Set up an ephemeral key](#ephemeral-key)[Set up an STPCustomerContext](#set-up-customer-context)[Set up an STPPaymentContext](#initialize-payment-context)[Handle the user's payment method](#handle-payment-method)[Handle the user's shipping info](#handle-shipping-info)[Submit the payment](#submit-payment)[Test the integration](#test)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`