htmlUsing Checkout and Go (legacy) | Stripe Documentation[Skip to content](#main-content)Home[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Flegacy-checkout%2Fgo)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Flegacy-checkout%2Fgo)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[](#)[](#)# Using Checkout and Go (legacy)

WarningThis page is for the legacy version of Checkout

The legacy version of Checkout does not support European Strong Customer Authentication requirements. Update your integration now to avoid declined payments.

New, SCA-ready version of Checkout supports card payments, Apple Pay, Google Pay, and Dynamic 3D Secure. You can use the Checkout Migration Guide to move from the legacy version of Checkout to the new version. If you’d like to embed your payments form on your site, we recommend using Stripe Elements.

This tutorial demonstrates how to accept payments with Stripe Checkout in a web application built with Go. The application uses Checkout to accept credit cards from the end user and send tokens to a back-end API. The back-end route uses the Stripe Go library to create a charge. There are four steps:

1. [Install dependencies](#step-1-install-dependencies)
2. [Create the view template](#step-2-create-the-view-template)
3. [Create the routes](#step-3-create-routes)
4. [Run the application](#step-4-run-the-application)

[Install and configure dependencies](#step-1-install-dependencies)To follow along, you need a working Go environment. Create and enter a new directory, then make sure your package is using Go Modules:

Command Line`go mod init`Create a file named main.go and add the necessary imports and configuration values:

`package main

import (
  "fmt"
  "html/template"
  "net/http"
  "os"
  "path/filepath"

  "github.com/stripe/stripe-go/v76.0.0"
  "github.com/stripe/stripe-go/v76.0.0/charge"
  "github.com/stripe/stripe-go/v76.0.0/customer"
  "github.com/stripe/stripe-go/v{{GOLANG_MAJOR_VERSION}}"
)

func main() {
  publishableKey := os.Getenv("PUBLISHABLE_KEY")
  stripe.Key = os.Getenv("SECRET_KEY")
}`The file includes two values, the secret and publishable keys. These keys identify your account when you communicate with Stripe. In this example, the application extracts the values from local environment variables in order to cleanly separate configuration from code. Avoid hard-coding API access keys and other sensitive data in your application code.

Assign the secret key to the Key property of the stripe package. Assign the publishable key to a new variable called publishableKey so that it can be used later.

[Create the view template](#step-2-create-the-view-template)This example uses Go’s html/template package for server-side templating. Create a file named views/index.html for the index template:

`<html>
<head>
  <title>Checkout Example</title>
</head>
<body>
<form action="/charge" method="post" class="payment">
  <article>
    <label class="amount">
      <span>Amount: $5.00</span>
    </label>
  </article>

  <script src="https://checkout.stripe.com/checkout.js" class="stripe-button" data-key="{{ .Key }}" data-description="A month's subscription" data-amount="500" data-locale="auto"></script>
</form>
</body>
</html>`To integrate the form, load Checkout in an HTML <script> tag. It adds a button to the form that the user can click to display the credit card overlay. The overlay automatically performs validation and error handling. The action attribute specifies the path of the charge route. In the next step, you will see how the .Key attribute is populated with the publishable key for your Stripe account.

Add the following code to the main function in your main.go file so that it will load the template when the application runs:

`tmpls, _ := template.ParseFiles(filepath.Join("views", "index.html"))`[Create routes](#step-3-create-routes)The server exposes two routes:

1. A GET route that displays the payment form
2. A POST route that receives the payment token and creates the charge

Add the route handlers to the main function of the main.go file:

`http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
  tmpl := tmpls.Lookup("index.html")
  tmpl.Execute(w, map[string]string{"Key": publishableKey})
})

http.HandleFunc("/charge", func(w http.ResponseWriter, r *http.Request) {
  r.ParseForm()

  customerParams := &stripe.CustomerParams{
    Email: stripe.String(r.Form.Get("stripeEmail")),
  }
  customerParams.SetSource(r.Form.Get("stripeToken"))

  newCustomer, err := customer.New(customerParams)

  if err != nil {
    http.Error(w, err.Error(), http.StatusInternalServerError)
    return
  }

  chargeParams := &stripe.ChargeParams{
    Amount:      stripe.Int64(500),
    Currency:    stripe.String(string(stripe.CurrencyUSD)),
    Description: stripe.String("Sample Charge"),
    Customer:    stripe.String(newCustomer.ID),
  }

  if _, err := charge.New(chargeParams); err != nil {
    http.Error(w, err.Error(), http.StatusInternalServerError)
    return
  }

  fmt.Fprintf(w, "Charge completed successfully!")
})

http.ListenAndServe(":4567", nil)`The index route renders the Checkout form and displays it to the user. Pass the publishable key into the render function via a map literal so that the template can embed it in the Checkout form markup.

The charge route retrieves the email address and card token from the POST request body. It uses those parameters to create a Stripe customer. Next, it invokes the charge.New function, providing the Customer ID as an option.

In this example, the application charges the user $5. Stripe expects the developer to describe charges in cents, so compute the value of the amount parameter by multiplying the desired number of dollars by one hundred. Stripe charges also take an optional Desc parameter, which lets you describe the charge.

When the charge completes successfully, the application displays a message to the user. You could optionally use a second template in the charge route instead of a plain string.

That’s it, a complete Stripe integration in about 60 lines of Go code.

[Run the application](#step-4-run-the-application)Run the application from the command line:

Command Line`PUBLISHABLE_KEY=pk_test_VOOyyYjgzqdm8I3SrBqmh9qY SECRET_KEY=sk_test_Gx4mWEgHtCMr4DYMUIqfIrsz go run main.go`Specify values for the publishable and secret key environment variables. `

Navigate to the running application in your browser and click the button to launch the payment form. If you’re using Stripe test keys, you can test it with some dummy data. Enter the test number 4242 4242 4242 4242, a three digit CVC, and a future expiry date. Submit the form and see if the application correctly displays the successful charge page.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Install and configure dependencies](#step-1-install-dependencies)[Create the view template](#step-2-create-the-view-template)[Create routes](#step-3-create-routes)[Run the application](#step-4-run-the-application)Products Used[Checkout](/payments/checkout)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`