htmlTable | Stripe Documentation[Skip to content](#main-content)Table[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ftable)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ftable)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# Table

Display a table using the Table component.To add the Table component to your app:

`import {Table, TableBody, TableCell, TableFooter, TableHead, TableHeaderCell, TableRow} from '@stripe/ui-extension-sdk/ui';`The following shows a preview of a Table component with a header, several rows of data, and a footer:

`<Table>
  <TableHead>
    <TableRow>
      <TableHeaderCell>Charge type</TableHeaderCell>
      <TableHeaderCell>Amount</TableHeaderCell>
    </TableRow>
  </TableHead>
  <TableBody>
    <TableRow>
      <TableCell>Setup fee</TableCell>
      <TableCell>$95.00</TableCell>
    </TableRow>
    <TableRow>
      <TableCell>Maintenance fee</TableCell>
      <TableCell>$50.45</TableCell>
    </TableRow>
    <TableRow>
      <TableCell>Extra storage space (per GB)</TableCell>
      <TableCell>$5.95</TableCell>
    </TableRow>
    <TableRow>
      <TableCell>Premium features</TableCell>
      <TableCell>$109.00</TableCell>
    </TableRow>
  </TableBody>
  <TableFooter>
    <TableRow>
      <TableCell>
        <Inline css={{font: 'bodyEmphasized'}}>Total</Inline>
      </TableCell>
      <TableCell>
        <Inline css={{font: 'bodyEmphasized'}}>$260.40</Inline>
      </TableCell>
    </TableRow>
  </TableFooter>
</Table>`## Sub-components

## TableBody

The TableBody component contains the rows and cells in a table.

## TableCell

The TableCell component contains one unit of information in a table corresponding to a row and column.

This component has no props.## TableFooter

The TableFooter component summarizes or aggregates the columns of information contained in a table.

## TableHead

The TableHead component describes the columns of information contained in a table.

## TableHeaderCell

The TableHeaderCell component describes one column of information in a table.

This component has no props.## TableRow

The TableRow component is an entry in a table composed of cells containing information for each column.

## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Sub-components](#sub-components)[TableBody](#tablebody)[TableCell](#tablecell)[TableFooter](#tablefooter)[TableHead](#tablehead)[TableHeaderCell](#tableheadercell)[TableRow](#tablerow)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`