# Notification banner

Renders a notification banner that lists open risk intervention tasks and onboarding requirements that can impact certain capabilities, such as accepting payments and payouts.

Use the external_account_collection feature to control whether the account onboarding component collects external account information. This parameter is enabled by default and can only be set to false for custom accounts. Note that when this option is enabled for custom accounts, user authentication will be required for certain embedded components like account onboarding.

[external_account_collection](/api/account_sessions/create#create_account_session-components-account_onboarding-features-external_account_collection)

[user authentication](/connect/get-started-connect-embedded-components#user-authentication-in-connect-embedded-components)

When creating an Account Session, enable notification banner by specifying notification_banner in the components parameter.

[creating an Account Session](/api/account_sessions/create)
