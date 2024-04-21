# Display cart details

The built-in screen of the Verifone P400,  BBPOS WisePOS E and Stripe Reader S700 can display line items. During the checkout process, you can update the reader’s screen to show individual items in the transaction, along with the total price.

[Verifone P400](/terminal/readers/verifone-p400)

[BBPOS WisePOS E](/terminal/readers/bbpos-wisepos-e)

[Stripe Reader S700](/terminal/readers/stripe-reader-s700)

Cart details screen

## Set the reader display

- setReaderDisplay (iOS)

[setReaderDisplay (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)setReaderDisplay:completion:)

- setReaderDisplay (Android)

[setReaderDisplay (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/set-reader-display.html)

- setReaderDisplay (JavaScript)

[setReaderDisplay (JavaScript)](/terminal/references/api/js-sdk#set-reader-display)

- setReaderDisplay (React Native)

[setReaderDisplay (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#setReaderDisplay)

To set the line items and total displayed on the reader during a payment, pass line items and total information into the setReaderDisplay method. The object you pass in will drive the contents displayed on the reader’s screen.

[setReaderDisplay](/terminal/references/api/js-sdk#set-reader-display)

The amounts passed to the setReaderDisplay method are only used for display purposes. The reader won’t automatically calculate tax or the total—your application must calculate the tax and total before displaying the values. You can use the Stripe Tax API to calculate taxes. Similarly, the total passed to setReaderDisplay doesn’t control the amount charged to the customer. Make sure the amount displayed on the reader matches the amount you’re charging your customer.

[Stripe Tax API](/tax/custom#calculate-tax)

To clear reader display on the server-driven integration, call the cancel_action endpoint.

[cancel_action](/api/terminal/readers/cancel_action)

## Pre-dip a card

Pre-dipping a card is only supported for payments in the US.

The Verifone P400, BBPOS WisePOS E, and Stripe Reader S700 support the ability to present a card to the reader before the transaction amount is finalized.

[Verifone P400](/terminal/readers/verifone-p400)

[BBPOS WisePOS E](/terminal/readers/bbpos-wisepos-e)

[Stripe Reader S700](/terminal/readers/stripe-reader-s700)

This option—known as pre-dip, pre-tap, or pre-swipe—can help speed up transaction times by allowing a customer to present a payment method before the end of the transaction.

The setReaderDisplay method prepares the reader for pre-dipping. The customer can present a payment method at any point after the method is called.

Even if a customer pre-dips their card, your application must still complete the full payment flow.
