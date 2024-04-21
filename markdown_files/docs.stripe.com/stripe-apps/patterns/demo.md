htmlDemo content for Stripe Apps | Stripe Documentation[Skip to content](#main-content)Demo content[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpatterns%2Fdemo)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpatterns%2Fdemo)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Design patterns](/docs/stripe-apps/patterns)# Demo content for Stripe Apps

Learn tips for displaying a demo of your app.When building a demo of your app, keep the content brief and only highlight the top functionality that your app offers.

## Before you begin

Create an app.

## Suggested use

- Add a dedicated page view that doesn’t interfere with the onboarding flow.
- Provide “just enough” information to communicate the main functionality of your app. For example:

![](https://b.stripecdn.com/docs-statics-srv/assets/demo-content.019b1bd485c337fe7592b54ef729db53.png)

## Example

The following sample shows demo content displayed within a SignInView component:

`import {SignInView, Banner, Button} from '@stripe/ui-extension-sdk/ui';
import appIcon from './icon.svg';

const Onboarding = () => (
  <SignInView
    description="Connect your SuperTodo account with Stripe."
    primaryAction={{label: 'Sign in', href: 'https://example.com'}}
    footerContent={
      <>
        Don't have an account? <Link href="https://example.com">Sign up</Link>
      </>
    }
    descriptionActionLabel="View demo"
    descriptionActionTitle="Todo lists"
    descriptionActionContents={
      <>
        <Box css={{marginBottom: 'small'}}>
          <Button type="primary" css={{width: 'fill', alignX: 'center'}}>
            Create list
          </Button>
        </Box>
        <Banner
          type="caution"
          title="You're viewing demo content"
          description="Your data will be visible once you sign in."
        />
        ...continued app demo content.
      </>
    }
    brandColor="#635bff"
    brandIcon={appIcon}
  />
);`Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Before you begin](#before-you-begin)[Suggested use](#suggested-use)[Example](#example)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`