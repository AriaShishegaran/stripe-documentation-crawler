htmlStripe Connector for Salesforce B2C Commerce implementation guide | Stripe Documentation[Skip to content](#main-content)Implementation Guide[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-commerce-cloud%2Fimplementation-guide)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fsalesforce-commerce-cloud%2Fimplementation-guide)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Salesforce](/docs/connectors/salesforce)[Salesforce B2C Commerce](/docs/connectors/salesforce-commerce-cloud)# Stripe Connector for Salesforce B2C Commerce implementation guide

## Set up Business Manager

The Stripe Connector for Salesforce B2C Commerce (LINK Cartridge) requires several cartridges for full functionality. Additionally, controller and SFRA support is broken out into two separate cartridges, thereby facilitating the installation and use of one or the other models.

Import all three cartridges into UX studio and associate them with a Server Connection.

### Site cartridge assignment

1. Navigate toAdministration > Sites > Manage Sites.
2. Click the site name for the storefront site you want to add Stripe functionality to.
3. Select theSettingstab.
4. For Storefront Reference Architecture (SFRA), add`app_stripe_sfra:int_stripe_sfra:int_stripe_core`to the cartridge path.

Repeat these steps for each storefront site where you want to implement Stripe.

### Business Manager cartridge assignment

1. Navigate toAdministration > Sites > Manage Sites.
2. Click theBusiness Manager Siteand then theManage the Business Manager sitelink.
3. Add`int_stripe_core`to the cartridge path.

### Metadata import

1. Navigate to the metadata folder of the project and open the`stripe_site_template`folder.
2. Open the`sites`folder and edit the`siteIDHere`folder to the site ID of the site you want.
3. Add a folder for each site you want Stripe on.
4. Navigate toAdministration > Site Development > Site Import & Export.
5. Compress the`stripe_site_template`folder into a zip file and import it.

### Build Stripe styling

If necessary, update the path to your base SFRA installation in package.json from the same root folder.

Normally, there’s a top-level project folder in which the repositories of the SFRA base cartridge and all required plugins, libraries, and any other LINK cartridges are cloned. If you cloned the Stripe cartridge into that folder as well, you don’t need to update the paths.base property. If you haven’t cloned the cartridge into that folder, update the paths.base property in package.json with the relative path to the local directory containing the Storefront Reference Architecture repository. The following is the default paths.base value:

`"paths": {
  "base": "../storefront-reference-architecture/cartridges/app_storefront_base/"
}`After you’re certain package.json has the correct path to SFRA cartridges, run the npm run compile:scss command from the root folder of the Stripe repository.

### Add new payment processors

There are two payment processors used in the Stripe cartridge. STRIPE_CREDIT handles credit card payments while STRIPE_APM handles local payment methods such as bank transfers and giropay.

Credit payment processor![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

1. Navigate toMerchant Tools > Ordering > Payment Processorsand clickNew.
2. In the new window, set the ID to`STRIPE_CREDIT`and clickApply.

APM payment processor![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

1. Navigate toMerchant Tools > Ordering > Payment Processorsand clickNew.
2. In the new window, set the ID attribute to value`STRIPE_APM`and clickApply.

### Update payment methods

Navigate to Merchant Tools > Ordering > Payment Methods, click the CREDIT_CARD payment method, and select the STRIPE_CREDIT payment processor in the dropdown under the CREDIT_CARD details section.

For dynamic payment methods or the Payment Request Button, enable STRIPE_APM_METHODS to include payment methods supported by Stripe. See the payment methods guide for more details.

To utilize the Stripe Payment Request Button, enable the STRIPE_PAYMENT_REQUEST_BTN payment method. Refer to payment request button for more details.

## Install the Stripe Salesforce Commerce app

Use Stripe Apps to bolster security and simplify the use of distinct restricted keys for each integration with your Stripe account. The process of installing the Stripe App and acquiring the newly generated secret and publishable keys is essential for your integration with the Salesforce Commerce connector. This approach eliminates the need to manually create your own restricted key or use a secret key. To integrate the Salesforce Commerce app and reinforce your account’s security infrastructure:

1. Navigate to the[Stripe App Marketplace](https://marketplace.stripe.com/), then click[Install the Salesforce Commerce app](https://marketplace.stripe.com/apps/install/link/com.stripe.SalesforceCommerce).
2. Select the Stripe account where you want to install the app.
3. Review and approve the app permissions, install the app in test mode or live mode, then clickInstall.
4. After you install the app, store the keys in a safe place where you won’t lose them. To help yourself remember where you stored it, you can[leave a note on the key in the Dashboard](/keys#reveal-an-api-secret-key-live-mode).
5. Use the newly generated publishable key and secret key to finish the Connector configuration.
6. To manage the app or generate new security keys after installation, navigate to the application settings page in[test mode](https://dashboard.stripe.com/test/settings/apps/com.stripe.SalesforceCommerce)or[live mode](https://dashboard.stripe.com/settings/apps/com.stripe.SalesforceCommerce).

## Configuration

Update Merchant Tools > Site Preferences > Custom Site Preferences > Stripe Configurations with site-specific values.

- Populate Stripe secret API key with the values from the Stripe Salesforce Commerce app.


- Populate publishable API key with the values from the Stripe Salesforce Commerce app.


- Is this SFRA installation: Set to yes if the current site is using SFRA.


- Capture Funds on Stripe Charge: The default value is true (Yes). Set to false (No) to authorize Stripe charges instead.


- Stripe card element CSS style: Set the CSS styling that the card element button inherits to fit within the overall storefront styles (for example, {"base": {"fontFamily": "Arial, sans-serif","fontSize": "14px","color": "#C1C7CD"},"invalid": {"color": "red" } }).


- Stripe API URL: https://js.stripe.com/v3/


- Stripe Payment Request Button Style: For the payment request button, select the limited CSS styling for the button. Refer to styling the element for more details.


- Apple Pay Verification String: Enter the Apple verification string provided from the Stripe Dashboard. This is a one-time enablement. The Stripe console proxies the Apple Pay for a web verification string upon setup. Configure this in the sandbox if using the Payment Request Button as a form of payment on the storefront.


- Country Code (Stripe Payment Request Button): This is the default country code (for example, US) for the Payment Request Button. You might need to customize on a multi-country single site in order to dynamically pass the country code rather than the site preference. Refer to creating a payment request instance for more details.


- Stripe webhook signing secret: Enter the webhook signing secret provided by the Stripe Dashboard. Stripe signs webhook events and passes a validation to SFCC. SFCC validates the contents of the message using this secret.


- Stripe Allowed Webhook Statuses: Configure the allowed statuses for webhooks to respond to.

![](https://b.stripecdn.com/docs-statics-srv/assets/configuration-webhook-statuses.01dca58aedb406537570122a457afa09.png)


- Allowed apm methods:

  - Enumeration of allowed payment methods from the Stripe API:`{ "default": [ "p24", "eps", "sepa_debit", "ideal", "sofort", "bitcoin", "alipay", "bancontact", "giropay" ], "en_UK": [ "p24", "eps" ], "de_AT": [ "sofort", "ideal" ] }`. Update this field per site locale to indicate which alternate payment methods are enabled for each locale. Refer to[sources](/sources)for more details.


- Stripe Enabled: Enables or disables the cartridge.



## Set up webhook endpoint and Apple Pay domain

Set up a new endpoint in the Stripe Dashboard with the Stripe-WebHook controller URL and subscribe to these events:

- `review.opened`
- `review.closed`
- `charge.succeeded`
- `source.canceled`
- `source.failed`
- `source.chargeable`
- `payment_intent.succeeded`
- `payment_intent.payment_failed`

Copy the signing secret to the Stripe Webhook Signing Secret preference. Make sure that this value is set to your Stripe account’s country code.

For Apple Pay:

1. Update`RedirectURL.js`:

RedirectURL.js`server.extend(page);

server.replace('Start', function (req, res, next) {
  const URLRedirectMgr = require('dw/web/URLRedirectMgr');

  // Intercept the incoming path request
  if (URLRedirectMgr.getRedirectOrigin() === '/.well-known/apple-developer-merchantid-domain-association') {
    res.render('stripe/util/apple');
    return next();
  }

  const redirect = URLRedirectMgr.redirect;
  const location = redirect ? redirect.location : null;
  const redirectStatus = redirect ? redirect.getStatus() : null;

  if (!location) {
    res.setStatusCode(404);
    res.render('error/notFound');
  } else {
    if (redirectStatus) {
      res.setRedirectStatus(redirectStatus);
    }
    res.redirect(location);
  }

  return next();
});`1. Set up an alias to one of the sites on the sandbox temporarily so that the domain can be verified in the Stripe Dashboard. The alias needs to be something like this:

`{
  "__version": "1",
    "settings": {
      "http-host": "your.sandbox.domain.demandware.net",
      "https-host": "your.sandbox.domain.demandware.net",
      "default": "true",
      "site-path": "/",
  },
  "your.sandbox.domain.demandware.net": [
    {
      "locale": "en_GB",
      "if-site-path": "/",
    }
  ]
}`The locale value needs to be a locale that isn’t disabled.

1. On the[Payment method domains page](https://dashboard.stripe.com/settings/payment_method_domains), clickAdd a new domain.
2. Enter your domain name.
3. ClickSave and continue.
4. Download the[domain association file](https://stripe.com/files/apple-pay/apple-developer-merchantid-domain-association).
5. Host the file at`/.well-known/apple-developer-merchantid-domain-association`. For example, if you register`https://example.com`, make that file available at`https://example.com/.well-known/apple-developer-merchantid-domain-association`.
6. ClickVerify.

## Update storefront code

The base LINK cartridge code contains support for all credit cards supported by Stripe. The list of allowed cards on the storefront is still limited by the Credit/Debit Cards list in Business Manager (Merchant Tools > Ordering > Payment Methods > Credit/Debit Cards).

Make the following updates to the Storefront Code. Examples provided are based on SFRA version 4.4. The following sections detail the customizations made to SFRA code.

There are many controller endpoints that are appends instead of replaces. Those aren’t covered as they should work without doing anything.

Controller updates are only required for replaced endpoints, as you might have already replaced that endpoint in your integration. Use the changes made to the base cartridge and add them to your already replaced controller. If you haven’t extended/replaced these endpoints, you don’t need to do anything.

### Controller: CheckoutServices.js

Path: app_stripe_sfra/cartridge/controllers/CheckoutServices.js

Remove the payment instrument validation in the SubmitPayment endpoint:

CheckoutServices.js`if (!paymentMethodID && currentBasket.totalGrossPrice.value > 0) {
  const noPaymentMethod = {};

  noPaymentMethod[billingData.paymentMethod.htmlName] = Resource.msg(
    'error.no.selected.payment.method',
    'payment',
    null
  );

  delete billingData.paymentInformation;
  res.json({
    form: billingForm,
    fieldErrors: [noPaymentMethod],
    serverErrors: [],
    error: true
  });
  return;
}

// Validate payment instrument
const creditCardPaymentMethod = PaymentMgr.getPaymentMethod(PaymentInstrument.METHOD_CREDIT_CARD);
const paymentCard = PaymentMgr.getPaymentCard(billingData.paymentInformation.cardType.value);

const applicablePaymentCards = creditCardPaymentMethod.getApplicablePaymentCards(
  req.currentCustomer.raw,
  req.geolocation.countryCode,
  null
);

if (!applicablePaymentCards.contains(paymentCard)) {
  // Invalid payment instrument
  const invalidPaymentMethod = Resource.msg('error.payment.not.valid', 'checkout', null);
  delete billingData.paymentInformation;
  res.json({
    form: billingForm,
    fieldErrors: [],
    serverErrors: [invalidPaymentMethod],
    error: true
  });
  return;
}`Update the order creation code:

CheckoutServices.js`// Re-calculate the payments
const calculatedPaymentTransactionTotal = COHelpers.calculatePaymentTransaction(currentBasket);
if (calculatedPaymentTransactionTotal.error) {
  res.json({
      error: true,
      errorMessage: Resource.msg('error.technical', 'checkout', null);
  });
  return next();
}
const stripeCheckoutHelper = require('int_stripe_core').getCheckoutHelper();
const order = stripeCheckoutHelper.createOrder(currentBasket);

if (!order) {
  res.json({
    error: true,
    errorMessage: Resource.msg('error.technical', 'checkout', null);
  });
  return next();
}`Update the order placement code:

CheckoutServices.js`var isAPMOrder = stripeCheckoutHelper.isAPMORder(order);

if (!isAPMOrder) {
  var stripePaymentInstrument = stripeCheckoutHelper.getStripePaymentInstrument(order);

  if (stripePaymentInstrument && order.custom.stripeIsPaymentIntentInReview) {
    res.json({
      error: false,
      orderID: order.orderNo,
      orderToken: order.orderToken,
      continueUrl: URLUtils.url('Order-Confirm').toString()
    });

    return next();
  }
  // Places the order
  var placeOrderResult = COHelpers.placeOrder(order, fraudDetectionStatus);

  if(placeOrderResult.error) {
    stripeCheckoutHelper.refundCharge(order);
    res.json({
      error: true,
      errorMessage: Resource.msg('error.technical', 'checkout', null)
    });
  const fraudDetectionStatus = hooksHelper(
    'app.fraud.detection',
    'fraudDetection',
    currentBasket,
    require('*/cartridge/scripts/hooks/fraudDetection').fraudDetection
  );

  if (fraudDetectionStatus.status === 'fail') {
    Transaction.wrap(function () {
      OrderMgr.failOrder(order);
    });

    // Fraud detection failed
    req.session.privacyCache.set('fraudDetectionStatus', true);

    res.json({
      error: true,
      cartError: true,
      redirectUrl: URLUtils.url('Error-ErrorCode', 'err', fraudDetectionStatus.errorCode).toString(),
      errorMessage: Resource.msg('error.technical', 'checkout', null);
    });
    return next();
  }
  COHelpers.sendConfirmationEmail(order, req.locale.id);

  // Reset usingMultiShip after successful Order placement
  req.session.privacyCache.set('usingMultiShip', false);

  res.json({
    error: false,
    orderID: order.orderNo,
    orderToken: order.orderToken,
    continueUrl: URLUtils.url('Order-Confirm').toString()
  });

  return next();
}`### Controller: PaymentInstruments.js

Path: app_stripe_sfra/cartridge/controllers/PaymentInstruments.js

Replace the DeletePayment endpoint with the following code:

PaymentInstruments.js`server.replace('DeletePayment', function(req, res, next) {
  var stripeHelper = require ('int_stripe_core').getStripeHelper();
  var wallet = stripeHelper.getStripeWallet(customer);
  var UUID = req.querystring.UUID;
  wallet.removePaymentInstrument({ custom: { stripeId: UUID }});

  res.json({  UUID: UUID });
  next();
});`### Controller: RedirectURL.js

Path: app_stripe_sfra/cartridge/controllers/RedirectURL.js

Add the following code to the Start function:

RedirectURL.js`server.replace('Start', function (req, res, next) {
  const URLRedirectMgr = require('dw/web/URLRedirectMgr');

  // Intercept the incoming path request
  if (URLRedirectMgr.getRedirectOrigin() === '/.well-known/apple-developer-merchantid-domain-association') {
    res.render('stripe/util/apple');
    return next();
  }

  const redirect = URLRedirectMgr.redirect;
  const location = redirect ? redirect.location : null;
  const redirectStatus = redirect ? redirect.getStatus() : null;

  if (!location) {
    res.setStatusCode(404);
    res.render('error/notFound');
  } else {
    if (redirectStatus) {
      res.setRedirectStatus(redirectStatus);
    }
    res.redirect(location);
  }

  return next();
});`## External interfaces

Stripe functionality relies heavily on external calls to Stripe services. All external interfaces use the service framework to communicate with the Stripe API.

Stripe accounts are free to create and use. Most communications with Stripe services are logged and accessible in the Stripe Dashboard. We encourage you to use the Stripe Dashboard to monitor and test your integration. You can find the main configuration for integration of the Stripe services under Administration > Operations > Services with a different service for each external call:

- `stripe.http.addCard`
- `stripe.http.authorizePayment`
- `stripe.http.createCharge`
- `stripe.http.createCustomer`
- `stripe.http.deleteCard`
- `stripe.http.fetchCustomerCards`
- `stripe.http.fetchCustomerSources`
- `stripe.http.refundCharge`
- `stripe.http.retrieveCustomer`
- `stripe.http.service`
- `stripe.http.updateCard`

All of these services use the same profile and the same credentials. The only thing that may be different is whether or not the communication log is enabled and the log name prefix. Here is the configuration of some of the services:

![](https://b.stripecdn.com/docs-statics-srv/assets/salesforce-addcard.af39346a7b5255e74be8acaa145593bc.png)

![](https://b.stripecdn.com/docs-statics-srv/assets/salesforce-authorize.f02620c9923d170c73748fa7499339ef.png)

![](https://b.stripecdn.com/docs-statics-srv/assets/salesforce-createcharge.3370eca839412304ffe706cecdcc942c.png)

## Stripe Payment Element

Stripe cartridge supports Stripe Payment Element as a payment method.

The Payment Element is an embedded UI component that lets you accept up to 25+ payment methods with a single integration.

![](https://b.stripecdn.com/docs-statics-srv/assets/payment-element.d9f32fe8ddd882f9cfe67f2b0d915b33.png)

To enable the Payment Element, navigate to Business Manager > Merchant Tools > Ordering > Payment Methods and enable the payment method with ID set to STRIPE_PAYMENT_ELEMENT. In storefront Checkout > Payment, there is a widget with all payment methods enabled in the Stripe Dashboard.

When you enable Payment Element in Business Manager, it can replace all other payment methods. You can disable all payment methods and use STRIPE_PAYMENT_ELEMENT instead.

To enable saving of payment methods for future use from Stripe Payment Element, navigate to Business Manager > Custom Preferences > Stripe Configs and set Stripe Payment Element: Enable Save Payment Method for Future Purchases to Yes.

To display a list of saved payment methods in checkout, navigate to Business Manager > Payments Methods and enable the CREDIT_CARD payment method. When it’s enabled with STRIPE_PAYMENT_ELEMENT, the credit card tab includes a list saved cards (if any).

## Stripe Radar insights display

Stripe LINK cartridge supports Radar insights view to showcase risk insights within the Orders section of Business Manager. Radar provides real-time fraud protection and requires no additional development time. Fraud professionals can add Radar for Fraud Teams to customize protection and get deeper insights.

![](https://b.stripecdn.com/docs-statics-srv/assets/radar-insights.be63001444ae6c6898ac8de4a13ae00e.png)

To enable the insights display, navigate to Business Manager > Merchant Tools > Custom Preferences > Stripe Configs and set Risk Score Data to Yes.

![](https://b.stripecdn.com/docs-statics-srv/assets/radar-configuration.54078bec7ed35de180bec62625dfde96.png)

## See also

- [Operations and maintenance](/connectors/salesforce-commerce-cloud/operations-and-maintenance)
- [User guide](/connectors/salesforce-commerce-cloud/user-guide)
- [Testing](/connectors/salesforce-commerce-cloud/testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Business Manager](#set-up-business-manager)[Install the Stripe Salesforce Commerce app](#install-the-stripe-salesforce-commerce-app)[Configuration](#configuration)[Set up webhook endpoint and Apple Pay domain](#stripe-dashboard-set-up)[Update storefront code](#update-storefront-code)[External interfaces](#external-interfaces)[Stripe Payment Element](#stripe-payment-element)[Stripe Radar insights display](#stripe-radar-insights-display)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`