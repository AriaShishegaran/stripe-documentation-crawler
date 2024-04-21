# Express Dashboard

[account types](https://stripe.com/docs/connect/accounts)

The Express Dashboard is a user interface that’s available to your platform’s users (connected accounts). Users can use the Express Dashboard to monitor their available balance, view upcoming payouts, and track their earnings in real time. This guide outlines the features of the Express Dashboard and how your users can access it.

[payouts](/payouts)

## Express Dashboard features

The Express Dashboard displays the user account’s balance transactions and net volume.

The Transactions list displays a user account’s balance transactions (charges, transfers, and payouts). The Transactions list organizes each balance transaction by type, date, and amount. By default, the Transactions list displays generic descriptions of charges and transfers, such as Payment from {YOUR PLATFORM}. To learn more about setting custom descriptions, see Customize the Express Dashboard.

[Customize the Express Dashboard](/connect/customize-express-dashboard)

The Earnings chart is a graph that displays the net volume of a user’s account. The chart tracks the net volume of charges and transfers over time. Users can choose to view the net volume over different time intervals.

## Accessing the Express Dashboard

There are two ways users can access the Express Dashboard.

We recommend adding a link on your platform that redirects users to the Express Dashboard login page. For example, your users can log into their Express Dashboard by clicking a link (such as a button) on your platform’s website or mobile application.

When users click your link, Stripe redirects the user to the Express Dashboard login page. On this page, users must verify their identity through SMS authentication to view their Express Dashboard. Stripe uses SMS authentication to confirm a user’s identity and grant authorized access to their Express Dashboard.

To learn more about creating this platform link, see Integrate the Express Dashboard.

[Integrate the Express Dashboard](/connect/integrate-express-dashboard)

This option is only available for livemode accounts. For testing, please create a login link instead.

[login link](/connect/integrate-express-dashboard)

Users can also access the Express Dashboard by directly signing into Stripe Express. To do this, they need to sign into Stripe Express using the email associated with their connected account. Stripe then sends an SMS verification code to the mobile number the connected account used during setup. Users must input this SMS verification code to gain access to their Express Dashboard.

[Stripe Express](https://connect.stripe.com/app/express)

To learn more about self-serve access, see Stripe Express support.

[Stripe Express support](https://support.stripe.com/express/questions/how-do-i-login-to-my-stripe-express-account)

## Supported browsers

The Express Dashboard supports the same set of browsers that the Stripe Dashboard currently supports:

[Stripe Dashboard currently supports](/dashboard/basics#browser-compatibility)

- The last 20 major versions of Chrome and Firefox

- The last two major versions of Safari and Edge

- The last two major versions of mobile Safari on iOS

The Express Dashboard does not support webviews, it is only supported in standalone browsers.

## See also

- Integrate the Express Dashboard

[Integrate the Express Dashboard](/connect/integrate-express-dashboard)

- Customize the Express Dashboard

[Customize the Express Dashboard](/connect/customize-express-dashboard)
