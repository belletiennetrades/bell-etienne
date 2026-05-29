# session_log.md — Local Digital Caretaker

## CURRENT STATE
Three preview demo sites + two reusable templates are live on GitHub Pages, and the main site now opens with a portfolio strip linking all five:
- **Main site (portfolio on top):** https://belletiennetrades.github.io/bell-etienne/
- **South Coast Aquatics:** https://belletiennetrades.github.io/bell-etienne/southcoast/
- **Marc Wilmers Heating & Air (photo-led editorial):** https://belletiennetrades.github.io/bell-etienne/marcwilmers/
- **RJ's Work Boots:** https://belletiennetrades.github.io/bell-etienne/rjsworkboots/
- **Handyman template:** https://belletiennetrades.github.io/bell-etienne/templates/handyman/
- **Mobile Detailer template:** https://belletiennetrades.github.io/bell-etienne/templates/detailer/

All three demos are ready to share with their respective prospects. Templates are ready to be rebranded for cold prospects in ~5 minutes via `TEMPLATE:` swap markers. Outreach pipeline still has a fresh 50-lead SFV "no-website" prospect list ready to mail to Charles + Chris — paused at the send step because the Gmail app password is not recoverable from current context.

## PICK UP HERE
1. **📌 PINNED: Send 50-prospect SFV list** to charles@olinthus.com + trickstand@gmail.com (Chris). Subject already chosen: "SFV prospects — 50 detailers + handymen with no website". Body = full contents of `prospects_no_website.md`. Sender = belletienne.trades@gmail.com. Two paths to unblock:
   - **A:** Charles pastes the Gmail app password in chat → I run `send_email.py` directly.
   - **B (recommended):** I write `send_prospects.py` (reads body from the markdown, reads pw from `BELL_PW` env var); Charles runs it with `! BELL_PW='…' python3 send_prospects.py` so the password never enters Claude's context.
2. **Share Demos:**
   - Send South Coast preview to Matt Warshaw (matt@southcoastaquatics.com, (805) 660-2082).
   - Send Marc Wilmers preview to (818) 517-6010 — Marc himself usually answers.
   - Send RJ's Work Boots preview to (661) 259-1978 — Ryan or Joseph.
3. **Sales Outreach:** Send the first real "Technical Leak" email to MEP Air (Manuel Ortega).
4. **Onboarding:** Draft the "Local Maintenance Proposal" template.
5. **Protocol Work (see Open Questions):** Formalize Discovery → Build → Deploy. Defer go-live protocol until first paying customer.

## OPEN QUESTIONS / PROTOCOLS TO DEFINE
- **Prospect Demo Protocol (Discovery → Build → Deploy):** Both South Coast and Marc Wilmers were built ad-hoc this week. The shape is starting to repeat — research the prospect (Yelp/Google for owner, phone, services, reviews), build a preview at `/<slug>/index.html` modeled on the established template (inline-SVG logo, top preview ribbon, tap-to-call, full sections, Bell-Etienne footer stamp), add `!<slug>/` to `.gitignore` allowlist, commit & push. Worth writing this up as a checklist before the next 2-3 demos so it's repeatable instead of remembered.
- **Go-Live Protocol:** Deferred until we have paying customers. Will cover: domain transfer/registration, DNS, SSL, redirect from old site, email/contact form wiring, analytics, ownership handoff, recurring caretaker setup. Not worth designing in the abstract — first real customer will define the real shape.

