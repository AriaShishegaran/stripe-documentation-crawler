# High risk merchant lists

Card networks, such as Visa and Mastercard, operate databases known as Terminated Merchant Files (TMFs) that contain information about accounts that have been closed by credit card processors around the world for high chargebacks or violations of card brand rules.

All payment processors must check these databases when accepting a new user, and must also add merchants to the database if they close the account and it meets TMF criteria.

Being placed on a TMF can have serious effects. While they’re only supposed to be informational tools during the account application process, many entities refuse to accept businesses or individuals listed on a TMF. For this reason, it’s important to be aware of TMF criteria and make sure you avoid becoming eligible.

The most common list—and the only one with global reach—is Mastercard’s MATCH, or the Mastercard Alert to Control High-Risk Merchants. In the following sections, we describe how MATCH qualification works and what happens to MATCH entries.

## Criteria for MATCH Qualification

When a relationship ends between a business and a credit card processor, the processor must determine whether the business meets criteria to be placed on MATCH.

If any MATCH criteria are satisfied, the processor must add information about the business to MATCH within one business day of termination or within one business day of the account becoming eligible for MATCH after termination.

The majority of MATCH criteria, or “reason codes,” involve breaches of card network rules, including illegal activity and collusion. These 11 reason codes, and the exact Mastercard definition, are listed below.

The Identity Theft reason code should be used when a fraudulent account is opened with stolen information, and the listing of this information on MATCH should not hamper the legitimate identity holder from opening a processing account. It instead serves as a warning to the credit card processor that the application may contain stolen identity information.

Two MATCH reason codes have specific numeric thresholds defined by Mastercard for when processors must add accounts to MATCH.

These reason codes, which involve chargeback and fraud activity on an account, are the most common reasons for being added to MATCH, and can affect businesses that are not engaged in illegal or rule-violating activity. These reason codes are as follows:

## Additional information on excessive chargebacks and fraud

These MATCH reason codes are separate from card brand chargeback and fraud monitoring programs operated by Visa and Mastercard. However, as defined, the excessive chargebacks criteria only applies to activity on Mastercard cards, even though MATCH is required by all major card networks. If dispute activity does not take place on a Mastercard card, it would not qualify toward MATCH counts. Other card networks may ask for businesses to be listed on MATCH if those businesses hit the “excessive” stages of their card brand monitoring programs or are fined as part of those programs.

A month is defined as a calendar month. For example, if a processor were evaluating MATCH eligibility from the month of January, they would look at the number of transactions in January and the number of chargebacks in January—not the number of chargebacks from transactions made in January.

Once a business meets the excessive chargebacks or fraud MATCH criteria in a calendar month, the merchant must be added to MATCH if the processing relationship is terminated, even if the processing relationship is not ended in that calendar month. For example, if a business only meets MATCH criteria in February, and the processing relationship is not ended until September, the processor is still required to add information to MATCH even though the qualifying activity took place in February. Additionally, even if a business does not meet MATCH criteria when the relationship is initially terminated, it can still qualify for MATCH if the criteria are met afterward—for example, if chargebacks are initiated after termination.

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

[contact Stripe support](https://support.stripe.com/contact)
