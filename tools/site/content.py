"""Site copy for tools/site/build.py.

Editorial rule: name no clients or projects; customer-journey examples are illustrative, not claims about results.
"""

SERVICES = [
    {
        "key": "web", "slug": "websites-branding", "icon": "web",
        "nav": "Websites & Branding",
        "blurb": "Positioning, websites and landing pages",
        "summary": "Clarify your story and create a digital experience built around the action you want visitors to take.",
        "link": "Explore Websites & Branding",
        "eyebrow": "Websites & Branding",
        "seo_title": "Website Design & Branding | Spark Media",
        "seo_desc": "Brand positioning, website design and landing pages that connect a compelling story to a clear next step.",
        "h1": "A better first impression. A clearer path forward.",
        "intro": "Your site should help people understand why you matter, trust what they see and know what to do next. We combine positioning, design, content and technology to make that possible.",
        "blocks": [
            ("Built around the decisions your customers make.",
             ["We start with the questions visitors bring to your site: Is this for me? Can they solve my problem? What happens if I reach out?",
              "Those answers guide the message, structure and design. From there, we build the forms, calls to action and system connections that turn an attractive site into a useful business asset."]),
        ],
        "help": ["Brand messaging and positioning", "Website strategy and design", "Landing pages", "Conversion-focused copy",
                 "Lead capture and booking flows", "SEO foundations", "Integration with your CRM and business tools"],
        "close_h2": "Make the website part of the workflow.",
        "close_body": "An inquiry shouldn’t end in an inbox nobody watches. We help connect your site to the people and systems responsible for the next step.",
        "cta": "Plan Your Website",
        "solutions": ["capture", "connect"],
    },
    {
        "key": "ai", "slug": "ai-agents-automation", "icon": "ai",
        "nav": "AI Agents & Automation",
        "blurb": "Voice, messaging and workflow automation",
        "summary": "Respond to inquiries, guide conversations and reduce repetitive work with AI and thoughtfully designed workflows.",
        "link": "Explore AI & Automation",
        "eyebrow": "AI Agents & Automation",
        "seo_title": "AI Agents & Business Automation | Spark Media",
        "seo_desc": "Practical AI voice, messaging and workflow automation to help your business respond faster and reduce manual work.",
        "h1": "Helpful conversations, even when your team is busy.",
        "intro": "A missed call or delayed response can turn a promising opportunity into a dead end. We design AI-assisted conversations and automations that help customers get answers, help your team get context and keep the next step moving.",
        "blocks": [
            ("AI with a job to do.",
             ["An AI agent can answer common questions, gather the details your team needs, route an inquiry or help someone book a time.",
              "Behind the conversation, workflows can update records, notify the right person and keep follow-up organized. Each implementation should reflect your business rules and include a clear way to hand off to a human."]),
        ],
        "help": ["AI voice agents", "Missed-call response", "Two-way SMS and email workflows", "Lead qualification",
                 "Appointment scheduling", "Lead reactivation", "Internal alerts and routing", "Workflow design and oversight"],
        "close_h2": "The best automation feels like good service.",
        "close_body": "We focus on the quality of the interaction, the accuracy of the information and the experience of the person on the other end.",
        "cta": "Explore an AI Use Case",
        "solutions": ["missed", "reactivate", "capture"],
    },
    {
        "key": "ads", "slug": "paid-media", "icon": "ads",
        "nav": "Paid Media",
        "blurb": "Google and Meta campaigns, tracked end to end",
        "summary": "Reach the right audience with Google and Meta campaigns connected to landing pages, follow-up and meaningful measurement.",
        "link": "Explore Paid Media",
        "eyebrow": "Paid Media",
        "seo_title": "Google & Meta Ads Management | Spark Media",
        "seo_desc": "Paid media strategy and management connected to landing pages, lead response and conversion tracking.",
        "h1": "Better campaigns start beyond the click.",
        "intro": "Getting attention is only the beginning. We connect paid advertising to the page, message and follow-up experience that comes after it.",
        "blocks": [
            ("Make every handoff count.",
             ["We develop campaigns around the people you’re trying to reach and the action you want them to take.",
              "Then we look at the full path: Does the landing page answer the right questions? Is the inquiry captured correctly? Who responds, and how quickly? What can the business learn from the outcome?"]),
        ],
        "help": ["Google Ads", "Meta Ads", "Retargeting", "Audience and offer strategy", "Landing-page alignment",
                 "Campaign creative testing", "Conversion tracking", "Reporting and optimization"],
        "close_h2": "See more than traffic and form fills.",
        "close_body": "We help you connect campaign activity to the conversations and opportunities that matter to your business.",
        "cta": "Talk About Advertising",
        "solutions": ["capture", "missed"],
    },
    {
        "key": "creative", "slug": "content-creative", "icon": "creative",
        "nav": "Content & Creative",
        "blurb": "Campaign creative, short-form video and UGC",
        "summary": "Make your message more compelling with campaign creative, content strategy, short-form video and UGC programs.",
        "link": "Explore Content & Creative",
        "eyebrow": "Content & Creative",
        "seo_title": "Content, Creative & UGC Strategy | Spark Media",
        "seo_desc": "Campaign creative, content and UGC strategy that make your message clear, credible and useful across channels.",
        "h1": "Creative that gives people a reason to care.",
        "intro": "Strong content shows what makes your business different in a way customers can feel and understand. We develop creative ideas and content systems that support your brand, your campaigns and the conversations you want to start.",
        "blocks": [
            ("The right message for the right moment.",
             ["Some audiences need a quick demonstration. Others need a detailed explanation, a customer perspective or a human face.",
              "We shape content around the questions people ask at each stage, then adapt it for your website, ads, social channels and follow-up."]),
        ],
        "help": ["Content strategy", "Copywriting", "Ad concepts and creative", "Short-form video strategy",
                 "UGC concepts and creator coordination", "Social content planning", "Creative testing"],
        "note": "Production may involve specialist collaborators depending on scope.",
        "close_h2": "Give your marketing something worth saying.",
        "close_body": "Tell us who you’re trying to reach and what they need to believe. We’ll help shape the ideas and the content system around them.",
        "cta": "Plan Your Creative",
        "extra_link": ("See our UGC and Instagram approach", "/social/"),
        "solutions": ["capture", "reactivate"],
    },
    {
        "key": "crm", "slug": "crm-sales-enablement", "icon": "crm",
        "nav": "CRM & Sales Enablement",
        "blurb": "Pipelines, routing and follow-up",
        "summary": "Give your team a clearer pipeline and a better way to qualify, follow up and book conversations.",
        "link": "Explore CRM & Sales",
        "eyebrow": "CRM & Sales Enablement",
        "seo_title": "CRM & Sales Enablement | Spark Media",
        "seo_desc": "CRM, pipeline and follow-up systems that help your team organize leads, book conversations and understand the sales journey.",
        "h1": "Give your sales process a better operating system.",
        "intro": "A new lead is only valuable if the right person sees it, understands it and knows what to do next. We help structure the information and workflows your team needs to move opportunities forward.",
        "blocks": [
            ("A clearer picture, from inquiry to outcome.",
             ["We map your stages, define useful handoffs and build follow-up around real buying behavior.",
              "Your team can see where a prospect came from, what they’ve asked, who owns the next action and where the opportunity stands."]),
        ],
        "help": ["CRM setup and architecture", "Pipeline design", "Lead routing and qualification", "Email and SMS nurturing",
                 "Appointment flows", "Database reactivation", "Sales tasks and alerts", "Practical reporting"],
        "close_h2": "Make it easier to follow through.",
        "close_body": "When everyone can see the next step, fewer opportunities go quiet. Let’s look at how your pipeline works today.",
        "cta": "Improve Your Sales Flow",
        "solutions": ["capture", "reactivate", "connect"],
    },
    {
        "key": "integration", "slug": "ai-consulting-integration", "icon": "integrate",
        "nav": "AI Consulting & Integration",
        "blurb": "Connect your software and find useful AI",
        "summary": "Find useful AI opportunities and help the software you rely on share information and trigger the right actions.",
        "link": "Explore Consulting & Integration",
        "eyebrow": "AI Consulting & Systems Integration",
        "seo_title": "AI Consulting & Systems Integration | Spark Media",
        "seo_desc": "Practical AI consulting and software integration for businesses with disconnected tools and manual workflows.",
        "h1": "Your tools should work together. Your people should have room to work.",
        "intro": "Many businesses have assembled a powerful software stack one purchase at a time. But when the systems don’t connect, staff become the integration. They re-enter data, chase status updates and work around information that lives in the wrong place.",
        "blocks": [
            ("We start by understanding how work actually moves.",
             ["We look at the systems you use, the information each one holds and the moments where work slows down.",
              "Then we recommend a practical path: connect existing platforms, redesign a workflow, build a useful dashboard, introduce an AI assistant or simplify a step altogether. The answer depends on the business, not on a preferred tool."]),
            ("A connected system is easier to run and easier to improve.",
             ["The aim is for information to reach the right place, for routine actions to happen reliably and for people to know when they need to step in.",
              "We design around the tools you own and the team that will use them."]),
        ],
        "help": ["Process mapping", "AI opportunity assessments", "CRM and software integrations", "Workflow automation",
                 "Operational dashboards", "AI-assisted internal processes", "Implementation planning and ongoing refinement"],
        "close_h2": "Let’s see how work moves through your business.",
        "close_body": "Bring a list of your tools and the steps that feel harder than they should. We’ll help you find where a connection would make the biggest difference.",
        "cta": "Let’s Map Your Systems",
        "solutions": ["connect", "capture"],
    },
]
for _s in SERVICES:
    _s["href"] = f'/services/{_s["slug"]}/'


