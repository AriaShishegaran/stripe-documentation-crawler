# Settings sign in for Stripe Apps

If you’re building a connect extension or a back-end only app, onboard users with a settings page.

## Before you begin

Create an app.

[Create an app](/stripe-apps/create-app)

## Suggested use

- Use a settings page to sign in users.

- Apply this design pattern the same way you would in a drawer. Avoid additional context that isn’t helpful when onboarding users. For example:

- When you need to add additional context to users, use a FocusView component to provide the information. For example:

[FocusView](/stripe-apps/components/focusview)

## Example

To add the SignInView component to your settings view, display it conditionally with the SettingsView component based on the user’s sign in state:
