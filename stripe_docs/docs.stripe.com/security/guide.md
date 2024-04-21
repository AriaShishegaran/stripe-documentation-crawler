# Integration security guide

Anyone involved with the processing, transmission, or storage of card data must comply with the Payment Card Industry Data Security Standard (PCI DSS). An independent PCI Qualified Security Assessor (QSA) audited and certified Stripe as a PCI Level 1 Service Provider. This is the most stringent level of certification available in the payments industry.

[Payment Card Industry Data Security Standard](https://www.pcisecuritystandards.org/pci_security/)

[PCI Level 1 Service Provider](https://www.visa.com/splisting/searchGrsp.do?companyNameCriteria=stripe,%20inc)

PCI compliance is a shared responsibility and applies to both Stripe and your business. When accepting payments, you must do so in a PCI compliant manner. The simplest way for you to be PCI compliant is to never see (or have access to) card data at all. Stripe makes this easy for you as we can do the heavy lifting to protect your customers’ card information. You can simplify your PCI compliance as long as you:

[PCI compliance](/security/guide#validating-pci-compliance)

- Use one of our recommended payments integrations to collect payment information, which is securely transmitted directly to Stripe without it passing through your servers.

[payments integrations](/payments)

- Serve your payment pages securely using Transport Layer Security (TLS) so that they make use of HTTPS

[Transport Layer Security](#tls)

[TLS](/security/guide#tls)

- Review and validate your account’s PCI compliance annually.

[validate](#validating-pci-compliance)

## Validate your PCI compliance

All Stripe users must validate their PCI compliance annually. Most users can do this with a Self-Assessment Questionnaire (SAQ) provided by the PCI Security Standards Council. The type of SAQ depends on how you integrated Stripe and which of the methods below you use to collect card data. Certain methods might require you to upload additional PCI documentation to us. If this is necessary, you can upload them in the Dashboard. If you’re using more than one of the methods below, you don’t need to upload multiple SAQs.

[Self-Assessment Questionnaire](https://www.pcisecuritystandards.org/document_library?category=saqs#results)

[PCI Security Standards Council](https://www.pcisecuritystandards.org/)

If you’re not sure how to prove that your business is PCI compliant (for example, a third-party built your integration), we suggest that you talk to a PCI QSA to determine how to best validate your compliance according to the current guidance from the PCI Council.

[current guidance](https://pcissc.secure.force.com/faq/articles/Frequently_Asked_Question/If-a-merchant-develops-an-application-that-runs-on-a-consumer-s-device-e-g-smartphone-tablet-or-laptop-that-is-used-to-accept-payment-card-data-what-are-the-merchant-s-obligations-regarding-PCI-DSS-and-PA-DSS-for-that-application)

Direct API

SAQ D

When you pass card information directly to Stripe’s API, your integration is directly handling that data and you’re required to annually prove your PCI compliance using the SAQ D–the most demanding of the SAQs. To reduce this burden:

[SAQ D](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2_1-SAQ-D_Merchant.pdf)

- Integrate with Checkout, Elements, or our mobile SDKs.

[Checkout](/payments/checkout)

[Elements](/payments/elements)

[mobile SDKs](/payments/accept-a-payment)

- Migrate to client-side tokenization of card information.

[client-side tokenization](/payments/elements)

In addition, our fraud prevention tool, Radar, which includes risk evaluation and rules, is only available when using any of our methods of client-side tokenization.

[Radar](/radar)

[risk evaluation](/radar/risk-evaluation)

[rules](/radar/rules)

[Checkout](/payments/checkout)

[Stripe.js and Elements](/payments/elements)

Dashboard

SAQ C-VT

Manual card payments through the Dashboard are possible for exceptional circumstances only, not routine payment processing. Provide a suitable payment form or mobile application for your customers to enter their card information.

We can’t verify that manually entered card information is secure outside of Stripe, so you must protect card data in accordance with PCI compliance requirements and complete the SAQ C-VT annually to prove your business is PCI compliant.

[SAQ C-VT](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2_1-SAQ-C_VT.pdf)

Mobile SDK

SAQ A

Stripe’s mobile SDK development and change control complies with PCI DSS (requirements 6.3-6.5) and deploys through our PCI validated systems. When you only use UI components from our official SDKs for iOS or Android, or build a payment form with Elements in a WebView, card numbers pass directly from your customers to Stripe, so you have the lightest PCI compliance burden.

[mobile SDK](/payments/accept-a-payment)

[Elements](/payments/elements)

If you do otherwise, such as writing your own code to handle card information, you might be responsible for additional PCI DSS requirements (6.3-6.5) and would be ineligible for an SAQ A. Talk to a PCI QSA to determine how to best validate your compliance according to the current guidance from the PCI Council.

[current guidance](https://pcissc.secure.force.com/faq/articles/Frequently_Asked_Question/If-a-merchant-develops-an-application-that-runs-on-a-consumer-s-device-e-g-smartphone-tablet-or-laptop-that-is-used-to-accept-payment-card-data-what-are-the-merchant-s-obligations-regarding-PCI-DSS-and-PA-DSS-for-that-application)

If your application requires your customers to enter their information on their own devices, then you qualify for SAQ A. If your application accepts card information for multiple customers on your device (for example, a point of sale app), consult a PCI QSA to learn how to best validate your PCI compliance.

[PCI QSA](https://www.pcisecuritystandards.org/assessors_and_solutions/qualified_security_assessors)

Stripe.js v2

SAQ A-EP

Using Stripe.js v2 to pass card data entered in a form hosted on your own site requires completing the SAQ A-EP annually to prove your business is PCI compliant.

[SAQ A-EP](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2_1-SAQ-A_EP.pdf)

Alternatively, both Checkout and Elements allow you the flexibility and customizability of a self-hosted form, while also meeting PCI eligibility for the SAQ A.

[Checkout](/payments/checkout)

[Elements](/payments/elements)

Terminal

SAQ C

If you exclusively collect card data through Stripe Terminal, you can validate using SAQ C.

If you integrate with Stripe using additional methods listed in this table, you must illustrate compliance for them separately as described.

If you’re processing more than 6 million transactions per year with Visa or MasterCard, or more than 2.5 million transactions with American Express, or are otherwise deemed to be a Level 1 provider by any of the card networks, you’re not eligible to use a SAQ to prove PCI compliance. Payment brands require you to complete a Report on Compliance (RoC) to validate your PCI compliance annually.

[Report on Compliance](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2_1-ROC-Reporting-Template.pdf)

## Use TLS and HTTPS

TLS refers to the process of securely transmitting data between the client—the app or browser that your customer is using—and your server. The Secure Sockets Layer (SSL) protocol originally performed this, but is outdated and no longer secure. TLS replaced SSL, but the term SSL continues to be used colloquially when referring to TLS and its function to protect transmitted data.

Payment pages must use a recent version (TLS 1.2 or above) because it significantly reduces the risk of man-in-the-middle attacks for both you and your customers. TLS attempts to accomplish the following:

- Encrypt and verify the integrity of traffic between the client and your server.

- Verify that the client is communicating with the correct server. In practice, this usually means verifying that the owner of the domain and the owner of the server are the same entity. This helps prevent man-in-the-middle attacks. Without it, there’s no guarantee that you’re encrypting traffic to the right recipient.

Additionally, your customers are more comfortable sharing sensitive information on pages visibly served over HTTPS, which can help increase your customer conversion rate.

You can test your integration without using HTTPS if you need to, and enable it when you’re ready to accept live charges. However, all interactions between your server and Stripe must use HTTPS (that is, when using our libraries).

[test](/testing)

## Set up TLS

Make sure any resources (for example, JavaScript, CSS, and images) are also served over TLS to avoid your customers seeing a mixed content warning in their browser.

[mixed content warning](https://web.dev/what-is-mixed-content/)

Using TLS requires a digital certificate—a file issued by a certification authority (CA). Installing this certificate assures the client that it’s actually communicating with the server it expects to be talking to, and not an impostor. Obtain a digital certificate from a reputable certificate provider, such as:

- Let’s Encrypt

[Let’s Encrypt](https://letsencrypt.org)

- DigiCert

[DigiCert](https://www.digicert.com/tls-ssl/basic-tls-ssl-certificates)

- NameCheap

[NameCheap](https://www.namecheap.com/security/ssl-certificates.aspx)

Certificates vary in cost, depending on the type of certificate and provider. “Let’s Encrypt” is a certificate authority that provides certificates for free.

To set up TLS:

- Purchase a certificate from a suitable provider.

- Configure your server to use the certificate. This step can be complex, so follow the installation guide of the provider you use.

As TLS is a complex suite of cryptographic tools, it’s easy to miss a few details. We recommend using the SSL Server Test by Qualys SSL Labs to make sure you set up everything in a secure way.

[SSL Server Test](https://www.ssllabs.com/ssltest/)

## Security considerations

Including JavaScript from other sites makes your security dependent on theirs and poses a security risk. If they’re ever compromised, an attacker could execute arbitrary code on your page. In practice, many sites use JavaScript for services like Google Analytics, even on secure pages. Nonetheless, we recommend trying to minimize it.

If you’re using webhooks, use TLS for the endpoint to avoid traffic being intercepted and having notifications altered (sensitive information is never included in a webhook event).

[webhooks](/webhooks)

While complying with the Data Security Standards is important, it shouldn’t be where you stop thinking about security. Some good resources to learn about web security are:

- OWASP

[OWASP](https://owasp.org/)

- SANS

[SANS](https://www.sans.org/reading-room/)

- NIST

[NIST](http://csrc.nist.gov/)

Stripe returns non-sensitive card information in the response to a charge request. This includes the card type, the last four digits of the card, and the expiration date. This information isn’t subject to PCI compliance, so you’re able to store any of these properties in your database. Additionally, you can store anything returned by our API.

[API](/api)

If you’ve deployed a Content Security Policy, the full set of directives that Checkout, Connect embedded components, and Stripe.js require are:

[Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)

- connect-src, https://checkout.stripe.com

- frame-src, https://checkout.stripe.com

- script-src, https://checkout.stripe.com

- img-src, https://*.stripe.com

## See also

- What is PCI DSS compliance

[What is PCI DSS compliance](https://stripe.com/guides/pci-compliance)

- Declines and failed payments

[Declines and failed payments](/declines)

- Disputes overview

[Disputes overview](/disputes)
