htmlAccount checklist | Stripe Documentation[Skip to content](#main-content)Account checklist[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Fchecklist%2Faccount)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Fchecklist%2Faccount)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)
Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Get started](/docs/get-started)Checklists# Account checklist

Complete this checklist before taking your Stripe account live.### Checklist progress

As you complete each item and check it off, the state of each checkbox is stored within your browser’s cache. You can refer back to this page at any time to see what you’ve completed so far.

You can log in to see some of your current settings.

The items in this checklist apply to all Stripe accounts, regardless of how or where you signed up for Stripe. We also have checklists for taking your integration live and adhering to website payment best practices. For the safety and security of your Stripe account, follow these steps before going live:

- Enable two-step authenticationFor security purposes, enable two-factor authentication (2FA) on your Stripe account. Two-factor authentication requires that you log in with both your username and password, and enter a code sent to your mobile device. Using 2FA makes it harder for someone else to access your Stripe account.


- Confirm your statement descriptor and public informationThe statement descriptor appears on customer statements when you charge their card. Missing or incorrect information can result in confused customers creating disputes, so make sure to review your statement descriptor in the Dashboard. Statement descriptors are limited to between 5 and 22 characters. They must contain at least 5 letters and can’t use the following special characters: <, >, \, ', or ". Stripe also recommends that you add text to your site that tells your users what they’ll see on their statements.

The card issuer can automatically include other account information—for example, business name, address, email, or phone number—to show on your customer’s statements. Check that all of this information in your Stripe account is acceptable for your customers to see.


- Set up email notificationsStripe can notify you of account activity by email. You can choose events to be notified of in your Communication preferences. If multiple team members have access to your account, each one can set their own notification preferences. At a minimum, we recommend turning on emails for successful charges and disputes.


- Set up SMS from Stripe for critical account health updatesChoose the events to receive notification of in your Communication preferences. Any team member with account access can set their own notification preferences.


- Prevent and manage fraud and disputesFraud and disputes are unfortunate realities in all commerce. While Stripe is constantly improving its tools to help reduce these incidents, we recommend that you’re set up to:

  - Regularly review[payments in the Dashboard](https://dashboard.stripe.com/test/payments).
  - [Report charges](/radar/risk-evaluation)that appear suspicious using the Dashboard or API.
  - Have[evidence](/disputes/responding#respond)at the ready for disputes.
  - Prevent and mitigate[card testing](/disputes/prevention/card-testing).


- Review your bank account informationIncorrect bank information is a common cause of payout delays. Before accepting live charges, confirm your bank details are correct. If you process charges in multiple currencies and have multiple bank accounts, also confirm you’ve established the correct default currency. Multiple bank accounts for additional currencies are optional as Stripe can convert any payments into your default currency.

When reviewing your bank information, set your preferred payout schedule. The recommended and default option is daily—as funds become available—but you can change this to best suit your business and reporting needs.


- Give your team members access to your Stripe accountYou can give your team members access to your Stripe account. Stripe even lets you give different team members different permissions depending on their roles.

Whenever you give a team member access to your Stripe account, don’t give them your login credentials. We also recommend that you ask your team members to enable 2FA.

If a team member no longer needs access to your Stripe account, remove them from your account.


- Understand industry-specific restrictionsReview our Prohibited & Restricted businesses list to determine if your business operates in an industry that Stripe restricts or prohibits.

If your business operates in a restricted industry, you might need to provide additional documentation before you can use Stripe as your payment processor. If your business operates in a prohibited industry, you won’t be able to use Stripe.

If you have any questions about onboarding requirements or restrictions applicable to your business, contact us.



## See also

- [Multiple accounts](/get-started/account/multiple-accounts)
- [Start a team](/get-started/account/teams)
- [Custom email domain](/get-started/account/email-domain)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`