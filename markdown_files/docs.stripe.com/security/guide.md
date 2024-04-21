htmlIntegration security guide | Stripe Documentation[Skip to content](#main-content)Integration guide[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsecurity%2Fguide)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fsecurity%2Fguide)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)
[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Security](/docs/security)# Integration security guide

Ensure PCI compliance and secure customer-server communications.Anyone involved with the processing, transmission, or storage of card data must comply with the Payment Card Industry Data Security Standard (PCI DSS). An independent PCI Qualified Security Assessor (QSA) audited and certified Stripe as a PCI Level 1 Service Provider. This is the most stringent level of certification available in the payments industry.

PCI compliance is a shared responsibility and applies to both Stripe and your business. When accepting payments, you must do so in a PCI compliant manner. The simplest way for you to be PCI compliant is to never see (or have access to) card data at all. Stripe makes this easy for you as we can do the heavy lifting to protect your customers’ card information. You can simplify your PCI compliance as long as you:

- Use one of our recommended[payments integrations](/payments)to collect payment information, which is securely transmitted directly to Stripe without it passing through your servers.
- Serve your payment pages securely using[Transport Layer Security](#tls)([TLS](/security/guide#tls)) so that they make use of HTTPS
- Review and[validate](#validating-pci-compliance)your account’s PCI compliance annually.

## Validate your PCI compliance

All Stripe users must validate their PCI compliance annually. Most users can do this with a Self-Assessment Questionnaire (SAQ) provided by the PCI Security Standards Council. The type of SAQ depends on how you integrated Stripe and which of the methods below you use to collect card data. Certain methods might require you to upload additional PCI documentation to us. If this is necessary, you can upload them in the Dashboard. If you’re using more than one of the methods below, you don’t need to upload multiple SAQs.

If you’re not sure how to prove that your business is PCI compliant (for example, a third-party built your integration), we suggest that you talk to a PCI QSA to determine how to best validate your compliance according to the current guidance from the PCI Council.

### PCI compliance requirement by integration

IntegrationRequirementRecommendationDirect API

SAQ D

When you pass card information directly to Stripe’s API, your integration is directly handling that data and you’re required to annually prove your PCI compliance using the SAQ D–the most demanding of the SAQs. To reduce this burden:

- Integrate with[Checkout](/payments/checkout),[Elements](/payments/elements), or our[mobile SDKs](/payments/accept-a-payment).
- Migrate to[client-side tokenization](/payments/elements)of card information.

In addition, our fraud prevention tool, Radar, which includes risk evaluation and rules, is only available when using any of our methods of client-side tokenization.

Checkout or ElementsSAQ A[Checkout](/payments/checkout)and[Stripe.js and Elements](/payments/elements)host all card data collection inputs within an iframe served from Stripe’s domain (not yours) so your customers’ card information never touches your servers. Because of this, you have the lightest PCI compliance burden.ConnectSAQ AIf you exclusively collect card data through a Connect platform (for example, Squarespace), we can determine whether the platform provides the necessary PCI documentation.Dashboard

SAQ C-VT

Manual card payments through the Dashboard are possible for exceptional circumstances only, not routine payment processing. Provide a suitable payment form or mobile application for your customers to enter their card information.

We can’t verify that manually entered card information is secure outside of Stripe, so you must protect card data in accordance with PCI compliance requirements and complete the SAQ C-VT annually to prove your business is PCI compliant.

Mobile SDK

SAQ A

Stripe’s mobile SDK development and change control complies with PCI DSS (requirements 6.3-6.5) and deploys through our PCI validated systems. When you only use UI components from our official SDKs for iOS or Android, or build a payment form with Elements in a WebView, card numbers pass directly from your customers to Stripe, so you have the lightest PCI compliance burden.

If you do otherwise, such as writing your own code to handle card information, you might be responsible for additional PCI DSS requirements (6.3-6.5) and would be ineligible for an SAQ A. Talk to a PCI QSA to determine how to best validate your compliance according to the current guidance from the PCI Council.

If your application requires your customers to enter their information on their own devices, then you qualify for SAQ A. If your application accepts card information for multiple customers on your device (for example, a point of sale app), consult a PCI QSA to learn how to best validate your PCI compliance.

Stripe.js v2

SAQ A-EP

Using Stripe.js v2 to pass card data entered in a form hosted on your own site requires completing the SAQ A-EP annually to prove your business is PCI compliant.

Alternatively, both Checkout and Elements allow you the flexibility and customizability of a self-hosted form, while also meeting PCI eligibility for the SAQ A.

Terminal

SAQ C

If you exclusively collect card data through Stripe Terminal, you can validate using SAQ C.

If you integrate with Stripe using additional methods listed in this table, you must illustrate compliance for them separately as described.

WarningIf you’re processing more than 6 million transactions per year with Visa or MasterCard, or more than 2.5 million transactions with American Express, or are otherwise deemed to be a Level 1 provider by any of the card networks, you’re not eligible to use a SAQ to prove PCI compliance. Payment brands require you to complete a Report on Compliance (RoC) to validate your PCI compliance annually.

## Use TLS and HTTPS

TLS refers to the process of securely transmitting data between the client—the app or browser that your customer is using—and your server. The Secure Sockets Layer (SSL) protocol originally performed this, but is outdated and no longer secure. TLS replaced SSL, but the term SSL continues to be used colloquially when referring to TLS and its function to protect transmitted data.

Payment pages must use a recent version (TLS 1.2 or above) because it significantly reduces the risk of man-in-the-middle attacks for both you and your customers. TLS attempts to accomplish the following:

- Encrypt and verify the integrity of traffic between the client and your server.
- Verify that the client is communicating with the correct server. In practice, this usually means verifying that the owner of the domain and the owner of the server are the same entity. This helps prevent man-in-the-middle attacks. Without it, there’s no guarantee that you’re encrypting traffic to the right recipient.

Additionally, your customers are more comfortable sharing sensitive information on pages visibly served over HTTPS, which can help increase your customer conversion rate.

You can test your integration without using HTTPS if you need to, and enable it when you’re ready to accept live charges. However, all interactions between your server and Stripe must use HTTPS (that is, when using our libraries).

## Set up TLS

### Serve resources securely

Make sure any resources (for example, JavaScript, CSS, and images) are also served over TLS to avoid your customers seeing a mixed content warning in their browser.

Using TLS requires a digital certificate—a file issued by a certification authority (CA). Installing this certificate assures the client that it’s actually communicating with the server it expects to be talking to, and not an impostor. Obtain a digital certificate from a reputable certificate provider, such as:

- [Let’s Encrypt](https://letsencrypt.org)
- [DigiCert](https://www.digicert.com/tls-ssl/basic-tls-ssl-certificates)
- [NameCheap](https://www.namecheap.com/security/ssl-certificates.aspx)

Certificates vary in cost, depending on the type of certificate and provider. “Let’s Encrypt” is a certificate authority that provides certificates for free.

To set up TLS:

1. Purchase a certificate from a suitable provider.
2. Configure your server to use the certificate. This step can be complex, so follow the installation guide of the provider you use.

As TLS is a complex suite of cryptographic tools, it’s easy to miss a few details. We recommend using the SSL Server Test by Qualys SSL Labs to make sure you set up everything in a secure way.

## Security considerations

Including JavaScript from other sites makes your security dependent on theirs and poses a security risk. If they’re ever compromised, an attacker could execute arbitrary code on your page. In practice, many sites use JavaScript for services like Google Analytics, even on secure pages. Nonetheless, we recommend trying to minimize it.

If you’re using webhooks, use TLS for the endpoint to avoid traffic being intercepted and having notifications altered (sensitive information is never included in a webhook event).

While complying with the Data Security Standards is important, it shouldn’t be where you stop thinking about security. Some good resources to learn about web security are:

- [OWASP](https://owasp.org/)
- [SANS](https://www.sans.org/reading-room/)
- [NIST](http://csrc.nist.gov/)

### Out-of-scope card data that you can safely store

Stripe returns non-sensitive card information in the response to a charge request. This includes the card type, the last four digits of the card, and the expiration date. This information isn’t subject to PCI compliance, so you’re able to store any of these properties in your database. Additionally, you can store anything returned by our API.

### Content Security Policy

If you’ve deployed a Content Security Policy, the full set of directives that Checkout, Connect embedded components, and Stripe.js require are:

CheckoutConnect embedded componentsStripe.js- `connect-src`,`https://checkout.stripe.com`
- `frame-src`,`https://checkout.stripe.com`
- `script-src`,`https://checkout.stripe.com`
- `img-src`,`https://*.stripe.com`

## See also

- [What is PCI DSS compliance](https://stripe.com/guides/pci-compliance)
- [Declines and failed payments](/declines)
- [Disputes overview](/disputes)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Validate your PCI compliance](#validating-pci-compliance)[Use TLS and HTTPS](#tls)[Set up TLS](#setting-up-tls)[Security considerations](#security-considerations)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`