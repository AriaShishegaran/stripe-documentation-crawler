htmlStripe for Salesforce Platform Installation Guide | Stripe Documentation[Skip to content](#main-content)Installation[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fplugins%2Fstripe-connector-for-salesforce%2Finstallation-guide)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fplugins%2Fstripe-connector-for-salesforce%2Finstallation-guide)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Salesforce](/docs/connectors/salesforce)[Stripe Connector for Salesforce Platform](/docs/connectors/stripe-connector-for-salesforce/overview)# Stripe for Salesforce Platform Installation Guide

Access the full Stripe platform from within Salesforce with low and no-code tools.Identify what environment you want to install your app in. We provide separate installation options for test and production environments.

- To Install this Application from the Salesforce AppExchange , follow this[link](https://appexchange.salesforce.com/appxListingDetail?listingId=4dff0f8e-0b10-47c2-a3a3-f3905e7f7927). For users in Japan,[AppExchange Japan](https://appexchangejp.salesforce.com/appxListingDetail?listingId=a0N3u00000RgdoWEAR)is also available.

1. Login into the Salesforce organization you wish to install the package into.
2. After logging in, you’re directed to the installation page. ClickContinueto begin the installation process.
3. We recommend installingInstall for Admins Only. This option allows for controlling access and permissions after the package has been installed.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_AdminOnly.39c4e7785aaaacfa3a88ffd07b8d2aa1.png)


4. Approve Third-Party Accesscheck off the box and clickContinueto start the package installation when the modal appears. As it states, this is to allow data to be sent back and forth between your Salesforce org and the Stripe PBO.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_3rdPartyAccess.f4fbd0b81b4316d943bb05bd522e07e8.png)



## Configure permission sets

The package incorporates both the Stripe Connector Integration User and the Stripe Connector Data User permission sets. These sets enable different users within your organization to access specific application features.

## Stripe Connector integration user

The Stripe Connector Integration User permission set must be assigned to any non-system administrator persona designated to manage setup log cleanup settings and event subscriptions. However, since system permissions are unable to be packaged due to limitations with Salesforce AppExchange apps. You must add additional permissions manually by cloning the permission set, in order for these users to access setup features.

1. Clone Permission SetTo clone the permission set, navigate toSetup > User > Permission Sets.
2. Next to theStripe Connector Integration Userpermission set, clickClone.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_PermissionSetClone.6ebe75de9179b7a3f83f748342ff13a7.png)


3. Enter a new uniqueLabelandAPI Name, then clickSave.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_PermissionSetLable.0a61995ecec91fb6d1dc5ad4f0cb77a9.png)


4. Modify Permission SetNavigate toSetup > User > Permission Setsand select your cloned permission set.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_PermissionSetClone.6ebe75de9179b7a3f83f748342ff13a7.png)


5. SelectSystem Permissions.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_PermissionSetPermissions.39daa8bb6675b52ceccaea30ba7ea353.png)


6. ClickEditthen select theDownload AppExchange Packagespermissions, and clickSave.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_PermissionSetPermissionsDownload.65460764a93765adacf3b4b015c22fb0.png)


7. ClickSaveagain to confirm changes.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_PermissionSetPermissionsSave.d84d2adfacdd78fe185c4048907f1f84.png)


8. Assign Permission Setto user(s) by navigating toSetup > User > Permission Sets.
9. Select your cloned permission set.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_PermissionSetClone.6ebe75de9179b7a3f83f748342ff13a7.png)


10. From the Permission Set Overview page, clickManage Assignments.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_PermissionManageAssignments.185046c3016d23886673fdb213a096fe.png)


11. ClickAdd Assignments.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_PermissionAddAssignments.bb1994dec3a8a6aad6c292b870bcaedb.png)


12. Check the box next to the user(s) to assign permission set to and clickNextat the bottom of the page.

Stripe Connector data user![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

The Stripe Connector Data User has the ability to perform operations on the Stripe_Event__c object records, which the Webhook Handler class creates. To provide non-admin users access to Stripe Event records, you must assign a data user permission set to their user profile.

1. Assign a permission set to a user by navigating toSetup > User > Permission Sets.
2. Select theStripe Connector Data Userpermission set.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_PermissionSetPermissions_data.1ea42a4f84910f5186a9f5e411084ff1.png)


3. From thePermission Set Overviewpage, clickManage Assignments.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_PermissionManageAssignments_data.0f15bdcc0b0e5d6a38d5082184a46d81.png)


4. ClickAdd Assignments.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_PermissionAddAssignments_data.5ceefddb997ec6f16fe68ee969447979.png)


5. Check the box next to a user to assign a permission set to them
6. ClickNextat the bottom of the page.

## Stripe for Salesforce Platform setup wizard

When users first access the Stripe Connector for Salesforce app, they must complete an Initial Setup flow. This guided wizard flow helps users authorize an org, add a Stripe account, and configure sync preferences. After completing the initial setup, the Account Management tab becomes the users’ landing page. Here, they can add more Stripe accounts or navigate to other tabs to edit configuration settings.

### Add a Stripe account using the setup wizard

1. Launch the initial setup wizard, and navigate toApp Launcher > Stripe Universal Connector for Salesforce![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_App.10a5208667229e897eb93dc0dfbb10c2.png)


2. Click theGet Startedbutton.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_AppGetStarted.78464fbff085da988de93c2d6de890d6.png)


3. Click theAuthorizebutton.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_AppGetStartedAuthorize.fe176d8502ff431cb46fe4bcb5ab59fb.png)


4. After the new window opens, clickAllowto grant access for your org.
5. Click theNextbutton.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_AppGetStartedAuthorizeNext.a696556bd86ed09857ef170e9032d39d.png)


6. Select an option for adding an account, then click theLog in to Stripebutton.

- Test Mode: Launches a window displaying your Stripe test mode accounts.
- Live Mode: Launches a window displaying your Stripe live mode accounts.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_AppGetStartedAuthorizeAccount.e51b1da06f1caf0065de32e6241125ad.png)



1. Log into Stripe and select the account you wish to add.
2. After you select an account, click theNextbutton.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_AppGetStartedAuthorizeAccountNext.ded02a21b3970c98af817266ea1e30fe.png)


3. (Optional) Click thetoggleif you wish to enable the Stripe Events and Sync Logs cleanup.
4. If the cleanup trigger is active, enter the numerical value in the input box to set the desired amount of records to be retained in the Salesforce org.
5. Click theNextbutton.![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_AppGetStartedRecordClean.e53021fe6e2fd9ff9270215033c35f00.png)


6. Click theStripe API Versiondropdown.
7. Select theStripe APIversion to install. If you’re unsure what version to install, select the latest version.
8. Click theInstall Packagebutton, which launches another window that you need to use to complete the installation of the extension package.
9. ClickFinish![](https://b.stripecdn.com/docs-statics-srv/assets/SFU_AppGetStartedAPIInstall.974d03ade65d799799f7b363c37d3b71.png)



## See also

- [Enablement videos](/plugins/stripe-connector-for-salesforce/videos)
- [Configure events](/plugins/stripe-connector-for-salesforce/configure-events)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Configure permission sets](#configure-permission-sets)[Stripe Connector integration user](#stripe-connector-integration-user)[Stripe for Salesforce Platform setup wizard](#stripe-for-salesforce-platform-setup-wizard)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`