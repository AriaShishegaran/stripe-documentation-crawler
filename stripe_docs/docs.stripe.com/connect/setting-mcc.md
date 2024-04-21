# Setting merchant category codes

MCCs are used to classify businesses by the type of goods or services they provide. For example, grocery stores, hotels, and airlines all have different MCCs. These codes are often used for calculating interchange fees, authorizing payments, and preventing fraud, so it’s important that your connected accounts have MCCs that match their businesses.

[MCCs](https://en.wikipedia.org/wiki/Merchant_category_code)

Each Stripe account has exactly one MCC. To view the MCC for a specific account, you can retrieve the business_profile.mcc field on the account object.

[retrieve](/api/accounts/retrieve)

Stripe automatically sets MCC codes for connected accounts, but you can choose to set them manually for accounts that your platform controls. That includes Custom and Express accounts.

## Setting MCCs automatically

Stripe automatically evaluates accounts to determine appropriate MCCs. That means you don’t need to build and maintain any custom logic. Generally, the industry listed in the Stripe Dashboard for the connected account is used to determine the MCC. For accounts where Stripe collects updated information for due or changed requirements, including Standard and Express accounts, and for Custom accounts using Stripe-hosted onboarding, the MCC is set during onboarding. For accounts created with the API and for Express accounts, you can set the MCC manually.

[Stripe-hosted onboarding](/connect/custom/hosted-onboarding)

[set the MCC manually](#mcc-manual)

If the industry that the user provides can’t be used, Stripe might use information from the connected account’s website to determine the MCC. If this also fails, the platform or Stripe’s default MCC (5734 Computer Software Stores) is used.

Sometimes accounts are flagged for manual review by Stripe. If this happens and Stripe determines the MCC on an account is inaccurate, we might update it. The new MCC can’t be manually changed by the platform, and an error is returned if the API is used to update the MCC.

## Setting MCCs manually

You can set the MCC manually when you create accounts. The examples below use the code for Computer Software Stores (5734), but you can see a full list in the next section.

[create accounts](/api/accounts/create#create_account-business_profile-mcc)

[full list](#list)

If your connected accounts share an MCC, you can provide the code using business_profile.mcc when you create accounts. In Connect Onboarding, your users won’t be asked for an industry. If you build your own onboarding UI, you don’t need to add a UI element for MCC.

[Connect](/connect)

If your connected accounts have different MCCs, Connect Onboarding will collect that information. If you aren’t using Connect Onboarding, you can provide a list of MCC options for users to choose from. Based on the user’s selection, you can pass an MCC appropriate for their business. If you don’t want to pass MCCs when you create accounts, you can update accounts with MCCs later.

[update accounts](/api/accounts/update#update_account-business_profile-mcc)

Similar to an MCC that’s set automatically, Stripe can override an MCC set manually if the connected account is flagged for review and we determine the MCC is inaccurate.

## Merchant category code list

The following is a list of supported MCCs that you can use when creating connected accounts. You must contact Stripe to use a restricted MCC.
