# Disputes on Connect platforms

If you’re using Connect and Custom or Express accounts, your platform is ultimately responsible for any disputes that occur. For payments created on Standard accounts using direct charges, those accounts are responsible for disputes and any funds are withdrawn from their balance—not the platform.

[Connect](/connect)

[direct charges](/connect/direct-charges)

When a disputed payment was made directly on an Express or Custom account, Stripe debits the disputed amount and dispute fee from that account’s balance. However, the platform account is ultimately liable. If Stripe can’t debit the disputed amount and fee from the connected account, we debit it from the platform account.

If the connected account turns out to be fraudulent, it’s unlikely to have an available balance. In that case, Stripe deducts the disputed amount and fee from the platform account.

If the disputed payment was created through the platform using destination charges or separate charges and transfers with or without on_behalf_of, the platform account is automatically debited for the disputed amount and fee. When this happens, the platform can attempt to recover funds from the connected account by reversing the transfer either through the Dashboard or by creating a transfer reversal.

[destination charges](/connect/destination-charges)

[separate charges and transfers](/connect/separate-charges-and-transfers)

[Dashboard](https://dashboard.stripe.com/test/transfers)

[creating a transfer reversal](/api#create_transfer_reversal)

If there is a negative balance on the connected account, Stripe attempts to debit its card issuer account only if debit_negative_balances is set to true.

## See also

- Responding to disputes

[Responding to disputes](/disputes/responding)

- Dispute categories

[Dispute categories](/disputes/categories)

- Preventing disputes and fraud

[Preventing disputes and fraud](/disputes/prevention)

- Using Radar with Connect

[Using Radar with Connect](/connect/radar)
