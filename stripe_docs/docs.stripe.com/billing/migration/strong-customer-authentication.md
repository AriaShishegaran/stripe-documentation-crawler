# SCA migration guide for Billing

As of April 2021, issuing banks in India have started taking steps to block transactions that don’t comply with the Reserve Bank of India’s (RBI) directive on the processing of e-mandates for recurring transactions. Businesses with customers in India should implement the changes outlined in this guide to prevent seeing higher payment failure rates on recurring transactions. Learn more on our dedicated support page.

[directive on the processing of e-mandates](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668)

[dedicated support page](https://support.stripe.com/questions/background-on-indian-government-regulations-affecting-card-payments)

Beginning September 14, 2019, PSD2 regulation requires Strong Customer Authentication for many online payments made by European customers. Businesses based in the European Economic Area (EEA) with customers in the EEA should implement the changes outlined in this guide to prevent declined payments.

[Strong Customer Authentication](/strong-customer-authentication)

[European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)

## Strong Customer Authentication

Strong Customer Authentication (SCA), a regulation that took effect on September 14, 2019, as part of PSD2 in Europe, requires changes to how your European customers authenticate online payments. This regulation applies to online payments where the customer’s bank and the business are both in the European Economic Area (EEA).

[Strong Customer Authentication (SCA)](/strong-customer-authentication)

[applies](/strong-customer-authentication)

[European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)

SCA requires that businesses use two independent authentication elements to verify payments. In practice, this means adding a new payment step where your customers must confirm their payment using an authentication method like a password, hardware token, or biometric. 3D Secure 2 is the primary authentication method used to meet SCA requirements for card payments.

[independent authentication elements](https://stripe.com/guides/strong-customer-authentication#what-is-strong-customer-authentication)

[3D Secure 2](https://stripe.com/guides/3d-secure-2)

Transactions that don’t meet these authentication requirements and that don’t qualify for an exemption may be declined.

## Stripe Billing changes

Due to the increased payment friction caused by SCA, you can expect longer collection times and lower conversion rates. The changes to Stripe Billing allow you to maximize your revenue under these constraints. These changes include:

- New subscription statuses to facilitate initial payment

[subscription statuses](#summary-statuses)

- PaymentIntents that are now exposed on invoices as a mechanism for multi-state payments

[PaymentIntents](#summary-payment-intents)

[invoices](/api/invoices)

- SetupIntents that can be used to collect authentication while customers are on-session

[SetupIntents](#summary-pending-setup-intent)

- A new webhook that indicates when SCA is required for payment

[webhook](#summary-webhooks)

- An updated Hosted Invoice Page allowing customers to complete the authentication step required by SCA

[Hosted Invoice Page](#hip)

- A new set of dunning emails to help collect payment when SCA is required

[dunning emails](/invoicing/integration/send-email)

## How SCA impacts Billing

SCA impacts card charges between EEA businesses and EEA customers. This changes how on-session and off-session payments are made.

[exempt](#sca-exemptions)

## Using previous authorization agreements

You can use Previous authorization agreements for off-session payments when they meet the following criteria:

[Previous authorization agreements](/strong-customer-authentication/previous-authorization-agreements)

- Cards from EU customers saved before December 31, 2020

- Cards from UK customers saved before September 14, 2021

For the following scenarios, this means that you don’t have to save the cards again and re-authenticate these customers. If you use Stripe for non-recurring payments, refer to the out of scope payments guide.

[out of scope payments](/strong-customer-authentication/previous-authorization-agreements#preparing)

[off_session](/api/subscriptions/create#create_subscription-off_session)

[creating a trial subscription](/billing/subscriptions/trials)

[passing a token, source, or payment method](/saving-cards)

[Pay](/api/invoices/pay)

[create a one-off invoice](/invoicing/dashboard#create-invoice)

## Updating your Billing integration to support SCA

The updates you need to make to your integration depend on how you use Stripe Billing. There are four possible scenarios you need to manage to support SCA. You need to evaluate your integration against these scenarios to find out which ones apply to you.

- Scenario 1: Charging customers on-session for their initial payment

[Scenario 1](#scenario-1)

- Scenario 2: Charging customers off-session for their initial payment

[Scenario 2](#scenario-2)

- Scenario 3: Managing recurring charges after customers make their first payment

[Scenario 3](#scenario-3)

- Scenario 4: One-off invoices

[Scenario 4](#scenario-4)

The first scenario applies to you if you immediately charge your customers when they subscribe. This means that your customer’s first payment is on-session. The second scenario applies to you if you don’t immediately charge your customers when they subscribe, and their initial payment occurs when they’re off-session.

The third scenario applies to most Billing users because it’s for managing recurring payments. These are any payments that occur after the first payment is made. The fourth scenario only applies to you if you use one-off invoices.

[one-off invoices](/invoicing/dashboard#create-invoice)

Regardless of the scenarios that apply to your integration, when you create subscriptions, you can expand the latest_invoice.payment_intent attribute to determine the outcome of a payment. You can also expand pending_setup_intent when handling subscriptions without an initial payment as shown in scenario 2.

[subscriptions](/billing/subscriptions/creating)

[expand](/api/expanding_objects)

[latest_invoice.payment_intent](/api/subscriptions/object#subscription_object-latest_invoice)

[pending_setup_intent](/api/subscriptions/object#subscription_object-pending_setup_intent)

[scenario 2](#scenario-2)

## Scenario 1: Charging customers on-session for their initial payment

When charging immediately, your customers’ first charge for a subscription requires SCA. This means you need to add handling for authentication in your application checkout or signup flow. When setting up a subscription for the first time, customers are on-session. This means that they’re on a browser or app and able to react to your prompts.

When setting up a subscription that bills immediately, Stripe attempts to charge the card on file for your customer as part of the Create Subscription or Create Customer call which generates the subscription.

[Create Subscription](/api/subscriptions/create)

[Create Customer](/api/customers/create)

Subscriptions have new incomplete statuses that you need to use to support SCA. However, you have two options for accessing these statuses. The first option allows you to remain on an older API version but requires you to pass a flag in some of your API calls. The second option is upgrading your API version. The options are explained in subsequent sections but the diagrams below provide an overview of the subscription behavior with these statuses.

[incomplete statuses](/billing/migration/strong-customer-authentication#summary-statuses)

When a payment succeeds, the subscription’s status is set to active and no further action is required. When a payment fails, the subscription’s status is set to incomplete and the latest_invoice.payment_intent.status attribute is set to requires_payment_method. In these situations, you should charge the customer with another payment method using the Pay Invoice endpoint.

[Pay Invoice](/api/invoices/pay)

When a payment requires SCA, the subscription’s status is set to incomplete and the latest_invoice.payment_intent.status attribute is set to requires_action. In these situations, you need your customer to complete a 3D Secure authentication flow using latest_invoice.payment_intent. The next step explains how to do this.

[3D Secure](https://stripe.com/guides/3d-secure-2)

[next step](/billing/migration/strong-customer-authentication#scenario-1-handling-sca)

You can use the regulatory test cards to explore this behavior in your test environment. For detailed instructions on how to build a complete subscriptions integration, see the integration guide.

[regulatory test cards](/testing#regulatory-cards)

[integration guide](/billing/subscriptions/build-subscriptions)

If you don’t upgrade your API version, but pass a new payment_behavior=allow_incomplete flag on subscription create and update calls, your subscriptions will use the new incomplete status functionality. This allows you to manage scenarios that require SCA, which is explained in the next step. See the FAQ at the bottom of this document for a complete list of endpoints you need to pass this flag to.

[payment_behavior=allow_incomplete](/api/subscriptions/create#create_subscription-payment_behavior)

[incomplete status](/billing/migration/strong-customer-authentication#summary-statuses)

[next step](/billing/migration/strong-customer-authentication#scenario-1-handling-sca)

[FAQ](#faq)

If you don’t upgrade your API version, and don’t pass the payment_behavior flag, attempts to create subscriptions that require SCA will fail and return a card_error. This is consistent with legacy behavior that blocks subscription creation if payment fails.

[card_error](/api/errors#errors-card_error)

If you upgrade to API version 2019-03-14 or newer, your subscriptions automatically use the new incomplete status functionality. After upgrading your API, you can move on to the next step.

[2019-03-14](/upgrades#2019-03-14)

[incomplete status](/billing/migration/strong-customer-authentication#summary-statuses)

[next step](/billing/migration/strong-customer-authentication#scenario-1-handling-sca)

In order to complete payment on a charge that requires SCA, you can either use Stripe.js or a browser-redirect flow. Stripe.js is recommended because most Stripe users already use it, and it makes it easier to manage 3DS authentication. Using Stripe.js involves passing the latest_invoice.payment_intent.client_secret into the confirmCardPayment method, which displays a modal that allows the customer to provide authentication for their payment.

[Stripe.js](/payments/elements)

[confirmCardPayment](/js#stripe-confirm-card-payment)

Alternatively, if you prefer to not use Stripe.js, you can pass a return_url to the PaymentIntent confirmation endpoint and initiate a redirect flow:

[https://www.example.com/return_url](https://www.example.com/return_url)

For more details about using the Payment Intents API to complete 3D Secure authentication for Billing, see the overview guide.

[Payment Intents API](/payments/payment-intents)

[3D Secure](/payments/3d-secure)

[overview guide](/billing/subscriptions/overview#requires-action)

After the customer successfully completes the redirect or modal flow, the subscription status is active and the invoice status is paid. Be aware that the customer might quit their browser after authentication, but before being redirected. To provide more robust handling, Stripe recommends listening to invoice webhooks as described in the next step.

[webhooks](/webhooks)

It’s possible for customers to leave their browser before the confirmCardPayment callback executes, or before the return_url redirect occurs. In these cases, your application might not be aware that payment is complete, and the associated product might not be provisioned for your customer. You can avoid these situations by listening to the invoice.paid event notification to verify that the invoice is paid and billing_reason=subscription_create. This means you can provision the subscription for your customer.

[invoice.paid](/api/events/types#event_types-invoice.paid)

## Scenario 2: Charging customers off-session for their initial payment

Creating subscriptions with free trials, using metered billing, and invoices discounted through coupons or customer balances often result in non-payment invoices. This means the customer isn’t immediately charged when the subscription is created. In these situations, you need to save the customer’s payment information and authenticate their card while they’re on-session so that you can charge them later.

[free trials](/billing/subscriptions/trials)

[metered billing](/products-prices/pricing-models#usage-based-pricing)

[save the customer’s payment information](/payments/save-and-reuse)

To manage situations like this, Stripe created the Setup Intents API, which allows you to:

[Setup Intents API](/api/setup_intents)

- Collect payment information

- Authenticate the customer’s card

- Authorize the customer’s card without charging it

Collecting payment information upfront and authenticating payments allows Stripe to apply for exemptions on your behalf. These exemptions generally decrease the chance that 3DS is required when you charge customers off-session.

If subscription creation does not require an initial payment and if authentication is recommended while the customer is on-session, Stripe Billing automatically creates a SetupIntent. This is exposed on the Subscription object through the pending_setup_intent attribute. See the Using SetupIntents section to learn more about SetupIntents and how to use them with Billing. To create subscriptions and charge customers off-session for their initial payment, you need to:

[pending_setup_intent](/api/subscriptions/object#subscription_object-pending_setup_intent)

[Using SetupIntents](/billing/subscriptions/overview#using-setupintents)

- Use CreatePaymentMethod to collect payment information

[CreatePaymentMethod](/js#stripe-create-payment-method)

- Create a customer using the ID of the PaymentMethod you created

[Create a customer](/api/customers/create#create_customer-payment_method)

[PaymentMethod](/api/payment_methods)

- Create the subscription

[Create the subscription](/api/subscriptions/create)

- Set up error handling using confirmCardSetup for authentication failures and confirmCardPayment for authorization failures

[confirmCardSetup](/js#stripe-confirm-card-setup)

[confirmCardPayment](/js#stripe-confirm-card-payment)

You can also use SetupIntents to change the payment method on a customer or subscription. The saving cards without payment section explains how to do this at the customer level. At the subscription level, Stripe automatically updates the pending_setup_intent field on the subscription object if authentication is recommended on the updated default payment method.

[saving cards without payment](/payments/save-and-reuse)

## Scenario 3: Managing recurring charges after customers make their first payment

Recurring charges usually occur when customers are off-session. If no exemptions apply to the charge, and SCA is required, you need to bring your user on-session so they can complete the payment. To do this, you can use Stripe’s prebuilt tools or create your own solution. The diagram below explains these options in more detail.

[exemptions](/billing/migration/strong-customer-authentication#sca-exemptions)

When a billing cycle date or a subscription threshold is reached, payment for the associated subscription is attempted. If the charge requires SCA, the subscription status changes to past_due. With Stripe’s tools, you can enable a set of emails specific to 3D Secure to be sent to your customers when SCA is required. Alternatively, if you want to send your own emails but don’t want to build your own authentication flow, you can use our Hosted Invoice Page.

[set of emails](#settings-3ds-payment)

[Hosted Invoice Page](#hip)

If you choose to build your own solution, you can listen to the new invoice.payment_action_required webhook or the existing customer.subscription.updated webhook to be notified of subscriptions that become past_due because of SCA requirements. When this happens, you need to bring your customer back on-session and have them complete an authentication flow similar to what is explained in the first scenario.

[first scenario](#scenario-1)

After the payment is authenticated and succeeds, the subscription status updates to active and the invoice status updates to paid.

## Scenario 4: One-off invoices

One-off invoices can also be subject to SCA. The changes you need to make to manage one-off invoices depends on how you use Billing today. If you already use our Hosted Invoice Page, you get SCA support out of the box without making any changes. If you use collection_method=charge_automatically, you might need to bring the customer back on-session to complete SCA. You can do so with our Hosted Invoice Page, or through the custom handling described in the third scenario.

[third scenario](#scenario-3)

If your application uses the Pay Invoice endpoint, you either need to start using the Hosted Invoice Page or build custom handling because this endpoint will return an HTTP 402 error when SCA is required. If you choose to build custom handling, you need to use the invoice’s PaymentIntent to drive the payment to completion. You also need to set off_session when attempting to pay an invoice using the endpoint.

[Pay Invoice](/api/invoices/pay)

[off_session](/api/invoices/pay#pay_invoice-off_session)

## Tools for collecting off-session payments

Stripe Billing offers a set of prebuilt tools that can automatically handle payments that require 3D Secure authentication.

This demo shows a sample invoice payment.

You can choose to have Stripe:

- Email your customers when an off-session payment requires 3D Secure authentication

- Schedule follow-up emails reminding customers to complete authentication

- Provide a link to a hosted invoice page where customers can complete authentication

You can customize emails and the hosted invoice page in your Branding settings.

[Branding settings](https://dashboard.stripe.com/account/branding)

The following table outlines the various actions you or Stripe can take to trigger SCA and whether or not Stripe considers the action on-session or off-session by default. For actions that are off-session, Stripe sends an authentication link if the SCA email setting is enabled.

The API actions for creating subscriptions, updating subscriptions, and paying invoices also have an off_session attribute that you can set manually. Setting this attribute to true indicates the payment is off-session, and false indicates the payment is on-session.

## Emails and dunning

You can send a dunning email to customers for overdue payments to increase recovery chances. Our suite of customer emails has been updated to include notifications for when 3D Secure authentication is required for off-session payments. This is in addition to support for sending invoices, receipts, and failed payment notifications.

[dunning email](/invoicing/integration/send-email)

## 3D Secure payment settings

You can schedule when to send 3D Secure emails and you can determine what effect non-payment has on subscriptions. Use the Billing settings in the Stripe Dashboard to configure these settings.

[Billing settings](https://dashboard.stripe.com/settings/billing/automatic)

A configurable email template is available to automatically send your customers an email asking them to authenticate to complete payment for their invoice or subscription.

## Hosted Invoice Page

Stripe Billing provides a Hosted Invoice Page that supports all invoices. To support SCA requirements, this page can now manage 3D Secure authentication.

[Hosted Invoice Page](/invoicing/hosted-invoice-page)

[3D Secure](https://stripe.com/guides/3d-secure-2)

If an off-session payment requires the customer to complete 3D Secure authentication, you can send them a link to a hosted invoice page. On the hosted invoice page, the customer can confirm their payment or add a new payment method if one is needed. After confirming their payment, the customer can complete authentication with their bank using a 3D Secure 2 modal that is displayed.

## SCA exemptions

The SCA regulation contains a set of exemptions. These exemptions mean that your customers might not need to provide additional authentication to confirm some payments. Stripe’s goal is to optimize your payment flow and attempt to automatically apply as many exemptions as possible in order to reduce the likelihood of your customers needing to authenticate.

[set of exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication)

## Summary of API changes

The API contains several updates to help manage SCA requirements and the authentication flow.

Two statuses have been added to the Subscription resource: incomplete and incomplete_expired. Subscriptions enter the incomplete status only when the first charge is attempted and either fails or requires SCA. Any subscription that remains in the incomplete state and is not successfully paid expires after 23 hours. This automatically changes the status to incomplete_expired. After a subscription is active it cannot enter incomplete again. Future payments that require SCA result in the subscription being past_due.

[statuses](/billing/subscriptions/overview#subscription-lifecycle)

Users on API version 2019-03-14 or newer automatically have access to this functionality. If you’re on an older API version, you need to use the payment_behavior flag to use these new statuses.

[2019-03-14](/upgrades#2019-03-14)

[payment_behavior](/api/subscriptions/create#create_subscription-payment_behavior)

The subscription’s latest_invoice field provides a reference to the invoice affecting the status of a subscription. This change is additive to all API versions.

The Payment Intents API is Stripe’s new payment API that manages the lifecycle of a payment. This includes a new requires_action payment status and a next_action attribute. These additions indicate how to complete payment, which is usually done through a redirect to the cardholder’s bank for authentication or using a URL embedded within the response. The Invoice object now has a payment_intent you can use to manage the payment lifecycle, in addition to the existing charge attribute.

[Payment Intents API](/api/payment_intents)

This change is additive to all API versions and is backwards compatible. You can still use the charge attribute to manage payments, but if your business needs to support SCA and wants future compatibility with other payment methods that require authentication, Stripe recommends using the payment_intent attribute.

Invoices for Stripe Billing are fully compatible with the Payment Intents API, so you get the benefit of the Stripe.js helper functions to assist with your checkout payment flow. Specifically, the confirmCardPayment JavaScript function helps you display a 3D Secure modal to collect the authentication information needed to complete payment. This change is only relevant if you use PaymentIntents.

[confirmCardPayment](/js#stripe-confirm-card-payment)

When an invoice requires customer action, Stripe sends a new invoice.payment_action_required webhook containing the associated invoice. This webhook is meant to complement existing invoice.paid and invoice.payment_failed webhooks. This change is additive to all API versions. Existing Stripe Billing users that are not concerned with SCA can ignore this webhook.

Subscription’s now have a pending_setup_intent attribute that references a SetupIntent. This SetupIntent can be used to collect authentication while customers are on-session, which optimizes off-session payments. This change is additive to all API versions.

## Frequently asked questions (FAQ)

- Does SCA apply to my business?Strong Customer Authentication (SCA) regulations apply to online payments where the cardholder’s bank and the business’s payment provider are both in the European Economic Area (EEA). Read more in the Strong Customer Authentication Overview.

Does SCA apply to my business?

Strong Customer Authentication (SCA) regulations apply to online payments where the cardholder’s bank and the business’s payment provider are both in the European Economic Area (EEA). Read more in the Strong Customer Authentication Overview.

[Customer](/api/customers)

[Strong Customer Authentication Overview](/strong-customer-authentication)

- What payment methods require SCA?Strong Customer Authentication will apply to “customer-initiated” online payments within Europe. As a result, most card payments and all bank transfers will require SCA. The major integration changes that are required pertain to cards, as documented in this guide. Bank transfers won’t require an integration change because it’s up to the customer’s bank to authenticate transfers using their existing online bank interface.

What payment methods require SCA?

Strong Customer Authentication will apply to “customer-initiated” online payments within Europe. As a result, most card payments and all bank transfers will require SCA. The major integration changes that are required pertain to cards, as documented in this guide. Bank transfers won’t require an integration change because it’s up to the customer’s bank to authenticate transfers using their existing online bank interface.

[“customer-initiated” online payments within Europe](https://stripe.com/guides/strong-customer-authentication#when-is-strong-customer-authentication-required)

- What happens if I don’t upgrade my integration, or start passing the payment_behavior flag?Calls to create or update subscriptions that result in charges requiring SCA will fail with an HTTP 402 error. Similarly, calls to the Pay Invoice endpoint will fail. As a result you might experience an overall increase in payment failures.

What happens if I don’t upgrade my integration, or start passing the payment_behavior flag?

Calls to create or update subscriptions that result in charges requiring SCA will fail with an HTTP 402 error. Similarly, calls to the Pay Invoice endpoint will fail. As a result you might experience an overall increase in payment failures.

[Pay Invoice](/api/invoices/pay)

- How can I use the new subscription behavior without upgrading my API version?Assuming that updating your API version is not an option, you should use the payment_behavior=allow_incomplete flag. Since payments can be initiated during subscription updates as well as subscription creation, you should pass this flag to all subscription and subscription_item creation or update calls. Below is a list of endpoints this flag applies to.Create CustomerUpdate CustomerCreate SubscriptionUpdate SubscriptionUpdate Subscription ItemFor creating and updating customers, the payment_behavior flag is only supported when subscribing a customer using an the API request. Creating and updating subscriptions using the Customer object is no longer documented, but the APIs are still supported for legacy reasons.

How can I use the new subscription behavior without upgrading my API version?

Assuming that updating your API version is not an option, you should use the payment_behavior=allow_incomplete flag. Since payments can be initiated during subscription updates as well as subscription creation, you should pass this flag to all subscription and subscription_item creation or update calls. Below is a list of endpoints this flag applies to.

[payment_behavior=allow_incomplete](/api/subscriptions/create#create_subscription-payment_behavior)

- Create Customer

[Create Customer](/api/customers/create)

- Update Customer

[Update Customer](/api/customers/update)

- Create Subscription

[Create Subscription](/api/subscriptions/create)

- Update Subscription

[Update Subscription](/api/subscriptions/update)

- Update Subscription Item

[Update Subscription Item](/api/subscription_items)

For creating and updating customers, the payment_behavior flag is only supported when subscribing a customer using an the API request. Creating and updating subscriptions using the Customer object is no longer documented, but the APIs are still supported for legacy reasons.

- How often will SCA be required and when will I be able to rely on exemptions?For subscriptions, Stripe is working to optimize the exemptions claimed on your behalf. SCA will systematically be applied to the first charge in a subscription where both the merchant and the customer are located in the EEA. Subsequent charges could be subject to exemptions. For one-off invoices and charges, Stripe will apply for exemptions on your behalf when possible.There are a couple of known caveats to SCA exemptions:Certain card issuing banks don’t support some or all exemption categories, though they may in the future.The card issuing bank has an unconditional right to challenge a legitimate exemption request. It is expected this will happen when they assess a transaction as high risk.When considering how to update your integration, plan for SCA every time.

How often will SCA be required and when will I be able to rely on exemptions?

For subscriptions, Stripe is working to optimize the exemptions claimed on your behalf. SCA will systematically be applied to the first charge in a subscription where both the merchant and the customer are located in the EEA. Subsequent charges could be subject to exemptions. For one-off invoices and charges, Stripe will apply for exemptions on your behalf when possible.

There are a couple of known caveats to SCA exemptions:

[SCA exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication)

- Certain card issuing banks don’t support some or all exemption categories, though they may in the future.

- The card issuing bank has an unconditional right to challenge a legitimate exemption request. It is expected this will happen when they assess a transaction as high risk.

When considering how to update your integration, plan for SCA every time.

- What is off-session and why is it important?A payment is off-session if it occurs without the direct involvement of the customer, using previously-collected payment information. Explicitly tagging transactions as off-session allows Stripe to claim exemptions on your behalf. For example, the merchant-initiated transaction (MIT) exemption only applies to off-session payments. Claiming this exemption decreases the chance that SCA is required, which reduces the friction on the customer.

What is off-session and why is it important?

A payment is off-session if it occurs without the direct involvement of the customer, using previously-collected payment information. Explicitly tagging transactions as off-session allows Stripe to claim exemptions on your behalf. For example, the merchant-initiated transaction (MIT) exemption only applies to off-session payments. Claiming this exemption decreases the chance that SCA is required, which reduces the friction on the customer.

[merchant-initiated transaction](https://stripe.com/guides/strong-customer-authentication#merchant-initiated-transactions-including-variable-subscriptions)

- When does Stripe automatically infer on-session and off-session on your behalf?Payments initiated through subscription creation are assumed to be on-session.Payments initiated by Stripe’s automated systems, like a payment for a recurring subscription, are considered off-session.Payments made using the Pay Invoice endpoint need to be explicitly tagged as on or off-session using the off_session attribute. If no value is set, Stripe defaults to true.

When does Stripe automatically infer on-session and off-session on your behalf?

- Payments initiated through subscription creation are assumed to be on-session.

- Payments initiated by Stripe’s automated systems, like a payment for a recurring subscription, are considered off-session.

- Payments made using the Pay Invoice endpoint need to be explicitly tagged as on or off-session using the off_session attribute. If no value is set, Stripe defaults to true.

[Pay Invoice](/api/invoices/pay)

[off_session](/api/invoices/pay#pay_invoice-off_session)

## SCA Migration Guide changelog

Below is a list of major revisions to this guide.

2019-07-15

- Add content explaining SetupIntents and when to use them

- Explain when Stripe automatically determines whether a payment is on or off-session

- Explain when and how to set off_session on the Pay Invoice endpoint

[Pay Invoice](/api/invoices/pay)

- Add link to new card for testing SCA

- Renamed the enable_incomplete_payments flag to payment_behaviorpayment_behavior can be set to either allow_incomplete or error_if_incomplete

[payment_behavior](/api/subscriptions/create#create_subscription-payment_behavior)

- payment_behavior can be set to either allow_incomplete or error_if_incomplete

2019-04-15

- Publish initial content
