# Use Stripe Tax with Connect

Stripe Tax supports Connect by helping you calculate and collect taxes. It provides transactional reports to help with tax reporting and filing for your platform or your connected accounts.

[Connect](/connect)

## Who is liable?

The first step for using Stripe Tax with Connect requires you to determine which entity has the obligation to collect and report taxes. The entity that’s liable for tax might be you or your connected account, depending on your business model, regulations (for example, marketplace laws in the US and EU), or the transaction details, such as the order amount or the type of goods being sold.

[marketplace laws in the US and EU](https://stripe.com/en-nl/guides/guide-to-sales-tax-and-vat-for-marketplace-sellers)

Consult with a tax advisor who understands your business model to determine the tax obligations for both your platform and your connected accounts.

## Tax for software platforms (non-marketplaces)

SaaS platforms enable other businesses with software services to reach their customers. In these configurations, the connected accounts typically assume responsibility for collecting and remitting taxes. Stripe Tax supports the following charge types and integrations for platforms:

[assume responsibility for collecting and remitting taxes](/tax/tax-for-platforms)

- Direct charges

[Direct charges](/connect/direct-charges)

- Destination charges

[Destination charges](/connect/destination-charges)

- Destination charges with on_behalf_of

[Destination charges with on_behalf_of](/connect/destination-charges#settlement-merchant)

- Separate charges and transfers

[Separate charges and transfers](/connect/separate-charges-and-transfers)

- Separate charges and transfers with on_behalf_of

[Separate charges and transfers with on_behalf_of](/connect/separate-charges-and-transfers#settlement-merchant)

- Payment Intents (using the Stripe Tax API)

[Tax API](/tax/custom)

- Checkout

[Checkout](/tax/checkout)

- Billing

[Billing](/tax/subscriptions)

- Invoicing

[Invoicing](/tax/invoicing)

- Payment Links

[Payment Links](/tax/paymentlinks)

- Off-Stripe payments

- Stripe Tax API

[Tax API](/tax/custom)

## Tax for marketplaces

Stripe Tax supports the following charges and integrations for marketplaces:

- Direct charges

[Direct charges](/connect/direct-charges)

- Payment Intents (using the Stripe Tax API)

[Tax API](/tax/custom)

- Destination charges

[Destination charges](/connect/destination-charges)

- Destination charges with on_behalf_of

[Destination charges with on_behalf_of](/connect/destination-charges#settlement-merchant)

- Separate charges and transfers

[Separate charges and transfers](/connect/separate-charges-and-transfers)

- Separate charges and transfers with on_behalf_of

[Separate charges and transfers with on_behalf_of](/connect/separate-charges-and-transfers#settlement-merchant)

- Payment Intents (using the Stripe Tax API)

[Tax API](/tax/custom)

- Checkout

[Checkout](/tax/checkout)

- Billing

[Billing](/tax/subscriptions)

- Invoicing

[Invoicing](/tax/invoicing)

- Payment Links

[Payment Links](/tax/paymentlinks)

- Off-Stripe payments

- Stripe Tax API

[Tax API](/tax/custom)

## What is a marketplace?

Marketplaces connect buyers and sellers on a single platform, and are websites or apps where products are listed by multiple third-party vendors. In some jurisdictions, marketplaces might be responsible for tax collection on transactions that they facilitate. The terminology used by the local tax authorities to refer to marketplaces that are responsible for tax collection varies by jurisdiction. Some examples include:

[marketplaces might be responsible for tax collection](/tax/tax-for-marketplaces)

Stripe Connect’s distinction between platforms and marketplaces doesn’t strictly correspond to the tax definition of marketplaces. We recommend you consult with a tax advisor to confirm if your business qualifies as a marketplace for tax purposes.

## See also

- Tax for platforms

[Tax for platforms](/tax/tax-for-platforms)

- Tax for marketplaces

[Tax for marketplaces](/tax/tax-for-marketplaces)
