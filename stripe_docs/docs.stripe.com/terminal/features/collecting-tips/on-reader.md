# Collect on-reader tips

Get notified when Stripe Reader S700 is available in your country.

[Get notified](https://dashboard.stripe.com/terminal/s700_notify)

BBPOS WisePad 3 on-reader tipping Beta

[BBPOS WisePad 3](/terminal/payments/setup-reader/bbpos-wisepad3)

BBPOS WisePOS E on-reader tipping

[BBPOS WisePOS E](/terminal/payments/setup-reader/bbpos-wisepos-e)

Stripe Reader S700 on-reader tipping

[Stripe Reader S700](/terminal/readers/stripe-reader-s700)

With on-reader tipping, you can display suggested tip amounts on the reader before the customer presents their payment method. The reader shows the customer three suggestions based on the tipping option that you set up. The reader automatically shows a tipping selection screen on every call to collect a payment. When you confirm the payment, the PaymentIntent is confirmed for an amount inclusive of the selected tip.

[tipping option](/terminal/features/collecting-tips/on-reader#customize-tips-reader)

[confirm the payment](/terminal/payments/collect-payment#confirm-payment)

Payment screen

Tipping selection screen (percentage)

Total screen

Approved screen

[Enable and customize on-reader tipping](#customize-tips-reader)

## Enable and customize on-reader tipping

Use a Configuration object to set the tipping configuration for your BBPOS WisePad 3 or BBPOS WisePOS E readers:

[Configuration](/api/terminal/configuration)

[BBPOS WisePad 3](/terminal/payments/setup-reader/bbpos-wisepad3)

[BBPOS WisePOS E](/terminal/payments/setup-reader/bbpos-wisepos-e)

- Suggest smart tips - The reader dynamically shows three percentages or amounts, depending on the size of the pre-tip amount.

- Suggest percentages - The reader displays three percentage-based tip amounts.

- Suggest amounts - The reader displays three tip amounts.

To use the on-reader tipping feature on your BBPOS WisePad 3, you must use one of the following Terminal SDK versions:

- Android SDK 2.8.1 or greater

- iOS SDK 2.16.1 or greater

You can suggest three tip percentages or three tip amounts on the reader. The reader dynamically displays either of these smart tips, depending on a pre-tip amount threshold. Create or update a Configuration object as follows. The tips you collect with on-reader tipping are post-tax tips.

With the above example, the reader dynamically chooses what to suggest:

- If the pre-tip amount is below the smart_tip_threshold ($10), the reader shows three buttons suggesting $1, $2, or $3 tips from top to bottom.

- If the pre-tip amount is at the smart_tip_threshold ($10) or above, the reader shows three buttons suggesting tips that are 15%, 20%, or 25% of the pre-tip total from top to bottom.

If specifying more than one currency in your Configuration object, you must provide the same configuration keys for each currency. In other words, if you only specify percentages for USD, you may not specify fixed_amounts or smart_tip_threshold for any other currencies.

After you create a Configuration object with your tipping configuration, you can assign the configuration to your account or a location. BBPOS WisePad 3 readers receive new or updated configurations when they connect to your POS application. BBPOS WisePOS E readers can take up to 5 minutes to receive new or updated configurations.

[assign the configuration](/terminal/fleet/splash-screen#assign-configuration-object)

[Collect payment](#collect-payment)

## Collect payment

For on-reader tipping, follow the instructions for collecting payments and create your PaymentIntents with capture_method as manual.

[collecting payments](/terminal/payments/collect-payment)

When you collect a payment method, your customer sees a tip selection screen on the reader that prompts them to select a tip before asking for their payment method.

[collect a payment method](/terminal/payments/collect-payment#collect-payment)

Depending on your tipping configuration, the customer can choose a suggested tip, specify a custom tip, or leave no tip.

[tipping configuration](/terminal/features/collecting-tips/on-reader#customize-tips-reader)

After the customer makes their selection, the reader waits for them to present a card.

When you process the payment, the reader adds the selected tip. If the payment is successful, the amount in the PaymentIntent and Charge is updated to include the tip amount.

[amount](/api/payment_intents/create#create_payment_intent-amount)

The tip amount is returned in the amount_details object:

[amount_details](/api/payment_intents/object#payment_intent_object-amount_details)

[amount](/api/payment_intents/object#payment_intent_object-amount_details-tip)

Customers won’t see a tipping selection screen in these cases:

- The Configuration object is missing a tipping configuration.

- You enabled skipTipping in your tipping configuration.

- The reader is in an unsupported country.

- A tipping configuration can’t be applied to the current payment currency. For example, if the payment is in EUR but the Configuration object only specifies a tipping configuration for USD.

When testing payments with the Stripe reader, the total amount (inclusive of any tip) may trigger decline responses depending on the decimal value of the total amount.

[testing payments](/terminal/references/testing#physical-test-cards)

[Skip tipping](#skip-tipping)

## Skip tipping

You can ignore the tipping configuration, which allows you to hide the tip selection screen on your BBPOS WisePad 3 or BBPOS WisePOS E reader when collecting payments.

[BBPOS WisePad 3](/terminal/payments/setup-reader/bbpos-wisepad3)

[BBPOS WisePOS E](/terminal/payments/setup-reader/bbpos-wisepos-e)

You can hide the tip selection screen for individual transactions or temporarily for all transactions, which allows your customers to go directly to the card presentment screen.

For example, your restaurant might want to accept tips on the reader for takeout orders, but only allow on-receipt tips for dine-in customers.

[on-receipt tips](/terminal/features/collecting-tips/on-receipt)

Include the following code on your server to enable bypassing the tip selection screen.

[Tip-eligible amounts](#tip-eligible)

## Tip-eligible amounts

Contact us if you’re interested in tip-eligible amounts on a BBPOS WisePad 3.

[Contact us](mailto:stripe-terminal-betas@stripe.com)

[BBPOS WisePad 3](/terminal/readers/bbpos-wisepad3)

When collecting a payment, you can set a tip-eligible amount that’s different from the pre-tip amount. Setting a tip-eligible amount changes the value that percentage-based tips are calculated from. The customer is also shown the tip-eligible amount alongside the pre-tip amount on the tip selection screen.

You can use this setting for businesses that provide services in addition to selling goods. For example, a salon that sells haircuts and bottles of shampoo might want their customer to know that they calculate percentage-based tips on haircuts only.

The above example sets a tip-eligible amount based on the currency of the payment. For a payment in USD, the tip-eligible amount is 15 USD.

The value of eligible_amount must be 0 or higher. If eligible_amount is equal to 0, tipping is skipped regardless of the value of skip_tipping. If eligible_amount is equal to the payment intent amount, eligible_amount is ignored and the tip is calculated based on the specified amount.

Setting a tip-eligible amount that’s greater than 0 while attempting to skip tipping results in an error.
