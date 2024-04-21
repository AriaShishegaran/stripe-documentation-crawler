# Treasury fraud guide

Stripe Treasury is a banking-as-a-service API that enables you to embed financial services into your platform’s product. With Stripe Treasury (through our partnerships with US domestic banks), you can offer your users a simple stored-value account that can send and receive funds (through ACH wires), earn yield, spend money through a card, and more—all directly integrated into your application.

Stripe Treasury uses the same workflows as Stripe Connect to get users up and running, including various KYC and compliance requirements. You can use our API to customize how you manage fraud risk and reduce friction for your users.

[KYC](https://en.wikipedia.org/wiki/Know_your_customer)

See the following high-level guidance about how to monitor and minimize fraud when using Stripe Treasury, because you’re liable for fraud losses and disputes from your users. This guide breaks fraud down into three main categories:

- Business fraud: A person creates a fraudulent connected account (often with a stolen identity) to commit fraud

- Transaction fraud: A legitimate connected account has their card or financial account information stolen or compromised resulting in unauthorized activity

- Account takeover fraud: A legitimate connected account owner’s login is compromised by a third party and unauthorized actions are taken on their account

## Business fraud examples

The most well known types of business fraud in the financial services industry are first party fraud, third party fraud, and force capture or overcapture fraud.

First party fraud example (ACH debit)

- A bad actor uses a compromised or synthetic identity to open a financial account (Financial Institution A).

- The bad actor logs into the Financial Institution A and initiates a 10,000 USD ACH debit to pull funds from another financial account they also have ownership over (Financial Institution B). In this case, Financial Institution A is the originator of the debit (ODFI) and Financial Institution B is the receiver of the debit (RDFI).

- When the debited funds become available in Financial Institution A, the bad actor immediately spends or transfers the funds out.

- The bad actor then goes to Financial Institution B and claims the ACH debit initiated by Financial Institution A wasn’t authorized.

- Financial Institution B initiates an ACH return, citing the debit wasn’t authorized and pulls back the full amount of the debit.

- Financial Institution A is left with a negative balance.

Third party fraud example (ACH debit)

- A bad actor uses a compromised or synthetic identity to open a financial account (Financial Institution A).

- The bad actor logs into Financial Institution A and initiates a 10,000 USD ACH to pull funds from another financial account they don’t have ownership over but have account and routing number information for at Financial Institution B. In this case, Financial Institution A is the originator of the debit (ODFI) and Financial Institution B is the receiver of the debit (RDFI).

- When the debited funds become available in Financial Institution A, the bad actor immediately spends or transfers the funds out.

- The accountholder of Financial Institution B then notices the erroneous debit to their account and reports it to their financial institution that the debit initiated by Financial Institution A wasn’t authorized.

- Financial Institution B initiates an ACH return, citing that the debit wasn’t authorized and pulls back the full amount of the debit.

- Financial Institution A is left with a negative balance.

Third party fraud example (ACH or wire credit)

- A bad actor uses a compromised or synthetic identity to open a financial account (Financial Institution A).

- The bad actor uses either compromised financial account login credentials or other means to initiate an ACH or wire credit transfer from another financial account into Financial Institution A.

- When the credited funds become available in Financial Institution A, the bad actor immediately spends or transfers the funds out.

- Financial Institution A might not be in a loss position here because only the originating financial institution can recall the incoming credit transfer or wire under limited circumstances. That said, Financial Institution A has enabled fraudulent activity through their account, which has compliance and reputation implications for Stripe and our financial partners.

Force capture or overcapture fraud example

- A bad actor uses a compromised or synthetic identity to open a financial account with a card attached (Financial Institution A).

- The bad actor creates a separate account, or compromises one in good standing on another acquirer (using account takeover, or ATO).

- The bad actor uses the account to create authorizations on the card issued by Financial Institution A that don’t have issuer dispute rights—for example, card-present transactions on a chip card or card not present transactions that attempt 3D Secure (3DS) or Visa Secure.

[3D Secure (3DS)](/payments/3d-secure)

- The bad actor then force captures or overcaptures on previous authorizations.

- The bad actor then gets paid out from the business account by the acquirer.

- The bad actor then files fraud disputes on the card issued by Financial Institution A, but Financial Institution A can’t file disputes against the acquirer due to lack of dispute rights and loses the disputes.

- The financial account is left with a negative balance in the amount of the overcaptured or force captured funds.

The best way to protect yourself from fraud on Treasury, including the previous scenarios, is to make sure the customers signing up for access to the Treasury product are legitimate. It’s a good practice to assess a new customer’s risk profile holistically. Generally, the better you understand your customers and their business, the better you can assess and manage your risk exposure.

Use the following risk mitigation strategies to protect yourself at the various stages of business.

- Monitor signup volume: Unexpected upticks in signup volume can indicate that your platform is being discovered and exploited by bad actors. It’s also common to see an influx of fraud after making a marketing announcement. Pay special attention to signups in these cases.

- Limit access to faster payouts: If your customers are also using Stripe for payments, we recommend limiting which customers have access to faster payouts to their Treasury accounts. Limit faster payouts to trusted customers. You might also consider implementing criteria through which users can demonstrate good intent and “earn” faster payouts (for example, a certain number of months of activity with no issues, or a set dollar amount of processed volume).

[faster payouts](/treasury/moving-money/payouts#payouts)

- ACH debit controls: ACH debits present an elevated risk of fraud due to their pull payment method nature. Given this elevated risk, it’s important to treat the funding method with the appropriate level of fraud protections and controls, including restricting this feature to trusted users.

- Additional identity verification: Although the Treasury product includes standard Connect KYC on your connected accounts, this process focuses on identity validation (whether the information provided at signup is valid) rather than identity verification (whether the person or business providing the information at signup is who they claim to be). You can optionally use Stripe Identity, an identity verification product that programmatically confirms the identity of customers so you can greatly reduce attacks from bad actors while minimizing friction for legitimate customers.

[Stripe Identity](/identity)

- Collect industry relevant information at signup:If your customers are small businesses, consider collecting URL and relevant social media information such as Linkedin, Facebook, and Twitter.If your customers are contractors or creators, consider collecting relevant social media information such as Facebook, Twitter, TikTok, YouTube, or Instagram.If your customers are businesses in an industry that requires a license, consider collecting that license at signup.

- If your customers are small businesses, consider collecting URL and relevant social media information such as Linkedin, Facebook, and Twitter.

- If your customers are contractors or creators, consider collecting relevant social media information such as Facebook, Twitter, TikTok, YouTube, or Instagram.

- If your customers are businesses in an industry that requires a license, consider collecting that license at signup.

- Domain verification: Confirm a connected account owner’s email address if it’s linked to their business domain (for example, send an email to an address at that domain and require a response from it).

- Duplicate detection: Conduct checks for duplicate account information associated with previously fraudulent customers, such as financial account information, name with DOB, and tax information. You might also consider weak links between accounts such as multiple accounts spun up from the same IP, device, and so on.

- Holistic fraud review: Perform a manual review for fraud at a certain point in each new customer’s lifecycle. Depending on the number of customers you have, your business model, and your risk appetite, it might make sense to do this at signup, at a certain dollar amount in inflows, a certain dollar amount in outflows, or similar conditions.

- Flag anomalous activity: Flag businesses who experience anomalous behavior for manual review, this can include but isn’t limited to a business with more than a certain number of transactions where there’s no authorization (force capture) or a capture greater than the authorization amount (overcapture), a large credit transfer or wire into an account, a large international wire out of an account, card transactions outside of the country, or a return for an ACH debit into the account.

If you suspect the business might be fraudulent, set the outbound_flows feature to restricted until you’re able to review the account and make a determination. Examples of information you might want to request from your customer when performing this manual review depend on your industry but can include social media profiles, business documentation, photos of inventory, tracking numbers for shipments, business licenses, and so on.

[feature](/treasury/account-management/financial-account-features#restricted-features)

If you’re confident a business is fraudulent, set the outbound_flows and inbound_flows features to restricted. If the account has a zero balance, close the account. If the account balance isn’t zero, you can’t close the account but you can disable the listed features.

## Transaction fraud

Transaction fraud is the unauthorized use of a credit card or financial account to fraudulently obtain money or property. On Stripe, transaction fraud manifests as unauthorized charges on a Stripe issued card or unauthorized debits to a Stripe issued financial account. Cards can be compromised either through physical theft or a lost card, or through credentials compromised through phishing, spyware, non-secure checkouts, external breaches, and so on. Financial accounts can be compromised if a bad actor gains knowledge of your financial account’s account and routing numbers.

Unlike the fraud outlined above, transaction fraud occurs on good customers and can occur at any point in a customer’s lifecycle. A customer of your platform can operate on the Treasury product for months or years with no problem before having their card or financial account compromised.

Currently, Issuing has fraud protection that extends to the card attach products within Treasury, but you should still monitor for transaction fraud. The most effective ways to combat transaction fraud are to empower your customers to be diligent about keeping their card and financial account information safe and have customers pay close attention to the activity on their Treasury account. Text message or email notifications of account activity can help increase visibility. Quick identification of fraudulent transactions gives your customers the best chance of being eligible to file disputes.

[fraud protection](/issuing/manage-fraud)

For card disputes, a transaction is only eligible for a dispute if fewer than 110 days have passed since capture of the transaction. Disputes are handled through the Dashboard or the API. Read the Issuing disputes guide for more information on filing Issuing disputes.

[Issuing disputes](/issuing/purchases/disputes)

For ACH debit disputes (returns), a transaction is only eligible for a dispute if you notify Stripe of any return request at least 24 hours before the settlement date of the transaction. ACH Debit disputes are currently handled manually through email. Read more about filing ACH Debit disputes.

[filing ACH Debit disputes](/treasury/moving-money/financial-accounts/out-of/debit-reversals)

If your customer’s card or financial account number is compromised resulting in unauthorized transactions, in addition to disputing eligible transactions, consider closing and reissuing the card and opening a new connect and financial account to prevent future instances of fraud.

[new connect and financial account](/treasury/account-management/financial-accounts#close-a-financialaccount)

You can also take proactive measures to manage transaction fraud on your platform. The following examples are some controls you can put in place:

- Enroll in 3DS: 3DS is an additional layer of authentication used by businesses to make sure a purchase is from a legitimate cardholder. The additional 3DS step at checkout typically involves showing the cardholder an authentication page on their financial institution’s website that has a prompt to enter a verification code sent to their phone or email. 3DS is used for online transactions only, and works only if the business and the issuer support it. If a business has 3DS enabled, liability automatically shifts to the issuer for fraudulent disputes, regardless of whether the issuer enables 3DS. For your best chance at mitigating fraud for online transactions, enable 3DS. Read more on 3DS and how to enable it.

[3DS and how to enable it](/issuing/3d-secure)

- Spending controls: Set spending controls to block merchant categories (for example, bakeries), or to set spending limits such as 100 USD per authorization or 3,000 USD per month. You can apply them to both cards and cardholders by either setting their spending_controls fields when you create them or by updating them later. Setting spending controls is particularly effective when a card or cardholder has an expected spending pattern and it’s likely that anomalous spending is unauthorized. Read more on spending controls and how to configure them.

[spending controls and how to configure them](/issuing/controls/spending-controls)

- VAA score: Stripe has certain fraud protections on Issuing transactions, which includes automatically blocking authorizations that look suspicious using Visa’s Advanced Authorization (VAA) score in some cases. If you want us to expose this score to you through the API, contact treasury-support@stripe.com.

[treasury-support@stripe.com](mailto:treasury-support@stripe.com)

- Flag high risk transactions for cardholder review: In some situations you might want to flag card transactions that appear to be high risk to your customers and request that they confirm whether the transaction is authorized. Some ideas of what to look out for include:Transactions that are for large or rounded amountsTransactions that significantly exceed the average charge size for the cardholderTransactions at retailers where gift cards are commonly sold (grocery stores, for example)Force capturesOvercapturesTransactions on businesses based outside of the country where the cardholder resides

- Transactions that are for large or rounded amounts

- Transactions that significantly exceed the average charge size for the cardholder

- Transactions at retailers where gift cards are commonly sold (grocery stores, for example)

- Force captures

[Force captures](/issuing/purchases/transactions#handling-other-transactions)

- Overcaptures

[Overcaptures](/issuing/purchases/transactions#handling-other-transactions)

- Transactions on businesses based outside of the country where the cardholder resides

- Flag high risk transactions for accountholder review: In some situations you might want to flag ACH debit transactions that appear to be high risk to your customers and request that they confirm whether the transaction is authorized. Some types of debits to be mindful of include:Debits that are for large amounts or for an amount close to enforced limitsDebits associated with a new originating partyDebits attempted when there aren’t sufficient funds in the account to cover

- Debits that are for large amounts or for an amount close to enforced limits

- Debits associated with a new originating party

- Debits attempted when there aren’t sufficient funds in the account to cover

## Account takeover (ATO) fraud

Account takeover fraud occurs when a third party gains access to your customer’s account. Typically the attacker takes unauthorized actions on the account motivated by financial gain. The most common actions taken by the attacker on a Treasury account are wiring or transferring funds to an external financial account and issuing a new card or viewing raw PAN data of an existing card and making unauthorized transactions on the card.

Protecting against account takeovers depends on whether your platform or Stripe owns the login experience of your customers.

The following are some examples of controls that you can put in place to protect against account takeovers:

- Implement 2FA on all connected accounts.

[Implement 2FA](https://support.stripe.com/topics/2fa)

- Educate users on phishing and not sharing their 2FA codes.

- Enforce unique password policies.

- Collect device and IP address information to trace whether high risk actions (such as password updates, 2FA method updates, creating a new card, sending funds to a new external financial account) are performed from aged devices or IP addresses.

- Monitor IP activity for logins from previously unseen locations or hosting providers.

- Implement challenges for high risk user actions, for example, requiring a 2FA code to send a wire to a new account.

- Monitor connected accounts for anomalous activity. Examples include a transfer or wire that zeros out the entire treasury balance or international card spending.

If you suspect an account has been taken over, set the outbound_flows and inbound_flows features to restricted, expire existing login sessions, and disable login. After you restrict the account, work with the original account owner to verify their identity and restore access to the account. Remediation is typically executed by calling the phone number associated with the customer (pre takeover) and verifying various pieces of personally identifiable information (PII) with the customer. After you confirm the customer’s identity, you can assist them with resetting their password or 2FA device (if changed during the takeover), re-enabling login, and re-enabling treasury capabilities previously set to restricted. Financial reimbursement for any funds lost during the takeover is dependent on your internal policies.

[features](/treasury/account-management/financial-account-features#restricted-features)

## Other risk mitigation considerations

In addition to those already described, take the following risk mitigation considerations into account also.

Offering faster payouts to new businesses presents risk and you should approach it cautiously. To mitigate risk, we recommend you implement controls to turn-off faster payouts availability if you see a fraud influx.

[faster payouts](/treasury/moving-money/payouts#automatic-payouts)

Offer faster payouts availability to users only after they meet a defined trust level, for example:

- More than 60 days of processing

- Greater than 2,000 USD lifetime total volume

- Less than 3% chargeback or return rate

- Offer T+1 faster payouts to users before graduating them to T+0 faster payouts

- While limiting faster payouts availability to trusted users helps mitigate fraud at signup, this doesn’t remove the possibility of fraud on account takeovers (ATO) or good-merchant-gone-bad (GMGB) accounts. It’s important to have alerts in place to trigger on businesses who display anomalous charge patterns usually indicative of ATO or GMGB (a spike in processing volume or a shift in average transaction size, sometimes affiliated with change in bank account or login).

Originating ACH debits (through Treasury InboundTransfers) presents an elevated risk of fraud because of its pull payment method nature. This means that Treasury account holders input customer details and pull funds from the customer’s account, rather than the customer pushing funds, as is the case with many other payment methods. Because of the elevated risk profile, we suggest a number of risk mitigation efforts for originated ACH debit:

[InboundTransfers](/treasury/moving-money/financial-accounts/into/inbound-transfers)

- Make sure that the business in question has permission to debit funds from a bank account and that the account is verified. Read more about ACH Debit authorization and verification.

[ACH Debit authorization and verification](/payments/ach-debit)

- For ACH debit, funds can be returned for a number of reasons, ranging from fraud to insufficient funds. Most failures (for example, insufficient funds or an invalid account) occur within 4 business days of their post date, so it’s important to make sure that users who haven’t built trust yet aren’t paid out funds prior to this initial settlement period passing.

- Given the elevated risk profile of ACH debit, it’s important that you either restrict access to this funding method to trusted users or place strict limits and monitor use to make sure fraudsters don’t exploit the product feature. For example, new users might have their ACH debit limited to a transaction size of 2,000 USD and a weekly limit of 5,000 USD to start out. As more trust builds with users, and their legitimacy and business case is further understood, you can increase these limits alongside their business growth.

## Fraud remediation checklist

When you suspect fraud, taking the appropriate actions to minimize financial loss and further fraudulent activity is extremely important. You can think of fraud remediation as two main steps:

- Stop the immediate damage.

- Build long term solutions to mitigate future abuse. Some important steps you can take when you identify fraud include the following:Make sure all funds flows and money movement are blocked for the account in question. For example, set the outbound_flows and inbound_flows features to restricted.Determine why the account in question wasn’t identified by fraud and risk controls and make sure that additional controls are put in place. When fraudsters identify a gap in risk systems, they continue to try to exploit this gap until it’s successfully fixed.Identify any other accounts attempting similar fraudulent behavior. As mentioned previously, fraudsters will continue to exploit gaps as long as they exist, and will try to do so at scale to maximize their return. When you identify one case of fraud, it’s important to make sure that the same type of fraud isn’t occurring on other accounts, and that the fraudster doesn’t simply create a new account and repeat the same actions. Doing so allows you to potentially get ahead of lagging signals, such as disputes, and minimize the return for fraudsters to disincentivize their return.

- Make sure all funds flows and money movement are blocked for the account in question. For example, set the outbound_flows and inbound_flows features to restricted.

[features](/treasury/account-management/financial-account-features#restricted-features)

- Determine why the account in question wasn’t identified by fraud and risk controls and make sure that additional controls are put in place. When fraudsters identify a gap in risk systems, they continue to try to exploit this gap until it’s successfully fixed.

- Identify any other accounts attempting similar fraudulent behavior. As mentioned previously, fraudsters will continue to exploit gaps as long as they exist, and will try to do so at scale to maximize their return. When you identify one case of fraud, it’s important to make sure that the same type of fraud isn’t occurring on other accounts, and that the fraudster doesn’t simply create a new account and repeat the same actions. Doing so allows you to potentially get ahead of lagging signals, such as disputes, and minimize the return for fraudsters to disincentivize their return.

## Suggested metrics monitoring

The following are some metrics we recommend monitoring to help guide identification and measurement of fraud on your Treasury-enabled customers. The following metrics assume your customers are using both our Treasury and Payments products. If this isn’t the case, you can modify them accordingly.

- Rejection rate on Treasury-enabled accounts versus other accounts, over time

- Absolute acquiring losses on Treasury-enabled accounts

- Percentage of lossy accounts that are Treasury-enabled versus not

- Absolute loss per account on Treasury-enabled accounts versus not

- Time to acquiring loss on Treasury-enabled accounts versus not

- Sign up rate over time, Treasury-enabled versus not

- Transfer amount anomaly: New user with high volume of ReceivedTransfers (not including acquiring payouts) in the first 30 days

- Transfer amount anomaly: Low acquiring processing volume with high volume ReceivedTransfers (not including acquiring payouts)

- List of accounts with material ReceivedTransfers followed by OutboundTransfers bringing the treasury balance to zero

- List of accounts who have X number of dollars or more in international card spending or OutboundTransfers
