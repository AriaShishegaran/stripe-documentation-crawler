# Stripe for Salesforce Platform Configuration

The Stripe for Salesforce Platform checks to prevent recursive actions. A logical loop occurs when one set of resources repeatedly detects and responds to updates from another set. For instance, if a flow listens to Stripe’s customer.updated events and then updates a Salesforce Account, but another flow is set up to detect updates to the Salesforce Account and then updates a Stripe customer, it creates a logical loop. This loop would run indefinitely.

## Default Events excluded from recursion detection

You can include and exclude specific events from recursion detection. If you’re an admin, you can modify these events in your settings by configuring recursion detection.

The Recursion Detection Configuration can be accessed by following these steps:

- Navigate to Setup > Custom Code > Custom Metadata Types.

- Under Recursion Detection Configuration, click Manage Records.

- Next to Default, click Edit.

Within this configuration, an admin can add either Included Events or Excluded Events.

## Configure sync preferences

- To configure Sync Preferences, launch the Stripe Connector for Salesforce App wizard, navigate to App Launcher > Stripe Universal Connector for Salesforce

- Click the Sync Preferences button.

- Enable or disable Enable Stripe Event Data Cleanup.

- Modify the Maximum Stripe Event Records Retained (Count).

- Enable or disable Sync Log Records.

- Modify the Maximum Sync Log Records Retained (Count).

## See also

- Enablement

[Enablement](/connectors/stripe-connector-for-salesforce/enablement)

- Installation guide

[Installation guide](/plugins/stripe-connector-for-salesforce/installation-guide)
