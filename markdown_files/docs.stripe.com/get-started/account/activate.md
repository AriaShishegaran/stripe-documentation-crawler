htmlActivate your account | Stripe Documentation[Skip to content](#main-content)Activate your account[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Factivate)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Factivate)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)
Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Get started](/docs/get-started)Create an account# Activate your account

Activate your Stripe account and keep it safe.### Account checklist

For the safety and security of your Stripe account, complete our account checklist before going live.

You can begin using your Stripe account in test mode as soon as you create it. In test mode, you can simulate all of Stripe’s features without moving real money. To accept real payments, you need to first activate your account and then use live mode. If you haven’t created your Stripe account yet, complete that process before continuing.

## Activate your account

To activate your account, fill out the account application requesting some basic information about your business, product, and your personal relationship to your business. After activating your account, you can immediately start accepting live payments.

Stripe’s “Know Your Customer” (KYC) obligations require that we collect and maintain this information on all Stripe users. These requirements come from our regulators and financial partners, and are intended to prevent abuse of the financial system. We review the information you provide internally to make sure that it complies with our services agreement. We’ll contact you if we need any further information.

After you activate your Stripe account, you can’t change its country. If you need to use Stripe in a different country that we support, you must create a new account.

CautionWe take privacy and security very seriously. Our privacy policy explains how and for what purposes we collect, use, retain, disclose, and safeguard any personal data you provide to us.

## Public business information

### Close your account

You can close your account any time you want. We recommend you leave it dormant, however, in case you need to access any financial data or take action to resolve a dispute.

Your customers see the following details on either their card statements or in email receipts sent by Stripe.

- Business name and website URL
- Business email address, phone number, and address
- Support site URL
- Statement descriptor text

You provide this information when you activate your account, and can update it any time in your Account settings. Make sure that your statement descriptor text and business information are clearly associated with you. If your customer can’t recognize one of your payments, they might dispute it.

Statement descriptors are limited to between 5 and 22 characters. They must contain at least 5 letters and can’t use the special characters <, >, \, ', ", or *.

You can also use dynamic statement descriptors when creating a charge so that each payment has a custom statement descriptor. This dynamic text is appended to the shortened descriptor set in the Stripe Dashboard. Statement descriptor prefixes are limited to between 2 and 10 characters. For detailed information, see the documentation on statement descriptors.

## Keep your account safe

After you set up your account, you’ll want to keep it safe. Here are our recommendations:

- Keep private information private: Don’t share your password and keep your secret API keys confidential on your own servers. As a reminder, Stripe employees will never ask you for your keys.


- Don’t reuse your Stripe password: Use a password that’s unique to Stripe. If you use your password on another site and that site is compromised, an attacker could use those stolen credentials to take over your account.


- Use team members to provide others with access to your account: You can invite others (with limited access) to your Stripe account so that they can log in and take certain actions.


- Update your computer and browser regularly: We recommend configuring your computer to automatically download and install updates (for example, macOS or Windows). This helps protect your system against automated attacks and malware.


- Beware of phishing: All genuine Stripe sites use the stripe.com domain and HTTPS. If you get an email from us that you don’t expect, go directly to our site to log in. Don’t enter your password after clicking a link in an email. If you’re ever not sure it’s really us, review Verified Stripe domains on Stripe Support.


- Enable two-factor verification: When you enable two-factor authentication, you’ll need to provide an additional unique code from your mobile device to complete the login process—either received as a text message or generated through an app like Google Authenticator. This means that even if someone steals your username and password, they won’t be able to log in. To enable this feature, go to your user settings.



## See also

- [Account checklist](/get-started/checklist/account)
- [Multiple accounts](/get-started/account/multiple-accounts)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Activate your account](#activation)[Public business information](#public-business-information)[Keep your account safe](#protect-your-account)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`