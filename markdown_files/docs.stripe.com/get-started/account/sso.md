htmlSingle sign-on (SSO) | Stripe Documentation[Skip to content](#main-content)Single sign-on[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fsso)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)
Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Get started](/docs/get-started)Create an account# Single sign-on (SSO)Beta

Authenticate to the Stripe Dashboard with an Identity Provider.NoteSingle sign-on for the Dashboard is currently in invite only beta.

SSO is an account security feature which allows customers to mandate sign-in requirements and team member access to systems like the Stripe Dashboard. Specifically, Stripe supports Security Assertion Markup Language (SAML) version 2.0, which allows for the creation and authentication of team member accounts to be deferred to an Identity Provider (IdP).

SSO is an account security feature which allows customers to mandate sign-in requirements and team member access to systems like the Stripe Dashboard. It leverages authentication decisions defined through an IdP, such as password policies and mandating two-factor authentication and allows new team members to instantly sign in to the Dashboard using Just-in-Time (JIT) account provisioning.

Security incidentsIf your IdP is compromised, unauthorized parties might be able to access your Stripe account. You’re responsible for mitigating your exposure to security incidents by assessing the security requirements of your business as well as selecting and implementing security procedures and controls.

## Features

Stripe supports the following SSO features:

- SSO configuration options: Configure Stripe accounts to either mandate SSO for all team members or allow sign-in using SSO or email and password.
- JIT account creation: Provision new Stripe accounts for team members without existing access, upon their first SSO sign-in.
- Custom Dashboard roles for team members: Configure Dashboard roles through the IdP. This is compatible with[user roles](/get-started/account/teams).
- IdP-initiated login: Directly authenticate from an IdP’s website or browser extension, assuming the IdP supports Service-Provider-Initiated login.

Stripe doesn’t support the following features:

- User Deletion in SAML: Due to the limitations of SAML, Stripe won’t be notified if user access is revoked in IdP. When users try to log in again through SSO after the current session expires, Stripe revokes their access. If this needs to happen instantly, you can delete the users in your[Team settings](https://dashboard.stripe.com/settings/team).
- System for Cross-domain Identity Management (SCIM): SCIM is a protocol that an IdP can use to synchronize user identity lifecycle processes (for example, provisioning and deprovisioning access, and populating user details) with the service provider, such as Stripe.

## See also

- [Activate your account](/get-started/account/activate)
- [Start a team](/get-started/account/teams)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Features](#sso-features)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`