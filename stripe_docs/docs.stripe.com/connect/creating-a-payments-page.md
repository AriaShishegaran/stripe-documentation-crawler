# Create a payments page

[](https://checkout.stripe.dev/)

Customize logo, images, and colors.

Built-in support for Apple Pay, and Google Pay.

View the demo to see a hosted example.

[View the demo](https://checkout.stripe.dev/)

[Accept a payment](#accept-a-payment)

## Accept a payment

Refer to your platform profile to determine if either direct charges or destination charges is right for your business.

[platform profile](https://dashboard.stripe.com/connect/settings/profile)

[direct charges](/connect/direct-charges)

[destination charges](/connect/destination-charges)

In this example, the platform is a home-rental marketplace that needs to create payments for homeowners who rent their properties. You can use destination charges in other applications as well.

A Checkout Session controls what your customer sees in the embeddable payment form such as line items, the order amount and currency, and acceptable payment methods.

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

On your server, make the following call to Stripe’s API. After creating a Checkout Session, redirect your customer to the URL returned in the response.

[URL](/api/checkout/sessions/object#checkout_session_object-url)

[https://example.com/success](https://example.com/success)

[https://example.com/failure](https://example.com/failure)

- payment_intent_data[transfer_data][destination] - This argument indicates that this is a destination charge. A destination charge means the charge is processed on the platform and then the funds are immediately and automatically transferred to the connected account’s pending balance. For our home-rental example, we want to build an experience where the customer pays through the platform and the homeowner gets paid by the platform.

[destination charge](/connect/destination-charges)

- line_items - This argument represents the items the customer is purchasing. The items are displayed in the Stripe-hosted user interface.

- success_url - This argument redirects a user after they complete a payment.

- cancel_url  - This argument redirects a user after they click cancel.

- payment_intent_data[application_fee_amount] - This argument specifies the amount your platform plans to take from the transaction. The full charge amount is immediately transferred from the platform to the connected account that’s specified by transfer_data[destination] after the charge is captured. The application_fee_amount is then transferred back to the platform, and the Stripe fee is deducted from the platform’s amount.

When performing destination charges, Checkout uses the brand settings of your platform account. See the Customize branding section for more information.

[Customize branding](/connect/creating-a-payments-page?platform=web&ui=stripe-hosted#branding)

This Session creates a destination charge. If you need to control the timing of transfers or need to transfer funds from a single payment to multiple parties, use separate charges and transfers instead.

After the payment is completed, you’ll need to handle any fulfillment necessary on your end. A home-rental company that requires payment upfront, for instance, would connect the homeowner with the renter after a successful payment.

Don’t rely on the redirect to the success_url parameter alone for fulfilling purchases as:

- Malicious users could directly access the success_url without paying and gain access to your goods or services.

- Customers may not always reach the success_url after a successful payment. It is possible they close their browser tab before the redirect occurs.

[Customers](/api/customers)

Configure a webhook endpoint (for events from your account) in your dashboard.

[webhook](/webhooks)

[in your dashboard](https://dashboard.stripe.com/account/webhooks)

Then create an HTTP endpoint on your server to monitor for completed payments to enable your sellers or service providers to fulfill purchases. Make sure to replace the endpoint secret key (whsec_...) in the example with your key.

[https://dashboard.stripe.com/apikeys](https://dashboard.stripe.com/apikeys)

[https://stripe.com/docs/webhooks#verify-events](https://stripe.com/docs/webhooks#verify-events)

Learn more in our fulfillment guide for Checkout.

[fulfillment guide for Checkout](/payments/checkout/fulfill-orders)

Use the Stripe CLI to test webhooks locally.

- First, install the Stripe CLI on your machine if you haven’t already.

First, install the Stripe CLI on your machine if you haven’t already.

[install the Stripe CLI](/stripe-cli#install)

- Then, to log in run stripe login in the command line, and follow the instructions.

Then, to log in run stripe login in the command line, and follow the instructions.

- Finally, to allow your local host to receive a simulated event on your connected account run stripe listen --forward-to localhost:{PORT}/webhook in one terminal window, and run stripe trigger --stripe-account={{CONNECTED_STRIPE_ACCOUNT_ID}} checkout.session.completed (or trigger any other supported event) in another.

Finally, to allow your local host to receive a simulated event on your connected account run stripe listen --forward-to localhost:{PORT}/webhook in one terminal window, and run stripe trigger --stripe-account={{CONNECTED_STRIPE_ACCOUNT_ID}} checkout.session.completed (or trigger any other supported event) in another.

[supported event](https://github.com/stripe/stripe-cli/wiki/trigger-command#supported-events)

As the settlement merchant on charges, your platform is responsible for disputes. Make sure you understand the best practices for responding to disputes.

[settlement merchant](/connect/destination-charges#settlement-merchant)

[best practices](/disputes/responding)

[Create a subscription](#subscriptions)

## Create a subscription

You can create a recurring payment on a connected account with subscriptions. Subscriptions are created with direct charges. Optionally, specify an application_fee_percent to direct a percentage of each invoice payment to your platform.

[subscriptions](/connect/subscriptions)

[Subscriptions](/billing/subscriptions/creating)

[application_fee_percent](/connect/subscriptions#collect-fees)

[invoice](/api/invoices)

The Checkout page uses the brand settings of the connected account, including its business name, icon, logo, and color. See the Customize branding section for more information.

[Customize branding](#branding)

You can include a combination of one-time line items and recurring plans in a Checkout Session. If specified, application_fee_percent will apply to both one-time and recurring items.

A Checkout Session controls what your customer sees in the Stripe-hosted payment page such as line items, the order amount and currency, and acceptable payment methods.

Add a checkout button to your website that calls a server-side endpoint to create a Checkout Session.

On your server, make the following call to the Stripe API. After creating a Checkout Session, redirect your customer to the URL returned in the response.

[URL](/api/checkout/sessions/object#checkout_session_object-url)

[https://example.com/success](https://example.com/success)

[https://example.com/cancel](https://example.com/cancel)

[Customize branding](#branding)

## Customize branding

Your platform and connected accounts with access to the Stripe Dashboard can use the Branding settings to customize branding on the payments page. When performing destination charges, Checkout uses the brand settings of the platform account. For direct charges, and destination charges with on_behalf_of, Checkout uses the brand settings of the connected account. Platforms can configure the brand settings of connected accounts that have access to the Express Dashboard or who don’t have access to a Stripe-hosted dashboard using the Accounts API.

[Branding settings](https://dashboard.stripe.com/account/branding)

[Accounts](/api/accounts/object#account_object-settings-branding)

The account update API accepts the following parameters for branding:

[account update](/api/accounts/update)

- icon - Displayed next to the business name in the header of the Checkout page.

- logo- If specified, displayed instead of the icon and business name in the header of the Checkout page.

- primary_color - Used as the background color on the Checkout page.

- secondary_color - Used as the button color on the Checkout page.

## Enable payment methods

View your payment methods settings and enable the payment methods you want to support. Card payments, Google Pay, and Apple Pay are enabled by default but you can enable and disable payment methods as needed.

[payment methods settings](https://dashboard.stripe.com/settings/payment_methods)

Before the payment form is displayed, Stripe evaluates the currency, payment method restrictions, and other parameters to determine the list of supported payment methods. Payment methods that increase conversion and that are most relevant to the currency and customer’s location are prioritized. Lower priority payment methods are hidden in an overflow menu.
