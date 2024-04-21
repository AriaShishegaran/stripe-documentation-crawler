htmlWeChat Pay payments with Sources | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsources%2Fwechat-pay)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsources%2Fwechat-pay)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# WeChat Pay payments with SourcesBeta

Use Sources to accept payments using WeChat Pay, a popular payment method in China.WarningWe deprecated the Sources API and plan to remove support for local payment methods. If you currently integrate with WeChat Pay using the Sources API, you must migrate to the Payment Methods API. We’ll send email communication with more information about this end of support.

For information about integrating WeChat Pay with the current APIs, see WeChat Pay payments.

Stripe users can use Sources—a single integration path for creating payments using any supported method—to accept WeChat Pay payments from customers from China.

During the payment process, a Source object is created and you receive a WeChat Pay URL that is used to authorize the payment in the WeChat app by scanning a QR code. After completing this, your integration uses the source to make a charge request and complete the payment.

WeChat Pay is a push-based, single-use and synchronous method of payment. This means that once your customer takes action to authorize the charge there is immediate confirmation about the success or failure of a payment.

[Create a Source object](#create-source)A Source object is either created client-side using Stripe.js or server-side using the Source creation endpoint, with the following parameters:

ParameterValue`type`wechat`amount`A positive integer in the[smallest currency unit](/currencies#zero-decimal)representing the amount to charge the customer (for example,1099for a 10.99 USD payment).`currency`The currency of the payment.  Must be the default currency for your country. Can beaud,cad,eur,gbp,hkd,jpy,sgd, orusd.`statement_descriptor`(optional)A custom statement descriptor for the payment.To create a source with Stripe.js, first include the library within your website and set your publishable API key. Once included, use the following createSource method to create a source client-side:

`stripe.createSource({
  type: 'wechat',
  amount: 1099,
  currency: 'usd',
}).then(function(result) {
  // handle result.error or result.source
});`Using either method, Stripe returns a Source object containing the relevant details for the method of payment used. Information specific to WeChat is provided within the wechat subhash.

`{
  "id": "src_18eYalAHEMiOZZp1l9ZTjSU0",
  "object": "source",
  "amount": 1099,
  "client_secret": "src_client_secret_UfwvW2WHpZ0s3QEn9g5x7waU",
  "created": 1445277809,
  "currency": "usd",
  "flow": "none",
  "livemode": true,
  "metadata": {},`See all 27 lines### Optional: Provide a custom statement descriptor

WeChat Pay can accept a statement descriptor before the customer is redirected to authorize the payment. By default, your Stripe account’s statement descriptor is used (you can review this in the Dashboard). You can provide a custom descriptor by specifying statement_descriptor when creating a source. WeChat statement descriptors support a maximum of 32 characters.

`stripe.createSource({
  type: 'wechat',
  amount: 1099,
  currency: 'usd',
  statement_descriptor: 'ORDER AT11990',
  owner: {
    name: 'Jenny Rosen',
  },
}).then(function(result) {
  // handle result.error or result.source
});`Providing a custom statement descriptor within a subsequent charge request has no effect.

### Error codes

Source creation for WeChat Pay payments may return any of the following errors:

ErrorDescription`payment_method_not_available`The payment method is currently not available. You should invite your customer to fallback to another payment method to proceed.`processing_error`An unexpected error occurred preventing us from creating the source. The source creation should be retried.[Have the customer authorize the payment](#customer-action)When creating a source, its status is initially set to pending and cannot yet be used to make a charge request. Your customer must authorize a WeChat Pay payment to make the source chargeable.

To do so, you will need to show the customer a QR code created from the URL provided within wechat[qr_code_url].

After the authorization process, if the customer has authorized the payment, the Source object’s status will transition to chargeable; it is then ready to be used in a charge request. If your customer declines the payment, the status will transition to failed.

To receive notifications of status changes on Source objects, your integration must use webhooks.

### Testing

For sources created in test mode, the wechat[qr_code_url] can be scanned using any QR Code scanning application rather than WeChat. The URL leads to a Stripe page that displays information about the API request, and where you can either authorize or cancel the payment.

[Charge the Source](#charge-request)Once the customer has authorized the payment, the source’s status transitions to chargeable and it can be used to make a charge request. This transition happens asynchronously.

Some customers using WeChat Pay will assume that the order process is complete once they have authorized the payment and received confirmation on WeChat Pay’s app. It is essential that your integration rely on webhooks to determine when the source becomes chargeable in order to create a charge. See our best practices for more details on how to best integrate payment methods using webhooks.

### Webhooks

The following webhook events are sent to notify you about changes to the source’s status:

EventDescription`source.chargeable`A`Source`object becomes`chargeable`after a customer has authorized and verified a payment.`source.failed`A`Source`object failed to become chargeable as your customer declined to authorize the payment.`source.canceled`A`Source`object expired and cannot be used to create a charge.### Make a charge request using the source

Once the source is chargeable, from your source.chargeable webhook handler, you can make a charge request using the source ID as the value for the source parameter to complete the payment.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d amount="1099" \
  -d currency="usd" \
  -d source=src_18eYalAHEMiOZZp1l9ZTjSU0`WeChat Pay Sources are single-use and cannot be used for recurring or additional payments. Learn more about using Sources with Customer objects.

[Confirm that the charge has succeeded](#charge-confirmation)Since WeChat Pay is a synchronous payment method and the customer has already authorized the payment using the WeChat application, the Charge will immediately succeed unless there’s an unexpected error.

You receive the following webhook event when the charge succeeds:

EventDescription`charge.succeeded`The charge succeeded and the payment is complete.Stripe recommends that you rely on the charge.succeeded webhook event to notify your customer that the payment process has been completed and their order is confirmed. See best practices for more details on integrating payment methods using webhooks.

### Disputed payments

If a customer’s WeChat Pay account is used illicitly, WeChat Pay and Stripe handle the issue internally. In the context of WeChat Pay, payments are only disputed if the customer has a complaint about the provided goods or service. Should a dispute occur, a charge.dispute.created webhook event is sent, and Stripe deducts the amount of the dispute from your Stripe balance.

### Refunds

Payments made with WeChat Pay can only be submitted for refund within 180 days from the date of the original charge. After 180 days, it is no longer possible to refund the charge.

### Sources expiration

A WeChat Pay source must be charged within six hours of becoming chargeable, or before 23:45 China Standard Time (GMT+8) due to Chinese government restrictions around settlement. If it is not, its status is automatically transitioned to canceled and your integration receives a source.canceled webhook event. Once a chargeable source is canceled, the customer’s authorized WeChat Pay payment is refunded automatically—no money is moved into your account. For this reason, make sure the order is canceled on your end and the customer is notified when you receive the source.canceled event.

Additionally, pending sources are canceled after one hour if they are not used to authorize a payment, ensuring that all sources eventually transition out of their pending state to the canceled state if they are not used.

## See also

- [Other supported payment methods](/sources)
- [Sources API reference](/api#sources)
- [Best practices](/sources/best-practices)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a Source object](#create-source)[Have the customer authorize the payment](#customer-action)[Charge the Source](#charge-request)[Confirm that the charge has succeeded](#charge-confirmation)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`