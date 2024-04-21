# Testing account verification during API onboarding

[account types](https://stripe.com/docs/connect/accounts)

This document assumes you’re familiar with Custom accounts, how to update accounts, and identity verification.

[Custom accounts](/connect/custom-accounts)

[update accounts](/connect/updating-service-agreements)

[identity verification](/connect/identity-verification)

Test your verification flows to make sure they can handle changes in account state (for example, when you enable or disable charges). Account states generally change after fulfilling requirements or when reaching processing or time thresholds. The sections below describe these changes and how to test your verification flows.

## Testing initial requirements

Start by creating a new Custom account in test mode, adding a bank account, and showing that the account holder accepted the Stripe Services Agreement. Explicit Services Agreement acceptance is required for making payouts. For this example, the business_type is set to company to illustrate a more complex scenario, and the external_account uses a tokenized Stripe test account as a reminder to avoid exposing sensitive information in API calls.

[required for making payouts](/connect/updating-service-agreements#tos-acceptance)

You must provide a test API key from a Stripe account which has begun Connect platform onboarding. The auto-filled Stripe test API key causes these sample requests to fail.

At this point, the account is created but charges and payouts are still disabled. In the response, check the requirements.currently_due array to determine what information you need to collect:

[payouts](/payouts)

Then, use the external account id returned in the response to update the account with the additional required information about the account:

[https://bestcookieco.com](https://bestcookieco.com)

After successfully updating the company details, checking requirements.currently_due shows the relationship requirements are still required:

Use the Persons API to create a profile for the person representing the relationship to the account. For this example, we create a profile for Jenny Rosen, and identify her as the representative. For this example, we also populate the optional title attribute.

[Persons](/api/persons)

For accounts with business_type set to individual, provide at least one individual property (for example, individual.first_name) and a Person object is created automatically. If you don’t, or for accounts with the business_type set to company, you need to create each Person for the account.

[business_type](/api/accounts/object#account_object-business_type)

[Person](/api/persons/object)

[create each Person](/api/persons/create)

When you create a Person, the response includes a requirements hash listing the required verification information for that person.

After you create a Person for your external account, checking the Account object shows that the required verification information for the newly created Person has been added to the requirements.currently_due list:

Use the Update a Person API to provide the requested verification information for Jenny Rosen:

[Update a Person](/api/persons/update)

Setting relationship[executive]=true confirms to Stripe that the representative is someone with significant control in the organization. US required verification information has more information about company representative verification details for US businesses.

[US required verification information](/connect/required-verification-information#additional-company-card-representative-us)

After providing the representative information, we still need to identify the owner for the account. In this example, Kathleen Banks owns 80% of The Best Cookie Co.

In our example, Kathleen Banks owns less than 100% of The Best Cookie Co. Since you haven’t defined another owner to make the ownership total 100%, Stripe requires you to confirm that you’ve provided information on all required owners.

Successful completion of your connected account at this stage means:

- You’ve completed all required information (requirements.currently_due=null).

- Charges are enabled for the account (charges_enabled=true).

- You received an account.updated webhook from Stripe.

[webhook](/webhooks)

## Testing thresholds

Whether you use upfront onboarding or incremental onboarding, Stripe might request more information about connected accounts as different thresholds are reached. Sometimes these thresholds are triggered by verification failures or OFAC checks. Other times, they’re triggered by a processing or time component. For example, more information might be required after 1,500 USD in charges or 30 days after an account is created (whichever comes first). To find out what information is required and by when, you can check the requirements.eventually_due array and the requirements.current_deadline timestamp.

[OFAC](https://www.treasury.gov/about/organizational-structure/offices/Pages/Office-of-Foreign-Assets-Control.aspx)

In some cases, if the you don’t collect new information by a certain date, charges and payouts might be disabled until you collect it. You can trigger these scenarios so that you can test these thresholds, and then collect the required information.

You can create a charge with the verification token (tok_visa_triggerVerification) to trigger a generic verification threshold. This doesn’t block charges or payouts, but it does trigger the request for additional information. If you’re listening to the account.updated webhook, you can check:

[verification](/connect/testing#trigger-cards)

- requirements.currently_due to find out what information is needed.

- requirements.current_deadline to find out when the information is needed.

If the information isn’t collected by the current_deadline, charges and payouts might be disabled. To test scenarios like this, see the blocking charges and payouts sections below.

[charges](#blocked-charges)

[payouts](#blocked-payouts)

You can also trigger more specific verification thresholds, like when there’s an identity mismatch or when an OFAC threshold is reached. Testing these thresholds is beneficial because they often happen when verification fails.

[identity mismatch](/connect/testing#test-personal-id-numbers)

[OFAC threshold](/connect/testing#test-dobs)

You can block charges by creating a test charge with the charge block token (tok_visa_triggerChargeBlock). After doing this, you should receive an account.updated webhook that shows:

[charge block](/connect/testing#trigger-cards)

- charges_enabled=false.

- The required information in the requirements.currently_due array.

- An empty requirements.eventually_due array.

You can then update the account with the new information. That triggers another webhook, which indicates that charges are enabled and that the requirements.currently_due and requirements.eventually_due arrays are both empty.

[update the account](/api/accounts/update)

You can block payouts by creating a test charge with the block transfer token (tok_visa_triggerTransferBlock). After doing this, you should receive an account.updated webhook that shows:

[block transfer](/connect/testing#trigger-cards)

- payouts_enabled=false.

- The required information in the requirements.currently_due array.

- An empty requirements.eventually_due array.

You can then update the account with the new information. That triggers another webhook, which indicates that payouts are enabled and that the requirements.currently_due and requirements.eventually_due arrays are both empty.

[update the account](/api/accounts/update)
