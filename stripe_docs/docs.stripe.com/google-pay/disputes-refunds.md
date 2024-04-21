# Google Pay liability shift, disputes, and refunds

Post payment activities can include disputes and refunds. When these use cases happen, learn how to address disputed payments, understand the nuances of liability shifts for Google Pay charges, and manage refunds effectively.

## Disputed payments

Users must authenticate payments with their Google Pay accounts, helping to reduce the risk of fraud or unrecognized payments. However, users can still dispute transactions after they complete payment. You can submit evidence to contest a dispute directly. The dispute process is the same as that for card payments. Learn how to manage disputes.

[manage disputes](/disputes/responding)

## Liability shift for Google Pay charges

Google Pay supports liability shift globally. This is true automatically for users on Stripe-hosted products and using Stripe.js. For Visa transactions outside of a Stripe-hosted product, you must enable liability shift in the Google Pay & Wallet Console. To do so, navigate to your Google Pay & Wallet Console, select Google Pay API in the navigation bar on the left, and then enable Fraud Liability Protection for Visa Device Tokens for liability shift protection.

[liability shift](/payments/3d-secure/authentication-flow#disputed-payments)

There are three use cases of Google Pay transactions:

- If the user adds a card to the Google Pay app using their mobile device, this card is saved as a Device Primary Account Number (DPAN), and it supports liability shift by default.

- If the user adds a card to Chrome or a Google property (for example, YouTube or Play), this card is saved as a Funding Primary Account Number (FPAN). Liability shift is supported for all major networks, including Visa, globally when 3D Secure is performed. You can customize Stripe Radar rules to request activation of 3D Secure.

[3D Secure](/payments/3d-secure)

[Stripe Radar rules](/radar/rules#request-3d-secure)

- If the user selects Google Pay as the payment method on an e-commerce site or in an app that pays with Google Pay, the cards are saved as e-commerce tokens that represent the cards on file. Neither liability shift nor 3D Secure are supported for e-commerce tokens at this time.

For Sigma users, the charges table contains a card_token_type field that indicates the Google Pay transaction type. An FPAN transaction sets the card_token_type to fpan. DPAN and ecommerce token transactions set the card_token_type to dpan_or_ecommerce_token.

## Refunds

You can partially or fully refund any successful Google Pay payment. The refund process is the same as that for card payments. See Refund and cancel payments for instructions on initiating or managing refunds.

[Refund and cancel payments](/refunds)
