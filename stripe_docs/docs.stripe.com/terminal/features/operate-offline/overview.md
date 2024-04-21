# Operate offlineBeta

When you’re operating with intermittent, limited, or no network connectivity, Stripe Terminal allows you to store payments locally on your POS device. When a network connection is restored, the SDK automatically forwards any stored payments to Stripe.

From your application’s perspective, the payment collection process is similar to operating online. While offline, the SDK securely stores the payment information and automatically forwards the stored payments when connectivity is restored. The SDK allows you to handle offline-related events using callbacks to your application.

## Availability

Payment methods: Visa, Mastercard, Discover, and American Express.

Customers can present a card or NFC-based mobile wallet belonging to a supported card brand. Swiping cards isn’t allowed. If you’re collecting payments in the European Economic Area, customers are required to insert their card and enter a PIN.

[European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)

Interac and eftpos aren’t supported. Co-branded eftpos cards are routed through the international scheme instead. For more information, see eftpos Australia.

[eftpos Australia](/payments/eftpos-australia)

Readers: BBPOS Chipper 2X BT, Stripe Reader M2, BBPOS WisePad 3

[BBPOS Chipper 2X BT](/terminal/readers/bbpos-chipper2xbt)

[Stripe Reader M2](/terminal/readers/stripe-m2)

[BBPOS WisePad 3](/terminal/readers/bbpos-wisepad3)

Integration types: iOS SDK, Android SDK

The following diagram describes the payment collection process when the Terminal SDK is offline. When storing payments, the SDK stores the payments to disk. You can safely reboot the POS device even if it has stored offline payments. When you re-initialize the SDK and it has reestablished a connection to the internet, and the SDK resumes forwarding any remaining stored payments.

The following diagram describes how stored payments are forwarded after connectivity is restored.

## See also

- Collect payments while offline

[Collect payments while offline](/terminal/features/operate-offline/collect-payments)
