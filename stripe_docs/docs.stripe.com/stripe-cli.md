# Get started with the Stripe CLI

The Stripe CLI is a developer tool to help you build, test, and manage your integration with Stripe directly from the command line. It’s simple to install, works on macOS, Windows, and Linux, and offers a range of functionality to enhance your developer experience with Stripe. You can use the Stripe CLI to:

- Create, retrieve, update, or delete any of your Stripe resources in test mode (for example, create a product)

- Stream real-time API requests and events happening in your account

- Trigger events to test your webhooks integration

[Install the Stripe CLI](#install)

## Install the Stripe CLI

From the command-line, use an install script or download and extract a versioned archive file for your operating system to install the CLI.

To install the Stripe CLI with homebrew, run:

[homebrew](https://brew.sh/)

[Log in to the CLI](#login-account)

## Log in to the CLI

Login and authenticate your Stripe user Account to generate a set of restricted keys. To learn more, see Stripe CLI keys and permissions.

[Account](/get-started/account/activate)

[Stripe CLI keys and permissions](/stripe-cli/keys)

Press the Enter key on your keyboard to complete the authentication process in your browser.

[https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1](https://dashboard.stripe.com/stripecli/confirm_auth?t=THQdJfL3x12udFkNorJL8OF1iFlN8Az1)

- Optionally, if you don’t want to use a browser, use the --interactive flag to authenticate with an existing API secret key or restricted key. This can be helpful when authenticating to the CLI without a browser, such as in a CI/CD pipeline.

- Optionally, use the --api-key flag to specify your API secret key inline each time you send a request.

[Get started with a video](#get-started)

## Get started with a video

Watch this video to learn different ways to use the Stripe CLI. It covers how to configure the CLI, download sample code, and work with Stripe objects.

## Next steps

- Stream real-time events with the Stripe CLI

[Stream real-time events with the Stripe CLI](/webhooks#local-listener)
