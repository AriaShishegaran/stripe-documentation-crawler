htmlStart a team | Stripe Documentation[Skip to content](#main-content)Start a team[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fteams)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fteams)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)
Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Get started](/docs/get-started)Create an account# Start a team

Learn how to invite and interact with team members.### Security history

Stripe logs the account activity of team members during the past 180 days. To review account activity information, go to Security history in the Dashboard.

You can invite members of your team to access your Stripe account. You must assign each team member at least one role before you can invite them. Roles protect your sensitive information and restrict the actions team members can perform on your account. See the list of actions that each role can and can’t perform before assigning the role to a team member.

You can invite team members individually, or invite multiple users at the same time by separating their email addresses with a comma or space. You can also assign multiple roles to a team member, which gives them the combined set of permissions granted by those roles. Invites to your Stripe account expire after 10 days.

![Invite a team member to access your Stripe account](https://b.stripecdn.com/docs-statics-srv/assets/invite-team-members.56ae9525e14e736f8fd9d7045b7e96f1.png)

Invite a team member to access your Stripe account

After a team member has accepted their invite, you can edit their role at any time from your account’s Team settings. To edit a team member’s role, click the overflow menu (), then click Edit.

## Mention team members

You can mention team members when you add a note to a payment. If you mention a team member, they receive an email notification with the note and a link to the associated payment.

![Mention a team member when you add a note to a payment](https://b.stripecdn.com/docs-statics-srv/assets/mention-team-members.b21aa27e9cf6862239796d842d869428.png)

Mention a team member

## Receive email notifications

You can configure email notifications under Communication preferences in your Profile, and apply them on a per-user basis. If your team members also want to receive notifications, they must customize their own settings. Stripe sends email notifications to you when any of the following events occur:

- A successful payment is received.
- An[application fee](/connect/direct-charges#collect-fees)is collected from a connected account.
- A payment is[disputed](/disputes)by a customer.
- A payment is marked as[elevated risk](/radar/risk-evaluation#elevated-risk)by Stripe or a custom[Stripe Radar](/radar)rule.
- You’re mentioned in a note.
- A customer sends an incorrect amount to pay their[invoice](/invoicing).
- A[webhook](/webhooks)delivery fails.

For a full list of notification events, go to your Communication preferences under Profile.

## See also

- [User roles](/get-started/account/teams/roles)

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Mention team members](#mentions)[Receive email notifications](#email-notifications)[See also](#see-also)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`