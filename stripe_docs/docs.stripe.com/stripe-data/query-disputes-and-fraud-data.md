# Query disputes and fraud data

The disputes table contains data about all disputes on your account. Each row represents a Dispute object, which is created when a charge is disputed. Each dispute also includes any available data about dispute evidence that you’ve submitted.

[disputes](/disputes)

[Dispute](/api#dispute_object)

The following example provides some preliminary information about the five most recent lost disputes. It joins the disputes and charges tables together using the disputes.charge_id and charges.id columns. Along with a dispute ID, each row contains an associated charge ID, the amount, and the outcome of the ZIP and CVC checks.

Using Sigma or Data Pipeline to create reports about your disputes can help you identify fraudulent payments, which you can prevent by using Radar.

[Radar](/radar)

## Radar for Fraud Teams Data

If you use Radar for Fraud Teams, you have a table radar_rules that contains all Radar custom rules with their action and predicate. You can use this to obtain the rule_id which can then be used in rule_decisions table to find all charges affected by rules. This is more flexible than looking at the outcome_rule_id attribute in the charges table, as it also shows 3DS Rules triggered for Payment Intents and Setup Intents. Radar’s built-in rules have fixed rule IDs.

[built-in rules](/radar/rules#built-in-rules)

The following example shows recent payments allowed by an allow-list and their Radar score to check if potentially fraudulent payments were allowed:

Multiparty payment businesses such as Connect platforms have particular risk management requirements. Here’s an example of listing destination charge businesses on your platform by their dispute rate:

[particular risk management requirements](/connect/risk-management)

[destination charge](/connect/destination-charges)

Sigma and Data Pipelines contains data on 3D Secure Authentication (3DS). This more complex example shows for each 3DS Rule how many times it triggered 3DS and what the outcomes were, considering there might be more than one attempt:

[3DS](/payments/3d-secure)

You also have access to the radar_rule_attributes table. Each row contains most of the Radar rule attribute values for a single charge. You can join the radar_rule_attributes and disputes tables together using the radar_rule_attributes.transaction_id and disputes.charge_id columns, which allows you to write rules targeting your disputes and understand trends in your good and bad customers.

[Radar rule attribute](/radar/rules/reference#supported-attributes)

[charge](/api/charges/object)

For more details on columns available see our guide on How to continuously improve your fraud management with Radar for Fraud Teams and Stripe Data. It explains, for instance, where to find Radar scores per Charges and so on.

[How to continuously improve your fraud management with Radar for Fraud Teams and Stripe Data](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data)

## Tracking Monitoring Programs

Card brand monitoring program metrics are difficult to track because rules are very specific. Some details are crucial, such as when to use volume or transaction count. Tracking them is required to estimate fraud and chargeback levels and take action promptly, because monitoring program notifications don’t happen immediately. We recommend a continous process to track and estimate chargeback and fraud metrics.

[Card brand monitoring program](/disputes/monitoring-programs)

[continous process](https://stripe.com/guides/improve-fraud-management-with-radar-for-fraud-teams-and-stripe-data)

With Sigma, you can write a query to estimate fraud levels that simulate how card monitoring programs might assess your payments. The query below isn’t perfect (for example, we assume this is a US merchant where domestic and cross-border payments are counted, but you can adjust the query for your use case). Most importantly, it takes FX (currency exchange rates) into account, and applies the same method of counting payment and fraud periods independently as the monitoring programs typically do.
