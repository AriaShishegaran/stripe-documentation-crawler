htmlWhat is Link? | Stripe Documentation[Skip to content](#main-content)What is Link?[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Flink%2Fwhat-is-link)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fpayments%2Flink%2Fwhat-is-link)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)
Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Payments](/payments)·[Home](/docs)[Payments](/docs/payments)[Faster checkout with Link](/docs/payments/link)# What is Link?

Learn what Link is and what you can do with it.### Country availability

See the list of countries and currencies that support Link.

Link is Stripe’s fast-checkout solution. It securely saves and autofills customer address and payment details, with support for credit cards, debit cards, US bank accounts, and other payment methods. Customers can save their shipping and payment details on your site or the checkout page of a different business—Link saves and autofills the information on any site where Link’s enabled.

If your customer wants to make changes to their account, view their purchase history, or reach out to the Link customer support team, have them visit link.com.

## Link authentication

Here’s how Link authenticates existing customers:

1. Link automatically detects if a customer is enrolled by using their email address, phone number, or browser cookie.
2. The customer receives a one-time passcode to authenticate their session.
3. After authentication succeeds, Link autofills their card (or bank payment) details and shipping information, allowing them to pay with one click.
4. After a customer enrolls with Link, they can add backup payment methods and change shipping addresses.

Link is a wallet and works with Checkout, Payment Links, Web Elements, Mobile Elements, and Invoicing. To accept payments using Link, go to your payment method settings.

## Link instant bank payments Beta

Link instant bank payments let you accept payments from customers with a US bank account. This gives your customers a choice in how they pay without you needing to manage the operational complexity of ACH Direct Debit.

Unlike ACH Direct Debit, where it can take up to four business days to successfully process a transaction, Link instant bank payments are instantly authorized. With this, settlement timing matches your card payments and you’re protected from bank-initiated returns that might occur after authorization.

You can’t accept both ACH Direct Debit and Link instant bank payments. If you’d rather accept ACH Direct Debit, you can toggle it on in your payment method settings. To learn more about ACH transaction fees, see its pricing details.

NoteAccess to Link instant bank payments is currently limited to beta users. If you’re interested in getting early access, please enter your email address in the signup form below.

When Link instant bank payments is enabled, a Bank tab appears on your checkout page. To be eligible for this beta, you must meet the following conditions:

- Your integration must use Checkout or the Payment Element.
- Enablement: You must enable Link on your account through your[payment settings dashboard](https://dashboard.stripe.com/settings/payment_methods)or[Link settings](https://dashboard.stripe.com/settings/link). You must also disable ACH Direct Debit in your payment method settings.
- Parameters: You use[automatic_payment_methods](/api/payment_intents/create#create_payment_intent-automatic_payment_methods)in your integration. Alternatively, you can update your integration to set[payment_method_type](/api/payment_intents/object#payment_intent_object-payment_method_types)to`link`.
- Two-step authentication: You’ve enabled[two-step authentication](https://support.stripe.com/questions/enable-two-step-authentication)on your Stripe account.
- Onboarding criteria: You must satisfy a set of onboarding criteria, including but not limited to: being a US business and having a history of Stripe usage.

Interested in getting early access to Link instant bank payments?Access is currently limited to beta users. If you're interested in trying it out, enter your email address.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you! We'll be in touch soon.## See also

- [Link with Checkout](/payments/link/checkout-link)
- [Link with Elements](/payments/link/elements-link)
- [Link with Billing](/payments/link/billing-link)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Link authentication](#link-authentication)[Link instant bank payments](#link-instant-bank-payments)[See also](#see-also)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`