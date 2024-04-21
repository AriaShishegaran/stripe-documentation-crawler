# Sources and customersDeprecated

As of September 2019, a regulation called Strong Customer Authentication (SCA) requires businesses in Europe to request additional authentication for online payments. Businesses based in the European Economic Area (EEA) with customers in the EEA should follow the accept a payment guide to use the Payment Intents API to meet these rules.

[Strong Customer Authentication](/strong-customer-authentication)

[European Economic Area](https://en.wikipedia.org/wiki/European_Economic_Area)

[accept a payment](/payments/accept-a-payment)

We deprecated the Sources API and plan to remove support for local payment methods. If you currently handle any local payment methods using the Sources API, you must migrate them to the Payment Methods API. We’ll send email communication with more information about this end of support.

[migrate them to the Payment Methods API](/payments/payment-methods/transitioning)

While we don’t plan to remove support for card payments, we recommend replacing any use of the Sources API with the PaymentMethods API, which provides access to our latest features and payment method types.

[PaymentMethods API](/api/payment_methods)

A Source object can be either single-use or reusable, as indicated by its usage parameter. While sources can be charged directly, reusable sources should always be attached to a Customer object for later reuse. Attaching reusable sources to Customer objects allows you to present your customers with a list of reusable payment methods that they have previously used with your app or website.

[Source](/api#sources)

[single-use or reusable](/sources#single-use-or-reusable)

[Customer](/api#customers)

## Reusable sources

Certain payment methods (for example, SEPA Direct Debit) support reusable sources, so that you can create additional payments without your customer’s needing to complete the payment process again. A source that you can reuse has its usage parameter set to reusable.

[SEPA Direct Debit](/sources/sepa-debit)

You must attach a reusable source to a Customer object before making a charge request. If you charge a reusable source without first attaching it, the source is consumed (its status changes from chargeable to consumed). Consumed sources cannot be used for further payments.

[attach](/api#attach_source)

You can create a Customer object and attach a source in one API call. This is useful if this is the first time you’re seeing this customer.

The source becomes the Customer object’s default source, since this is the customer’s first and only payment method. The default source is automatically selected if you make a charge request using the customer parameter without specifying a source.

[default source](/api#customer_object-default_source)

When you update a Customer object that has a default source, this automatically detaches the existing source, and adds the provided source as the new default. To add a source without replacing the existing default, use the attach method, as shown below.

[update](/api#update_customer)

[attach](/api#attach_source)

Here, because a default source might already exist for the Customer object, the newly attached source does not become the default source. However, you can change the default source by updating the Customer object and specifying the source as a value for default_source.

You must specify both the Customer object and the source when making a charge request.

If you attempt to charge a Customer object without specifying a source, Stripe uses the customer’s default source.

If you need to remove a source from a particular Customer object, you can detach the source. Doing so changes the source’s status to consumed, so it cannot be used once detached.

[detach the source](/api#detach_source)

## Single-use sources

Single-use sources must be created each time a customer makes a payment, and cannot be reused. For that reason, we do not recommend that you permanently attach them to customers.

If you want to associate a payment with a particular Customer object, you can include a customer parameter when making a charge request with a source, even if the source is not attached.

The resulting Charge object references both the Customer and Source objects, even if they are not directly related to one another.

## See also

- Supported payment methods on Sources

[Supported payment methods on Sources](/sources)

- Best practices for using Sources

[Best practices for using Sources](/sources/best-practices)

- Cloning saved payment methods

[Cloning saved payment methods](/connect/cloning-customers-across-accounts)

- Sources API reference

[Sources API reference](/api#sources)
