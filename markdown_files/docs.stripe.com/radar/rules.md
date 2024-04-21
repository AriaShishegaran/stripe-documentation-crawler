htmlRules | Stripe Documentation[Skip to content](#main-content)Rules[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fradar%2Frules)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fradar%2Frules)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)
[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Radar](/radar)·[Home](/docs)[Get started](/docs/get-started)[Protect against fraud](/docs/radar)# Rules

Use fraud prevention rules to guard your business.Fraud prevention rules allow you to take action whenever a payment matches certain criteria.

Stripe Radar provides built-in rules to help detect and guard against fraud risk for all Stripe users.

Radar for Fraud Teams users can use the Dashboard to create custom rules based on the unique business logic specific to your business. For example, you can:

- Request 3D Securefor all payments that support it and are made by a new customer
- Allowall payments from your call center’s IP address
- Blockpayments made from a location or card issued outside your country
- Reviewall payments greater than 1,000 USD that have been made with a prepaid card

CautionEU merchants might be affected by the Geo-blocking Regulation and its prohibitions on blocking payments from customers based in EU member states.

## Built-in rules

The following rules are enabled by default for all Radar users.

### Machine learning risk checks

Stripe Radar and Stripe Radar for Fraud Teams provide a set of default rules based on the judgments of our machine learning models, which are:

Block if :risk_level: = 'highest'

The rule blocks and won’t process payments with a high risk of fraud. This rule is enabled by default for users of Radar or Radar for Fraud Teams.

Review if :risk_level: = 'elevated'

The default behavior for Stripe Radar for Fraud Teams is to place payments into review that we suspect have an elevated risk of fraud.

### Traditional card checks

A payment can still be successful even if the CVC or address (AVS) check fails, because card issuers take many signals into account when making a decision about whether to approve or decline a payment. In some cases, a card issuer might still approve a payment they consider legitimate, even if the CVC or postal code verification check fails.

Stripe has built-in rules so you can block payments even if they’ve been approved by the card issuer. These rules can be enabled or disabled using the Stripe Dashboard.

These rules also apply to the card validation process that occurs when attaching a card to a customer. In cases where you create the card and customer together, CVC or postal code validation failure prevents the successful creation of the customer record. This rule might not be enabled for your account by default. You can enable or disable it any time using the Stripe Dashboard.

Block if CVC verification fails

Stripe blocks payments that fail a card issuer’s CVC verification check. If the customer doesn’t provide the CVC number, for example because they use a wallet, or their card issuer doesn’t support its verification, the rule can’t block the payment.

Block if postal code verification fails

Stripe blocks payments when they fail a card issuer’s postal code verification check. If the customer doesn’t provide the postal code, or their card issuer doesn’t support its verification, the rule can’t block the payment. This rule might not be enabled for your account by default. You can enable or disable it any time using the Stripe Dashboard.

### Built-in rules to request 3D Secure

### Can I use 3DS rules with Stripe Checkout or Stripe Billing?

Because Stripe Checkout and Stripe Billing use PaymentIntents internally, the information in this section also applies to payments created through these products.

Learn how to use 3DS with Stripe Billing.

Using 3D Secure prompts customers to complete an additional authentication step before they can complete the purchase flow. If 3D Secure authenticates a payment, the liability for any fraud-related disputes for that payment typically shift from the seller to the issuer. This means that in most cases, the seller isn’t responsible for fraud costs on 3D Secure authenticated payments.

Stripe automatically handles soft decline codes indicating that 3DS is required by issuers. We also trigger 3DS when necessary, adhering to regulations like the Strong Customer Authentication (SCA) mandated by the PSD2. Disabling Radar doesn’t prevent 3D Secure from being triggered in cases where it’s necessary.

Stripe provides three default disabled rules you can enable to dynamically request 3DS when using Radar with Payment Intents or Setup Intents:

1. `Request 3D Secure if 3D Secure is required for card`  - Disabled by default. Enabling this rule prompts the customer for 3D Secure authentication if historically the card[required 3D Secure](/payments/3d-secure/authentication-flow#three-ds-cards).
  - Stripe automatically handles soft decline codes indicating that 3DS is required by issuers. Furthermore, we also trigger 3DS when necessary, adhering to regulations like the[Strong Customer Authentication](https://stripe.com/guides/strong-customer-authentication)mandated by the PSD2.


2. `Request 3D Secure if 3D Secure is supported for card`  - Disabled by default but similar to the previous rule. Enabling this rule prompts the customer for 3D Secure authentication as long as their card supports it.
  - Use this rule instead of the previous one if you want to maximize the number of payments that have liability shift. Be aware that this additional requirement may decrease conversion rates.


3. `Request 3D Secure if 3D Secure is recommended for card`  - Disabled by default. Enabling this rule prompts the customer for 3D Secure authentication when Stripe believes that 3D Secure authentication can take place with minimal impact on conversion rates.
  - Enable this if you want to maximize the number of payments that have liability shift.



Because 3D Secure requires your customer to go through an additional layer of authentication, indiscriminate use of 3D Secure might lower conversion rates. Stripe recommends that you enable default Request 3D Secure rules only if you need to send all payments from supported cards through 3D Secure.

Requesting 3D Secure does not necessarily mean the issuer actually performs 3D Secure. For more details about possible outcomes, refer to the 3D Secure documentation.

Custom rules to request 3D Secureand act on specific outcomes![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

After attempting 3D Secure authentication, if you have Radar for Fraud Teams, you can evaluate the result in allow, block, or review rules.

The most important attributes for custom Radar rules are:

- `is_3d_secure`which is true if the card is supported, 3D Secure was attempted by the issuer and the user did not fail authentication. We generally recommend using this in block rules.
- `is_3d_secure_authenticated`which is true if 3D Secure was attempted by the issuer and the user successfully went through a full authentication. Using this attribute in a block rule excludes legitimate transactions that might have an SCA exemption or don’t fall into a clear failure or successful authentication such as processing errors.
- `has_liability_shift`which is true if Stripe expects the payment to be covered under theliability shiftrule. This might[not always be the same as 3D Secure](/payments/3d-secure/authentication-flow#disputed-payments), for example Apple Pay in certain regions.

For custom rules, we recommend keeping Request 3D Secure and Block rules aligned depending on your risk appetite. However, don’t block transactions where 3D Secure isn’t supported, such as some wallets.

Here are some examples that show how to achieve this for different use cases:

Request 3D Secure based on Radar risk level![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You want to use Radar to request 3D Secure on all charges based on Radar risk level and above a certain amount.

Radar ruleDescription`Request 3D Secure if :risk_level: != 'normal' and :amount_in_usd: > 25`This rule checks for Radar’s risk level then requests 3D Secure on all charges with an elevated or high risk level above a certain amount.In this case, without a block rule, cards or wallets that don’t support 3D Secure isn’t blocked. 3D Secure attempts with failed authentication don’t continue to charge authorization.

Always require 3D Secure based on Radar risk level![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You want to use Radar to request 3D Secure on all charges based on elevated or high risk Radar risk level and above a certain amount. If cards don’t support 3D Secure, you don’t want to accept them.

Radar ruleDescription`Request 3D Secure if :risk_level: != 'normal' and :amount_in_usd: > 25`This rule checks for Radar’s risk level then requests 3D Secure on all charges with an elevated or high risk level above a certain amount.`Block if not :is_3d_secure:  and :risk_level: != 'normal' and :amount_in_usd: > 25 and  not :is_off_session:  and  :digital_wallet: != 'apple_pay'  and  not (:digital_wallet: = 'android_pay'  and  :has_cryptogram:)`This rule blocks payments without a 3D Secure flow for charges with an elevated or high risk level above a certain amount. However, it accepts legitimate transactions that might have an SCA exemption or don’t have a clear failure or successful authentication such as`attempt_acknowledged`. It accepts off-session payments such as recurring subscription charges and wallets such as Apple Pay or Google Pay to succeed.Only accept fully 3D Secure authenticated transactions if 3D Secure is supported![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You rely on Stripe triggering 3D Secure when necessary in cases such as Strong Customer Authentication (SCA), but don’t want to accept edge cases such as processing errors.

Radar ruleDescription`Block if :is_3d_secure: and not :is_3d_secure_authenticated:`This rule blocks payments where the card is enrolled in 3D Secure and 3D Secure was attempted but the user didn’t successfully authenticate. Cards that don’t support 3D Secure, SCA exemptions, off-session payments such as recurring subscription charges, and wallets such as Apple Pay or Google Pay are accepted.Request 3D Secure based on Metadata![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You want to use Radar to request 3D Secure on all charges with a custom metadata attribute.

Radar ruleDescription`Request 3D Secure if ::foo:: = 'bar'`This rule checks for a metadata condition and then requests 3D Secure. To check Customer metadata, replace`::foo:: = 'bar'`with a value like`::customer:trusted:: = 'false'`.In this case, without a block rule, cards or wallets that don’t support 3D Secure aren’t blocked. 3D Secure attempts with failed authentication don’t continue to charge authorization.

Always require 3D Secure based on Metadata![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You want to use Radar to request 3D Secure on all charges with a custom metadata attribute and block cards that don’t support it.

Radar ruleDescription`Request 3D Secure if ::foo:: = 'bar'`This rule checks for a metadata condition and then requests 3D Secure. To check Customer metadata, replace`::foo:: = 'bar'`with a value like`::customer:trusted:: = 'false'`.`Block if ::foo:: = 'bar' and not :is_3d_secure and not :is_off_session: and :digital_wallet: != 'apple_pay' and not(:digital_wallet: = 'android_pay' and :has_cryptogram:)`This rule blocks payments without a 3D Secure flow for charges with a custom metadata attribute. However, it accepts legitimate transactions that might have an SCA exemption or don’t have a clear failure or successful authentication such as`attempt_acknowledged`. It accepts off-session payments such as recurring subscription charges and wallets such as Apple Pay or Google Pay to succeed.Request 3D Secure for all new cards and review if 3D Secure was not supported![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You want to use Radar to request 3D Secure on all new cards and manually review charges from cards that don’t support 3D Secure.

Radar ruleDescription`Request 3D Secure if is_missing(:seconds_since_card_first_seen:)`This rule requests 3D Secure on all cards that haven’t been used on your account. To reduce user friction, you can add an additional condition to only request 3D secure if`:risk_level: != 'normal'`.`Request 3D Secure if :is_new_card_on_customer:`As an alternative to the rule above, this rule requests 3D Secure on all cards that are newly used on a[Customer](/api/customers). To reduce user friction, you can add an additional condition to only request 3D secure if`:risk_level: != 'normal'`.`Review if not :is_3d_secure and not:is_off_session: and :digital_wallet: != 'apple_pay' and not(:digital_wallet: = 'android_pay' and :has_cryptogram:)`This rule marks payments where 3D Secure is expected but isn’t supported for manual review. It ignores off-session payments such as recurring subscription charges and wallets such as Apple Pay or Google Pay. Payments marked for review continue to authorization and can give additional signals, such as issuer CVC checks.In this case, without a block rule, cards or wallets that don’t support 3D Secure aren’t blocked. 3D Secure attempts with failed authentication don’t continue to charge authorization.

Always require 3D Secure for certain issuer countries![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You want to use Radar to request 3D Secure on all charges from card issuers originating from countries on a custom list and block cards that don’t support it.

Radar ruleDescription`Request 3D Secure if :card_country: in @enforce_3ds_list`This rule checks for a condition based on card issuers originating from countries and compares them to a[custom list](/radar/lists), if they match it requests 3D Secure.`Block if :card_country: in @enforce_3ds_list and not :is_3d_secure and not :is_off_session: and :digital_wallet: != 'apple_pay' and not(:digital_wallet: = 'android_pay' and :has_cryptogram:)`This rule blocks payments without a 3D Secure flow for charges originating from countries on the custom list. However, it accepts legitimate transactions that might have an SCA exemption or don’t have a clear failure or successful authentication such as`attempt_acknowledged`. It accepts off-session payments such as recurring subscription charges and wallets such as Apple Pay or Google Pay to succeed.Always require 3D Secure based on Radar risk level and review edge cases![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You want to use Radar to request 3D Secure on all charges based on Radar risk level and block cards that don’t support 3D Secure, but manually review edge cases.

Radar ruleDescription`Request 3D Secure if :risk_level: != 'normal'`This rule checks for Radar’s risk level then requests 3D Secure on all charges with an elevated or high risk level above a certain amount.`Block if not :is_3d_secure:  and :risk_level: != 'normal' and  not :is_off_session:  and  :digital_wallet: != 'apple_pay'  and  not (:digital_wallet: = 'android_pay'  and  :has_cryptogram:)`This rule blocks payments without a 3D Secure flow for charges with an elevated or high risk level above a certain amount. However, it accepts legitimate transactions that might have an SCA exemption. It accepts off-session payments such as recurring subscription charges and wallets such as Apple Pay or Google Pay to succeed.`Review if not :is_3d_secure_authenticated:  and :risk_level: != 'normal' and  not :is_off_session:  and  :digital_wallet: != 'apple_pay'  and  not (:digital_wallet: = 'android_pay'  and  :has_cryptogram:)`This rule marks payments for manual review that were using 3D Secure, but did not result in a fully authenticated flow. This would review[edge cases](/api/charges/object#charge_object-payment_method_details-card-three_d_secure-result)such as`attempt_acknowledged`and would also mark legitimate payments despite SCA exemptions. Because review rules are evaluated after block rules, cards that don’t support 3D Secure are blocked.## When to create rules

### Team members creating rules

Only the account owner, administrators, and developers can create rules. If you need team members to create rules, check your team settings to make sure they have administrative access.

Stripe’s default rules can block a substantial number of fraudulent payments. Businesses that need more control over which payments they want to review, allow, or block can write custom rules through Radar for Fraud Teams.

Consider the following questions when deciding whether to enable custom rules:

- Do you see certain features or user behaviors as more risky (for example, use of a disposable email)?
- Do you want to implement rules based on payment amounts or perceived risk level (for example, automatically review if the payment is over 500 USD, automatically allow if the payment is under 5 USD)?
- Do your existing disputed and refunded payments share any common patterns (for example, similar amounts, card types, or countries)?
- Do you have existing rules you want to migrate to Stripe? Many of these rules might already be covered by Stripe’s machine learning models, and it’s worth seeing how our system performs for your business before customizing it.

### How to create effective rules

While rules can help you automate your existing workflows, they can also negatively affect your business if used incorrectly. For example, a rule can automatically allow a large number of payments that are fraudulent or block a large number of legitimate payments if it’s not set up properly.

Some helpful tips to keep in mind while setting up rules include:

- Rules only apply to future payments and don’t apply to any that have already been processed.
- Request 3D Secure rules only apply when using[Stripe Checkout](/payments/checkout),[Payment Intents](/payments/accept-a-payment), or[Setup Intents](/payments/save-and-reuse), and are evaluated before review, block, and allow rules.
- Before implementing any block rule to block all payments that meet its criteria, consider whether you’d rather review such payments first.
- Implement allow rules minimally, because they override Stripe’s default rules along with any other custom rules that match the same criteria.
- You can create a maximum of 200 rules across all rule types per account.

## Construct rules

You can add and manage rules from the Rules tab of the Radar page in the Dashboard.

To add a new rule:

1. Click+ Add rule.
2. Choose the type rule type from the sub-menu.
3. In the rule editor, construct a rule using the syntax`{action} if {attribute} {operator} {value}`where:  - {action}: How Radar responds when the rule criteria is met. This value is pre-populated based on the rule type selection you chose.
  - {attribute}: The element of the transaction to evaluate, such as the amount or card type. Begin typing with`:`to open a list of valid attributes. You can also evaluate your custom metadata by enclosing it in double colons, for example,`::product_sku::`.
  - {operator}: How to compare the attribute to the value, such as`=`,`>`,`!=`, and so on.
  - {value}: The value of the attribute to evaluate.


4. ClickTest rule.
5. Correct any detected validation errors, if necessary.
6. On theReview new rulepage, review how this rule performs against your recent transactions to confirm whether you want to enable it.
7. ClickAdd ruleto begin applying this rule to all future transactions.

### Use Radar Assistant

### Share your feedback

Help us continue to improve Radar Assistant. Click Share feedback and tell us how the Assistant performed for you and what we can do to improve. We welcome all opinions, whether it’s about the accuracy of the suggestion, the UI, or any other aspect of your interaction.

Stripe’s rule editor has a built-in LLM assistant that constructs a Radar rule from a natural language prompt.

To use Radar Assistant:

1. From the[Rules tab of the Radar page](https://dashboard.stripe.com/test/radar/rules)in the Dashboard, click+ Add rule.
2. Choose the type rule type from the sub-menu.
3. In the rule editor, clickRadar Assistant.

![Manual rule writing](https://b.stripecdn.com/docs-statics-srv/assets/manual-rule-writing-view.598ac04a039b6222f5f7b46e14a74204.png)

Manual rule writing

![Radar assistant](https://b.stripecdn.com/docs-statics-srv/assets/radar-assistant-view.4b7580fb9a503ae6df62990b4dea0a68.png)

Radar Assistant

1. In the message field, enter your rule request. You might ask to:  - Review payments where the card and IP countries are different.
  - Block Discover card payments of more than $1000.
  - Allow payments from stripe.com email addresses.


2. When the Assistant returns its suggestion, you can either enter an additional command to make adjustments to the rule or you can clickTest ruleto see how the rule performs against your recent transaction history.
3. When you’re satisfied with the rule, clickAdd ruleto enable it for all future transactions.

Training data consent: By using Radar Assistant you agree that Stripe can log and use your chat entries to train and improve the Radar Assistant capabilities. If you don’t want to have your chat entries used for this purpose, write rules manually.

Learn more about Stripe AI services.

### Review rules

Stripe still processes payments normally when they meet a review rule’s criteria. But we place them into your review queue so your team can look at them more closely. Setting up a rule that’s too broad can result in too many payments being placed into your review queue, slowing down your customers and burdening your review team.

Stripe’s rule testing interface runs a simulation on the last six months of charges to determine how many legitimate, fraudulent, and blocked payments would have been affected by the rule, had it been implemented. While testing a rule and examining the last six months, you should make sure that:

- Overall volume of payments is low. Reviewing these payments shouldn’t create a burden to your team.
- Human reviewers add value. A human reviewer can generally identify if a payment was fraudulent with greater confidence than the automated system.
- The rule results in a mix of successful and refunded or disputed payments. This means that additional inspection on these types of payments can help separate legitimate ones from those that are fraudulent.

The following is an example of how to improve a review rule created by a business that wants to review pre-paid credit cards.

Original ruleImproved rule`Review if :card_funding: = 'prepaid'``Review if :is_disposable_email: and :card_funding: = 'prepaid'`Too broad—results in too many reviewsMore focused—results in a smaller number of reviews### Block rules

You can use block rules to block payments that you’re fairly certain are fraudulent, or based on any restrictions your business has in place (such as blocking payments from prepaid cards). If you’re not sure how to apply block rules, we recommend placing payments in review using a review rule. After spending some time reviewing these payments for potential false positives, you can confirm if you’d like to create a block rule instead.

Block rules only impact fraudulent and successful payments, as already blocked payments would be unaffected. While testing a rule, make sure that you:

- Keep false positives as low as possible. During testing, Stripe identifies the number of successful and disputed payments that would’ve been matched by the rule. A good block rule results in significantly more fraudulent payments blocked than legitimate payments.
- Minimize unnecessary rules. If your rule appears to perform very well but is already covered by an existing rule, your newer rule may not be necessary. Similarly, if the results during testing appear to be mixed, consider setting up a review rule instead so you can gather more information about those types of payments.

The following is an example of how to improve a block rule created by a business that’s suffering from a high level of fraud from payments outside the US:

Original ruleImproved rule`Block if :card_country: != 'US'``Block if :card_country: != 'US' and :risk_level: = 'elevated'`Too broad—high number of legitimate payments blockedMore focused—results in a smaller number of reviews### Allow rules

### Allow rule availability

The ability to create allow rules isn’t immediately available to all users. If you’d like to enable this feature, contact us.

Allow rules override all other rules, including Stripe’s machine learning models, and you should use them with caution. Many businesses may not need to implement allow rules. If you have concerns that an allow rule could let through even a small number of fraudulent payments, you should consider adjustments to further restrict these rules before implementing them. As allow rules override all other rules, including Stripe’s machine learning judgments, you should create allow rules that continue to block any payments we believe are likely to be fraudulent.

Allow rules apply to all new payments as soon as you create the rule. This includes any payments that are similar to previously blocked payments. While testing a rule, make sure that you:

- Examine the number of previously blocked payments that would have been allowed. Allow rules override all other rules and Stripe’s risk assessment. When testing a new allow rule, all of the payments shown would have been allowed if this rule were active. This can include payments that had been blocked or disputed, impacting your future dispute rates.
- Continue to block any high-risk payments. You can do this by adding the following to any allow rule:`and :risk_level: != 'highest'`
- Evaluate a history of legitimate transactions at your business. You can leverage connections between your own customers to allow a higher volume of transactions based on a history of legitimate purchases. This helps you block fewer payments from customers that have a proven history at your business. To do this, review the[attributes list](/radar/rules/reference#supported-attributes)and look for attributes that include the word “customer.”

The following is an example of how to improve an allow rule for a business that generally (but not always) sees good payments coming from customers in the United Kingdom:

Original ruleImproved rule`Allow if :ip_country: = 'GB'``Allow if :ip_country: = 'GB' and :risk_level: != 'highest'`Too broad—some fraudulent payments are allowedMore focused-–-a smaller number of fraudulent payments are allowed## Maintaining your rules

As your business continues to grow, you want to be sure that your rules continue to reflect the types of customers that you want to do business with. The following are some best practices to keep rules current for the state of your business.

### Regularly monitor rules to ensure they’re still effective

Rule metrics![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

Fraud patterns constantly change, so we provide metrics to show how these rules are performing. These metrics vary depending on the type of rule, because the rule types perform different actions.

![](https://b.stripecdn.com/docs-statics-srv/assets/rule-performance.8d495f28c352641ff7b710df3c3df2ed.png)

You may spot a difference in the number of payments that matched review rules and the number of payments sent to your review queue in the same time period. Since only successful payments are placed in review, payments that match a review rule’s criteria but get declined by the issuer, for example, are not sent to your review queue.

Use the rule performance chart to understand the behavior of your Radar rules. Look for unexpected spikes or declines in the number of payments matching your rules, such as allow rules letting too many payments through or block rules blocking too many. These spikes may indicate a change in the types of payments your business is receiving or that may warrant updates to the rules themselves. Updates made to rules are displayed as triangles on the graph and can help you compare the impact of the change before and after you make it.

Color-coded lines track the number of payments that match 3D Secure rules, allow rules, block rules, and review rules. Triangular symbols on these graph lines represent updates to rules of the corresponding type.

You can find information about the effectiveness of your rules and see how many payments each one has taken action against. You can also view and download a filtered list of every payment that a rule has been applied to. Evaluate this information to help you decide if you need to make changes to any rules or remove them entirely.

To view additional commands, click the ellipses (•••) icon. Additional commands include: Disable, Enable, Edit or Delete for any rule.

Optionally, you can use our reporting products Sigma and Data Pipelines to query disputes and fraud data, including rule decisions and attributes for each individual payment.

Evaluate rule effectiveness![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You can find information about the effectiveness of your rules and see how many payments each one has affected. You can also view and download a filtered list of every payment that a rule has been applied to. Review the sample questions in the following table to help you decide if you need to make changes to any rules or remove them entirely.

Rule TypeEvaluateActions to considerGeneralDoes this rule no longer match any payments at all?Remove the rule.Does this rule have anomalous behavior, such as allowing more payments than in previous time periods?Manually review payments that matched this rule to determine if this is the behavior that you want.3DSIs 3DS completion rate high, but the number of disputes/EFWs is low?Remove the rule since you may be issuing friction to good users.Is fraud high for transactions that pass 3DS?Consider modifying your 3DS rule into a block rule to prevent these users from passing frictionless flow (controlled by issuers) or committing first party fraud.Is conversion rate for 3DS low?This may be a good rule since it might be mostly blocking fraudsters, but consider manually investigating matched payments to make sure your good users aren’t abandoning due to additional friction.AllowIs the number of disputes, EFWs, Refunds, or Failed payments high?Remove the rule that allows bad payments through.BlockIs the number of blocks going down, but your fraud is still steady or is increasing?Modify your rule since it may no longer be effective.Is the number of blocks going up, but your fraud is still steady or increasing?Modify your rule since it may be blocking good users.Is the number of blocks going up and your fraud is going down?This suggests that your rule is effective, but consider manually reviewing a few transactions to ensure that you are not blocking too many good users.Manual ReviewIs the percentage of payments that get reviewed low?Make the rule more restrictive since it may be too broad.Is the number of successful or approved payments high?Remove the manual review rule entirely or write an allow rule to target those payments.Is the number of refunds or disputes & Early Fraud Warnings high?Convert to a block rule.Request 3DS rules

For request 3DS rules, we display:

- 3DS Requested— the number of times a rule triggered a 3DS request.

Click a 3DS rule to see the following metrics:

![](https://b.stripecdn.com/docs-statics-srv/assets/request-credentials-rule-details.c22b65bc432aafec9e5bcb6079c53528.png)

Allow rules

For allow rules, Radar for Fraud Teams users can view:

If these disputed metrics are high, you might consider writing more narrowly targeted allow rules, so that you’re not allowing payments through that are eventually disputed.

- Allowed payments— the total number of payments allowed by your rules.
- Volume, allowed payments— the total amount, in your local currency, associated with payments allowed by your rules.
- Risk score— the corresponding[risk outcomes](/radar/risk-evaluation#risk-outcomes)assigned by Stripe machine learning models to the set of payments allowed by your rules.
- Disputes from overrides— the total number of allowed payments that were disputed.
- Volume, disputes from overrides— the total amount, in your local currency, associated with disputes from allowed payments.

Click an Allow rule to see the following metrics:

![](https://b.stripecdn.com/docs-statics-srv/assets/allow-rule-details.e8da078613fdbca5592d2f9330c0f6d4.png)

Block rules

For block rules, we display:

If estimated false positive rate metrics are high, you might consider writing more narrowly targeted block rules or reviewing which payments are covered by the rule to avoid blocking as many non-fraudulent payments.

- Blocked payments— the total number of payments blocked by your rules.
- Volume, blocked payments— the total amount, in your local currency, associated with payments blocked by your rules.

Radar for Fraud Teams users can also view:

- Risk score— the corresponding[risk outcomes](/radar/risk-evaluation#risk-outcomes)assigned by Stripe machine learning models to the set of payments allowed by your rules.
- Est. false positive rate— the estimated percentage of non-fraudulent payments that were blocked for both your block rules as a set and by individual rules. (These estimates are made using the estimated false positive rates of the corresponding machine learning risk scores, which we calculate with experiments across the Stripe network.)
- Est. disputes avoided— the estimated number of disputes that your block rules prevented. This is estimated using the precision of the corresponding machine learning risk scores, which we calculate with experiments across the Stripe network.

Click a Block rule to see the following metrics:

![](https://b.stripecdn.com/docs-statics-srv/assets/block-rule-details.5df9a2e8652f228cf61b525a32ef56da.png)

Review rules

For review rules, Radar for Fraud Teams users can view:

- Payments sent to review— the total number of payments that were sent to manual review by your rules.
- Volume, approved reviews— the total amount, in your local currency, associated with approved payment reviews.
- Refund rate— the percentage of reviews that were refunded.
- Disputes from approved reviews— the total number of payments that were approved in your review, but were ultimately disputed.
- Volume, disputes from approved reviews— the total amount, in your local currency, associated with disputes from approved payment reviews.

Click a Review rule to see the following metrics:

![](https://b.stripecdn.com/docs-statics-srv/assets/review-rule-details.10851302ef65dee05ffce64f7989528f.png)

### Regularly monitor your manual review queue

If your review queue is getting too large to manage, check to see if you have the right rules in place. If most reviews end up being refunded as fraudulent, consider some additional rules to block payments. Likewise, if most payments are approved, consider making your review rules more focused.

### Analyze your disputed and refunded payments

Disputes are inherently linked to fraud, so the more you do to reduce fraud, the lower your dispute rate. You should check to see if disputed payments share any similar characteristics (for example, from the same locations or of similar amounts). You can also perform this type of investigation by looking at payments that have been refunded during a review. If you see trends, you can test and create the appropriate rules. If any payments appear to be fraudulent, refund and report them as fraud to avoid potential disputes.

Optionally, you can use our reporting products Sigma and Data Pipelines to query disputes and fraud data.

You can respond to any incoming disputes using the Dashboard or through the API, and our dispute documentation includes some suggestions on how to present a well documented case.

### Anticipate large changes to your business that might impact your fraud rate

If you’re planning any major product releases or changes to your service (for example, a new, high-value product or expanding your service into new countries), you may want to monitor these payments in the beginning. For these kinds of changes, it’s a good practice to set up some review rules so you can examine any new payments. Reviewing these payments and identifying patterns can help you set up new rules to protect your business from fraud.

## See also

- [3DS Rule Examples](/radar/rules#request-3d-secure)
- [Continuous Fraud Management Guide](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data)
- [Query Disputes and Fraud Data](/stripe-data/query-disputes-and-fraud-data)
- [Radar 101 Guide](https://stripe.com/guides/radar-rules-101)
- [Rules Reference](/radar/rules/reference)
- [Supported Attributes](/radar/rules/supported-attributes)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Built-in rules](#built-in-rules)[When to create rules](#when-to-create-rules)[Construct rules](#construct-rules)[Maintaining your rules](#maintaining-your-rules)[See also](#see-also)Products Used[Radar](/radar)[Payments](/payments)[Sigma](/stripe-data/access-data-in-dashboard)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`