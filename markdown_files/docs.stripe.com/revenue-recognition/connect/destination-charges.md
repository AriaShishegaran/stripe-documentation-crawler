htmlRevenue Recognition for destination charges | Stripe Documentation[Skip to content](#main-content)Destination charges[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fconnect%2Fdestination-charges)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Frevenue-recognition%2Fconnect%2Fdestination-charges)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/finance-automation)[Billing](#)[Tax](#)[Reporting](#)
[Data](#)[Startup incorporation](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Finance automation](/docs/finance-automation)[Reporting](/docs/stripe-reports)[Revenue recognition](/docs/revenue-recognition)[Connect platforms](/docs/revenue-recognition/connect)# Revenue Recognition for destination chargesBeta

Learn how Revenue Recognition works with destination charges.## Revenue collected with application_fee_amount

If the destination charges collects fees with application_fee_amount, the charge and transfer happen immediately, and the application_fee_amount is immediately recognized as the revenue.

In this example, the application_fee_amount="200" is set on the charge.

- On January 15, the full charge amount of 10 USD is added to your platform account.  - 10 USD is transferred to the connected account.
  - The 2 USD application fee is transferred back to your platform.



AccountJanRevenue+2.00Cash+2.00## Revenue collected with transfer_data[amount]

If the destination charges collect fees with transfer_data[amount], the charge and transfer happen immediately, where you subtract your platform’s fees from the charge amount, then pass the result of this calculation as the transfer_data[amount]. The platform’s fees are immediately recognized as revenue.

In this example, the transfer_data[amount]="800" is set on the charge.

- On January 15, the full charge amount 10 USD is added to your platform account.  - 8 USD is transferred to the connected account.
  - The 2 USD is recognized as the revenue.



AccountJanRevenue+2.00Cash+2.00## Loss and contra revenue with issuing refunds

When collecting fees with application_fee_amount

If the destination charges issue refunds, by default the destination account keeps the funds that were transferred to it, leaving the platform account to cover the negative balance from the refund. The refund amount is booked as the ConnectTransferLoss.

In this example, the charge collects fees with application_fee_amount, and it is fully refunded in February.

- On January 15, the full charge amount of 10 USD is added to your platform account.  - 10 USD is transferred to the connected account.
  - The 2 USD application fee is transferred back to your platform.


- On February 21, the full charge amount 10 USD is refunded.

AccountJanFebRevenue+2.00Cash+2.00-10.00ConnectTransferLoss+10.00If the platform account sets reverse_transfer=true and refund_application_fee=true when calling the refund API:

- If the transfer reversal succeeded, the ConnectTransferLoss is canceled out by the transfer reversal.
- The refunded application fee is booked as contra revenue.

AccountJanFebRevenue+2.00Cash+2.00-2.00Refunds+2.00When collecting fees with transfer_data[amount]

In this example, the charge collects fees with transfer_data[amount], and it’s partially refunded in February and March.

- On January 15, the full charge amount of 10 USD is added to your platform account.  - 8 USD is transferred to the connected account.
  - The 2 USD is recognized as the revenue.


- On February 21, the partial charge amount 4 USD is refunded, and a proportional amount of the transfer 3.20 USD is reversed.
- On March 10, the partial charge amount 6 USD is refunded, and a proportional amount of the transfer 4.80 USD is reversed.

AccountJanFebMarTotalRevenue+2.00+2.00Cash+2.00-0.80-1.20Refunds+0.80+1.20+2.00## Best practices for effectively accessing the feature

Audit the destination charges journal entries

You can select the platform fee ID, platform fee refund ID, transfer ID, transfer refund ID, and charge destination ID columns when downloading the CSV reports format by invoice or line item.

![Revenue recognition report columns for the destination charges](https://b.stripecdn.com/docs-statics-srv/assets/connect-destination-charges-report-columns.503bbea8698306dc3a1282676b1e0d2c.png)

The month summary reports contain new items Revenue from platform fees and Less refunds from platform fees—you can find the details in the month summary section.

![Revenue recognition month summary items for the destination charges](https://b.stripecdn.com/docs-statics-srv/assets/connect-destination-charges-month-summary.6ac0f42f9d596630e5ffb95f7d84a451.png)

Check if your accounting period is open or closed when you’re added to the beta

It generates corrections if the beta is retroactively applied to transactions from past (closed) accounting periods. If you want to avoid this, reopen your books by opening your accounting periods prior to gating into the beta.

Destination charges exclusion rule

If you’re on destination charges exclusion rule, you can either delete the exclusion rules or set an effective period end date to apply the feature.

![Revenue recognition exclusion rule for the destination payments](https://b.stripecdn.com/docs-statics-srv/assets/connect-destination-charges-exclusion-rule.d002006b2460151217a08cdcbbef344d.png)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Revenue collected with application_fee_amount](#revenue-collected-with-application_fee_amount)[Revenue collected with transfer_data[amount]](#revenue-collected-with-transfer_data[amount])[Loss and contra revenue with issuing refunds](#loss-and-contra-revenue-with-issuing-refunds)[Best practices for effectively accessing the feature](#best-practices-for-effectively-accessing-the-feature)Products Used[Revenue Recognition](/billing/revenue-recognition)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`