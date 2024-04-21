htmlConnect margin reports | Stripe Documentation[Skip to content](#main-content)Connect margin reports[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fmargin-reports)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register/connect)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnect%2Fmargin-reports)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)
[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Connect](/connect)·[Home](/docs)[Payments](/docs/payments)[Connect](/docs/connect)# Connect margin reportsBeta

Compute your margins by analyzing your Connect volume, revenue and costs.Interested in the margin reports beta?Enter your email below and we'll reach out if you're eligible for the beta.Sign upRead our[privacy policy](https://stripe.com/privacy).Signed up successfully!Thank you for your interest!The Connect margin reports show platforms their aggregated and transaction-level payment volumes, fees, and revenue associated with activity where the platform is responsible for pricing and fees. Use these reports to calculate your margins and set your fees appropriately given your underlying Stripe fees and network costs.

## Platform support

These reports only support platforms that explicitly state an application fee on their charges, either directly in the API or through Platform Pricing Tools. They identify fees taken using application_fee_amount, but don’t identify fees taken using transfer_data.amount or account debits.

## User access

Users with the following user roles can access the Margin Reports:

- Administrator
- Analyst
- Data Migration Specialist
- Developer
- Tax Analyst
- View only

## Margin report data

Margin reports include charges based on the timestamp of the originating event, not the timestamp when a fee is assessed. For example, to view a fee assessed on February 1 for a charge created on January 31, run the report for January.

A margin report includes data for the following types of charges:

- [Connect direct charges](/connect/direct-charges)where the platform collects application fees
- [Destination charges](/connect/destination-charges)where the platform collects application fees, with or without on_behalf_of

It does not include data for the following types of charges:

- Direct charges where the connected account is responsible for fees
- Direct charges on the platform (such as SaaS subscriptions they run on the same account)
- Separate charges and transfers
- Non-Connect direct charges on a connected account

NoteA margin report normalizes all values to USD using the conversion rate at the time of activity. We plan to add other normalization currencies in a future release.

## Available margin reports

Report typeDescriptionUsageSummaryPlatform-level aggregated view of Connect volume, revenue and feesCalculate monthly margins for your platformTransactionTransaction-level view of Connect volume, revenue and feesIdentify which transactions are driving margins up or downConnected Account(coming soon)Connected account-level view of Connect volume, revenue and feesIdentify which connected accounts are driving margins up or down![Example of a summary margin report](https://b.stripecdn.com/docs-statics-srv/assets/summary-margin-report.4b348d78a47df2e2ab99328136a93cb4.png)

Summary margin report example

## Access the margin reports

1. Navigate to the[Reports hub](https://dashboard.stripe.com/reports/hub)in your Stripe Dashboard.
2. ClickConnect Margin Report.
3. Using the month picker, select thetime-periodfor which you’d like the Margin Report. The report for a month is available 7 days after the end of that month.
4. ClickDownloadon your desired Margin Report type.

## Available columns for each margin report

The Summary margin report shows aggregated monthly data, while the Transaction margin report shows data for individual transactions.

NoteThe total amounts shown in the Summary margin report are normally greater than the sum of the amounts in the Transaction margin report. That’s because the Transaction report includes only fees that apply at a transaction level. It doesn’t include out-of-band fees, such as Card Account Updater fees or non-transactional scheme fees.

### Summary margin report

This report shows the aggregated volume, revenue, and costs for the platform for the entire month.

Amount fields include:

- subtotal_amount: Amount excluding any tax
- tax_amount: Amount of tax
- total_amount: sum of`subtotal_amount`and`tax_amount`

The Summary margin report includes the following data:

TypeCategoryDescriptionVolumeCharges, Payment method ={payment method}Volume of charges for the{payment method}payment methodRefundsVolume of refundsDisputesVolume of disputesRevenueApplication fee, payment method ={payment method}Amount of application fees for the{payment method}payment methodApplication fee refundsAmount of application fees refunded by the platformNetwork fee (assessed by card networks)Card payments - Transaction network costsInterchange (or discount, for Amex) fees and transaction-level scheme fees; a single charge typically incurs one interchange fee and one or more scheme feesCard payments - Other network costsNon-transactional scheme fees, such as FANF or MLF, assessed monthlyStripe feeStripe processing fees -{payment method}Stripe processing fees for cards and other payment methodsConnect -{fee type}Connect fees, such as Account Volume Billing, Active Account Billing, and (for Stripe Managed Risk and Support) Loss LiabilityVariesOther product fees that apply to the platform, such as for Radar and Card Account Updater### Transaction margin report

This report shows a transaction-level breakdown of volume, revenue, and costs for the entire month.  It doesn’t include non-transactional fees. You can use it to understand which transactions are margin-positive, margin-neutral, or margin-negative.

Charge detail fields include:

- charge_id: Unique identifier of the charge
- connected_account_id: Unique identifier of the connected account associated with the charge
- activity_at: Time in UTC at which we attribute the line item
- payment_method_type: Type of payment method used for the transaction, such as`card`,`ACH credit transfer`, or`link`
- card_funding: Card[funding type](/api/external_account_cards/object#account_card_object-funding); can be`credit`,`debit`,`prepaid`, or`unknown`
- card_brand: Card[brand](/api#card_object-brand); can be`American Express`,`Diners Club`,`Discover`,`Eftpos Australia`,`JCB`,`MasterCard`,`UnionPay`,`Visa`, or`Unknown`
- card_network: Identifies which[network](/api/charges/object#charge_object-payment_method_details-card-network)processed the transaction; examples include`amex`,`cartes_bancaires`,`diners`,`discover`,`eftpos_au`,`interac`,`jcb`,`mastercard`,`unionpay`,`visa`,`unknown`
- card_country: Two-letter ISO code representing the country of the transaction card
- connected_account_country: Two-letter ISO code representing the country of the transaction account

The Transaction margin report includes the following data:

TypeCategoryDescriptionVolumeamountAmount of the charge, excluding any taxamount_refundedAmount of the charge that was refundedamount_disputedAmount of the charge that was disputed by the customerRevenueapplication_fee_amountAmount requested by the platform to be deducted from the charge amountapplication_fee_amount_refundedApplication fee amount that was refundedCoststripe_processing_fees_subtotal_amountFees charged by Stripe for payments processing, such as fees for using payment methods like Affirm or AfterPay; does not include card payments or network costsstripe_processing_fees_tax_amountTax on the fees charged by Stripe for payments processingstripe_dispute_fees_subtotal_amountDispute fees charged by Stripestripe_dispute_fees_tax_amountTax on the dispute fees charged by Stripestripe_refund_fees_subtotal_amountStripe processing fees that were refundedstripe_refund_fees_tax_amountTax on the Stripe processing fees that were refundednetwork_costs_subtotal_amountInterchange (or discount, for Amex) fees and transaction-level scheme fees; a single charge typically incurs one interchange fee and one or more scheme feesnetwork_costs_tax_amountTax on the transaction-level network costs charged to the platformstripe_per_auth_fee_subtotal_amountPer-authorization fees charged by Stripestripe_per_auth_fee_tax_amountTax on the per-authorization fees charged by Stripestripe_volume_fee_subtotal_amountVolume fees charged by Stripestripe_volume_fee_tax_amountTax on the volume fees charged by Stripestripe_other_cardpayments_fees_subtotal_amountOther fees charged by Stripe for card processingstripe_other_cardpayments_fees_tax_amountTax on the other fees charged by Stripe for card processingstripe_radar_fees_subtotal_amountRadar fees charged to the platformstripe_radar_fees_tax_amountTax on the Radar fees charged to the platformstripe_adaptive_acceptance_fee_subtotal_amountAdaptive acceptance fees charged to the platformstripe_adaptive_acceptance_fee_tax_amountTax on the adaptive acceptance fees charged to the platformstripe_connect_loss_liability_fee_subtotal_amountLoss liability fees charged by Stripe to manage risk on the transactionstripe_connect_loss_liability_fee_tax_amountTax on the loss liability fees charged by Stripe to manage risk on the transactionstripe_other_fees_subtotal_amountAll other fees charged on the transaction that aren’t explicitly included in another fieldstripe_other_fees_tax_amountTax charged on the other feescurrencyCurrency of the charge and feesWas this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Platform support](#platform-support)[User access](#user-access)[Margin report data](#margin-report-data)[Available margin reports](#available-margin-reports)[Access the margin reports](#access-the-margin-reports)[Available columns for each margin report](#available-columns-for-each-margin-report)Products Used[Connect](/connect)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`