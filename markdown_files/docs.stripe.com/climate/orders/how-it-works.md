htmlHow it works | Stripe Documentation[Skip to content](#main-content)How it works[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fclimate%2Forders%2Fhow-it-works)[The Stripe Docs logo](/)[Search the docs/](#)[Create account](https://dashboard.stripe.com/register)[Sign in](https://dashboard.stripe.com/login?redirect=https%3A%2F%2Fdocs.stripe.com%2Fclimate%2Forders%2Fhow-it-works)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[No-code](/no-code)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[](#)[Get started](/get-started)[Payments](/payments)[Finance automation](/finance-automation)[Banking as a service](/financial-services)[Developer tools](/development)[](#)APIs & SDKsHelp[Overview](/docs/payments)[Accept a payment](#)[About Stripe payments](#)[Upgrade your integration](/docs/payments/upgrades)Start an integration[Payment Links](#)[Checkout](#)[Web Elements](#)[Mobile Elements](#)Payment scenarios[During the payment](#)[After the payment](#)[Add payment methods](#)[More payment scenarios](#)[Faster checkout with Link](#)Other Stripe products[Connect](#)[Terminal](#)[Financial Connections](#)[Crypto](#)[Climate](#)
Resources[About the APIs](#)[Regulation support](#)[Testing](/docs/testing)NetherlandsEnglish (United States)[](#)[](#)[Climate](/climate/faqs)·[Home](/docs)[Payments](/docs/payments)[Climate](/docs/climate)[Orders](/docs/climate/orders)# How it works

Learn how to create, monitor, and manage your carbon removal orders.Climate Orders enables companies to buy permanent carbon removal from the Frontier offtake portfolio and its individual suppliers. When you purchase carbon removal, your company can help contribute to the world’s net zero carbon goals and help fund emerging carbon removal technologies.

To help you incorporate carbon removal into your climate offering, Frontier does the following for you:

- Procures supply: This requires establishing purchasing criteria, sourcing promising projects, and negotiating contracts.
- Monitors supplier progress: This includes monitoring supplier performance against key milestones.
- Manages deliveries: This includes validating delivery and retiring purchases.

![Diagram describing the life cycle of a carbon removal order](https://b.stripecdn.com/docs-statics-srv/assets/frontier-diagram.9a70cf7ffa99c0589082ee922804e333.svg)

## Procure supply

Frontier’s in-house team of experts and a group of 60+ technical reviewers source and vet all suppliers. We look for permanent carbon removal solutions that have the potential to be low-cost and high-volume in the future, even if they aren’t today.

We use these factors to make purchasing decisions:

ApproachExecutionPortfolioDoes the carbon removal approach meet our target criteria?Can this team deliver on the proposal, given where the technology is today?Does this purchase help us build a diverse, risk-adjusted portfolio of carbon removal approaches?Specifically, Frontier focuses on technologies that meet the following criteria:

CriteriaDescriptionDurabilityStore carbon permanently (>1,000 years)Physical footprintTake advantage of carbon sinks and sources that don’t compete for arable landCostHave a path to being affordable at scale (<100 USD per ton)CapacityHave a path to being a meaningful part of the carbon removal solution portfolio (>0.5 gigatons per year)Net negativityMaximize net removal of atmospheric carbon dioxideAdditionalityResult in net new carbon removed, rather than taking credit for removal that was already going to occurVerifiabilityHave a published protocol that addresses key pathway uncertainties, has responded to scientific community feedback, and has a plan for independent verification of outcomesSafety and legalityHave a compelling case for why they don’t cause additional ecosystem damage or other ongoing externalities, has published ecosystem impact data and responded to feedback from the scientific community, and will actively manage the minimal remaining uncertainty within their deployments based on ongoing ecosystem monitoringPerformance dataHave technology that has been validated by data obtained through a pilot deploymentCommunity engagementHave a community benefits plan and has proactively engaged stakeholders and incorporated feedback into their deployment plansWe conduct diligence and sign long-term offtake agreements with the most promising suppliers that meet our criteria so that you don’t have to. Early offtakes are a unique way to buy carbon removal because they help projects start building today so that they can deliver tons in the near future.

Learn more about our available inventory.

## Monitor supplier progress

Because the carbon removal industry is in its early stages, it’s likely that some suppliers will be delayed or fail. Apart from conducting careful diligence, Frontier minimizes delivery delays and failures by actively monitoring progress against supplier-specific milestones, reallocating offtake agreements across suppliers as needed, and maintaining an inventory buffer.

NoteIf an order is delayed or fails, we’ll send you an email and the relevant webhook at least 60 days in advance.

- Delays. You’ll have the option of receiving a full refund or waiting for the tons to be delivered.
- Individual supplier failures. We’ll try to substitute your order with another similar supplier in the Frontier portfolio. Substituted carbon removal units might vary by pathway, geography, and price. If you don’t want a substitute, you can cancel the order and receive a full refund.

## Manage deliveries

When Frontier receives the verified carbon removal from the supplier, the carbon removal units are retired on an independent third party registry. All deliveries are third party verified.

At the time of delivery, Frontier shares a delivery certificate and important details about the suppliers that fulfilled your order.

![Preview of a carbon removal order certificate](https://b.stripecdn.com/docs-statics-srv/assets/frontier-certificate.377888457bcfecad08286964dd7e1751.svg)

When possible, Frontier retires the carbon removal units on your behalf (or on behalf of your beneficiary). If we can’t name the buyer on the third party registry, we’ll retire orders in Frontier’s name.

After delivery of your order, you can use your carbon removal units for net zero¹ or carbon neutrality claims.² You can’t make these claims prior to delivery.

## Get started

You can purchase carbon removal programmatically using the Climate API or manually using the Dashboard.

[Use the APIGet up and running using the Climate API.](/docs/climate/orders/order-carbon-removal)[Order manuallyNo CodePurchase manually from the Dashboard.](/docs/climate/orders/order-carbon-removal?dashboard-or-api=dashboard)

¹ The Science Based Targets Initiative (SBTi) has become the de facto standard for companies setting net zero targets. SBTi requires that, to make a net zero claim, companies must (i) plan to reduce their current emissions by at least 90% relative to current levels, (ii) purchase permanent carbon removal—such as that being sold through the Climate API—on behalf of the remaining 10% of emissions, and (iii) support beyond value chain mitigation—a somewhat unclear concept that’s meant to capture all the various ways that companies can contribute to mitigating climate change or reducing its impacts outside of reducing their own emissions (or neutralizing them through permanent carbon removal purchases).

² Carbon neutrality is somewhat poorly defined, but is generally claimed when a company purchases an amount of carbon credits (or carbon removal units) equal to their remaining emissions.

Was this page helpful?[Yes](#)[No](#)Need help?[Contact Support](https://support.stripe.com/).Check out our[product changelog](https://stripe.com/blog/changelog).Questions?[Contact Sales](https://stripe.com/contact/sales).Powered by[Markdoc](https://markdoc.dev)Sign up for developer updates:Sign upYou can unsubscribe at any time. Read our[privacy policy](https://stripe.com/privacy).On this page[Procure supply](#procure-supply)[Monitor supplier progress](#monitor-supplier-progress)[Manage deliveries](#manage-deliveries)[Get started](#get-started)Products Used[Climate](/climate/faqs)Stripe ShellTest modeAPI Explorer[](https://stripe.com/docs/stripe-cli#install)`Welcome to the Stripe Shell!

Stripe Shell is a browser-based shell with the Stripe CLI pre-installed. Log in to your
Stripe account and press Control + Backtick (`) on your keyboard to start managing your Stripe
resources in test mode.

- View supported Stripe commands: stripe help ▶️
- Find webhook events: stripe trigger ▶️ [event]
- Listen for webhook events: stripe listen ▶
- Call Stripe APIs: stripe [api resource] [operation] (e.g., stripe customers list ▶️)`The Stripe Shell is best experienced on desktop.`$`