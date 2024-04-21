# The Sources APIDeprecated

As of September 2019, a regulation called Strong Customer Authentication (SCA) requires businesses in Europe to request additional authentication for online payments. Businesses based in the European Economic Area (EEA) with customers in the EEA should follow the accept a payment guide to use the Payment Intents API to meet these rules.

[Strong Customer Authentication](/strong-customer-authentication)

[European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)

[accept a payment](/payments/accept-a-payment)

We deprecated the Sources API and plan to remove support for local payment methods. If you currently handle any local payment methods using the Sources API, you must migrate them to the Payment Methods API. We’ll send email communication with more information about this end of support.

[migrate them to the Payment Methods API](/payments/payment-methods/transitioning)

While we don’t plan to remove support for card payments, we recommend replacing any use of the Sources API with the PaymentMethods API, which provides access to our latest features and payment method types.

[PaymentMethods API](/api/payment_methods)

Source objects allow you to accept a variety of payment methods with a single API. A source represents a customer’s payment instrument, and can be used with the Stripe API to create payments. Sources can be charged directly, or attached to customers for later reuse.

[Source](/api#sources)

Each payment method supported by the Sources API is defined by four key characteristics. The combination of these characteristics determines how a source is made chargeable, and how it is used in a charge request to complete a payment.

[payment method supported](#supported-payment-methods)

- Pull or push: How the funds for the method of payment are transferred from your customer

[Pull or push](#pull-or-push-of-funds)

- Flow: The type of action your customer must take to authenticate the payment

[Flow](#flow-for-customer-action)

- Usage: Whether the Source is reusable or not

[Usage](#single-use-or-reusable)

- Synchronous or asynchronous: Whether the resulting charge can be confirmed immediately, or only after a delay

[Synchronous or asynchronous](#synchronous-or-asynchronous-confirmation)

For a complete example illustrating how to accept any payment method using the Sources API, check out this sample e-commerce store, and browse its source code on GitHub.

[sample e-commerce store](https://stripe-payments-demo.appspot.com)

[source code on GitHub](https://github.com/stripe/stripe-payments-demo)

## Supported payment methods

You can enable any payment method available to you within the Dashboard. Activation is generally instantaneous, and does not require additional contracts nor include a lengthy process. For a detailed listing, take a look at the available payment methods and their supported geographical regions.

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

[supported geographical regions](https://stripe.com/payments/payment-methods-guide#payment-methods-fact-sheets)

The following table maps the aforementioned key characteristics to the supported payment methods:

[Cards](/sources/cards)

[ACH debits with authentication](/ach-deprecated)

[ACH debits with microdeposits](/ach-deprecated)

- Alipay (Deprecated)

- Bancontact (Deprecated)

- giropay (Deprecated)

- iDEAL (Deprecated)

- Przelewy24 (Deprecated)

- WeChat Pay (Deprecated)

## Pull or push of funds

Each method of payment is categorized as either pull or push, depending on how funds are transferred from the customer’s payment method.

- Using a pull method, you debit the funds from the customer’s account after the customer has provided consent. Card payments are an example of a pull method: your customer’s card is debited when a payment is made, and no customer interaction is required for subsequent debits.

[Card payments](/sources/cards)

- Using a push method, the customer sends the funds to you. ACH Credit Transfers are an example of a push method: Your customer is provided with bank routing and account numbers to which they should send (push) the correct amount. After confirmation that your customer has sent the funds to you, the source becomes chargeable, and is ready to be used in a charge request. Other push payment methods, such as iDEAL or Sofort, rely on a redirect for your customer to push the money to you directly from their online bank account. Generally, push methods require a customer interaction for each payment.

## Flow for customer action

Certain payment methods require your customer to complete a particular action (flow) before the source is chargeable. The type of flow that applies to a payment method is stated within the Source object’s flow parameter. Each method is categorized into one of the following flow types.

No action is required from your customer. Some payment methods (generally pull methods), such as cards (excluding 3D Secure), require no additional authentication beyond collecting the payment information from customers. Sources representing this payment method can be used immediately when making charge requests.

Once the required flow has been completed and a source becomes chargeable, the source must be used to make a charge request for the payment to be completed. If not, the source is canceled and the customer’s authenticated payment is refunded automatically—no money is moved into your account.

## Single-use or reusable

Certain payment methods allow for the creation of sources that can be reused for additional payments without your customer needing to complete the payment process again. Sources that can be reused have their usage parameter set to reusable.

Conversely, if a source can only be used once, this parameter is set to single_use, and a source must be created each time a customer makes a payment. Such sources should not be attached to customers—instead, they should be charged directly. They can be charged only once, and their status will change to consumed when charged.

Reusable sources must be attached to a Customer in order to be reused. (If charged directly, their status will change to consumed.) To learn how to attach Sources to Customers, and to manage a Customer’s sources list, refer to the Sources and Customers guide.

[Customer](/api#customers)

[Customers](/api/customers)

[Sources and Customers](/sources/customers)

## Synchronous or asynchronous confirmation

Once you use a payment method to create a Charge object, that charge’s status can be confirmed either immediately (synchronously), or after a certain amount of time (asynchronously).

[Charge](/api#charges)

- With a synchronous payment method, the charge request’s status can be immediately confirmed as either succeeded or failed. If the charge request is successful, the payment is completed—it’s considered guaranteed that the customer has been charged, and that you’ll receive the funds. Card payments are an example of a synchronous payment method: there is real-time confirmation of the payment’s success or failure.

With a synchronous payment method, the charge request’s status can be immediately confirmed as either succeeded or failed. If the charge request is successful, the payment is completed—it’s considered guaranteed that the customer has been charged, and that you’ll receive the funds. Card payments are an example of a synchronous payment method: there is real-time confirmation of the payment’s success or failure.

- For asynchronous payment methods, it can take up to several days to confirm whether the payment has been successful. During this time, the payment cannot be guaranteed. The status of the payment’s Charge object is initially set to pending, until the payment has been confirmed as successful or failed.  ACH debits are an example of an asynchronous method: with these debits, it takes a few days to confirm that the payment has succeeded.

For asynchronous payment methods, it can take up to several days to confirm whether the payment has been successful. During this time, the payment cannot be guaranteed. The status of the payment’s Charge object is initially set to pending, until the payment has been confirmed as successful or failed.  ACH debits are an example of an asynchronous method: with these debits, it takes a few days to confirm that the payment has succeeded.

Stripe sends a webhook event once a charge’s status has changed. When accepting any payment method that is asynchronous, your integration must be able to receive webhooks, so that it can receive this notification and confirm whether the customer’s payment was successful or has failed.

[webhook](/webhooks)

## See also

- Sources API reference

[Sources API reference](/api#sources)

- Best practices using Sources

[Best practices using Sources](/sources/best-practices)

- Payment methods guide

[Payment methods guide](https://stripe.com/payments/payment-methods-guide)
