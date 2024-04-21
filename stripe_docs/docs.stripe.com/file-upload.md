# File upload guide

We support the ability to upload files to Stripe directly from the browser. Write JavaScript that calls the appropriate endpoint and includes your publishable API key. However, if you want to create a file link when uploading a file, you have to use the secret key.

When you upload a file to Stripe using the API, a file token and other information about the file is returned. The token can then be used in other API calls. This guide provides a detailed walk-through of this process.

## Uploading a file

To upload a file, send a multipart/form-data request to https://files.stripe.com/v1/files. Note that the subdomain files.stripe.com is different than most of Stripe’s API endpoints. The request should specify a purpose and a file. The following example uploads a file located at /path/to/a/file.jpg on your local file system with the purpose dispute_evidence:

The following example uploads a file using our Android SDK with the purpose dispute_evidence:

There are several valid purpose values, each with file format and size requirements.

[several valid purpose](/api#create_file-purpose)

identity_document images also need to be smaller than 8,000px by 8,000px.

The MIME type of the file you wish to upload must correspond to its file format.

Any Microsoft Office documents containing VBA macros will be rejected due to security concerns.

A successful request returns a file object.

[file](/api/files/object)

## Retrieving a File API resource

To retrieve the API resource for a File, make a GET request to the /v1/files endpoint of the files.stripe.com subdomain providing the file upload ID:

## Downloading File Contents

If the file purpose allows downloading the file contents, then the file includes a non-null url field indicating how to access the contents. This url requires authentication with your Stripe API keys.

[file](/api/files/object)

If you want unauthenticated access to a file whose purpose allows downloading, then you can produce anonymous download links by creating a file_link.

[file_link](/api#file_links)

The file_link resource has a url field that will allow unauthenticated access to the contents of the file.

## Using a file

After a file is uploaded, the file upload ID can be used in other API requests. For example, to attach an uploaded file to a particular dispute as evidence:

Note that you can only use an uploaded file in a single API request.

## Handling Upload Errors

When you use the File API to upload a PDF document, we run it through a series of checks to validate that it is correctly formatted and meets PDF specifications. We return an error for uploads that fail any of our checks.

Try the following to fix errors that we detect:

- Remove annotations or additional media you added to the document.

- If you cannot remove your annotations or media, or if you combined several PDFs into one, try using your computer’s Print to PDF function to create a fresh document.Print to PDF with macOSPrint to PDF with Adobe Acrobat

- Print to PDF with macOS

[Print to PDF with macOS](https://support.apple.com/guide/mac-help/save-a-document-as-a-pdf-on-mac-mchlp1531/mac)

- Print to PDF with Adobe Acrobat

[Print to PDF with Adobe Acrobat](https://helpx.adobe.com/acrobat/using/print-to-pdf.html)
