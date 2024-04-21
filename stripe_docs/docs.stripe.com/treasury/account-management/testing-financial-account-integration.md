# Testing financial account integration

Stripe Treasury includes a live mode and test mode. You can toggle between modes from your Dashboard using the mode toggle in the upper-right corner.

Test mode toggle

You must complete the Gaining API access to Treasury guide’s live mode steps before you have access to live mode financial accounts.

[Gaining API access to Treasury](/treasury/access)

To access test mode in the API, use the test mode API key with your requests. The test mode API key is included within most documentation code examples, but you can also find it in the Developers page of your Dashboard. Make sure to use the test key for testing and not the live one. The test key has the form sk_test_xxx, whereas the live key is in the form sk_live_xxx.

[Dashboard](https://dashboard.stripe.com/test/apikeys)

Before creating a test financial account, create a test connected account using POST /v1/accounts. Use the connected account ID you receive from the response to assign the financial account you create in the next step to this account. Treasury is supported only in the US, so assign US to the country parameter. You’re also requesting capabilities for the connected account that Treasury requires to function properly. Make note of the id value in the response. As mentioned, you use the ID as the value for the Stripe-Account header in the following code example.

If successful, the response returns the new connected account Account object.

[Account](/api/accounts)

Next, create a financial account using POST /v1/treasury/financial_accounts. Include a Stripe-Account header set to the value of the connected account ID you created in the previous instruction. The only required value in the body is to set supported_currencies[] to usd. To learn more about financial accounts, see Working with financial accounts or the FinancialAccounts object description in the Stripe API reference.

[Working with financial accounts](/treasury/account-management/financial-accounts)

[FinancialAccounts](/api/treasury/financial_accounts)

If successful, the response returns the newly created FinancialAccount object.

You now have a test mode financial account attached to a test mode connected account. However, the connected account hasn’t been onboarded so required information is missing from the requirements hash. If you call GET /v1/treasury/financial_accounts/{{FINANCIAL_ACCOUNT_ID}} using the financial account ID in the JSON response of the previous instruction, you see the financial_addresses array of hashes has an entry for the requested aba with a status of restricted because the connected account has requirements_past_due.

To enable requested features on your test mode financial account without first going through connected account onboarding, you must use POST /v1/accounts/{{CONNECTED_ACCOUNT_ID}} to provide test values that fulfill all the requirements, as in the following request that uses a previously created connected account to apply the required account details.

[provide test values](/connect/testing-verification)

You can’t create a test mode financial account attached to a live mode connected account.

[https://bestcookieco.com](https://bestcookieco.com)
