# Card declines

Card payments can fail for a variety of reasons. Some of the most common are:

- Insufficient customer funds: If a customer has insufficient customer funds or credit, the card issuer declines the transaction. To help minimize declines due to insufficient funds, consider adding a Buy Now, Pay Later (BNPL) option.

Insufficient customer funds: If a customer has insufficient customer funds or credit, the card issuer declines the transaction. To help minimize declines due to insufficient funds, consider adding a Buy Now, Pay Later (BNPL) option.

[Buy Now, Pay Later (BNPL)](/payments/buy-now-pay-later)

- Incorrect card data: If a customer enters an incorrect card number, CVV, or expiration date, the card issuer might decline the transaction. In these cases, request your customer to re-enter their card information.

Incorrect card data: If a customer enters an incorrect card number, CVV, or expiration date, the card issuer might decline the transaction. In these cases, request your customer to re-enter their card information.

- Fraudulent activity: If a card issuer suspects fraudulent activity, which can be triggered by large purchases or a large volume of transactions over a short period of time, they might decline payments. Your customer must resolve this issue by communicating with their issuing bank and confirming their identity.

Fraudulent activity: If a card issuer suspects fraudulent activity, which can be triggered by large purchases or a large volume of transactions over a short period of time, they might decline payments. Your customer must resolve this issue by communicating with their issuing bank and confirming their identity.

Use Stripe Sigma to analyze your decline rate. Our interactive SQL reporting environment offers prebuilt queries for this purpose. To investigate declines outside Sigma, consider the Card object fingerprints instead of charge IDs to exclude repeat attempts.

[Stripe Sigma](/stripe-data)

[fingerprints](/api/cards/object#card_object-fingerprint)

## Card declines

When your customer’s card issuer receives a charge, their automated systems and models decide whether to authorize it. These tools analyze signals such as spending habits, account balance, and card data including expiration date, address information, and CVC.

If the card issuer declines a payment, Stripe shares some of the decline information we receive. This information is available in the Dashboard and through the API. Sometimes, issuers provide specific explanations, such as an incorrect card number or low funds. We show these as decline codes.

[decline codes](/declines/codes)

Card issuer’s categorize most declines as generic (generic_decline), making the exact decline reason unclear. If the card information is correct, request your customer to contact their card issuer to understand why a transaction was declined. For privacy and security reasons, card issuers discuss the specifics of a decline only with their cardholders.

[generic_decline](/declines/codes#generic_decline)

## Reduce card declines

You can typically resolve card issuer declines resulting from inaccurate card details (such as an incorrect card number or expiration date) by asking your customers to correct the error or use a different card or payment method. For example, Checkout provides feedback to the customer when a card declines and allows them to try again.

[Checkout](/payments/checkout)

To avoid declines that stem from suspected fraudulent activity, request your customers to provide their CVC and postal code during checkout. The impact of other data that you gather, such as the full billing address, might vary by card brand and country. If you continue to see elevated decline rates, Stripe recommends collecting extra customer information. You can also implement 3D Secure to authenticate payment, which can lower decline rates in countries that support it.

[3D Secure](/payments/3d-secure)

For a clear insight into why the card issuer declined the card during generic or do_not_honor declines, examine the associated data. For example, if CVC or Address Verification Service (AVS) checks fail when your customer adds a card, request your customer to verify both of these details before initiating another charge.

[do_not_honor](/declines/codes#do_not_honor)

If you notice that a customer is using a card issued in one country while operating from an IP address in another, it might be a legitimate decline due to possible unauthorized card use. However, exceptions can occur, particularly when customers are traveling internationally and use their cards from various locations.

Some customers find that their card has restrictions on the types of purchasable items. FSA or HSA cards are often limited to certain types of businesses (for example, healthcare providers), so card issuer’s decline any other type of purchase. Additionally, some card issuers might not allow purchases from certain countries or outside of their own. In either case, your customer must contact their card issuer to inquire about potential restrictions.

If your customers use cards issued in a different country than where you registered your Stripe account, they might see an increased rate of declines. To resolve this, your customer must contact their issuing bank to authorize the charge. If you have a global customer base with concentrations in various locations, you might want to set up Stripe accounts in larger markets, or in regions that encounter higher decline rates. This allows you to process charges locally.

## Declined card retries

When a payment gets declined, Stripe offers a reason for the decline and briefly suggests a resolution path.

Declined payment due to insufficient funds

If you’re a Stripe Billing user, you can create a custom retry schedule for subscriptions. If you upgrade to Billing Scale, use Smart Retries to choose the best times to retry failed payment attempts. We recommend a maximum of four retries for charges that permit retries. Card issuers might see creating additional retries as potential fraud, which can result in increased declines for legitimate charges.

[Stripe Billing](/billing)

[Billing Scale](https://stripe.com/billing/pricing)

[Smart Retries](/invoicing/automatic-collection#smart-retries)

## Manage declines programmatically

There are several ways to programmatically handle declines:

- Retrieve the last_payment_error.decline_code property from the PaymentIntent object to see why the card issuer declined the payment attempt.

[last_payment_error.decline_code](/api/payment_intents/object#payment_intent_object-last_payment_error-decline_code)

[PaymentIntent](/api/payment_intents/object)

- Iterate over the PaymentIntent’s attempted charges and inspect the failure message.

[attempted charges](/payments/payment-intents/verifying-status#identifying-charges)

[failure message](/api/charges/object#charge_object-failure_message)

- Use webhooks to monitor PaymentIntent status updates. For example, the payment_intent.payment_failed event triggers when a payment attempt is unsuccessful.

[webhooks](/payments/payment-intents/verifying-status#webhooks)

You might also need to manage additional payment failure situations such as when your customer is present (on-session) or absent (off-session) during your checkout process. As you develop your integration, Stripe advises treating all possible API exceptions, including unexpected errors.

[errors](/error-codes)

Stripe Billing handles many of these payment failure scenarios with features like Automatic Collection and Hosted Invoices.

[Stripe Billing](/billing)

[Automatic Collection](/invoicing/automatic-collection)

[Hosted Invoices](/invoicing/hosted-invoice-page)

If your customer is present in your website or application’s checkout flow, prompt them to try their payment method again or ask for a new payment method.

If your customer isn’t available to make a payment or update a payment method, notify them (for example, send them an email or in-app notification) to visit your website or application. If your business is affected by regulations like Strong Customer Authentication, payment attempts might also require authentication and fail with an authentication_required decline code. For more information on handling these scenarios, see off-session payments with saved cards.

[Strong Customer Authentication](/strong-customer-authentication)

[authentication_required](/declines/codes)

[off-session payments with saved cards](/payments/save-during-payment?platform=web#charge-saved-payment-method)

## See also

- Decline codes

[Decline codes](/declines/codes)

- Disputes and fraud

[Disputes and fraud](/disputes)
