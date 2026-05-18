# session_log.md — Local Digital Caretaker

## CURRENT STATE
Two preview demo sites are live on GitHub Pages:
- **South Coast Aquatics:** https://belletiennetrades.github.io/bell-etienne/southcoast/
- **Marc Wilmers Heating & Air:** https://belletiennetrades.github.io/bell-etienne/marcwilmers/

Both are ready to share with their respective prospects. Sales outreach to MEP Air and other North Hills prospects is still pending.

## PICK UP HERE
1. **Share Demos:**
   - Send South Coast preview to Matt Warshaw (matt@southcoastaquatics.com, (805) 660-2082).
   - Send Marc Wilmers preview to (818) 517-6010 — Marc himself usually answers.
2. **Sales Outreach:** Send the first real "Technical Leak" email to MEP Air (Manuel Ortega).
3. **Onboarding:** Draft the "Local Maintenance Proposal" template.
4. **Protocol Work (see Open Questions):** Formalize Discovery → Build → Deploy. Defer go-live protocol until first paying customer.

## OPEN QUESTIONS / PROTOCOLS TO DEFINE
- **Prospect Demo Protocol (Discovery → Build → Deploy):** Both South Coast and Marc Wilmers were built ad-hoc this week. The shape is starting to repeat — research the prospect (Yelp/Google for owner, phone, services, reviews), build a preview at `/<slug>/index.html` modeled on the established template (inline-SVG logo, top preview ribbon, tap-to-call, full sections, Bell-Etienne footer stamp), add `!<slug>/` to `.gitignore` allowlist, commit & push. Worth writing this up as a checklist before the next 2-3 demos so it's repeatable instead of remembered.
- **Go-Live Protocol:** Deferred until we have paying customers. Will cover: domain transfer/registration, DNS, SSL, redirect from old site, email/contact form wiring, analytics, ownership handoff, recurring caretaker setup. Not worth designing in the abstract — first real customer will define the real shape.

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
