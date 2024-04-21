htmlChip | Stripe Documentation[Skip to content](#main-content)Chip[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fchip)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Fchip)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# Chip

Use chips to display and allow users to manipulate values.To add the Chip component to your app:

`import {Chip, ChipList} from '@stripe/ui-extension-sdk/ui';`This is a preview of several Chip components in a ChipList component with different property configurations:

`<ChipList>
  <Chip
    label="Currency"
    value="USD"
    onDropdown={() => {
      alert('Dropdown function triggered');
    }}
    onClose={() => {
      alert('Close function triggered');
    }}
  />
  <Chip
    label="Status"
    value="Succeeded"
    onDropdown={() => {
      alert('Dropdown function triggered');
    }}
    onClose={() => {
      alert('Close function triggered');
    }}
  />
  <Chip
    label="Amount"
    onAddSuggestion={() => {
      alert('Add Amount suggestion');
    }}
  />
  <Chip
    label="Date"
    onAddSuggestion={() => {
      alert('Add Date suggestion');
    }}
  />
</ChipList>`### Props

PropTypelabel`string`onAddSuggestion`(() => void)`onClose`(() => void)`onDropdown`(() => void)`value`string | string[]`## Suggested chip

To suggest to the user with a plus icon that they add something represented by a chip, pass a callback function to the onAddSuggestion property.

`<Chip
  label="Date"
  onAddSuggestion={() => {
    alert('Suggestion function triggered');
  }}
/>`## Chip with dropdown

If you want to allow the user to edit the value of a chip after they’ve made their initial selection, provide an onDropdown callback function to open a selection interface needed for making edits.

`import {useState} from 'react';
import {Box, Chip} from '@sail/ui';

const WithDropdown = () => {
  const [open, setOpen] = useState(false);
  return (
    <>
      <Chip
        label="Status"
        value="Succeeded"
        onDropdown={() => setOpen(!open)}
        onClose={() => {
          alert('Close function triggered');
        }}
      />
      {open && (
        <Box
          css={{
            font: 'caption',
            borderRadius: 'medium',
            background: 'container',
            margin: 'small',
            padding: 'medium',
            color: 'secondary',
          }}
        >
          Dropdown contents
        </Box>
      )}
    </>
  );
};`## Representing multiple values

When you populate the Chip component’s value property with an array of values, they’re listed within the chip.

`<Chip
  label="Status"
  value={['Refunded', 'Succeeded']}
  onDropdown={() => {
    alert('Dropdown function triggered');
  }}
  onClose={() => {
    alert('Close function triggered');
  }}
/>`## Presenting chips in a list

In many cases, chips aren’t presented on their own—they’re alongside other chips. The ChipList component handles the appropriate spacing and wrapping of chips in a list, and also provides for convenient keyboard navigation of chips using the right and left arrow keys.

`<ChipList>
  <Chip
    label="Currency"
    value="USD"
    onDropdown={() => {
      alert('Dropdown function triggered');
    }}
    onClose={() => {
      alert('Close function triggered');
    }}
  />
  <Chip
    label="Status"
    value="Succeeded"
    onDropdown={() => {
      alert('Dropdown function triggered');
    }}
    onClose={() => {
      alert('Close function triggered');
    }}
  />
  <Chip
    value="jenny.rosen@stripe.com"
    onClose={() => {
      alert('Closed jenny.rosen');
    }}
  />
  <Chip
    value="usr_0As2kXSWDS1lTZsH5agB"
    onClose={() => {
      alert('Closed usr_0As2kXSWDS1lTZsH5agB');
    }}
  />
  <Chip
    label="Amount"
    onAddSuggestion={() => {
      alert('Add Amount suggestion');
    }}
  />
  <Chip
    label="Date"
    onAddSuggestion={() => {
      alert('Add Date suggestion');
    }}
  />
</ChipList>`## Non-closeable chip

When a Chip represents a required value, it can be useful to present a chip without an add or cancel icon. Exclude the onAddSuggestion and onClose callbacks to present users with a non-closeable chip.

`<ChipList>
  <Chip label="Amount" value="$10" />
  <Chip
    label="Age"
    value="18-24"
    onDropdown={() => {
      alert('Dropdown function triggered');
    }}
  />
</ChipList>`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Suggested chip](#suggested-chip)[Chip with dropdown](#chip-with-dropdown)[Representing multiple values](#representing-multiple-values)[Presenting chips in a list](#presenting-chips-in-a-list)[Non-closeable chip](#non-closeable-chip)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`