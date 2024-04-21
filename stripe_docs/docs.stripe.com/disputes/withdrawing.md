# Dispute withdrawals

The most effective dispute strategy for your business is to reduce the number of disputes it receives in the first place.

[reduce the number of disputes](/disputes/prevention)

If you do receive a dispute, the most effective way to proceed is to work directly with your customer to resolve the issue.

Every card network has some provision in its dispute system for the cardholder to retract a dispute after filing it. If you can settle the matter amicably with your customer, and convince them to withdraw the dispute, that’s the best way to win it.

## What is a withdrawn dispute

A withdrawn dispute is one that your customer has asked their card issuer to cancel. It isn’t necessarily a won dispute, as the dispute might still resolve as a loss if you haven’t submitted evidence.

A withdrawn dispute is otherwise no different from any other dispute.

- It doesn’t resolve as a win or loss more quickly than other disputes.

- It doesn’t show up differently from any other dispute in the Dashboard or API.

- It still counts against your dispute rate with the network.

[dispute rate](/disputes/measuring)

Cardholders can only withdraw fully financial disputes—that is, a chargeback, where your account balance has been debited. They can’t withdraw an Early Fraud Warning or an inquiry, which don’t have financial impact. The cardholder might decline to escalate these, but can’t undo them.

[Early Fraud Warning](/disputes/how-disputes-work#early-fraud-warnings)

[inquiry](/disputes/how-disputes-work#inquiries)

## Assessing the value of pursuing a dispute withdrawal

Although a dispute withdrawal is a good way to turn a dispute into a win, and a way to resolve a negative experience for your customer, it also requires some effort to initiate and complete an interaction with your customer. It might not be the most cost efficient approach for every dispute, and you’ll have to weigh the increased operational burden against the lift it gives your dispute win rate.

For disputes with a high likelihood of winning, you might want to only submit evidence to fight it, without reaching out to your customer. For low value disputes you might want to go ahead and accept the dispute.

[high likelihood of winning](/disputes/best-practices#likelihood-of-winning-disputes)

[accept the dispute](/disputes/responding#decide)

## Talk to your customer

Reach out to your customer to better understand their complaint, and try to work through the problem with them. If you’re able to satisfy the customer, ask them to reach out to their card issuer and withdraw the dispute. The process for this varies by issuer, but in general the customer should use whatever normal support channels they use to get help from their issuer.

If your customer does agree to withdraw the dispute, consider asking them whether they would provide confirmation of the withdrawal, such as a withdrawal-confirmation email from their bank or a screenshot of their mobile banking statement showing they  were re-billed for the charge. This type of evidence isn’t required for your response to the issuer, but it could be helpful if your customer is willing to do it.

If part of the resolution with your customer involves an agreement that you will issue a refund to them, be aware that it might be weeks or even months before you’re able to issue one. Your customer withdrawing the dispute doesn’t necessarily speed up their issuer’s dispute timeline. You can’t issue a refund on a disputed charge until your customer’s card issuer returns a win on the dispute.

[can’t issue a refund](/disputes/how-disputes-work#receiving-a-dispute)

## Submit evidence

Regardless of what happens between you and your customer, you still need to submit evidence if you want to win the dispute.

[submit evidence](/disputes/responding#respond)

Always provide evidence for every dispute you hope to have resolved in your favor, even if your customer told you they’re withdrawing the dispute. Many card issuers treat failure to submit evidence as an acceptance of liability on your part. This means that even if the customer did withdraw the dispute with their issuer, you can still lose the dispute if you don’t submit evidence.

You can submit evidence for a dispute just one time, so you want to wait long enough for your conversation with the customer to play out, but not so long that you miss the deadline. The card network rules don’t allow you to submit evidence after the deadline.

If you can’t convince the customer to withdraw the dispute before the evidence deadline, that’s okay. You should still file appropriate evidence to challenge the dispute reason.

[appropriate evidence](/disputes/categories)

## Wait for the dispute resolution

In general, disputes that have been withdrawn don’t resolve any faster than other kinds of dispute.

After your customer withdraws a dispute, and you submit evidence, you can expect that the dispute will still follow the normal dispute timeline to come back with a win or loss from the network.

[normal dispute timeline](/disputes/how-disputes-work#timing)

## Late withdrawal of dispute

It’s technically possible on every card network for a cardholder to withdraw a dispute after the response deadline, and even long after a dispute itself is lost. However, some card issuers within that network might not support the late withdrawal of a dispute in every case. As with any other dispute, the cardholder needs to reach out to their issuer to request a late withdrawal and find out whether or not they allow it.

Keep in mind that late withdrawals often happen outside the networks’ dispute systems. Unlike with the regular dispute lifecycle, they aren’t governed by any network rules or regulations. Consequently when a customer withdraws an old, lost dispute, it’s hard to set a realistic expectation for how soon you can expect to see it reflected in your Stripe account. It’s possible it could take the cardholder’s issuer weeks or months to process this type of adjustment.
