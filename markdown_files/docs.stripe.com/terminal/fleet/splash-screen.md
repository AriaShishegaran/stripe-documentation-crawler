htmlConfigure readers with a custom splash screen | Stripe Documentation[Skip to content](#main-content)Configure the splash screen[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffleet%2Fsplash-screen)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffleet%2Fsplash-screen)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Configure readers with a custom splash screen

Customize the default splash screen for your readers.After you order and register readers to your Stripe account, you can configure them with a custom splash screen to match your brand.

A splash screen is the default screen that displays when your BBPOS WisePOS E or Verifone P400 is ready to accept payments. You can set a custom splash screen for these readers in one of two ways:

- [In the Dashboard](/terminal/fleet/splash-screen#dashboard)
- [Using the Configuration API](/terminal/fleet/splash-screen#configuration-api)

NoteTo customize checkout on the BBPOS WisePad 3 or BBPOS Chipper 2X BT, modify the UI of your application directly.

[In the Dashboard](#dashboard)Use the Dashboard to set a custom splash screen for your BBPOS WisePOS E or Verifone P400.

You can configure an account default splash screen, which applies to all readers in your fleet. You can also configure a custom splash screen for individual locations, which overrides the splash screen configured at the account level. Locations without a custom splash screen inherit the account default splash screen.

### Configure account default splash screen

1. Navigate to the[Reader Settings](https://dashboard.stripe.com/settings/terminal/reader)section of the Dashboard.
2. Upload an image to display on your readers. JPG and PNG images must be less than 2MB. GIF images must be less than 4 MB. Each reader has a specific display resolution and you must crop your JPG or PNG image to fit those dimensions. GIF images scale automatically.

Only BBPOS WisePOS E readers can use GIF images for the splash screen.

ReaderResolution (W x H)BBPOS WisePOS E720 x 1280Verifone P400320 x 480After uploading, it can take several minutes for the splash screen to appear.

### Configure splash screen for individual locations

You can also customize the splash screen for each location, so that all readers registered to a site share the same branding. For Connect users, custom splash screens enable you to create different checkout experiences to reflect the various merchants connected to your platform.

1. Navigate to the[Locations](https://dashboard.stripe.com/terminal/locations)section of the Dashboard.
2. Click the location you want to configure.
3. In the location details, clickReader settings.
4. Upload an image to display on your readers. JPG and PNG images must be less than 2MB. GIF images must be less than 4 MB. Each reader has a specific display resolution and you must crop your JPG or PNG image to fit those dimensions. GIF images scale automatically.

## Using the Configuration API

Use the Configuration API to specify settings and set a custom splash screen for your BBPOS WisePOS E or Verifone P400.

1. Upload a file.
2. Create or update a[Configuration](/api/terminal/configuration)object.
3. Assign the`Configuration`to a`Location`.

[Upload a file](#upload-file)Use the File Upload API to upload an image to display on your readers. JPG and PNG images must be less than 2MB. GIF images must be less than 4 MB. Each reader has a specific display resolution and you must crop your JPG or PNG image to fit those dimensions. GIF images scale automatically.

Only BBPOS WisePOS E readers can use GIF images for the splash screen.

ReaderResolution (W x H)BBPOS WisePOS E720 x 1280Verifone P400320 x 480Command Line[curl](#)`curl https://files.stripe.com/v1/files \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -F "file"="@/path/to/a/file.jpg" \
  -F "purpose"="terminal_reader_splashscreen"`[Create or update a Configuration object](#configuration-object)Use a Configuration object to set the custom splash screen for your specified device type. The supported device types are bbpos_wisepos_e and verifone_p400.

NoteStripe automatically provisions an account default configuration for you. You can optionally create a Configuration object for another configuration, or you can continue to the next step to apply the default configuration settings to the entire account.

To create a Configuration object, use the Configuration Create request:

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/configurations \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "bbpos_wisepos_e[splashscreen]"=file_1KjBJdE7XUJuZdf0F6GgO9uY`To update a Configuration object, use the Configuration Update request:

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/configurations/tmc_EjHtMwLT8HmATT \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d "bbpos_wisepos_e[splashscreen]"=file_1KjBJdE7XUJuZdf0F6GgO9uY`[Assign a Configuration object](#assign-configuration-object)Terminal Configuration objects follow a hierarchical approach. You can set configurations as follows:

- On individual[Locations](/api/terminal/locations)– Applies to all readers registered to that location
- At the account level – Applies to all readers in your fleet

Configurations are hierarchical and location-level settings can override account-level settings. Settings that aren’t configured at the location inherit the account-level settings.

For example, you can model your Configuration objects as follows:

![Configuration Hierarchy](https://b.stripecdn.com/docs-statics-srv/assets/configuration-object-tree.5ec745ad57500a800c4f34f0a970224e.png)

To assign a configuration to a location, provide the Configuration object you created earlier:

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/locations/tml_DPJxAAnxbn3JQz \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d configuration_overrides=tmc_EjHtMwLT8HmATT`[Update the default account configuration](#update-default-account-configuration)Stripe automatically provisions the default configuration for your account. When you set up your hierarchy, any setting that isn’t established at the location level inherits the setting from the default configuration. You can’t apply the default configuration directly to a location.

To retrieve the default configuration:

Command Line[curl](#)`curl -G https://api.stripe.com/v1/terminal/configurations \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d is_account_default=true`After you retrieve the default configuration, you can update it as you would any other configuration.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[In the Dashboard](#dashboard)[Using the Configuration API](#configuration-api)[Upload a file](#upload-file)[Create or update a Configuration object](#configuration-object)[Assign a Configuration object](#assign-configuration-object)[Update the default account configuration](#update-default-account-configuration)Products Used[Terminal](/terminal)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`