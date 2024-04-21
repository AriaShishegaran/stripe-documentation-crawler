# Alipay payments with Sources

We deprecated the Sources API and plan to remove support for local payment methods. If you currently integrate with Alipay using the Sources API, you must migrate to the Payment Methods API. We’ll send email communication with more information about this end of support.

[migrate to the Payment Methods API](/payments/payment-methods/transitioning)

For information about integrating Alipay with the current APIs, see Alipay payments.

[Alipay payments](/payments/alipay)

Stripe users can use Sources to accept Alipay payments from customers from China.

[Sources](/sources)

[Alipay](https://alipay.com/)

During the payment process, a Source object is created and your customer is redirected to Alipay for authorization. After completing this, your integration uses the source to make a charge request and complete the payment.

[Source](/api#sources)

Alipay is a push-based, single-use  and synchronous method of payment. This means that your customer takes action to authorize the push of funds through a redirect. There is immediate confirmation about the success or failure of a payment.

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

Using either method, Stripe returns a Source object containing the relevant details for the method of payment used. Information specific to Alipay is provided within the alipay subhash.

Source creation for Alipay payments may return any of the following errors:

[Have the customer complete authorization](#customer-action)

## Have the customer complete authorization

When creating a source, its status is initially set to pending and cannot yet be used to make a charge request. Your customer must authorize an Alipay payment to make the source chargeable. To allow your customer to authorize the payment, redirect them to the URL provided within theredirect[url] attribute of the Source object.

After the authorization process, your customer is redirected back to the URL provided as a value of redirect[return_url]. This happens regardless of whether authorization was successful or not. If the customer has authorized the payment, the Source object’s status will transition to chargeable when it is ready to be used in a charge request. If your customer declines the payment, the status will transition to failed.

Stripe populates the redirect[return_url] with the following GET parameters when returning your customer to your website:

- source: a string representing the original ID of the Source object

- livemode: indicates if this is a live payment, either true or false

- client_secret: used to confirm that the returning customer is the same one who triggered the creation of the source (source IDs are not considered secret)

You may include any other GET parameters you may need when specifying redirect[return_url]. Do not use the above as parameter names yourself as these would be overridden with the values we populate.

To integrate Alipay within a mobile application, provide your application URI scheme as the redirect[return_url] value. By doing so, your customers are returned to your app after completing authorization. Direct redirects to the Alipay app are also supported when using our native SDKs.

For Android sources, the Alipay SDK is required for app-to-app support.

[Alipay SDK](https://doc.open.alipay.com/doc2/detail.htm?treeId=54&articleId=104509&docType=1)

When creating a Source object using your test API keys, you can follow the URL returned in the redirect[url] field. This leads to a Stripe page that displays information about the API request, and where you can either authorize or cancel the payment. Authorizing the payment redirects you to the URL specified in redirect[return_url].

[Charge the Source](#charge-request)

## Charge the Source

Your integration must use webhooks in order for you to receive notifications of status changes on Source and Charge objects.

[webhooks](/webhooks)

Once the customer has authorized the payment, the source’s status transitions to chargeable and it can be used to make one charge request. This transition happens asynchronously and may occur after the customer was redirected back to your website.

Some customers using Alipay assume that the order process is complete once they have authorized the payment and received confirmation on Alipay’s site or app. This results in customers who close their browser instead of following the redirect and returning to your app or website.

For these reasons it is essential that your integration rely on webhooks to determine when the source becomes chargeable in order to create a charge. Please refer to our best practices for more details on how to best integrate payment methods using webhooks.

[webhooks](/webhooks)

[best practices](/sources/best-practices)

The following webhook events are sent to notify you about changes to the source’s status:

Once the source is chargeable, from your source.chargeable webhook handler, you can make a charge request using the source ID as the value for the source parameter to complete the payment.

By default, your account’s statement descriptor appears on customer statements whenever you create an Alipay payment.

[statement descriptor](/get-started/account/statement-descriptors)

Charge creation for Alipay payments may return any of the following errors:

[Confirm that the charge has succeeded](#charge-confirmation)

## Confirm that the charge has succeeded

Since the customer has already authorized the payment as part of the redirect, unless there is an unexpected error, the Charge will immediately succeed.

[Charge](/api#charge_object)

You will also receive the following webhook event as the charge is created:

We recommend that you rely on the charge.succeeded webhook event to notify your customer that the payment process has been completed and their order is confirmed. Please refer to our best practices for more details on how to best integrate payment methods using webhooks.

[best practices](/sources/best-practices)

## Disputed payments

If a customer’s Alipay account is used illicitly, Alipay and Stripe handle the issue internally. Alipay payments are disputed only if the customer has a complaint about the provided goods or service. Should a dispute occur, a charge.dispute.created webhook event is sent to your webhook endpoint, and Stripe deducts the amount of the dispute from your Stripe balance.

## Refunds

Payments made with Alipay can only be submitted for refund within 90 days from the date of the original charge. After 90 days, it is no longer possible to refund the charge.

## Single-use Sources expiration

A single-use Alipay source must be charged within six hours of becoming chargeable, or before 23:45 China Standard Time (GMT+8) due to Chinese government restrictions around settlement. If it is not, its status is automatically transitioned to canceled and your integration receives a source.canceled webhook event. Once a chargeable source is canceled, the customer’s authorized Alipay payment is refunded automatically—no money is moved into your account. For this reason, make sure the order is canceled on your end and the customer is notified when you receive the source.canceled event.

Additionally, pending sources are canceled after one hour if they are not used to authorize a payment, ensuring that all sources eventually transition out of their pending state to the canceled state if they are not used.

## Settlement currencies

Alipay supports settlement in the default currency of your account. If you have a bank account in another currency and would like to create Alipay sources in that currency, please get in touch. Support for additional currencies is provided on a case-by-case basis.

[get in touch](https://support.stripe.com/email)

## See also

- Other supported payment methods

[Other supported payment methods](/sources)

- Sources API reference

[Sources API reference](/api#sources)

- Best practices

[Best practices](/sources/best-practices)
