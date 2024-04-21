htmlLink in the Card Element | Stripe Documentation[Skip to content](#main-content)Link in the Card Element[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Flink%2Fcard-element-link)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Flink%2Fcard-element-link)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)
Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[Faster checkout with Link](/docs/payments/link)[Link with Web Elements](/docs/payments/link/elements-link)# Link in the Card Element

Enable one-click checkout using Link with the Card Element.CautionStripe no longer recommends using the Card Element as part of your Web Elements integration. To integrate Link, use one of our preferred Elements: the Link Authentication Element, Express Checkout Element, or Payment Element.

Use Link in the Card Element to save and autofill payment information for your customers, so they don’t need to enter their payment details manually.

The Card Element can take on two forms: a single line Card Element or split Elements (like Card Number, Expiry, and CVC). When referring to the Card Element, the following information applies to both forms.

## The Link flow

Single line Card ElementSplit ElementsWhen Link is enabled, the card input form displays a Link button, which an authenticated customer can click to autofill their payment details. They only need to authenticate their account once every 90 days on any Link-enabled business.

![Link autofilling customer payment details](https://b.stripecdn.com/docs-statics-srv/assets/link-single-ce-returning-user.e50d94e96551810ac4f95c2fabfd33b9.png)

Link autofilling customer payment details

If a customer hasn’t signed up for Link and they click the Link button, they’re asked to add their email address, phone number, and payment method. A customer can also enter their card details into the Card Element first, and save that card in a Link account.

![A customer signing up for Link](https://b.stripecdn.com/docs-statics-srv/assets/link-single-ce-new-user.b8495f2e5258b8cf04b5d43e3a290ec0.png)

A customer signing up for Link

If a returning Link customer clicks the Link button and needs to authenticate, Link asks them to do it with an SMS or email code. After the customer authenticates, Link loads their previously saved payment details, allowing them to check out faster.

![Link authenticating a customer](https://b.stripecdn.com/docs-statics-srv/assets/link-in-ce-dialog.ec3340f0aaa847f610249e7dcc3fb7ad.png)

Link authenticating a customer

We’re continuously optimizing Link to improve checkout conversion, and may selectively show Link when it’s most beneficial to customers at checkout. You can expect to see changes over time, including how and when Link appears.

## Link enablement

Link is supported in the Card Element globally for all businesses with granted access and doesn’t require additional fees or code changes (see note below for details). Link is fully compatible with the other features you receive from card payments.

Stripe automatically enables Link in the Card Element. If you want to turn Link off for all instances of the Card Element, visit the Link section of your payment Method settings and disable the Link in Card Element setting. This setting applies to both forms of the Card Element. To selectively disable Link in the Card Element, use the disableLink parameter. You only need to use one of these controls—if either disableLink is true or Link in the Card Element is disabled in settings, Link won’t appear in the Card Element.

Link isn’t visible in the Card Element if:

- The parent container that the Card Element is mounted in is too short in height or narrow in width to display the Link button.


- The Card Element is displayed on a browser that doesn’t support pop-ups, including in-app browsers. View information about supported browsers.


- The Cross-Origin-Opener-Policy is set to same-origin. The Link pop-up must communicate with the page that opened it, so Link in the Card Element isn’t compatible with configurations that block this communication.



NoteWe’re releasing Link in the Card Element in phases. Link for the single line Card Element was released in 2023, followed by Link in split Elements in late 2023 and early 2024. Only accounts with granted access can see Link in the Card Element in their Payment Method settings or use Link in production or test mode. Link isn’t currently supported for Stripe accounts based in India.

## Use the Card Element and Payment Request Button

You can also use Link with the Payment Request Button. Link in the Card Element operates independently from Link in the Payment Request button. If you use both the Payment Request Button and the Card Element, Link might appear in both during checkout. For more information on when Link appears in the Payment Request Button, see Link in the Payment Request Button.

## Link and Connect platforms

Link is automatically available to any accounts that access the Card Element through a Connect platform integration. Depending on a platform’s integration, a platform may be able to give its users (connected accounts) the ability to customize their own Link settings in the Dashboard:

### Eligibility requirements for connected platforms

If the following conditions are all met by your platform, then your connected accounts can manage their Link settings directly in their own Dashboard.

- You use direct charges.


- You create and charge payment methods on your connected accounts.


- Your connected accounts have access to the full Stripe Dashboard.



To set the default state for all connected accounts on your platform:

1. Click Edit settings under Your connected accounts in Payment Method settings.


2. Navigate to Link in the Card Element in the Link section.



### Ineligible connected platforms

In the following cases, Link is controlled by your platform account settings, and your connected accounts can’t customize their Link settings for payments processed through your platform:

- You create payment methods on your platform and then clone payment methods to your connected accounts.


- You use destination charges or separate charges and transfers.


- Your connected accounts don’t have access to the full Stripe Dashboard.



To manage your platform account settings:

1. Click Edit settings under Your Account in Payment Method settings.


2. Navigate to Link in the Card Element in the Link section. If you want to turn Link off for only specific connected accounts, you can use the disableLink parameter.



### Payment processing for connected accounts

- If your platform offers you the ability to customize your Link settings for platform payments, then you can manage your Link in Card Element settings within Payment Method settings by selecting your platform from the dropdown menu at the top of the page.


- If your platform isn’t able to offer you settings customization, then the platform determines Link’s availability for all payments processed through the platform, and you won’t have settings control for platform payments in your Dashboard.


- For payments you process without a platform, you can manage Link in your Payment Method settings by selecting “no platform” from the dropdown menu at the top of the page.



## Test Link in the Card Element

CautionDon’t store real user data in test mode Link accounts. Treat them as if they’re publicly available, because these test accounts are associated with your publishable key.

Link works with the following browsers:

- Chrome, Chrome Mobile, and Microsoft Edge.


- Safari on desktop and iOS (last 3 major versions).



Link is available in both production and test mode. You can create test mode Link accounts using any valid email address. The following table shows the fixed one-time passcode values that Stripe accepts for authenticating Link test mode accounts:

ValueOutcomeAny other 6 digits not listed belowSuccess000001Error, code invalid000002Error, code expired000003Error, max attempts exceededEnabling Link in test mode presents Link on all Card Element test mode sessions that meet the enablement requirements. In production, Link’s visibility might vary to maximize Link’s conversion benefits in each checkout session.

## See also

- [Stripe Web Elements](/payments/elements)
- [Link Authentication Element](/payments/elements/link-authentication-element)
- [Payment Element](/payments/payment-element)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[The Link flow](#the-link-experience)[Link enablement](#enable-link)[Use the Card Element and Payment Request Button](#payment-request-button)[Link and Connect platforms](#link-ce-for-connect)[Test Link in the Card Element](#test-link-in-the-card-element)[See also](#see-also)Products Used[Payments](/payments)[Elements](/payments/elements)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`