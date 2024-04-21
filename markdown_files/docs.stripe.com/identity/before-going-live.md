htmlBefore going live | Stripe Documentation[Skip to content](#main-content)Before going live[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fidentity%2Fbefore-going-live)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fidentity%2Fbefore-going-live)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)
NetherlandsEnglish (United States)[](#)[](#)[Identity](/identity)·[Home](/docs)[Get started](/docs/get-started)[Verify identities](/docs/identity)# Before going live

Best practices to build a production-ready Stripe Identity integration.### Checklist progress

As you complete each item and check it off, the state of each checkbox is stored within your browser’s cache. You can refer back to this page at any time to see what you have completed so far.

- Make sure your use case and business are supportedReview the supported use cases and terms of service to make sure that your business can use Stripe Identity.


- Setup brandingThe verification experience shows your company name, logo, and color. Make sure to configure the branding settings for your account before going live.


- Limit the number of submission attemptsTo prevent fraudsters from abusing your verification flow and incurring charges on your account, we recommend that you limit the number of times a user can verify themselves.


- Limit how much sensitive information you storeAs much as possible, store only references to the verification and use the API to retrieve the VerificationSession when you need access to sensitive information. This simplifies your integration and limits your exposure from a security perspective, and helps you comply with privacy laws (such as GDPR) that require you to minimize data retention.


- Always authenticate your userWe recommend that you authenticate your user before showing or sending them to Stripe Identity. This allows you to keep relevant internal references and adds a layer of security to prevent fraudsters from abusing your verification flow.


- Provide an alternative verification methodStripe Identity may not be able to verify all of your users. For example, your user might decline to be verified using biometric technology, they might attempt to verify with an unsupported document type, or they might not be covered by Identity’s verification checks. We recommend that you provide alternative ways to verify your user, such as reaching out to your support team. In some jurisdictions, privacy laws (such as GDPR) might require you to offer a non-biometric verification option for users who decline to consent to using their biometric information.


- Follow webhook best practicesIf your integration depends on webhooks, make you sure you’ve tested that your integration handles Identity events correctly and that you’re following the Best practices for using webhooks.


- Follow the Stripe development checklistFollow the Development checklist to ensure a smooth transition when taking your integration live.


- Update your privacy policy if necessaryStripe Identity collects sensitive information, such as facial and identity document images. Make sure that your own privacy policy tells your customers about all the ways you may use or reuse the collected identity data and that this data is shared with Stripe. You could add the following paragraph to your policy if it doesn’t already include information about how their data is disclosed to Stripe:

We use Stripe for identity document verification. Stripe collects identity document images, facial images, ID numbers and addresses as well as advanced fraud signals and information about the devices that connect to its services. Stripe shares this information with us and also uses this information to operate and improve the services it provides, including for fraud detection. You may also choose to allow Stripe to use your data to improve Stripe’s biometric verification technology. You can learn more about Stripe and read its privacy policy at https://stripe.com/privacy.


- Provide a URL to your privacy policyMake sure your account settings include a link to your privacy policy. This URL will be linked from Stripe Identity.


- Explain ID verification and Stripe Identity to your customersAdd information to your site answering common questions about identity verification and your use of Stripe Identity. See the FAQ template.


- Explain to your users how to delete their data from Stripe’s serversWhen your users request their data to be deleted, redact the VerificationSession and let your users know that they’ll need to contact Stripe support to remove their data from Stripe’s servers. You could add the following paragraph to your application:

We use Stripe for identity document verification. Stripe retains a copy of all the data provided as part of a verification. You may also have consented to allow Stripe to use your data to improve their technology. You can delete your information from Stripe’s servers or revoke your consent by visiting https://support.stripe.com.



## See also

- [Is my use case supported?](/identity/use-cases)
- [Development checklist](/get-started/checklist/go-live)
- [Take webhooks live](/webhooks#register-webhook)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`