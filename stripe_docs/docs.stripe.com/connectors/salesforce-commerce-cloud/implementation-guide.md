# Stripe Connector for Salesforce B2C Commerce implementation guide

## Set up Business Manager

The Stripe Connector for Salesforce B2C Commerce (LINK Cartridge) requires several cartridges for full functionality. Additionally, controller and SFRA support is broken out into two separate cartridges, thereby facilitating the installation and use of one or the other models.

Import all three cartridges into UX studio and associate them with a Server Connection.

- Navigate to Administration > Sites > Manage Sites.

- Click the site name for the storefront site you want to add Stripe functionality to.

- Select the Settings tab.

- For Storefront Reference Architecture (SFRA), add app_stripe_sfra:int_stripe_sfra:int_stripe_core to the cartridge path.

Repeat these steps for each storefront site where you want to implement Stripe.

- Navigate to Administration > Sites > Manage Sites.

- Click the Business Manager Site and then the Manage the Business Manager site link.

- Add int_stripe_core to the cartridge path.

- Navigate to the metadata folder of the project and open the stripe_site_template folder.

- Open the sites folder and edit the siteIDHere folder to the site ID of the site you want.

- Add a folder for each site you want Stripe on.

- Navigate to Administration > Site Development > Site Import & Export.

- Compress the stripe_site_template folder into a zip file and import it.

If necessary, update the path to your base SFRA installation in package.json from the same root folder.

Normally, there’s a top-level project folder in which the repositories of the SFRA base cartridge and all required plugins, libraries, and any other LINK cartridges are cloned. If you cloned the Stripe cartridge into that folder as well, you don’t need to update the paths.base property. If you haven’t cloned the cartridge into that folder, update the paths.base property in package.json with the relative path to the local directory containing the Storefront Reference Architecture repository. The following is the default paths.base value:

After you’re certain package.json has the correct path to SFRA cartridges, run the npm run compile:scss command from the root folder of the Stripe repository.

There are two payment processors used in the Stripe cartridge. STRIPE_CREDIT handles credit card payments while STRIPE_APM handles local payment methods such as bank transfers and giropay.

- Navigate to Merchant Tools > Ordering > Payment Processors and click New.

- In the new window, set the ID to STRIPE_CREDIT and click Apply.

- Navigate to Merchant Tools > Ordering > Payment Processors and click New.

- In the new window, set the ID attribute to value STRIPE_APM and click Apply.

Navigate to Merchant Tools > Ordering > Payment Methods, click the CREDIT_CARD payment method, and select the STRIPE_CREDIT payment processor in the dropdown under the CREDIT_CARD details section.

For dynamic payment methods or the Payment Request Button, enable STRIPE_APM_METHODS to include payment methods supported by Stripe. See the payment methods guide for more details.

