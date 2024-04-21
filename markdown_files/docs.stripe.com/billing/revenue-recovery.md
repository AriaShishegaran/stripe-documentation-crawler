htmlRevenue recovery | Stripe Documentation[Skip to content](#main-content)Revenue recovery[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Frevenue-recovery)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/billing)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fbilling%2Frevenue-recovery)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)
[Tax](#)[Reporting](#)[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Billing](/docs/billing)# Revenue recovery

Learn about automated recovery features that reduce and recover failed subscription payments.Prevent lost revenue and reduce churn with Stripe’s revenue recovery features. These automated tools make sure you don’t lose revenue to failed payments or missed trial conversions. None of the features require you to write code, so you can start recovering revenue today.

Recovering one-off invoicesThis page describes recovery features for subscriptions and other recurring revenue. Learn more about setting up automatic collection and recovery for one-off invoices.

## Revenue recovery features

Stripe provides a full tool set to help you recover recurring revenue:

[Recovery analyticsAnalyze subscription payment failure rates, recovery rates, and recent failed payments for top customers.](/billing/revenue-recovery/recovery-analytics)[Smart RetriesAutomatically retry failed payments to prevent involuntary churn due to temporary issues.](/billing/revenue-recovery/smart-retries)[Email notificationsAutomatically send emails to customers when a payment fails, a card expires, or a payment method requires an update.](/billing/revenue-recovery/customer-emails)[No code AutomationsImplement your own custom recovery logic without writing code.](/billing/revenue-recovery/automations)[Smarter saved cardsStripe automatically updates your customer’s card information when they get a new card number.](/billing/revenue-recovery/smarter-saved-cards)## Recurring revenue recovery optimizations

Stripe recommends including the following recurring revenue recovery optimizations in your integration. As you complete each item, check it off. Your browser’s cache stores the state of each checkbox so you can refer back to this page to see what you’ve completed so far.

- Set up failed payment retriesRetrying failed payments is one of the most effective ways to recover revenue. It requires no manual intervention from you or the customer.

You can set up Smart Retries and custom retry schedules in the Stripe Dashboard without writing any code. Smart Retries use data points to find the best time to retry the payment and are more effective than scheduled retries.

  - [Automate payment retries](/billing/revenue-recovery/smart-retries)


- Set up automatic customer emailsSet up automated customer emails to notify customers of possible issues. You can enable these based on your business’s use cases. Many businesses use failed payment and 3D Secure emails to help customers immediately fix failing payments.

  - [Automate customer emails](/billing/revenue-recovery/customer-emails).


- Set up automationsYou can set up more automations for custom logic and revenue recovery without writing code, including workflows like:

  - [Custom dunning flow for annual subscribers](/billing/revenue-recovery/automation-recipes#custom-dunning-flow)
  - [Notify your team when high value invoices are overdue](/billing/revenue-recovery/automation-recipes#invoice-overdue-notifications)
  - [Email a confirmation when a subscription is canceled](/billing/revenue-recovery/automation-recipes#subscription-cancellation-confirmation)

  - [Automation recipes](/billing/revenue-recovery/automation-recipes)
  - [Automations](/billing/revenue-recovery/automations)



Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Revenue recovery features](#revenue-recovery-features)[Recurring revenue recovery optimizations](#recurring-revenue-recovery-optimizations)Products Used[Billing](/billing)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`