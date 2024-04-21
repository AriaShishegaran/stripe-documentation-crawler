# Onboarding

Onboarding is the process your users go through to get your app set up after installation. It’s their first interaction with your app, and it needs to be intuitive and polished, with minimal friction before they can start using your app.

The required onboarding steps are different for every app, but we provide tools and best practices to help you build a great user experience.

[Design patterns](#design-patterns)

## Design patterns

View our onboarding design patterns for common scenarios including activation, sign in, redirection, and so on.

[onboarding design patterns](/stripe-apps/patterns#onboarding)

[Display your onboarding view](#display-your-view)

## Display your onboarding view

When a user installs your app and goes to view it in the Dashboard, it’s important that the onboarding flow is the first thing they encounter. Make sure to:

- Create an onboarding component (using SignInView, if a sign in flow is needed).

[SignInView](/stripe-apps/components/signinview)

- In all of your page-specific views, check to see if the user has completed onboarding when the view first loads, and display your onboarding component appropriately. For example:import {SignInView, ContextView} from '@stripe/ui-extension-sdk/ui';
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
};

[page-specific views](/stripe-apps/reference/viewports#page-specific-availability)

- Do the same in your Dashboard default view. If you don’t have a default view, create one so that wherever the user is in the Dashboard, they’re presented with the right flow when they open your app. If you don’t need a Default view for purposes other than onboarding, you can return null from the view if the user has already completed onboarding and the Dashboard displays the Stripe Dashboard default drawer that guides users to a page-specific view. For example:import {SignInView} from '@stripe/ui-extension-sdk/ui';
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
};

[Dashboard default view](/stripe-apps/reference/viewports#dashboard-wide-availability)

[Rely on Stripe authentication for a zero-touch onboarding user experience](#rely-on-stripe-authentication)

## Rely on Stripe authentication for a zero-touch onboarding user experience

If you’re building an app that stores data in an external backend but doesn’t need its own concept of user accounts, you can rely on Stripe’s authentication to offer a zero-touch onboarding experience. Using this method, your app doesn’t require any onboarding and is usable immediately after installation.

Start by setting up your backend to authenticate requests from your app’s UI. With that in place, you can store information in your database with an added column for the user ID or account ID provided by Stripe. Users are already signed into the Stripe Dashboard when they use your app, so there’s no need for additional authentication.

[authenticate requests from your app’s UI](/stripe-apps/build-backend#authenticate-ui-to-backend)

## See also

- SignInView

[SignInView](/stripe-apps/components/signinview)

- Add an app settings page

[Add an app settings page](/stripe-apps/app-settings)
