# Managing payout schedule

When using automatic payouts, the settings.payouts.schedule hash on an Account contains details on when a Stripe account’s funds are available and when the balance is automatically paid out:

[settings.payouts.schedule](/api/accounts/object#account_object-settings-payouts-schedule)

[Account](/api/accounts/object)

The delay_days property reflects how long it takes for on_behalf_of charges (or direct charges performed on the connected account) to become available for payout. You can edit this property on accounts where you own fraud and dispute liability.

[delay_days](/api/accounts/object#account_object-settings-payouts-schedule-delay_days)

[own fraud and dispute liability](/connect/accounts)

This field is useful for dictating automatic payouts. For example, if you want your connected accounts to receive their funds two weeks after the charge is made, set interval to daily and delay_days to 14. Stripe calculates the delay in business days or calendar days based on the connected accounts’ country. When setting or updating this field, you can pass the string minimum to choose the lowest permitted value.

[connected accounts’ country](/payouts#standard-payout-timing)

For accounts where Stripe manages fraud and dispute liability (for example, Standard accounts), the default is the lowest permitted value for the account, determined by the connected account’s country. If you’re opted into accelerated payout speeds, the value uses the accelerated timing. You can request to lower this by contacting Stripe Support. For accounts where you own fraud and dispute liability, the value remains at your original payout speed by default.

[connected account’s country](/payouts#standard-payout-timing)

[accelerated payout speeds](/payouts#accelerated-payout-speeds)

[Stripe Support](https://support.stripe.com/contact)

Platforms that manage fraud and dispute liability, or have platform controls, can adjust the payout interval. There are four possible settings for the interval property:

[platform controls](/connect/platform-controls-for-stripe-dashboard-accounts#control-payout-timing)

- manual: This setting prevents automatic payouts. You will have to manually pay out the account’s balance using the Payouts API (acting as the connected account). You also set an account to manual to use Instant Payouts.

[Payouts API](/api#create_payout)

[Instant Payouts](/connect/instant-payouts)

- daily: This setting automatically pays out charges delay_days days after they’re created. The delay_days value can’t be less than your own payout schedule or less than the default payout schedule for the account.

- weekly: This setting automatically pays out the balance once a week, with the day specified by the weekly_anchor parameter (a lower-case weekday such as monday).

- monthly: This setting automatically pays out the balance once a month, as specified by the monthly_anchor parameter (a number from 1 to 31). Payouts nominally scheduled between the 29th and 31st of the month are instead sent on the last day of a shorter month.
