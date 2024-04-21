# Issuing merchant categories

Every business that processes card payments is categorized using Merchant Category Codes (MCC). The category name is provided as a value for merchant_data.category on Authorization objects. Some businesses may not fit into a specific category, in which case they’re categorized as miscellaneous.

[Merchant Category Codes](https://en.wikipedia.org/wiki/Merchant_category_code)

[Authorization](/api#issuing_authorization_object)

You can use these categories when creating spending controls to restrict issued cards from being used with certain business types.

[spending controls](/issuing/controls/spending-controls)
