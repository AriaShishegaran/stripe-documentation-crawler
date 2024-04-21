# Using Connect with Standard accounts

This is the recommended method for creating standard accounts. If you’re an extension or an application that needs access to an existing account so you can provide services to your users, you can still use OAuth.

[OAuth](/connect/oauth-reference)

A Standard Stripe account is a conventional Stripe account where the account holder (that is, your platform’s user) has a relationship with Stripe, is able to log in to the Dashboard, and can process charges on their own.

[Dashboard](https://dashboard.stripe.com/)

Stripe’s sample integration, Kavholm, shows you how to use Connect Onboarding for a seamless user onboarding experience.

[Kavholm](https://github.com/stripe-samples/connect-onboarding-for-standard)

[Connect Onboarding](https://stripe.com/connect/onboarding)

## Get started

If you’re new to Connect, start with a guide to use Standard accounts to enable other businesses to accept payments directly.

[Connect](/connect)

[enable other businesses to accept payments directly](/connect/enable-payment-acceptance-guide)

## How to use Connect Onboarding for Standard accounts

- Go to your Connect settings page to customize the visual appearance of the form with the name, color, and icon of your brand. Connect Onboarding requires this information.

Go to your Connect settings page to customize the visual appearance of the form with the name, color, and icon of your brand. Connect Onboarding requires this information.

[Connect settings page](https://dashboard.stripe.com/account/applications/settings)

- Use the /v1/accounts API to create a new account and get the account ID. You can prefill information on the account object for the user before you generate the account link. You must pass the following parameter:type = standardNoteAfter you create the new account, check to see that the account displays in the Dashboard.

Use the /v1/accounts API to create a new account and get the account ID. You can prefill information on the account object for the user before you generate the account link. You must pass the following parameter:

[create](/api/accounts/create)

- type = standard

After you create the new account, check to see that the account displays in the Dashboard.

- Call the Account Links API to create a link for the account to onboard with.

Call the Account Links API to create a link for the account to onboard with.

[Account Links](/api/account_links)

- In the onboarding flow for your own platform, redirect your user to the url returned by Account Links.

In the onboarding flow for your own platform, redirect your user to the url returned by Account Links.

[Account Links](/api/account_links)

- Handle additional account states, redirecting your account to the Connect Onboarding flow if necessary.

Handle additional account states, redirecting your account to the Connect Onboarding flow if necessary.

- Optional: You can add additional procedures, such as Tax or Climate, to the Connect Onboarding flow through the platform product configuration in the Dashboard.

Optional: You can add additional procedures, such as Tax or Climate, to the Connect Onboarding flow through the platform product configuration in the Dashboard.

[platform product configuration](https://dashboard.stripe.com/connect/setup)

[Create a Standard account and prefill information](#create-account)

## Create a Standard account and prefill information

Use the Create Account API to create a connected account with type set to standard. You can prefill any information, but at a minimum, you must specify the type. The country of the account defaults to the same country as your platform, and the account confirms the selection during onboarding.

[Create Account](/api/accounts/create)

This example includes only some of the fields you can set when creating an account. For a full list of the fields you can set, such as address and website_url, see the Create Account API reference.

[Create Account API reference](/api/accounts/create)

If you’ve already collected information for your connected accounts, you can prefill that information on the account object. You can prefill any account information, including personal and business information, external account information, and so on.

Connect Onboarding doesn’t ask for the prefilled information. However, it does ask the account holder to confirm the prefilled information before accepting the Connect service agreement.

[Connect service agreement](/connect/service-agreement-types)

When testing your integration, prefill account information using test data.

[test data](/connect/testing)

[Create an account link](#create-link)

## Create an account link

You can create an account link by calling the Account Links API with the following parameters:

[Account Links](/api/account_links)

- account - use the account ID returned by the API from the previous step

- refresh_url

- return_url

- type = account_onboarding

[https://example.com/reauth](https://example.com/reauth)

[https://example.com/return](https://example.com/return)

[Redirect your user to the account link URL](#redirect-link)

## Redirect your user to the account link URL

The response to your Account Links request includes a value for the key url. Redirect to this link to send your user into the flow. You can only use URLs from the account links once because they grant access to the account holder’s personal information. Authenticate the user in your application before redirecting them to this URL. After you create an account link on a Standard account, you won’t be able to read or write Know Your Customer (KYC) information. Prefill any KYC information before creating the first account link.

[Account Links](/api/account_links)

[account links](/api/account_links)

[Know Your Customer](https://support.stripe.com/questions/know-your-customer)

Don’t email, text, or otherwise send account link URLs outside of your platform application. Instead, provide them to the authenticated account holder within your application.

[Handle the user returning to your platform](#return-user)

## Handle the user returning to your platform

Connect Onboarding requires you to pass both a return_url and refresh_url to handle all cases where you redirect the user to your platform. It’s important that you implement these correctly to provide the best experience for your user.

You can use HTTP for your return_url and refresh_url while in test mode (for example, to test with localhost), but you can only use HTTPS in live mode. Be sure to swap testing URLs for HTTPS URLs before going live.

Stripe issues a redirect to this URL when the user completes the Connect Onboarding flow. This doesn’t mean that all information has been collected or that there are no outstanding requirements on the account. This only means the flow was entered and exited properly.

No state is passed through this URL. After redirecting a user to your return_url, check the state of the details_submitted parameter on their account by doing either of the following:

- Listening to account.updated webhooks

[webhooks](/webhooks)

- Calling the Accounts API and inspecting the returned object

[Accounts](/api/accounts)

Your user redirects to the refresh_url in these cases:

- The link expired (a few minutes went by since the link was created)

- The user already visited the link (they refreshed the page, or clicked back or forward in the browser)

- Your platform is no longer able to access the account

- The account has been rejected

Your refresh_url triggers a method on your server to call Account Links again with the same parameters, and redirect the user to the Connect Onboarding flow to create a seamless experience.

[Account Links](/api/account_links)

[Handle users that have not completed onboarding](#handle-users)

## Handle users that have not completed onboarding

A user that is redirected to your return_url might not have completed the onboarding process. Use the /v1/accounts endpoint to retrieve the user’s account and check for charges_enabled. If the account isn’t fully onboarded, provide UI prompts to allow the user to continue onboarding later. The user can complete their account activation through a new account link (generated by your integration). You can check the state of the details_submitted parameter on their account to see if they’ve completed the onboarding process.

[OptionalEnable Stripe Tax obligation monitoring](#enable-stripe-tax)

## OptionalEnable Stripe Tax obligation monitoring

## See also

- Creating charges

[Creating charges](/connect/charges)

- Authentication

[Authentication](/connect/authentication)

- OAuth reference

[OAuth reference](/connect/oauth-reference)
