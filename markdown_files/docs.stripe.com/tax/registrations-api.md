htmlUse the Registrations API to manage tax registrations | Stripe Documentation[Skip to content](#main-content)Using the Registrations API[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fregistrations-api)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fregistrations-api)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)[Register](/docs/tax/registering)# Use the Registrations API to manage tax registrations

Learn how to add, schedule, and check active tax registrations.Businesses are required to register to collect taxes in locations where they have tax obligations. The Tax Registration API lets you retrieve and configure tax registrations using an API instead of the Dashboard. Adding your registrations in Stripe turns on tax calculation and collection for your transactions made through Stripe.

Different rules determine when and how a business needs to register to collect tax depending on the location. Learn more about tax collection in different locations.

- Connect platform: As a platform, you can use this API to manage the registrations of your connected accounts or to check an account’s active registrations.
- Direct usage: You can use this API to manage and check your registrations.

Connect platformDirect usage## List all tax registrations for your connected accounts

To get a list of your connected accounts’ tax registrations, make a list registrations call. You can filter the response by setting the status parameter to active, expired, or scheduled.

Command Line[curl](#)`curl -G https://api.stripe.com/v1/tax/registrations \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d status=active \
  -d limit=3`If your connected accounts don’t have access to the Stripe Dashboard, your platform can provide a UI for them to manage their tax registrations. The registrations endpoint helps you implement that functionality.

## Add a tax registration for your connected account

If a tax obligation and registration of the connected account is known to the platform, you can perform a create registration call using the Stripe-Account header with a value of the connected account ID to add or schedule the registration for the connected account.

Command Line[curl](#)`curl https://api.stripe.com/v1/tax/registrations \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d country=IE \
  -d "country_options[ie][type]"=oss_union \
  -d active_from=now`In this case, a tax.registration object is created in the connected account.

`{
  "object": "tax.registration",
  "active_from": 1669249440,
  "country": "IE",
  "country_options": {
    "ie": {
      "type": "oss_union"
    }
  },
  "livemode": false,
  "status": "active",
  ...
}`Alternatively, for connected accounts with access to the Stripe Dashboard (for example, Standard accounts), you can instruct them to set up Stripe Tax using the Dashboard, which includes adding tax registrations.

## Update and expire a tax registration for your connected account

You can’t delete a registration after it’s created, but you can end it by setting expires_at to a time when the registration is no longer active. Update the registrations with an update registration call using the Stripe-Account header with a value of the connected account ID:

Command Line[curl](#)`curl https://api.stripe.com/v1/tax/registrations/taxreg_NkyGPRPytKq66j \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d expires_at=now`In this case, the registration expires immediately. Tax calculations performed for the connected account after the expires_at won’t use this registration.

`{
  "object": "tax.registration",
  "active_from": 1669248000,
  "created": 1669219200,
  "expires_at": 1669334400,
  "livemode": false,
  "status": "active",
  ...
}`Are you looking to offer sales tax, VAT, and GST compliance to your connected accounts?We plan to offer early access to embedded components for tax, which are UI widgets you can integrate into your platform to enable tax compliance for your connected accounts. To request early access, enter your email below.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.## See also

- [Use the Settings API to configure Stripe Tax](/tax/settings-api)
- [Use Stripe Tax with Connect](/tax/connect)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[List all tax registrations for your connected accounts](#list-registrations)[Add a tax registration for your connected account](#adding-registration)[Update and expire a tax registration for your connected account](#expiring-registration)[See also](#see-also)Products Used[Tax](/tax)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`