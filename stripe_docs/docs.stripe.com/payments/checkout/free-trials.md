# Configure a free trial without collecting payment details

Stripe Checkout lets you sign up customers for a free trial of a subscription service without collecting their payment details. At the end of the trial period you specify, use Stripe to configure a reminder email to collect a customer’s payment details.

[Configure Checkout session](#section-1)

## Configure Checkout session

Create a Checkout Session with the following:

- A subscription_data parameter with:trial_period_days set to the length (in days) of your free trial. In this example, the trial period is 30 days.trial_settings[end_behavior][missing_payment_method] set to cancel (or pause) if the trial ends without a payment method attached. View Use trial periods to learn more.

- trial_period_days set to the length (in days) of your free trial. In this example, the trial period is 30 days.

- trial_settings[end_behavior][missing_payment_method] set to cancel (or pause) if the trial ends without a payment method attached. View Use trial periods to learn more.

[Use trial periods](/billing/subscriptions/trials#create-free-trials-without-payment)

- The payment_method_collection parameter set to if_required. This tells Stripe that collecting payment information at checkout is optional.

[Collect payment details when the trial is about to expire](#collect-payment)

## Collect payment details when the trial is about to expire

Before the trial expires, collect payment details from your customer.

Under Manage free trial messaging in your Subscriptions and emails settings, you can choose to automatically send a reminder email when a customer’s trial is about to expire.

[Subscriptions and emails settings](https://dashboard.stripe.com/settings/billing/automatic)

Next, select the Link to a Stripe-hosted page option so the reminder email contains a link for the customer to add or update their payment details. We don’t send free trial reminder emails in test mode. Learn more about how to set up free trial reminders.

[set up free trial reminders](/billing/revenue-recovery/customer-emails#trial-ending-reminders)

You must comply with card network requirements when offering trials. Learn more about compliance requirements for trials and promotion.

[compliance requirements for trials and promotion](/billing/subscriptions/trials#compliance)

[OptionalCollect payment details in the Billing customer portal](#customer-portal)

## OptionalCollect payment details in the Billing customer portal
