# Manage locations

Get notified when Stripe Reader S700 is available in your country.

[Get notified](https://dashboard.stripe.com/terminal/s700_notify)

If your Terminal deployment uses many readers across multiple physical locations, keeping track of them all can get overwhelming. Locations help you manage readers and their activity by associating them with a physical operating site. They also ensure your readers download the proper regional configurations.

Use the Terminal Locations object to group readers, view their connectivity status, and customize their settings by physical location. This can be especially helpful for marketplaces with many connected accounts.

[Locations](/api/terminal/locations)

[marketplaces](/terminal/features/connect)

After creating Locations, you can use them to help you group readers, improve reader discovery flows, customize their settings by physical location, and more.

## Create a location Server-side Dashboard

Create a Location for each physical location that your readers operate at. If your business requires you to move your readers frequently, your locations may use addresses that represent a primary place of business.

To create a new location using the API, use the create location request.

[create location](/api/terminal/locations/create)

A Location’s required address properties differ based on country:

[address properties](/api/terminal/locations/create#create_terminal_location-address)

To create a location for an account using direct charges, use the Stripe-Account header in your request. Only the Connect account you authenticate as can access these locations. If the business operates in multiple physical sites, you can create multiple locations for any individual accounts with direct charges.

[direct charges](/connect/direct-charges)

For integrations using destination charges, locations belong to the platform account and aren’t mapped strictly to connected accounts. If your platform needs to associate accounts using destination charges with locations, you can store a reference to the relevant account(s) in the location’s metadata property.

[destination charges](/connect/destination-charges)

[metadata](/api/terminal/locations/object#terminal_location_object-metadata)

You can also create locations from the Stripe Dashboard, on the Manage locations page.

[Manage locations](https://dashboard.stripe.com/terminal/locations)

When you register your reader to a location, the specified location groups the reader and defines its country settings.

[register your reader to a location](/terminal/fleet/locations#register)

## Scope connection tokens Server-side Smart readers

When creating a ConnectionToken for the Terminal SDK, you may provide a location parameter to control access to smart readers. If you provide a location, the ConnectionToken is only usable with smart readers assigned to that location. If you don’t provide a location, the ConnectionToken is usable with all readers.

[ConnectionToken](/api/terminal/connection_tokens)

For Bluetooth readers, the location of a ConnectionToken has no effect. This ensures that Bluetooth readers near you are always discoverable.

## Register a reader to a location

You must register your reader to a location to accept payments. The process for registering your reader to a location differs based on whether it’s an smart reader or a Bluetooth reader.

Register smart readers (Verifone P400, BBPOS WisePOS E, and Stripe Reader S700) to a location during reader registration.

[Verifone P400](/terminal/payments/connect-reader?reader-type=internet#register-reader)

[BBPOS WisePOS E](/terminal/payments/connect-reader?reader-type=internet#register-reader)

[Stripe Reader S700](/terminal/payments/connect-reader?reader-type=internet#register-reader)

You can also register readers in the Dashboard, either on the Readers page or on the Manage locations page.

[Readers](https://dashboard.stripe.com/terminal/readers)

[Manage locations](https://dashboard.stripe.com/terminal/locations)

Register Bluetooth readers (Stripe Reader M2, BBPOS Chipper 2X BT, and BBPOS WisePad 3) to a location while connecting to the reader by specifying the locationId in your BluetoothConnectionConfiguration. If you’d like, you can register the reader to the last used location by passing in the reader.locationId from a discovered reader.

[Stripe Reader M2](/terminal/readers/stripe-m2)

[BBPOS Chipper 2X BT](/terminal/payments/connect-reader?reader-type=bluetooth#connect-reader)

[BBPOS WisePad 3](/terminal/payments/connect-reader?reader-type=bluetooth#connect-reader)

Terminal SDK versions prior to v2.0.0 don’t support registering BBPOS Chipper 2X BT or WisePad 3 readers to locations.

## Filter discovered readers

- discoverReaders (JavaScript)

[discoverReaders (JavaScript)](/terminal/references/api/js-sdk#discover-readers)

- discoverReaders (iOS)

[discoverReaders (iOS)](https://stripe.dev/stripe-terminal-ios/docs/Classes/SCPTerminal.html#/c:objc(cs)SCPTerminal(im)discoverReaders:delegate:completion:)

- discoverReaders (Android)

[discoverReaders (Android)](https://stripe.dev/stripe-terminal-android/core/com.stripe.stripeterminal/-terminal/discover-readers.html)

- discoverReaders (React Native)

[discoverReaders (React Native)](https://stripe.dev/stripe-terminal-react-native/api-reference/interfaces/StripeTerminalSdkType.html#discoverReaders)

Your application uses the SDK’s discoverReaders method to look for readers it can connect to. When discovering a smart reader like the Verifone P400 or BBPOS WisePOS E, you can discover the intended reader more easily by filtering results by location.

[Verifone P400](/terminal/payments/connect-reader?reader-type=internet#discover-readers)

[BBPOS WisePOS E](/terminal/payments/connect-reader?reader-type=internet#discover-readers)

With the code below, your app’s callback only returns readers in a given location. You can find the location’s ID on the Manage locations page in the Dashboard.

[Manage locations](https://dashboard.stripe.com/terminal/locations)

Because mobile readers use Bluetooth for connection, discoverReaders returns all nearby readers.  No additional filtering is applied by default.  However, you can use the returned registeredLocation parameter on the Reader object to optionally apply additional filtering in your application.
