# PIN management

Some Point-of-Sale and ATM card terminals require cardholders to enter their card’s PIN to authenticate transactions. Cardholders also need to use their PINs with physical cards in many regions of the world. You can use the Stripe API and Stripe Elements to manage and view PINs on your issued cards.

[Stripe Elements](/payments/elements)

Both physical card and virtual card PINs are set to a random value at creation. Cards created as a replacement for other cards won’t inherit the old card’s PIN. In test mode, all PINs are set to 0000 by default.

[physical card](/issuing/cards/physical)

[virtual card](/issuing/cards/virtual)

[replacement for](/api/issuing/cards/create#create_issuing_card-replacement_for)

[test mode](/test-mode)

## Setting a card’s initial PIN at creation

When issuing a new card through the API, you can provide a desired PIN to be pre-set on the card. This is optional, and if you don’t provide an initial PIN, we randomly generate one for you. You can always view a card’s PIN.

[view a card’s PIN](#viewing-a-cards-pin)

To pre-set a PIN when issuing a new card, pass it in encrypted form as the pin.encrypted_number parameter to the Create Card API method:

See Encrypting PINs for more information about how to encrypt a PIN before passing it to the Stripe API or your own servers.

[Encrypting PINs](#encrypting-pins)

When setting a card’s initial PIN in a request to the Create Card API method, the response to the creation request won’t return the PIN (in either encrypted or plain-text form).

## Viewing a card’s PIN

You can use Issuing Elements to retrieve a card’s PIN in a PCI-DSS-compliant way.

[Issuing Elements](/issuing/elements)

[PCI-DSS](/security/guide#validating-pci-compliance)

Stripe provides a browser-side JavaScript library that allows you to display the sensitive data (including PINs) of your Issuing cards in a PCI-compliant manner. The PIN renders inside of a Stripe-hosted iframe and never touches your servers. Stripe offers this library as a part of Stripe.js.

[Stripe.js](/js)

All Issuing users, whether they’re PCI-compliant or not, can use Issuing Elements to retrieve PINs.

To retrieve a card’s PIN using Issuing Elements, first create an Issuing Elements integration, and then use it to display the issuingCardPinDisplay Element:

[create an Issuing Elements integration](/issuing/elements)

## Changing a PIN

Cardholders can change the PIN for their Stripe Issuing card at most ATMs. The cardholder must know the card’s current PIN to change it at an ATM. You can retrieve a card’s PIN before changing it. Some countries, such as France, don’t provide PIN management features at ATMs.

[retrieve a card’s PIN](#viewing-a-cards-pin)

## Unblocking a PIN

If a card’s PIN is entered incorrectly three consecutive times, the card becomes blocked. No further payments can be made through the card until the PIN is unblocked.

In most countries, cardholders can unblock a card’s PIN at an ATM.

## Encrypting PINs

To enable you to set a card’s PIN in a way that doesn’t require it to pass through your servers in plain text, the Stripe API expects you to provide PINs in an encrypted form.

Encrypt the desired PIN (for example, "0123") in JWE (JSON Web Encryption) format using Stripe’s RSA public key. When encrypting, use the RSA-OAEP algorithm for key wrapping and A128CBC-HS256 for content encryption.

[Stripe’s RSA public key](https://issuing-key.stripe.com/v1/keys)

Stripe provides its public key for PIN encryption in both PKCS#8 and JWK format. Depending on your client environment and the library used, one might be easier to use than the other.

- Don’t cache, store, or reuse encrypted PINs for longer than necessary to call the Stripe API.

- Don’t encrypt PINs on your servers. Instead, perform encryption as soon as your user provides the PIN (for example, in your mobile application or in your web application’s frontend) and pass the encrypted form to your servers, and then on to the Stripe API.

- Don’t cache Stripe’s Issuing public key: we can change it or rotate it without notice. Instead, fetch it for every PIN operation you perform on the Stripe API.

- Don’t roll your own cryptography. JWE libraries are available for most common languages and platforms.

[https://issuing-key.stripe.com/v1/keys](https://issuing-key.stripe.com/v1/keys)

The example above encrypts a PIN (0123) using JSON Object Signing and Encryption libraries for various languages. Equivalent libraries exist for other languages:

[jose](https://github.com/panva/jose)

[jwcrypto](https://github.com/latchset/jwcrypto)

[ruby-jose](https://github.com/potatosalad/ruby-jose)

[go-jose](https://github.com/square/go-jose)

[JOSESwift](https://github.com/airsidemobile/JOSESwift)

[jose4j](https://bitbucket.org/b_c/jose4j/wiki/Home)

[jose-jwt](https://github.com/dvsekhvalnov/jose-jwt)
