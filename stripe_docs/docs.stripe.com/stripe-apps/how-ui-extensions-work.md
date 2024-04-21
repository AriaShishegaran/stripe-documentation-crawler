# How UI extensions work

Stripe Apps UI extensions let you render your own UI into Stripe’s products using TypeScript and React. These tools should be familiar if you’ve developed in React. But because they run within a secure sandbox embedded on another web page, they differ from standard browser-based React applications in several ways.

[TypeScript](https://www.typescriptlang.org/)

[React](https://reactjs.org/)

## Overview

- ​​Intro to React

[​​Intro to React](https://reactjs.org/tutorial/tutorial.html)

- ​​Get started with TypeScript

[​​Get started with TypeScript](https://www.typescriptlang.org/docs/)

- ​​Stripe’s UI components

[​​Stripe’s UI components](/stripe-apps/components)

UI extensions are written in TypeScript and use React to create UI using Stripe’s UI toolkit. Unlike other React environments, UI extensions don’t support arbitrary HTML. Instead, they exclusively use UI components provided by Stripe. The structure of a UI extension involves some key directories and files:

[Stripe’s UI toolkit](/stripe-apps/components)

- stripe-app.json: The app manifest. It describes how apps interact with Stripe, including what permissions they need, whether they have a UI extension, and—if so—where that extension appears in Stripe’s UI.

[app manifest](/stripe-apps/reference/app-manifest)

- package.json: NPM package metadata. The UI extensions are regular NPM packages. You can manage dependencies using npm or yarn.

[NPM packages](https://docs.npmjs.com/about-packages-and-modules)

[npm](https://docs.npmjs.com/cli)

[yarn](https://yarnpkg.com/)

- src: The actual TypeScript source code for the UI extension. By default, the CLI places a generic view in src/views with a corresponding entry in stripe-app.json.

Developing a UI extension relies on the Stripe CLI app plugin. The CLI takes care of initializing apps with the correct structure, configuring the app manifest, running a development server, and bundling the app appropriately for submission to Stripe.

- As the app developer, you write views, which are React components registered to appear whenever a specific viewport appears on the screen. For example, to make a view appear whenever a user is viewing an invoice details page, register it to the viewport stripe.dashboard.invoice.detail.

[viewport](/stripe-apps/reference/viewports)

- When you’re ready to upload your app, CLI commands help you bundle up your code, upload it to Stripe, and host your app on Stripe’s CDN.

- When your app’s UI extension gets initialized, Stripe downloads the app’s code into a sandboxed iframe.

- When a user goes to a page that has a particular viewport (for example, /invoices/inv_1283):Stripe defines the UI extension’s view inside the sandbox with the context provided by the viewport.Stripe passes the view to the Dashboard to be displayed to users.When users interact with the UI extension (for example, by clicking a button), event handlers in the UI extension sandbox receive the event and can update the view.

- Stripe defines the UI extension’s view inside the sandbox with the context provided by the viewport.

- Stripe passes the view to the Dashboard to be displayed to users.

- When users interact with the UI extension (for example, by clicking a button), event handlers in the UI extension sandbox receive the event and can update the view.

## Views and viewports

To display UI to users of an app, create a React view and register it with a viewport.

Views are React components that the app exports. Viewports are identifiers that indicate where the view displays. When you upload an app, all views exported by the app register with the associated viewport.

Views automatically register with viewports when you run stripe apps add view. Behind the scenes, this adds an entry to the app manifest.

[app manifest](/stripe-apps/reference/app-manifest)

## Lifecycle of a UI extension

UI extensions run in an invisible, sandboxed iframe that asynchronously sends UI updates to the Stripe Dashboard, which then displays the UI updates. A single sandbox can accommodate multiple views at the same time.

The lifecycle of the sandbox and the views it powers works like this:

- The Dashboard loads the UI extension sandbox, which happens between when the Dashboard loads and when the user opens the app.

- When a view needs to be displayed, the Dashboard waits for the sandbox to be initialized, and then directs the sandbox to mount the correct view and passes in the appropriate context.

[appropriate context](/stripe-apps/reference/extensions-sdk-api#props)

- When the user dismisses the view (for example, when they close the app drawer), the view unmounts. Unmounting the view removes it from the DOM and from the sandboxed React tree.

- The sandbox might stay running or shut down depending on resource usage. The only guarantee is that the Dashboard makes a best-effort attempt to allow useEffect and other cleanup handlers to run before terminating the sandbox.

[useEffect](https://reactjs.org/docs/hooks-effect.html)

Lifecyle of a Stripe Apps UI extension

## Sandbox limitations

Because of the unique sandbox environment where UI extension code runs, a Stripe Apps UI extension can’t do everything that a regular React app running in a full browser context can do.

- Stripe Apps don’t have direct access to the DOM. They run in an iframe with a separate DOM that’s invisible from the Dashboard.

- The Dashboard proxies and serializes all data to the app. UI toolkit components only accept serializable data.

- The Dashboard also proxies and serializes all props to the app, so functions passed to or triggered by UI toolkit components are asynchronous.

The restrictions below affect what you can do with React and JavaScript when developing your app. The React tree doesn’t render to the DOM until the Stripe Dashboard host environment deserializes and evaluates it. The DOM for the app updates, and the instance of React in the Dashboard manages data input.

The DOM environment that the UI extension code is running in is locked down by the sandboxed iframe. This means that top-level APIs like localStorage, indexedDB, and BroadcastChannel are unavailable. Any DOM API that relies on the same-origin policy doesn’t work as expected because sandboxed iframes have a null origin.

[sandboxed iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-sandbox)

[localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)

[indexedDB](https://developer.mozilla.org/en-US/docs/web/api/indexeddb)

[BroadcastChannel](https://developer.mozilla.org/en-US/docs/web/api/broadcastchannel)

[same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)

UI components don’t support React ref props because the React tree is serialized and passed to the Stripe Dashboard to be rendered. The DOM that the components are eventually rendered into is inaccessible from the sandboxed App code.

The default package.json file generated with each Stripe app has a dependency entry for react, but changing this version has no effect on the version of React that renders your app. The Stripe Dashboard uses its version of React (currently version 17) to render all apps. The react dependency in the local package.json only performs type checking and unit testing and you shouldn’t change it (unless instructed by Stripe) to ensure compatibility.

The Dashboard serializes and proxies all data input to the app, which results in input lag while using React controlled components. This lag is perceptible by the user and can potentially overwrite characters that they typed in the meantime. It also results in the cursor skipping to the end of a text input if they try to edit text at the beginning.

[controlled components](https://reactjs.org/docs/forms.html#controlled-components)

To reduce lag in your app, use user inputs in an uncontrolled manner:

The restrictions below apply to UI components. While your extension runs in an isolated environment, UI components render directly in the Dashboard. The SDK informs the Dashboard to render UI toolkit components, which results in the following limitations.

[UI components](/stripe-apps/components)

Because event handlers are called asynchronously, the event has already propagated by the time the app’s event handler is called. As a result, the app can’t stop event propagation or bubbling.

UI components only accept serializable data types. Passing unserializable data types like Map or Set as a prop to a UI Toolkit component throws an error.

Use only simple types, functions, or React events as props. Supported types are:

- Strings, numbers, true, false, null, and undefined

- Objects whose keys and values are all simple types

- Arrays whose values are all simple types

- Functions, but they become asynchronous when proxied. Any functions passed as arguments or returned are also subject to the type limitations

- React events

React renders synchronously, but functions passed to UI components become asynchronous after the Dashboard proxies them to the app. Functions that generate markup passed to a UI component don’t finish rendering in time for React to use their results. As a result, no UI components accept render functions.

This means that the following patterns don’t work:

UI components support props that take a single React element:

More complex JSX data structures are unsupported, however:

If you need to pass multiple React elements to a UI component, wrap them in a fragment:

A similar constraint applies to children. Arrays and objects containing JSX are unsupported, but multiple React elements are allowed:

## Installing NPM Packages

There aren’t any restrictions on adding third-party NPM packages to Stripe Apps; feel free to install packages as you see fit. However, not all packages work as expected given the sandbox limitations of UI extensions.

[sandbox limitations](/stripe-apps/how-ui-extensions-work#sandbox-limitations)

Using a utility library like lodash is fine, because lodash doesn’t require DOM access:

Using a form library like react-hook-form won’t work because react-hook-form uses Refs to manage form state:

## See also

- Build and test views

[Build and test views](/stripe-apps/build-ui)

- Design your app

[Design your app](/stripe-apps/design)

- Style your app

[Style your app](/stripe-apps/style)

- Distribution options

[Distribution options](/stripe-apps/distribution-options)
