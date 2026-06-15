# CTO Compliance Work Plan — AFFG & Technijian

**Owner:** Ravi Jain (CTO) · **Created:** 2026-05-28 · **Scope:** the 31 document/policy tickets assigned to you (portal **#1459345–#1459375**, RoleType = CTO).

These are the tickets where the deliverable is a **policy, plan, procedure, or compliance document**. Hands-on technical/operational tickets (84) sit with Sai's IRV:TS1 pod and are out of scope here.

## How to use this document
- One entry per ticket. Each has: **Portal #**, priority/due, **Objective**, **Regulatory basis**, **What to produce** (the actual content), **Inputs needed**, **Dependencies**, **Definition of done (DoD)**, and **Est. hours**.
- **Log time** against the portal ticket # as you work each item.
- Phase deadlines (from today, 2026-05-28):
  - **Phase 1 (Critical):** by **2026-06-27** (0–30 days)
  - **Phase 2 (High):** by **2026-07-27** (30–60 days)
  - **Phase 3 (Medium):** by **2026-08-26** (60–90 days)

## Recommended execution order
1. **AFFG Criticals** — AFFG-001 → 002 → 003 → 017
2. **CMMC foundational** — CMMC-019 → 005 → 004 → 021 → 001 → 003 → 016
3. **AFFG High** — AFFG-004, 005, 006, 007, 008, 015
4. **AFFG Medium** — AFFG-009–014, 018, 019 → then **016 (capstone sign-off)**
5. **Standing** — AFFG-020; WISP-013, 014, 033; set **AFFG-021** recurring annual

## Sign-off gates & cross-dependencies
- **CMMC-001 (SSP) is the bottleneck for the DoD pipeline** — Sai's SPRS score (CMMC-002) and most tool-stack evidence cannot finish until the SSP exists.
- **Your AFFG documents gate Sai's AFFG recurring tests** (AFFG-022–029) — he cannot test/run a BCP that isn't written.
- **AFFG-016 (registered-principal approval) is the capstone** — sign only after AFFG-001 through AFFG-020 are drafted.
- Everything AFFG is **client-facing** — route through your review before anything goes to AFS.

---

# Part A — AFFG (American Fundstars Financial Group, LLC)

**Client profile:** dually-registered RIA / Broker-Dealer (SEC + FINRA). **Regulatory basis:** SEC Regulation S-P (2024 amendments), FINRA Rule 4370 (Business Continuity Plans), FINRA Rule 3110 (Supervision). Source: Technijian's *BCP Compliance Review* (20 findings + roadmap). Deliverables update AFFG's BCP / IRP / policy set.

### AFFG-001 — Incident Response Program  ·  #1459345  ·  CRITICAL (Phase 1)  ·  16h
- **Objective:** Give AFFG a written program to detect, respond to, and recover from unauthorized access to customer information (Reg S-P now mandates this).
- **What to produce:** A standalone Incident Response Plan (or integrated BCP section) containing: (1) **detection procedures** — monitoring sources and what constitutes an incident; (2) **containment protocols**; (3) **forensic investigation steps**; (4) an **escalation matrix** — roles, named contacts, timelines; (5) **evidence preservation**; (6) **eradication & recovery**; (7) **post-incident review**.
- **Inputs needed:** AFS systems/asset list, current monitoring/security tooling, key personnel + roles, after-hours contacts.
- **Dependencies:** Feeds AFFG-002 (breach notification) and AFFG-017 (cyber integration).
- **DoD:** Written IRP covering detection → recovery for customer-information incidents; your review complete; filed to the ticket.

### AFFG-002 — Customer Breach Notification Procedures  ·  #1459346  ·  CRITICAL (Phase 1)  ·  10h
- **Objective:** Procedure to notify affected individuals within **30 days** of determining sensitive customer info was (or is reasonably likely to have been) accessed without authorization.
- **What to produce:** (1) **criteria** for when notification is required (the "reasonably likely" standard); (2) the **30-day timeline** from determination; (3) **notification-letter content** — what was accessed, date/incident summary, steps taken, what the firm is doing, protective steps for the individual, contact info; (4) **scoping process** to identify affected individuals; (5) **template notification letters**.
- **Inputs needed:** AFS customer-data inventory; legal review of the letter template.
- **Dependencies:** Detection/escalation steps from AFFG-001.
- **DoD:** Documented procedure + at least one approved template letter.

### AFFG-003 — Service-Provider Oversight Framework  ·  #1459347  ·  CRITICAL (Phase 1)  ·  12h
- **Objective:** Written oversight of service providers so they protect customer info, including a **72-hour breach-notification** obligation from each provider.
- **What to produce:** A Service Provider Management section: (1) **due-diligence** procedure for vendor selection; (2) **contractual requirements** including 72-hour breach notification; (3) **ongoing monitoring** of provider security posture; (4) an **inventory** of all providers with access to customer information (start from AT&T, RingCentral, AWS, Microsoft 365, Synology).
- **Inputs needed:** AFS vendor list + contracts; which vendors touch customer data.
- **DoD:** Oversight framework + populated provider inventory + 72-hr clause language ready for contracts.

### AFFG-017 — Cybersecurity Incident Response Integration  ·  #1459361  ·  HIGH (Phase 1)  ·  12h
- **Objective:** Replace the vague two-bullet "Unauthorized Access" text with real cybersecurity controls and tie them to the IRP.
- **What to produce:** Expanded cybersecurity section (or reference the standalone Cyber IRP from AFFG-001) covering: intrusion detection/prevention, endpoint protection, MFA, network segmentation, forensic investigation, law-enforcement coordination, and cyber-insurance coverage.
- **Dependencies:** Reference AFFG-001 rather than re-writing the IR flow.
- **DoD:** Cybersecurity section that names concrete controls and links to the IRP.

### AFFG-004 — Reg S-P Recordkeeping  ·  #1459348  ·  HIGH (Phase 2)  ·  6h
- **Objective:** Records to evidence Reg S-P compliance, retained **5 years**.
- **What to produce:** Recordkeeping requirements specifying: record types (policies, incident reports, notifications, testing results), the 5-year retention period, storage location/format, and the designated custodian.
- **DoD:** Recordkeeping section adopted; custodian named.

### AFFG-005 — Data Backup & Recovery Specifications  ·  #1459349  ·  HIGH (Phase 2)  ·  10h
- **Objective:** Replace vague backup language with specifics (FINRA 4370(c)(1)).
- **What to produce:** Backup frequency/schedule, **RPO and RTO per data category**, encryption standards (at rest + in transit), geographic separation of backup sites, hard-copy document backup procedures, and a restoration-testing routine with documented results.
- **Inputs needed:** AFS's actual backup setup (Synology NAS, cloud), data categories.
- **Dependencies:** Sai's AFFG-024 (recurring restore test) executes against this spec.
- **DoD:** Backup section with concrete RPO/RTO, encryption, and test cadence.

### AFFG-006 — Mission-Critical Systems Inventory  ·  #1459350  ·  HIGH (Phase 2)  ·  12h
- **Objective:** Identify "mission-critical systems" per FINRA 4370(c)(2).
- **What to produce:** An inventory mapping each system → business function, owner, dependencies, RTO/RPO, and alternate processing. Must cover order management, trade execution, clearing/settlement, customer account access, and fund/securities delivery.
- **Inputs needed:** AFS application/system list and which carrying/clearing firms they use.
- **DoD:** Completed mission-critical systems inventory.

### AFFG-007 — Financial & Operational Assessment Procedures  ·  #1459351  ·  HIGH (Phase 2)  ·  8h
- **Objective:** Written procedures to assess operational/financial/credit-risk exposure after a disruption (FINRA 4370(c)(3)).
- **What to produce:** Procedures to assess the firm's ability to fund operations during disruption, evaluate changes to credit-risk exposure, determine ability to meet margin/capital requirements, and decision criteria for continuing vs. suspending operations.
- **DoD:** Assessment procedure section adopted.

### AFFG-008 — Customer Access to Funds & Securities  ·  #1459352  ·  HIGH (Phase 2)  ·  10h
- **Objective:** Ensure prompt customer access to funds/securities if the firm cannot continue (FINRA 4370(c)(10)).
- **What to produce:** Procedures for transferring/making accounts accessible, arrangements with carrying/clearing firms for direct access, timelines to restore access, and steps if the firm cannot continue (incl. **SIPC notification**).
- **Inputs needed:** AFS clearing/custody arrangements.
- **DoD:** Customer-access procedures, including the cannot-continue path.

### AFFG-015 — Supervisory Continuity  ·  #1459359  ·  HIGH (Phase 2)  ·  8h
- **Objective:** Maintain FINRA Rule 3110 supervision and WSPs during a disruption.
- **What to produce:** A Supervisory Continuity section: designation of alternate supervisory personnel, communications-review continuity, customer-account monitoring continuity, trade supervision at alternate locations, and documentation of supervisory activities during disruption.
- **DoD:** Supervisory-continuity section adopted.

### AFFG-009 — Alternate Communications: Customers  ·  #1459353  ·  MEDIUM (Phase 3)  ·  6h
- **Produce:** Specific alternate channels per disruption scenario (firm-only, building, district, city, regional): alternate phone numbers, backup email, website notifications, social media, written correspondence. **DoD:** Per-scenario customer comms plan.

### AFFG-010 — Alternate Communications: Employees  ·  #1459354  ·  MEDIUM (Phase 3)  ·  6h
- **Produce:** Mass-notification system, backup tools (SMS/messaging), out-of-band procedures, and a tested call tree with documented results. **DoD:** Expanded employee comms plan; tie test cadence to Sai's AFFG-025.

### AFFG-011 — Critical Business Constituent Impact  ·  #1459355  ·  MEDIUM (Phase 3)  ·  6h
- **Produce:** Identify clearing firms, custodians, banks, counterparties; procedures to notify them, maintain connectivity, access backup systems, and document impact assessments. **DoD:** Constituent list + impact procedures.

### AFFG-012 — Regulatory Reporting Continuity  ·  #1459356  ·  MEDIUM (Phase 3)  ·  5h
- **Produce:** List of all filings + deadlines (FOCUS, trade reporting, etc.), alternate submission methods, designated personnel, and extension-request procedures. **DoD:** Regulatory-reporting continuity section.

### AFFG-013 — BCP Customer Disclosure Statement  ·  #1459357  ·  MEDIUM (Phase 3)  ·  5h
- **Produce:** A BCP disclosure statement + procedures to provide at account opening, post on the website, mail on request, update on material change, addressing varying disruption scenarios (FINRA 4370(e)). **DoD:** Disclosure statement + distribution procedure. Ties to Sai's AFFG-028 (upkeep).

### AFFG-014 — FINRA Contact System Emergency Contacts  ·  #1459358  ·  MEDIUM (Phase 3)  ·  4h
- **Produce:** Procedures to register/maintain emergency contacts in the **FINRA Contact System (FCS)**, update promptly on material change, and review annually by the **17th business day after year-end** (FINRA 4370(f)). **DoD:** Documented FCS procedure. Ties to Sai's AFFG-022 (annual review).

### AFFG-018 — Customer Information Disposal  ·  #1459362  ·  MEDIUM (Phase 3)  ·  4h
- **Produce:** Disposal procedures (Reg S-P): secure wiping/degaussing of electronic records, cross-cut shredding of hard copy, disposal documentation, and third-party disposal-vendor oversight. **DoD:** Disposal procedure section.

### AFFG-019 — Comprehensive BCP Refresh & Currency  ·  #1459363  ·  MEDIUM (Phase 3)  ·  8h
- **Produce:** Verify all personnel/contacts/titles are current; update technology references (the doc is dated Oct 2023); document the annual review (date + reviewer); implement version control. **DoD:** Refreshed, current BCP with a change log.

### AFFG-016 — Registered-Principal Approval & Version Control  ·  #1459360  ·  MEDIUM (Phase 3 — CAPSTONE)  ·  3h
- **Objective:** Provide the FINRA 4370(b) registered-principal approval the plan currently lacks.
- **Produce:** Formal approval section — registered-principal signature block, approval date, annual-review certification, version-control/change log.
- **Dependencies:** **Do LAST** — this is your sign-off after AFFG-001–020 are drafted.
- **DoD:** Approved, signed, version-controlled BCP.

### AFFG-020 — Alternate Site Capabilities  ·  #1459364  ·  LOW  ·  4h
- **Produce:** Document the alternate site (84 Spacial, Irvine) — available infrastructure (desks, connectivity, phones), capacity, pre-arranged agreements, activation time, readiness testing. **DoD:** Alternate-site detail section.

### AFFG-021 — Annual BCP Review & Principal Approval  ·  #1459365  ·  RECURRING (Annual)  ·  8h
- **Objective:** Yearly FINRA 4370(b) review/update + your principal approval.
- **Action:** **Set this up as a recurring annual ticket.** Validate RTO/RPO, recovery strategies, contacts, technology; document reviewer + date; update the version log.
- **DoD:** Recurring ticket configured; first annual review scheduled.

---

# Part B — Technijian (CMMC readiness + governance)

**Context:** Technijian's own NIST 800-171 / CMMC Level 2 readiness and governance documents. These unblock the DoD/Electrocute prospect. **Posture invariant:** Technijian does not store/process/transmit CUI on its own systems; only encrypted ciphertext backups (client-held keys) reach Technijian.

### CMMC-019 — CMMC Scope Position Statement  ·  #1459371  ·  6h  ·  *do early*
- **Objective:** Lock the architectural invariant every client design must preserve.
- **Produce:** A short, approved statement: Technijian does not store/process/transmit CUI on its own systems; only encrypted backup ciphertext (client holds the key) reaches the Technijian DC; Technijian cannot decrypt. This sentence governs the rest.
- **DoD:** Signed scope-position statement; referenced by the SSP (CMMC-001) and CRM (CMMC-004).

### CMMC-005 — CUI Data Category & Handling Procedures  ·  #1459369  ·  12h
- **Objective:** Add CUI/FCI to the WISP and define handling.
- **Produce:** WISP §5.1 addendum adding **CUI** and **FCI** categories; document CUI identification, marking, labeling, storage, transmission, media handling/transport, and destruction (NIST 800-171 MP family).
- **Dependencies:** Feeds the SSP (CMMC-001); training delivery is Sai's CMMC-017.
- **DoD:** Approved WISP addendum.

### CMMC-004 — Customer Responsibility Matrix (template)  ·  #1459368  ·  16h
- **Objective:** The core ESP artifact — who does which control.
- **Produce:** A reusable matrix mapping each applicable NIST 800-171 control → **Technijian / Client / Shared**, with an implementation note per control.
- **Dependencies:** Extended by CMMC-021.
- **DoD:** Reusable CRM template.

### CMMC-021 — CRM to 320 L2 Assessment Objectives  ·  #1459372  ·  20h
- **Objective:** Take the CRM to assessment-objective depth.
- **Produce:** Extend CMMC-004 from the 110 controls to all **320 Level 2 assessment objectives**; mark each Client/Technijian/Shared with a note; avoid vague "Technijian handles security."
- **Dependencies:** Requires CMMC-004 first.
- **DoD:** Objective-level CRM ready to drop into a client SSP.

### CMMC-001 — NIST 800-171 System Security Plan (SSP)  ·  #1459366  ·  32h  ·  *keystone*
- **Objective:** The authoritative document of how Technijian meets all **110** NIST 800-171 Rev 2 requirements.
- **Produce:** Map each control to existing WISP/IRP/BCP procedures + technical config; define the **system boundary**; describe **network and data flows**; identify **inherited controls** (TPX data center SOC 2, Microsoft 365).
- **Dependencies:** Use CMMC-019 (scope) + CMMC-005 (CUI) + CMMC-004 (CRM) as inputs. **Gates Sai's CMMC-002 (SPRS) and CMMC-003 (POA&M).**
- **DoD:** SSP covering all 110 controls, ready for assessor/client review.

### CMMC-003 — POA&M  ·  #1459367  ·  12h
- **Objective:** Track every not-yet-met requirement to closure.
- **Produce:** For each gap from the SSP: deficiency, planned remediation, owner, milestone dates, compensating controls. Review monthly.
- **Dependencies:** Built from the CMMC-001 SSP gap list.
- **DoD:** POA&M covering all open gaps; review cadence set.

### CMMC-016 — DoD-Client MSA/SOW Addendum  ·  #1459370  ·  8h
- **Objective:** Contract language for serving DoD-adjacent clients.
- **Produce:** Addendum covering: agreement to be named in the client SSP, willingness to be assessed as a **Security Protection Asset**, **DFARS 252.204-7012/7021** flow-down acceptance, CUI handling terms, and a reference to the CRM.
- **Inputs/dep:** Route through legal review before use.
- **DoD:** Legal-reviewed addendum template.

### WISP-013 — Privacy Impact Assessment (PIA) Process  ·  #1459373  ·  8h
- **Produce:** A PIA template + process; triggers (new systems, new vendors, new PII/PHI engagements); Security Officer as reviewer; initial PIAs for current processing; store in the controlled-document repository. **DoD:** Template + process + initial PIAs filed.

### WISP-014 — Change Management Process  ·  #1459374  ·  12h
- **Produce:** A formal change-management process in the ticketing system; change-request templates (description, justification, risk classification, affected systems, rollback plan, testing, approvals); Standard / Normal / Emergency workflows; train IT staff. **DoD:** Documented process + templates + staff trained.

### WISP-033 — BAA Inventory & Tracking Process  ·  #1459375  ·  6h
- **Produce:** A register of active Business Associate Agreements (client, execution date, scope, PHI types, renewal/expiry); annual review; downstream BAAs with subcontractors; BAA termination + PHI-destruction procedures. **DoD:** BAA register + tracking process.

---

## Appendix — Ticket # ↔ ref map (your 31)

| Ref | Portal # | Ref | Portal # |
|---|---|---|---|
| AFFG-001 | 1459345 | AFFG-017 | 1459361 |
| AFFG-002 | 1459346 | AFFG-018 | 1459362 |
| AFFG-003 | 1459347 | AFFG-019 | 1459363 |
| AFFG-004 | 1459348 | AFFG-020 | 1459364 |
| AFFG-005 | 1459349 | AFFG-021 | 1459365 |
| AFFG-006 | 1459350 | CMMC-001 | 1459366 |
| AFFG-007 | 1459351 | CMMC-003 | 1459367 |
| AFFG-008 | 1459352 | CMMC-004 | 1459368 |
| AFFG-009 | 1459353 | CMMC-005 | 1459369 |
| AFFG-010 | 1459354 | CMMC-016 | 1459370 |
| AFFG-011 | 1459355 | CMMC-019 | 1459371 |
| AFFG-012 | 1459356 | CMMC-021 | 1459372 |
| AFFG-013 | 1459357 | WISP-013 | 1459373 |
| AFFG-014 | 1459358 | WISP-014 | 1459374 |
| AFFG-015 | 1459359 | WISP-033 | 1459375 |
| AFFG-016 | 1459360 | | |

**Totals:** AFFG 21 tickets (~163h) · Technijian 10 tickets (~132h) · **31 tickets, ~295h.**
