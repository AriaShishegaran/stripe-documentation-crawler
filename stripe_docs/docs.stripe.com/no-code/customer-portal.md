# Set up the customer portal

- Stripe compatibility: Payment Links, Checkout, pricing table, customer portal

- Requires: Stripe account

- Good for: SaaS businesses, individual creators, e-commerce businesses

- Pricing: Stripe Billing pricing for recurring payments, Invoicing pricing for invoice-only setup

[Stripe Billing pricing](https://stripe.com/billing/pricing)

[Invoicing pricing](https://stripe.com/invoicing/pricing)

When you’re ready to offer your customers a way to self-serve their billing accounts, you can set up the customer portal. Use it to let your customers manage their billing information, subscriptions, and invoices as your business scales.

Stripe hosts the customer portal, which means you can use it even if you don’t have a website. You can also link users to it from an existing site or Stripe integration.

First, you need a Stripe account. Register now.

[Register now](https://dashboard.stripe.com/register/)

[Create a product](#create-product)

## Create a product

To create a product in the Dashboard:

- Go to More > Product catalog.

- Click +Add product.

- Enter the Name of your product.

- (Optional) Add a Description. The description appears at checkout, on the customer portal, and in quotes.

[customer portal](/customer-management)

[quotes](/quotes)

- (Optional) Add an Image of your product. Use a JPEG or PNG file that’s smaller than 2MB. The image appears at checkout.

- (Optional) If you’re using Stripe Tax, select a Tax code for your product. See tax codes for more information about the appropriate category for your product.

[Stripe Tax](/tax)

[tax codes](/tax/tax-codes)

- (Optional) Enter a Statement descriptor. This descriptor overrides any account descriptors for recurring payments. Choose something that your customers would recognize on a bank statement.

- (Optional) Enter a Unit label. This describes how you sell your product. For example, if you charge by the seat, enter “seat” so the line item includes “per seat” for the price. Unit labels appear at checkout, and in invoices, receipts, and the customer portal.

[customer portal](/billing/subscriptions/customer-portal)

For more details about get started with products and prices.

[get started with products and prices](/products-prices/getting-started)

[Set up the customer portal](#set-up-customer-portal)

## Set up the customer portal

- Activate a customer portal link  On the customer portal configuration page, click Activate link in the Ways to get started section.

Activate a customer portal link  On the customer portal configuration page, click Activate link in the Ways to get started section.

[customer portal configuration](https://dashboard.stripe.com/settings/billing/portal)

- Configure the portal  Go to the customer portal configuration page and select your configuration options. Learn more about configuration options.

Configure the portal  Go to the customer portal configuration page and select your configuration options. Learn more about configuration options.

[customer portal configuration](https://dashboard.stripe.com/settings/billing/portal)

[configuration options](/customer-management/configure-portal)

- Share the portal login link  Add the link you activated to your site, or send it directly to your customers. They can log in to the portal with their email address and a one-time passcode.Make sure your customers have an email set. If multiple customers have the same email address, Stripe selects the most recently created customer that has both that email and an active subscription.For security purposes:Customers can’t update their email address through this link.If a customer doesn’t receive a one-time passcode after clicking the login link, make sure their email address matches the email address of an existing customer. To check, enter the email address in the search bar of your Stripe dashboard.

Share the portal login link  Add the link you activated to your site, or send it directly to your customers. They can log in to the portal with their email address and a one-time passcode.

Make sure your customers have an email set. If multiple customers have the same email address, Stripe selects the most recently created customer that has both that email and an active subscription.

[email](/api/customers/object#customer_object-email)

For security purposes:

- Customers can’t update their email address through this link.

- If a customer doesn’t receive a one-time passcode after clicking the login link, make sure their email address matches the email address of an existing customer. To check, enter the email address in the search bar of your Stripe dashboard.

[Stripe dashboard](https://dashboard.stripe.com/)

[OptionalCustomize branding](#branding)

## OptionalCustomize branding

[OptionalPrefill customer email](#url-parameters)

## OptionalPrefill customer email
