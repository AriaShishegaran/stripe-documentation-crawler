htmlManage locations | Stripe Documentation[Skip to content](#main-content)Manage locations[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffleet%2Flocations)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fterminal%2Ffleet%2Flocations)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)
[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Terminal](/terminal)·[Home](/docs)[Payments](/docs/payments)[Terminal](/docs/terminal)# Manage locations

Group and manage your readers by physical location.Stripe Reader S700Get notified when Stripe Reader S700 is available in your country.

Locations APINavigating locations and zonesBetaIf your Terminal deployment uses many readers across multiple physical locations, keeping track of them all can get overwhelming. Locations help you manage readers and their activity by associating them with a physical operating site. They also ensure your readers download the proper regional configurations.

Use the Terminal Locations object to group readers, view their connectivity status, and customize their settings by physical location. This can be especially helpful for marketplaces with many connected accounts.

After creating Locations, you can use them to help you group readers, improve reader discovery flows, customize their settings by physical location, and more.

## Create a location Server-side Dashboard

Create a Location for each physical location that your readers operate at. If your business requires you to move your readers frequently, your locations may use addresses that represent a primary place of business.

To create a new location using the API, use the create location request.

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/locations \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d display_name=HQ \
  -d "address[line1]"="1272 Valencia Street" \
  -d "address[city]"="San Francisco" \
  -d "address[state]"=CA \
  -d "address[country]"=US \
  -d "address[postal_code]"=94110`A Location’s required address properties differ based on country:

CountriesRequired Address PropertiesAustraliaCanadaItalySpainUnited States`line1`,`city`,`state`,`postal_code`,and`country`Austria+BelgiumCzech Republic+DenmarkFinland+FranceGermanyLuxembourg+Malaysia+NetherlandsNew Zealand+Norway+Portugal+SwedenSwitzerland+United Kingdom`line1`,`city`,`postal_code`,and`country`IrelandSingapore`line1`,`postal_code`,and`country`+Terminal is currently in beta in this country.**Compatibility for this mobile SDK also applies when used with React Native.### Create a location for accounts using direct charges

To create a location for an account using direct charges, use the Stripe-Account header in your request. Only the Connect account you authenticate as can access these locations. If the business operates in multiple physical sites, you can create multiple locations for any individual accounts with direct charges.

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/locations \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -H "Stripe-Account: {{CONNECTED_ACCOUNT_ID}}" \
  -d display_name=HQ \
  -d "address[line1]"="1272 Valencia Street" \
  -d "address[city]"="San Francisco" \
  -d "address[state]"=CA \
  -d "address[country]"=US \
  -d "address[postal_code]"=94110`### Create a location for accounts using destination charges

For integrations using destination charges, locations belong to the platform account and aren’t mapped strictly to connected accounts. If your platform needs to associate accounts using destination charges with locations, you can store a reference to the relevant account(s) in the location’s metadata property.

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/locations \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "display_name"="HQ" \
  -d "address[line1]"="Frederik Roeskestraat 96" \
  -d "address[city]"="Amsterdam" \
  -d "address[country]"="NL" \
  -d "address[postal_code]"="1076 ED" \
  -d "metadata[connected_account]"={{CONNECTED_ACCOUNT_ID}}`You can also create locations from the Stripe Dashboard, on the Manage locations page.

When you register your reader to a location, the specified location groups the reader and defines its country settings.

## Scope connection tokens Server-side Smart readers

When creating a ConnectionToken for the Terminal SDK, you may provide a location parameter to control access to smart readers. If you provide a location, the ConnectionToken is only usable with smart readers assigned to that location. If you don’t provide a location, the ConnectionToken is usable with all readers.

NoteFor Bluetooth readers, the location of a ConnectionToken has no effect. This ensures that Bluetooth readers near you are always discoverable.

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/connection_tokens \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d location={{LOCATION_ID}}`## Register a reader to a location

You must register your reader to a location to accept payments. The process for registering your reader to a location differs based on whether it’s an smart reader or a Bluetooth reader.

### Smart readers Server-side

Register smart readers (Verifone P400, BBPOS WisePOS E, and Stripe Reader S700) to a location during reader registration.

Command Line[curl](#)`curl https://api.stripe.com/v1/terminal/readers \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d registration_code={{READER_REGISTRATION_CODE}} \
  --data-urlencode label="Alice's reader" \
  -d location={{LOCATION_ID}}`You can also register readers in the Dashboard, either on the Readers page or on the Manage locations page.

### Bluetooth readers Client-side

Register Bluetooth readers (Stripe Reader M2, BBPOS Chipper 2X BT, and BBPOS WisePad 3) to a location while connecting to the reader by specifying the locationId in your BluetoothConnectionConfiguration. If you’d like, you can register the reader to the last used location by passing in the reader.locationId from a discovered reader.

NoteTerminal SDK versions prior to v2.0.0 don’t support registering BBPOS Chipper 2X BT or WisePad 3 readers to locations.

## Filter discovered readers

### Smart readers Client-side

### SDK Reference

- [discoverReaders (JavaScript)](/terminal/references/api/js-sdk#discover-readers)
- [discoverReaders (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)discoverReaders:delegate:completion:)
- [discoverReaders (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/discover-readers.html)
- [discoverReaders (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#discoverReaders)

Your application uses the SDK’s discoverReaders method to look for readers it can connect to. When discovering a smart reader like the Verifone P400 or BBPOS WisePOS E, you can discover the intended reader more easily by filtering results by location.

With the code below, your app’s callback only returns readers in a given location. You can find the location’s ID on the Manage locations page in the Dashboard.

JavaScriptiOSAndroidReact Native`async function discoverReaders() {
  const config = {simulated: false, location: '{{LOCATION_ID}}'}
  const discoverResult = await terminal.discoverReaders(config);
  if (discoverResult.error) {
    console.log('Failed to discover: ', discoverResult.error);
  } else if (discoverResult.discoveredReaders.length === 0) {
    console.log('No available readers.');
  } else {
    // You should show the list of discoveredReaders to the
    // cashier here and let them select which to connect to (see below).
    connectReader(discoverResult);
  }
}`### Bluetooth readers Client side

Because mobile readers use Bluetooth for connection, discoverReaders returns all nearby readers.  No additional filtering is applied by default.  However, you can use the returned registeredLocation parameter on the Reader object to optionally apply additional filtering in your application.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Create a location](#create-location)[Scope connection tokens](#connection-tokens)[Register a reader to a location](#register)[Filter discovered readers](#discover)Products Used[Terminal](/terminal)[Payments](/payments)[Connect](/connect)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`