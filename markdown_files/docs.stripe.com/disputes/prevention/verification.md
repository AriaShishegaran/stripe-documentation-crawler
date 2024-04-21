htmlCard verification checks | Stripe Documentation[Skip to content](#main-content)Verification checks[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdisputes%2Fprevention%2Fverification)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdisputes%2Fprevention%2Fverification)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)
[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Radar](/radar)·[Home](/docs)[Get started](/docs/get-started)[Protect against fraud](/docs/radar)[Disputes and fraud](/docs/disputes)[Fraud prevention](/docs/disputes/prevention)# Card verification checks

Learn how to make use of card verification checks to protect against disputes and fraud.When a card payment is submitted to a card network for authorization, Stripe provides the CVC, postal code, and billing street address for them to verify (if you collected these from the customer in your checkout flow). The card issuer checks this against the information they have on file for the cardholder. If the provided information doesn’t match, the verification check fails. A failed CVC or postal code check can indicate the payment is fraudulent, so review it carefully before fulfilling the order.

Each Charge object includes the verification response as part of its source attribute. You can also find the verification results in the Dashboard when viewing a payment.

If no information is collected, the card issuer can’t perform a verification check. Collect the CVC, postal code, and billing address for every payment to avoid this issue. The results of verification checks help improve the detection of fraudulent activity.

## Card verification code check (CVC)

The CVC (also referred to as CVV) is the three- or four-digit number printed directly on a card, usually on the signature strip or the front of the card. Radar includes a rule to block any payments that fail the CVC verification check, which you can enable or disable within the Dashboard.

This doesn’t affect payments where the CVC check couldn’t be performed or is unavailable, for example Wallets like Apple Pay or off-session payments.

You can perform CVC verification by providing the CVC value either when you create a payment with a new card payment method, or when you attach a new card payment method to a customer.

In general, only cardholders in physical possession of the card should have access to the CVC number. Businesses are not permitted to store the CVC number, so it’s unlikely that a fraudster can obtain this information through a computer breach. However, CVC verification doesn’t protect against the physical theft of a card, nor card information being used on a computer or website that isn’t secure.

## Address verification (AVS)

Address verification (AVS) checks two pieces of information, the postal code and the billing street address. AVS checks determine whether this information matches the billing address on file with the card issuer. Radar includes a rule to block any payments that fail postal code verification, which you can enable or disable within the Dashboard.

If enabled, these address checks can fail on legitimate payments in some situations. For example, a customer entering their address incorrectly or moving and not updating their address with the card issuer could cause the address check to fail.

Support for both types of AVS checks varies by country and card issuer (for example, certain countries don’t use a postal code or some card issuers don’t support street address verification). However, street address verification is commonly supported for cards issued in the United States, Canada, and the United Kingdom.

## See also

- [Best Practices for Preventing Fraud](/disputes/prevention/best-practices)
- [Types of Fraud](/disputes/prevention/fraud-types)
- [Identifying Fraud](/disputes/prevention/identifying-fraud)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Card verification code check (CVC)](#cvc-check)[Address verification (AVS)](#avs-check)[See also](#see-also)Products Used[Radar](/radar)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`