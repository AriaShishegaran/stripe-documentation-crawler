# SEPA Direct Debit payments with Sources

We deprecated the Sources API and plan to remove support for local payment methods. If you currently integrate with SEPA Direct Debit using the Sources API, you must migrate to the Payment Methods API. We’ll send email communication with more information about this end of support.

[migrate to the Payment Methods API](/payments/payment-methods/transitioning)

For information about integrating SEPA Direct Debit with the current APIs, see SEPA Direct Debit payments.

[SEPA Direct Debit payments](/payments/sepa-debit)

Stripe users in Europe and the United States can use Sources—a single integration path for creating payments using any supported method—to accept SEPA Direct Debit payments from customers in countries within the Single Euro Payments Area.

[Sources](/sources)

[Single Euro Payments Area](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area)

During the payment process, your integration collects your customer’s EUR-denominated IBAN bank account information. SEPA Direct Debits require the bank account holder to accept a mandate (debit authorization) that allows you to debit their account. A Source object is then created and your integration uses this to make a charge request and complete the payment.

[IBAN](https://en.wikipedia.org/wiki/International_Bank_Account_Number)

[mandate](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit/sdd-mandate)

Within the scope of Sources, SEPA Direct Debit is a pull-based, reusable and asynchronous method of payment. This means that you take action to debit the amount from the customer’s account. It can take up to 14 business days to confirm the success or failure of a payment.

[pull](/sources#pull-or-push-of-funds)

[reusable](/sources#single-use-or-reusable)

[asynchronous](/sources#synchronous-or-asynchronous-confirmation)

SEPA direct debit transactions have a limit of 10,000 EUR each. For new users, there’s an additional weekly limit of 10,000 EUR, which quickly increases as you process more SEPA direct debit payments. If you need higher limits, please contact support.

[contact support](https://support.stripe.com/contact)

[Prerequisite: Collect mandate acceptance](#prerequisite)

## Prerequisite: Collect mandate acceptance

Before a source can be created, your customer must accept the SEPA Direct Debit mandate. Their acceptance authorizes you to collect payments for the specified amount from their bank account using SEPA Direct Debit.

[SEPA Direct Debit mandate](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit/sdd-mandate)

The mandate text is also available for download in other languages from the European Payments Council.

[European Payments Council](https://www.europeanpaymentscouncil.eu/other/core-sdd-mandate-translations)

When your customer confirms the payment they are making, they are also accepting a mandate. Their acceptance authorizes you to collect payments for the specified amount from their bank account via SEPA Direct Debit. You must display the following standard authorization text, replacing Rocketship Inc. with your company name, close to the payment confirmation button so that your customer can read and accept it.

By providing your IBAN and confirming this payment, you authorise (A) Rocketship Inc. and Stripe, our payment service provider, to send instructions to your bank to debit your account and (B) your bank to debit your account in accordance with those instructions. You are entitled to a refund from your bank under the terms and conditions of your agreement with your bank. A refund must be claimed within 8 weeks starting from the date on which your account was debited.

The details of the accepted mandate is generated as part of the Source object creation. A URL to view the mandate is returned as the value for sepa_debit[mandate_url]. Since this is the mandate that the customer has implicitly signed when accepting the terms suggested above, it must be communicated to them, either on the payment confirmation page or by email.

[Create a Source object](#create-source)

## Create a Source object

Bank account information is sensitive by nature. To securely collect your customer’s IBAN details and create a source, use Stripe.js and the IBAN Element. This prevents your customer’s bank account information from touching your server and reduces the amount of sensitive data that you need to handle securely.

[Stripe.js](/payments/elements)

[IBAN Element](/payments/sepa-debit)

Follow the IBAN Element Quickstart to create your payment form, collect your customers’ IBAN, and create a source. Once you’ve created a source object, you can proceed to charge the source in the next step.

[IBAN Element Quickstart](/payments/sepa-debit)

If you choose to handle bank account numbers yourself, you can create your own form and call stripe.createSource as described in the Stripe.js reference. When doing so, make sure to collect the following information from your customer:

[Stripe.js reference](/js#stripe-create-source)

[Sources API](/api/sources/create#create_source-owner-address)

Use Stripe.js to create a SEPA Direct Debit source. Although doing so is optional, if you forgo this step and pass the information directly to Stripe when creating a Source object, you must take appropriate steps to safeguard the sensitive bank information that passes through your servers.

Only IBANs with the following country codes require the owner address: AD, PF, TF, GI, GB, GG, VA, IM, JE, MC, NC, BL, PM, SM, CH, WF

Using either method, Stripe returns a Source object containing the relevant details for the method of payment used. Information specific to SEPA Direct Debit is provided within the sepa_debit subhash.

As SEPA Direct Debit payments are a pull-based payment method, there is no movement of funds during the creation of a source. Only when a successful charge request has been made is the customer’s bank account debited and you eventually receive the funds.

If you’re building an iOS or Android app, you can implement sources using our mobile SDKs. Refer to our sources documentation for iOS or Android to learn more.

[iOS](/mobile/ios/sources)

[Android](/mobile/android/sources)

Source creation for SEPA Direct Debit payments may return any of the following errors:

[Charge the source](#charge-request)

## Charge the source

Unlike most other payment methods, SEPA Direct Debit payments do not require any customer action after the source has been created. Once the customer has provided their IBAN details and accepted the mandate, no further action is needed and the resulting source is directly chargeable.

Before creating a charge request to complete the payment, you should attach the source to a Customer for later reuse.

[Customer](/api#customers)

You must attach a source to a Customer object if you plan to reuse it for future payments (for example, with a billing product).

[Customer](/api#customers)

[billing product](/billing)

Refer to our sources and customers documentation for more details on how to attach sources to new or existing Customer objects and how they interact together.

[sources and customers](/sources/customers)

Once attached, you can use the Source object’s ID along with the Customer object’s ID to perform a charge request and finalize the payment.

The resulting Charge object is created with a status of pending. At this stage, the payment is in progress.

[Charge](/api#charge_object)

By default, your account’s statement descriptor appears on customer statements whenever you create a SEPA Direct Debit payment. If you need to provide a custom description for a payment, include the statement_descriptor parameter when making a charge request. Statement descriptors are limited to 22 characters and cannot use the special characters <, >, ', or ".

[statement descriptor](/get-started/account/activate#public-business-information)

[Confirm that the charge has succeeded](#charge-confirmation)

## Confirm that the charge has succeeded

Your integration must use webhooks in order for you to receive notifications of status changes on Source and Charge objects.

[webhooks](/webhooks)

SEPA Direct Debit payments are an asynchronous method, so funds are not immediately available. A charge created from a SEPA Direct Debit source can remain in a pending state for up to 14 business days from its creation, though the average time is around five business days. Once the charge is confirmed, its status is updated to succeeded.

[asynchronous](/sources#synchronous-or-asynchronous-confirmation)

The following events are sent when the charge’s status is updated:

After confirming that the charge has succeeded, notify your customer that the payment process has been completed and their order is confirmed. Refer to our best practices for more details on how to best integrate payment methods using webhooks.

[best practices](/sources/best-practices)

[webhooks](/webhooks)

A charge is successful once we receive funds from the customer’s bank. However, this often occurs before the bank has debited their customer’s bank account. If there is a problem debiting the customer’s bank account after a charge has been successful, the funds are retrieved in the form of a dispute.

[dispute](#disputed-payments)

## Testing Sepa Direct Debit

You can mimic a successful or failed charge by first creating a test source with one of the following test IBAN account numbers. Use the resulting source in a charge request to create a test charge that is either successful or failed.

## Handling failed charges

If a charge is not confirmed, its status automatically transitions from pending to failed. Should a charge fail, notify your customer immediately upon receipt of the charge.failed event. When using SEPA Direct Debit, you may prefer not to fulfill orders until the charge.succeeded webhook has been received.

[webhook](/webhooks)

If a SEPA Direct Debit charge fails and we have reason to believe that subsequent charges will also fail, we will update the source to failed.

SEPA Direct Debit charges can fail due to exceeding your rolling-window processing limits. If charging the source fails with error code charge_exceeds_source_limit, then you can retry the charge later. Please get in touch if you need to request higher processing limits.

[get in touch](https://support.stripe.com/email)

## Notifying customers of recurring payments

The SEPA Direct Debit rulebook requires that you notify your customer each time a debit is to be made on their account. You can send these notifications separately or together with other documents (for example, an invoice).

[SEPA Direct Debit rulebook](http://www.europeanpaymentscouncil.eu/index.cfm/sepa-direct-debit/sepa-direct-debit-core-scheme-sdd-core)

[invoice](/api/invoices)

These notifications should be sent at least 14 calendar days before you create a payment. You can send them closer to the payment date as long as your mandate makes it clear when your customer can expect to receive them. The mandate provided by Stripe specifies this can happen up to two calendar days in advance of future payments, allowing you to send notifications during charge creation. For recurring payments of the same amount (for example, a subscription of a fixed amount), you may indicate multiple upcoming debits with corresponding dates in a single notice.

[subscription](/billing/subscriptions/creating)

When sending your customers a notice, it must include:

- The last 4 digits of the debtor’s bank account

- The mandate reference (sepa_debit[mandate_reference] on the Source object)

- The amount to be debited

- Your SEPA creditor identifier

- Your contact information

Source objects provide tooling to help you notify your users compliantly. At Source creation it is possible to specify a mandate[notification_method]. The possible values are the following:

By default, mandate[notification_method] is set to none at Source creation but can be updated later.

This section applies to EU businesses only.

For EU businesses, your SEPA creditor identifier is associated with each SEPA Direct Debit payment instruction and identifies the company making the payment. While companies may have multiple creditor identifiers, each creditor identifier is unique and allows your customers to easily identify the debits on their account. This can help reduce the likelihood of disputed payments. Some payment providers don’t request that you provide your own SEPA creditor identifier. Stripe requests a SEPA creditor identifier to improve the experience of your customers.

[SEPA creditor identifier](https://www.sepa.ch/en/home/direct-debits/creditor-identifier.html)

You can request a SEPA creditor identifier from a financial institution in the country in which you have your main office or residence. For example, you can request the SEPA creditor identifier from the bank that holds your account. This is commonly done online and can sometimes take a few days. In some cases, your bank may take additional steps to issue a creditor identifier. When contacting your bank for your SEPA creditor identifier, clarify that you are not requesting they process SEPA Direct Debit payments for you.

If you have trouble obtaining your creditor identifier, let us know.

[let us know](https://support.stripe.com/contact)

## Disputed payments

For more details on the SEPA Direct Debit dispute process, consult the SEPA Direct Debit rulebook.

[SEPA Direct Debit rulebook](https://www.europeanpaymentscouncil.eu/what-we-do/sepa-payment-schemes/sepa-direct-debit/sepa-direct-debit-core-rulebook-and)

SEPA Direct Debit provides a dispute process for bank account holders to dispute payments. As such, you should make the appropriate decisions regarding your business and how you approach SEPA Direct Debit payments.

For a period of eight weeks after their account was debited, an account holder can dispute a payment through their bank on a “no questions asked” basis. Any disputes within this period are automatically honored.

Beyond the eight-week period after the creation of the payment, and for up to 13 months, a customer may only dispute a payment with their bank if they consider the debit had not been authorized. In this event, we automatically provide the customer’s bank with the mandate that the customer approved. This does not guarantee that the dispute can be canceled as the customer’s bank can still decide that the debit was not authorized by the mandate—and that their customer is entitled to a refund.

A dispute can also occur if the customer’s bank is unable to debit their account because of a problem (for example, the account is frozen or has insufficient funds), but it has already provided the funds to make a charge successful. In this instance, the bank reclaims those funds in the form of a dispute.

If a dispute is created, a charge.dispute.created webhook event is sent and Stripe deducts the amount of the dispute and dispute fee from your Stripe balance. This fee varies based on your account’s default settlement currency:

Unlike credit card disputes, all SEPA Direct Debit disputes are final and there is no appeals process. If a customer successfully disputes a payment, you must reach out to them if you would like to resolve the situation. If you’re able to come to an arrangement and your customer is willing to return the funds to you, they will need to make a new payment.

[credit card disputes](/disputes)

In general, each dispute includes the reason for its creation, though this can vary from country to country. For instance, disputed payments in Germany do not provide additional information for privacy reasons.

## Refunds

Partial refunds on SEPA Direct Debit payments are not supported in the Dashboard. Instead, you can use the API to create a partial refund.

[create a partial refund](/api#create_refund)

Payments made with SEPA Direct Debit can only be submitted for refund within 180 days from the date of the original charge. After 180 days, it is no longer possible to refund the charge. Similar to the delays introduced to payments with SEPA Direct Debit, refunds also require additional time to process (typically 3-4 business days). Should you accidentally debit your customer, please contact them immediately to avoid having the payment disputed.

A refund can only be processed after the payment process has completed. If you create a full or partial refund on a payment that hasn’t yet been completed, the refund is actioned once the Charge object’s status has transitioned to succeeded. In the event of a payment where the Charge object’s status transitioned to failed, full and partial refunds are marked as canceled, as the money never left the customer’s bank account.

SEPA does not explicitly label refunds when the funds are deposited back to the customer’s account. Instead, they are processed as a credit and include a visible reference to the original payment’s statement descriptor.

Due to longer settlement time periods and the nature of how banks process SEPA Direct Debit transactions, there is potential for confusion between you, your customer, your customer’s bank, and Stripe. For instance, your customer may contact both you and their bank to dispute a payment. If you proactively issue your customer a refund while the customer’s bank also initiates the dispute process, your customer could end up receiving two credits for the same transaction.

When issuing a refund, it’s important that you immediately inform your customer that it may take up to five business days for the refund to arrive in their bank account.

## See also

- Other supported payment methods

[Other supported payment methods](/sources)

- Sources API reference

[Sources API reference](/api#sources)

- Best practices

[Best practices](/sources/best-practices)
