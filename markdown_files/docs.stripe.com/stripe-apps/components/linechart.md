htmlLineChart | Stripe Documentation[Skip to content](#main-content)LineChart[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Flinechart)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Flinechart)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# LineChart

A line chart visualizes data as a series of data points connected into a line.To add the LineChart component to your app:

`import {LineChart} from '@stripe/ui-extension-sdk/ui';`The following shows a preview of the LineChart UI component:

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

<LineChart data={sales} x="date" y="sold" />`### Props

PropTypeDescriptiondataRequired`Record<string | number, any>[]`The data used to generate the chart.xRequired`Accessor`The property or accessor for the point on the x axis.yRequired`Accessor`The property or accessor for the point on the y axis.axis`"none" | "x" | "y" | "both"`Determines whether to render labels and ticks for each axis.color`string | number | Omit<Channel, "range">`Groups data by color based on a property or accessor.grid`"none" | "x" | "y" | "both"`Determines whether to render grid lines for each axis.legend`boolean`Determines whether to render the legend (when more than one item is present).tooltip`boolean`Determines whether to render a tooltip when hovering over the chart.z`Accessor`Groups data based on a property or accessor.## Using color

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

<LineChart data={sales} x="date" y="sold" color="product" />`## Axis and value formatting

Instead of passing a string for an axis value, you can add richer formatting by passing an object including the value, label and/or format properties.

PropertyTypeDescription`value``string | number`The property name in the data set. Required.`label``string`The display text for the axis.`format``object`Format a number with one of the[supported currency codes](https://raw.githubusercontent.com/unicode-org/cldr/main/common/validity/currency.xml)for example`{currency: 'USD'}`, or a[supported unit](https://tc39.es/proposal-unified-intl-numberformat/section6/locales-currencies-tz_proposed_out.html#sec-issanctionedsimpleunitidentifier)such as`{unit: 'minute'}`. You can also create a compound unit with`-per-`in between, such as`{unit: 'megabyte-per-hour'}`.`<LineChart
  data={[
    {
      date: 'January',
      sold: 10,
    },
    {
      date: 'February',
      sold: 41,
    },
    {
      date: 'March',
      sold: 22,
    },
    {
      date: 'April',
      sold: 38,
    },
  ]}
  x="date"
  y={{value: 'sold', label: 'Price', format: {currency: 'USD'}}}
/>`## Domain

To set the minimum and maximum values of an axis, use the domain prop. For example, if you always want the y axis to go from 0 to 10 (rather than automatically adjusting to the data provided), add the domain property to your configuration:

`const sales = [
  {
    date: 'Jan',
    sold: 1,
  },
  {
    date: 'Feb',
    sold: 4,
  },
  {
    date: 'Mar',
    sold: 2,
  },
  {
    date: 'Apr',
    sold: 3,
  },
];

<LineChart
  data={sales}
  x="date"
  y={{value: 'sold', label: 'Sold', domain: [0, 10]}}
/>`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Using color](#using-color)[Axis and value formatting](#axis-and-value-formatting)[Domain](#domain)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`