htmlPIN management | Stripe Documentation[Skip to content](#main-content)PIN management[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fpin-management)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fpin-management)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)# PIN management

Let your cardholders manage their personal identification numbers.Some Point-of-Sale and ATM card terminals require cardholders to enter their card’s PIN to authenticate transactions. Cardholders also need to use their PINs with physical cards in many regions of the world. You can use the Stripe API and Stripe Elements to manage and view PINs on your issued cards.

Both physical card and virtual card PINs are set to a random value at creation. Cards created as a replacement for other cards won’t inherit the old card’s PIN. In test mode, all PINs are set to 0000 by default.

## Setting a card’s initial PIN at creation

When issuing a new card through the API, you can provide a desired PIN to be pre-set on the card. This is optional, and if you don’t provide an initial PIN, we randomly generate one for you. You can always view a card’s PIN.

To pre-set a PIN when issuing a new card, pass it in encrypted form as the pin.encrypted_number parameter to the Create Card API method:

Command Line`curl https://api.stripe.com/v1/issuing/cards \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "cardholder"="ich_1D4b3fdsa" \
  -d "pin[encrypted_number]"="eyJhbGciOiJSU0..."
  -d "type"="virtual" \
  -d "currency"="usd"`See Encrypting PINs for more information about how to encrypt a PIN before passing it to the Stripe API or your own servers.

NoteWhen setting a card’s initial PIN in a request to the Create Card API method, the response to the creation request won’t return the PIN (in either encrypted or plain-text form).

## Viewing a card’s PIN

You can use Issuing Elements to retrieve a card’s PIN in a PCI-DSS-compliant way.

### Using Issuing Elements

Stripe provides a browser-side JavaScript library that allows you to display the sensitive data (including PINs) of your Issuing cards in a PCI-compliant manner. The PIN renders inside of a Stripe-hosted iframe and never touches your servers. Stripe offers this library as a part of Stripe.js.

All Issuing users, whether they’re PCI-compliant or not, can use Issuing Elements to retrieve PINs.

To retrieve a card’s PIN using Issuing Elements, first create an Issuing Elements integration, and then use it to display the issuingCardPinDisplay Element:

`const stripe = Stripe("pk_test_VOOyyYjgzqdm8I3SrBqmh9qY");

const cardId = 'ic_abc123'; // ID of the issued Card you want to retrieve the PIN for
const ephemeralKeyNonce = ...;
const ephemeralKey = ...;

// create the PIN Element with Stripe.js
const pinElement = stripe.elements().create('issuingCardPinDisplay', {
  issuingCard: cardId,
  nonce: ephemeralKeyNonce,
  ephemeralKeySecret: ephemeralKey.secret,
});

// Mount the PIN element onto DOM elements on your web page
pinElement.mount('#card-pin');`## Changing a PIN

### Changing a PIN at an ATM

Cardholders can change the PIN for their Stripe Issuing card at most ATMs. The cardholder must know the card’s current PIN to change it at an ATM. You can retrieve a card’s PIN before changing it. Some countries, such as France, don’t provide PIN management features at ATMs.

## Unblocking a PIN

If a card’s PIN is entered incorrectly three consecutive times, the card becomes blocked. No further payments can be made through the card until the PIN is unblocked.

In most countries, cardholders can unblock a card’s PIN at an ATM.

## Encrypting PINs

To enable you to set a card’s PIN in a way that doesn’t require it to pass through your servers in plain text, the Stripe API expects you to provide PINs in an encrypted form.

Encrypt the desired PIN (for example, "0123") in JWE (JSON Web Encryption) format using Stripe’s RSA public key. When encrypting, use the RSA-OAEP algorithm for key wrapping and A128CBC-HS256 for content encryption.

Stripe provides its public key for PIN encryption in both PKCS#8 and JWK format. Depending on your client environment and the library used, one might be easier to use than the other.

### PIN encryption best practices

- Don’t cache, store, or reuse encrypted PINs for longer than necessary to call the Stripe API.
- Don’t encrypt PINs on your servers. Instead, perform encryption as soon as your user provides the PIN (for example, in your mobile application or in your web application’s frontend) and pass the encrypted form to your servers, and then on to the Stripe API.
- Don’t cache Stripe’s Issuing public key: we can change it or rotate it without notice. Instead, fetch it for every PIN operation you perform on the Stripe API.
- Don’t roll your own cryptography. JWE libraries are available for most common languages and platforms.

### PIN encryption examples

[JavaScript](#)`import fetch from 'node-fetch';
import { importJWK, CompactEncrypt } from 'jose'

async function encryptPin(myNewPin) {
  // Fetch Stripe's RSA public key
  const keyData = await fetch('https://issuing-key.stripe.com/v1/keys')
    .then(r => r.json());

  // Import the public key. Here, we choose to import the JWK-formatted key,
  // but it will also be available in PKCS#8 format as `keyData.pkcs8`
  const publicKey = await importJWK(keyData.jwk, 'RSA');

  // Encrypt the new PIN with the given public key, using the RSA-OAEP
  // algorithm to wrap the key, and A128CBC-HS256 to produce the ciphertext
  const jwe = await new CompactEncrypt(new TextEncoder().encode(myNewPin))
    .setProtectedHeader({ alg: 'RSA-OAEP', enc: 'A128CBC-HS256', kid: keyData.key_id })
    .encrypt(publicKey);

  // Return our JWE (JWEs are base64url-encoded)
  return jwe;
}

await encryptPin("0123");
// => eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkExMjhDQkMtSFMyNTYiLCJraWQiOiJz...`The example above encrypts a PIN (0123) using JSON Object Signing and Encryption libraries for various languages. Equivalent libraries exist for other languages:

LanguageLibraryJavaScript[jose](https://github.com/panva/jose)Python[jwcrypto](https://github.com/latchset/jwcrypto)Ruby[ruby-jose](https://github.com/potatosalad/ruby-jose)Go[go-jose](https://github.com/square/go-jose)Swift[JOSESwift](https://github.com/airsidemobile/JOSESwift)Java[jose4j](https://bitbucket.org/b_c/jose4j/wiki/Home).NET[jose-jwt](https://github.com/dvsekhvalnov/jose-jwt)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Setting a card’s initial PIN at creation](#setting-a-card’s-initial-pin-at-creation)[Viewing a card’s PIN](#viewing-a-cards-pin)[Changing a PIN](#changing-a-pin)[Unblocking a PIN](#unblocking-a-pin)[Encrypting PINs](#encrypting-pins)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`