SOLUTIONS = [
    {
        "key": "connect", "slug": "connect-your-systems", "icon": "connect",
        "nav": "Connect Your Systems",
        "blurb": "Get your software sharing the right information",
        "problem": "Our software doesn’t talk to each other.",
        "summary": "Connect the platforms and handoffs that keep your business moving.",
        "seo_title": "Connect Disconnected Business Software | Spark Media",
        "seo_desc": "Bring your CRM, website, scheduling, marketing and industry software into a more useful workflow.",
        "h1": "Make your software stack act like a team.",
        "intro": "Your company may run on ten, twenty or more platforms. Each one solves a particular problem, but the gaps between them create new ones. We help your tools exchange the right information so your team doesn’t have to carry it between systems by hand.",
        "blocks": [
            ("Where does the work get stuck?",
             ["A form submission doesn’t reach the sales team. A booked appointment isn’t visible in the CRM. A status change in one platform never triggers the next step. Reporting stops at the ad click because the outcome lives somewhere else.",
              "These are workflow problems, and they can often be solved without replacing the entire stack."]),
        ],
        "steps": ["Map the tools, owners and key handoffs.", "Identify the data and events each system needs.",
                  "Design integrations, alerts and human checkpoints.", "Test the real-world path and refine it as the business changes."],
        "outcome": "Fewer blind spots. Less copying and pasting. A clearer picture of what happens from first contact to completed work.",
        "cta": "Map My Workflow",
        "services": ["integration", "crm", "ai"],
    },
    {
        "key": "capture", "slug": "capture-convert-leads", "icon": "capture",
        "nav": "Capture & Convert Leads",
        "blurb": "Turn inquiries into real conversations",
        "problem": "We’re getting leads but losing momentum.",
        "summary": "Improve what happens between inquiry, qualification and the next conversation.",
        "seo_title": "Lead Capture & Conversion Systems | Spark Media",
        "seo_desc": "Connect campaigns, pages, CRM and follow-up to turn more inquiries into useful sales conversations.",
        "h1": "Don’t let the next opportunity stall after “submit.”",
        "intro": "A lead form isn’t the finish line. The experience that follows determines whether an interested person gets help, books a conversation or drifts away.",
        "blocks": [
            ("Build the path from interest to action.",
             ["We connect your advertising and website to a response process that fits the inquiry. That can include better forms, smarter routing, automated first responses, qualification, scheduling, reminders and clear ownership for your team.",
              "We also help you see where inquiries came from and what happened next."]),
        ],
        "components": ["Campaign and landing-page alignment", "Lead capture", "CRM integration", "Routing and qualification",
                       "Email and SMS follow-up", "Appointment booking", "Conversion reporting"],
        "cta": "Improve My Lead Flow",
        "services": ["ads", "web", "crm", "ai"],
    },
    {
        "key": "missed", "slug": "never-miss-an-opportunity", "icon": "phone",
        "nav": "Never Miss an Opportunity",
        "blurb": "A dependable first response, day or night",
        "problem": "We miss calls and respond too slowly.",
        "summary": "Create a more dependable first response with the right mix of AI, automation and human follow-through.",
        "seo_title": "Missed Call & Fast Lead Response Solutions | Spark Media",
        "seo_desc": "AI-assisted calls, messages and lead routing to help your business respond when customers are ready to talk.",
        "h1": "Be there when a customer is ready to talk.",
        "intro": "Calls come in after hours. Inquiries arrive while your team is with another customer. Good prospects don’t always try twice. We help you build a first-response experience that keeps the conversation moving.",
        "blocks": [
            ("A response that fits the situation.",
             ["Depending on your needs, that could mean an AI voice agent, a timely text, a helpful email, an alert to your team or a booking flow.",
              "The system should answer what it can, collect useful context and bring in a person when the conversation calls for one."]),
        ],
        "components": ["Missed-call follow-up", "AI call handling", "Lead intake and qualification", "Booking and reminders",
                       "Urgent inquiry routing", "Conversation logging and team alerts"],
        "cta": "Improve My Response Process",
        "services": ["ai", "crm", "integration"],
    },
    {
        "key": "reactivate", "slug": "reactivate-your-database", "icon": "reactivate",
        "nav": "Reactivate Your Database",
        "blurb": "Reconnect with past inquiries",
        "problem": "Our database is full of unfinished conversations.",
        "summary": "Reconnect with past inquiries through relevant, organized outreach.",
        "seo_title": "Lead Reactivation & Follow-Up | Spark Media",
        "seo_desc": "Reconnect with past inquiries using relevant outreach, organized conversations and clear next steps.",
        "h1": "Your next conversation may already be in your database.",
        "intro": "Many prospects weren’t ready when they first reached out. Others never got the follow-up they needed. We help you find sensible ways to reconnect, learn where interest stands and make it easy to take the next step.",
        "blocks": [
            ("Relevant outreach, with room for a real conversation.",
             ["We segment contacts around the context you have, develop appropriate messages and set up follow-up that responds to what people actually say.",
              "Interested replies move to your team or into a booking path. People who don’t want further contact are respected."]),
        ],
        "components": ["Contact segmentation", "Reactivation campaigns", "Two-way SMS and email", "Response categorization",
                       "Appointment routing", "CRM updates and reporting"],
        "cta": "Explore Reactivation",
        "services": ["crm", "ai", "creative"],
    },
]
for _s in SOLUTIONS:
    _s["href"] = f'/solutions/{_s["slug"]}/'


