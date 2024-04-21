htmlAdditional context for Stripe Apps | Stripe Documentation[Skip to content](#main-content)Additional context[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpatterns%2Fadditional-context)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fpatterns%2Fadditional-context)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)[Design patterns](/docs/stripe-apps/patterns)# Additional context for Stripe Apps

Learn about how additional contexts in onboarding can help users better understand your app.If you need to share any additional context before users sign in, dedicate a space for it on a separate screen.

## Before you begin

Create an app.

## Suggested use

- Use a[FocusView](/stripe-apps/components/focusview)component to provide additional context, or to show a[demo](/stripe-apps/patterns/demo)screen of how your app works.
- Make sure the sign in screen is focused on onboarding tasks. Any additional context should be brief and contextualized. For example:

![](https://b.stripecdn.com/docs-statics-srv/assets/contextview-wide.05a45f6c9e0e4af6a0e47d783badb9f6.png)

## Example

The following sample shows additional content displayed within a SignInView component:

`import {SignInView, Img, Link} from '@stripe/ui-extension-sdk/ui';
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
    descriptionActionLabel="Learn more"
    descriptionActionTitle="Learn more"
    descriptionActionContents={
      <>
        <Img href="https://example.com/screenshot.png" />
        To import existing data from SuperTodo, you will need to connect your SuperTodo account to Stripe.
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