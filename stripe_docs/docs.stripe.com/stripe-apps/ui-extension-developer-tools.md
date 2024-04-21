# UI extension developer tools

When you create an app using the Stripe CLI, the generated package includes development environment tooling with best practices built in to help you build a UI extension. This document details the tools that we include and how to modify them (if desired) to suit your app.

[create an app](/stripe-apps/create-app)

## Type checking

Apps come with Typescript support, and all of the supporting packages we ship have type definitions to aid development. Typescript warnings display in supported code editors automatically, but you can also check your code using the command line:

[Typescript](https://www.typescriptlang.org)

Your app’s root directory has a tsconfig.json file that extends our recommended configuration in the @stripe/ui-extension-tools package. Most developers won’t need to modify this file, but advanced users can add their own properties or even remove the extends property and create their own Typescript configuration.

To enable image imports, we include a ui-extensions.d.ts type definition file that references type definitions from the @stripe/ui-extension-tools package. We don’t recommend removing this file because it’s a helpful indicator of what image types our CLI can process.

## Linting

Linting (checking code for syntax and formatting errors) is an invaluable developer tool, and apps come with an ESLint configuration. We include best-practice linter rules and also Stripe-specfic rules to prevent common mistakes. Linting warnings display in supported code editors automatically, but you can also check your code using the command line:

[ESLint](https://eslint.org)

The ESLint configuration is in the package.json file in the eslintConfig property. It extends the configuration in the @stripe/ui-extension-tools package. Most developers won’t need to modify this configuration, but advanced users can add their own properties or even remove the extends property and create their own set of linting rules.

## Testing

App developers can write unit tests for their React components and utility functions using the bundled test harness built with Jest. Run your tests on the command line:

[write unit tests](/stripe-apps/ui-testing)

[Jest](https://jestjs.io)

Your app’s root directory has a jest.config.js file that extends our recommended configuration in the @stripe/ui-extension-tools package. Most developers won’t need to modify this file, but advanced users can add their own properties or even remove the import and create their own configuration.

[OptionalUpdate older apps to use the ui-extension-tools package](#migrating-ui-extension-tools)

## OptionalUpdate older apps to use the ui-extension-tools package

## See also

- How UI extensions work

[How UI extensions work](/stripe-apps/how-ui-extensions-work)

- UI testing

[UI testing](/stripe-apps/ui-testing)