### Session 8 — 2026-05-28 → 2026-05-29
- **Portfolio on main site (top):** Added "Live Demos" and "Ready Templates" sections to the top of `index.html` as five dark contrasting tile-cards. Iteration: initially placed mid-page, then user asked to move to top and use contrasting boxes that pop. Final layout = two grouped lists (3 demos + 2 templates), gold-accent hover arrows.
- **Two reusable templates built:** `/templates/handyman/index.html` and `/templates/detailer/index.html`. Both ship with neutral typographic wordmarks ("HANDYMAN CO.", "DETAIL CO.") — see [[feedback-template-branding]] in memory for the rationale (Option C of the partner's three-option logo question). Handyman: navy + safety-orange, 8 services, before/after gallery, booking + payment CTAs, service area, contact form, licensed/insured/bonded badge strip. Detailer: jet-black + electric cyan, 3 pricing tiers, before/after gallery (later swapped for car photos), booking + payment, 8 add-ons, service area, contact form with vehicle/package fields. Every swap point marked `<!-- TEMPLATE:* -->` for fast rebrand (~5 min per site).
- **Wilmers HVAC redesigned as photo-led editorial:** User said the three demos felt too similar and asked for a "super different" look. Replaced the grid-and-icon layout with a magazine-style design — full-bleed Unsplash hero photo (AC unit), Fraunces serif display type, scrolling trust marquee, photo-on-left meet-Marc split, six photo-led service cards, full-bleed italic pull-quote over a dimmed interior photo, slate stats band with italic serif numerals, 4-step process with sticky thermostat photo, photo-backed service-area map, big tap-to-call final CTA over a dimmed AC photo. Palette (slate-navy + ember) preserved; cream paper background gives the editorial vibe. See [[feedback-demo-variety]] in memory for the differentiation pattern.
- **Detailer template photo update:** Added Unsplash photos covering four car categories the user named — JDM tuner, classic Camaro, family SUV, work truck. Hero swapped to a dark parking-garage car photo. Gallery uses the same photo on both before/after halves with CSS filters dimming the "before" side, so a real prospect rebrand needs only one URL swap per pair, not two.
- **Photo sourcing workflow established:** WebFetch Unsplash search pages → extract `https://images.unsplash.com/photo-<id>` URLs → verify each with `curl -s -o /dev/null -w "%{http_code}"` before committing. 18 photos verified across this session, zero broken links shipped.
- **Memory:** Wrote two feedback memories — [[feedback-demo-variety]] (visual differentiation via photo-led layouts + per-demo font swaps) and [[feedback-template-branding]] (neutral wordmark approach, Option C of the partner's question).
- **Outreach pipeline:** No change — 50-prospect email still blocked on Gmail app password; three demo-share tasks for South Coast, Marc Wilmers, and RJ's still pending.

### Session 7 — 2026-05-22
- **RJ's Work Boots Demo Live:** Reviewed previously-built `rjsworkboots/index.html` (1651 lines, leather/brass/oxblood palette, Santa Clarita specialty boot shop — 27 brands, expert fitting). `.gitignore` was already allowlisted for the directory from a prior session. Committed (`6463004`), pushed to main, polled GitHub Pages until live (HTTP 200 on 3rd attempt). Now live at https://belletiennetrades.github.io/bell-etienne/rjsworkboots/.
- **Demo count:** 3 (southcoast, marcwilmers, rjsworkboots). Protocol-formalization task in Open Questions now overdue — every demo so far has reused the same shape (preview ribbon, inline SVG logo, custom palette, tap-to-call, Bell-Etienne footer stamp).
- **Outreach pipeline:** No change — 50-prospect email still blocked on Gmail app password, both share-the-demo tasks for South Coast and Marc Wilmers still pending.

### Session 6 — 2026-05-18 → 2026-05-19 (Late evening)
- **New Prospect List:** Compiled 50 SFV businesses with active Yelp listings but no discoverable website — 25 mobile detailers + 25 handymen. Two parallel research agents (general-purpose) each verified their 25; Yelp profile pages return HTTP 403 to fetchers, so verification was Google-search-based (reject if a proprietary `.com`/`.us`/`.co`/Square/Webflow surfaces). Bench rows and rejected-with-reason lists included.
  - **Master:** `prospects_no_website.md` (50-row table, "strongest cold-call tier" callout, suggested pitch angle — opposite of the Caretaker pitch: "Yelp owns your leads, take them back").
  - **Detail:** `prospects_no_website_detailers.md` (25 + 2 bonus + 17 rejects), `prospects_no_website_handymen.md` (25 + 10 bench + 22 rejects).
  - **Caveats logged in each file:** phone numbers came from Google snippets not live Yelp pages (spot-check rows flagged); ~1-in-15 may turn out to have an obscure site missed; out-of-state area codes on detailer #11 (504), handyman #38 (267), #47 (412) need verification.
- **Email Send (PAUSED):** Confirmed recipients (charles@olinthus.com + trickstand@gmail.com / Chris) and subject line. Search for the Gmail app password came up empty across env vars, `.claude/settings.local.json`, project files, and the recoverable jsonl transcripts in `~/.claude/projects/-home-charles-agents-bell-n-etienne/`. Session paused before send — see PICK UP HERE #1.
- **Memory:** No new memory written this session (prospect-list workflow may be worth a memory next time it's repeated).

### Session 5 — 2026-05-18 (Afternoon)
- **New Lead:** Marc Wilmers Heating & Air (Valencia/Santa Clarita) — sourced from Yelp (5.0★, 211 reviews, top 4% CA contractors per BuildZoom).
- **Demo Build:** Built full preview at `/marcwilmers/index.html` — slate-navy + ember-orange "heating + cooling" palette (distinct from southcoast's aquatic blue), inline SVG flame+snowflake logo, 6-service grid (AC install, furnace, repairs, multi-zone, maintenance, rental/property), about-Marc block with trust badges, 5-star Yelp summary + 3 testimonial cards, SCV service-area strip with 8 cities + ZIPs, tap-to-call (818) 517-6010 throughout, top ribbon + footer stamp for Bell-Etienne preview attribution.
- **Deployment:** Updated `.gitignore` allowlist to include `marcwilmers/`, committed (`28d25b3`), pushed to main, live at https://belletiennetrades.github.io/bell-etienne/marcwilmers/.
- **Process Note:** Two demos in, the Discovery → Build → Deploy flow is repeating itself. Flagged in Open Questions to formalize next session before the 3rd demo.

### Session 4 — 2026-05-18 (Late evening)
- **South Coast Rebuild:** Replaced the staged demo with a full, polished preview at `/southcoast/index.html` — inline SVG logo (no hotlink risk), preview ribbon replaces the tacked-on "Digital Handyman Upgrades" section, programs grid, mission/quote block, coaches strip, contact card with real phone/email/address, and full footer with social links.
- **Design:** Inter + Playfair Display pairing, navy/blue/aqua/gold palette, mobile-first responsive, tap-to-call and SMS links throughout.
- **Deployment:** Pushed (`c9c848f`) and confirmed live (HTTP 200) at https://belletiennetrades.github.io/bell-etienne/southcoast/.

### Session 3 — 2026-05-18 (Evening)
- **GitHub Deployment:** Moved from Surge.sh to GitHub Pages: [https://belletiennetrades.github.io/bell-etienne/](https://belletiennetrades.github.io/bell-etienne/).
- **UI/UX Enhancement:** Refined typography, added "Trade Gold" accent color, and implemented functional `tel:` and `sms:` links for mobile users.
- **Task Management:** Consolidated all project action items into a centralized `tasks.md`.
- **Email Automation:** Developed `send_email.py` Python script for CLI-based outreach.
- **Sales Strategy:** Drafted the "Technical Leak" cold email template and initialized `sales_tracker.md`.
- **Progress Reporting:** Delivered a comprehensive project status report to stakeholders via the new automation system.
- **Email Warm-up:** Successfully sent test emails to multiple personal domains to establish sender reputation.
- **Staging Demo:** Created and staged a high-performance home page clone for `southcoastaquatics.com` at `/southcoast/index.html`.
- **SSH Configuration:** Set up a dedicated SSH key for the `belletiennetrades` GitHub account on the headless machine.

### Session 2 — 2026-05-18 (Morning)
- **Branding:** Renamed the project to **Bell-Etienne**.
- **Strategy Shift:** Adopted the **"Digital Handyman"** persona, framing web maintenance as the "digital equivalent of plumbing" for tradespeople.
- **Website Creation:** Designed and built a minimalist, responsive one-page website (`index.html`).
- **Deployment:** Deployed initial version to Surge.sh (later moved to GitHub).
- **Identity Setup:** Created dedicated business Gmail and GitHub accounts.

### Session 1 — 2026-05-17
- Analyzed business plan and initialized memory system.
- Targeted North Hills, CA for initial research.
- Identified 10 prospects and created `sales_call_list.md`.
