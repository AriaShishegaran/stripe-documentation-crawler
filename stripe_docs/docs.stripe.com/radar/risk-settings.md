# Risk controls

To adjust the default risk score for blocking payments, use Radar for fraud teams. Go to the Radar risk controls page to make your adjustments.

[Radar risk controls](https://dashboard.stripe.com/settings/radar/risk-controls)

The risk settings dialog shows your block threshold, your dispute rate, and other important statistics

## How it works

Stripe Radar gives each charge a numerical risk score between 0 and 99, where 0 is the lowest risk and 99 highest.

[risk score](/radar/risk-evaluation#risk-outcomes)

The default blocking threshold is 75, meaning Radar blocks charges with a score of 75 or higher.  If you decrease your threshold, you’ll block more payments.

You need to make sure the default block rule or an equivalent custom rule is enabled for Radar to block transactions based on this threshold.

[the default block rule](/radar/rules#built-in-rules)

The default manual review threshold is 65, meaning Radar sends charges with a score of 65 or higher to manual review.  Changing the blocking threshold automatically changes the manual review threshold accordingly.

For Radar to send transactions to manual reviews based on this threshold, you need to enable the default review rule or equivalent custom rules.

[the default review rule](/radar/rules#built-in-rules)

When you change your blocking threshold, you see the following statistics:

## When to use it

The ability to increase risk score thresholds beyond their defaults isn’t immediately available to all users. If you’d like to enable this feature, contact us.

[contact us](https://support.stripe.com/contact)

You can customize the default threshold to fit your own business needs. Setting the risk score threshold requires you to consider a tradeoff between how much fraud Radar blocks and how many payments it allows.

If your business is experiencing higher rates of fraud, you can decrease the score for blocking payments. To determine what risk score is right for your business, hover over the Block additional payments by setting your acceptable risk score chart.

This chart shows how many fraudulent and good payments you would’ve blocked if you set your threshold at that risk score. Here, you can see:

Ultimately, it is up to your business to decide what tradeoff you’re willing to accept in terms of how much fraud versus good payments you block.

If your business has low fraud rates and costs, you might want to increase the default blocking score so that you can allow more payments overall.

This chart shows how many payments you would allow if you set your threshold at that risk score. Here, you can see:

If you’re increasing the risk score for blocking charges, we can’t accurately predict the impact of this change on your fraud rate (as some charges that were previously blocked will now be allowed). Be careful when adjusting the risk score in this direction.

## See also

- Risk Evaluation

[Risk Evaluation](/radar/risk-evaluation)

- Review

[Review](/radar/reviews)

- Integration Checklist

[Integration Checklist](/radar/integration)
