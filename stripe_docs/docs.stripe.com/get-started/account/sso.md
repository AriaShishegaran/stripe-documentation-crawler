# Single sign-on (SSO)Beta

Single sign-on for the Dashboard is currently in invite only beta.

SSO is an account security feature which allows customers to mandate sign-in requirements and team member access to systems like the Stripe Dashboard. Specifically, Stripe supports Security Assertion Markup Language (SAML) version 2.0, which allows for the creation and authentication of team member accounts to be deferred to an Identity Provider (IdP).

SSO is an account security feature which allows customers to mandate sign-in requirements and team member access to systems like the Stripe Dashboard. It leverages authentication decisions defined through an IdP, such as password policies and mandating two-factor authentication and allows new team members to instantly sign in to the Dashboard using Just-in-Time (JIT) account provisioning.

If your IdP is compromised, unauthorized parties might be able to access your Stripe account. You’re responsible for mitigating your exposure to security incidents by assessing the security requirements of your business as well as selecting and implementing security procedures and controls.

## Features

Stripe supports the following SSO features:

- SSO configuration options: Configure Stripe accounts to either mandate SSO for all team members or allow sign-in using SSO or email and password.

- JIT account creation: Provision new Stripe accounts for team members without existing access, upon their first SSO sign-in.

- Custom Dashboard roles for team members: Configure Dashboard roles through the IdP. This is compatible with user roles.

[user roles](/get-started/account/teams)

- IdP-initiated login: Directly authenticate from an IdP’s website or browser extension, assuming the IdP supports Service-Provider-Initiated login.

Stripe doesn’t support the following features:

- User Deletion in SAML: Due to the limitations of SAML, Stripe won’t be notified if user access is revoked in IdP. When users try to log in again through SSO after the current session expires, Stripe revokes their access. If this needs to happen instantly, you can delete the users in your Team settings.

[Team settings](https://dashboard.stripe.com/settings/team)

- System for Cross-domain Identity Management (SCIM): SCIM is a protocol that an IdP can use to synchronize user identity lifecycle processes (for example, provisioning and deprovisioning access, and populating user details) with the service provider, such as Stripe.

## See also

- Activate your account

[Activate your account](/get-started/account/activate)

- Start a team

[Start a team](/get-started/account/teams)
