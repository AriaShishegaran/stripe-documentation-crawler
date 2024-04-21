# Get started with Connect embedded components

Use Connect embedded components to add connected account dashboard functionality to your website. These libraries and their supporting API allow you to grant your users access to Stripe products directly in your dashboard.

For an immersive version of this guide, see the Connect embedded components integration quickstart. You can also download a sample integration from there. To customize the appearance of Connect embedded components, use the appearance options when you initialize StripeConnectInstance. See the full list of appearance parameters.

[Connect embedded components integration quickstart](/connect/connect-embedded-components/quickstart)

[full list of appearance parameters](/connect/customize-connect-embedded-components)

[Initialize Connect.jsClient-sideServer-side](#account-sessions)

## Initialize Connect.jsClient-sideServer-side

Stripe uses an AccountSession to express your intent to delegate API access to your connected account.

[AccountSession](/api/account_sessions)

The AccountSessions API returns a client secret that allows an embedded component in the web client to access a connected account’s resources as if you were making the API calls for them.

[client secret](/api/account_sessions/object#account_session_object-client_secret)

In a single page application, your client initiates a request to obtain the account session to your server. You can create a new endpoint on your server that returns the client secret to the browser:

Install the npm package to use Connect.js as a module.

[npm package](https://github.com/stripe/connect-js)

Call loadConnectAndInitialize with your publishable key and a function that retrieves a client secret by calling the new endpoint you created on your server. Use the returned StripeConnectInstance to create embedded components. After initializing Connect.js, you can mount components to or unmount components from the DOM at any time. That includes any elements rendered inside React or Vue portals.

To create a component, call create on the StripeConnectInstance that you created above, then pass in the component name. This returns a custom element that Connect.js registers and uses to automatically wire your DOM up to Stripe. You can then append this element to your DOM.

[custom element](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements)

Call create with payments, then add the result to your DOM to render a payments UI.

See a complete list of supported embedded components →

[See a complete list of supported embedded components →](/connect/supported-embedded-components)

[Configuring Connect.jsClient-side](#configuring-connect-js)

## Configuring Connect.jsClient-side

The loadConnectAndInitialize method on the client takes several different options to configure Connect.js.

[publishable key](/keys)

[client secret](/api/account_sessions/object#account_session_object-client_secret)

[locale](#supported-languages)

[CssFontSource](/connect/get-started-connect-embedded-components#css-font-source)

[CustomFontSource](/connect/get-started-connect-embedded-components#custom-font-source)

## Customize the look of Connect embedded components

We offer a set of options to customize the look and feel of Connect embedded components. These customizations affect buttons, icons, and other accents in our design system.

You can set these options when initializing StripeConnectInstance by passing values to the appearance object. You can only use the Connect.js options to modify styles in Connect embedded components. The font family and background color of Connect embedded components can be overridden with CSS selectors, but Stripe doesn’t support overriding any other styles.

[Connect.js options](/connect/get-started-connect-embedded-components#configuring-connect-js)

[https://myfonts.example.com/mycssfile.css](https://myfonts.example.com/mycssfile.css)

[https://my-domain.com/assets/my-font-2.woff)`,](https://my-domain.com/assets/my-font-2.woff)`,)

The fonts object in stripeConnect.initialize takes an array of CssFontSource or CustomFontSource objects.

[CssFontSource](/js/appendix/css_font_source_object)

[CustomFontSource](/js/appendix/custom_font_source_object)

If you’re using custom fonts in your page (that is, .woff or .tff files), you must specify these files when initializing Connect embedded components. Doing this allows Connect embedded components to properly render these fonts. You can specify these as:

Use this object to pass a stylesheet URL that defines your custom fonts when creating a StripeConnectInstance. With a CssFontSource object, your CSP configuration must allow fetching the domains associated with the CSS file URLs specified as CssFontSource.

[CSP configuration](/connect/get-started-connect-embedded-components#csp-and-http-header-requirements)

[@font-face](https://developer.mozilla.org/en/docs/Web/CSS/@font-face)

[content security policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)

[additional directives](/security/guide#content-security-policy)

Use this object to pass custom fonts when creating a StripeConnectInstance.

[src](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/src)

[font-display](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display)

[unicode-range](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/unicode-range)

[font-weight](https://developer.mozilla.org/en-US/docs/Web/CSS/font-weight)

The appearance object in loadConnectAndInitialize takes the following optional properties:

[full list of appearance variables](/connect/embedded-appearance-options)

The update method supports updating Connect embedded components after initialization. This is useful for switching appearance options at runtime (without refreshing the page). To do so, use the same stripeConnectInstance object you created with initialize and call the update method on it:

Not all options (e.g. fonts) are updatable. The supported options for this method are a subset of the options offered in initialize. This supports updating the appearance and locale.

Connect embedded components behave like regular block HTML elements. By default, they take 100% of the width of their parent HTML element, and grow in height according to the content rendered inside. You can control the width of Connect embedded components by specifying the width of the HTML parent. You can’t directly control the height as that depends on the rendered content, however, you can limit the height with maxHeight and overflow: scroll, just like with other HTML block elements.

## Authentication

We offer a set of APIs to manage account sessions and user credentials in Connect embedded components.

On long running sessions, the session from the initially provided client secret might expire. When it expires, we automatically use fetchClientSecret to retrieve a new client secret and refresh the session. You don’t need to pass in any additional parameters.

[client secret](/api/account_sessions/object#account_session_object-client_secret)

We recommend that you call logout on the stripeConnectInstance to destroy the associated account session object after a user logs out of your app. This disables all Connect embedded components that link to that stripeConnectInstance.

## CSP and HTTP header requirements

If your website implements a Content Security Policy, you need to update the policy by adding the following rules:

[Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)

- frame-src https://connect-js.stripe.com https://js.stripe.com

- img-src https://*.stripe.com

- script-src https://connect-js.stripe.com https://js.stripe.com

- style-src sha256-0hAheEzaMe6uXIKV4EehS9pu1am1lj/KnnzrOYqckXk= (SHA of empty style element)

If you’re using a CSS file to load web fonts for use with Connect embedded components, its URL must be allowed by your connect-src CSP directive.

[web fonts](/connect/get-started-connect-embedded-components#fonts-object)

[connect-src](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/connect-src)

Setting certain HTTP response headers enables the full functionality of Connect embedded components:

[HTTP response headers](https://developer.mozilla.org/en-US/docs/Glossary/Response_header)

- Cross-Origin-Opener-Policy, unsafe-none. Note: this is the default value of the header, so not setting this header works.

[Cross-Origin-Opener-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cross-Origin-Opener-Policy)

## Supported browsers

We support the same set of browsers that the Stripe Dashboard currently supports:

[Stripe Dashboard currently supports](/dashboard/basics#browser-compatibility)

- The last 20 major versions of Chrome and Firefox

- The last two major versions of Safari and Edge

- The last two major versions of mobile Safari on iOS

Connect embedded components aren’t supported in webviews, they are only supported in standalone browsers.

## Supported languages

We localized Connect embedded components for the following languages:

[Integrate without frontend npm packages](#integrate-without-sdk)

## Integrate without frontend npm packages

We recommend integrating with our javascript and React component wrappers, which simplify the loading of Connect embedded components and provide TypeScript definitions for our supported interfaces. If your build system currently doesn’t support taking a dependency on packages, you can integrate without these packages.

[javascript](https://github.com/stripe/connect-js)

[React component wrappers](https://github.com/stripe/react-connect-js)

Manually add the Connect.js script tag to the <head> of each page on your site.

[https://connect-js.stripe.com/v1.0/connect.js](https://connect-js.stripe.com/v1.0/connect.js)

After Connect.js completes loading, it initializes the global window variable StripeConnect and calls StripeConnect.onLoad if you define it. You can safely initialize Connect.js by setting up an onload function and calling StripeConnect.init with the same Connect.js options as loadConnectAndInitialize.

[Connect.js options](/connect/get-started-connect-embedded-components#configuring-connect-js)

## User authentication in Connect embedded components

Connect embedded components typically don’t require user authentication–they’ll offer the functionality they’re configured for directly. In some cases, Connect embedded components requires the user to sign in with their Stripe account to perform the necessary functionality required by that component (for example, writing information to the account legal entity in the case of the account onboarding component).

[account onboarding](/connect/supported-embedded-components/account-onboarding)

Authentication involves a popup to a Stripe owned window. When the user completes authentication in that popup, it closes and the user can continue their workflow.

The account onboarding and account management components require authentication to boot. Other components might require user authentication within the component after the initial render. Authentication in these components and scenarios is required for all Connect account types except Custom accounts where the platform hasn’t configured external account collection within the Stripe dashboard.

[account onboarding](/connect/supported-embedded-components/account-onboarding)

[account management](/connect/supported-embedded-components/account-onboarding)

[Custom](/connect/custom-accounts)

[Stripe dashboard](https://dashboard.stripe.com/settings/connect/payouts/onboarding)
