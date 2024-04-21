htmlGo-live checklist | Stripe Documentation[Skip to content](#main-content)Go-live checklist[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Fchecklist%2Fgo-live)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Fchecklist%2Fgo-live)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)
Your account[Create an account](#)Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Get started](/docs/get-started)Checklists# Go-live checklist

Use this checklist to ensure a smooth transition when taking your integration live.NoteBecome a Stripe Partner to access additional best practices and receive relevant news and updates from Stripe.

### Checklist progress

As you complete each item and check it off, the state of each checkbox is stored within your browser’s cache. You can refer back to this page at any time to see what you’ve completed so far.

You can log in to see some of your current settings.

Stripe has designed its live and test modes to function as similarly as possible. Flipping the switch is mostly a matter of swapping your API keys.

If you are a developer, or had a developer perform an integration for you, you should also consider the following items before going live. If you’re using Stripe through a connected website or a plug-in, most won’t apply.

- Set the API versionWarningAll requests use your account API settings, unless you override the API version. The changelog lists every available version. Note that by default webhook events are structured according to your account API version, unless you set an API version during endpoint creation.

If you’re using a strongly typed language (Go, Java, TypeScript, .NET), the server-side library pins the API version based on the library version being used. If you’re not familiar with how Stripe manages versioning, please see the versioning docs.

To make sure everything is in sync:

  - Upgrade to the latest API version in your[Stripe Dashboard](https://dashboard.stripe.com/developers)
  - For dynamic languages (Node.js, PHP, Python, Ruby):[set the API version](/libraries#server-side-libraries)in the server-side library
  - For strongly typed languages (Go, Java, TypeScript, .NET):[upgrade to the latest version](/libraries#server-side-libraries)of your chosen library


- Handle edge casesWe’ve created several test values you can use to replicate various states and responses. Beyond these options, perform your due diligence, testing your integration with:

  - Incomplete data
  - Invalid data
  - Duplicate data (for example, retry the same request to see what happens)We also recommend you have someone else test your integration, especially if that other person isn’t a developer themselves.


- Review your API error handlingOnce you’ve gone live is an unfortunate time to discover you’ve not properly written your code to handle every possible error type, including those that should “never” happen. Be certain your code is defensive, handling not just the common errors, but all possibilities.

When testing your error handling, pay close attention to what information is shown to your users. A card being declined (that is, a card_error) is a different concern than an error on your backend (for example, an invalid_request_error).


- Review your loggingStripe logs every request made with your API keys, with these records being viewable in the Dashboard. We recommend that you log all important data on your end, too, despite the apparent redundancy. Your own logs will be a life-saver if your server has a problem contacting Stripe or there’s an issue with your API keys—both cases would prevent us from logging your request.

Regularly examine your logs to ensure they’re storing only the information you need and not anything of a sensitive nature (for example, credit card details or personally identifiable information).


- Ensure you're not relying on test mode objectsStripe objects created in test mode—such as plans, coupons, products, and SKUs—are not usable in live mode. This prevents your test data from being inadvertently used in your production code. When recreating necessary objects in live mode, be certain to use the same ID values (for example, the same plan ID, not the same name) to guarantee your code will continue to work without issue.


- Ensure you've registered your production webhooksYour Stripe account can have both test and live webhook endpoints. If you’re using webhooks, make sure you’ve defined live endpoints in your Stripe account. Then confirm that the live endpoint functions exactly the same as your test endpoint.

While examining your webhooks status, also take a moment to check that your production endpoint:

  - Gracefully handles delayed webhook notifications
  - Gracefully handles duplicate webhook notifications
  - Does not require event notifications to occur in a specific order


- Subscribe to the API announcements mailing listWe recommend all developers subscribe to our API updates mailing list to keep up with new features as we release them.


- Change and secure your API keysAs a security measure, we recommend rolling your API keys on a regular basis, and also just before going live. This is in case they have been saved somewhere outside of your codebase during development. Make sure your workflow doesn’t result in your API keys being represented or stored in multiple places—this leads to bugs—or even ending up in your version control software.



Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`