HOME = {
    "eyebrow": "Marketing + AI + Connected Systems",
    "h1": "Make every part of your business work together.",
    "body": "Your website creates an inquiry. Your ads bring in a lead. Your phone rings. Your team follows up. But when those steps live in separate tools, opportunities slip through the cracks. Spark Media brings marketing, AI and business automation together so your customer journey works as one connected system.",
    "intro_h2": "More software shouldn’t mean more friction.",
    "intro_body": [
        "Most growing companies already have the tools: a website, ad accounts, a CRM, scheduling software, email, texting, reporting and a stack of industry-specific platforms. The problem is that those tools often don’t share the right information at the right time. Teams copy data by hand, leads wait for a response and nobody has a clear picture of what’s working.",
        "We help you untangle the stack, connect the steps that matter and design better ways to work. Sometimes that means a stronger website or better advertising. Sometimes it’s an AI agent, a smarter follow-up process or an integration between the systems you already use. Usually, it’s the combination that moves the business forward.",
    ],
    "what_h2": "Creative thinking. Technical execution. One clear goal.",
    "cards": [
        {"icon": "web", "title": "Build your presence", "body": "Websites, brand positioning, landing pages and digital experiences that make it easy to understand your business and take the next step."},
        {"icon": "ads", "title": "Create demand", "body": "Google and Meta campaigns, content, creative and UGC strategy that bring the right people into the conversation."},
        {"icon": "ai", "title": "Convert opportunities", "body": "AI voice and messaging, lead qualification, CRM workflows, appointment scheduling and sales follow-up that help teams respond while interest is high."},
        {"icon": "integrate", "title": "Connect the business", "body": "Integrations, dashboards and practical AI implementations that reduce manual work and make information useful across your tools."},
    ],
    "connect_h2": "From first impression to real conversation.",
    "connect_body": [
        "Imagine someone clicks an ad, lands on a page built for their needs and requests a consultation. Their details flow into the right place. A fast, relevant response helps qualify the inquiry and offers a time to talk.",
        "That’s the kind of connected experience we build: useful for the customer, visible to your team and measurable for the business.",
    ],
    "journey": [
        ("click", "They click an ad", "A campaign reaches someone who needs what you offer."),
        ("web", "They land on a page built for them", "The message matches the ad and answers their first questions."),
        ("form", "They request a consultation", "Their details flow straight into the right place in your CRM."),
        ("ai", "A fast, relevant response", "An AI-assisted reply helps qualify the inquiry and offers a time to talk."),
        ("users", "Your team sees the full context", "Who they are, what they asked and where they came from."),
        ("reactivate", "Follow-up keeps going", "If they aren’t ready yet, the conversation doesn’t quietly end."),
        ("chart", "You see what started it", "Which campaign began the conversation and what happened after."),
    ],
    "stack_h2": "Twenty tools. One business. Let’s get them talking.",
    "stack_body": [
        "The goal isn’t to replace every platform you use. It’s to understand what each system does, where the handoffs fail and which connections will make the biggest difference.",
        "We map your workflows, clean up the flow of information and build automation around how your team actually works.",
    ],
    "tools": [
        ("Website forms", "on"), ("CRM", "on"), ("Google Ads", "on"), ("Meta Ads", ""), ("Phone system", "broken"),
        ("Scheduling", "on"), ("Email", ""), ("Texting", "broken"), ("Invoicing", ""), ("Reporting", "broken"),
        ("Spreadsheets", "broken"), ("Industry software", ""), ("Reviews", ""), ("Team chat", "on"), ("Payments", ""),
        ("Help desk", ""), ("AI assistant", "on"), ("Project management", ""),
    ],
    "approach_h2": "Start with the bottleneck. Build for the whole journey.",
    "steps": [
        ("Discover", "We learn how customers find you, how your team responds and which tools hold the critical information."),
        ("Design", "We prioritize the changes that can improve the customer experience and make work easier for your team."),
        ("Build", "We create the pages, campaigns, automations and connections that make the plan real."),
        ("Improve", "We look at what happens after launch, refine the system and help it evolve with your business."),
    ],
    "close_h2": "Tell us what’s slowing you down.",
    "close_body": "Whether you need a better website, more qualified demand or a way to make your software work together, we’ll help identify the next move.",
}

