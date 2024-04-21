htmlListen for address input | Stripe Documentation[Skip to content](#main-content)Listen for address input[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Felements%2Faddress-element%2Fcollect-addresses)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Felements%2Faddress-element%2Fcollect-addresses)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)
[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Elements](/payments/elements)·[Home](/docs)[Payments](/docs/payments)[Web Elements](/docs/payments/elements)[Address Element](/docs/elements/address-element)# Listen for address input

Collect addresses to use in custom ways using an event listenerWebiOSAndroidReact NativeThemeDefaultSizeDesktopCustomer LocationUnited StatesPhone numberAutocompleteContactsThe Address Element enables you to collect local and international shipping or billing addresses from your customers.

[Set up StripeServer-side](#set-up-stripe)First, create a Stripe account or sign in.

Use our official libraries to access the Stripe API from your application:

Command Line[Ruby](#)`# Available as a gem
sudo gem install stripe`Gemfile[Ruby](#)`# If you use bundler, you can add this line to your Gemfile
gem 'stripe'`[Collect address detailsClient-side](#web-collect-address)You’re ready to collect address details on the client with the Address Element.

HTML + JSReact### Set up Stripe.js

The Address Element is automatically available as a feature of Stripe.js. Include the Stripe.js script on your checkout page by adding it to the head of your HTML file. Always load Stripe.js directly from js.stripe.com to remain PCI compliant. Don’t include the script in a bundle or host a copy of it yourself.

checkout.html`<head>
  <title>Checkout</title>
  <script src="https://js.stripe.com/v3/"></script>
</head>`### Create a Stripe instance

Create an instance of Stripe on your checkout page:

checkout.js`// Set your publishable key: remember to change this to your live publishable key in production
// See your keys here: https://dashboard.stripe.com/apikeys
const stripe = Stripe('pk_test_VOOyyYjgzqdm8I3SrBqmh9qY');`### Add the Address Element to your page

The Address Element needs a place on your page. Create an empty DOM node (container) with a unique ID in your form.

checkout.html`<form id="address-form">
  <h3>Address</h3>
  <div id="address-element">
    <!-- Elements will create form elements here -->
  </div>
</form>`After this form loads, create an instance of the Address Element, specify the address mode and mount it to the container DOM node.

If you already have an Elements instance created, you can use the same instance to create the Address Element. Otherwise, create a new Elements instance first.

ShippingBillingcheckout.js`const options = {
  // Fully customizable with appearance API.
  appearance: { /* ... */ }
};

// Only need to create this if no elements group exist yet.
// Create a new Elements instance if needed, passing the
// optional appearance object.
const elements = stripe.elements(options);

// Create and mount the Address Element in shipping mode
const addressElement = elements.create("address", {
  mode: "shipping",
});
addressElement.mount("#address-element");`[Retrieve address detailsClient-side](#web-retrieve-address)You can retrieve the address details by listening to the change event. The change event fires whenever the user updates any field in the Element.

HTML + JSReact`addressElement.on('change', (event) => {
  if (event.complete){
    // Extract potentially complete address
    const address = event.value.address;
  }
})`Alternatively, you can use getValue.

checkout.js`const handleNextStep = async () => {
  const addressElement = elements.getElement('address');

  const {complete, value} = await addressElement.getValue();

  if (complete) {
    // Allow user to proceed to the next step
    // Optionally, use value to store the address details
  }
};`In a single-page checkout flow with the Payment Element, the Address Element automatically passes the shipping or billing information when you confirm the PaymentIntent or SetupIntent.

In a multi-page checkout flow, you can manually update the PaymentIntent or update the Customer object with the address details received from the change event or getValue method before moving to the next step.

[Configure the Address ElementClient-side](#web-configure-address-element)You can configure the Address Element to suit your needs.

### Autocomplete

The Address Element has a built in address autocomplete feature that uses the Google Maps API Places Library. By default, the autocomplete is enabled with a Stripe provided Google Maps API key if any of the following conditions are met:

- In a single page checkout flow where the[Payment Element](/payments/payment-element)is mounted in the same elements group as the Address Element.
- In a checkout flow that uses the Address Element in an active[Link](/payments/link)session.

To enable autocomplete in the Address Element for all other scenarios, you can use the autocomplete option with mode set to google_maps_api. Set the apiKey to be your own Google Maps API key that’s configured to allow the Places API usage. Your Google Maps API key is only used when the Stripe provided Google Maps API key isn’t available.

NoteIf you’ve deployed a CSP and want to enable autocomplete with your own Google Maps API key, include https://maps.googleapis.com as a connect-src and script-src directive. Refer to the Google Maps API official guide for the most updated CSP requirement.

HTML + JSReact`const addressElement = elements.create("address", {
  mode: "shipping",
  autocomplete: {
    mode: "google_maps_api",
    apiKey: "{YOUR_GOOGLE_MAPS_API_KEY}",
  },
});`### Prefill address form

The Address Element accepts a defaultValues which lets you prefill the address form when the page loads. An Address Element with all values prefilled looks similar to:

HTML + JSReact`const addressElement = elements.create("address", {
  mode: "shipping",
  defaultValues: {
    name: 'Jane Doe',
    address: {
      line1: '354 Oyster Point Blvd',
      line2: '',
      city: 'South San Francisco',
      state: 'CA',
      postal_code: '94080',
      country: 'US',
    },
  },
});`### Other options

Refer to Stripe.js for the complete list of options in detail.

HTML + JSReact`// Sample of a options object
const addressElement = elements.create("address", {
  mode: 'shipping',
  allowedCountries: ['US'],
  blockPoBox: true,
  fields: {
    phone: 'always',
  },
  validation: {
    phone: {
      required: 'never',
    },
  },
});`[Validate address detailsClient-side](#web-validate-address-details)Stripe provides a few ways to validate for completeness of an address and trigger errors such as “This field is incomplete.” to display on any incomplete individual address fields.

If you’re using the Address Element with a Payment Intent or Setup Intent, use stripe.confirmPayment or stripe.confirmSetup respectively to complete the intent and then validation errors will appear in the Address Element if there are any.

For other use cases such as multi-page checkout flow, use getValue to trigger validation errors to display in the Address Element.

[OptionalCustomize the appearanceClient-side](#customize-appearance)Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Set up Stripe](#set-up-stripe)[Collect address details](#web-collect-address)[Retrieve address details](#web-retrieve-address)[Configure the Address Element](#web-configure-address-element)[Validate address details](#web-validate-address-details)Products Used[Elements](/payments/elements)[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`