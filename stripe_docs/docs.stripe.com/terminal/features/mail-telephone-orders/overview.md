# Mail order and telephone order (MOTO) payments

When building your checkout flow, make sure you can obtain all necessary customer consents and agreements to save card details for future use, and comply with all applicable laws and rules in your region.

Mail order and telephone order (MOTO) processing using Stripe Terminal enables you to collect card details over the telephone or by mail using the server-driven integration on BBPOS WisePOS E readers. You might decide to use the details collected to either charge the customer for the order or save their card details for online reuse. MOTO isn’t currently supported on Stripe’s iOS, Android, JavaScript, or React Native SDKs.

[server-driven integration](/terminal/payments/setup-integration?terminal-sdk-platform=server-driven)

[BBPOS WisePOS E readers](/terminal/payments/setup-reader/bbpos-wisepos-e)

When using MOTO, enter the card information on the card reader instead of tapping or inserting. After initiating MOTO, the reader prompts you to enter the cardholder’s card number, CVC, expiration date, and postal code. The reader then displays a summary of the details you entered, and you can submit the payment for confirmation or save the card details.

MOTO is a gated, paid feature that requires P2PE. Please reach out to your sales representative for more information. After we enable the changes, you must disconnect from and reconnect to your reader for the updated configuration to take effect immediately.

[P2PE](https://support.stripe.com/questions/stripe-terminal-encryption-e2ee-vs-p2pe)

[sales representative](https://stripe.com/contact/sales)

## See also

- Process MOTO payments

[Process MOTO payments](/terminal/features/mail-telephone-orders/payments)

- Saving cards using MOTO

[Saving cards using MOTO](/terminal/features/mail-telephone-orders/save-directly)
