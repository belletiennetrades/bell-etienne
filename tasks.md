# Bell-Etienne Task Tracker

## 🌐 Website & Deployment (Current Focus)
- [x] Create initial `index.html`
- [x] Setup local Git repository
- [x] Create GitHub account `belletiennetrades`
- [x] Link local repo and push to GitHub
- [x] **Fix GitHub Pages 404:** Enable "Pages" in GitHub Settings (Branch: `main`, Folder: `/root`)
- [x] Verify live site at `https://belletiennetrades.github.io/bell-etienne/`
- [x] **South Coast Demo:** Refine demo at `/southcoast/index.html` (Fix logo, condense Handyman section) — rebuilt as full preview site, deployed
- [x] Initial staging of South Coast demo at `/southcoast/index.html`
- [x] **Marc Wilmers Demo:** Build full preview at `/marcwilmers/index.html` and deploy to GitHub Pages
- [x] **RJ's Work Boots Demo:** Build full preview at `/rjsworkboots/index.html` and deploy to GitHub Pages
- [x] **Portfolio on main site:** Promote a "Live Demos" + "Ready Templates" strip to the top of `index.html` as five contrasting dark tile-cards
- [x] **Handyman template:** Build cookie-cutter `/templates/handyman/index.html` with neutral wordmark and `TEMPLATE:` swap markers
- [x] **Mobile Detailer template:** Build cookie-cutter `/templates/detailer/index.html` with neutral wordmark, including car photos across 4 categories (JDM, muscle, family SUV, work truck)
- [x] **Wilmers visual differentiation rebuild:** Convert `/marcwilmers/index.html` to a photo-led editorial magazine layout (Fraunces serif, full-bleed Unsplash photos, scrolling trust marquee, photo-backed pull-quote)
- [ ] Share live demo with Matt Warshaw / South Coast Aquatics for feedback
- [ ] Share live demo with Marc Wilmers — (818) 517-6010
- [ ] Share live demo with RJ's Work Boots — (661) 259-1978
- [ ] Enhance UI/UX (Refine typography, mobile links, subtle accents)
- [ ] Visually differentiate `southcoast` and `rjsworkboots` against the new Wilmers editorial style if needed (both still use Playfair display)

## 📋 Protocols (To Formalize)
- [ ] **Prospect Demo Protocol (Discovery → Build → Deploy):** Write a repeatable checklist now that we have three demos under our belt — research inputs needed, template anchor file, palette/copy decisions, `.gitignore` allowlist step, commit/push steps, sharing message format.
- [ ] **Go-Live Protocol:** Defer until first paying customer. Will cover domain handoff, DNS/SSL, redirects, contact form wiring, analytics, ownership transfer, recurring caretaker setup.

## 📞 Sales & Outreach
- [x] Research 10 local prospects in North Hills
- [x] Perform micro-audits and write custom pitch scripts
- [x] Create `sales_call_list.md`
- [x] Create `sales_tracker.md` to log call outcomes
- [x] Draft "Digital Handyman" cold email template
- [x] Send first cold email test to Chris Bell & liegev@gmail.com
- [x] **Compile SFV "no website" prospect list (50 leads):** 25 mobile detailers + 25 handymen with active Yelp listings but no discoverable website. Saved to `prospects_no_website.md` (master) plus `prospects_no_website_detailers.md` and `prospects_no_website_handymen.md` (detail + rejects + bench).
- [ ] **📌 PINNED: Email the 50-prospect list** to charles@olinthus.com + Chris (trickstand@gmail.com). Subject: "SFV prospects — 50 detailers + handymen with no website". Sender: belletienne.trades@gmail.com via `send_email.py`. **Blocker:** Gmail app password not stored anywhere accessible (not in env, settings, project files, or recoverable transcripts). On resume: either Charles pastes the app password, OR build a `send_prospects.py` wrapper that reads body from the markdown file and password from a `BELL_PW` env var so Charles can run it himself with `! BELL_PW='...' python3 ...`.
- [ ] Spot-check phone numbers on flagged prospect rows before mass outreach (detailers #15, #16, #22; out-of-state area codes: detailers #11/504, handymen #38/267, #47/412)
- [ ] Send first real cold email to a prospect (e.g., MEP Air Incorporation)
- [ ] Conduct first batch of 10 calls/visits
- [ ] Draft "Local Maintenance Proposal" template for "YES" responses

## ⚙️ Backend & Automation
- [x] Set up Gmail App Passwords for `belletienne.trades@gmail.com`
- [x] Setup email automation for micro-audit delivery (`send_email.py`)

## ✅ Completed Milestones
- [x] Project Identity & Branding: Bell-Etienne "Digital Handyman"
- [x] Business Plan & Tier Pricing defined
- [x] Local Research & Audit phase finished
