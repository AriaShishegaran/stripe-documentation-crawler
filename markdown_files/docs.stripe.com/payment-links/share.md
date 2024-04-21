htmlShare a payment link | Stripe Documentation[Skip to content](#main-content)Share a payment link[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayment-links%2Fshare)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayment-links%2Fshare)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)
[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[Payment Links](/docs/payment-links)# Share a payment link

Share payment links across social media, emails, or your website.After you create a payment link, share it with your customers to accept payments without a digital storefront.

## Share your link

Use the Dashboard to copy your payment link and share it online. Click the copy icon next to an existing link on the Payment Links page, or go to the payment link’s details page. You can share your payment link multiple times and anywhere online, including emails, text messages, and social media platforms.

## Generate a QR code

You can create a QR code for a payment link in the Dashboard. Choose an existing link from the Payment Links page, or create a new link and then click QR code. Copy or download a PNG image of the QR code.

The QR code doesn’t expire. If you deactivate the underlying payment link, the QR code redirects to an expiration page.

## Embed a button on your site

Turn your payment link into an embeddable buy button to sell a product or subscription from your website. Select an existing link from the Payment Links page or create a new link and then click Buy button. Copy the code and paste it into your website. To learn more on how to embed and customize a button, see Create a buy button.

## Deactivate a link

You can use the Dashboard to deactivate a payment link. Click the overflow menu () to the right of the desired payment link, and then Deactivate. After you deactivate a link, customers are no longer able to make a purchase using it. You can choose to reactivate the payment link at any time. You can also use the API to deactivate a payment link.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Share your link](#share-online)[Generate a QR code](#create-qr-code)[Embed a button on your site](#embed-button)[Deactivate a link](#deactivate-a-link)Products Used[Payments](/payments)[Payment Links](/payments/payment-links)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`