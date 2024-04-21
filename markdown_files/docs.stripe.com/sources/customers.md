htmlSources and customers | Stripe Documentation[Skip to content](#main-content)Sources and customers[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsources%2Fcustomers)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsources%2Fcustomers)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)[Older APIs](/docs/payments/older-apis)[Sources](/docs/sources)# Sources and customersDeprecated

Learn how to attach and manage sources with Customer objects.CautionAs of September 2019, a regulation called Strong Customer Authentication (SCA) requires businesses in Europe to request additional authentication for online payments. Businesses based in the European Economic Area (EEA) with customers in the EEA should follow the accept a payment guide to use the Payment Intents API to meet these rules.

WarningWe deprecated the Sources API and plan to remove support for local payment methods. If you currently handle any local payment methods using the Sources API, you must migrate them to the Payment Methods API. We’ll send email communication with more information about this end of support.

While we don’t plan to remove support for card payments, we recommend replacing any use of the Sources API with the PaymentMethods API, which provides access to our latest features and payment method types.

A Source object can be either single-use or reusable, as indicated by its usage parameter. While sources can be charged directly, reusable sources should always be attached to a Customer object for later reuse. Attaching reusable sources to Customer objects allows you to present your customers with a list of reusable payment methods that they have previously used with your app or website.

## Reusable sources

Certain payment methods (for example, SEPA Direct Debit) support reusable sources, so that you can create additional payments without your customer’s needing to complete the payment process again. A source that you can reuse has its usage parameter set to reusable.

You must attach a reusable source to a Customer object before making a charge request. If you charge a reusable source without first attaching it, the source is consumed (its status changes from chargeable to consumed). Consumed sources cannot be used for further payments.

### Attaching a source to a new Customer object

You can create a Customer object and attach a source in one API call. This is useful if this is the first time you’re seeing this customer.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  --data-urlencode email="paying.user@example.com" \
  -d source=src_18eYalAHEMiOZZp1l9ZTjSU0`The source becomes the Customer object’s default source, since this is the customer’s first and only payment method. The default source is automatically selected if you make a charge request using the customer parameter without specifying a source.

### Attaching a Source to an existing Customer object

When you update a Customer object that has a default source, this automatically detaches the existing source, and adds the provided source as the new default. To add a source without replacing the existing default, use the attach method, as shown below.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers/cus_AFGbOSiITuJVDs/sources \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "source"="src_18eYalAHEMiOZZp1l9ZTjSU0"`Here, because a default source might already exist for the Customer object, the newly attached source does not become the default source. However, you can change the default source by updating the Customer object and specifying the source as a value for default_source.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers/cus_AFGbOSiITuJVDs \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d default_source=src_18eYalAHEMiOZZp1l9ZTjSU0`### Charging an attached source

You must specify both the Customer object and the source when making a charge request.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d amount="1099" \
  -d currency="eur" \
  -d customer=cus_AFGbOSiITuJVDs \
  -d source=src_18eYalAHEMiOZZp1l9ZTjSU0`If you attempt to charge a Customer object without specifying a source, Stripe uses the customer’s default source.

### Detaching a source

If you need to remove a source from a particular Customer object, you can detach the source. Doing so changes the source’s status to consumed, so it cannot be used once detached.

## Single-use sources

Single-use sources must be created each time a customer makes a payment, and cannot be reused. For that reason, we do not recommend that you permanently attach them to customers.

If you want to associate a payment with a particular Customer object, you can include a customer parameter when making a charge request with a source, even if the source is not attached.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d amount="1099" \
  -d currency="eur" \
  -d customer=cus_AFGbOSiITuJVDs \
  -d source=src_18eYalAHEMiOZZp1l9ZTjSU0`The resulting Charge object references both the Customer and Source objects, even if they are not directly related to one another.

## See also

- [Supported payment methods on Sources](/sources)
- [Best practices for using Sources](/sources/best-practices)
- [Cloning saved payment methods](/connect/cloning-customers-across-accounts)
- [Sources API reference](/api#sources)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Reusable sources](#reusable-sources)[Single-use sources](#single-use-sources)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`