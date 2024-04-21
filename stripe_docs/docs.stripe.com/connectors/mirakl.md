# Stripe Connector for Mirakl

Connect is the perfect fit for Mirakl marketplaces:

[Connect](/connect)

[Mirakl](https://www.mirakl.com/)

- Compatible with all the payment methods offered by Stripe.

[payment methods](https://stripe.com/payments/features#payment-options)

- Works for B2C and B2B marketplaces.

- Supports multi-seller and hybrid orders.

- Automated payouts based on your configuration.

[payouts](/payouts)

## Integration steps

The main tasks to set up payments for your marketplace using Mirakl are:

- First, you need a Stripe account. Register.

[Register](https://dashboard.stripe.com/register)

- Implement the relevant payment methods. Use one of our existing plugins or build your own integration.

[existing plugins](/connectors)

[build your own integration](/payments)

- Activate Connect in your Dashboard. Choose Platform or marketplace as your integration type.

[Activate Connect](https://dashboard.stripe.com/connect/accounts/overview)

- Configure your Connect branding settings.

[Connect branding settings](https://dashboard.stripe.com/settings/connect)

- Configure and install the connector on your test environment.

[Configure](/connectors/mirakl/configuration)

[install](/connectors/mirakl/install)

- Adapt your communication to sellers as described in the onboarding workflow.

[onboarding workflow](/connectors/mirakl/onboarding-sellers#communication)

- Adapt your payments requests as described in the payment split workflow

[payment split workflow](/connectors/mirakl/payments#payment-validation)

- Test the different workflows: onboarding, payments, refunds, and payouts.

- Activate your Stripe account.

[Activate](https://dashboard.stripe.com/account/onboarding)

- Complete your Platform profile.

[Platform profile](https://dashboard.stripe.com/connect/profile)

- Configure and install the connector on your live environment.

[Configure](/connectors/mirakl/configuration)

[install](/connectors/mirakl/install)

- Go live.

Optionally, you can use Radar for fraud protection or Stripe Billing to create and manage invoices and recurring payments.

[Radar](/radar)

[Stripe Billing](/billing)

[invoices](/api/invoices)

## Workflows

Learn more about each workflow:

- Onboarding sellers

[Onboarding sellers](/connectors/mirakl/onboarding-sellers)

- Payments

[Payments](/connectors/mirakl/payments)

- Payouts

[Payouts](/connectors/mirakl/payouts)

## Alerting

The workflows supported by the connector don’t require any manual intervention or operational supervision. In case an operation fails, the alerting job sends you an email.

[alerting job](/connectors/mirakl/reference#alerting)
