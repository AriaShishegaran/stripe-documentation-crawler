htmlHigh risk merchant lists | Stripe Documentation[Skip to content](#main-content)High risk merchant lists[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdisputes%2Fmatch)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fdisputes%2Fmatch)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)
[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Radar](/radar)·[Home](/docs)[Get started](/docs/get-started)[Protect against fraud](/docs/radar)[Disputes and fraud](/docs/disputes)# High risk merchant lists

Learn the criteria for inclusion in Mastercard's Alert to Control High-Risk Merchants (MATCH) list.Card networks, such as Visa and Mastercard, operate databases known as Terminated Merchant Files (TMFs) that contain information about accounts that have been closed by credit card processors around the world for high chargebacks or violations of card brand rules.

All payment processors must check these databases when accepting a new user, and must also add merchants to the database if they close the account and it meets TMF criteria.

Being placed on a TMF can have serious effects. While they’re only supposed to be informational tools during the account application process, many entities refuse to accept businesses or individuals listed on a TMF. For this reason, it’s important to be aware of TMF criteria and make sure you avoid becoming eligible.

The most common list—and the only one with global reach—is Mastercard’s MATCH, or the Mastercard Alert to Control High-Risk Merchants. In the following sections, we describe how MATCH qualification works and what happens to MATCH entries.

## Criteria for MATCH Qualification

When a relationship ends between a business and a credit card processor, the processor must determine whether the business meets criteria to be placed on MATCH.

If any MATCH criteria are satisfied, the processor must add information about the business to MATCH within one business day of termination or within one business day of the account becoming eligible for MATCH after termination.

### Qualitative criteria

The majority of MATCH criteria, or “reason codes,” involve breaches of card network rules, including illegal activity and collusion. These 11 reason codes, and the exact Mastercard definition, are listed below.

The Identity Theft reason code should be used when a fraudulent account is opened with stolen information, and the listing of this information on MATCH should not hamper the legitimate identity holder from opening a processing account. It instead serves as a warning to the credit card processor that the application may contain stolen identity information.

CodeReasonDescription#1Account Data CompromiseAn occurrence that results, directly or indirectly, in the unauthorized access to or disclosure of Account data.#2Common Point of PurchaseAccount data is stolen at the Merchant and then used for fraudulent purchases at other Merchant locations.#3LaunderingThe Merchant was engaged in laundering activity. Laundering means that a Merchant presented to its Acquirer Transaction records that were not valid Transactions for sales of goods or services between that Merchant and a bona fide Cardholder.#7Fraud ConvictionThere was a criminal fraud conviction of a principal owner or partner of the Merchant.#8Mastercard Questionable Merchant Audit ProgramThe Merchant was determined to be a Questionable Merchant as per the criteria set forth in the Mastercard Questionable Merchant Audit Program.#9Bankruptcy/Liquidation/InsolvencyThe Merchant was unable or is likely to become unable to discharge its financial obligations.#10Violation of StandardsWith respect to a Merchant reported by a Mastercard Acquirer, the Merchant was in violation of one or more Standards that describe procedures to be employed by the Merchant in Transactions in which Cards are used, including, by way of example and not limitation, the Standards for honoring all Cards, displaying the Marks, charges to Cardholders, minimum/ maximum Transaction amount restrictions, and prohibited Transactions set forth in Chapter 5 of the Mastercard Rules manual.#11Merchant CollusionThe Merchant participated in fraudulent collusive activity.#12PCIDSS Non-ComplianceThe Merchant failed to comply with Payment Card Industry (PCI) Data Security Standard (DSS) requirements.#13Illegal TransactionsThe Merchant was engaged in illegal Transactions.#14Identity TheftThe Acquirer has reason to believe that the identity of the listed Merchant or its principal owner(s) was unlawfully assumed for the purpose of unlawfully entering into a Merchant Agreement.### Quantitative criteria

Two MATCH reason codes have specific numeric thresholds defined by Mastercard for when processors must add accounts to MATCH.

These reason codes, which involve chargeback and fraud activity on an account, are the most common reasons for being added to MATCH, and can affect businesses that are not engaged in illegal or rule-violating activity. These reason codes are as follows:

CodeReasonDescription#4Excessive ChargebacksWith respect to a Merchant reported by a Mastercard Acquirer, the number of Mastercard chargebacks in any single month exceeded 1% of the number of Mastercard sales Transactions in that month, and those chargebacks totaled USD 5,000 or more.#5Excessive FraudThe Merchant effected fraudulent Transactions of any type (counterfeit or otherwise) meeting or exceeding the following minimum reporting Standard: the Merchant’s fraud-to-sales dollar volume ratio was 8% or greater in a calendar month, and the Merchant effected 10 or more fraudulent Transactions totaling USD 5,000 or more in that calendar month.## Additional information on excessive chargebacks and fraud

These MATCH reason codes are separate from card brand chargeback and fraud monitoring programs operated by Visa and Mastercard. However, as defined, the excessive chargebacks criteria only applies to activity on Mastercard cards, even though MATCH is required by all major card networks. If dispute activity does not take place on a Mastercard card, it would not qualify toward MATCH counts. Other card networks may ask for businesses to be listed on MATCH if those businesses hit the “excessive” stages of their card brand monitoring programs or are fined as part of those programs.

A month is defined as a calendar month. For example, if a processor were evaluating MATCH eligibility from the month of January, they would look at the number of transactions in January and the number of chargebacks in January—not the number of chargebacks from transactions made in January.

Once a business meets the excessive chargebacks or fraud MATCH criteria in a calendar month, the merchant must be added to MATCH if the processing relationship is terminated, even if the processing relationship is not ended in that calendar month. For example, if a business only meets MATCH criteria in February, and the processing relationship is not ended until September, the processor is still required to add information to MATCH even though the qualifying activity took place in February. Additionally, even if a business does not meet MATCH criteria when the relationship is initially terminated, it can still qualify for MATCH if the criteria are met afterward—for example, if chargebacks are initiated after termination.

### Example qualification data

Take the following sample data from a calendar month:

- Number of Mastercard transactions: 125
- Number of Mastercard chargebacks: 6
- Ratio of chargebacks to transactions: (6/125) = 4.8%
- Volume of Mastercard chargebacks: $6250

In this case, the business would qualify for MATCH for excessive chargebacks if the processing relationship later terminates. It does not matter if chargebacks are later reversed or won by the merchant.

There is no minimum number of chargebacks for MATCH qualification for excessive chargebacks.

## Information added to MATCH

The card networks require that the following information be added to MATCH if available:

- Business Legal Name and DBA
- Business Address
- Business Phone Number
- Business Tax ID
- Business URL
- Principal Owner Name
- Principal Owner Address
- Principal Owner Phone Number
- Principal Owner Tax ID
- Account Opening Date and Termination Date
- MATCH Reason Code

Mastercard does not assess the accuracy of MATCH listings.

## Removal from MATCH

Unfortunately, Stripe—or any other processor—usually cannot remove an account’s information from MATCH upon request. A processor can only remove a MATCH entry if:

- The processor added the business to MATCH in error.
- The listing is for MATCH reason code 12 (Payment Card Industry Data Security Standard Noncompliance) and the processor has confirmed that the business has become compliant with the Payment Card Industry Data Security Standard.

If you believe either of those two situations exist, you’ll need to reach out to the processor that listed your information on MATCH to be removed. Records remain on the MATCH system for five years before being automatically purged by Mastercard.

## Next steps if you are listed on MATCH

If you’re listed on MATCH, you’re likely to find out when you attempt to sign up for a new processor. MATCH is only supposed to be used as an informational tool by processors during the application process; however, the presence of a MATCH listing often means that an application is declined.

You’ll need to reach out to your previous processor to find out why your information was added to MATCH. Note, however, that MATCH criteria are determined by Mastercard and processors are required to follow this criteria. Stripe cannot remove a merchant that met the “excessive chargebacks” criteria even if the business has remediated the issues leading to chargebacks, for example.

Due to banking partner restrictions, Stripe generally cannot process for businesses listed on MATCH unless extenuating circumstances apply, such as the case of a legitimate merchant who previously had their identity information stolen.

If you require assistance with a dispute, contact Stripe support.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Criteria for MATCH Qualification](#criteria-for-match-qualification)[Additional information on excessive chargebacks and fraud](#additional-information-on-excessive-chargebacks-and-fraud)[Information added to MATCH](#information-added-to-match)[Removal from MATCH](#removal-from-match)[Next steps if you are listed on MATCH](#next-steps-if-you-are-listed-on-match)Products Used[Radar](/radar)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`