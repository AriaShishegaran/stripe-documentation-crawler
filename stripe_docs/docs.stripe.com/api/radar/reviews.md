- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Reviews

[Reviews](/api/radar/reviews)

Reviews can be used to supplement automated fraud detection with human expertise.

Learn more about Radar and reviewing payments here.

[Radar](/radar)

[here](/radar/reviews)

[GET/v1/reviews/:id](/api/radar/reviews/retrieve)

[GET/v1/reviews](/api/radar/reviews/list)

[POST/v1/reviews/:id/approve](/api/radar/reviews/approve)

# The Review object

[The Review object](/api/radar/reviews/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- chargenullable stringExpandableThe charge associated with this review.

The charge associated with this review.

- openbooleanIf true, the review needs action.

If true, the review needs action.

- payment_intentnullable stringExpandableThe PaymentIntent ID associated with this review, if one exists.

The PaymentIntent ID associated with this review, if one exists.

- reasonstringThe reason the review is currently open or closed. One of rule, manual, approved, refunded, refunded_as_fraud, disputed, or redacted.

The reason the review is currently open or closed. One of rule, manual, approved, refunded, refunded_as_fraud, disputed, or redacted.

- objectstring

- billing_zipnullable string

- closed_reasonnullable enum

- createdtimestamp

- ip_addressnullable string

- ip_address_locationnullable object

- livemodeboolean

- opened_reasonenum

- sessionnullable object

# Retrieve a review

[Retrieve a review](/api/radar/reviews/retrieve)

Retrieves a Review object.

No parameters.

Returns a Review object if a valid identifier was provided.

# List all open reviews

[List all open reviews](/api/radar/reviews/list)

Returns a list of Review objects that have open set to true. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

No parameters.

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit reviews, starting after review starting_after. Each entry in the array is a separate Review object. If no more reviews are available, the resulting array will be empty.

# Approve a review

[Approve a review](/api/radar/reviews/approve)

Approves a Review object, closing it and removing it from the list of reviews.

No parameters.

Returns the approved Review object.
