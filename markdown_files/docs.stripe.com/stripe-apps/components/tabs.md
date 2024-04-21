htmlTabs | Stripe Documentation[Skip to content](#main-content)Tabs[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ftabs)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fcomponents%2Ftabs)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Components](/docs/stripe-apps/components)# Tabs

Use tabs to display sections of content.Tabs are sections of content that display one panel of content at a time. The list of tab elements sits along the top edge of the currently displayed panel.

To add the Tabs component to your app:

`import {Tabs, Tab, TabList, TabPanel, TabPanels} from '@stripe/ui-extension-sdk/ui';`## Basic Tabs

`<Tabs fitted>
  <TabList>
    {[1, 2].map((i) => (
      <Tab key={i} tabKey={i}>Tab {i}</Tab>
    ))}
  </TabList>
  <TabPanels>
    {[1, 2].map((i) => (
      <TabPanel key={i} tabKey={i}>
        <Box css={{background: 'container', padding: 'large'}}>Tab panel {i}</Box>
      </TabPanel>
    ))}
  </TabPanels>
</Tabs>`### Props

PropTypechildrenRequired`ReactNode`fitted`boolean`onSelectionChange`((arg: Key) => void)`selectedKey`Key`size`"small" | "medium" | "large"`## Small Tabs

`<Tabs size="small">
  <TabList>
    {[1, 2, 3, 4, 5].map((i) => (
      <Tab key={i} tabKey={i}>Tab {i}</Tab>
    ))}
  </TabList>
  <TabPanels>
    {[1, 2, 3, 4, 5].map((i) => (
      <TabPanel key={i} tabKey={i}>
        <Box css={{background: 'container', padding: 'large'}}>Tab panel {i}</Box>
      </TabPanel>
    ))}
  </TabPanels>
</Tabs>`## Disabled Tabs

`<Tabs size="large" fitted>
  <TabList>
    <Tab tabKey="1">Tab</Tab>
    <Tab tabKey="2">Another Tab</Tab>
    <Tab tabKey="3" disabled>Disabled Tab</Tab>
  </TabList>
  <TabPanels>
    <TabPanel tabKey="1">
      <Box css={{background: 'container', padding: 'large'}}>Test Tab Panel 1</Box>
    </TabPanel>
    <TabPanel tabKey="2">
      <Box css={{background: 'container', padding: 'large'}}>Test Tab Panel 2</Box>
    </TabPanel>
    <TabPanel tabKey="3">
      <Box css={{background: 'container', padding: 'large'}}>Test Tab Panel 3</Box>
    </TabPanel>
  </TabPanels>
</Tabs>`## Tab

The TabList component supports the selection of content.  TabList is made up of a collection of Tab components.  Each Tab can be uniquely identified with a tabKey prop. If you render Tab components using a map function, you must still add a key to satisfy the rules of React.

### Props

PropTypechildrenRequired`React.ReactNode`disabled`boolean`tabKey`any`## TabPanel

The TabPanels component supports displaying panels of content with Tabs.  TabPanels is made up of a collection of TabPanel components.  Each TabPanel can be uniquely identified with a tabKey prop. If you render TabPanel components using a map function, you must still add a key to satisfy the rules of React.

### Props

PropTypechildrenRequired`React.ReactNode`tabKey`any`## Controlled Tabs

Use the selectedKey prop from Tabs in combination with the tabKey prop from Tab and TabPanel to create a controlled component.

`<Tabs selectedKey={key} onSelectionChange={setSelectedKey}>
  <TabList>
    {['a', 'b', 'c', 'd', 'e'].map((key) => (
      <Tab key={key} tabKey={key}>Tab {key}</Tab>
    ))}
  </TabList>
  <TabPanels>
    {['a', 'b', 'c', 'd', 'e'].map((key) => (
      <TabPanel key={key} tabKey={key}>
        <Box css={{background: 'container', padding: 'large'}}>Tab panel {key}</Box>
      </TabPanel>
    ))}
  </TabPanels>
</Tabs>`## Unsupported uses

Tabs don’t support conditional content within fragments unless the fragment children are given the same key.

`const UnsupportedExample = () => {
  const [result, setResult] = useState(null);

  return (
    <Tabs>
      <TabList>
        <Tab tabKey="1">
          <>
            {result && <Inline>View results</Inline>}
            {!result && <Inline>Create results</Inline>}
          </>
        </Tab>
      </TabList>
      <TabPanels>
        <TabPanel tabKey="1">
          <>
            {result && <Inline>Results</Inline>}
            {!result && <Inline>No results yet</Inline>}
          </>
        </TabPanel>
      </TabPanels>
    </Tabs>
  );
}`To avoid unsupported uses of Tabs, use components instead of fragments.  Alternatively, give the children of fragments a shared key.

`const SupportedExample = () => {
  const [result, setResult] = useState(null);

  return (
    <Tabs>
      <TabList>
        <Tab tabKey="1">
          <Box>
            {result && <Inline>View results</Inline>}
            {!result && <Inline>Create results</Inline>}
          </Box>
        </Tab>
      </TabList>
      <TabPanels>
        <TabPanel tabKey="1">
          <>
            {result && <Inline key="tab-panel-result">Results</Inline>}
            {!result && <Inline key="tab-panel-result">No results yet</Inline>}
          </>
        </TabPanel>
      </TabPanels>
    </Tabs>
  );
}`## See also

- [Design patterns to follow](/stripe-apps/patterns)
- [Style your app](/stripe-apps/style)
- [UI testing](/stripe-apps/ui-testing)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Basic Tabs](#basic-tabs)[Small Tabs](#small-tabs)[Disabled Tabs](#disabled-tabs)[Tab](#tab)[TabPanel](#tabpanel)[Controlled Tabs](#controlled-tabs)[Unsupported uses](#unsupported-uses)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`