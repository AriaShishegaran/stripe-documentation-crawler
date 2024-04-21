# Disputed PayPal payments

The risk of fraud or unrecognized PayPal payments is low because the customer must authenticate the payment with their PayPal account.

## Overview

Customers must authenticate any payment with their PayPal account to decrease the risk of fraud. However, customers can dispute PayPal payments if for example:

- They don’t receive the goods they paid for

- The received goods don’t match their description

Note that your settlement choice when activating PayPal affects the funds flow for PayPal disputes. See Choose settlement preference for more context.

[Choose settlement preference](/payments/paypal/choose-settlement-preference#refunds-and-disputes)

## Dispute process

Customers can file a dispute on PayPal up to 180 calendar days from the date of purchase. They can also file a dispute through the payment instrument they used to complete the PayPal purchase (such as their bank).

After the customer initiates a dispute, Stripe notifies you through:

- Email

- The Stripe Dashboard

[Stripe Dashboard](https://dashboard.stripe.com/disputes)

- An API charge.dispute.created event (if your integration is set up to receive webhooks)

[webhooks](/webhooks)

- Push notification (if you’ve subscribed)

Depending on the type of dispute and where it was filed, PayPal might offer the ability for you to communicate directly with the customer in an attempt to resolve the dispute before countering it. Currently, Stripe doesn’t offer this functionality and requests that you turn to PayPal to contact the customer.

If no agreement is reached, you can either accept or counter the dispute. If you choose to counter, Stripe requests that you submit evidence that you fulfilled the purchase order in the Stripe Dashboard. This evidence helps PayPal determine if a dispute is valid or if they should reject it. The evidence you provide must contain as much detail as possible from what the customer provided at checkout. You must submit the requested information within 19 calendar days. PayPal aims to make a decision within 30 calendar days of evidence submission.

[submit evidence](/disputes/responding#respond)

[Stripe Dashboard](/disputes/responding#respond)

If you prefer to handle disputes programmatically, you can respond to disputes using the API.

[respond to disputes using the API](/disputes/api)

## Dispute resolution

If PayPal resolves the dispute with you winning, the disputed amount will be returned to your balance.

If PayPal rules in favor of the customer, the dispute is lost and the balance charge becomes permanent.

In some cases, PayPal will allow a lost dispute to be appealed. Currently, Stripe does not support appeals and requests that you turn to PayPal to file an appeal. In these cases, the dispute will remain open on Stripe until a final resolution has been reached by PayPal. Please refer to PayPal to be notified on when a dispute becomes appealable.

Read more about disputes on how disputes work and best practices for responding to disputes.

[how disputes work](/disputes/how-disputes-work)

[best practices for responding to disputes](/disputes/best-practices)

## Fees

PayPal might charge fees for disputes. The terms and amount of PayPal dispute fees are set by PayPal. Stripe does not charge any additional fees for PayPal disputes.

## Testing your integration

Stripe allows you to simulate a disputed transaction by specifying email values that match the patterns described in test scenarios when you create a PaymentIntent (as part of the billing details). You can choose from the different test scenarios to simulate disputes of all relevant categories.

[disputed transaction](/disputes)

[test scenarios](#scenarios)

[billing details](/api/payment_intents/create#create_payment_intent-payment_method_data-billing_details)

For example, creating the PaymentIntent server-side and simulating a disputed transaction where the buyer claims they didn’t receive the product looks like:

If using Checkout or Payment Links, you can enter the email in the checkout form. Shortly after the payment has been completed, it will be disputed as product_not_received.

[Checkout](/payments/checkout)

[Payment Links](/no-code/payment-links)

The table below displays the scenarios available to test. Each scenario produces a dispute shortly after a payment has been completed.

.* represents any valid character in an email. For example, the pattern .*dispute_duplicate@.* is matched by an email such as my_dispute_duplicate@mycompany.com.

To simulate winning or losing the dispute, respond with one of the evidence values from the table below.

- If you respond using the API, pass the value from the table as uncategorized_text.

[respond using the API](/disputes/api)

[uncategorized_text](/api/disputes/update#update_dispute-evidence-uncategorized_text)

- If you respond in the Dashboard, enter the value from the table in the Additional information field. Then, click Submit evidence.

[respond in the Dashboard](/disputes/responding)
