htmlMirakl Connector configuration | Stripe Documentation[Skip to content](#main-content)Configuration[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fmirakl%2Fconfiguration)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fconnectors%2Fmirakl%2Fconfiguration)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)
Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)[Stripe Connectors](/docs/connectors)[Mirakl](/docs/connectors/mirakl)# Mirakl Connector configuration

Before installing the connector, prepare a file with the variables below.

We provide a configuration file sample in our repository that you can copy and rename to .env.

## General settings

ParameterDescriptionAPP_SECRETTo be generated. Commonly used to add more entropy to security related operations. Learn more on the[Symfony documentation](https://symfony.com/doc/current/reference/configuration/framework.html#secret).OPERATOR_PASSWORDTo be generated. Used to secure requests to the API exposed by the connector. Set the`X-AUTH-TOKEN`header to this value when calling the API.DATABASE_URLThe connection URL to your database. Learn more on the[Doctrine documentation](https://www.doctrine-project.org/projects/doctrine-dbal/en/2.9/reference/configuration.html#connecting-using-a-url). For example,`pgsql://symfony:symfony@db:5432/symfony?charset=UTF-8`.MESSENGER_TRANSPORT_DSNThe transport used for the queuing system.See the[Symfony Messenger documentation](https://symfony.com/doc/current/messenger.html#transports-async-queued-messages)for supported transports. For example,`amqp://guest:guest@localhost:5672/%2f/messages`. Defaults to`doctrine://default`.STRIPE_CLIENT_SECRETYour Stripe API secret key available in your[API keys settings](https://dashboard.stripe.com/apikeys). We recommend creating a specific API key for the connector. Restricted keys are not supported.MIRAKL_HOST_NAMEHost name of your Mirakl Instance. For example,`https://mymarketplace.mirakl.net`.MIRAKL_API_KEYThe Mirakl operator key. Can be generated as a Mirakl operator in your API settings. We recommend creating a specific operator for the connector.## Onboarding

ParameterDescriptionREDIRECT_ONBOARDINGThe connector redirects the seller to this URL after completing their account creation on Stripe. Defaults to`$MIRAKL_HOST_NAME/mmp/shop/account/shop`.BASE_HOSTThe domain of the server hosting your connector. For example,`stripe-mirakl.example.com`.SCHEMEThe scheme used by your base host. Defaults to`https`.STRIPE_SELLERS_WEBHOOK_SECRETYour Stripe webhook secret available in your[Connect webhook settings](https://dashboard.stripe.com/webhooks)when adding the endpoint, see below.MIRAKL_CUSTOM_FIELD_CODECode of the custom field that you have to add, see below. Defaults to`stripe-url`.### Add a Stripe webhook endpoint for connected accounts

1. Go to your[webhook settings](https://dashboard.stripe.com/webhooks).
2. Add a[webhook](/webhooks)endpoint.
3. Set the URL to`<BASE_HOST>/api/public/webhook/sellers`.
4. SelectListen to events on Connected accounts.
5. Add`account.updated`in theEvents to send:
6. ClickAdd endpoint.
7. Use the webhook secret for the`STRIPE_SELLERS_WEBHOOK_SECRET`environment variable.

### Add a custom field to your Mirakl shops

1. Log in to your Mirakl back office as an Operator.
2. VisitSettings>Advanced Parameters>Shops.
3. Go to theCustom Fieldstab.
4. Use the following values to create a new field:

ParameterDescriptionCodeUse`stripe-url`unless you chose a different key in your environment file.Type`Link`Shops permissions`Read only`Required field`No`## Payments

ParameterDescriptionPAYMENT_METADATA_COMMERCIAL_ORDER_IDMetadata key used in Charges to convey the Mirakl commercial order ID. Defaults to`mirakl_commercial_order_id`.ENABLE_PRODUCT_PAYMENT_SPLITEnable the[payment split workflow](/connectors/mirakl/payments#payment-split)for product orders. Defaults to`false`.ENABLE_SERVICE_PAYMENT_SPLITEnable the[payment split workflow](/connectors/mirakl/payments#payment-split)for service orders. Defaults to`false`.ENABLE_PRODUCT_PAYMENT_REFUNDEnable the[payment refund workflow](/connectors/mirakl/payments#payment-refund)for product orders. Defaults to`false`.ENABLE_SERVICE_PAYMENT_REFUNDEnable the[payment refund workflow](/connectors/mirakl/payments#payment-refund)for service orders. Defaults to`false`.STRIPE_OPERATOR_WEBHOOK_SECRETYour Stripe webhook secret available in your[account webhook settings](https://dashboard.stripe.com/webhooks)when adding the endpoint, see below.### Add a Stripe webhook endpoint for your account

1. Go to your[webhook settings](https://dashboard.stripe.com/webhooks).
2. Add a webhook endpoint for youraccount.
3. Set the URL to`<BASE_HOST>/api/public/webhook/operator`.
4. Add the following in theEvents to send:`charge.succeeded`,`charge.updated`.
5. ClickAdd endpoint.
6. Use the webhook secret for the`STRIPE_OPERATOR_WEBHOOK_SECRET`environment variable.

## Notifications and alerting

ParameterDescriptionMAILER_DSNThe entire Symfony Mailer configuration using a DSN-like URL format. Learn more on the[Symfony documentation](https://symfony.com/doc/current/components/mailer.html#mailer-dsn). For example,`smtp://user:pass@host:port`. Defaults to`smtp://null`(mailer disabled).TECHNICAL_ALERT_EMAILThe recipicient of all technical alerts. For example,`myemail@example.com`. Defaults to empty. Required if mailer is enabled per`MAILER_DSN`.TECHNICAL_ALERT_EMAIL_FROMThe sender of all technical emails. Defaults to empty, required if mailer is configured. For example,`noreply@example.com`.OPERATOR_NOTIFICATION_URLThe endpoint on your server set to receive notifications from the connector. Defaults to empty (notifications disabled).MAIL_ON_NOTIFICATION_ENDPOINT_DOWNEnable email alerts if a URL is provided in`OPERATOR_NOTIFICATION_URL`and that URL is not available or responds with an error. Defaults to`true`.MAIL_ON_NOTIFICATION_ENDPOINT_DOWN_COOLDOWNTime between each email alert. Use`0`to disable throttling. The maximum value depends on the notification worker maximum life, that is,`3600`by default. Defaults to`10`.## See also

- [Integration steps](/connectors/mirakl#integration-steps).

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[General settings](#general-settings)[Onboarding](#onboarding)[Payments](#payments)[Notifications and alerting](#alerting)[See also](#see-also)Products Used[Connect](/connect)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`