# Card payments with SourcesDeprecated

Stripe recommends using the Payment Intents API instead of this API. With a PaymentIntent integration, you can use Dynamic 3D Secure, which helps you avoid declined payments due to Strong Customer Authentication regulation in Europe. To get started, follow the Accept a payment guide.

[Payment Intents API](/payments/payment-intents)

[Dynamic 3D Secure](/payments/3d-secure/authentication-flow#three-ds-radar)

[Strong Customer Authentication](/strong-customer-authentication)

[Accept a payment](/payments/accept-a-payment)

Stripe users can process card payments from customers around the world using Sources—a single integration path for creating payments using any supported method. During the payment process, your integration creates a source representing the card information. This source is then used in a charge request to debit the card and complete the payment.

[Sources](/sources)

Within the scope of Sources, cards are a pull-based, reusable and synchronous method of payment. This means that, after capturing the customer’s card details, you can debit arbitrary amounts from the customer’s card without them having to take any additional action and there is immediate confirmation about the success or failure of a payment.

[pull](/sources#pull-or-push-of-funds)

[reusable](/sources#single-use-or-reusable)

[synchronous](/sources#synchronous-or-asynchronous-confirmation)

## Handling card information

Card information is sensitive by nature. Card sources must be created client-side using Stripe.js and Elements. This ensures that no sensitive card data passes through your server so your integration can operate in a PCI compliant way.

[Stripe.js and Elements](/payments/elements)

[PCI compliant](https://stripe.com/guides/pci-compliance)

When your customer submits their card information using your payment form, it is sent directly to Stripe, and a representative Source object is returned for you to use. The process is similar to the creation of tokens. If you’re already using Elements to tokenize card information, switching to Sources is only a small change.

[Source](/api#sources)

[tokens](/api/tokens)

[Prerequisite: Consider a flexible checkout flow if you want to accept additional payment methods](#considerations)

## Prerequisite: Consider a flexible checkout flow if you want to accept additional payment methods

Card payments with Sources has fewer steps and requirements than other payment methods. As it’s a synchronous method and there is no additional customer action to take, the use of webhooks isn’t necessary. If you only want to accept card payments, you can simply follow the steps within this documentation to begin accepting cards with Sources.

[webhooks](/webhooks)

However, accepting other methods of payment through Sources (for example, iDEAL, SEPA Direct Debit, and so on) requires additional steps, making the use of webhooks necessary. You can refer to our best practices for developing a flexible checkout flow that supports different payment methods.

[iDEAL](/sources/ideal)

[SEPA Direct Debit](/sources/sepa-debit)

[best practices](/sources/best-practices)

[Create a Source object](#create-source)

## Create a Source object

This guide supplements our Stripe.js and Elements documentation with specific usage for Sources.

[Stripe.js and Elements](/payments/elements)

To create a card Source client-side, please refer to Accept a payment. You then create a Source object instead of a Token by calling the createSource instead of the createToken method.

[Accept a payment](/payments/accept-a-payment-charges#web-create-token)

You can also provide an optional owner dictionary containing additional cardholder information, such as their name and full billing address.

[owner](/api#create_source-owner)

If your Elements payment form collects a billing postal code, it’s used as the value for the owner field address[postal_code] during source creation. This also overrides any value that is being provided separately as part of owner. If you are already collecting your customer’s billing postal code elsewhere on your checkout page, we recommend including it as part of owner and hiding the Elements postal code field—set the Element option of hidePostalCode to true.

[Element option](/js/elements_object/create_element?type=card#elements_create-options-hidePostalCode)

The last steps of the Accept a payment guide remain similar and consist of submitting the source, along with any additional information that has been collected, to your server.

[Accept a payment](/payments/accept-a-payment-charges#web-submit-payment)

When the source is created, its status immediately changes to chargeable. No additional customer action is needed so the source can be used right away. Information about the card is provided within the card subhash.

[card](/api#cards)

As card payments are a pull-based payment method, there is no movement of funds during the creation of a source. Only when a successful charge request has been made is the customer’s card debited and you receive the funds.

If you’re building an iOS or Android app, you can implement sources using our mobile SDKs. Refer to our sources documentation for iOS or Android to learn more.

[iOS](/mobile/ios/sources)

[Android](/mobile/android/sources)

[Charge the Source](#charge-request)

## Charge the Source

After creating a card Source, and before creating a charge request to complete the payment, attach it to a Customer for later reuse.

[Customer](/api#customers)

Attaching the Source to a Customer is required for you to reuse it for future payments. Please refer to our Sources & Customers guide for more details on how to attach Sources to new or existing Customers and how the two objects interact together. The following snippet attaches the Source to a new Customer:

[Customer](/api/customers)

[Sources & Customers](/sources/customers)

Once attached, you can use the Source object’s ID along with the Customer object’s ID to perform a charge request and finalize the payment.

A card source must be used within a few minutes of its creation as CVC information is only available for a short amount of time. Card sources do not expire, but using them after a delay can result in a charge request that is performed without CVC information. The consequences of this can be higher decline rates and increased risk of fraud.

Although the status of the source is chargeable, this does not mean that the payment is going to be successful. A charge request can still fail if the customer’s card issuer declines the payment.

[declines](/declines)

[Confirm that the charge has succeeded](#charge-confirmation)

## Confirm that the charge has succeeded

Card payments are a synchronous method so confirmation of the charge’s status happens in real-time.

[synchronous](/sources#synchronous-or-asynchronous-confirmation)

Your integration immediately receives the result of the charge request—either a Charge object upon success or an exception upon failure. Once the charge has been confirmed as successful, the payment has been successfully completed and you can notify your customer and fulfill the order.

[Charge](/api#charges)

If you’re making use of webhooks, your integration also receives either of the following events:

[webhooks](/webhooks)

Card networks provide a process for cardholders to dispute payments made with their card. A dispute can be filed by the cardholder any time after a payment has been successful. It is still possible for a successful payment to be reversed if the card issuer investigates a dispute and decides it should be refunded.

[dispute](/disputes)

Disputes can be made for a variety of reasons. As such, you should make the appropriate decisions regarding your business and how you manage disputes, if they occur, and how to avoid them completely.

You can update the card[exp_month] and card[exp_year] attributes of card sources, allowing you to update their expiration date:

## See also

- Declines & failed payments

[Declines & failed payments](/declines)

- Other supported payment methods

[Other supported payment methods](/sources)

- Sources API reference

[Sources API reference](/api#sources)

- Best practices

[Best practices](/sources/best-practices)
