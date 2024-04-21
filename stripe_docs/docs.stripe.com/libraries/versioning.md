# Stripe versioning and support policy

## Stripe API versions

Stripe’s API versioning policy is based on the release date. For example, 2023-01-15. We release a new API version together with a new version of the SDK. To understand what to expect from a new API version, see API upgrades.

[API upgrades](/upgrades)

## Stripe SDK versions

Stripe’s SDK versioning policy is based on the semantic versioning standard. For example, in version 4.3.2, 4 is the major, 3 is the minor, and 2 is the patch. When we release a new SDK version for new features or bug fixes, we increment one of these three version components depending on the type of change introduced.

- Major. We increment the major version component when the version contains breaking changes that are backwards incompatible with the latest version: to add a required parameter, change a type, property, method, or parameter. For example, renaming the SDK’s exception classes.

- Minor. We increment the minor version component when the version contains new features that are backwards compatible with the latest version: to add a new type, property, method, optional parameter, or supported parameter value. For example, clarifying the SDK’s metadata deletion message.

- Patch. We increment the patch version component when the version contains backward-compatible bug fixes: to modify a behavior if correcting that behavior doesn’t change any documented types, properties, methods, or parameters. For example, fixing a bug where file uploads weren’t listed properly.

You can access certain Stripe products and features in the beta stage with beta SDKs. The versions of these beta SDKs have the beta or b suffix, for example, 5.1.0b3 in Python and 5.1.0-beta.3 in other language SDKs. Try these beta SDKs and share feedback with us before the features reach the stable phase. To learn more about how to use the beta SDKs, read the readme file in the GitHub repository of the individual language SDKs.

## Stripe SDK support policy

New features and bug fixes are released on the latest major version of the SDK. If you’re on an older major SDK version, we recommend upgrading to the latest major version to take advantage of these features and bug fixes. Older major versions of the package continue to be available for use, but won’t receive any additional updates.

We provide migration guides to help you upgrade from older major SDK versions. You can find them in the wiki section of our SDK GitHub repositories.

- Python SDK wiki

[Python SDK wiki](https://github.com/stripe/stripe-python/wiki)

- .NET SDK wiki

[.NET SDK wiki](https://github.com/stripe/stripe-dotnet/wiki)

- Java SDK wiki

[Java SDK wiki](https://github.com/stripe/stripe-java/wiki)

- Go SDK wiki

[Go SDK wiki](https://github.com/stripe/stripe-go/wiki)

- PHP SDK wiki

[PHP SDK wiki](https://github.com/stripe/stripe-php/wiki)

- Ruby SDK wiki

[Ruby SDK wiki](https://github.com/stripe/stripe-ruby/wiki)

- Node.js SDK wiki

[Node.js SDK wiki](https://github.com/stripe/stripe-node/wiki)

## See also

- Set a Stripe API version

[Set a Stripe API version](/libraries/set-version)
