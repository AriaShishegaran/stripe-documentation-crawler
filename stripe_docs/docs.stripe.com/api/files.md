- API Reference

- Docs

[Docs](/)

- Support

[Support](https://support.stripe.com)

- Sign in →

[Sign in →](https://dashboard.stripe.com/login)

# Files

[Files](/api/files)

This object represents files hosted on Stripe’s servers. You can upload files with the create file request (for example, when uploading dispute evidence). Stripe also creates files independently (for example, the results of a Sigma scheduled query).

[create file](#create_file)

[Sigma scheduled query](#scheduled_queries)

Related guide: File upload guide

[File upload guide](/file-upload)

[POST/v1/files](/api/files/create)

[GET/v1/files/:id](/api/files/retrieve)

[GET/v1/files](/api/files/list)

# The File object

[The File object](/api/files/object)

- idstringUnique identifier for the object.

Unique identifier for the object.

- purposeenumThe purpose of the uploaded file.Possible enum valuesaccount_requirementAdditional documentation requirements that can be requested for an account.additional_verificationAdditional verification for custom accounts.business_iconA business icon.business_logoA business logo.customer_signatureCustomer signature image.dispute_evidenceEvidence to submit with a dispute response.finance_report_runUser-accessible copies of query results from the Reporting dataset.identity_documentA document to verify the identity of an account owner during account provisioning.identity_document_downloadableImage of a document collected by Stripe Identity.pci_documentA self-assessment PCI questionnaire.Show 4 more

The purpose of the uploaded file.

[purpose](/file-upload#uploading-a-file)

Additional documentation requirements that can be requested for an account.

Additional verification for custom accounts.

A business icon.

A business logo.

Customer signature image.

Evidence to submit with a dispute response.

User-accessible copies of query results from the Reporting dataset.

A document to verify the identity of an account owner during account provisioning.

Image of a document collected by Stripe Identity.

A self-assessment PCI questionnaire.

- typenullable stringThe returned file type (for example, csv, pdf, jpg, or png).

The returned file type (for example, csv, pdf, jpg, or png).

- objectstring

- createdtimestamp

- expires_atnullable timestamp

- filenamenullable string

- linksnullable object

- sizeinteger

- titlenullable string

- urlnullable string

# Create a file

[Create a file](/api/files/create)

To upload a file to Stripe, you need to send a request of type multipart/form-data. Include the file you want to upload in the request, and the parameters for creating a file.

All of Stripe’s officially supported Client libraries support sending multipart/form-data.

- fileobjectRequiredA file to upload. Make sure that the specifications follow RFC 2388, which defines file transfers for the multipart/form-data protocol.Show child parameters

A file to upload. Make sure that the specifications follow RFC 2388, which defines file transfers for the multipart/form-data protocol.

- purposeenumRequiredThe purpose of the uploaded file.Possible enum valuesaccount_requirementAdditional documentation requirements that can be requested for an account.additional_verificationAdditional verification for custom accounts.business_iconA business icon.business_logoA business logo.customer_signatureCustomer signature image.dispute_evidenceEvidence to submit with a dispute response.identity_documentA document to verify the identity of an account owner during account provisioning.pci_documentA self-assessment PCI questionnaire.tax_document_user_uploadA user-uploaded tax document.terminal_reader_splashscreenSplashscreen to be displayed on Terminal readers.

The purpose of the uploaded file.

[purpose](/file-upload#uploading-a-file)

Additional documentation requirements that can be requested for an account.

Additional verification for custom accounts.

A business icon.

A business logo.

Customer signature image.

Evidence to submit with a dispute response.

A document to verify the identity of an account owner during account provisioning.

A self-assessment PCI questionnaire.

A user-uploaded tax document.

Splashscreen to be displayed on Terminal readers.

- file_link_dataobject

Returns the file object.

# Retrieve a file

[Retrieve a file](/api/files/retrieve)

Retrieves the details of an existing file object. After you supply a unique file ID, Stripe returns the corresponding file object. Learn how to access file contents.

[access file contents](/file-upload#download-file-contents)

No parameters.

If the identifier you provide is valid, a file object returns. If not, Stripe raises an error.

[an error](#errors)

# List all files

[List all files](/api/files/list)

Returns a list of the files that your account has access to. Stripe sorts and returns the files by their creation dates, placing the most recently created files at the top.

- purposestringFilter queries by the file purpose. If you don’t provide a purpose, the queries return unfiltered files.

Filter queries by the file purpose. If you don’t provide a purpose, the queries return unfiltered files.

- createdobject

- ending_beforestring

- limitinteger

- starting_afterstring

A dictionary with a data property that contains an array of up to limit files, starting after the starting_after file. Each entry in the array is a separate file object. If there aren’t additional available files, the resulting array is empty.
