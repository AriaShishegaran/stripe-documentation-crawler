# Installing the Stripe Connector for Adobe Commerce (Magento 2)

We recommend that you test the module before installing it on your production environment. If you experience an installation issue, see the Troubleshooting documentation.

[Troubleshooting](/connectors/adobe-commerce/troubleshooting)

## Install the module

- Place an order for the module through the Adobe Marketplace.

[Adobe Marketplace](https://marketplace.magento.com/stripe-stripe-payments.html)

- Open a terminal and run the following command in your Adobe Commerce directory:

At this stage, you might have to submit your username and password. Provide your Adobe Commerce authentication keys. You can accept to save your credentials when prompted by Composer. If you’ve saved your keys and see the error Invalid Credentials, update your keys in ~/.composer/auth.json or delete this file and run the command again.

[Adobe Commerce authentication keys](https://devdocs.magento.com/guides/v2.3/install-gde/prereq/connect-auth.html)

- Set up the module by running the following commands:

- If you run Adobe Commerce in production mode, you must also compile and deploy the module’s static files.

## Upgrade the module

Before you upgrade:

- Backup your files and database.

- Start with your test environment.

- Keep a copy of any customization you made to the module’s original code.

- Check out the CHANGELOG.

[CHANGELOG](https://github.com/stripe/stripe-magento2-releases/blob/master/CHANGELOG.md)

Patch releases (x.x.Y) are backward compatible and require no extra development on your side after you upgrade. Minor and major releases might add new features or change code in a backwards incompatible way. If you customized the module’s code, you’ll need to port these customizations after upgrading and resolve any potential conflict.

Run the following commands:

## Uninstall the module

Before you uninstall:

- Backup your files and database.

- Keep a copy of any customization you made to the module’s original code in case you need to reinstall it later.

Run the following commands:

## Lifecycle policy

The latest version of the module supports the following versions of Adobe Commerce:

For stripe/stripe-payments:3.5.* and newer, we provide new features, bug fixes, and security patches.

Older versions are deprecated. Stripe recommends you upgrade at the earliest opportunity.

All releases are available in the Adobe Marketplace and in the stripe-magento2-releases GitHub repository.

[stripe-magento2-releases](https://github.com/stripe/stripe-magento2-releases)

## See also

- Configuring the Stripe Connector for Adobe Commerce

[Configuring the Stripe Connector for Adobe Commerce](/connectors/adobe-commerce/configuration)

- Using the Adobe Commerce admin panel

[Using the Adobe Commerce admin panel](/connectors/adobe-commerce/admin)

- Troubleshooting

[Troubleshooting](/connectors/adobe-commerce/troubleshooting)
