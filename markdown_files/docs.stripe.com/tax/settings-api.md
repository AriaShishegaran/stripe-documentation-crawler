htmlUse the Settings API to configure Stripe Tax | Stripe Documentation[Skip to content](#main-content)Using the Settings API[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsettings-api)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftax%2Fsettings-api)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)
[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Tax](/tax)·[Home](/docs)[Finance automation](/docs/finance-automation)[Tax](/docs/tax)# Use the Settings API to configure Stripe Tax

Learn how to configure tax settings, and check whether an account is ready to perform tax calculations.The Stripe Tax Settings API lets you retrieve and configure the settings required to calculate tax without relying on the Stripe Dashboard.

- Connect platform: As a platform, you can use this API to set up your connected accounts to use Stripe Tax, or to validate whether an account is already set up appropriately.
- Direct usage: You can use this API to set up Stripe Tax, or to validate whether you’re already set up appropriately.

Connect platformDirect usage## Check if the connected account is ready to use Stripe Tax

Complete this check when the Standard account configures Stripe Tax through the Stripe Dashboard but your platform needs to assess if Stripe Tax can be enabled.

Use our official libraries for access to the Stripe API from your application. To check the Stripe Tax settings on the connected account, retrieve the tax.settings object using the Stripe-Account header with a value of the connected account ID:

Command Line[curl](#)`curl https://api.stripe.com/v1/tax/settings \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}"`You can also listen to the tax.settings.updated webhook event which triggers when accounts update their tax settings or when new required tax settings are introduced. See take webhooks live to learn how to add a webhook endpoint, and make sure you select Listen to events on Connected accounts in the Dashboard.

An account is ready to use Stripe Tax if the response tax.settings object retrieved by the API or webhook event returns "active" for status. The defaults.tax_code and defaults.tax_behavior settings are only required if not provided in the product or price on each API call.

`{
  "object": "tax.settings",
  "defaults": {
    "tax_code": null,
    "tax_behavior": null
  },
  "head_office": {
    "address": {
      "country": "DE"
    }
  },
  "livemode": false,
  "status": "active",
  "status_details": {
    "active": {}
  }
}`An account isn’t ready to use Stripe Tax if the response tax.settings object returns "pending" for status. The status_details[pending][missing_fields] has a list of all required missing fields.

`{
  "object": "tax.settings",
  "defaults": {
    "tax_code": null,
    "tax_behavior": null
  },
  "head_office": null,
  "livemode": false,
  "status": "pending",
  "status_details": {
    "pending": {
      "missing_fields": ["head_office"]
    }
  }
}`## Configure connected account settings

Complete this step when you manage all Stripe Tax configuration through an interface on your platform.

You can modify the connected account settings through an update settings call. Perform a call providing the head office location, the preset tax code, and the tax behavior by using the Stripe-Account header with a value of the connected account ID.

Command Line[curl](#)`curl https://api.stripe.com/v1/tax/settings \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d "defaults[tax_code]"=txcd_10000000 \
  -d "defaults[tax_behavior]"=inclusive \
  -d "head_office[address][country]"=DE`The updated tax.settings object now has a head office, a preset tax code, and a default tax behavior, which allows you to enable Stripe Tax for this connected account.

`{
  "object": "tax.settings",
  "defaults": {
    "tax_code": "txcd_10000000",
    "tax_behavior": "inclusive"
  },
  "head_office": {
    "address": {
      "country": "DE"
    }
  },
  "livemode": false,
  "status": "active",
  "status_details": {
    "active": {}
  }
}`### Validations and errors

The tax codes must refer to available tax codes and the tax behavior must be set as inclusive, exclusive, or inferred_by_currency (after being set, it can’t be set to null). The head_office must include a supported address.

The head_office[address] has the fields line1, line2, city, state, postal_code, and country. The tables below describe the supported address formats.

United StatesCanadaEverywhere elseExample addressesExplanationSupported- `line1`: 27 Fredrick Ave
- `city`: Brothers
- `state`: OR
- `postal_code`: 97712
- `country`: US

Full address

A full address includes at least a line1 (street address), city, state, postal code, and country.

The address is matched to the closest address or street in the US Postal Service address database. If a match isn’t found, we use the geographical center (average location of addresses) of the 5-digit postal code as a fallback.

9-digit postal code:

- `postal_code`: 97712-4918
- `country`: US

5-digit postal code:

- `postal_code`: 97712
- `country`: US

Country and postal code

If you provided a 5-digit or 9-digit postal code, we calculate tax at the geographical center (average location of addresses) of the 5-digit postal code area. Check that this is suitable for your business.

- `state`: OR
- `country`: US

Country and state

We can’t calculate tax for US customers with only an ISO country code and state code.

- `country`: US

Country

We can’t calculate tax for US customers with only an ISO country code.

Use one of the above address formats to make sure that we can consistently recognize your connected account’s head office location. The country field must always be a valid ISO country code.

NoteThe validation and errors listed here are part of the setup phase. You can still see other errors when trying to call the API on your Stripe integration.

Are you looking to offer sales tax, VAT, and GST compliance to your connected accounts?We plan to offer early access to embedded components for tax, which are UI widgets you can integrate into your platform to enable tax compliance for your connected accounts. To request early access, enter your email below.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.## See also

- [Use the Registrations API to manage tax registrations](/tax/registrations-api)
- [Use Stripe Tax with Connect](/tax/connect)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Check if the connected account is ready to use Stripe Tax](#checking-settings)[Configure connected account settings](#updating-settings)[See also](#see-also)Products Used[Tax](/tax)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`