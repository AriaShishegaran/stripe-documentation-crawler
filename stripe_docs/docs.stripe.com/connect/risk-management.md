# Risk management with Connect

All business owners assume a certain amount of risk when accepting payments for goods and services. This guide defines the risks to consider as a Connect platform owner and the approaches you can take to mitigate those risks.

## Components of payments risk

Any approach to risk management involves many potential sources of payments risk, which can be split into two general categories:

- Transaction risk: The risk that a customer might charge back a transaction, such as disputes or fraud identified from card testing. With direct charges, transaction risk primarily affects connected accounts; with destination charges and separate charges and transfers, transaction risk primarily affects platforms.

[disputes](/disputes)

[direct charges](/connect/direct-charges)

[destination charges](/connect/destination-charges)

[separate charges and transfers](/connect/separate-charges-and-transfers)

- Merchant risk: The risk that a connected account is unable or unwilling to cover the costs of chargebacks on its transactions, leading to unrecoverable negative balances. Merchant risk primarily affects platforms.

There are two main types of merchant risk: credit risk and fraud risk. Both can result in chargebacks and unrecoverable negative balances.

- No intent to deliver: A fraudulent online storefront charged customers for goods that they didn’t intend to deliver. The connected account then paid out the money to their external bank account. When the customers realized that their orders were never going to arrive, they submitted chargebacks, which were covered by the platform.

- Payment method cashing: A fraudster stole a customer’s credit card number, opened a connected account, and made purchases through that account using the stolen payment method credentials. When the customer discovered the fraudulent charges, they submitted chargebacks, which were covered by the platform.

## Connect merchant risk options

Each connected account’s Account object has a controller.losses.payments property that determines who’s responsible for covering any negative payments balance on that account.

[controller.losses.payments](/api/accounts/object#account_object-controller-losses-payments)

[responsible for covering any negative payments balance](/connect/risk-management)

The controller.losses.payments property applies only to the connected account’s payments balance. It doesn’t affect responsibility for covering negative Issuing or Treasury balances.

You can select whether you or Stripe is responsible for negative balance liabilities on your accounts. Because your choice of negative balance liability can significantly impact your platform and connected accounts, consider it carefully before onboarding any accounts. This table describes some important elements of the decision:

[API value](/api/accounts/object#account_object-controller-losses-payments)

We recommend that new platforms have Stripe take responsibility for negative balances on connected accounts. Only consider taking responsibility as the platform if you’re highly confident in your ability to manage merchant risk.

## Stripe solutions for risk management

Stripe provides a variety of solutions to help manage both transaction and merchant risk. These solutions fall into two categories:

- Tools to manage risk: Tools that Stripe provides to help platforms manage risks without Stripe being liable for any resulting losses.

- Full service risk management: Risk-management services that Stripe provides where Stripe covers the costs of any resulting losses.

This table describes the main solution that Stripe provides in each category for each type of risk:

[Radar](/radar)

[Chargeback protection](https://stripe.com/radar/chargeback-protection)

[Stripe Managed Risk](/connect/risk-management/managed-risk)

## Know Your Customer (KYC) and compliance

In addition to operational risk management solutions, Stripe provides KYC and risk-based screening to help onboard connected accounts and maintain compliance with evolving regulations. Stripe screens include the following:

- Identity verifications

- Risk-based KYC and AML checks for individuals and businesses

- Sanctions screening

- MATCH (Member Alert To Control High-risk businesses) list checks

- Secure credit card data tokenization for PCI compliance

- Money transmitter licenses (MTL) in the US and e-money (EMI) licenses in the EU

- Prohibited business checks

[Prohibited business checks](https://stripe.com/legal/restricted-businesses)
