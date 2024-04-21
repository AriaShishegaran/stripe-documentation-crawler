htmlBox | Stripe Documentation[Skip to content](#main-content)Box[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fbox)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fbox)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# Box

Use boxes to wrap other components and add custom styles and layouts.To add the Box component to your app:

`import {Box} from '@stripe/ui-extension-sdk/ui';`Boxes are block-level elements, equivalent to a div HTML element. They support custom styles. If you want to render or style inline elements, see the Inline component.

`<Box
  css={{
    padding: 'xxlarge',
    color: 'secondary',
    background: 'container',
    borderRadius: 'small',
  }}
>
  This is a box.
</Box>`## Nesting boxes

For some components, you can use a Box to manage the layout and spacing of their children. For example, nest a Box inside an AccordionItem to add padding:

`<Accordion>
  <AccordionItem title="Apples">
    <Box css={{padding: 'xlarge'}}>Accordion contents</Box>
  </AccordionItem>
  <AccordionItem title="Bananas">
    <Box css={{padding: 'xlarge'}}>Accordion contents</Box>
  </AccordionItem>
  <AccordionItem title="Peaches" subtitle="A subtitle can be provided">
    <Box css={{padding: 'xlarge'}}>Accordion contents</Box>
  </AccordionItem>
</Accordion>`Or nest a Box inside a Button to organize the layout of a label and icon:

`<Button>
  <Icon name="mobile" size="xsmall" />
  <Inline>New messages</Inline>
</Button>
<Badge type="positive">
  <Icon name="mobile" size="xsmall" />
  New messages
</Badge>`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Nesting boxes](#nesting-boxes)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`