SERVICES_PAGE = {
    "h1": "Everything your growth system needs to work.",
    "intro": "Marketing generates attention. Your website turns attention into interest. Your team and systems turn that interest into customers. We work across those connections, bringing creative, technical and operational skills together around your goals.",
    "close_h2": "You don’t need all six services to get started.",
    "close_body": "We’ll begin with the problem you need to solve and bring in the right capabilities as the work calls for them.",
}

SOLUTIONS_PAGE = {
    "h1": "Start with the problem. Connect the right solution.",
    "intro": "You shouldn’t need to diagnose which service category your problem belongs in. Tell us what isn’t working. We’ll trace the customer and team experience, then build the pieces that solve it.",
}

INDUSTRIES_PAGE = {
    "h1": "Different businesses. Different buying journeys. Connected thinking.",
    "intro": "A venue inquiry, a local service call and a complex B2B sales conversation require different experiences. We adapt the message, channels and systems to the way your customers actually make decisions.",
    "items": [
        {"eyebrow": "Hospitality & venues", "title": "From first interest to tour or booking.",
         "body": "Help guests understand the experience, inquire with confidence and move smoothly from first interest to tour or booking. Websites, content, inquiry flows and coordinated follow-up can work together around the customer journey.",
         "tags": ["Inquiry flows", "Content & creative", "Tour and booking follow-up"],
         "img": "industry-hospitality.jpg", "alt": "A host welcomes guests into an event venue set with long tables and string lights"},
        {"eyebrow": "B2B & industrial", "title": "Explain complex capabilities clearly.",
         "body": "Support a longer buying cycle and create better handoffs between marketing and sales. We can connect positioning, website content, targeted campaigns and account-focused follow-up.",
         "tags": ["Positioning", "Targeted campaigns", "Marketing-to-sales handoffs"],
         "img": "industry-b2b.jpg", "alt": "Two colleagues review information on a tablet inside a modern manufacturing facility"},
        {"eyebrow": "Healthcare & wellness", "title": "Make the next step easy to find.",
         "body": "Make it easier for prospective patients or customers to find the right information, reach your team and understand the next step. Workflows should fit the sensitivity and requirements of the information involved.",
         "tags": ["Clear information", "Appointment flows", "Appropriate data handling"],
         "img": "industry-healthcare.jpg", "alt": "A staff member helps a client at the front desk of a bright wellness clinic"},
        {"eyebrow": "Local services", "title": "Turn high-intent moments into conversations.",
         "body": "Turn high-intent searches, calls and form fills into timely conversations. We help connect ads, local pages, lead response and scheduling.",
         "tags": ["Search ads", "Local pages", "Fast lead response", "Scheduling"],
         "img": "industry-local.jpg", "alt": "A home service technician holding a tablet smiles at a customer’s front door"},
    ],
    "close_h2": "Don’t see your industry?",
    "close_body": "If growth depends on a better customer journey and less friction between your tools, we should talk.",
}

