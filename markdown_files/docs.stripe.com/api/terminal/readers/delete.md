htmlDelete a Reader | Stripe API Reference[](/api)Find anything/
[Core Resources](#)
[Payment Methods](#)[Products](#)[Checkout](#)[Payment Links](#)[Billing](#)[Connect](#)[Fraud](#)[Issuing](#)[Terminal](#)[Treasury](#)[Entitlements](#)[Sigma](#)[Reporting](#)[Financial Connections](#)[Tax](#)[Identity](#)[Crypto](#)[Climate](#)[Forwarding](#)[Webhooks](#)[Sign in →](https://dashboard.stripe.com/login)# Delete a Reader

Deletes a Reader object.

### Parameters

No parameters.

### Returns

Returns the Reader object that was deleted.

DELETE/v1/terminal/readers/:idServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X DELETE https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7 \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "deleted": true}`# Cancel the current reader action

Cancels the current reader action.

### Parameters

No parameters.

### Returns

Returns an updated Reader resource.

POST/v1/terminal/readers/:id/cancel_actionServer-side languageStripe CLIcURL.NETGoJavaNode.jsPHPPythonRuby[](#)[](#)`curl -X POST https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/cancel_action \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"`Response`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "action": null,  "device_sw_version": "",  "device_type": "simulated_wisepos_e",  "ip_address": "0.0.0.0",  "label": "Blue Rabbit",  "last_seen_at": 1695402450407,  "livemode": false,  "location": "tml_FDOtHwxAAdIJOh",  "metadata": {},  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",  "status": "online"}`# Collect inputs using a ReaderPreview feature

Initiates an input collection flow on a Reader.

### Parameters

- inputsarray of objectsRequiredList of inputs to be collected using the Reader

Show child parameters
- metadataobjectSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to metadata.



### Returns

Returns an updated Reader resource.

POST/v1/terminal/readers/:id/collect_inputscURL[](#)[](#)`curl https://api.stripe.com/v1/terminal/readers/tmr_OXYJvwsea7PDiDHNciXRkytb/collect_inputs \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d "inputs[0][type]"=signature \  -d "inputs[0][custom_text][title]"=Signature \  -d "inputs[0][custom_text][description]"="Please sign below" \  -d "inputs[0][custom_text][submit_button]"=Submit \  -d "inputs[0][custom_text][skip_button]"=Skip \  -d "inputs[0][required]"=false \  -d "inputs[1][type]"=selection \  -d "inputs[1][custom_text][title]"=Selection \  -d "inputs[1][custom_text][description]"="Please select one" \  -d "inputs[1][required]"=true \  -d "inputs[1][selection][choices][0][style]"=primary \  -d "inputs[1][selection][choices][0][value]"=choice_1 \  -d "inputs[1][selection][choices][1][style]"=secondary \  -d "inputs[1][selection][choices][1][value]"=choice_2 \  -d "inputs[2][type]"=email \  -d "inputs[2][custom_text][title]"="Enter your email" \  --data-urlencode "inputs[2][custom_text][description]"="We'll send updates on your order and occasional deals" \  -d "inputs[2][custom_text][submit_button]"=Submit \  -d "inputs[2][custom_text][skip_button]"=Skip \  -d "inputs[2][required]"=false`Response`{  "id": "tmr_OXYJvwsea7PDiDHNciXRkytb",  "object": "terminal.reader",  "action": {    "failure_code": null,    "failure_message": null,    "collect_inputs": {      "inputs": [        {          "type": "signature",          "custom_text": {            "title": "Signature",            "description": "Please sign below",            "submit_button": "Submit",            "skip_button": "Skip"          },          "required": false,          "value": null        },        {          "type": "selection",          "custom_text": {            "title": "Selection",            "description": "Please select one"          },          "required": true,          "selection": {            "choices": [              {                "style": "primary",                "value": "choice_1"              },              {                "style": "secondary",                "value": "choice_2"              }            ],            "value": null          }        },        {          "type": "email",          "custom_text": {            "title": "Enter your email",            "description": "We'll send updates on your order and occasional deals",            "submit_button": "Submit",            "skip_button": "Skip"          },          "required": false,          "value": null        }      ]    },    "status": "in_progress",    "type": "collect_inputs"  },  "device_deploy_group": null,  "device_sw_version": null,  "device_type": "bbpos_wisepos_e",  "ip_address": "192.168.2.2",  "label": "Blue Rabbit",  "livemode": false,  "location": null,  "metadata": {},  "serial_number": "123-456-789",  "software": null,  "status": "online"}`# Confirm a PaymentIntent on the ReaderPreview feature

Finalizes a payment on a Reader.

### Parameters

- payment_intentstringRequiredPaymentIntent ID



### Returns

Returns an updated Reader resource.

POST/v1/terminal/readers/:id/confirm_payment_intentcURL[](#)[](#)`curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/confirm_payment_intent \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d payment_intent=pi_1NrpbFBHO5VeT9SUiCEDMdc8`Response`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "action": {    "failure_code": null,    "failure_message": null,    "collect_payment_method": {      "payment_intent": "pi_1NrpbFBHO5VeT9SUiCEDMdc8"    },    "status": "in_progress",    "type": "confirm_payment_intent"  },  "device_sw_version": "",  "device_type": "simulated_wisepos_e",  "ip_address": "0.0.0.0",  "label": "Blue Rabbit",  "last_seen_at": 1681320543815,  "livemode": false,  "location": "tml_FDOtHwxAAdIJOh",  "metadata": {},  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",  "status": "online"}`# Hand-off a PaymentIntent to a Reader and collect card detailsPreview feature

Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation.

### Parameters

- payment_intentstringRequiredPaymentIntent ID



### More parametersExpand all

- collect_configobject

### Returns

Returns an updated Reader resource.

POST/v1/terminal/readers/:id/collect_payment_methodcURL[](#)[](#)`curl https://api.stripe.com/v1/terminal/readers/tmr_FDOt2wlRZEdpd7/collect_payment_method \  -u "sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:" \  -d payment_intent=pi_1NrpbFBHO5VeT9SUiCEDMdc8`Response`{  "id": "tmr_FDOt2wlRZEdpd7",  "object": "terminal.reader",  "action": {    "failure_code": null,    "failure_message": null,    "collect_payment_method": {      "payment_intent": "pi_1NrpbFBHO5VeT9SUiCEDMdc8"    },    "status": "in_progress",    "type": "collect_payment_method"  },  "device_sw_version": "",  "device_type": "simulated_wisepos_e",  "ip_address": "0.0.0.0",  "label": "Blue Rabbit",  "last_seen_at": 1681320543815,  "livemode": false,  "location": "tml_FDOtHwxAAdIJOh",  "metadata": {},  "serial_number": "259cd19c-b902-4730-96a1-09183be6e7f7",  "status": "online"}`Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`