htmlBest practices for managing secret API keys | Stripe Documentation[Skip to content](#main-content)Best practices for managing secret API keys[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fkeys-best-practices)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fkeys-best-practices)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)
[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)API[API keys](/docs/keys)# Best practices for managing secret API keys

Learn how to manage secret API keys and handle key leaks.Secret API keys are a form of account credentials, like a username and password. If bad actors obtain a secret key, they can use it to harm your business and other parties in the Stripe ecosystem.

Stripe users own the responsibility of keeping secret API keys safe. Here are some best practices for how to do that, including by using Stripe-offered security features.

## Protecting against key leakage

- Use secure key management systems (KMS) to store secret keys.When you create a secret live mode key from the Stripe Dashboard, it is only revealed once. Immediately copy the key to a KMS, which is designed to handle sensitive information with encryption and access controls. Make sure you don’t leave a copy of the key in the local file.
- Grant access only to those who need it.Define a clear policy on which users have permission to create, update or read keys. Limit the access only to those who need it. Audit the access periodically to avoid excess privilege on keys.
- Don’t share secret keys using insecure means.Don’t share keys in emails, chat messages, or customer support messages. Stripe never asks you for your secret API key.
- Don’t store keys in source code repositories (such as GitHub).Bad actors might scan public source repositories for leaked keys. Even if the source repository is private, it could be shared with team members on their development environments.
- Don’t embed secret keys in applications.Bad actors can exploit secret keys by matching a certain string pattern in the application. Avoid embedding keys in applications such as client tools, SDKs, and mobile apps.
- Exercise your ability to roll your API Keys.Defining and exercising a process for rolling keys helps you understand where your keys are being used and prepares your organization in the event your API key is leaked. By having key rolling processes in place you’ll be prepared to respond to a key leak event with a minimum of impact on your business.
- Audit API request logs to monitor suspicious activities.We recommend that you regularly audit or monitor API[request logs](/development/dashboard/request-logs)to proactively identify misused API keys. Make sure your developers aren’t using live mode keys when a test mode key is appropriate. Learn more at[test mode versus live mode](/keys#test-live-modes).
- Regular training and updating documentation.Maintain up-to-date documentation about how to handle secret API keys within your organization and host regular training sessions to make sure best practices are followed.

## Adopt security features to protect your integration

- [Use restricted API keys](/keys#limit-access).Restricted API keys can customize read or write access to specific API resources. With restricted keys, especially when giving access to third parties, you can allow only the minimum access to resources required and limit the risk of keys.
- [Limit the IP addresses that can send API requests](/keys#ip-allowlist).You can configure your API key so that only requests from designated IP addresses are allowed. We recommended this if your service has stable egress IP ranges and a change management process for updating the allowlist when those egress ranges change.

## Handle leaked secret API keys

If you identified a secret key leak, such as if a key is accidentally published to GitHub， immediately roll the key from Stripe Dashboard and replace your integration with the new key. If you detected abnormal behaviors without confirming that the API key is leaked, we recommended that you roll the API keys proactively while investigating the root cause in parallel.

If Stripe detects that a live mode secret API key has been exposed, we will immediately notify you and request that you roll the key. It’s crucial for businesses to act promptly to reduce potential damages and financial losses caused by unauthorized use of the leaked key. Depending on the imposed risk and activity on the account, we might decide to roll the key on your behalf. In this case you will receive notifications about any action taken.

Stripe doesn’t guarantee that we will detect all leaked keys. You’re responsible for following the best practices to prevent potential key leaks and ensure your integration with Stripe is secure.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Protecting against key leakage](#protecting-against-key-leakage)[Adopt security features to protect your integration](#adopting-security-features)[Handle leaked secret API keys](#handling-leaked-keys)Related Guides[API keys](/docs/keys)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`