[payment methods guide](https://stripe.com/payments/payment-methods-guide)

To utilize the Stripe Payment Request Button, enable the STRIPE_PAYMENT_REQUEST_BTN payment method. Refer to payment request button for more details.

[payment request button](/stripe-js/elements/payment-request-button)

## Install the Stripe Salesforce Commerce app

Use Stripe Apps to bolster security and simplify the use of distinct restricted keys for each integration with your Stripe account. The process of installing the Stripe App and acquiring the newly generated secret and publishable keys is essential for your integration with the Salesforce Commerce connector. This approach eliminates the need to manually create your own restricted key or use a secret key. To integrate the Salesforce Commerce app and reinforce your account’s security infrastructure:

[keys](/keys)

- Navigate to the Stripe App Marketplace, then click Install the Salesforce Commerce app.

[Stripe App Marketplace](https://marketplace.stripe.com/)

[Install the Salesforce Commerce app](https://marketplace.stripe.com/apps/install/link/com.stripe.SalesforceCommerce)

- Select the Stripe account where you want to install the app.

- Review and approve the app permissions, install the app in test mode or live mode, then click Install.

- After you install the app, store the keys in a safe place where you won’t lose them. To help yourself remember where you stored it, you can leave a note on the key in the Dashboard.

[leave a note on the key in the Dashboard](/keys#reveal-an-api-secret-key-live-mode)

- Use the newly generated publishable key and secret key to finish the Connector configuration.

- To manage the app or generate new security keys after installation, navigate to the application settings page in test mode or live mode.

[test mode](https://dashboard.stripe.com/test/settings/apps/com.stripe.SalesforceCommerce)

[live mode](https://dashboard.stripe.com/settings/apps/com.stripe.SalesforceCommerce)

## Configuration

Update Merchant Tools > Site Preferences > Custom Site Preferences > Stripe Configurations with site-specific values.

- Populate Stripe secret API key with the values from the Stripe Salesforce Commerce app.

Populate Stripe secret API key with the values from the Stripe Salesforce Commerce app.

- Populate publishable API key with the values from the Stripe Salesforce Commerce app.

Populate publishable API key with the values from the Stripe Salesforce Commerce app.

- Is this SFRA installation: Set to yes if the current site is using SFRA.

Is this SFRA installation: Set to yes if the current site is using SFRA.

- Capture Funds on Stripe Charge: The default value is true (Yes). Set to false (No) to authorize Stripe charges instead.

Capture Funds on Stripe Charge: The default value is true (Yes). Set to false (No) to authorize Stripe charges instead.

- Stripe card element CSS style: Set the CSS styling that the card element button inherits to fit within the overall storefront styles (for example, {"base": {"fontFamily": "Arial, sans-serif","fontSize": "14px","color": "#C1C7CD"},"invalid": {"color": "red" } }).

Stripe card element CSS style: Set the CSS styling that the card element button inherits to fit within the overall storefront styles (for example, {"base": {"fontFamily": "Arial, sans-serif","fontSize": "14px","color": "#C1C7CD"},"invalid": {"color": "red" } }).

- Stripe API URL: https://js.stripe.com/v3/

Stripe API URL: https://js.stripe.com/v3/

- Stripe Payment Request Button Style: For the payment request button, select the limited CSS styling for the button. Refer to styling the element for more details.

Stripe Payment Request Button Style: For the payment request button, select the limited CSS styling for the button. Refer to styling the element for more details.

[styling the element](/stripe-js/elements/payment-request-button#html-js-styling-the-element)

- Apple Pay Verification String: Enter the Apple verification string provided from the Stripe Dashboard. This is a one-time enablement. The Stripe console proxies the Apple Pay for a web verification string upon setup. Configure this in the sandbox if using the Payment Request Button as a form of payment on the storefront.

Apple Pay Verification String: Enter the Apple verification string provided from the Stripe Dashboard. This is a one-time enablement. The Stripe console proxies the Apple Pay for a web verification string upon setup. Configure this in the sandbox if using the Payment Request Button as a form of payment on the storefront.

- Country Code (Stripe Payment Request Button): This is the default country code (for example, US) for the Payment Request Button. You might need to customize on a multi-country single site in order to dynamically pass the country code rather than the site preference. Refer to creating a payment request instance for more details.

Country Code (Stripe Payment Request Button): This is the default country code (for example, US) for the Payment Request Button. You might need to customize on a multi-country single site in order to dynamically pass the country code rather than the site preference. Refer to creating a payment request instance for more details.

[creating a payment request instance](/stripe-js/elements/payment-request-button)

- Stripe webhook signing secret: Enter the webhook signing secret provided by the Stripe Dashboard. Stripe signs webhook events and passes a validation to SFCC. SFCC validates the contents of the message using this secret.

Stripe webhook signing secret: Enter the webhook signing secret provided by the Stripe Dashboard. Stripe signs webhook events and passes a validation to SFCC. SFCC validates the contents of the message using this secret.

[webhook](/webhooks)

- Stripe Allowed Webhook Statuses: Configure the allowed statuses for webhooks to respond to.

Stripe Allowed Webhook Statuses: Configure the allowed statuses for webhooks to respond to.

[allowed statuses](#stripe-dashboard-set-up)

- Allowed apm methods:Enumeration of allowed payment methods from the Stripe API: { "default": [ "p24", "eps", "sepa_debit", "ideal", "sofort", "bitcoin", "alipay", "bancontact", "giropay" ], "en_UK": [ "p24", "eps" ], "de_AT": [ "sofort", "ideal" ] }. Update this field per site locale to indicate which alternate payment methods are enabled for each locale. Refer to sources for more details.

Allowed apm methods:

- Enumeration of allowed payment methods from the Stripe API: { "default": [ "p24", "eps", "sepa_debit", "ideal", "sofort", "bitcoin", "alipay", "bancontact", "giropay" ], "en_UK": [ "p24", "eps" ], "de_AT": [ "sofort", "ideal" ] }. Update this field per site locale to indicate which alternate payment methods are enabled for each locale. Refer to sources for more details.

[sources](/sources)

- Stripe Enabled: Enables or disables the cartridge.

Stripe Enabled: Enables or disables the cartridge.

## Set up webhook endpoint and Apple Pay domain

Set up a new endpoint in the Stripe Dashboard with the Stripe-WebHook controller URL and subscribe to these events:

[Stripe Dashboard](https://dashboard.stripe.com/test/webhooks)

- review.opened

- review.closed

- charge.succeeded

- source.canceled

- source.failed

- source.chargeable

- payment_intent.succeeded

- payment_intent.payment_failed

Copy the signing secret to the Stripe Webhook Signing Secret preference. Make sure that this value is set to your Stripe account’s country code.

For Apple Pay:

- Update RedirectURL.js:

- Set up an alias to one of the sites on the sandbox temporarily so that the domain can be verified in the Stripe Dashboard. The alias needs to be something like this:

The locale value needs to be a locale that isn’t disabled.

- On the Payment method domains page, click Add a new domain.

[Payment method domains page](https://dashboard.stripe.com/settings/payment_method_domains)

- Enter your domain name.

- Click Save and continue.

- Download the domain association file.

[domain association file](https://stripe.com/files/apple-pay/apple-developer-merchantid-domain-association)

- Host the file at /.well-known/apple-developer-merchantid-domain-association. For example, if you register https://example.com, make that file available at https://example.com/.well-known/apple-developer-merchantid-domain-association.

- Click Verify.

## Update storefront code

The base LINK cartridge code contains support for all credit cards supported by Stripe. The list of allowed cards on the storefront is still limited by the Credit/Debit Cards list in Business Manager (Merchant Tools > Ordering > Payment Methods > Credit/Debit Cards).

Make the following updates to the Storefront Code. Examples provided are based on SFRA version 4.4. The following sections detail the customizations made to SFRA code.

There are many controller endpoints that are appends instead of replaces. Those aren’t covered as they should work without doing anything.

Controller updates are only required for replaced endpoints, as you might have already replaced that endpoint in your integration. Use the changes made to the base cartridge and add them to your already replaced controller. If you haven’t extended/replaced these endpoints, you don’t need to do anything.

Path: app_stripe_sfra/cartridge/controllers/CheckoutServices.js

Remove the payment instrument validation in the SubmitPayment endpoint:

Update the order creation code:

Update the order placement code:

Path: app_stripe_sfra/cartridge/controllers/PaymentInstruments.js

Replace the DeletePayment endpoint with the following code:

Path: app_stripe_sfra/cartridge/controllers/RedirectURL.js

Add the following code to the Start function:

## External interfaces

Stripe functionality relies heavily on external calls to Stripe services. All external interfaces use the service framework to communicate with the Stripe API.

Stripe accounts are free to create and use. Most communications with Stripe services are logged and accessible in the Stripe Dashboard. We encourage you to use the Stripe Dashboard to monitor and test your integration. You can find the main configuration for integration of the Stripe services under Administration > Operations > Services with a different service for each external call:

[Stripe Dashboard](https://dashboard.stripe.com/)

- stripe.http.addCard

- stripe.http.authorizePayment

- stripe.http.createCharge

- stripe.http.createCustomer

- stripe.http.deleteCard

- stripe.http.fetchCustomerCards

- stripe.http.fetchCustomerSources

- stripe.http.refundCharge

- stripe.http.retrieveCustomer

- stripe.http.service

- stripe.http.updateCard

All of these services use the same profile and the same credentials. The only thing that may be different is whether or not the communication log is enabled and the log name prefix. Here is the configuration of some of the services:

## Stripe Payment Element

Stripe cartridge supports Stripe Payment Element as a payment method.

The Payment Element is an embedded UI component that lets you accept up to 25+ payment methods with a single integration.

To enable the Payment Element, navigate to Business Manager > Merchant Tools > Ordering > Payment Methods and enable the payment method with ID set to STRIPE_PAYMENT_ELEMENT. In storefront Checkout > Payment, there is a widget with all payment methods enabled in the Stripe Dashboard.

[Dashboard](https://dashboard.stripe.com/settings/payment_methods)

When you enable Payment Element in Business Manager, it can replace all other payment methods. You can disable all payment methods and use STRIPE_PAYMENT_ELEMENT instead.

To enable saving of payment methods for future use from Stripe Payment Element, navigate to Business Manager > Custom Preferences > Stripe Configs and set Stripe Payment Element: Enable Save Payment Method for Future Purchases to Yes.

To display a list of saved payment methods in checkout, navigate to Business Manager > Payments Methods and enable the CREDIT_CARD payment method. When it’s enabled with STRIPE_PAYMENT_ELEMENT, the credit card tab includes a list saved cards (if any).

## Stripe Radar insights display

Stripe LINK cartridge supports Radar insights view to showcase risk insights within the Orders section of Business Manager. Radar provides real-time fraud protection and requires no additional development time. Fraud professionals can add Radar for Fraud Teams to customize protection and get deeper insights.

[Radar](/radar)

[Radar for Fraud Teams](https://stripe.com/radar/fraud-teams)

To enable the insights display, navigate to Business Manager > Merchant Tools > Custom Preferences > Stripe Configs and set Risk Score Data to Yes.

## See also

- Operations and maintenance

[Operations and maintenance](/connectors/salesforce-commerce-cloud/operations-and-maintenance)

- User guide

[User guide](/connectors/salesforce-commerce-cloud/user-guide)

- Testing

[Testing](/connectors/salesforce-commerce-cloud/testing)
