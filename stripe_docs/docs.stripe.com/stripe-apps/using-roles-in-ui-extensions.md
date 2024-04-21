# Using roles in UI extensions

Stripe Apps UI extensions can read the active user’s role in the Dashboard. Apps can expose different functionality to different user roles.

The UI Extension SDK provides valuable information about the end user of your app. The roles field of the userContext object gives a list of the active user’s roles. You can tailor the app’s content based on the user’s role, using the roles in the user context.

## How to determine the user’s Dashboard role

Extensions have a userContext prop that’s populated with information about the active Dashboard user. This object has a roles field, which is an array of RoleDefinition objects for each role that the active user is attributed to.

A role definition has these fields:

[private apps](/stripe-apps/distribution-options#share-with-team-members)

The name field provides the name of the user role, and you can use it to modify the functionality of your UI Extension.

## Custom user roles (private apps only)

Each role definition has a type field, which specifies the role type. The type field can either be ‘builtIn’ or ‘custom’. Because custom roles are specific to a given account, these roles are only available for private apps.

## Tailoring content based on the Dashboard role

A common use of this information is to conditionally display content based on the user role. Below is an example app that shows content tailored to particular user roles.

The result of the example app when viewing the app as an Administrator user

## See also

- Build a UI

[Build a UI](/stripe-apps/build-ui)

- Extension SDK API reference

[Extension SDK API reference](/stripe-apps/reference/extensions-sdk-api)

- User roles

[User roles](/get-started/account/teams/roles)
