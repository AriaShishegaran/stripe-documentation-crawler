htmlVirtual cards with Issuing | Stripe Documentation[Skip to content](#main-content)Virtual cards[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fvirtual)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/issuing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fissuing%2Fcards%2Fvirtual)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)
[Treasury](#)[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Issuing](/issuing)·[Home](/docs)[Banking as a service](/docs/financial-services)[Issuing cards](/docs/issuing)# Virtual cards with Issuing

Learn about virtual cards created with Issuing.You can retrieve or display virtual card details through the Dashboard, the API, or by using Issuing Elements. PCI-DSS rules protect cardholder data, and not all methods of card information retrieval are PCI-DSS compliant.

## Display virtual card details to cardholders

You can use Issuing Elements to display virtual card details to your cardholders without this information passing through your servers. This method is fully PCI-DSS compliant, and we recommend it for most Issuing users. Stripe offers Issuing Elements as a part of Stripe.js.

## Retrieve virtual card details

For PCI-DSS compliance, we recommend limiting retrieval of virtual card information to the Dashboard or Issuing Elements. If you use the API to retrieve card information, or if you export virtual card information from the Dashboard, store it in a password manager or otherwise encrypt it.

You can retrieve both the full unredacted card number and CVC from the API. For security reasons, you can only use these fields with virtual cards in live mode, and we omit them unless you explicitly request them with the expand property. You can only retrieve these fields for physical cards in test mode. Additionally, you can only access them through the Retrieve a card endpoint.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/issuing/cards \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "expand[]"=number \
  -d "expand[]"=cvc`## Details about PCI-DSS

If you are generating virtual cards for your own use, you are not required to attain PCI-DSS compliance for Issuing activity. If you are generating virtual cards for use by your users, you may be considered a Service Provider under PCI-DSS rules. Service Providers must be PCI-DSS compliant.

If you accept payments through Stripe, read more about your PCI-DSS obligations. These obligations are in addition to requirements noted above.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Display virtual card details to cardholders](#display-virtual-card-details-to-cardholders)[Retrieve virtual card details](#retrieve-virtual-card-details)[Details about PCI-DSS](#details-about-pci-dss)Products Used[Issuing](/issuing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`