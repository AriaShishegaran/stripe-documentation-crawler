# Query Issuing data

The Issuing objects represented within Sigma or Data Pipeline includes Authorizations, Transactions, Cards, and Cardholders. Issuing-specific tables can be found within the Issuing section of the schema.

[Authorizations](/api/issuing/authorizations/object)

[Transactions](/api/issuing/transactions/object)

[Cards](/api/issuing/cards/object)

[Cardholders](/api/issuing/cardholders/object)

Issuing data for your connected accounts can be found within tables prefaced with connected_account_, for example,connected_account_issuing_authorizations. More information about using Connect with Sigma or Data Pipeline can be found in the Connect section of the documentation.

[Connect](/connect)

[Connect](/stripe-data/query-connect-data)

## Authorizations

Whenever an issued card is used to make a purchase, an Authorization object is created. Each row within the issuing_authorizations table represents data about this object. The same information can be retrieved through the API and is available in the Stripe Dashboard. Note that the request history field isn’t currently available. Every authorization that has been created on your account is available in Sigma or Data Pipeline.

[Authorization](/api/issuing/authorizations/object)

[Stripe Dashboard](https://dashboard.stripe.com/test/issuing/authorizations)

[request history](/api/issuing/authorizations/object#issuing_authorization_object-request_history)

The card_id column of this table stores the ID of the card used to make the purchase. You can find additional information about the card that initiated the authorization by joining the column with the issuing_cards table.

To access the transactions associated with a particular authorization, you can join the authorization_id column in the issuing_transactions table.

The following query computes counts of authorizations grouped by approval status.

## Transactions

An Issuing Transaction object represents any use of an issued card that results in funds entering or leaving your Stripe account, such as a completed purchase or refund. The issuing_transactions table stores information about these objects. You can retrieve the same information through the API, and it’s also available in the Stripe Dashboard.

[Transaction](/api/issuing/transactions/object)

[Stripe Dashboard](https://dashboard.stripe.com/test/issuing/transactions)

For additional details about the transaction, such as the fee, you can access the associated balance transaction. You can do this by joining the balance_transaction_id column with the id column of the balance_transactions table. Balance transactions are not Issuing-specific objects. More information about working with balance transactions in Sigma or Data Pipeline can be found in the Transactions section of the documentation.

[balance transaction](/api#balance_transaction_object)

[Transactions](/stripe-data/query-transactions)

The authorization_id column allows you to access the Authorization object associated with the Transaction by joining on the id column of the issuing_authorizations table. This can provide additional details about how the transaction was authorized. The authorization_id column on an Issuing transaction can be empty in the event of force capture and for some instances of refunds.

[Authorization](/api/issuing/authorizations/object)

[force capture](/issuing/purchases/transactions#handling-other-transactions)

[refunds](/issuing/purchases/transactions)

You can also access both the card and cardholder involved in the transaction via the card_id and cardholder_id columns. Information about the card is stored in the issuing_cards table, and information about the cardholder is stored in the issuing_cardholders table. The Card and Cardholder objects can provide additional details about who initiated the transaction.

[Card](/api/issuing/cards/object)

[Cardholder](/api/issuing/cardholders/object)

The following query returns information about the three most recent over captures. It joins the issuing_authorizations table to determine if this transaction is an over capture by comparing the amounts of the two objects.

[over captures](/issuing/purchases/transactions#handling-other-transactions)

One of the benefits of using Sigma or Data Pipeline with Issuing is the ability to aggregate data. The following example joins the balance_transactions table and aggregates each of the types of fees for Issuing transactions by month.

## Cards

The issuing_cards table contains data about an individual Card object. The same information is available through the API and within the Stripe Dashboard. The spending controls field isn’t currently available.

[Card](/api/issuing/cards/object)

[Stripe Dashboard](https://dashboard.stripe.com/test/issuing/cards)

[spending controls](/api/issuing/cards/object#issuing_card_object-spending_controls)

Every issued card has an associated Cardholder, which can be accessed by joining the issuing_cardholders table on the cardholder_id column.

[Cardholder](/api/issuing/cardholders)

## Cardholders

Cardholder data is stored within the issuing_cardholders table. The same information can be retrieved through the API or with the Stripe Dashboard. The spending controls field isn’t currently available.

[Cardholder](/api/issuing/cardholders/object)

[Stripe Dashboard](https://dashboard.stripe.com/test/issuing/cardholders)

[spending controls](/api/issuing/cards/object#issuing_card_object-spending_controls)

This table can be joined to other tables to provide information about the entity that initiated a transaction or owns an issued card.

The following example retrieves information about the three most recently created active cardholders.

Metadata for each Issuing object is stored in a separate table. The names of these tables is the name of the object’s table with the addition of _metadata to the end, for example, issuing_transactions_metadata. The metadata table contains a foreign key to the corresponding object in the primary table that you can use to join the two tables. For example, every row in the issuing_transactions_metadata table has the column issuing_transaction_id that references the id column of a row in the issuing_transactions table.

The following example creates a dictionary from the issuing_transactions table’s metadata table. It then uses it to access the value of the metadata key 'my_label' for several transactions.
