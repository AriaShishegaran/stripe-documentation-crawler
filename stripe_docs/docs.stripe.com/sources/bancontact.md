# Bancontact payments with Sources

We deprecated the Sources API and plan to remove support for local payment methods. If you currently integrate with Bancontact using the Sources API, you must migrate to the Payment Methods API. We’ll send email communication with more information about this end of support.

[migrate to the Payment Methods API](/payments/payment-methods/transitioning)

For information about integrating Bancontact with the current APIs, see Bancontact payments.

[Bancontact payments](/payments/bancontact)

Before you can use Bancontact, you must activate it in the Dashboard. Your use of Bancontact must be in accordance with our Bancontact Terms of Service.

[Dashboard](https://dashboard.stripe.com/account/payments/settings)

[Bancontact Terms of Service](https://stripe.com/bancontact/legal)

Stripe users in Europe and the United States can accept Bancontact payments from customers in Belgium using Sources.

[Bancontact](https://www.bancontact.com/)

[Sources](/sources)

During the payment process, a Source object is created and your customer is redirected to their bank’s website or mobile application to authorize the payment. After completing this, your integration uses the source to make a charge request and complete the payment.

[Source](/api#sources)

Bancontact is a push-based, single-use and synchronous method of payment. This means your customer takes action to send the amount to you through a redirect and there is immediate confirmation about the success or failure of a payment.

[push](/sources#pull-or-push-of-funds)

[single-use](/sources#single-use-or-reusable)

[synchronous](/sources#synchronous-or-asynchronous-confirmation)

[redirect](/sources#flow-for-customer-action)

[Create a Source object](#create-source)

## Create a Source object

A Source object is either created client-side using Stripe.js or server-side using the Source creation endpoint, with the following parameters:

[Stripe.js](/payments/elements)

[Source creation endpoint](/api#create_source)

[smallest currency unit](/currencies#zero-decimal)

To create a source with Stripe.js, first include the library within your website and set your publishable API key. Once included, use the following createSource method to create a source client-side:

[Stripe.js](/payments/elements)

[publishable API key](https://dashboard.stripe.com/apikeys)

Using either method, Stripe returns a Source object containing the relevant details for the method of payment used. Information specific to Bancontact is provided within the bancontact subhash.

If you’re building an iOS or Android app, you can implement sources using our mobile SDKs. Refer to our sources documentation for iOS or Android to learn more.

[iOS](/mobile/ios/sources)

[Android](/mobile/android/sources)

Bancontact requires a statement descriptor before the customer is redirected to authenticate the payment. By default, your Stripe account’s statement descriptor is used (you can review this in the Dashboard). You can provide a custom descriptor by specifying statement_descriptor when creating a source. Bancontact statement descriptors support a maximum of 35 characters.

[statement descriptor](https://support.stripe.com/questions/when-i-charge-a-customer-what-will-they-see-on-their-card-statements)

[Dashboard](https://dashboard.stripe.com/settings/public)

Providing a custom statement descriptor within a subsequent charge request has no effect.

Source creation for Bancontact payments may return any of the following errors:

[Have the customer authorize the payment](#customer-action)

## Have the customer authorize the payment

When creating a source, its status is initially set to pending and cannot yet be used to make a charge request. Your customer must authorize a Bancontact payment to make the source chargeable. To allow your customer to authorize the payment, redirect them to the URL provided within theredirect[url] attribute of the Source object.

After the authorization process, your customer is redirected back to the URL provided as a value of redirect[return_url]. This happens regardless of whether authorization was successful or not. If the customer has authorized the payment, the Source object’s status is updated to chargeable and it is ready to use in a charge request. If your customer declines the payment, the status transitions to failed.

Stripe populates the redirect[return_url] with the following GET parameters when returning your customer to your website:

- source: a string representing the original ID of the Source object

- livemode: indicates if this is a live payment, either true or false

- client_secret: used to confirm that the returning customer is the same one who triggered the creation of the source (source IDs are not considered secret)

You may include any other GET parameters you may need when specifying redirect[return_url]. Do not use the above as parameter names yourself as these would be overridden with the values we populate.

To integrate Bancontact within a mobile application, provide your application URI scheme as the redirect[return_url] value. By doing so, your customers are returned to your app after completing authorization. Refer to our Sources documentation for iOS or Android to learn more.

[iOS](/mobile/ios/sources)

[Android](/mobile/android/sources)

If you are integrating without using our mobile SDKs, the redirect URL must be opened using the device’s native browser. The use of in-app web views and containers can prevent your customer from completing authentication—resulting in a lower conversion rate.

When creating a Source object using your test API keys, you can follow the URL returned in the redirect[url] field. This leads to a Stripe page that displays information about the API request, and where you can either authorize or cancel the payment. Authorizing the payment redirects you to the URL specified in redirect[return_url].

Alternatively, to accelerate testing, use the following value for owner[email], where xxx_ is any prefix of your choice (these patterns are significant only in testmode):

[Charge the Source](#charge-request)

## Charge the Source

Your integration must use webhooks in order for you to receive notifications of status changes on Source and Charge objects.

[webhooks](/webhooks)

Once the customer has authenticated the payment, the source’s status transitions to chargeable and it can be used to make a charge request. This transition happens asynchronously and may occur after the customer was redirected back to your website.

Some customers using Bancontact assume that the order process is complete once they have authenticated the payment and received confirmation from their bank. This results in customers who close their browser instead of following the redirect and returning to your app or website.

For these reasons it is essential that your integration rely on webhooks to determine when the source becomes chargeable in order to create a charge. Please refer to our best practices for more details on how to best integrate payment methods using webhooks.

[webhooks](/webhooks)

[best practices](/sources/best-practices)

The following webhook events are also sent to notify you about changes to the source’s status:

Once the source is chargeable, from your source.chargeable webhook handler, you can make a charge request using the source ID as the value for the source parameter to complete the payment.

Bancontact Sources are single-use and cannot be used for recurring or additional payments.

[single-use](/sources#single-use-or-reusable)

Refer to our Sources & Customers guide for more information on how single-use Sources interact with Customers.

[Sources & Customers](/sources/customers)

[Customers](/api/customers)

[Confirm that the charge has succeeded](#charge-confirmation)

## Confirm that the charge has succeeded

Since Bancontact is a synchronous payment method and the customer has already authenticated the payment as part of the redirect, unless there is an unexpected error, the Charge will immediately succeed.

[synchronous](/sources#synchronous-or-asynchronous-confirmation)

[Charge](/api#charge_object)

You will also receive the following webhook event as the charge is created:

We recommend that you rely on the charge.succeeded webhook event to notify your customer that the payment process has been completed and their order is confirmed. Please refer to our best practices for more details on how to best integrate payment methods using webhooks.

[best practices](/sources/best-practices)

The risk of fraud or unrecognized payments is extremely low with Bancontact as the customer must authenticate the payment with their bank. As such, there is no dispute process that can result in a chargeback and funds withdrawn from your Stripe account.

Payments made with Bancontact can only be submitted for refund within 180 days from the date of the original charge. After 180 days, it is no longer possible to refund the charge.

A source must be used within six hours of becoming chargeable. If it is not, its status is automatically transitioned to canceled and your integration receives a source.canceled webhook event. Additionally, pending sources are canceled after one hour if they are not used to authenticate a payment.

Once a source is canceled, the customer’s authenticated payment is refunded automatically—no money is moved into your account. For this reason, make sure the order is canceled on your end and the customer is notified once you receive the source.canceled event.

## See also

- Other supported payment methods

[Other supported payment methods](/sources)

- Sources API reference

[Sources API reference](/api#sources)

- Best practices

[Best practices](/sources/best-practices)
