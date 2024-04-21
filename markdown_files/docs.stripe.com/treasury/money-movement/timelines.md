htmlMoney movement timelines | Stripe Documentation[Skip to content](#main-content)Money movement timelines[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoney-movement%2Ftimelines)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Ftreasury%2Fmoney-movement%2Ftimelines)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/financial-services)[Start an integration](#)Products[Issuing cards](#)[Treasury](#)
[Business financing](#)NetherlandsEnglish (United States)[](#)[](#)[Treasury](/treasury)·[Home](/docs)[Banking as a service](/docs/financial-services)[Treasury](/docs/treasury)# Money movement timelines

Learn about the timelines for various types of money movement in Treasury.Stripe Treasury integrates with banking partners and payment networks which each have varying processing and cutoff times.

## OutboundPayment and OutboundTransfer transactions

NetworkBehavior`ach``OutboundPayment`and`OutboundTransfer`requests processed before the cutoff time are submitted to our banking partner on the same day. These transfers are expected to arrive at the receiving bank within the next one to two business days. Same DayACHtransactions arrive at the receiving bank the same business day if the request is received before the cutoff time.`us_domestic_wire``OutboundPayment`and`OutboundTransfer`requests processed before the cutoff are expected to arrive at the receiving bank on the same business day.`stripe``OutboundPayment`requests using the`stripe`network post immediately and arrive at the receiving financial account within minutes, both during and outside of business hours.`OutboundTransfer`requests aren’t yet supported for`stripe`network transactions.### Evolve Bank & Trust

- `ach`cutoff:  - Default Speed: 6pm central time (CST/CDT)
  - Same Day speed: 11am central time (CST/CDT)


- `us_domestic_wire`cutoff: 3pm central time (CST/CDT)

Submission dateArrival date (by end of business day)ACHWireMondayTuesdayMondayTuesdayWednesdayTuesdayWednesdayThursdayWednesdayThursdayFridayThursdayFridayMondayFridaySaturdayTuesdayMondaySundayTuesdayMondayYou can programmatically access expected_arrival_date field on OutboundPayment or OutboundTransfer to reference when Stripe expects the funds to arrive at their destination.

Requests that are received after the cutoff times are processed the following business day. Default speed requests that are received after the cutoff times are processed the following business day. Same Day ACH requests received after cut off time arrive the following business day by end of day.

## InboundTransfer transactions

NetworkBehavior`ach``InboundTransfer`If using the default speed,`InboundTransfer`requests processed before the cut-off time are submitted to our banking partner on the same business day. Otherwise, they’re submitted on the following business day. Transfers are expected to arrive in the Treasury financial account on the morning of the fourth business day, after submission to the banking partner, if no returns are received during that time.### Evolve Bank & Trust

Submission date, before 6pm central time (CST/CDT)Available at approximately 10am central time (CST/CDT)MondayFridayTuesdayMondayWednesdayTuesdayThursdayWednesdayFridayThursdaySaturdayFridaySundayFriday## ReceivedCredit and ReceivedDebit transactions

Credits and debits initiated from outside Stripe and received on a financial account are processed as soon as Stripe receives notification of the transfer. The time it takes to complete the transfer depends on the originating institution.

NetworkBehavior`ach`Available same day or next business day depending on originating institution.`us_domestic_wire`Depends on originating institution.`stripe`Transfers using the`stripe`network post immediately and are expected to arrive at the receiving financial account within minutes.`card`Card transaction are typically captured within 24 hours of authorization approval; however, some companies can capture funds for up to 30 days after authorization. See[Issuing transactions](/issuing/purchases/transactions).## Automatic payouts

All platforms using Treasury have access to standard automatic payouts, which move money from Stripe Payments to a Treasury financial account on a T+2 or slower schedule from the time of transaction (T+2 for card payments, slower for ACH).

You can request a platform risk review to access faster payouts; upon approval, your platform can use T+1 and T+0 automatic payouts for connected accounts. T+1 and T+0 faster payout schedules apply to all payment types, including both card payments and ACH payments, and the timelines start when the transaction occurs (faster payouts eliminate the need to wait for standard payments fund settlement times).

Contact treasury-support@stripe.com if you want to request access to faster payouts for your platform.

For more details, see the Automatic payouts guide.

## Manual payouts

Platforms using Treasury also have access to standard manual payouts, which move funds in one business day (T+1 schedule) but can only draw on an account’s available payments balance. In other words, you must wait for funds from a payment to settle in the payments balance before initiating a standard manual payout to a Treasury financial account.

Platforms granted access to faster payouts also have ‘instant’ manual payouts available, which move funds to a connected account’s financial account within an hour (T+0 schedule) and are available anytime, including nights, weekends, and holidays. Instant manual payouts are drawn on a connected account’s instant_available balance rather than being limited to the available balance.

For more details, see the Manual payouts guide.

## Top ups

Stripe Connect platform users can top up their existing Stripe platform account balance using a Stripe Treasury financial account by verifying the routing and account numbers. These funds settle to your account balance according to the Top ups settlement timing.

See Adding funds to your platform balance for more details.

## See also

- [Moving money out of financial accounts](/treasury/moving-money/moving-money-out-of-financial-accounts)
- [Moving money into financial accounts](/treasury/moving-money/moving-money-into-financial-accounts)
- [Payouts](/treasury/moving-money/payouts)

## Same Day ACH regulations

ACH transactions are regulated by NACHA. Consider the following when using Same Day ACH:

- Individual Same Day ACH transactions don’t exceed 1,000,000 USD.
- Payments made to a single entity for a single purpose (such as vendor payment) aren’t divided to exceed the 1,000,000 USD limit per transaction. If this happens, Stripe remits the funds exceeding the limit the following day.
- Payments to different parties for different purposes can exceed 1,000,000 USD if they’re divided across separate transactions.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[OutboundPayment and OutboundTransfer transactions](#outboundpayment-and-outboundtransfer-transactions)[InboundTransfer transactions](#inboundtransfer-transactions)[ReceivedCredit and ReceivedDebit transactions](#receivedcredit-and-receiveddebit-transactions)[Automatic payouts](#automatic-payouts)[Manual payouts](#manual-payouts)[Top ups](#top-ups)[See also](#see-also)[Same Day ACH regulations](#same-day-ach-regulations)Products Used[Treasury](/treasury)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`