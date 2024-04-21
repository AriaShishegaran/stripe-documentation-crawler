htmlWaiting screens for Stripe Apps | Stripe Documentation[Skip to content](#main-content)Waiting screens[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpatterns%2Fwaiting-screens)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpatterns%2Fwaiting-screens)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Design patterns](/docs/stripe-apps/patterns)# Waiting screens for Stripe Apps

Learn how to use the waiting screen.Keep users informed throughout the entire onboarding process and set clear expectations of wait times and next steps with waiting screens.

## Before you begin

Create an app.

## Suggested use

- If users navigate back to Stripe during the onboarding flow, keep them informed about what’s happening. For example:

![A screen with a step to complete, supporting context, an action to complete, and affordance to start over](https://b.stripecdn.com/docs-statics-srv/assets/waiting-screens-01.9722e1605d31c8f01f2045f1a5587f33.png)

- Only add a call-to-action if it leads users to the next step of the onboarding process, or to provide additional context they need to complete in the next step.
- Keep language clear and concise. Avoid providing more context than what users might actually require. For example:

![A screen that prompts users to complete an application or start over](https://b.stripecdn.com/docs-statics-srv/assets/waiting-screens-02.1e3d5a7715a3911377a7c1b98575faef.png)

- If you must take users outside of Stripe to connect to your account (notrecommended), use a waiting screen that clearly communicates this transition. For example:

![A screen that prompts users to finish onboarding or start over](https://b.stripecdn.com/docs-statics-srv/assets/waiting-screens-03.d4038dfb4db72022ac2b627d863d9df8.png)

## Example

The following sample shows a waiting screen built in a ContextView component:

`import {
  Box,
  Button,
  ContextView,
  Icon,
  Inline,
  Link,
} from "@stripe/ui-extension-sdk/ui";
const WaitingScreen = () => {
  return (
    <ContextView
      title="Finish onboarding"
      footerContent={
        <Box>
          <Button type="primary" css={{ width: "fill" }}>
            Finish onboarding
          </Button>
          <Box
            css={{
              marginTop: "small",
              textAlign: "center",
              stack: "x",
              alignX: "center",
              gap: "small",
            }}
          >
            <Box>Want to go back?</Box>
            <Link>Start over.</Link>
          </Box>
        </Box>
      }
    >
      <Box css={{ marginBottom: "xlarge" }}>
        <Inline
          css={{
            background: "container",
            keyline: "neutral",
            borderRadius: "small",
            paddingX: "small",
            paddingTop: "small",
            paddingBottom: "xsmall",
          }}
        >
          <Icon name="clock" css={{ fill: "secondary" }} />
        </Inline>
      </Box>
      <Box>Please finish onboarding to SuperTodo.</Box>
    </ContextView>
  );
};`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Suggested use](#suggested-use)[Example](#example)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`