# Country-specific considerations for cross-border payouts

Connected accounts in certain countries might have additional bank or fund flow restrictions when using cross-border payouts.

## Bank restrictions

Most banks can accept payments from other countries without any special requirements. Some banks in certain countries require more information regarding recipient identity or transaction information for risk and compliance purposes. The receiving bank often has discretion over what they require for cross-border transactions, which can differ between banks, even within the same country.

If a seller or service provider onboards as a connected account to your platform in one of these countries, we send an email to alert your user of the possibility for additional requirements. If the receiving bank requires additional information, they should reach out to your user directly with their requirements.

Banks might have special requirements in certain countries, so your user might pay additional fees for the payout. Stripe might also set a higher minimum payout threshold to account for possible fees charged by certain banks.

[minimum payout](/payouts#cbp-minimum-payout-amounts)

The list of possible requirements for the following countries isn’t exhaustive, as Stripe isn’t involved with creating these conditions. If you encounter additional requirements that aren’t listed, please notify Stripe support.

[Stripe support](https://support.stripe.com/)

Possible special requirements include:

- Submitting a remittance form.

- Providing a receipt or invoice as proof that the recipient is legitimately receiving the payment.

- Paying additional fees.

- Visiting a bank location to submit a copy of their ID and additional paperwork, if they haven’t previously done so. Banks require a national ID card number (MyNumber) to be submitted and on file before they can receive or send international transfers.

- Providing a receipt or invoice as proof that the recipient is legitimately receiving the payment.

- Paying additional fees.

- Supporting payouts only to banks participating in the Foreign Exchange Yen Clearing System (FXYCS).

- Providing additional information on the purpose of the payment.

- Providing a receipt or invoice as proof that the recipient is legitimately receiving the payment.

- Submitting a remittance form.

## Fund flow restrictions

The following fund flows are generally supported in countries for cross-border payouts:

- Separate charges and transfers without the on_behalf_of parameter

[Separate charges and transfers](/connect/separate-charges-and-transfers)

- Top-up and transfers

- Destination charges

[Destination charges](/connect/destination-charges)

Direct charges and destination charges with the on_behalf_of parameter aren’t supported. However, some countries have additional limitations.

For Brazil, India, and Thailand, only the following fund flows are supported:

[India](https://support.stripe.com/questions/stripe-india-support-for-marketplaces)

[Thailand](https://support.stripe.com/questions/stripe-thailand-support-for-marketplaces)

- Separate charges and transfers without the on_behalf_of parameter

[Separate charges and transfers](/connect/separate-charges-and-transfers)

- Top-up and transfers