ABOUT_PAGE = {
    "h1": "Marketing people and systems people, at the same table.",
    "intro": "Spark Media exists for businesses that need more than another campaign or another software subscription. We bring marketing strategy, creative execution and technical implementation together so each investment supports the next.",
    "principles": [
        ("We care about what happens after the click.",
         ["A compelling ad can start a conversation. A strong website can build confidence.",
          "But growth also depends on who responds, what information they have, how the customer is guided and whether the business can learn from the outcome. We work across that full experience."]),
        ("Practical AI, built around people.",
         ["We look for places where technology can make service more responsive and work more manageable.",
          "That means understanding the job first, choosing tools for a reason and making sure your team remains in control of the process."]),
        ("Built to fit your business.",
         ["Your workflows, customers and existing platforms shape the solution. We aim to make the systems you rely on more useful and give your team a clearer view of what happens next.",
          "Your business should have appropriate access to and ownership of its client-facing assets, accounts and data, as defined in the project agreement."]),
    ],
    "founder": "Spark Media is led by founder Dave McCormick. If you’d like to talk through your goals directly, call (702) 747-5589 or book a conversation.",
}

CONTACT_PAGE = {
    "h1": "Let’s find the next move that matters.",
    "intro": "Tell us what you’re trying to improve. A clearer website? Better lead flow? Faster responses? A software stack that finally works together? We’ll start with a conversation about the goal and the obstacles in the way.",
    "topics": ["Website & Branding", "Advertising", "AI & Automation", "CRM & Sales", "Systems Integration", "Not sure yet? That’s fine too."],
}


# ---------------------------------------------------------------- imagery
# Photos and abstract art live in /assets/images/site/. "chips" are the small floating UI notes over hero photos;
# they illustrate the kind of thing the system does and are not claims about results.

