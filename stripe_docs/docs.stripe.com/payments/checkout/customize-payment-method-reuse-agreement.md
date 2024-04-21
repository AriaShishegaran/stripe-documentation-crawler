# Customize payment method reuse agreement

Checkout displays a message to customers about reusing their payment method when a session is in either setup or subscription mode, or when a payment mode session has setup_future_usage set. You can hide this text and use custom text to set different language governing the reuse of a payment method. This text appears alongside additional legal text for some payment methods and includes information about trials when applicable.

Default payment method reuse agreement in subscription mode

[Hide the payment method reuse agreement](#hidden-payment-method-reuse-agreement)

## Hide the payment method reuse agreement

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

[https://www.example.com/)](https://www.example.com/))

To hide the payment method reuse agreement text, set consent_collections.payment_method_reuse_agreement.position='hidden'. Checkout won’t display its default language governing the reuse of the payment method. To set your own text in place of Stripe’s default language, set custom_text.after_submit.message. You can also use custom_text.submit or custom_text.terms_of_service_acceptance to display your own version of this language.

By customizing this text, you’re responsible for maintaining compliance, which includes updating this text as card network rules and local regulations change. Don’t use this feature without consulting with your legal team or setting custom text that includes information regarding the reuse of the payment method. Make sure that your customized text covers all modes you plan to support.

## See also

- Customize Checkout

[Customize Checkout](/payments/checkout/customization)
