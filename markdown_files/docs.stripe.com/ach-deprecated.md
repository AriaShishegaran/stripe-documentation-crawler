htmlACH Direct Debit with Charges | Stripe Documentation[Skip to content](#main-content)ACH Direct Debit[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fach-deprecated)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fach-deprecated)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)Resources[About the APIs](#)
[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Home](/docs)[Payments](/docs/payments)[About the APIs](/docs/payments-api/tour)[Older APIs](/docs/payments/older-apis)[Sources](/docs/sources)# ACH Direct Debit with ChargesDeprecated

Legacy guide for accepting ACH payments with our older Charges API.NoteIf you’re building a new integration, we offer several ways to accept ACH payments.

If you have an existing integration that accepts ACH payments using the Charges API, we recommend migrating it to use the Payment Intents API. The Payment Intents API includes built-in instant verification.

### US Bank Transfers with ACH

You can also receive ACH credit payments sent by customers using US Bank Transfers.

Stripe allows you to accept ACH payments in nearly the same way as you accept credit card payments, by providing a verified bank account as the source argument for a charge request. However, accepting bank accounts requires a slightly different initial workflow than accepting credit cards:

1. You must first[verify](#verifying)bank accounts.
2. Your customer must[authorize](#authorization)you to use them.

After taking both steps for a bank account, your customer can use it like other payment methods, including for recurring charges and Connect applications. The two key differences between using bank accounts and credit cards are:

- ACH payments take up to 5 business days to receive acknowledgment of their success or failure. Because of this, your Stripe balance takes up to 7 business days to reflect ACH payments in your available Stripe balance.
- You can only accept funds in USD and only from US bank accounts. In addition, your account must have a US (USD) bank account to accept ACH payments.

## Collecting and verifying bank accounts

Before you can create an ACH charge, you must first collect and verify your customer’s bank account and routing number. In order to properly identify the bank account, you also need to collect the name of the person or business who owns the account, and if the account is owned by an individual or a company. Stripe provides two methods for doing so: instant collection and verification with Plaid or collection using Stripe.js with delayed-verification using microdeposits.  You may incur additional costs when using Plaid, depending on the size of your business. Take this into account when making your decision.

Because charging a bank account requires both verification of the account and customer authorization to use it, the best practice is to store the bank account on a Customer object in Stripe so you can reuse it.

## Using Plaid

![plaid logo](https://b.stripecdn.com/docs-statics-srv/assets/plaid.291ca97692152302c6cbab16a1c39257.png)

Plaid provides the quickest way to collect and verify your customer’s banking information. Using the Stripe + Plaid integration, you can instantly receive a verified bank account, which allows for immediate charging. This is done using Plaid Link, and you receive the Stripe bank account token directly from Plaid.

Step 1: Set up your Plaid account

If you don’t have a Plaid account, create one. Your account is automatically enabled for integration access. To verify that your Plaid account is enabled for the Stripe integration, go to the Integrations section of the account dashboard. Make sure your Stripe account is connected there.

Step 2: Fetch a Link token

A link_token is a one-time use token that initializes Plaid Link. You can create a link_token and configure it for your specific Link flow by calling the Create Link Token endpoint from your server.

Command Line[curl](#)`curl https://sandbox.plaid.com/link/token/create \
  -H "Content-Type: application/json" \
  -d "{\"client_id\": \"{{PLAID_CLIENT_ID}}\",\"secret\": \"{{PLAID_SECRET}}\",\"client_name\": \"My App\",\"user\": {\"client_user_id\": \"Stripe test\"},\"products\": [\"auth\"],\"country_codes\": [\"US\"],\"language\": \"en\", \"webhook\": \"https://webhook.sample.com/\"}"`Step 3: Integrate with Plaid Link

Integrating with Link only takes a few lines of client-side JavaScript and a small server-side handler to exchange the Link public_token for a Plaid access_token and a Stripe bank account token.

`<button id="link-button">Link Account</button>

<script src="https://cdn.plaid.com/link/v2/stable/link-initialize.js"></script>
<script type="text/javascript">
(async function() {

  const configs = {
    // Pass the link_token generated in step 2.
    token: '{{LINK_TOKEN}}',
    onLoad: function() {
      // The Link module finished loading.
    },
    onSuccess: function(public_token, metadata) {
      // The onSuccess function is called when the user has
      // successfully authenticated and selected an account to
      // use.
      //
      // When called, you will send the public_token
      // and the selected account ID, metadata.accounts,
      // to your backend app server.
      //
      // sendDataToBackendServer({
      //   public_token: public_token,
      //   account_id: metadata.accounts[0].id
      // });
      console.log('Public Token: ' + public_token);
      switch (metadata.accounts.length) {
        case 0:
          // Select Account is disabled: https://dashboard.plaid.com/link/account-select
          break;
        case 1:
          console.log('Customer-selected account ID: ' + metadata.accounts[0].id);
          break;
        default:
          // Multiple Accounts is enabled: https://dashboard.plaid.com/link/account-select
      }
    },
    onExit: async function(err, metadata) {
      // The user exited the Link flow.
      if (err != null) {
          // The user encountered a Plaid API error
          // prior to exiting.
      }
      // metadata contains information about the institution
      // that the user selected and the most recent
      // API request IDs.
      // Storing this information can be helpful for support.
    },
  };

  var linkHandler = Plaid.create(configs);

  document.getElementById('link-button').onclick = function() {
    linkHandler.open();
  };
})();
</script>`Step 4: Write server-side handler

The Link module handles the entire onboarding flow securely and quickly, but doesn’t actually retrieve account data for a user.  Instead, the Link module returns a public_token and an accounts array, which is a property on the metadata object, and part of the onSuccess callback.

The accounts array contains information about bank accounts associated with the credentials entered by the user, and may contain multiple accounts if the user has more than one bank account at the institution. To avoid any confusion about which account your user wants to use with Stripe, set Select Account to Enabled for one account in the Plaid developer dashboard. When you select this setting, it means the accounts array will always contain exactly one element.

When your server has the public_token and account_id, you must make two calls to the Plaid server to get the Stripe bank account token along with the Plaid access_token to use for other Plaid API requests.

Command Line[curl](#)`curl https://sandbox.plaid.com/item/public_token/exchange \
  -H "Content-Type: application/json" \
  -d "{\"client_id\": \"{{PLAID_CLIENT_ID}}\", \"secret\": \"{{PLAID_SECRET}}\", \"public_token\": \"{{PLAID_LINK_PUBLIC_TOKEN}}\"}"

curl https://sandbox.plaid.com/processor/stripe/bank_account_token/create \
  -H "Content-Type: application/json" \
  -d "{\"client_id\": \"{{PLAID_CLIENT_ID}}\", \"secret\": \"{{PLAID_SECRET}}\", \"access_token\": \"{{PLAID_ACCESS_TOKEN}}\", \"account_id\": \"{{PLAID_ACCOUNT_ID}}\"}"`The response contains a verified Stripe bank account token ID. You can attach this token to a Stripe Customer object, or create a charge directly on it.

`{
  "stripe_bank_account_token": "btok_yEGk0aNKgnb2KBQX6uex",
  "request_id": "[Unique request ID]"
}`Step 5: Get ready for production

Plaid uses different API hosts for test and production requests. The above request uses Plaid’s Sandbox environment, which uses simulated data. To test with live users, use Plaid’s Development environment. Plaid’s Development environment supports up to 100 live objects, which you won’t be billed for. When it’s time to go live, use Plaid’s Production environment.

## Manually collecting and verifying bank accounts

Plaid supports instant verification for many of the most popular banks. However, if Plaid doesn’t support your customer’s bank or you don’t want to integrate with Plaid, collect and verify the customer’s bank using Stripe alone.

First, use Stripe.js to securely collect your customer’s bank account information, receiving a representative token in return. When you have that, attach it to a Stripe customer in your account.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "description"="Example customer" \
  -d "source"="btok_4XNshPRgmDRCVi"`Customer bank accounts require verification. When using Stripe without Plaid, Stripe automatically sends two small deposits for this purpose. These deposits take 1-2 business days to appear on the customer’s online statement. The statement has a description that includes ACCTVERIFY. Your customer must relay these amounts to you.

When accepting these amounts, be aware that the limit is three failed verification attempts. If you exceed this limit, we can’t verify the bank account. Clear messaging about what these microdeposits are and how you use them can help your customers avoid verification issues. As soon as you have these amounts, you can verify the bank account.

Command Line[curl](#)`curl https://api.stripe.com/v1/customers/cus_AFGbOSiITuJVDs/sources/ba_17SHwa2eZvKYlo2CUx7nphbZ/verify \
  -u sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \
  -d "amounts[]"=32 \
  -d "amounts[]"=45`After we verify the bank account, you can make charges against it.

## Payment authorization

Before creating an ACH charge, get authorization from your customer to debit their account. Doing so ensures compliance with the ACH network and helps protect you from disputes, additional fees, and reversed payments. See the support page for more information on authorization requirements.

## Creating an ACH charge

To create a charge on a verified bank account, use the stored Customer object the same way you would when using a card.

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1500 \
  -d currency=usd \
  -d customer=cus_AFGbOSiITuJVDs`Attempting to charge an unverified bank account results in an error with the message “The customer’s bank account must be verified in order to create an ACH payment.”

If the customer has multiple stored sources (of any type), specify which bank account to use by passing its ID in as the source parameter.

## Testing this integration

You can mimic successful and failed ACH charges using the following bank routing and account numbers:

- Routing number:`110000000`
- Account number:  - `000123456789`(success)
  - `000111111116`(failure upon use)
  - `000111111113`(account closed)
  - `000222222227`(NSF/insufficient funds)
  - `000333333335`(debit not authorized)
  - `000444444440`(invalid currency)



To mimic successful and failed bank account verifications, use these meaningful amounts:

- `[32, 45]`(success)
- `[any other number combinations]`(failure)

## ACH payments workflow

ACH payments take up to 5 business days to receive acknowledgment of their success or failure:

- When created, ACH charges have the initial status of`pending`.
- Apendingbalance transaction is immediately created reflecting the payment amount, less our fee.
- Payments created on or after 22:00 UTC are currently processed on the next business day.
- During the following 4 business days, the payment transitions to either`succeeded`or`failed`depending on the customer’s bank.
- Successful ACH payments are reflected in your Stripe available balance after 7 business days, at which point the funds are available for automatic or manual transfer to your bank account.
- Failed ACH payments reverse thependingbalance transaction created.
- Your customer sees the payment reflected on their bank statement 1-2 days after creating the charge. (Your customer knows if the payment succeeds before the bank notifies Stripe.)

Failures can happen for a number of reasons such as insufficient funds, a bad account number, or the customer disabling debits from their bank account.

In rare situations, Stripe might receive an ACH failure from the bank after a payment has transitioned to succeeded. If this happens, Stripe creates a dispute with a reason of:

- `insufficient_funds`
- `incorrect_account_details`
- `bank_cannot_process`

Stripe charges a failure fee in this situation.

## Handling disputes in this integration

Disputes on ACH payments are fundamentally different than those on credit card payments. If a customer’s bank accepts the request to return the funds for a disputed charge, Stripe immediately removes the funds from your Stripe account. Unlike credit card disputes, you can’t contest ACH reversals. You must contact your customer to resolve the situation.

Customers can generally dispute an ACH Direct Debit payment through their bank for up to 60 calendar days after a debit on a personal account, or up to 2 business days for a business account. In rare instances, a debit payment can be successfully disputed outside these timelines.

### Risk of double-crediting with ACH refunds and disputes

If you proactively issue your customer a refund while their bank also initiates the dispute process, they may receive two credits for the same transaction.

When issuing a refund for an ACH payment, you must notify your customer immediately that you’re issuing the refund and that it may take 2-5 business days for the funds to appear in their bank account.

## Refunds

You can refund ACH charges, for up to 90 days from the date of the original payment, using the Refund endpoint, but the timing and risks associated with ACH refunds are different from card refunds.  If a refund for an ACH charge succeeds, Stripe won’t send any notification. If a refund for an ACH charge fails, however, you’ll receive a charge.refund.updated notification, which means that we haven’t been able to process the refund. You must return the funds to your customer outside of Stripe. This is rare—normally occurring when an account is frozen between the original charge and the refund request.

## ACH-specific webhook notifications

When using ACH, you’ll receive many of the standard charge webhook notifications, with a couple of notable differences:

- After creating the charge, you receive a`charge.pending`notification. You won’t receive`charge.succeeded`or`charge.failed`notification until up to 5 business days later.
- You receive a`charge.succeeded`notification after the charge has transitioned to`succeeded`and the funds are available in your balance.
- You receive a`charge.failed`notification if the ACH transfer fails for any reason. The charge’s`failure_code`and`failure_message`will be set, and the funds are reversed from your Stripe pending balance at this point.
- You receive a`customer.source.updated`notification when the bank account is properly verified. The bank account’s`status`is set to`verified`.
- If the bank account couldn’t be verified because either of the two small deposits failed, you receive a`customer.source.updated`notification. The bank account’s`status`is set to`verification_failed`.

## Connect support

With Connect, your platform can earn money while processing charges. You can either:

- Create the customer on the connected account, then create a[direct charge](/connect/direct-charges)
- Create the customer[on the platform account](/connect/cloning-customers-across-accounts), then create a[destination charge](/connect/destination-charges)using the`transfer_data`parameter (as in the code below)

Command Line[curl](#)`curl https://api.stripe.com/v1/charges \
  -u "sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \
  -d amount=1500 \
  -d currency=usd \
  -d customer=cus_AFGbOSiITuJVDs \
  -d "transfer_data[amount]"=850 \
  -d "transfer_data[destination]"={{CONNECTED_STRIPE_ACCOUNT_ID}}`## Services Agreement

Use of the live mode API is subject to the Stripe Services Agreement. Let us know if you have any questions on that agreement.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Collecting and verifying bank accounts](#verifying)[Using Plaid](#using-plaid)[Manually collecting and verifying bank accounts](#manually-collecting-and-verifying-bank-accounts)[Payment authorization](#authorization)[Creating an ACH charge](#creating-an-ach-charge)[Testing this integration](#testing-this-integration)[ACH payments workflow](#ach-payments-workflow)[Handling disputes in this integration](#handling-disputes-in-this-integration)[Refunds](#refunds)[ACH-specific webhook notifications](#ach-specific-webhook-notifications)[Connect support](#connect)[Services Agreement](#services-agreement)Products Used[Payments](/payments)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`