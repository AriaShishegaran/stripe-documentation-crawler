# Account management

Renders a UI component for connected accounts to view and manage their account details. Connected accounts can view and edit account information like personal or business information, public information, and payout bank accounts.

Use the external_account_collection feature to control whether the account onboarding component collects external account information. This parameter is enabled by default and can only be set to false for custom accounts. Note that when this option is enabled for custom accounts, user authentication will be required for certain embedded components like account onboarding.

[external_account_collection](/api/account_sessions/create#create_account_session-components-account_onboarding-features-external_account_collection)

[user authentication](/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)

## Creating an Account Session

When creating an Account Session, enable account management by specifying account_management in the components parameter.

[creating an Account Session](/api/account_sessions/create)

## Rendering account management component
