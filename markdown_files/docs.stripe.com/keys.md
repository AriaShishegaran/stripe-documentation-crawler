htmlAPI keys | Stripe Documentation[Skip to content](#main-content)API keys[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fkeys)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fkeys)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/development)[Building your integration](#)Developer tools[SDKs](#)[API](#)
[Testing](#)[Webhooks](#)[Stripe CLI](#)[Stripe Shell](#)[Developer Dashboard](#)[Workbench](#)[Stripe for Visual Studio Code](/docs/stripe-vscode)[File uploads](/docs/file-upload)[Feedback](/docs/dev-tools-csat)Resources[Security](#)[Sample projects](#)[Videos](#)Extend Stripe[Stripe Apps](#)[Stripe Connectors](#)Partners[Partner ecosystem](/docs/partners)[Partner certification](/docs/partners/training-and-certification)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Developer tools](/docs/development)API# API keys

Use API keys to authenticate API requests.Stripe authenticates your API requests using your account’s API keys. If a request doesn’t include a valid key, Stripe returns an invalid request error. If a request includes a deleted or expired key, Stripe returns an authentication error.

Use the Developers Dashboard to create, reveal, delete, and roll API keys. To access your v1 API keys, select the API Keys tab in your Dashboard.

## Test mode versus live mode

All Stripe API requests occur in either test mode or live mode. Use test mode to access test data, and live mode to access actual account data. Each mode has its own set of API keys. Objects in one mode aren’t accessible to the other. For instance, a test-mode product object can’t be part of a live-mode payment.

Live mode key accessYou can only reveal a live mode secret or restricted API key one time. If you lose it, you can’t retrieve it from the Dashboard. In that case, roll it or delete it and create a new one.

TypeWhen to useObjectsHow to useConsiderationstest modeUse test mode, and its associated test API keys, as you build your integration. In test mode, card networks and payment providers don’t process payments.API calls return simulated objects. For example, you can retrieve and use test`account`,`payment`,`customer`,`charge`,`refund`,`transfer`,`balance`, and`subscription`objects.Use[test credit cards and accounts](/testing#cards). You can’t accept real payment methods or work with real accounts.[Identity](/identity)doesn’t perform any verification checks. Also, Connect[account objects](/api/accounts/object)don’t return sensitive fields.live modeUse live mode, and its associated live API keys, when you’re ready to launch your integration and accept real money. In live mode, card networks and payment providers do process payments.API calls return real objects. For example, you can retrieve and use real`account`,`payment`,`customer`,`charge`,`refund`,`transfer`,`balance`, and`subscription`objects.Accept real credit cards and work with customer accounts. You can accept actual payment authorizations, charges, and captures for credit cards and accounts.Disputes have a more nuanced flow and a simpler[testing process](/testing#disputes). Also, some[payment methods](/payments/payment-methods)have a more nuanced flow and require more steps.## Secret and publishable keys

All accounts have a total of four API keys by default—two for test mode and two for live mode:

1. Test mode secret key: Use this key to authenticate requests on your server when in test mode. By default, you can use this key to perform any API request without restriction.
2. Test mode publishable key: Use this key for testing purposes in your web or mobile app’s client-side code.
3. Live mode secret key: Use this key to authenticate requests on your server when in live mode. By default, you can use this key to perform any API request without restriction.
4. Live mode publishable key: Use this key, when you’re ready to launch your app, in your web or mobile app’s client-side code.

Testing and developmentUse only your test API keys for testing and development. This ensures that you don’t accidentally modify your live customers or charges.

You can find your secret and publishable keys on the API keys page in the Developers Dashboard. While you’re logged in, Stripe documentation automatically populates code examples with your test mode API keys. (Only you can see these values). If you’re not logged in, our code examples include randomly generated API keys. Replace them with your own test keys or log in to see the code examples populated with your own test API keys. If you can’t view your API keys, ask the owner of your Stripe account to add you to their team with the proper permissions.

The following table shows randomly generated examples of secret and publishable test API keys:

Restricted API keysThe Dashboard can also include restricted API keys, which allow customizable limited access to the API. Stripe doesn’t provide any restricted keys by default.

TypeValueWhen to useSecret`sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz`On the server side: Must be secret and stored securely in your web or mobile app’s server-side code (such as in an environment variable or credential management system) to call Stripe APIs. Don’t expose this key on a website or embed it in a mobile application.Publishable`pk_test_VOOyyYjgzqdm8I3SrBqmh9qY`On the client side: Can be publicly accessible in your web or mobile app’s client-side code (such as checkout.js) to securely collect payment information, such as with[Stripe Elements](/payments/elements). By default,[Stripe Checkout](/payments/checkout)securely collects payment information.RestrictedA string that starts with`rk_test_`In microservices: Must be secret and stored securely in your microservice code to call Stripe APIs. Don’t expose this key on a website or embed it in a mobile application.### Keep your keys safe

Anyone can use your live mode secret API key to make any API call on behalf of your account, such as creating a charge or performing a refund. Keep your keys safe by following the secret API keys best practices.

Customize API access with restricted API keys![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

To provide limited access to the API, create restricted API keys. You can configure a restricted API key to allow read or write access to specific API resources. When using microservices that interact with the API on your behalf, define restricted keys that allow only the minimum access those microservices require. For example, if you use a dispute monitoring service, create a restricted key that only provides read access to dispute-related resources. That key allows the service to get the data it needs, but doesn’t allow it to make any changes or access any other data.

Restricted keys can’t interact with many parts of Stripe’s API because they’re only intended to reduce risk when using or building microservices. Don’t use restricted keys as an alternative to your account’s secret or publishable API keys during development of your Stripe integration.

Permission errorsIf you use a restricted API key in a call it doesn’t have access to, Stripe raises a permission error.

Limit the IP addresses that can send API requests![](https://b.stripecdn.com/docs-statics-srv/assets/fcc3a1c24df6fcffface6110ca4963de.svg)

You can increase the security of a secret or restricted key by limiting the IP addresses that can use it to send API requests. Additionally, you can restrict a key to one or more IP addresses or to a range of IP addresses.

## Reveal a secret API key for test mode

In test mode, you can reveal a secret API key as many times as you want.

To reveal a secret key in test mode:

1. In the Developers Dashboard, select the[API keys](https://dashboard.stripe.com/test/apikeys)tab.
2. In theStandard keyslist, in theSecret keyrow, clickReveal test key.
3. Copy the key value by clicking it.
4. Save the key value.
5. ClickHide test key.

## Reveal a secret or restricted API key for live mode

For security, in live mode Stripe only shows you a secret or restricted API key one time. Store the key in a safe place where you won’t lose it. To help yourself remember where you stored it, you can leave a note on the key in the Dashboard. If you lose the key, you can roll it or delete it and create another.

You can't reveal a live mode secret key that you createdAfter you create a secret or restricted API key in live mode, we display the value before you save it. You must copy the value before saving it because you can’t reveal it later. You can only reveal a default secret key or a key generated by a scheduled roll.

To reveal a secret or restricted key in live mode and attach a note:

NoteThe API keys link here opens in live mode.

1. In the Developers Dashboard, select the[API keys](https://dashboard.stripe.com/apikeys)tab.
2. In theStandard keyslist orRestricted keyslist, in the row for the key you want to reveal, clickReveal live key.
3. Copy the key value by clicking it.
4. Save the key value.
5. ClickHide test key.
6. Click the overflow menu () next to the key, then selectEdit key….
7. In theNotefield, enter the location where you saved the key, then clickSave.
8. If you created the key before Stripe introduced this feature, clickHide live key.

NoteKeys that you created before Stripe introduced this feature aren’t automatically hidden when they’re revealed. You must manually hide them.

## Roll an API key

Rolling a key revokes it and generates a replacement key. You can roll a key immediately or schedule a key to roll after a certain time. Roll a key in scenarios such as the following examples:

- If you’re in live mode and you lose a secret key or restricted key, you can’t recover it from the Dashboard and must replace it.
- If a secret or restricted key is compromised, you need to revoke it to block any potentially malicious API requests that might use it.
- Your policy requires rotating keys at certain intervals.

To roll an API key:

1. Open the[API keys](https://dashboard.stripe.com/test/apikeys)page.
2. In the row for the key you want to roll, click the overflow menu (), then selectRoll key….
3. Choose an expiration date from theExpirationdropdown.
4. ClickRoll API key.
5. The dialog displays the new key value. Copy it by clicking it.
6. Save the key value. You can’t retrieve it later.
7. In theAdd a notefield, enter the location where you saved the key and clickDoneorSave.

If you chose Now for the Expiration, we delete the old key. If you selected a different time, you can see the time remaining until the key expires below its name.

Regardless of the old key’s expiration time, the new key is ready to use immediately.

When you roll a publishable key, the replacement key’s name is always Publishable key. When you roll a secret key, the replacement key’s name is always Secret key. When you roll a restricted key, the replacement key’s name is the same as the rolled key. You can rename a secret or restricted key by clicking its overflow menu and selecting Edit key….

## Delete a secret or restricted API key

If you delete a key, any code that uses that key can no longer make API calls. Create a new key and update the code to use it.

NoteYou can’t delete a publishable key.

To delete a key:

1. In the Developers Dashboard, select the[API keys](https://dashboard.stripe.com/test/apikeys)tab.
2. Locate the key you want to delete in either theStandard keysorRestricted keyslist. Click the overflow menu icon () in the row of that key, then selectDelete key….
3. In the Delete API key dialog, if you’re sure that you want to delete the key, clickDelete key. Otherwise, clickCancel.

## Create a secret API key

To create a secret API key:

1. Open the[API keys](https://dashboard.stripe.com/test/apikeys)page.
2. ClickCreate secret key.
3. Stripe sends a verification code to your email address or in a text message. (As with any email or text message, it might not arrive immediately.) Enter the code in the dialog. If the dialog doesn’t continue automatically, clickContinue.
4. Enter a name in theKey namefield.
5. ClickCreate.
6. The dialog displays the new key value. Copy it by clicking it.
7. Save the key value. You can’t retrieve it later.
8. In theAdd a notefield, enter the location where you saved the key and clickDone.

## Create a restricted API key

A restricted API key only allows the level of access that you specify.

To create a restricted API key:

1. Open the[API keys](https://dashboard.stripe.com/test/apikeys)page.
2. You can create a restricted key from scratch or start by cloning an existing restricted key.  - To create a restricted key from scratch, clickCreate restricted key. In this case, the default value for all permissions isNone.
  - To clone an existing key, in the row for the key you want to clone, click the overflow menu (), then selectDuplicate key…. In this case, the default value for each permission is its value in the cloned key.


3. In theKey namefield, enter a name. If you cloned an existing key, the default name is the cloned key’s name.
4. For each resource you want the new key to access, select the permission for this key to allow. If you use Connect, you can also select the permission for this key to allow when accessing connected accounts. Available permissions areNone,Read, orWrite.
5. ClickCreate key.
6. Stripe sends a verification code to your email address or in a text message. (As with any email or text message, it might not arrive immediately.) Enter the code in the dialog. If the dialog doesn’t continue automatically, clickContinue.
7. The dialog displays the new key value. Copy it by clicking it.
8. Save the key value. You can’t retrieve it later.
9. In theAdd a notefield, enter the location where you saved the key and clickDone.

## Limit secret or restricted keys to a list or range of IP addresses

To limit API requests using a key to one or more specific IP addresses or to a range of IP addresses:

Valid IP address rangesIf you specify a range of IP addresses, they can only span the fourth byte of the address. All addresses in the range must have the same first three bytes. For example, a valid range could be 100.10.38.1 - 100.10.38.12, specified as 100.10.38.1/12. All addresses in the range must start with 100.10.38.

1. Open the[API keys](https://dashboard.stripe.com/test/apikeys)page.
2. In theStandard keyslist orRestricted keyslist, in the row for the key you want to reveal, click the overflow menu (), then selectManage IP restrictions….
3. ClickRestrict IP addresses that can use the API key.
4. Enter a list or range of IP addresses:  - For a list of IP addresses, enter the first IP address in the fields. For each additional IP address, click+ Add IP addressand enter the address.
  - For a range of IP addresses, clickCIDR, then enter the range in Classless Inter-Domain Routing (CIDR) notation. In the first three fields, enter the first three numbers of the IP addresses in the range. In the fourth and fifth fields, enter the fourth number of the first and last addresses in the range, respectively.


5. ClickSave.

ShortcuttingPress Ctrl+V or ⌘+V with a valid IP address on your clipboard to input text into all of the fields.

## Change a secret or restricted API key’s name or note

To change the name or note text of a secret or restricted key:

1. Open the[API keys](https://dashboard.stripe.com/test/apikeys)page.
2. In the row for the key you want to change, click the overflow menu (), then selectEdit key….
3. If you want to change the name, inKey name, enter the new name.
4. If you want to change the note text, inNote, enter the new note text.
5. ClickSave.

## View the API request logs

To open the API request logs, click the overflow menu () for any key, then select View request logs. Opening the logs redirects you to the main Stripe Dashboard.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Test mode versus live mode](#test-live-modes)[Secret and publishable keys](#obtain-api-keys)[Reveal a secret API key for test mode](#reveal-an-api-secret-key-for-test-mode)[Reveal a secret or restricted API key for live mode](#reveal-an-api-secret-key-live-mode)[Roll an API key](#rolling-keys)[Delete a secret or restricted API key](#delete-secret-key)[Create a secret API key](#create-api-secret-key)[Create a restricted API key](#create-restricted-api-secret-key)[Limit secret or restricted keys to a list or range of IP addresses](#limit-api-secret-keys-ip-address)[Change a secret or restricted API key’s name or note](#change-key-name-or-note)[View the API request logs](#view-request-logs)Related Guides[Testing](/docs/testing)[Test mode](/docs/test-mode)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`