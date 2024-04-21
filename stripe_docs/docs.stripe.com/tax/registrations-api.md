# Use the Registrations API to manage tax registrations

Businesses are required to register to collect taxes in locations where they have tax obligations. The Tax Registration API lets you retrieve and configure tax registrations using an API instead of the Dashboard. Adding your registrations in Stripe turns on tax calculation and collection for your transactions made through Stripe.

[Tax Registration API](/api/tax/registrations)

Different rules determine when and how a business needs to register to collect tax depending on the location. Learn more about tax collection in different locations.

[Learn more about tax collection in different locations](/tax/supported-countries)

- Connect platform: As a platform, you can use this API to manage the registrations of your connected accounts or to check an account’s active registrations.

- Direct usage: You can use this API to manage and check your registrations.

## List all tax registrations for your connected accounts

To get a list of your connected accounts’ tax registrations, make a list registrations call. You can filter the response by setting the status parameter to active, expired, or scheduled.

[list registrations](/api/tax/registrations)

If your connected accounts don’t have access to the Stripe Dashboard, your platform can provide a UI for them to manage their tax registrations. The registrations endpoint helps you implement that functionality.

## Add a tax registration for your connected account

If a tax obligation and registration of the connected account is known to the platform, you can perform a create registration call using the Stripe-Account header with a value of the connected account ID to add or schedule the registration for the connected account.

[create registration](/api/tax/registrations/create)

In this case, a tax.registration object is created in the connected account.

Alternatively, for connected accounts with access to the Stripe Dashboard (for example, Standard accounts), you can instruct them to set up Stripe Tax using the Dashboard, which includes adding tax registrations.

[set up Stripe Tax](/tax/set-up)

## Update and expire a tax registration for your connected account

You can’t delete a registration after it’s created, but you can end it by setting expires_at to a time when the registration is no longer active. Update the registrations with an update registration call using the Stripe-Account header with a value of the connected account ID:

[update registration](/api/tax/registrations/update)

In this case, the registration expires immediately. Tax calculations performed for the connected account after the expires_at won’t use this registration.

[Tax calculations](/api/tax/calculations)

[privacy policy](https://stripe.com/privacy)

## See also

- Use the Settings API to configure Stripe Tax

[Use the Settings API to configure Stripe Tax](/tax/settings-api)

- Use Stripe Tax with Connect

[Use Stripe Tax with Connect](/tax/connect)
