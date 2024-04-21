# Set up an onramp integrationBeta

View our full SDK reference to learn about all available methods, objects, and errors.

[full SDK reference](/crypto/using-the-api)

To integrate with the onramp SDK:

- Install the SDK and client library.

[Install the SDK and client library](#install)

- Generate a crypto onramp session on your backend.

[Generate a crypto onramp session](#onramp-session)

- Render the onramp UI on your website.

[Render the onramp UI](#onramp-ui)

- View your integration’s usage on the Stripe Dashboard.

[View your integration’s usage on the Stripe Dashboard](#dashboard)

[Install the SDK and client libraryclient-sideserver-side](#install)

## Install the SDK and client libraryclient-sideserver-side

Include the following scripts using script tags within the <head> element of your HTML. These scripts must always load directly from Stripe’s domains, https://js.stripe.com and https://crypto-js.stripe.com, for compatibility and PCI compliance. Don’t include the scripts in a bundle or host a copy yourself. If you do, your integration might break without warning.

[PCI compliance](/security/guide#validating-pci-compliance)

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

[https://crypto-js.stripe.com/crypto-onramp-outer.js](https://crypto-js.stripe.com/crypto-onramp-outer.js)

Use the npm package to load the onramp JS SDK as an ES module. The package includes Typescript type definitions.

[ES module](/crypto/esmodule)

Our official libraries don’t contain built-in support for the API endpoints because the onramp API is in limited beta. As a result, our examples use curl for backend interactions.

[Generate a crypto onramp sessionserver-side](#onramp-session)

## Generate a crypto onramp sessionserver-side

Generate a crypto onramp session by running the following curl command in your terminal:

[crypto onramp session](/crypto/using-the-api#api-reference)

Sample response:

You can see a full list of the parameters you can pass into Session creation in our API documentation.

[API documentation](/crypto/using-the-api#api-reference)

[Render the Onramp UIclient-side](#onramp-ui)

## Render the Onramp UIclient-side

Import both the StripeJS and the OnrampJS bundles (lines 8 and 9).

[https://js.stripe.com/v3/](https://js.stripe.com/v3/)

[https://crypto-js.stripe.com/crypto-onramp-outer.js](https://crypto-js.stripe.com/crypto-onramp-outer.js)

Use the client_secret from your server-side call in the previous step to initiate and mount the onramp session (lines 7 and 9).

After running the script, the onramp renders the following:

Test mode transaction amounts are overridden by our pre-decided limits.

Use the following values to complete an onramp transaction in test mode:

[test mode](/test-mode)

- On the OTP screen, use 000000 for the verification code.

- On the personal information screen, use 000000000 for SSN and address_full_match for address line 1.

- On the payment details screen, use the test credit card number 4242424242424242.

[View your integration's usage on the Stripe Dashboard](#dashboard)

## View your integration's usage on the Stripe Dashboard

After you’ve launched the Crypto Onramp, you can view customized usage reports in the Stripe Dashboard.

[Stripe Dashboard](https://dashboard.stripe.com/crypto-onramp/reports)

You can also return to the onboarding page to update the domains where you plan to host the onramp and check the status of any onboarding tasks.

[onboarding page](https://dashboard.stripe.com/crypto-onramp/onboarding)
