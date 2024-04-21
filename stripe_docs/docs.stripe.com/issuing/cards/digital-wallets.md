# Use digital wallets with Issuing

Digital wallets are currently only available in the US, and not yet available in the UK and euro area.

Issuing allows users to add cards to digital wallets like Apple Pay and Google Pay. Stripe supports the addition of cards through two methods:

- Manual Provisioning: cardholders enter their card details into a phone’s wallet application to add it to their digital wallets.

- Push Provisioning: mobile applications allow users to add cards to their digital wallets straight from the app.

When a card is added to a digital wallet, a tokenized representation of that card is created. Network tokens are managed separately from cards. For more information about network tokens and how they work, see Token Management.

[Token Management](/issuing/controls/token-management)

## Manual Provisioning

Cardholders can add Stripe Issuing virtual cards and physical cards to their Apple Pay, Google Pay, and Samsung Pay wallets through manual provisioning.

[virtual cards](/issuing/cards/virtual)

[physical cards](/issuing/cards/physical)

To do so, cardholders open the wallet app on their phone and enter their card details. Stripe then sends a 6-digit verification code to the phone_number or email of the cardholder associated with the card.

A card not supported error displays if neither field is set on the cardholder when the card was provisioned.

No code is required to implement manual provisioning, but the process to set it up can vary depending on the digital wallet provider and the country you’re based in:

Apple Pay wallets require approval from Apple. Check your digital wallets settings to view the status of Apple Pay in your account. You might need to submit an application before using Apple Pay.

