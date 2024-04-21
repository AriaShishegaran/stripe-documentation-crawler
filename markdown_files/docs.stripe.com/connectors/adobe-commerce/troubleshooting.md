htmlTroubleshooting for Adobe Commerce | Stripe Documentation[Skip to content](#main-content)Troubleshooting[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fadobe-commerce%2Ftroubleshooting)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fadobe-commerce%2Ftroubleshooting)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Adobe Commerce](/docs/connectors/adobe-commerce)# Troubleshooting for Adobe Commerce

Learn how to troubleshoot the Stripe Connector for Adobe Commerce.### Switching to developer mode

Enable the developer mode to make it easier to find errors.

## Installation issues

The most common issue during the installation process is getting the following error when using Composer:

`Composer package not found: Could not find a matching version of package stripe/stripe-payments`If you encounter this problem, follow these steps:

1. Order the module from the[Adobe Marketplace](https://marketplace.magento.com/stripe-stripe-payments.html).
2. Delete the file under`~/.composer/auth.json`in case you entered the wrong Adobe Commerce API keys.
3. Run the Composer command again. You may have to enter a username and password. Make sure that you enter the Adobe Commerce API keys of the account that you used to place the order. You can[get your authentication keys](https://devdocs.magento.com/guides/v2.4/install-gde/prereq/connect-auth.html)from Adobe Commerce.

## Upgrades and caching issues

If you upgrade the module but for some reason don’t see the new changes, you can manually clear the Adobe Commerce cache by deleting a set of directories. The official Adobe Commerce documentation describes which directories to delete for Adobe Commerce 2.3 and Adobe Commerce 2.4.

After you delete these directories, run the following commands:

Command Line`php bin/magento setup:upgrade
php bin/magento cache:flush`If you’re running in production mode, you have to compile and deploy your static assets:

Command Line`php bin/magento setup:di:compile
php bin/magento setup:static-content:deploy`If you’re running Varnish, you must also restart Varnish after deleting the var/cache/* files. Some browsers also cache Adobe Commerce requests; if you still have caching issues, try a different browser.

## No payment method appear at checkout

The payment method may not show at checkout for a few possible reasons:

- You’re missing the Stripe PHP library or you’re using an old version. You can install this dependency by following step 3 of the[installation instructions](/connectors/adobe-commerce/install)
- You have another Stripe module installed that’s using an older version of the Stripe PHP library. Disable or uninstall any other active Stripe module.
- You didn’t[configure the Stripe API keys](/connectors/adobe-commerce/configuration#general-settings)properly.
- You limited the availability of the payment method to specific countries or currencies.

## The Apple Pay or Google Pay button doesn’t appear

If you configured the Payment Request button and it still doesn’t appear, try the following:

- Make sure that you enabled Apple Pay and Google Pay in your[payment methods settings](https://dashboard.stripe.com/settings/payment_methods).
- For Apple Pay, use Safari on an iPhone running iOS 10 and above.
- For Google Pay, use Chrome Desktop or Chrome Mobile with a logged in Google account.
- Make sure that you have at least one card in your Wallet.– In iOS, you can add a card by going toSettings>Wallet>Apple Pay.– In Chrome, you can add a card by going toSettings>Autofill>Payment methods>Add new credit card.
- Confirm that your[iOS device supports Apple Pay](https://stripe.com/apple-pay).
- Confirm that your[Android device supports Google Pay](/stripe-js/elements/payment-request-button).
- If your website domain starts with`www`, make sure the domain is`www.example.com`and not`example.com`.
- You must serve your website over HTTPS using a valid[TLS](/security/guide#tls)1.2 certificate—check this from your browser or from[SSL Labs](https://www.ssllabs.com/ssltest/).
- Make sure that your HTTPS page doesn’t load any images, CSS, or JavaScript insecurely. You can check this by clicking the padlock on your browser URL bar.
- Make sure that you enabled theWalletbutton in the module’s configuration section.
- Make sure that you configured a default fallback country (Stores>Configuration>General>Country Options>Default Country).
- Make sure that you’re not using an older Stripe API key. Apple Pay requires a modern API key, which starts with`pk_live_`or`pk_test_`. You can roll your publishable key in the[Developers section](https://dashboard.stripe.com/test/apikeys)of the Dashboard.
- If you’re using a OneStepCheckout module, you may additionally need to configure the OSC module to refresh the payment form when guest customers submit their billing address. In most cases, this isn’t necessary.

If Apple Pay appears at checkout, but it doesn’t appear on the product pages, it may be because of additional reasons:

- You disabled guest checkouts from the Adobe Commerce admin.
- Your website is serving your product pages without a valid TLS 1.2 certificate.
- You overwrote theAdd to Cartbutton template in your theme. Try adding some text to`app/code/StripeIntegration/Payments/view/frontend/templates/express/product_button.phtml`. If your product pages remain unchanged, customize your theme and integrate the two templates together.
- JavaScript errors occur when Stripe.js is initializing. Check your browser console for any JavaScript errors related to Stripe.js.

## Order stuck in pending status

When creating an order, the initial status is Pending, which indicates that the authorization of the payment by the customer’s bank is still pending. For all redirect-based payment methods, when an authorization occurs, Stripe notifies your website using webhooks. If your orders don’t change from Pending to Processing, this might indicate that webhooks are missing or incorrect.

Go to your webhooks settings to check if a webhook endpoint with your store URL exists. If not, you can try to manually create it by running the following command from your Magento root directory:

Command Line`bin/magento stripe:webhooks:configure`If the webhook endpoint already exists, check the Error Rate to identify the failing webhooks. You can click on the webhook endpoint to see the error messages. To get assistance on webhook issues that aren’t due to incorrect server configuration, contact us at magento@stripe.com while sharing the details about the errors you encounter.

After fixing the webhook issue, you need to resend the charge.succeeded events that weren’t delivered correctly to your website. The module provides three commands to resend a single event, a range of events, or events within a date range:

`bin/magento stripe:webhooks:process-event [-f|--force] <event_id>
bin/magento stripe:webhooks:process-events-range <from_event_id> <to_event_id>
bin/magento stripe:webhooks:process-events-date-range <from_date> [<to_date>]`NoteYou can set a full date and time (2021-12-21 11:22:33+0200) or use any English textual datetime description (last Monday). This function uses your Magento default timezone unless specified otherwise.

See strtotime for all the supported date formats.

You can get a list of all failed charge.succeeded events in the Developers section of your Stripe Dashboard and decide which ones to resend using one of the commands above.

## Error logging and server-side errors (HTTP 500)

Adobe Commerce logs any errors and exceptions it encounters during application runtime in the var/log directory. You can find these errors in the following two files:

`var/log/system.log
var/log/exception.log`If you have SSH access, you can filter the error messages with the following command:

Command Line`grep -i Stripe var/log/system.log`You can display errors live in the console as they occur (or when you refresh a given page). To monitor errors, run the following command to watch the error log:

Command Line`tail -f var/log/*`If you don’t have shell access, you can download this file and search for Stripe errors with a text editor.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Installation issues](#installation-issues)[Upgrades and caching issues](#upgrades-and-caching-issues)[No payment method appear at checkout](#no-payment-method-appear-at-checkout)[The Apple Pay or Google Pay button doesn’t appear](#wallet-button)[Order stuck in pending status](#order-stuck-in-pending-status)[Error logging and server-side errors (HTTP 500)](#error-logging)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`