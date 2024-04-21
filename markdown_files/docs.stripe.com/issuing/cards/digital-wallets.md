htmlUse digital wallets with Issuing | Stripe Documentation[Skip to content](#main-content)Digital wallets[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fdigital-wallets)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fdigital-wallets)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)# Use digital wallets with Issuing

Learn how to use Issuing to add cards to digital wallets.NoteDigital wallets are currently only available in the US, and not yet available in the UK and euro area.

Issuing allows users to add cards to digital wallets like Apple Pay and Google Pay. Stripe supports the addition of cards through two methods:

1. Manual Provisioning:cardholders enter their card details into a phone’s wallet application to add it to their digital wallets.
2. Push Provisioning:mobile applications allow users to add cards to their digital wallets straight from the app.

When a card is added to a digital wallet, a tokenized representation of that card is created. Network tokens are managed separately from cards. For more information about network tokens and how they work, see Token Management.

## Manual Provisioning

Cardholders can add Stripe Issuing virtual cards and physical cards to their Apple Pay, Google Pay, and Samsung Pay wallets through manual provisioning.

To do so, cardholders open the wallet app on their phone and enter their card details. Stripe then sends a 6-digit verification code to the phone_number or email of the cardholder associated with the card.

A card not supported error displays if neither field is set on the cardholder when the card was provisioned.

No code is required to implement manual provisioning, but the process to set it up can vary depending on the digital wallet provider and the country you’re based in:

### US

Apple Pay wallets require approval from Apple. Check your digital wallets settings to view the status of Apple Pay in your account. You might need to submit an application before using Apple Pay.

Google Pay and Samsung Pay have no additional required steps.

### EU/UK

Digital wallet integrations require additional approval from the Stripe partnership team. Get in touch with your account representative or contact Stripe for more information.

Apple Pay wallets require additional approval. Check your digital wallets settings to view the status of Apple Pay in your account. You might need to submit an application before using Apple Pay.

## Push Provisioning

With push provisioning, cardholders can add their Stripe Issuing cards to their digital wallets using your app, by pressing an “add to wallet” button like the ones shown below.

Users must first complete manual provisioning steps in order to enable push provisioning in the US. In addition to manual provisioning approval, push provisioning requires you to integrate with the Stripe SDK.

This requires both approval processes through Stripe and code integration with the Stripe SDK for each platform you wish to support push provisioning on. Platform approvals cascade down to all of their connected accounts.

Samsung Pay push provisioning isn’t supported with our SDKs.

iOSAndroidReact Native![A black UI button that says Add to Apple Wallet. There is an Apple Wallet logo image to the left of the text. It is a grey wallet with blue, yellow, green, and red cards stacked slightly offset.](https://b.stripecdn.com/docs-statics-srv/assets/add_to_apple_wallet.fe8cd234760a7478e34f5e91d22677bb.png)

[Request Access](#request-access)Push provisioning requires a special entitlement from Apple called com.apple.developer.payment-pass-provisioning. You can request it by emailing support-issuing@stripe.com. In your email, include your:

- App name—Your app’s name.
- Developer team ID—Found in your Apple Developer account settings under[membership](https://developer.apple.com/account/#/membership)(for example,`2A23JCNA5E`).
- ADAM ID—Your app’s unique numeric ID. Found in[App Store Connect](https://appstoreconnect.apple.com), or in the App Store link to your app (for example,`https://apps.apple.com/app/id123456789`).
- Bundle ID—Your app’s bundle identifier, also found in App Store Connect (for example,`com.example.yourapp`).

If you have multiple apps (such as for testing), that have any different fields for the above attributes, you will need to request access for each of these.

After we approve and apply your request, your app appears on the details page of a provisioned card in the Wallet app, and the PKSecureElementPass object is available in your app by calling PKPassLibrary().passes(). You might need to remove and re-provision the card for the change to take effect.

[Check eligibilityClient-side](#check-eligibility)Make sure you’ve integrated the latest version of the Stripe iOS SDK with your app.

Determine if the device is eligible to use push provisioning.

1. Check that the value of`wallets[apple_pay][eligible]`in the issued card is`true`.
2. Call`PKPassLibrary().canAddSecureElementPass(primaryAccountIdentifier:)`with the`wallets[primary_account_identifier]`from your card, and check that the result is`true`. If the`primary_account_identifier`is empty, pass an empty string to`canAddSecureElementPass()`.

Retrieve these values on your backend, then pass them to your app for the eligibility check.

WarningYou must check the server-side wallets[apple_pay][eligible] flag and the result of canAddSecureElementPass() before showing the PKAddPassButton. If you show an Add to Apple Wallet button without checking these values, App Review might reject your app.

[Swift](#)`import Stripe

class MyViewController: UIViewController {

  @IBOutlet weak var addPassButton: PKAddPassButton!
  // ...
  func handleEligibilityResponse(eligible: Bool, primaryAccountIdentifier: String?) {
    if eligible &&
    PKPassLibrary().canAddSecureElementPass(primaryAccountIdentifier: primaryAccountIdentifier ?? "") {
      addPassButton.isHidden = false
    } else {
      addPassButton.isHidden = true
    }
  }

}`For more context, see the code snippets and references to the sample app at each step. For this step, see how the sample app checks eligibility.

[Provision a cardClient-side](#provision-a-card)When the user taps the PKAddPassButton, create and present a PKAddPaymentPassViewController, which contains Apple’s UI for the push provisioning flow.

NotePKAddPaymentPassViewController can use the primaryAccountIdentifier from the previous step to determine if a card has already been provisioned on a specific device. For example, if the card has already been added to an iPhone, Apple’s UI offers to add it to a paired Apple Watch.

[Swift](#)`import Stripe

class MyViewController: UIViewController {
  // ...
  func beginPushProvisioning() {
    let config = STPPushProvisioningContext.requestConfiguration(
      withName: "Jenny Rosen", // the cardholder's name
      description: "RocketRides Card", // optional; a description of your card
      last4: "4242", // optional; the last 4 digits of the card
      brand: .visa, // optional; the brand of the card
      primaryAccountIdentifier: self.primaryAccountIdentifier // the primary_account_identifier value from the previous step
    )
    let controller = PKAddPaymentPassViewController(requestConfiguration: config, delegate: self)
    self.present(controller!, animated: true, completion: nil)
  }
}`For more context, see how the sample app uses a PKAddPaymentPassViewController.

The PKAddPaymentPassViewController’s initializer takes a delegate that you need to implement – typically this can just be the view controller from which you’re presenting it. We provide a class called STPPushProvisioningContext to help you implement these methods.

[Swift](#)`class MyViewController: UIViewController {
  var pushProvisioningContext: STPPushProvisioningContext? = nil
  // ...
}

extension MyViewController: PKAddPaymentPassViewControllerDelegate {
  func addPaymentPassViewController(_ controller: PKAddPaymentPassViewController, generateRequestWithCertificateChain certificates: [Data], nonce: Data, nonceSignature: Data, completionHandler handler: @escaping (PKAddPaymentPassRequest) -> Void) {
    self.pushProvisioningContext = STPPushProvisioningContext(keyProvider: self)
    // STPPushProvisioningContext implements this delegate method for you, by retrieving encrypted card details from the Stripe API.
    self.pushProvisioningContext?.addPaymentPassViewController(controller, generateRequestWithCertificateChain: certificates, nonce: nonce, nonceSignature: nonceSignature, completionHandler: handler);
  }

  func addPaymentPassViewController(_ controller: PKAddPaymentPassViewController, didFinishAdding pass: PKPaymentPass?, error: Error?) {
    // Depending on if `error` is present, show a success or failure screen.
    self.dismiss(animated: true, completion: nil)
  }
}`For more context, see how the sample app implements PKAddPaymentPassViewControllerDelegate.

You can see that the STPPushProvisioningContext’s initializer expects a keyProvider. This is an instance of a class that implements the STPIssuingCardEphemeralKeyProvider protocol.

This protocol defines a single required method, createIssuingCardKeyWithAPIVersion:completion. To implement this method, make an API call to your backend. Your backend creates an Ephemeral Key object using the Stripe API, and returns it to your app. Your app then calls the provided completion handler with your backend’s API response.

[Swift](#)`extension MyViewController: STPIssuingCardEphemeralKeyProvider {
    func createIssuingCardKey(withAPIVersion apiVersion: String, completion: @escaping STPJSONResponseCompletionBlock) {
        // This example uses Alamofire for brevity, but you can make the request however you want
        AF.request("https://myapi.com/ephemeral_keys",
                   method: .post,
                   parameters: ["api_version": apiVersion])
        .responseJSON { response in
            switch response.result {
            case .success:
                if let data = response.data {
                    do {
                        let obj = try JSONSerialization.jsonObject(with: data, options: []) as! [AnyHashable: Any]
                        completion(obj, nil)
                    } catch {
                        completion(nil, error)
                    }
                }
            case .failure(let error):
                completion(nil, error)
            }
        }
    }
}`For more context, see how the sample app implements STPIssuingCardEphemeralKeyProvider.

[Update your backendServer-side](#update-your-backend)The push provisioning implementation exposes methods that expect you to communicate with your own backend to create a Stripe Ephemeral Key and return a JSON of it to your app. This key is a short-lived API credential that you can use to retrieve the encrypted card details for a single instance of a card object.

To make sure that the object returned by the Stripe API is compatible with the version of the iOS or Android SDK you’re using, the Stripe SDK lets you know what API version it prefers. You must explicitly pass this API version to our API when creating the key.

Command Line[curl](#)`curl https://api.stripe.com/v1/ephemeral_keys \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "issuing_card"="{{ISSUING_CARD_ID}}" \
  -H "Stripe-Version: {{API_VERSION}}"``{
    "id": "ephkey_1G4V6eEEs6YsaMZ2P1diLWdj",
    "object": "ephemeral_key",
    "associated_objects": [
        {
            "id": "ic_1GWQp6EESaYspYZ9uSEZOcq9",
            "type": "issuing.card"
        }
    ],
    "created": 1586556828,
    "expires": 1586560428,
    "livemode": false,
    "secret": "ek_test_YWNjdF8xRmdlTjZFRHelWWxwWVo5LEtLWFk0amJ2N0JOa0htU1JzEZkd2RpYkpJdnM_00z2ftxCGG"
}`For more context, see how the sample backend creates a Stripe Ephemeral Key.

[Testing](#testing)The com.apple.developer.payment-pass-provisioning entitlement only works with distribution provisioning profiles, meaning even after you obtain it, the only way to test the end-to-end push provisioning flow is by distributing your app with TestFlight or the App Store.

To help with testing, we provide a mock version of PKAddPaymentPassViewController called STPFakeAddPaymentPassViewController that can be used interchangeably during testing.

[Swift](#)`import Stripe

class MyViewController: UIViewController {
  // ...
  func beginPushProvisioning() {
    let config = STPPushProvisioningContext.requestConfiguration(
      withName: "Jenny Rosen", // the cardholder's name
      description: "RocketRides Card", // optional; a description of your card
      last4: "4242", // optional; the last 4 digits of the card
      brand: .visa // optional; the brand of the card
    )
    let controller = STPFakeAddPaymentPassViewController(requestConfiguration: config, delegate: self)
    self.present(controller!, animated: true, completion: nil)
  }
}`To build the sample app, follow the steps in the readme. You don’t need to build the app to follow the instructions above.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Manual Provisioning](#manual-provisioning)[Push Provisioning](#push-provisioning)[Request Access](#request-access)[Check eligibility](#check-eligibility)[Provision a card](#provision-a-card)[Update your backend](#update-your-backend)[Testing](#testing)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`