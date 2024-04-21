# Stripe Managed Risk

Stripe Managed Risk is an end-to-end merchant risk management solution for platforms that includes ongoing monitoring and mitigation for credit and fraud risk. In addition, Stripe assumes risk of loss in the event of unrecoverable negative balances on connected accounts.

When Stripe manages risk, we monitor risk signals on connected accounts, apply risk interventions on connected accounts in response to observed signals, and seek to recover negative balances from your connected accounts. You aren’t liable for unrecoverable negative balances on your connected accounts.

## Components of Stripe Managed Risk

There are three core components of the Stripe Managed Risk offering:

- Screening & detection

- Monitoring & mitigation

- Stripe Negative Balance Liability

When you onboard new connected accounts to your platform, Stripe conducts a number of upfront risk-based onboarding checks. These checks are for adherence to our compliance and regulatory standards as well as for identifying fraud and credit risk signals.

You can implement additional onboarding verifications to meet relevant regulations for products or services offered by your platform or connected accounts.

Stripe performs ongoing monitoring of risk signals (KYC, transaction data, and so on) to identify connected accounts that might pose credit or fraud risks. We use automated processes, such as machine learning models, and Stripe risk team manual reviews. Stripe automates interventions against risky businesses to reduce fraud and risk of loss. For example, Stripe’s processes might flag a risky connected account in response to a number of signals such as elevated losses, spikes in chargeback rates, or refunds. In response, Stripe might take targeted action on that account using any of a large number of interventions to reduce risk exposure. Some of Stripe’s key risk interventions include:

- Changes to capabilities: In response to risk signals, Stripe might slow or pause payouts, or pause a connected account’s ability to process charges.

- Reserves: In response to risk signals, Stripe might hold a reserve on the connected account balance. It can be a fixed amount or a percentage of transaction amounts.

- Offboarding: In the extreme case that a business poses significant risk to Stripe or your platform (ToS violations, fraud, and so on), Stripe might deactivate the connected account.

When you choose to use Stripe negative balance liability for connected accounts, Stripe assumes the risk of losses from unrecoverable negative balances on those connected accounts. In particular, Stripe doesn’t deduct unrecoverable negative connected account balances from your platform account.

Stripe Managed Risk has these requirements:

- Radar: You must use Radar on connected account transactions. (For users who pay Stripe’s listed prices for payments processing, Radar is included at no additional cost.)

- Connected account onboarding: When onboarding connected accounts, you must use either Stripe-hosted onboarding or the embedded onboarding component. Connected accounts where Stripe is liable for negative balances, including Standard accounts, can’t complete onboarding in any other way.

- Connected account dashboard: Connected accounts where Stripe is liable for negative balances must have access to a Stripe-hosted dashboard, or your platform’s interface must include both the Notifications Banner and Account Management embedded components. Some Stripe risk interventions require them to allow connected accounts to update their business information.

## The Stripe Managed Risk experience for connected accounts

You define your connected accounts’ experiences with Stripe Managed Risk by configuring their onboarding flow and their dashboard or other platform interface.

When Stripe is liable for negative balances, you can onboard connected accounts using Stripe-hosted onboarding or the embedded onboarding component. With either option, Stripe collects the required information for risk management and prompts the connected account to accept Stripe’s terms of service. You can pre-fill any information that you have previously collected in your onboarding flow via the Accounts API.

[embedded onboarding component](/connect/supported-embedded-components/account-onboarding)

Most connected accounts are likely to have few, if any, interactions with Stripe’s risk management. However, in the event that Stripe requires additional risk-related information from one of your connected accounts, Stripe notifies your connected account and provides a pathway for them to respond to and resolve the intervention.

To resolve an intervention, a connected account owner might provide additional KYC information, complete a form, or provide other documentation. Stripe reviews their response to assess whether to lift, revise, or continue the intervention.

## Fees for Stripe Managed Risk

The fees for Stripe Managed Risk depend on the economic model:

- Revenue share: For connected accounts where the platform uses a revenue share economic model for payments processing, including Standard accounts, Stripe Managed Risk is included at no additional cost.

- Buy rate: For connected accounts where the platform uses a buy-rate economic model, including Express and Custom accounts, Stripe Managed Risk fees depend on the pricing arrangements:Listed pricing: For platforms that pay listed pricing for payments processing and Connect fees, Stripe Managed Risk is included at no additional cost.Negotiated pricing: For platforms with negotiated pricing for either payments processing or Connect fees, Stripe Managed Risk involves additional fees. For more information, contact Stripe Sales.

- Listed pricing: For platforms that pay listed pricing for payments processing and Connect fees, Stripe Managed Risk is included at no additional cost.

- Negotiated pricing: For platforms with negotiated pricing for either payments processing or Connect fees, Stripe Managed Risk involves additional fees. For more information, contact Stripe Sales.
