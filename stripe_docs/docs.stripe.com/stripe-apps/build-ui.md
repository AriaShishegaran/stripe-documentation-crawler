# Build a UI

Give your app a user interface by using TypeScript, React, and Stripe’s UI Extensions SDK and UI toolkit to extend the Stripe Dashboard. This guide explains how to build a simple UI by creating and removing views.

[UI Extensions SDK](/stripe-apps/reference/extensions-sdk-api)

[UI toolkit](/stripe-apps/design)

For a more technical overview, learn how UI extensions work.

[learn how UI extensions work](/stripe-apps/how-ui-extensions-work)

[Add a view](#add-a-view)

## Add a view

Use views to develop your app UI. A view is a pairing of a React component and a specified viewport. The React component is composed of UI components from our UI toolkit. The viewport is the page or section of the Stripe Dashboard where you want to display it.

- Use the add command from your project root directory:Command Linestripe apps add view

Use the add command from your project root directory:

- Follow the prompts:Select the viewport for your view to appear in. See a list of available viewports.Name your view (for example, MyComponentName). The CLI suggests names based on your viewport selection.Stripe automatically adds your view to the views array in your app manifest, creates a new React component file in the src/views directory, and creates a unit test file alongside it.

Follow the prompts:

- Select the viewport for your view to appear in. See a list of available viewports.

[available viewports](/stripe-apps/reference/viewports)

- Name your view (for example, MyComponentName). The CLI suggests names based on your viewport selection.

Stripe automatically adds your view to the views array in your app manifest, creates a new React component file in the src/views directory, and creates a unit test file alongside it.

[app manifest](/stripe-apps/reference/app-manifest)

[Preview the application](#preview-the-application)

## Preview the application

You can run your app locally, make updates, and preview your changes in the Dashboard.

- From your project root directory, start the development server:Command Linestripe apps start

From your project root directory, start the development server:

- Press Enter to open your browser.

Press Enter to open your browser.

- Click Continue to preview your app in your Stripe account:

Click Continue to preview your app in your Stripe account:

- To stop the development server, type Ctrl+C from your command line.

To stop the development server, type Ctrl+C from your command line.

When the development server is running, you can make changes to your app and see them automatically in the Dashboard without refreshing the page. Until you resolve them, any errors automatically show up in the Stripe Dashboard, your browser’s dev tools, and the Stripe CLI.

You can disable previewing the local version of your app to preview a recently installed version of your app in test mode. If you’ve never installed any version of your app in test mode, you can’t switch previews.

[installed version of your app in test mode](/stripe-apps/upload-install-app)

To preview the most recently installed version of your app in test mode, run your development server and follow these steps:

- In your app, click the overflow menu  in the top right of your app.

- Click Turn off app preview, then Continue.

[Access Stripe objects in the Dashboard](#access-stripe-objects)

## Access Stripe objects in the Dashboard

When you assign a component to a viewport, the component can receive context about the Stripe object on that page using the environment.objectContext object.

For example, if you create a view that uses the stripe.dashboard.customer.detail viewport, the environment.objectContext object returns a customer object type and the current customer’s ID. You can then use those values to get more information about the Customer object and modify attributes like their address, description, and so on.

[Customer](/api/customers?lang=node)

For an index of the objects that a viewport gives, see viewports reference documentation.

[viewports reference documentation](/stripe-apps/reference/viewports)

The following code updates the customer name by using the Stripe Node.js API client and the viewport’s environment.objectContext ID:

[Stripe Node.js API client](/api?lang=node)

- Add the customer_write permission to your app:Command Linestripe apps grant permission "customer_write" "Allows the app to update the name of the customer."

Add the customer_write permission to your app:

- Use the Stripe API in your app to update the customer’s name:import {createHttpClient, STRIPE_API_KEY} from '@stripe/ui-extension-sdk/http_client';
import Stripe from 'stripe';

// Initiate communication with the stripe client.
const stripe = new Stripe(STRIPE_API_KEY, {
  httpClient: createHttpClient(),
  apiVersion: '2022-08-01',
})

const App = ({environment, userContext}) => {
  // Call the Stripe API to make updates to customer details.
  const updateCurrentCustomer = async (newCustomerName) => {
    try {
      // If the user has permission to update customers, this should succeed.
      const updatedCustomer = await stripe.customers.update(
        // We can use the current objectContext to get the customer ID.
        environment.objectContext.id,
        {name: newCustomerName}
      );

      console.log(updatedCustomer.name);
    } catch (error) {}
  };
}

Use the Stripe API in your app to update the customer’s name:

If your app changes data in the Dashboard, use the useRefreshDashboardData function to generate a callback that refreshes the data:

[useRefreshDashboardData](/stripe-apps/reference/extensions-sdk-api#useRefreshDashboardData)

[Use third-party APIs](#use-third-party-apis)

## Use third-party APIs

Your UI extension can call third-party APIs (your own API or any public API) to have your app request or send data.

- Use the grant url command to add the third-party API URL:Command Linestripe apps grant url "https://*.api.example.com/path/" "Send data to example service..."Connect-src URL must meet the following requirements:Use secure HTTPS protocol (example: https://www.example.com/api/users/).Contain a path (example: https://www.example.com/api/users/ URL is valid, not https://www.example.com/). Adding a base path with a trailing slash covers all paths after it (example: https://www.example.com/api/ enables calls to https://www.example.com/api/users/abc123/address).Can’t be a call to a Stripe API.If using a wildcard (*), it must be in the left-most DNS label (example: https://*.example.com/api/users/).Stripe Apps adds the URL in the connect-src array of your project’s app manifest:"ui_extension": {
    "views": [],
    "actions": [],
    "content_security_policy": {
      "connect-src": [
        "https://*.api.example.com/",
        "https://o0.ingest.example.io/api/",
      ],
      "purpose": "Send data to example service. The Example app sends data to the Example service to provide its functionality and sends anonymous error reports to our partner Example for debugging purposes"
    }
  }To remove a connect-src URL, you can also use the Stripe CLI:Command Linestripe apps revoke connect-src "https://*.api.example.com/path/"

Use the grant url command to add the third-party API URL:

[https://*.api.example.com/path/](https://*.api.example.com/path/)

Connect-src URL must meet the following requirements:

- Use secure HTTPS protocol (example: https://www.example.com/api/users/).

- Contain a path (example: https://www.example.com/api/users/ URL is valid, not https://www.example.com/). Adding a base path with a trailing slash covers all paths after it (example: https://www.example.com/api/ enables calls to https://www.example.com/api/users/abc123/address).

- Can’t be a call to a Stripe API.

- If using a wildcard (*), it must be in the left-most DNS label (example: https://*.example.com/api/users/).

Stripe Apps adds the URL in the connect-src array of your project’s app manifest:

[app manifest](/stripe-apps/reference/app-manifest)

[https://*.api.example.com/](https://*.api.example.com/)

[https://o0.ingest.example.io/api/](https://o0.ingest.example.io/api/)

To remove a connect-src URL, you can also use the Stripe CLI:

[https://*.api.example.com/path/](https://*.api.example.com/path/)

- To preview your app in the browser, start your development server and follow the CLI prompts:Command Linestripe apps start

To preview your app in the browser, start your development server and follow the CLI prompts:

- Add the fetch call with the URL of your third-party API in your app.For example, if you add the https://www.example.com/api/users connect-src URL to your app manifest, you could use this fetch call:const makeRequestToService = (endpoint, requestData) => {
  return fetch(`https://www.example.com/api/${endpoint}/`, {
    'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: requestData,
  });
};

Add the fetch call with the URL of your third-party API in your app.

For example, if you add the https://www.example.com/api/users connect-src URL to your app manifest, you could use this fetch call:

[app manifest](/stripe-apps/reference/app-manifest)

[https://www.example.com/api/${endpoint}/`,](https://www.example.com/api/${endpoint}/`,)

- To use different app manifest values in local development and production, load an extended manifest file.

To use different app manifest values in local development and production, load an extended manifest file.

[app manifest](/stripe-apps/reference/app-manifest)

[load an extended manifest file](/stripe-apps/reference/app-manifest#extended-manifest)

- If the third-party API has a JavaScript client library, you can add the dependency to your app using the npm add command.

If the third-party API has a JavaScript client library, you can add the dependency to your app using the npm add command.

[Debug the application](#debug-the-application)

## Debug the application

While developing your app, you can use your browser’s dev tools console as a debugging tool.

To isolate the messages related to your app:

- Find your app ID in the app manifest.

[app manifest](/stripe-apps/reference/app-manifest)

- On the Console panel of your dev tools browser, enter [Stripe App <your app ID>] in the Filter box. It should look something like [Stripe App com.example.helloworld].

[Write tests for your view](#write-tests-for-your-view)

## Write tests for your view

We recommend writing tests for your views. In addition to verifying that your view behaves as intended, unit tests also make it safer to make changes to code in the future.

When you create your view, the test file ending in .test.tsx contains a test of the default view:

You can run all your tests using the included Jest test runner with the npm run test or yarn test command. If you’ve used popular React testing tools like Testing Library and Enzyme, the test package included in @stripe/ui-extension-sdk/testing is most familiar.

[Jest](https://jestjs.io/)

[Testing Library](https://testing-library.com/docs/react-testing-library/intro)

[Enzyme](https://enzymejs.github.io/enzyme)

A typical test follows this pattern:

- Render your view.

- Make an assertion about the initial state, such as text existing.

- Interact with the view.

- Make an assertion about the new state, such as new text appearing.

For more methods and features of the test package, see UI testing reference.

[UI testing reference](/stripe-apps/ui-testing)

[OptionalRemove a view](#remove-a-view)

## OptionalRemove a view

## See also

- UI components

[UI components](/stripe-apps/components)

- Add an app settings page

[Add an app settings page](/stripe-apps/app-settings)
