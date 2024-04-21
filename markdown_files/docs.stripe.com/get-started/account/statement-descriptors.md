htmlStatement descriptors | Stripe Documentation[Skip to content](#main-content)Statement descriptors[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fstatement-descriptors)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fget-started%2Faccount%2Fstatement-descriptors)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/get-started)[Explore all products](/docs/products)[Plan your integration](#)[Checklists](#)Your account[Create an account](#)
Migrate to Stripe[Migrate customer data](/docs/get-started/data-migrations)[PAN data migrations](#)Fraud prevention[Protect against fraud](#)[Verify identities](#)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Get started](/docs/get-started)Create an account# Statement descriptors

Learn how statement descriptors work.### Connect

If you manage a Connect platform with Custom or Express connected accounts, see Set statement descriptors with Connect.

Statement descriptors explain charges or payments on bank statements. Using clear and accurate statement descriptors can reduce chargebacks and disputes. Banks and card networks require the inclusion of certain types of information that help customers understand their statements, and statement descriptors provide this information.

When you activate your account, you can set a single statement descriptor (static statement descriptor) that appears on all customer statements. For card charges, you can also create a statement descriptor that contains a static prefix associated with your account but with a dynamic suffix associated with each charge. This enables you to specify details about the product, service, or payment on bank or card statements.

Most banks display this information consistently, but some might display it incorrectly or not at all.

## Statement descriptor requirements

A complete statement descriptor—either a single static descriptor or the combination of a prefix and suffix—must meet the following requirements:

- Contains only Latin characters.
- Contains between 5 and 22 characters, inclusive.
- Contains at least one letter (if using a prefix and a suffix, both require at least one letter).
- Doesn’t contain any of the following special characters:`<`,`>`,`\`,`'``"``*`.
- Reflects your Doing Business As (DBA) name.
- Contains more than a single common term or common website URL. A website URL only is acceptable if it provides a clear and accurate description of a transaction on a customer’s statement.

A static prefix, also called a shortened descriptor in the Dashboard, must contain between 2 and 10 characters, inclusive. The remaining characters are reserved for the dynamic suffix.

## Set the static component

You set a static statement descriptor or the shortened descriptor (prefix) in the Dashboard. This value appears on all customer statements for charges or payments.

A static statement descriptor is sufficient if:

- Your business provides only a single product or service.
- Your customers understand a static value for any transaction with your business.
- You prefer to provide the same statement descriptor for all transactions.

For card charges, consider a static prefix with dynamic suffix if:

- You provide multiple products or services.
- Your customers might not understand a single value for all their transactions with your business.
- You prefer to provide transaction-specific details on the statement descriptor.

Set both the statement descriptor and the shortened statement descriptor for flexibility in setting statement descriptors on charges.

If you set the statement descriptor on card charges and don’t set a prefix (shortened descriptor), Stripe truncates the account statement descriptor as needed to set the prefix value. If the account statement descriptor contains fewer than 10 characters, we don’t truncate it.

## Set a dynamic suffix

Dynamic suffixes are supported only for card charges. The suffix should specify details about the transaction so your customer can understand it clearly on their statement. The suffix is concatenated with the prefix, the * symbol, and a space to form the complete statement descriptor that your customer sees.

Make sure that the total length of the concatenated descriptor is no more than 22 characters, including the * symbol and the space. If the prefix is RUNCLUB (7 characters), the dynamic suffix can contain up to 13 characters—for example, 9-22-19 10K (11 characters) or OCT MARATHON (12 characters). The computed statement descriptor is RUNCLUB* 9-22-19 10K or RUNCLUB* OCT MARATHON.

For card charges, providing a dynamic statement descriptor requires the statement_descriptor_suffix value. For non-card charges, if you set a value only for statement_descriptor on a payment intent, Stripe uses it in place of the account statement descriptor (static descriptor).

The following examples show how to add a suffix to the PaymentIntent object.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1099 \
  -d currency=usd \
  -d "payment_method_types[]"=card \
  -d statement_descriptor_suffix="example descriptor"`## Set the statement descriptor on non-card charges

Use the statement_descriptor parameter to set the complete statement descriptor for non-card charges. Attempting to set this parameter for card charges results in a 400 error. For payments made with a card, use statement_descriptor_suffix instead.

## Set Japanese statement descriptors

Japanese merchants can set kanji and kana statement descriptors. Providing clear and easy to understand statement descriptors is important to reduce confusion and chargebacks. We recommend setting statement descriptors in all three supported scripts (kanji, kana, and Latin characters).

You can change your account’s static kanji and kana statement descriptors and shortened descriptors (prefix) in the Dashboard.

For card charges, you can set dynamic suffixes in kanji and kana on Payment Intents and Checkout Sessions. We compute the full descriptor that cardholders see by concatenating the shortened prefix and separators, in the same way as statement_descriptor_suffix.

The following example shows how to set kanji and kana suffixes on a Payment Intent.

Command Line[curl](#)`curl https://api.stripe.com/v1/payment_intents \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1000 \
  -d currency=jpy \
  -d "payment_method_types[]"=card \
  -d statement_descriptor_suffix="example descriptor" \
  -d "payment_method_options[card][statement_descriptor_suffix_kanji]"="漢字サフィックス" \
  -d "payment_method_options[card][statement_descriptor_suffix_kana]"="カナサフィックス"`### Requirements

While Japanese statement descriptors share some requirements with English requirements, the following table shows additional requirements for kanji and kana descriptors.

KanjiKanaMaximum total length1722Minimum prefix length12Maximum prefix length1010Supported character typeKanji, kana, and LatinKanaValidation rule`< > \ ' " * ＊`are not allowedOnly kana, spaces, dashes, and dots are allowedNoteTotal length is the length of either the static descriptor or the concatenated descriptor (prefix + separator + suffix). Descriptors exceeding the maximum length are truncated.

### Issuer behavior

Japanese statement descriptors are available only when both of these are true:

- The card is a Visa or Mastercard issued in Japan.
- The charge is processed by a Japanese merchant or on behalf of a Japanese merchant.

While most issuers use a Japanese statement descriptor rather than a Latin one, it is ultimately up to the issuer to decide which statement descriptor (kanji, kana, or Latin) to show on the cardholder’s statement.

The calculated_statement_descriptor in API responses is always the Latin statement descriptor, but it doesn’t mean the issuer needs to select the Latin statement descriptor rather than the Japanese one.

### ST* prefix

In addition to the behavior described above, Japanese merchants’ JPY-denominated Mastercard payments are prefixed with ST* (or ＳＴ＊ for kanji descriptors) automatically to comply with brand requirements.

### Statement descriptor display timing

Statement descriptors for Japanese merchants’ JPY-denominated payments are sent to issuers at time of payment capture. As a result, they usually take a few days to appear on cardholder statements. In the meantime, depending on the card, a temporary descriptor might be visible to cardholders:

- Mastercard:`ST*ONLINE PAYMENT`,`ＳＴ＊オンライン決済`(kanji), or`ST*オンラインケッサイ`(kana)
- Visa, JCB, Diners Club, and Discover:the account’s default statement descriptor

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Statement descriptor requirements](#requirements)[Set the static component](#static)[Set a dynamic suffix](#dynamic)[Set the statement descriptor on non-card charges](#set-the-statement-descriptor-on-non-card-charges)[Set Japanese statement descriptors](#set-japanese-statement-descriptors)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`