PAGE_MEDIA = {
    # services
    "web": {"img": "svc-web.jpg", "alt": "A designer and a business owner review a website layout on a large monitor",
            "chips": [("web", "Landing page live", "Built for the campaign"), ("form", "New inquiry", "Sent to the CRM")],
            "band": ("abs-glass.jpg", "Every page should lead somewhere.", "Clear message, clear next step, connected to the people who follow up.")},
    "ai": {"img": "svc-ai.jpg", "alt": "A café owner glances at a phone notification about a customer conversation while her team works",
           "chips": [("ai", "Conversation handled", "Details captured"), ("calendar", "Call booked", "Thu 10:30 AM")],
           "band": ("abs-network.jpg", "Fast answers. Clear handoffs.", "AI handles the routine parts of the conversation and brings in your team when it matters.")},
    "ads": {"img": "svc-ads.jpg", "alt": "Two marketers review advertising performance charts on a laptop",
            "chips": [("ads", "Campaign", "Search + social"), ("chart", "Source tracked", "From click to booking")],
            "band": ("abs-ribbons.jpg", "Attention is the start, not the finish.", "Campaigns work harder when the page, the response and the reporting are built with them.")},
    "creative": {"img": "svc-creative.jpg", "alt": "A small crew films a business owner talking to camera in her boutique",
                 "chips": [("creative", "Short-form video", "Cut for every channel"), ("users", "Real people", "Your team and customers")],
                 "band": ("abs-orbs.jpg", "Say something worth stopping for.", "Content shaped around the questions your customers actually ask.")},
    "crm": {"img": "svc-crm.jpg", "alt": "A sales coordinator with a headset works at a desk with a pipeline board on the monitor",
            "chips": [("crm", "Pipeline updated", "Stage: Consultation"), ("users", "Owner assigned", "Next step is clear")],
            "band": ("abs-blocks.jpg", "Everyone can see the next step.", "A pipeline your team trusts is one they actually use.")},
    "integration": {"img": "svc-integration.jpg", "alt": "A consultant and an operations manager map a workflow with sticky notes on a glass wall",
                    "chips": [("integrate", "Systems connected", "CRM · scheduling · billing"), ("connect", "Data in sync", "No re-typing")],
                    "band": ("abs-blocks.jpg", "Staff shouldn’t be the integration.", "Let the systems pass the information along, so people can focus on the work.")},
    # solutions
    "connect": {"img": "sol-connect.jpg", "alt": "An operations manager at a standing desk with two monitors showing simple connected dashboards",
                "chips": [("connect", "Handoff automated", "Form → CRM → team"), ("chart", "One clear view", "First contact to done")],
                "band": ("abs-network.jpg", "Fewer blind spots.", "Information reaches the right place without anyone carrying it there by hand.")},
    "capture": {"img": "sol-capture.jpg", "alt": "A young professional on a sofa fills out a short inquiry form on a phone",
                "chips": [("form", "Form submitted", "Routed in seconds"), ("calendar", "Time offered", "Book a consultation")],
                "band": ("abs-ribbons.jpg", "Interest fades fast.", "The experience right after “submit” decides what happens next.")},
    "missed": {"img": "sol-missed.jpg", "alt": "A restaurant host helps guests while a phone on the counter lights up with a call",
               "chips": [("phone", "Missed call", "Text sent right away"), ("ai", "Question answered", "Team alerted")],
               "band": ("abs-orbs.jpg", "Be there on the first try.", "A dependable first response, even when everyone is busy.")},
    "reactivate": {"img": "sol-reactivate.jpg", "alt": "A woman at her kitchen table smiles as she reads a text message on her phone",
                   "chips": [("reactivate", "Reply received", "“Yes, still interested”"), ("calendar", "Moved to booking", "Team notified")],
                   "band": ("abs-waves.jpg", "Pick the conversation back up.", "Relevant, respectful outreach to people who already raised their hand.")},
    # other pages
    "services": {"img": "abs-glass.jpg", "alt": "", "abstract": True},
    "solutions": {"img": "abs-orbs.jpg", "alt": "", "abstract": True},
    "industries": {"img": "abs-waves.jpg", "alt": "", "abstract": True},
    "about": {"img": "abs-ribbons.jpg", "alt": "", "abstract": True},
    "contact": {"img": "contact.jpg", "alt": "A consultant shakes hands with a small business owner across a cafe table",
                "chips": [("users", "Real conversation", "About your goals"), ("calendar", "Pick a time", "That works for you")]},
}


# ---------------------------------------------------------------- home services (emergency Google Search offer)

TIERS = [
    {"label": "Most start here", "name": "Phone ring", "price": "$249", "per": "/mo",
     "summary": "Call-only Google Ads. Emergency search. The call hits your phone.",
     "items": ["Call-only Google Search campaigns", "Emergency, call-now keywords", "Tight geo targeting",
               "Calls route to your phone", "Ad spend is yours, extra"]},
    {"label": "Adds follow-up", "name": "Ring + follow-up", "price": "$399", "per": "/mo",
     "summary": "Everything in Phone ring, plus GoHighLevel so a missed ring is not a missed job.",
     "items": ["Everything in Phone ring", "Missed-call text-back", "Job follow-up",
               "Review ask after the job", "Ad spend is still yours, extra"], "featured": True},
]

OFFER_FAQ = [
    ("Is ad spend included?", "No. $249 and $399 are our management fees. You pay Google for the clicks."),
    ("Long-term contract?", "No. Month-to-month. We keep the account by making the phone ring."),
    ("Do I need a new website?", "No. This is call-only. The ad’s job is to make your phone ring."),
    ("Who is this for?", "Plumbers, HVAC, electricians, locksmiths and garage door companies: trades where people call the moment something breaks."),
]

OFFER_STEPS = [
    ("Strategy call", "15–20 minutes. We learn the trade, the service area, and whether you can pick up emergency calls. If it is not a fit, we say so."),
    ("The offer", "$249/mo: call-only Google Ads to your phone. $399/mo adds missed-call text, job follow-up, and a review ask. Ad spend is yours, extra."),
    ("If we turn it on", "Emergency keywords. Tight geo. The homeowner taps Call. It rings your phone."),
]