[digital wallets settings](https://dashboard.stripe.com/settings/issuing/digital-wallets)

Google Pay and Samsung Pay have no additional required steps.

Digital wallet integrations require additional approval from the Stripe partnership team. Get in touch with your account representative or contact Stripe for more information.

[contact Stripe](https://stripe.com/contact/sales)

Apple Pay wallets require additional approval. Check your digital wallets settings to view the status of Apple Pay in your account. You might need to submit an application before using Apple Pay.

[digital wallets settings](https://dashboard.stripe.com/settings/issuing/digital-wallets)

## Push Provisioning

With push provisioning, cardholders can add their Stripe Issuing cards to their digital wallets using your app, by pressing an “add to wallet” button like the ones shown below.

Users must first complete manual provisioning steps in order to enable push provisioning in the US. In addition to manual provisioning approval, push provisioning requires you to integrate with the Stripe SDK.

This requires both approval processes through Stripe and code integration with the Stripe SDK for each platform you wish to support push provisioning on. Platform approvals cascade down to all of their connected accounts.

Samsung Pay push provisioning isn’t supported with our SDKs.

[Request Access](#request-access)

## Request Access

Push provisioning requires a special entitlement from Apple called com.apple.developer.payment-pass-provisioning. You can request it by emailing support-issuing@stripe.com. In your email, include your:

[support-issuing@stripe.com](mailto:support-issuing@stripe.com)

- App name—Your app’s name.

- Developer team ID—Found in your Apple Developer account settings under membership (for example, 2A23JCNA5E).

[membership](https://developer.apple.com/account/#/membership)

- ADAM ID—Your app’s unique numeric ID. Found in App Store Connect, or in the App Store link to your app (for example, https://apps.apple.com/app/id123456789).

[App Store Connect](https://appstoreconnect.apple.com)

- Bundle ID—Your app’s bundle identifier, also found in App Store Connect (for example, com.example.yourapp).

If you have multiple apps (such as for testing), that have any different fields for the above attributes, you will need to request access for each of these.

After we approve and apply your request, your app appears on the details page of a provisioned card in the Wallet app, and the PKSecureElementPass object is available in your app by calling PKPassLibrary().passes(). You might need to remove and re-provision the card for the change to take effect.

[Check eligibilityClient-side](#check-eligibility)

## Check eligibilityClient-side

Make sure you’ve integrated the latest version of the Stripe iOS SDK with your app.

[Stripe iOS SDK](/payments/accept-a-payment?platform=ios)

Determine if the device is eligible to use push provisioning.

- Check that the value of wallets[apple_pay][eligible] in the issued card is true.

- Call PKPassLibrary().canAddSecureElementPass(primaryAccountIdentifier:) with the wallets[primary_account_identifier] from your card, and check that the result is true. If the primary_account_identifier is empty, pass an empty string to canAddSecureElementPass().

Retrieve these values on your backend, then pass them to your app for the eligibility check.

You must check the server-side wallets[apple_pay][eligible] flag and the result of canAddSecureElementPass() before showing the PKAddPassButton. If you show an Add to Apple Wallet button without checking these values, App Review might reject your app.

For more context, see the code snippets and references to the sample app at each step. For this step, see how the sample app checks eligibility.

[sample app](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/ios/Code/ViewController.swift#L201-L218)

[Provision a cardClient-side](#provision-a-card)

## Provision a cardClient-side

When the user taps the PKAddPassButton, create and present a PKAddPaymentPassViewController, which contains Apple’s UI for the push provisioning flow.

PKAddPaymentPassViewController can use the primaryAccountIdentifier from the previous step to determine if a card has already been provisioned on a specific device. For example, if the card has already been added to an iPhone, Apple’s UI offers to add it to a paired Apple Watch.

For more context, see how the sample app uses a PKAddPaymentPassViewController.

[sample app](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/ios/Code/ViewController.swift#L280-L288)

The PKAddPaymentPassViewController’s initializer takes a delegate that you need to implement – typically this can just be the view controller from which you’re presenting it. We provide a class called STPPushProvisioningContext to help you implement these methods.

For more context, see how the sample app implements PKAddPaymentPassViewControllerDelegate.

[sample app](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/ios/Code/ViewController.swift#L293-L349)

You can see that the STPPushProvisioningContext’s initializer expects a keyProvider. This is an instance of a class that implements the STPIssuingCardEphemeralKeyProvider protocol.

This protocol defines a single required method, createIssuingCardKeyWithAPIVersion:completion. To implement this method, make an API call to your backend. Your backend creates an Ephemeral Key object using the Stripe API, and returns it to your app. Your app then calls the provided completion handler with your backend’s API response.

[https://myapi.com/ephemeral_keys](https://myapi.com/ephemeral_keys)

For more context, see how the sample app implements STPIssuingCardEphemeralKeyProvider.

[sample app](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/ios/Code/ViewController.swift#L379-L394)

[Update your backendServer-side](#update-your-backend)

## Update your backendServer-side

The push provisioning implementation exposes methods that expect you to communicate with your own backend to create a Stripe Ephemeral Key and return a JSON of it to your app. This key is a short-lived API credential that you can use to retrieve the encrypted card details for a single instance of a card object.

To make sure that the object returned by the Stripe API is compatible with the version of the iOS or Android SDK you’re using, the Stripe SDK lets you know what API version it prefers. You must explicitly pass this API version to our API when creating the key.

For more context, see how the sample backend creates a Stripe Ephemeral Key.

[sample backend](https://github.com/stripe-samples/push-provisioning-samples/blob/main/server/ruby/README.md)

[Stripe Ephemeral Key](https://github.com/stripe-samples/push-provisioning-samples/blob/main/server/ruby/server.rb#L68-L88)

[Testing](#testing)

## Testing

The com.apple.developer.payment-pass-provisioning entitlement only works with distribution provisioning profiles, meaning even after you obtain it, the only way to test the end-to-end push provisioning flow is by distributing your app with TestFlight or the App Store.

To help with testing, we provide a mock version of PKAddPaymentPassViewController called STPFakeAddPaymentPassViewController that can be used interchangeably during testing.

To build the sample app, follow the steps in the readme. You don’t need to build the app to follow the instructions above.

[readme](https://github.com/stripe-samples/push-provisioning-samples/blob/main/client/ios/README.md)
