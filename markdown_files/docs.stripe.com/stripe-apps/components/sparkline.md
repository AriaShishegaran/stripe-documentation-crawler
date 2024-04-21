htmlSparkline | Stripe Documentation[Skip to content](#main-content)Sparkline[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fsparkline)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fsparkline)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# Sparkline

A type of line chart to display data succinctly as a simple line.To add the Sparkline component to your app:

`import {Sparkline} from '@stripe/ui-extension-sdk/ui';`The following shows a preview of the Sparkline UI component:

`const sales = [
  {
    date: 'Jan',
    sold: 1
  },
  {
    date: 'Feb',
    sold: 4
  },
  {
    date: 'Mar',
    sold: 2
  },
  {
    date: 'Apr',
    sold: 3
  }
];

<Sparkline data={sales} x="date" y="sold" />`### Props

PropTypeDescriptiondataRequired`Record<string | number, any>[]`The data used to generate the chart.xRequired`Accessor`The property or accessor for the point on the x axis.yRequired`Accessor`The property or accessor for the point on the y axis.color`string | number | Omit<Channel, "range">`Groups data by color based on a property or accessor.tooltip`boolean`Determines whether to render a tooltip when hovering over the chart.z`Accessor`Groups data based on a property or accessor.## Using color

The color channel groups data:

`const sales = [
  {
    date: 'Jan',
    sold: 1,
    product: 'tables'
  },
  {
    date: 'Jan',
    sold: 2,
    product: 'chairs'
  },
  {
    date: 'Feb',
    sold: 4,
    product: 'tables'
  },
  {
    date: 'Feb',
    sold: 6,
    product: 'chairs'
  },
  {
    date: 'Mar',
    sold: 2,
    product: 'tables'
  },
  {
    date: 'Mar',
    sold: 4,
    product: 'chairs'
  },
  {
    date: 'Apr',
    sold: 7,
    product: 'tables',
  },
  {
    date: 'Apr',
    sold: 9,
    product: 'chairs',
  },
];

<Sparkline data={sales} x="date" y="sold" color="product" />`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Using color](#using-color)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`