htmlTrack a payment link | Stripe Documentation[Skip to content](#main-content)Track a payment link[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayment-links%2Furl-parameters)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayment-links%2Furl-parameters)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)
[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Payment Links](/docs/payment-links)# Track a payment link

Use URL parameters and UTM codes to track a payment link.Modify your payment link with URL parameters and Urchin Tracking Module (UTM) codes to get insight into customer behaviors and your marketing strategy’s effectiveness. These tools help identify the source of your traffic and the marketing campaigns leading to the most conversions.

## Track campaigns with UTM codes

Use UTM codes to track how customers find your site when they pay using your payment link. You can add the following UTM codes as parameters in the query string of your URL: utm_source, utm_content, utm_medium, utm_term, and utm_campaign.

ParameterDescription`utm_source`Identifies where the traffic originated (for example, a website name, social media, or a search engine).`utm_content`Identifies what content your customer chooses. Use this parameter to distinguish between links that point to the same payment page.`utm_medium`Identifies the marketing medium that accesses your payment link (for example, email, cost per click (cpc), or other methods).`utm_term`Identifies specific search terms and keywords in your paid search ads.`utm_campaign`Identifies your marketing campaigns using the payment link URL.To add UTM codes, specify redirect as your confirmation behavior. When customers complete a payment, your redirect URL contains the UTM code parameters specified in your payment link URL. Here’s what a payment link looks like with an appended UTM codes: https://buy.stripe.com/test_eVa5nPg1j1wmfXq5kr?utm_medium=earned_email&utm_source=marketo&utm_campaign=campaign_a

CautionConstruct UTM codes using alphanumeric characters, dashes, or underscores, ensuring they don’t exceed a 150-character limit. Invalid values are discreetly discarded, guaranteeing your payment links performance remains unaffected.

## Simplify reconciliation with a URL parameter

You can simplify reconciliation with the client_reference_id URL parameter. Use URL parameters in the query string of your payment link URL. To configure URL parameters directly in the Dashboard Payment Links page:

1. Click the payment link you want to modify.
2. Click the down arrow of theCopybutton and selectURL parameters.
3. In the dialog, use the drop-down menu to selectClient reference ID.
4. Enter a value that meets the requirements described in the following table to append the reference to your URL.
5. Copy the amended URL for use in your integration.

ParameterDescriptionSyntax`client_reference_id`Use`client_reference_id`to attach a unique string of your choice to the Checkout Session. This can be a customer ID or a cart ID (or similar), and you can use it to reconcile the Session with your internal systems. If you add this parameter to your payment link, it’s sent in the[checkout.session.completed](/api/events/types#event_types-checkout.session.completed)[webhook](/webhooks)after payment completion.`client_reference_id`can be composed of alphanumeric characters, dashes, or underscores, and be any value up to 200 characters. Invalid values are silently dropped, but your payment page continues to work as expected.Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Track campaigns with UTM codes](#track-campaigns-with-utm-codes)[Simplify reconciliation with a URL parameter](#streamline-reconciliation-with-a-url-parameter)Products Used[Payments](/payments)[Payment Links](/payments/payment-links)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`