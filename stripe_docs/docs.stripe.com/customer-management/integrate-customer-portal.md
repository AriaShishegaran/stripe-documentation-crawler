# Integrate the customer portal with the API

## Get started

With the customer portal, you can provide subscription, billing, and invoicing management to your customers without building it yourself. After you configure and integrate the portal, customers redirect to a co-branded dashboard where they can manage their account based on the functionality you configured.

To integrate your application with the customer portal:

- Configure the portal’s features and user interface (UI). You can do this in the Dashboard.

[Configure](#configure)

- Implement a redirect to integrate the portal with your application.

[Implement a redirect](#redirect)

- Listen to webhooks to receive updates to customers’ subscriptions and payment methods.

[Listen to webhooks](#webhooks)

- Go live to use the portal in your production environment.

[Go live](#go-live)

Or clone one of our sample projects:

- Firebase

[Firebase](https://github.com/stripe-samples/firebase-subscription-payments)

- Netlify Identity

[Netlify Identity](https://github.com/stripe-samples/netlify-stripe-subscriptions)

- Ruby on Rails.

[Ruby on Rails](https://github.com/stripe-samples/developer-office-hours/tree/master/2020-06-29-customer-portal)

You can optionally customize portal sessions to enable different features for different customers.

[customize](#customize)

[Configure the portal](#configure)

## Configure the portal

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register/)

Before you integrate the customer portal, configure its functionality and branding in the Dashboard to define what your users can do with the portal. Its features depend on your product and price catalog, so there are different settings for live and test modes.

If you’re using the customer portal with Stripe Connect, make sure you configure the customer portal for the platform, not a connected account.

If you want to create multiple portal configurations for different sets of customers—or if you’re a Connect platform and would like to manage configurations for your connected accounts—you can do that by using the API:

[Connect](/connect)

[API](/api/customer_portal/configuration)

If you allow customers to upgrade, downgrade, or change the quantities of their subscriptions, you must also set a product catalog. This includes the products and prices that your customers can upgrade or downgrade to, as well as the subscriptions they can update quantities on. See the guide for more details about creating products and prices. If you’re using the customer portal only for invoicing, you don’t need to set a product catalog.

[guide](/products-prices/getting-started#create-product)

The portal displays the following attributes of your product catalog:

- Product name and description—these attributes are editable in the Dashboard and API.

- Quantity restrictions per product—these attributes are editable in the Dashboard.

- Price amount, currency, and billing interval—these attributes are immutable and you can only set them when you create them in the Dashboard and API.

If you use Stripe Tax to automatically collect taxes for subscriptions or invoices, you can let customers set and update their tax IDs in the customer portal. Stripe Billing adds the tax IDs to the customers’ invoices. To enable this, go to the Customer portal settings and toggle on Tax ID. For more information, see how customer tax IDs work with subscriptions and invoices.

[Stripe Tax](/tax)

[invoices](/api/invoices)

[Customer portal settings](https://dashboard.stripe.com/settings/billing/portal)

[subscriptions](/billing/customer/tax-ids)

[invoices](/invoicing/taxes/account-tax-ids)

Learn how to set up Stripe Tax, collect taxes for recurring payments, collect taxes in your custom payment flows and set tax rates for line items and invoices.

[set up Stripe Tax](/tax/set-up)

[collect taxes for recurring payments](/billing/taxes/collect-taxes)

[collect taxes in your custom payment flows](/tax/custom#existing-customer)

[set tax rates for line items and invoices](/tax/invoicing)

As you configure your settings, you can preview the portal by clicking Preview. This launches a read-only version of the portal that lets you see how your customers could manage their subscriptions and billing details.

After saving your settings, you can launch the portal and test it by using a customer in test mode. Navigate to a customer in the Dashboard, click Actions, and then select Open customer portal.

Previewing the portal as a read-only version is only available when your Dashboard is in test mode. If you’re unable to preview and test the portal, check your settings to make sure that your configuration is saved in test mode. For previewing and testing to work, you also need to have edit permissions in the Dashboard.

[Implement a redirect on your siteClient-sideServer-side](#redirect)

## Implement a redirect on your siteClient-sideServer-side

A portal session is the entry point into the customer portal. It provides a unique, temporary link to the portal. When a customer wants to manage their billing or invoicing, create a new portal session and redirect them to the session’s url.

On your site, add a button that customers can click to enter the portal. Use a POST request to create a portal session:

Next, add an endpoint that creates a portal session and redirects your customers. Make sure to authenticate customers on your site before creating sessions for them. To create a session, you need the customer’s ID and a return_url, which is required if a default return URL isn’t set in the Dashboard configuration.

[create a session](/api/customer_portal/sessions/create)

When you create a portal session, Stripe returns the portal session object, which contains the session’s short-lived URL that your customers use to access the customer portal.

[short-lived URL](/api/customer_portal/session?lang=curl#portal_session_object-url)

[Listen to webhooksServer-side](#webhooks)

## Listen to webhooksServer-side

When subscriptions are upgraded, downgraded, or canceled, you need to make sure that customers receive only the products or services they’re actively subscribed to. Stripe sends notifications of these changes to your integration using webhooks. In the Event object, look at the ID for the subscription or the customer to determine which customer the event applies to.

[webhooks](/webhooks)

Stripe also sends notifications if an invoice is paid to your integration using webhooks. In the Event object, look at the ID for the invoice or the customer to determine which customer the event applies to.

[webhooks](/webhooks)

If you haven’t set up a webhook endpoint with Stripe before, you can use Stripe’s webhooks documentation to get started, and then listen for the events described below.

[webhooks documentation](/webhooks)

customer.subscription.updated

[customer.subscription.updated](/api/events/types#event_types-customer.subscription.updated)

Listen to this to monitor subscription upgrades and downgrades. For upgrades, check the subscription.items.data[0].price attribute in the subscription object to find the price the customer is subscribed to. Then, grant access to the new product. For downgrades, check the same attribute and adjust or revoke access as needed.

When a customer uses the portal to upgrade or downgrade a subscription with a trial, the subscription’s trial ends immediately when switching to the new price.

[trial](/billing/subscriptions/trials)

[customer.subscription.updated](/api/events/types#event_types-customer.subscription.updated)

customer.subscription.deleted

[customer.subscription.deleted](/api/events/types#event_types-customer.subscription.deleted)

Listen to this to monitor subscription cancellations. When you receive this event, revoke the customer’s access to the product. If you configure the portal to cancel subscriptions at the end of a billing period, listen to the customer.subscription.updated event to be notified of cancellations before they occur. If cancel_at_period_end is true, the subscription is canceled at the end of its billing period.

[customer.subscription.updated](/api/events/types#event_types-customer.subscription.updated)

If a customer changes their mind, they can reactivate their subscription prior to the end of the billing period. When they do this, a customer.subscription.updated event is sent. Check that cancel_at_period_end is false to confirm that they reactivated their subscription.

[customer.subscription.updated](/api/events/types#event_types-customer.subscription.updated)

[payment_method.attached](/api/events/types#event_types-payment_method.attached)

[payment_method.detached](/api/events/types#event_types-payment_method.detached)

[customer.updated](/api/events/types#event_types-customer.updated)

[customer.tax_id.created](/api/events/types#event_types-customer.tax_id.created)

[tax IDs guide](/billing/customer/tax-ids)

[customer.tax_id.deleted](/api/events/types#event_types-customer.tax_id.deleted)

[tax IDs guide](/billing/customer/tax-ids)

[customer.tax_id.updated](/api/events/types#event_types-customer.tax_id.updated)

[tax IDs guide](/billing/customer/tax-ids)

[billing_portal.configuration.created](/api/events/types#event_types-billing_portal.configuration.created)

[billing_portal.configuration.updated](/api/events/types#event_types-billing_portal.configuration.updated)

[billing_portal.session.created](/api/events/types#event_types-billing_portal.session.created)

[Go live](#go-live)

## Go live

Make sure to test the portal before enabling it in production. When you’re ready to go live:

When you create a portal session, Stripe returns the portal session object, which contains the session’s short-lived URL that your customers must use to access the customer portal. You can also create one shareable link for each configuration of the portal with the login_page parameter.

[short-lived URL](/api/customer_portal/session?lang=curl#portal_session_object-url)

[login_page](/api/customer_portal/configuration#portal_configuration_object-login_page)

- Turn off View test data in the Dashboard.

- Configure the portal in live mode.

[Configure](https://dashboard.stripe.com/settings/billing/portal)

- Add your webhooks in live mode.

[webhooks](https://dashboard.stripe.com/webhooks)

Stripe maintains two distinct sets of portal configurations: one for live mode and one for test mode. To help you validate your integration, making changes in one mode does not affect your configuration in the other.

[OptionalDeep link to specific pages](#deep-links)

## OptionalDeep link to specific pages

[OptionalCustomize a portal sessionServer-side](#customize)

## OptionalCustomize a portal sessionServer-side

[OptionalCustomize branding](#branding)

## OptionalCustomize branding
