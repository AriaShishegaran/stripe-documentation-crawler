htmlOnboarding | Stripe Documentation[Skip to content](#main-content)Onboarding[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fonboarding)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fstripe-apps%2Fonboarding)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)
[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Apps](/docs/stripe-apps)# Onboarding

Guide your users through your app's sign in and initial setup flows.Onboarding is the process your users go through to get your app set up after installation. It’s their first interaction with your app, and it needs to be intuitive and polished, with minimal friction before they can start using your app.

The required onboarding steps are different for every app, but we provide tools and best practices to help you build a great user experience.

[Design patterns](#design-patterns)View our onboarding design patterns for common scenarios including activation, sign in, redirection, and so on.

[Display your onboarding view](#display-your-view)When a user installs your app and goes to view it in the Dashboard, it’s important that the onboarding flow is the first thing they encounter. Make sure to:

- Create an onboarding component (using[SignInView](/stripe-apps/components/signinview), if a sign in flow is needed).
- In all of your[page-specific views](/stripe-apps/reference/viewports#page-specific-availability), check to see if the user has completed onboarding when the view first loads, and display your onboarding component appropriately. For example:`import {SignInView, ContextView} from '@stripe/ui-extension-sdk/ui';
import appIcon from './icon.svg';

// This component can be defined in a separate file for reuse between views
const Onboarding = () => (
  <SignInView
    description="Connect your SuperTodo account to Stripe."
    primaryAction={{label: 'Sign in', href: 'https://supertodo.example.com'}}
    brandColor="#635bff"
    brandIcon={appIcon}
  />
);

const CustomerDetailView = () => {
  // The definition of "isSignedIn" is dependent upon your app's sign in method
  if (!isSignedIn) {
    return <Onboarding />
  }

  return (
    <ContextView title="SuperTodo customer view">
      // your signed-in content here
    </ContextView>
  );
};`
- Do the same in your[Dashboard default view](/stripe-apps/reference/viewports#dashboard-wide-availability). If you don’t have a default view, create one so that wherever the user is in the Dashboard, they’re presented with the right flow when they open your app. If you don’t need a Default view for purposes other than onboarding, you can return`null`from the view if the user has already completed onboarding and the Dashboard displays the Stripe Dashboard default drawer that guides users to a page-specific view. For example:`import {SignInView} from '@stripe/ui-extension-sdk/ui';
import appIcon from './icon.svg';

// This component can be defined in a separate file for reuse between views
const Onboarding = () => (
  <SignInView
    description="Connect your SuperTodo account to Stripe."
    primaryAction={{label: 'Sign in', href: 'https://supertodo.example.com'}}
    brandColor="#635bff"
    brandIcon={appIcon}
  />
);

const DashboardDefaultView = () => {
  // The definition of "isSignedIn" is dependent upon your app's sign in method
  if (!isSignedIn) {
    return <Onboarding />
  }

  return null;
};`

[Rely on Stripe authentication for a zero-touch onboarding user experience](#rely-on-stripe-authentication)If you’re building an app that stores data in an external backend but doesn’t need its own concept of user accounts, you can rely on Stripe’s authentication to offer a zero-touch onboarding experience. Using this method, your app doesn’t require any onboarding and is usable immediately after installation.

Start by setting up your backend to authenticate requests from your app’s UI. With that in place, you can store information in your database with an added column for the user ID or account ID provided by Stripe. Users are already signed into the Stripe Dashboard when they use your app, so there’s no need for additional authentication.

## See also

- [SignInView](/stripe-apps/components/signinview)
- [Add an app settings page](/stripe-apps/app-settings)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Design patterns](#design-patterns)[Display your onboarding view](#display-your-view)[Rely on Stripe authentication for a zero-touch onboarding user experience](#rely-on-stripe-authentication)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`