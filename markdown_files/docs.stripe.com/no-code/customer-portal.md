htmlSet up the customer portal | Stripe Documentation[Skip to content](#main-content)Set up customer portal[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Fcustomer-portal)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Fcustomer-portal)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/no-code)[Find your use case](/docs/no-code/get-started)[No-code payments](#)[Customer experience](#)
NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[No-code](/docs/no-code)Customer experience# Set up the customer portal

Let your customers manage their own billing accounts with a portal that Stripe hosts.- Stripe compatibility:Payment Links, Checkout, pricing table, customer portal
- Requires:Stripe account
- Good for:SaaS businesses, individual creators, e-commerce businesses
- Pricing:[Stripe Billing pricing](https://stripe.com/billing/pricing)for recurring payments,[Invoicing pricing](https://stripe.com/invoicing/pricing)for invoice-only setup

When you’re ready to offer your customers a way to self-serve their billing accounts, you can set up the customer portal. Use it to let your customers manage their billing information, subscriptions, and invoices as your business scales.

Stripe hosts the customer portal, which means you can use it even if you don’t have a website. You can also link users to it from an existing site or Stripe integration.

First, you need a Stripe account. Register now.

[Create a product](#create-product)To create a product in the Dashboard:

1. Go toMore>Product catalog.
2. Click+Add product.
3. Enter theNameof your product.
4. (Optional)Add aDescription. The description appears at checkout, on the[customer portal](/customer-management), and in[quotes](/quotes).
5. (Optional)Add anImageof your product. Use a JPEG or PNG file that’s smaller than 2MB. The image appears at checkout.
6. (Optional)If you’re using[Stripe Tax](/tax), select aTax codefor your product. See[tax codes](/tax/tax-codes)for more information about the appropriate category for your product.
7. (Optional)Enter aStatement descriptor. This descriptor overrides any account descriptors for recurring payments. Choose something that your customers would recognize on a bank statement.
8. (Optional)Enter aUnit label. This describes how you sell your product. For example, if you charge by the seat, enter “seat” so the line item includes “per seat” for the price. Unit labels appear at checkout, and in invoices, receipts, and the[customer portal](/billing/subscriptions/customer-portal).

For more details about get started with products and prices.

[Set up the customer portal](#set-up-customer-portal)1. Activate a customer portal link  On the customer portal configuration page, click Activate link in the Ways to get started section.


2. Configure the portal  Go to the customer portal configuration page and select your configuration options. Learn more about configuration options.


3. Share the portal login link  Add the link you activated to your site, or send it directly to your customers. They can log in to the portal with their email address and a one-time passcode.

Make sure your customers have an email set. If multiple customers have the same email address, Stripe selects the most recently created customer that has both that email and an active subscription.

For security purposes:

  - Customers can’t update their email address through this link.
  - If a customer doesn’t receive a one-time passcode after clicking the login link, make sure their email address matches the email address of an existing customer. To check, enter the email address in the search bar of your[Stripe dashboard](https://dashboard.stripe.com/).



[OptionalCustomize branding](#branding)[OptionalPrefill customer email](#url-parameters)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a product](#create-product)[Set up the customer portal](#set-up-customer-portal)Products Used[Payments](/payments)[Billing](/billing)[Tax](/tax)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`