# WeChat Pay payments with SourcesBeta

We deprecated the Sources API and plan to remove support for local payment methods. If you currently integrate with WeChat Pay using the Sources API, you must migrate to the Payment Methods API. We’ll send email communication with more information about this end of support.

[migrate to the Payment Methods API](/payments/payment-methods/transitioning)

For information about integrating WeChat Pay with the current APIs, see WeChat Pay payments.

[WeChat Pay payments](/payments/wechat-pay)

Stripe users can use Sources—a single integration path for creating payments using any supported method—to accept WeChat Pay payments from customers from China.

[Sources](/sources)

[WeChat Pay](https://pay.weixin.qq.com/index.php/public/wechatpay)

During the payment process, a Source object is created and you receive a WeChat Pay URL that is used to authorize the payment in the WeChat app by scanning a QR code. After completing this, your integration uses the source to make a charge request and complete the payment.

[Source](/api#sources)

WeChat Pay is a push-based, single-use and synchronous method of payment. This means that once your customer takes action to authorize the charge there is immediate confirmation about the success or failure of a payment.

[push](/sources#pull-or-push-of-funds)

[single-use](/sources#single-use-or-reusable)

[synchronous](/sources#synchronous-or-asynchronous-confirmation)

[Create a Source object](#create-source)

## Create a Source object

A Source object is either created client-side using Stripe.js or server-side using the Source creation endpoint, with the following parameters:

[Stripe.js](/payments/elements)

[Source creation endpoint](/api#create_source)

[smallest currency unit](/currencies#zero-decimal)

To create a source with Stripe.js, first include the library within your website and set your publishable API key. Once included, use the following createSource method to create a source client-side:

[Stripe.js](/payments/elements)

[publishable API key](https://dashboard.stripe.com/apikeys)

Using either method, Stripe returns a Source object containing the relevant details for the method of payment used. Information specific to WeChat is provided within the wechat subhash.

WeChat Pay can accept a statement descriptor before the customer is redirected to authorize the payment. By default, your Stripe account’s statement descriptor is used (you can review this in the Dashboard). You can provide a custom descriptor by specifying statement_descriptor when creating a source. WeChat statement descriptors support a maximum of 32 characters.

[statement descriptor](https://support.stripe.com/questions/when-i-charge-a-customer-what-will-they-see-on-their-card-statements)

[Dashboard](https://dashboard.stripe.com/settings/public)

Providing a custom statement descriptor within a subsequent charge request has no effect.

Source creation for WeChat Pay payments may return any of the following errors:

[Have the customer authorize the payment](#customer-action)

## Have the customer authorize the payment

When creating a source, its status is initially set to pending and cannot yet be used to make a charge request. Your customer must authorize a WeChat Pay payment to make the source chargeable.

To do so, you will need to show the customer a QR code created from the URL provided within wechat[qr_code_url].

After the authorization process, if the customer has authorized the payment, the Source object’s status will transition to chargeable; it is then ready to be used in a charge request. If your customer declines the payment, the status will transition to failed.

To receive notifications of status changes on Source objects, your integration must use webhooks.

[webhooks](/webhooks)

For sources created in test mode, the wechat[qr_code_url] can be scanned using any QR Code scanning application rather than WeChat. The URL leads to a Stripe page that displays information about the API request, and where you can either authorize or cancel the payment.

[Charge the Source](#charge-request)

## Charge the Source

Once the customer has authorized the payment, the source’s status transitions to chargeable and it can be used to make a charge request. This transition happens asynchronously.

Some customers using WeChat Pay will assume that the order process is complete once they have authorized the payment and received confirmation on WeChat Pay’s app. It is essential that your integration rely on webhooks to determine when the source becomes chargeable in order to create a charge. See our best practices for more details on how to best integrate payment methods using webhooks.

[webhooks](/webhooks)

[best practices](/sources/best-practices)

The following webhook events are sent to notify you about changes to the source’s status:

Once the source is chargeable, from your source.chargeable webhook handler, you can make a charge request using the source ID as the value for the source parameter to complete the payment.

WeChat Pay Sources are single-use and cannot be used for recurring or additional payments. Learn more about using Sources with Customer objects.

[single-use](/sources#single-use-or-reusable)

[Sources with Customer objects](/sources/customers)

[Confirm that the charge has succeeded](#charge-confirmation)

## Confirm that the charge has succeeded

Since WeChat Pay is a synchronous payment method and the customer has already authorized the payment using the WeChat application, the Charge will immediately succeed unless there’s an unexpected error.

[synchronous](/sources#synchronous-or-asynchronous-confirmation)

[Charge](/api#charge_object)

You receive the following webhook event when the charge succeeds:

Stripe recommends that you rely on the charge.succeeded webhook event to notify your customer that the payment process has been completed and their order is confirmed. See best practices for more details on integrating payment methods using webhooks.

[best practices](/sources/best-practices)

If a customer’s WeChat Pay account is used illicitly, WeChat Pay and Stripe handle the issue internally. In the context of WeChat Pay, payments are only disputed if the customer has a complaint about the provided goods or service. Should a dispute occur, a charge.dispute.created webhook event is sent, and Stripe deducts the amount of the dispute from your Stripe balance.

Payments made with WeChat Pay can only be submitted for refund within 180 days from the date of the original charge. After 180 days, it is no longer possible to refund the charge.

A WeChat Pay source must be charged within six hours of becoming chargeable, or before 23:45 China Standard Time (GMT+8) due to Chinese government restrictions around settlement. If it is not, its status is automatically transitioned to canceled and your integration receives a source.canceled webhook event. Once a chargeable source is canceled, the customer’s authorized WeChat Pay payment is refunded automatically—no money is moved into your account. For this reason, make sure the order is canceled on your end and the customer is notified when you receive the source.canceled event.

Additionally, pending sources are canceled after one hour if they are not used to authorize a payment, ensuring that all sources eventually transition out of their pending state to the canceled state if they are not used.

## See also

- Other supported payment methods

[Other supported payment methods](/sources)

- Sources API reference

[Sources API reference](/api#sources)

- Best practices

[Best practices](/sources/best-practices)
