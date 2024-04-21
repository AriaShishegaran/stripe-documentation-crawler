htmlCreate an embeddable pricing table | Stripe Documentation[Skip to content](#main-content)Create a pricing table[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Fpricing-table)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fno-code%2Fpricing-table)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/no-code)[Find your use case](/docs/no-code/get-started)[No-code payments](#)[Customer experience](#)
NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[No-code](/docs/no-code)Customer experience# Create an embeddable pricing table

Display a pricing table on your website and take customers directly to Stripe Checkout.- Compatible with:Subscriptions,[customer portal](/billing/subscriptions/customer-portal)
- Requires:Stripe account, website
- Good for:SaaS businesses, individual creators, e-commerce businesses
- Pricing:[Pay-as-you-go](https://stripe.com/pricing),[Stripe Billing pricing](https://stripe.com/billing/pricing)

You can use the Stripe Dashboard to create a table that displays different subscription pricing levels to your customers. You don’t need to write any custom code to create or embed a pricing table. This guide describes how to:

- Use the Stripe Dashboard to configure the UI component
- Copy the generated code from the Dashboard
- Embed the code on your website to show your customers pricing information and take them to a checkout page

[Overview](#overview)![The pricing table is an embedded UI that displays pricing information and takes customers to checkout.](https://b.stripecdn.com/docs-statics-srv/assets/pricing-table-embed.b27a06fcd84b57a8866a8b4b62323fdc.png)

Embed a pricing table on your website to display pricing details and convert customers to checkout.

A pricing table is an embeddable UI that:

- Displays[pricing information](/products-prices/pricing-models)and takes customers to a prebuilt checkout flow. The checkout flow uses[Stripe Checkout](/payments/checkout)to complete the purchase.
- Supports common subscription business models like[flat-rate](/products-prices/pricing-models#flat-rate),[per-seat](/products-prices/pricing-models#per-seat),[tiered pricing](/products-prices/pricing-models#tiered-pricing), and free trials.
- Lets you configure, customize, and update product and pricing information directly in the Dashboard, without needing to write any code.
- Embeds into your website with a`<script>`tag and web component. Stripe automatically generates the tag. You copy and paste it into your website’s code.

The diagram below summarizes how the customer goes from viewing a pricing table to completing checkout.

[Create pricing table](#Create)1. In the Dashboard, go toMore>Product catalog>[pricing tables](https://dashboard.stripe.com/pricing-tables).
2. Click+Create pricing table.
3. Add products relevant to your customers (up to four per pricing interval). Optionally, include a free trial.
4. Adjust the look and feel inDisplay settings. You can highlight a specific product and customize the language, colors, font, and button design.
5. Configure payment settings by clickingContinue. Customize what customers see on the payments page and whether to display a confirmation page or redirect customers back to your site after a successful purchase.
6. Configure the[customer portal](/no-code/customer-portal)by clickingContinue.
7. ClickCopy codeto copy the generated code and[embed it into your website](/no-code/pricing-table#embed).

![Customizing a pricing table](https://b.stripecdn.com/docs-statics-srv/assets/create-pricing-table-step-1.45ac9351d8f043a0a63554b89b2cedfc.png)

Customize your pricing table

![Configure payment settings](https://b.stripecdn.com/docs-statics-srv/assets/create-pricing-table-step-2.dab4cc0d56704ffeb6fb8eeb289ace4d.png)

Configure payment settings

[Embed pricing table](#embed)After creating a pricing table, Stripe automatically returns an embed code composed of a <script> tag and a <stripe-pricing-table> web component. Click the Copy code button to copy the code and paste it into your website.

![Pricing table detail page](https://b.stripecdn.com/docs-statics-srv/assets/pricing-table-detail-page.dee9a93d69e802759dabd0e4ce62f1bd.png)

Copy the pricing table’s code and embed it on your website.

If you’re using HTML, paste the embed code into the HTML. If you’re using React, include the script tag in your index.html page to mount the <stripe-pricing-table> component.

CautionThe pricing table uses your account’s publishable API key. If you revoke the API key, you need to update the embed code with your new publishable API key.

pricing-page.html[HTML](#)`<body>
  <h1>We offer plans that help any business!</h1>
  <!-- Paste your embed code script here. -->
  <script
    async
    src="https://js.stripe.com/v3/pricing-table.js">
  </script>
  <stripe-pricing-table
    pricing-table-id='{{PRICING_TABLE_ID}}'
    publishable-key="pk_test_VOOyyYjgzqdm8I3SrBqmh9qY"
  >
  </stripe-pricing-table>
</body>`[Track subscriptions](#track-subscriptions)When a customer purchases a subscription, you’ll see it on the subscriptions page in the Dashboard.

### Handle fulfillment with the Stripe API

The pricing table component uses Stripe Checkout to render a prebuilt, hosted payment page. When a payment is completed using Checkout, Stripe sends the checkout.session.completed webhook that you can use for fulfillment and reconciliation. Make sure to listen to additional webhooks if you enable payment methods like bank debits or vouchers, which can take 2-14 days to confirm the payment. For more information, see the guide for fulfilling orders after a customer pays.

The <stripe-pricing-table> web component supports setting the client-reference-id property. When the property is set, the pricing table passes it to the Checkout Session’s client_reference_id attribute to help you reconcile the Checkout Session with your internal system. This can be an authenticated user ID or a similar string. client-reference-id can be composed of alphanumeric characters, dashes, or underscores, and be any value up to 200 characters. Invalid values are silently dropped and your pricing table will continue to work as expected.

CautionSince the pricing table is embedded on your website and is accessible to anyone, check that client-reference-id does not include sensitive information or secrets, such as passwords or API keys.

pricing-page.html[HTML](#)`<body>
  <h1>We offer plans that help any business!</h1>
  <!-- Paste your embed code script here. -->
  <script
    async
    src="https://js.stripe.com/v3/pricing-table.js">
  </script>
  <stripe-pricing-table
    pricing-table-id='{{PRICING_TABLE_ID}}'
    publishable-key="pk_test_VOOyyYjgzqdm8I3SrBqmh9qY"
    client-reference-id="{{CLIENT_REFERENCE_ID}}"
  >
  </stripe-pricing-table>
</body>`[OptionalAdd product marketing features](#product-marketing-features)[OptionalAdd a custom call-to-action](#custom-cta)[OptionalPass the customer email](#customer-email)[OptionalPass an existing customer](#customer-session)[OptionalCustomize the post-purchase experience](#post-purchase-experience)[OptionalUpdate pricing table](#update)[OptionalConfigure free trials](#free-trials)[OptionalContent Security Policy](#csp)[OptionalLet customers manage their subscriptionsNo code](#customer-portal)[OptionalPresent local currencies](#price-localization)[OptionalAdd custom fields](#custom-fields)[Limitations](#limitations)- Business models—The pricing table supports common subscription business models like flat-rate, per-seat, tiered pricing, and trials. Other[advanced pricing models](/billing/subscriptions/usage-based/pricing-models#advanced)aren’t supported.
- Product and price limits—You can configure the pricing table to display a maximum of four products, with up to three prices per product. You can only configure three unique pricing intervals across all products.
- Account creation—The pricing table call-to-action takes customers directly to checkout. It doesn’t currently support adding an intermediate step (for example, asking the customer to create an account on your website before checking out).
- Rate limit—The pricing table has a[rate limit](/rate-limits)of up to 50 read operations per second. If you have multiple pricing tables, the rate limit is shared.
- Checkout redirect—The pricing table can’t redirect customers to checkout if your website provider sandboxes the embed code in an iframe without the`allow-top-navigation`attribute enabled. Contact your website provider to enable this setting.
- Testing the pricing table locally—The pricing table requires a website domain to render. To test the pricing table locally, run a local HTTP server to host your website’s`index.html`file over the`localhost`domain. To run a local HTTP server, use Python’s[SimpleHTTPServer](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server#running_a_simple_local_http_server)or the[http-server](https://www.npmjs.com/package/http-server)npm module.

[Limit customers to one subscription](#limit-subscriptions)You can redirect customers that already have a subscription to the customer portal or your website to manage their subscription. Learn more about limiting customers to one subscription.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Overview](#overview)[Create pricing table](#Create)[Embed pricing table](#embed)[Track subscriptions](#track-subscriptions)[Limitations](#limitations)[Limit customers to one subscription](#limit-subscriptions)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`