TRADES = [
    {"slug": "plumber", "path": "/plumber-marketing.html", "name": "Plumber", "kind": "emergency", "img": "trade-plumber.jpg",
     "alt": "A plumber repairs pipes under a kitchen sink in a bright home",
     "h1": "Burst pipe. The Google call hits your phone.",
     "lede": "They are not shopping. Water is on the floor. They Google “emergency plumber” and tap Call. We run that ad. $249/mo. Ad spend extra.",
     "search": "emergency plumber", "related": ["hvac", "electrician", "locksmith"]},
    {"slug": "hvac", "path": "/hvac-marketing.html", "name": "HVAC", "kind": "emergency", "img": "trade-hvac.jpg",
     "alt": "An HVAC technician checks an outdoor air conditioning unit beside a house",
     "h1": "No AC. The Google call hits your phone.",
     "lede": "House is hot. They are not reading a blog. They Google “AC not cooling” and tap Call. We run that ad. $249/mo. Ad spend extra.",
     "search": "AC not cooling", "related": ["plumber", "electrician", "garage-door"]},
    {"slug": "electrician", "path": "/electrician-marketing.html", "name": "Electrician", "kind": "emergency", "img": "trade-electrician.jpg",
     "alt": "An electrician in safety glasses works on a residential electrical panel",
     "h1": "No power. The Google call hits your phone.",
     "lede": "Lights out. Outlet sparking. They Google “emergency electrician” and tap Call. We run that ad. $249/mo. Ad spend extra.",
     "search": "emergency electrician", "related": ["plumber", "hvac", "locksmith"]},
    {"slug": "locksmith", "path": "/locksmith-marketing.html", "name": "Locksmith", "kind": "emergency", "img": "trade-locksmith.jpg",
     "alt": "A locksmith rekeys the front door lock of a modern home",
     "h1": "Locked out. The Google call hits your phone.",
     "lede": "Keys in the car. Door won’t open. They Google “locksmith near me” and tap Call. We run that ad. $249/mo. Ad spend extra.",
     "search": "locksmith near me", "related": ["plumber", "hvac", "garage-door"]},
    {"slug": "garage-door", "path": "/garage-door-marketing.html", "name": "Garage door", "kind": "emergency", "img": "trade-garage-door.jpg",
     "alt": "A technician adjusts the spring and track of a residential garage door",
     "h1": "Door won’t open. The Google call hits your phone.",
     "lede": "Spring broke. Late for work. They Google “garage door won’t open” and tap Call. We run that ad. $249/mo. Ad spend extra.",
     "search": "garage door won’t open", "related": ["plumber", "hvac", "locksmith"]},
    {"slug": "roofer", "path": "/roofer-marketing.html", "name": "Roofing", "kind": "search", "img": "trade-roofer.jpg",
     "alt": "A roofer in a safety harness inspects shingles on a residential roof",
     "h1": "More booked jobs for roofing companies.",
     "lede": "If you do great work but your phone isn’t ringing consistently, you don’t need “more marketing.” You need to show up when someone in your area is ready to hire, and turn that click into a call.",
     "noun": "roofing companies", "related": ["tree-removal", "window-cleaning", "hvac"]},
    {"slug": "tree-removal", "path": "/tree-removal-marketing.html", "name": "Tree removal", "kind": "search", "img": "trade-tree-removal.jpg",
     "alt": "An arborist crew safely removes a large tree limb in a backyard",
     "h1": "More booked jobs for tree removal.",
     "lede": "If you do great work but your phone isn’t ringing consistently, you don’t need “more marketing.” You need to show up when someone in your area is ready to hire, and turn that click into a call.",
     "noun": "tree removal services", "related": ["roofer", "window-cleaning", "plumber"]},
    {"slug": "window-cleaning", "path": "/window-cleaners.html", "name": "Window cleaning", "kind": "search", "img": "trade-window-cleaning.jpg",
     "alt": "A window cleaner uses a squeegee on the large windows of a modern home",
     "h1": "Get more window cleaning jobs from Google searches.",
     "lede": "We help window cleaning businesses show up when people search “window cleaning near me”, and turn those high-intent searches into booked customers.",
     "noun": "window cleaning businesses", "related": ["roofer", "tree-removal", "garage-door"],
     "challenges": [
         ("Wasted ad spend", "Paying for clicks that don’t convert because ads target the wrong keywords or show to people not ready to book."),
         ("Missed local searches", "When someone searches “window cleaning near me” or “commercial window cleaning” in your city, your business doesn’t appear on the first page."),
         ("Manual lead follow-up", "Hours spent calling leads that go nowhere, instead of cleaning windows and growing the business."),
     ]},
]

SEARCH_PILLARS = [
    ("ads", "High-intent keywords", "We focus on searches from people who need the service now, not browsers."),
    ("web", "Call-first landing", "Fast, mobile-first pages designed to turn clicks into calls and form leads."),
    ("chart", "Clear tracking", "Call tracking and conversion tracking so you know what it costs to get a booked job."),
]
SEARCH_STEPS = [
    ("Campaign build and targeting", "Tight geo targeting, intent-based ad groups, negatives, and call-focused ads."),
    ("Landing page and lead capture", "A conversion-first page that makes it easy to call, request service, and trust you."),
    ("Call and conversion tracking", "Track calls, forms, and booked jobs, so we optimize toward profit, not vanity metrics."),
    ("Ongoing optimization", "Search terms, bids, ads, and landing page improvements, reviewed every week."),
]
SEARCH_FAQ = [
    ("How fast can I get leads?", "Most accounts can start generating calls within days of launch. Optimization improves costs over weeks."),
    ("Do you require a long-term contract?", "No. We keep it month-to-month and earn retention by performance and communication."),
    ("What’s the best budget to start?", "It depends on your service area and cost per click. On the strategy call, we’ll recommend a budget that can win."),
    ("Do you build the landing page?", "Yes. We can build a dedicated page for your trade and wire up tracking so results are measurable."),
]

