htmlViewports reference | Stripe Documentation[Skip to content](#main-content)Viewports[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Freference%2Fviewports)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Freference%2Fviewports)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# Viewports reference

A list of available viewports for Stripe Apps and how your end users see them.A viewport specifies the page in the Dashboard where your view can appear. A viewport can provide an environment.objectContext object that allows you to receive context on a current page’s Stripe object. For more information, see Access Stripe objects in the Dashboard.

Available viewports for your UI extension:

Viewport IDPageURLsObject type`stripe.dashboard.payment.list`Payments page`dashboard.stripe.com/payments``null``stripe.dashboard.payment.detail`Payment details page`dashboard.stripe.com/payments/:id``charge`,`payment_intent``stripe.dashboard.customer.list`Customers page`dashboard.stripe.com/customers``null``stripe.dashboard.customer.detail`Customer details page`dashboard.stripe.com/customers/:id``customer``stripe.dashboard.invoice.list`Invoices page`dashboard.stripe.com/invoices``null``stripe.dashboard.invoice.detail`Invoice details page`dashboard.stripe.com/invoices/:id``invoice``stripe.dashboard.product.list`Products page`dashboard.stripe.com/products/``null``stripe.dashboard.product.detail`Product details page`dashboard.stripe.com/products/:id``product``stripe.dashboard.subscription.list`Subscriptions page`dashboard.stripe.com/subscriptions``null``stripe.dashboard.subscription.detail`Subscription details page`dashboard.stripe.com/subscriptions/:id``subscription``stripe.dashboard.payment-link.list`Payment Links page`dashboard.stripe.com/payment-links``null``stripe.dashboard.payment-link.detail`Payment Link details page`dashboard.stripe.com/payment-links/:id``payment_link``stripe.dashboard.home.overview`Dashboard homepage`dashboard.stripe.com/dashboard``null``stripe.dashboard.balance.overview`Balance page`dashboard.stripe.com/balance/overview``null``stripe.dashboard.billing.overview`Billing page`dashboard.stripe.com/billing``null``stripe.dashboard.report.overview`Reports > Overview page`dashboard.stripe.com/reports/hub``null``stripe.dashboard.revenue-recognition.overview`Revenue Recognition page`dashboard.stripe.com/revenue-recognition``null``stripe.dashboard.tax-report.overview`Reports > Tax page`dashboard.stripe.com/tax/reporting``null``stripe.dashboard.drawer.default`Available across all pages (For more information, see[Dashboard-wide availability](#dashboard-wide-availability))`null``settings`App settings page (For more information, learn how to[add an app settings page](/stripe-apps/app-settings).)`null`## Application availability

You can make your application available across all pages or specific to a single page in the Dashboard.

### Dashboard-wide availability

If your app specifies a view for the stripe.dashboard.drawer.default viewport, this view appears on every page in the Dashboard except for where you have defined page-specific views.

For example, if the ui_extension.views field in your app’s stripe-app.json manifest is as follows:

stripe-app.json`{
  "id": "com.example.app",
  "version": "1.2.3",
  "name": "Example App",
  "icon": "./example_icon_32.png",
  "permissions": [
    {
      "permission": "customer_read",
      "purpose": "Receive access to the customer information"
    }
  ],
  "ui_extension": {
    "views": [
      {
        "viewport": "stripe.dashboard.customer.detail",
        "component": "CustomerView"
      },
      {
        "viewport": "stripe.dashboard.drawer.default",
        "component": "EverywhereElseView"
      }
    ]
  }
}`“CustomerView” would appear when the application is open on the Customer details page, and “EverywhereElseView” would appear on every other page in the Dashboard.

The stripe.dashboard.drawer.default view doesn’t receive objectContext data the way that a page-specific view does. If your app needs to access information like the id of an invoice shown on an “Invoice details” page, you need to create a view that uses the stripe.dashboard.invoice.detail viewport. For more information, see Page-specific availability.

### Page-specific availability

Page-specific views relate to the current page the user is viewing, and allow apps to receive additional context about the page through the environment property. For more information, see Access Stripe objects in the Dashboard.

For example, if your app has a view for the stripe.dashboard.product.detail viewport, when a user opens your app on the Product details page, that view appears in the app.

If your app doesn’t have either a page-specific view for the current page or an app-specific default view, the drawer displays a generic default view that shows the user how to access the app.

For example, if your app has two views on page-specific viewports, shown in the app manifest below:

stripe-app.json`{
  "id": "com.example.app",
  "version": "1.2.3",
  "name": "Example App",
  "icon": "./example_icon_32.png",
  "permissions": [
    {
      "permission": "customer_read",
      "purpose": "Receive access to the customer information"
    }
  ],
  "ui_extension": {
    "views": [
      {
        "viewport": "stripe.dashboard.customer.detail",
        "component": "CustomerView"
      },
      {
        "viewport": "stripe.dashboard.product.detail",
        "component": "ProductView"
      }
    ]
  }
}`When the end user opens your app on the Dashboard homepage, the application displays links to the Customers and Products pages. If the user then navigates to the Customers page, the app displays a message prompting them to select a customer to see related information in your app.

## See also

- [Design your app](/stripe-apps/design)
- [How UI extensions work](/stripe-apps/how-ui-extensions-work)
- [Permissions reference](/stripe-apps/reference/permissions)
- [UI extension SDK reference](/stripe-apps/reference/extensions-sdk-api)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`