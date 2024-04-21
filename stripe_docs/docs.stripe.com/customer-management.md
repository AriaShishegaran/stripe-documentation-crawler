# Customer management

To let your customers manage their account on their own, use Stripe’s hosted solutions, like the customer portal and hosted recovery flows. You can set up and use these solutions without writing any code.

[hosted recovery flows](/billing/revenue-recovery/automations)

## Get started with the customer portal

[Share a link to customer portalNo code](/customer-management/activate-no-code-customer-portal)

[Integrate into your site](/customer-management/integrate-customer-portal)

[Streamline customer portal flows](/customer-management/portal-deep-links)

## Customer portal features

The customer portal allows your customers to self-manage their payment details, invoices, and subscriptions in one place.

See what your customers can do in the customer portal

Key customer portal features

- Download invoices

- Update payment methods

- Cancel a subscription

- Update customer information

- Upgrade and downgrade subscriptions

View demo

[View demo](https://billing.stripe.com/customer-portal-demo)

- Update billing information, including their tax IDs

- Update payment methods

- Update subscriptions

- Cancel, pause, resume, and view subscriptions

- Pay, download, and view current and past invoices

- Checkout

[Checkout](/payments/checkout)

- Payment Links

[Payment Links](/payment-links)

- Connect

[Connect](/connect)

- Invoices

[Invoices](/invoicing)

- Billing

[Billing](/billing)

- Stripe Tax

[Stripe Tax](/tax)

[supported payment methods](#supported-payment-methods)

[payment methods](/payments/payment-methods/integration-options)

- Turn on test mode in the Dashboard (nothing you do in test mode affects your live setup).

- Go to the Customers page, and select a customer.

[Customers page](https://dashboard.stripe.com/customers)

- Create a new invoice for the customer.

- Click Actions, then Open customer portal. For security reasons, the quick view option isn’t available for live mode customers.

- Bulgarian (bg)

- Chinese Simplified (zh)

- Chinese Traditional—Hong Kong (zh-Hant-HK)

- Chinese Traditional—Taiwan (zh-Hant-TW)

- Croatian (hr)

- Czech (cs)

- Danish (da)

- Dutch (nl)

- English, US (en)

- English, UK (en-GB)

- Estonian (et)

- Filipino (fil)

- Finnish (fi)

- French, France (fr)

- French, Canada (fr-CA)

- German (de)

- Greek (el)

- Hungarian (hu)

- Indonesian (id)

- Italian (it)

- Japanese (ja)

- Korean (ko)

- Latvian (lv)

- Lithuanian (lt)

- Malay (ms)

- Maltese (mt)

- Norwegian Bokmål (nb-NO)

- Polish (pl)

- Portuguese, Portugal (pt)

- Portuguese, Brazil (pt-BR)

- Romanian (ro)

- Russian (ru)

- Slovak (sk)

- Slovenian (sl)

- Spanish, Spain (es)

- Spanish, Latin America (es-419)

- Swedish (sv)

- Thai (th)

- Turkish (tr)

- Vietnamese (vi)

The customer portal has the following limitations:

- If subscriptions use any of the following, customers can only cancel them in the portal (they can’t update such subscriptions):Multiple products Usage-based billingSending invoices for collection. Read more about the collection_method parameter. If you use the Dashboard to create the subscription, you make this selection in the Payment method section.Unsupported payment methods

If subscriptions use any of the following, customers can only cancel them in the portal (they can’t update such subscriptions):

- Multiple products

[Multiple products](/billing/subscriptions/multiple-products)

- Usage-based billing

[Usage-based billing](/products-prices/pricing-models#usage-based-pricing)

- Sending invoices for collection. Read more about the collection_method parameter. If you use the Dashboard to create the subscription, you make this selection in the Payment method section.

[parameter](/api/subscriptions/object#subscription_object-collection_method)

[use the Dashboard](/billing/subscription-resource?dashboard-or-api=dashboard#create-subscriptions)

- Unsupported payment methods

- Customers can’t update or cancel subscriptions that currently have an update scheduled with a subscription schedule.

Customers can’t update or cancel subscriptions that currently have an update scheduled with a subscription schedule.

[subscription schedule](/billing/subscriptions/subscription-schedules)

- Customers can only modify subscriptions if the new price has the same tax behavior as the initial price. Additionally, no modifications are allowed if the tax behavior is unspecified, even if the tax behavior of the new price is unspecified. Learn more about the tax_behavior parameter and how it relates to subscriptions.

Customers can only modify subscriptions if the new price has the same tax behavior as the initial price. Additionally, no modifications are allowed if the tax behavior is unspecified, even if the tax behavior of the new price is unspecified. Learn more about the tax_behavior parameter and how it relates to subscriptions.

[tax behavior](/api/prices/create#create_price-tax_behavior)

[relates to subscriptions](/billing/taxes/collect-taxes?tax-calculation=stripe-tax#product-and-price-setup)

- The portal doesn’t display the payment method section if the portal doesn’t support the customer’s default payment method.

The portal doesn’t display the payment method section if the portal doesn’t support the customer’s default payment method.

- Customers can’t define multiple Prices with the same product and recurring.interval values. For example, to offer a magazine for 4.00 USD per month regular price and 3.00 USD per month for students, create a separate student magazine Product version.

Customers can’t define multiple Prices with the same product and recurring.interval values. For example, to offer a magazine for 4.00 USD per month regular price and 3.00 USD per month for students, create a separate student magazine Product version.

[Prices](/api/prices)

[Product](/api/product)

- Customer modifications to a trialing subscription will end the free trial and create an invoice for immediate payment.

Customer modifications to a trialing subscription will end the free trial and create an invoice for immediate payment.

- When you allow customers to switch plans, you can specify a maximum of 10 products for them to choose from.

When you allow customers to switch plans, you can specify a maximum of 10 products for them to choose from.

[allow customers to switch plans](/customer-management/configure-portal#configure-subscription-management)

## Supported payment methods

[Payment method](/api/payment_methods/object#payment_method_object-type)

[Requires approval](/payments/paypal/set-up-future-payments#enable-recurring-payments-support-from-stripe-dashboard)

## Other hosted resources to use with the customer portal

Stripe offers multiple prebuilt resources so you can bill your customers quickly and maximize revenue retention and recovery.

[Payment links](/payment-links)

[Checkout](/payments/checkout)

[Pricing table](/payments/checkout/pricing-table)
