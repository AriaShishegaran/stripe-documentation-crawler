htmlManaging payout schedule | Stripe Documentation[Skip to content](#main-content)Manage payout schedule[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fmanage-payout-schedule)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fmanage-payout-schedule)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Managing payout schedule

Manage the automatic payout schedule to your connected accounts.When using automatic payouts, the settings.payouts.schedule hash on an Account contains details on when a Stripe account’s funds are available and when the balance is automatically paid out:

`{
  "id": "{{CONNECTED_ACCOUNT_ID}}",
  "object": "account",
  "settings": {
    "payouts": {
      "schedule": {
        "delay_days": 7,
        "interval": "daily"
      },
      ...
    },
    ...
  },
  ...
}`### delay_days property

The delay_days property reflects how long it takes for on_behalf_of charges (or direct charges performed on the connected account) to become available for payout. You can edit this property on accounts where you own fraud and dispute liability.

This field is useful for dictating automatic payouts. For example, if you want your connected accounts to receive their funds two weeks after the charge is made, set interval to daily and delay_days to 14. Stripe calculates the delay in business days or calendar days based on the connected accounts’ country. When setting or updating this field, you can pass the string minimum to choose the lowest permitted value.

For accounts where Stripe manages fraud and dispute liability (for example, Standard accounts), the default is the lowest permitted value for the account, determined by the connected account’s country. If you’re opted into accelerated payout speeds, the value uses the accelerated timing. You can request to lower this by contacting Stripe Support. For accounts where you own fraud and dispute liability, the value remains at your original payout speed by default.

### Interval property

Platforms that manage fraud and dispute liability, or have platform controls, can adjust the payout interval. There are four possible settings for the interval property:

- manual: This setting prevents automatic payouts. You will have to manually pay out the account’s balance using the[Payouts API](/api#create_payout)(acting as the connected account). You also set an account to`manual`to use[Instant Payouts](/connect/instant-payouts).
- daily: This setting automatically pays out charges`delay_days`days after they’re created. The`delay_days`value can’t be less than your own payout schedule or less than the default payout schedule for the account.
- weekly: This setting automatically pays out the balance once a week, with the day specified by the`weekly_anchor`parameter (a lower-case weekday such asmonday).
- monthly: This setting automatically pays out the balance once a month, as specified by the`monthly_anchor`parameter (a number from 1 to 31). Payouts nominally scheduled between the 29th and 31st of the month are instead sent on the last day of a shorter month.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`