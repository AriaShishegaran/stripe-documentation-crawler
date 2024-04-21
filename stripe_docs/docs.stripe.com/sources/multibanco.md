# Multibanco payments with SourcesBeta

We deprecated the Sources API and plan to remove support for local payment methods. If you currently integrate with Multibanco using the Sources API, you must migrate to the Payment Methods API. We’ll send email communication with more information about this end of support.

[migrate to the Payment Methods API](/payments/payment-methods/transitioning)

Before you can use Multibanco, you must activate it in the Dashboard. Your use of Multibanco must be in accordance with our Multibanco Terms of Service.

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

[Multibanco Terms of Service](https://stripe.com/multibanco/legal)

Stripe users in Europe and the United States can accept Multibanco payments from customers in Portugal using Sources—a single integration path for creating payments using any supported method.

[Sources](/sources)

During the payment process, a Source object is created and your customer is either redirected to the Multibanco website, your website, or a Multibanco ATM to send the funds. After completing this, your integration uses the source to make a charge request and complete the payment.

[Source](/api#sources)

Multibanco is a push-based, single-use and synchronous method of payment. This means your customer takes action to send the amount to you through a receiver.  The pushing of funds may take as little as a few minutes or at most seven days, since your customer must do this outside of your checkout flow.  Once the funds have been received the amount is immediately available to be charged. Upon charge, there is immediate confirmation about the success or failure of a payment.

[push](/sources#pull-or-push-of-funds)

[single-use](/sources#single-use-or-reusable)

[synchronous](/sources#synchronous-or-asynchronous-confirmation)

[receiver](/sources#flow-for-customer-action)

[Create a Source object](#create-source)

## Create a Source object

A Source object is either created client-side using Stripe.js or server-side using the Source creation endpoint, with the following parameters:

[Stripe.js](/payments/elements)

[Source creation endpoint](/api#create_source)

[smallest currency unit](/currencies#zero-decimal)

To create a source with Stripe.js, first include the library within your website and set your publishable API key. Once included, use the following createSource method to create a source client-side:

[Stripe.js](/payments/elements)

[publishable API key](https://dashboard.stripe.com/apikeys)

Using either method, Stripe returns a Source object containing the relevant details for the method of payment used. Information specific to Multibanco is provided within the multibanco subhash.

If you’re building an iOS or Android app, you can implement sources using our mobile SDKs. Refer to our sources documentation for iOS or Android to learn more.

[iOS](/mobile/ios/sources)

[Android](/mobile/android/sources)

[Have the customer send the funds](#customer-action)

## Have the customer send the funds

When creating a source, its status is initially set to pending and cannot yet be used to make a charge request.  To pay with Multibanco, your customers will need to initiate a transfer of funds from their bank account using reference and entity numbers provided by you and either their computer, phone, or local ATM.

Portuguese merchants will often display these details within their checkout flow after the customer has confirmed their purchase and by including them in an order confirmation email.

You may also redirect your customer to a Multibanco-hosted page that will display these details for you, by using the URL provided within theredirect[url] attribute of the Source object. Multibanco then redirects them back to the URL provided as a value of redirect[return_url], regardless of whether funds have been sent or not.

When the customer does send funds, the Source object’s status will transition to chargeable, allowing you to charge the source and complete the transaction.  If you don’t do this, the status will transition to canceled after six hours.

Stripe populates the redirect[return_url] with the following GET parameters when returning your customer to your website:

- source: a string representing the original ID of the Source object

- livemode: indicates if this is a live payment, either true or false

- client_secret: used to confirm that the returning customer is the same one who triggered the creation of the source (source IDs are not considered secret)

You may include any other GET parameters you may need when specifying redirect[return_url]. Do not use the above as parameter names yourself as these would be overridden with the values we populate.

To integrate Multibanco within a mobile application, provide your application URI scheme as the redirect[return_url] value. By doing so, your customers are returned to your app after completing authorization. Refer to our Sources documentation for iOS or Android to learn more.

[iOS](/mobile/ios/sources)

[Android](/mobile/android/sources)

When creating a Source object using your test API keys, the test payment is fulfilled with a three second delay. Use one of the following test email addresses when you need to test Multibanco payments under different conditions.

The URL returned in the redirect[url] field of takes you to a sample payment page.  Returning from this page takes you to the URL specified in redirect[return_url].

[Charge the Source](#charge-request)

## Charge the Source

Your integration must use webhooks in order for you to receive notifications of status changes on Source and Charge objects.

[webhooks](/webhooks)

Once the customer has pushed the funds, the source’s status transitions to chargeable and it can be used to make a charge request. This transition happens asynchronously and may occur after the customer was redirected back to your website.

It may take minutes, hours, or days for a customer to send the funds after following and returning from the redirect.

For this reason it is essential that your integration rely on webhooks to determine when the source becomes chargeable in order to create a charge. Please refer to our best practices for more details on how to best integrate payment methods using webhooks.

[webhooks](/webhooks)

[best practices](/sources/best-practices)

The following webhook events are sent to notify you about changes to the source’s status:

Once the source is chargeable, from your source.chargeable webhook handler, you can make a charge request using the source ID as the value for the source parameter to complete the payment.

Multibanco Sources are single-use and cannot be used for recurring or additional payments. Refer to our Sources & Customers guide for more information on how single-use Sources interact with Customers.

[single-use](/sources#single-use-or-reusable)

[Sources & Customers](/sources/customers)

[Customers](/api/customers)

[Confirm that the charge has succeeded](#charge-confirmation)

## Confirm that the charge has succeeded

Since Multibanco is a synchronous payment method and the customer has already sent funds, unless there is an unexpected error, the Charge will immediately succeed.

[synchronous](/sources#synchronous-or-asynchronous-confirmation)

[Charge](/api#charge_object)

You will also receive the following webhook event as the charge is created:

We recommend that you rely on the charge.succeeded webhook event to notify your customer that the payment process has been completed and their order is confirmed. Please refer to our best practices for more details on how to best integrate payment methods using webhooks.

[best practices](/sources/best-practices)

The risk of fraud or unrecognized payments is extremely low with Multibanco as the customer has to push funds from their bank account. As such, there is no dispute process that can result in a chargeback and funds withdrawn from your Stripe account.

As a customer can make a payment at any time directly through the ATM, it is possible, although unlikely, for a customer to supply funds to a canceled or expired source.  In these cases, Stripe automatically initiates the refund process for the mispaid amount as described above.

Payments made with Multibanco can only be submitted for refund within 180 days from the date of the original charge. After 180 days, it is no longer possible to refund the charge.

Multibanco payments can be refunded through either the Dashboard or API. Multibanco does not itself provide any facility for refunds, and so Stripe handles this by creating an IBAN credit transfer.  We contact the customer at the email address provided during source creation, and a credit is sent to the customer once they’ve supplied their account information. No interaction from the merchant is required beyond the initial refund request.

[Dashboard](https://dashboard.stripe.com/test/payments)

[API](/api#create_refund)

Some users may want to manage the collection of the refund IBAN details themselves. Multibanco refunds require the customer’s IBAN number, account holder name, and the full address including street, city, country, and postal code. Please contact us to learn more about this option.

[contact us](https://support.stripe.com/email)

A chargeable Multibanco source must be charged within six hours of becoming chargeable. If it is not, its status is automatically transitioned to canceled and your integration receives a source.canceled webhook event. Once a chargeable source is canceled, the customer’s authenticated Multibanco payment is refunded automatically—no money is moved into your account. For this reason, make sure the order is canceled on your end and the customer is notified when you receive the source.canceled event.

Additionally, pending sources are canceled after seven days if they are not used to receive funds.  This ensures that all sources eventually transition out of their pending state to the canceled state if they are not used.

## See also

- Other supported payment methods

[Other supported payment methods](/sources)

- Sources API reference

[Sources API reference](/api#sources)

- Best practices

[Best practices](/sources/best-practices)