HOME_SERVICES = {
    "h1": "When it’s an emergency, the Google call hits your phone.",
    "intro": "Call-only Google Ads for plumbers, HVAC, electricians, locksmiths and garage door companies, plus search campaigns and lead capture for roofing, tree removal and window cleaning.",
}

# ---------------------------------------------------------------- social / UGC

SOCIAL = {
    "h1": "Content that looks like the feed, not an ad.",
    "intro": "Real people. Real places. Short vertical video your customers actually stop for. We script it, shoot it, edit it, and post it, or hand it off ready to run as ads.",
    "why_h2": "People trust people.",
    "why_body": "Polished brand videos get skipped. A chef plating tonight’s special, a family’s Saturday out, a tech showing the fix: that reads like a friend’s post. It earns the watch, the follow, and the visit.",
    "why": [
        ("Native to the feed", "Vertical, fast, captioned, sound-on or off. Built for how Instagram actually plays."),
        ("Shows the real work", "Your team, your space, your work. Proof you can’t fake with stock footage."),
        ("Doubles as ad creative", "The same clips can run as paid ads on Instagram and Facebook, cut to length with hooks up front."),
        ("Keeps you top of mind", "When it’s time to book, order or call, they already know your name and face."),
    ],
    "formats": [
        ("ugc.jpg", "Mom filming a selfie video at an indoor family fun center while her kids run and jump behind her", "UGC video", "Creator-style testimonials, unboxings, walk-throughs and “day in the life” clips featuring your team or real customers."),
        ("reels.jpg", "Bartender pouring a cocktail while a phone on a small tripod films the pour", "Instagram Reels", "Hook in the first second, trending audio where it fits, on-screen captions, tight edits. 15–60 seconds."),
        ("carousel.jpg", "Overhead shot of tacos, a burger, salad and drinks shared on a restaurant table", "Carousels", "Swipeable tips, checklists and before/afters that get saved and shared: the posts that keep working."),
        ("stories.jpg", "Service crew chatting beside their van in early morning light", "Stories", "Behind-the-scenes, polls, Q&A stickers and offers. Quick, daily, and personal."),
    ],
    "steps": [
        ("Brief", "We learn your services, your area and your customers, then write hooks and scripts for the month."),
        ("Shoot", "On-site filming with your team, or creators who fit your audience. Phone-native, so it looks real."),
        ("Edit", "Cut into Reels, stories and carousels. Captions, pacing, cover frames and ad-ready versions."),
        ("Post", "Scheduled to your Instagram with captions and hashtags, plus files you own to reuse anywhere."),
    ],
    "get_h2": "A feed that stays full.",
    "get_body": "Monthly packages scale with how often you want to post. Every package includes the raw files. The content is yours.",
    "get": ["Monthly content calendar and hooks", "Scripted UGC and Reels shot on location", "Vertical edits with captions and covers",
            "Carousels and story sets from every shoot", "Ad-ready cuts for Instagram and Facebook", "Posting and scheduling on your account",
            "Raw and final files you own"],
    "faq": [
        ("Do I have to be on camera?", "No. We can feature your team, real customers, or creators we cast for you. Whoever fits the brand."),
        ("Can you post for us?", "Yes. We schedule and post to your Instagram, or deliver the files if your team prefers to post."),
        ("Can the videos run as ads?", "Yes. Every shoot includes ad-ready cuts sized for Instagram and Facebook placements."),
        ("Who owns the content?", "You do. You get the finals and the raw footage to use anywhere."),
    ],
}

# ---------------------------------------------------------------- insights (blog)

POSTS = [
    {"slug": "post-1", "path": "/blog/post-1.html", "category": "AI Automation", "date": "March 7, 2026", "read": "5 min read",
     "title": "How OpenClaw Will Streamline Business Automation in 2026",
     "excerpt": "What once required teams of specialists and hours of admin work can now run automatically. Here’s where AI automation saves the most time.",
     "img": "blog-automation.jpg", "alt": "Abstract glass blocks connected by glowing data lines"},
    {"slug": "post-2", "path": "/blog/post-2.html", "category": "Cost Optimization", "date": "March 7, 2026", "read": "6 min read",
     "title": "Stop Wasting Money: How AI Cut Ad Spend by 40% in 2026",
     "excerpt": "Poor targeting, the wrong hours and ignored data quietly drain ad budgets. How AI-driven optimization finds and stops the waste.",
     "img": "blog-adspend.jpg", "alt": "Abstract glass coins beside a gently descending line of light"},
]
