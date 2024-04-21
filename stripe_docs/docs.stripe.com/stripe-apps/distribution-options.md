# Distribution options

Stripe Apps gives you two ways to distribute your apps. You can make them publicly available or share them only with your team members.

[team members](/dashboard/teams)

## Publish your app on the Stripe App Marketplace

The Stripe App Marketplace is how you share your application with the Stripe user community.

When you publish an app on the App Marketplace, make sure the app complies with all app review requirements. We also recommend reviewing our app listing guidelines for best practices and recommended coding patterns. Stripe reviews all apps to make sure they comply with the published requirements before listing them in the marketplace.

[app review requirements](/stripe-apps/review-requirements#app-review-requirements)

[app listing guidelines](/stripe-apps/listing-guidelines)

Stripe can only support English language listings at this time. To support additional languages, reach out to Stripe.

The publishing process consists of these steps:

- Select the version of the app that you want to publish.

- Create an app listing that provides prospective users with information about your app and defines how your app appears in the App Marketplace.

- Submit the application for review.

- Publish the app to the App Marketplace.

For more information, learn how to publish your app.

[publish your app](/stripe-apps/publish-app)

## Share your app with team members

With Stripe Apps, you have the option of sharing your app only with team members. For example, you might develop an app that sends sale data into your own custom accounting system. Or you might build an app that connects paid orders with your fulfillment system. For these and other situations, you can make the application only available to team members of your Stripe account.

[team members](/dashboard/teams)

Unlike apps on the App Marketplace, apps shared with team members don’t go through a review process. However, we recommend reviewing our app review requirements and app listing guidelines when you build your app.

[app review requirements](/stripe-apps/review-requirements#app-review-requirements)

[app listing guidelines](/stripe-apps/listing-guidelines)

Sharing your app with team members consists of these steps:

- Specify that you want to share your app only with members of your Stripe account.

- Select the version of the app that you want to upload and make available.

[upload and make available](/stripe-apps/upload-install-app)

If you later decide you want to publish your app on the Stripe App Marketplace, you must uninstall your app in live mode first.

[live mode](/stripe-apps/upload-install-app#install-in-live-mode)

## Setting the distribution type for your app

To set the distribution type for your app, run the following command:

This updates the app manifest to reflect the distribution type. The new distribution takes effect after you upload your app. The private distribution type is the default type, which you don’t need to explicitly set.

[upload your app](/stripe-apps/upload-install-app)

You can continue to change the distribution type until you upload an app. After you upload an app with a public distribution, you can’t set a public distribution for another app within the same Stripe account. You can change the distribution type from private to public if there are no other public apps within the same Stripe account.

## See also

- Publish your app

[Publish your app](/stripe-apps/publish-app)

- Upload your app

[Upload your app](/stripe-apps/upload-install-app)

- Invite team members or developers to access your Stripe account

[Invite team members or developers to access your Stripe account](https://support.stripe.com/questions/invite-team-members-or-developers-to-access-your-stripe-account)
