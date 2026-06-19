# Technijian, Inc.

# CMMC Client Onboarding and Scoping Procedure

**Document ID:** TJN-CMMC-101
**Owner:** Technijian Corporation (Information Security)
**Classification:** Internal — provided to clients and assessors under NDA
**Status:** DRAFT for principal approval
**Version:** 0.1 (2026-06-19)
**Related:** CMMC-100 (Client-Support Program); CMMC-019 (CUI Scope); CMMC-005 (CUI/FCI Handling); CMMC-004 (CRM); CMMC-001 (SSP template); CMMC-003 (POA&M template)

---

## 1. Purpose & scope

### 1.1 Purpose

This procedure is the **authoritative, step-by-step playbook** Technijian follows to onboard a new Defense Industrial Base (DIB) client that must meet **CMMC 2.0 Level 2 / NIST SP 800-171 Rev 2**. It defines, in order, the work Technijian performs from the first scoping call through steady-state governance, and it fixes the boundaries of Technijian's role so that every downstream artifact (SSP, CRM, POA&M, evidence) is built on the same scoping assumptions.

### 1.2 Technijian's role — read this first

> **Technijian is a Managed Service Provider (MSP) / External Service Provider (ESP). Technijian is NOT itself CMMC-certified.** Technijian helps the client achieve and sustain CMMC 2.0 Level 2 / NIST SP 800-171 Rev 2 compliance; the **certification (or self-assessment affirmation) belongs to the client / Organization Seeking Certification (OSC)**, not to Technijian.

The single most important architectural fact governing this onboarding, and the basis for the scope position in [[CMMC-019]]:

> Technijian holds only **encrypted backup ciphertext**. The **client holds the encryption keys**. Technijian **cannot decrypt** client data, and any **restore returns ciphertext** to the client for decryption inside the client's own boundary. Technijian therefore does not store, process, or transmit CUI in usable form on Technijian-operated systems.

Encryption is **FIPS 140-2/3 validated and performed client-side** before data leaves the client boundary. Ciphertext is stored **ciphertext-only at rest** on Technijian-operated QNAP / Nimbus storage in the **TPX data center, Irvine, CA**. Technijian relies on the **TPx SOC 2 Type II report** (`../tpx-dc/`) for physical and environmental controls of that facility.

A dedicated, **segregated CMMC management plane** is stood up for each DIB client — separate remote-support session groups, a separate RMM/ITSM instance, and dedicated cloud admin groups — so that CMMC client management is isolated from Technijian's general MSP fleet.

### 1.3 Scope of this procedure

| In scope | Out of scope |
|---|---|
| Scoping, boundary definition, ESP role confirmation | Performing the client's C3PAO assessment (the assessor does this) |
| Standing up FIPS-validated, client-keyed encrypted backup | Custody, escrow, or recovery of the client's encryption keys |
| Standing up the segregated CMMC management plane | Implementing controls inside the client's own CUI enclave that Technijian does not operate |
| Delivering and helping populate SSP / CRM / POA&M | Issuing a CMMC certificate or self-assessment affirmation (client owns these) |
| Evidence-collection setup and ongoing review cadence | Legal interpretation of the client's DoD contracts (client counsel owns this) |

---

## 2. Roles & responsibilities

| Role | Party | Responsibility in onboarding |
|---|---|---|
| Technijian Security Officer / vCISO | Technijian | Owns this procedure end-to-end; runs the scoping call; signs off the boundary, key-custody, and ESP-role determination; reviews assessor questions |
| Technijian Account Team / Project Lead | Technijian | Coordinates schedule, contracts, and deliverable handoffs; tracks the onboarding checklist to completion |
| Technijian Backup / Infrastructure Engineer | Technijian | Configures NAKIVO client-side encryption, the QNAP/Nimbus ciphertext store, and the segregated management plane; runs the no-decrypt and restore tests |
| Client ISSO / Information Security POC | Client | Owns the client's CMMC program and affirmation; generates and retains encryption keys; populates client-owned SSP/CRM/POA&M items; supplies DoD contract context |
| Client Executive Sponsor | Client | Approves scope, signs the MSA/SOW addendum and NDA, accepts residual risk |
| Client C3PAO / Assessor | Third party | Performs the Level 2 assessment; makes the final asset-categorization and scoping determination [VERIFY per engagement] |

> Names and titles are engagement-specific and recorded in the per-client onboarding record, not in this template. [VERIFY]

---

## 3. Step 1 — Initial scoping call

**Goal:** Establish what the client must comply with, why, and on what timeline, so the rest of the onboarding is correctly sized.

### 3.1 Confirm the data types in play

Determine whether the client handles **FCI (Federal Contract Information)**, **CUI (Controlled Unclassified Information)**, or both:

- **FCI only** → CMMC Level 1 obligations may apply (FAR 52.204-21). Confirm whether the client also has CUI; if not, Level 2 scoping below is reduced accordingly. [VERIFY]
- **CUI present** → CMMC 2.0 Level 2 / NIST SP 800-171 Rev 2 applies. Proceed with full Level 2 scoping.

### 3.2 Identify the contractual / regulatory drivers

Capture, from the client and their counsel:

- The DoD contracts or subcontracts that impose the requirement, and the **DFARS 252.204-7012** ("Safeguarding Covered Defense Information and Cyber Incident Reporting") clause and any **DFARS 252.204-7019/7020/7021** flow-downs.
- The associated **72-hour DoD cyber-incident reporting** obligation (carried into Step 8).
- Any prime-contractor flow-down requirements the client must satisfy.

### 3.3 Confirm the assessment target

| Target | Meaning | Typical trigger |
|---|---|---|
| **Level 2 Self-Assessment** | Client self-assesses against 800-171 Rev 2 and affirms in SPRS | Lower-criticality CUI, contract permits self-assessment [VERIFY] |
| **Level 2 C3PAO Certification** | Independent C3PAO assessment | Higher-criticality CUI / contract requires certification [VERIFY] |

### 3.4 Establish the timeline

Record target dates for: boundary sign-off, backup cutover, management-plane go-live, SSP/CRM/POA&M draft, evidence baseline, and the client's assessment/affirmation date. Tie these to the onboarding checklist in Section 12.

**Output of Step 1:** a short scoping memo (data types, drivers, target, timeline, named POCs) filed in the client onboarding record and used to confirm contract scope in [[CMMC-016]].

---

## 4. Step 2 — Define the CUI / FCI boundary

**Goal:** Draw the line around where CUI/FCI lives, and document — on paper and in a diagram — that Technijian's systems sit **outside** the CUI processing boundary because they hold ciphertext only.

### 4.1 Inventory the data and where it lives

With the client ISSO, list:

1. **What** CUI/FCI the client handles (categories, e.g. CDI, technical data) — at a category level only; Technijian does not need the data itself.
2. **Where** it is created, stored, processed, and transmitted inside the client environment (endpoints, file shares, M365/GCC, line-of-business apps, the client's CUI enclave).
3. **Which** of those systems are **CUI Assets**, **Security Protection Assets (SPA)**, **Contractor Risk-Managed Assets (CRMA)**, or **Out-of-Scope** per the CMMC Level 2 Scoping Guide. [VERIFY with assessor]

### 4.2 Confirm and document Technijian's ESP role

Technijian's role is **backup and security only**. State explicitly, consistent with [[CMMC-019]]:

- The only client data reaching Technijian-operated infrastructure is **encrypted backup ciphertext**.
- The **client retains sole custody of the encryption keys**; Technijian has **no access to the means of decryption**.
- Technijian-operated storage is therefore categorized as a **Security Protection Asset / Contractor Risk-Managed Asset**, **not** a CUI Asset — subject to assessor confirmation.

### 4.3 Produce the data-flow + key-custody diagram

Create a diagram for inclusion in the client's **SSP** and **CRM** that shows:

- Client CUI enclave → **client-side FIPS-validated encryption** → ciphertext over TLS 1.2+ → **QNAP/Nimbus ciphertext store in TPX Irvine** → restore path returning **ciphertext** to the client.
- A clear **key-custody boundary**: keys never leave the client; no Technijian process, account, or tool can decrypt.

Diagram production and content standards are defined in **CMMC-024**; reference that document for the diagram template and required elements.

**Output of Step 2:** boundary narrative + data-flow/key-custody diagram (per CMMC-024), reviewed by the Technijian vCISO and the client ISSO, ready to drop into the SSP and CRM.

---

## 5. Step 3 — Stand up FIPS-validated, client-keyed encrypted backup

**Goal:** Bring the encrypted backup service online so that Technijian provably **cannot** read client data, and prove it with a no-decrypt check and a client-keyed restore test.

### 5.1 Configure source-side encryption (client-keyed)

- Configure **NAKIVO source-side / network encryption** so data is encrypted **at the client boundary before transmission**, using a **FIPS 140-2/3 validated** cryptographic module. [VERIFY module/version per deployment]
- The **encryption key is generated and held by the client** (or a client-controlled KMS). The key is **not escrowed with, accessible to, or recoverable by Technijian**.
- Detailed encryption configuration and FIPS-mode settings are specified in **CMMC-022**.

### 5.2 Configure the ciphertext-only store

- Target the **QNAP / Nimbus** appliance in the **TPX data center, Irvine, CA** as a **ciphertext-only repository** — no client decryption keys are present on, or accessible to, that store.
- Storage hardening, retention, and integrity controls are specified in **CMMC-023**.
- Rely on the **TPx SOC 2 Type II** report (`../tpx-dc/`) for the physical/environmental controls of the facility.

### 5.3 Verify Technijian cannot decrypt

- Demonstrate and **record evidence** that no Technijian process, service account, or tool can decrypt the stored ciphertext (e.g. attempt to open/restore without the client key and show it yields only ciphertext). Store this evidence in the client's `evidence/backup-recovery/` and `evidence/data-protection/` folders (see Section 8).

### 5.4 Test a client-keyed restore

- Perform an end-to-end **restore test**: Technijian restores the **ciphertext**, the **client supplies its key inside the client boundary**, and the client confirms successful decryption/recovery. Technijian never receives the plaintext or the key.
- The restore-test method, success criteria, and key-custody handling are defined in **CMMC-024** (data-flow/restore) together with **CMMC-022** and **CMMC-023**; record the test result as evidence.

**Output of Step 3:** operational client-keyed encrypted backup, a recorded **no-decrypt** demonstration, and a passed **client-keyed restore test**.

---

## 6. Step 4 — Stand up the segregated CMMC management plane

**Goal:** Isolate management of this DIB client from Technijian's general MSP fleet, so CMMC-relevant administration runs through a dedicated, controlled plane. Full build specification is in **CMMC-020**; the steps below are the onboarding actions.

### 6.1 Segregated remote support

- Create a **separate ScreenConnect session group** dedicated to this client. Do **not** manage CMMC client endpoints from shared/general session groups.

### 6.2 Segregated RMM / ITSM

- Stand up a **separate ManageEngine instance** for the client's CMMC-scoped assets (distinct from the general fleet instance), with its own access control and logging.

### 6.3 Segregated identity / admin

- Create a **dedicated Entra ID admin group** for the technicians authorized on this client, with least-privilege role assignment and MFA enforced. Authorization to this group is the gate for management-plane access.

### 6.4 FIPS mode where required

- Enable **FIPS mode** on management-plane components where the control set or contract requires it. [VERIFY per engagement / per tool support]

**Output of Step 4:** a segregated management plane (separate ScreenConnect group + separate ManageEngine instance + dedicated Entra admin group, FIPS where required), built and documented per **CMMC-020**, with access recorded as evidence under `evidence/access-control/`.

---

## 7. Step 5 — Deliver the governance artifacts

**Goal:** Put the core CMMC documentation in the client's hands, tailored, and help the client populate it.

### 7.1 Tailor and deliver the CRM ([[CMMC-004]])

- Provide the **Customer Responsibility Matrix**, tailored to this engagement, mapping each NIST SP 800-171 Rev 2 control to **Client**, **Technijian (ESP)**, or **Shared** responsibility.
- Anchor the matrix to the scope position in [[CMMC-019]]: Technijian owns the security-protection/backup controls; the client owns CUI handling inside its own boundary; keys are client-only.

### 7.2 Provide the SSP template ([[CMMC-001]])

- Provide the **System Security Plan** template and the data-flow/key-custody diagram from Step 2 for inclusion. Help the client describe the in-boundary environment and the Technijian ESP relationship.

### 7.3 Provide the POA&M template ([[CMMC-003]])

- Provide the **Plan of Action & Milestones** template. Seed it with any gaps identified during onboarding (e.g. controls not yet implemented in the client environment) with owners and target dates.

### 7.4 Help the client populate

- Work alongside the client ISSO to populate the SSP and CRM and to open POA&M items. **The client owns the content and the affirmation**; Technijian provides the templates, the ESP-side facts, and hands-on assistance.

**Output of Step 5:** tailored CRM, SSP (with diagram), and POA&M in the client's hands, with population underway.

---

## 8. Step 6 — Evidence-collection setup

**Goal:** Stand up the evidence repository and cadence so the client can demonstrate control implementation continuously, not scramble at assessment time.

### 8.1 Create per-control-domain evidence folders

Mirror the established `clients/<code>/evidence/` structure so evidence is organized by control domain:

```text
clients/<code>/evidence/
  ├── access-control/
  ├── asset-management/
  ├── backup-recovery/
  ├── change-management/
  ├── configuration-management/
  ├── data-protection/
  ├── endpoint-security/
  ├── incident-response/
  ├── logging-monitoring/
  ├── network-security/
  ├── patch-management/
  ├── physical-security/
  ├── risk-management/
  ├── security-awareness/
  └── vendor-management/
```

### 8.2 Set cadence and ownership

- Assign each evidence domain an **owner** (Technijian or client) consistent with the CRM, and a **collection cadence** (e.g. quarterly evidence pull per `../../templates/evidence-collection/quarterly-evidence-checklist.md`, with monthly items where required).
- Pre-load the ESP-side evidence Technijian produces: the no-decrypt demonstration and restore test (`backup-recovery/`, `data-protection/`), management-plane access records (`access-control/`), and the TPx SOC 2 reliance (`vendor-management/`, `physical-security/`).

**Output of Step 6:** an initialized per-domain evidence repository with named owners and a documented collection cadence.

---

## 9. Step 7 — Contracts

**Goal:** Paper the engagement so DoD obligations flow down correctly and Technijian's documents can be shared with the assessor.

### 9.1 MSA / SOW DoD addendum

- Execute the **DoD-client MSA/SOW addendum** that defines Technijian's ESP scope (backup + security, ciphertext-only, client-keyed), service levels, and responsibilities. Use the addendum defined in **CMMC-016**.

### 9.2 Flow-down clauses

- Include the applicable **DFARS 252.204-7012** safeguarding/reporting flow-down and any **252.204-7019/7020/7021** terms the client's prime/contract requires, scoped to Technijian's actual role. [VERIFY exact clauses per contract]

### 9.3 NDA for assessor sharing

- Put an **NDA** in place so Technijian's internal CMMC documents (this procedure, [[CMMC-019]], the CRM, diagrams, evidence) can be shared with the client's **C3PAO / assessor** under confidentiality, consistent with the "provided to clients and assessors under NDA" classification on these documents.

**Output of Step 7:** signed MSA/SOW DoD addendum (per CMMC-016), confirmed flow-down clauses, and an NDA covering assessor disclosure.

---

## 10. Step 8 — Incident-reporting integration

**Goal:** Wire Technijian's incident response into the client's **DoD 72-hour reporting** obligation so that a security event affecting the backup/management service is handled and escalated correctly.

### 10.1 The client's obligation

- Under **DFARS 252.204-7012**, the client must **report a cyber incident to DoD (via DIBNet) within 72 hours** of discovery. **The reporting obligation and the DoD report are the client's** — Technijian supports it but does not file on the client's behalf unless explicitly contracted. [VERIFY]

### 10.2 How Technijian's IRP supports it

- Technijian's **Incident Response Plan** (`../Incident_Response_Plan_IRP.md`; see also [[CMMC-010]] for the CMMC-specific incident handling/reporting integration) defines detection, triage, containment, and **client notification timelines designed to give the client enough runway to meet the 72-hour DoD deadline**.
- On any incident touching the CMMC management plane or the ciphertext store, Technijian **notifies the client ISSO promptly**, provides the technical facts the client needs for its DIBNet report, preserves evidence in `evidence/incident-response/`, and supports the client's reporting and recovery.
- Because Technijian holds only ciphertext and no keys, a compromise of Technijian-side storage does **not** by itself constitute a CUI spill — this is documented so incident scoping is accurate. [VERIFY with assessor/client]

**Output of Step 8:** an agreed notification flow tying the Technijian IRP to the client's 72-hour DoD reporting, with contacts and timelines recorded.

---

## 11. Step 9 — Ongoing review cadence

**Goal:** Keep the program current after go-live.

| Cadence | Activity | Owner |
|---|---|---|
| **Monthly** | POA&M review — update status, close items, add new gaps; pull monthly evidence where required | Client ISSO + Technijian vCISO |
| **Quarterly** | Evidence collection pull (`../../templates/evidence-collection/quarterly-evidence-checklist.md`); management-plane access review | Technijian + Client |
| **Annually** | SSP review and refresh (re-affirm boundary, key-custody, diagram); CRM re-validation | Client ISSO + Technijian vCISO |
| **Annually** | **TPx SOC 2 Type II** review — obtain and review the current report (`../tpx-dc/`); confirm no carve-outs or exceptions affect the relied-upon physical/environmental controls | Technijian vCISO |
| **On change** | Re-run relevant onboarding steps on any material change to backup architecture, key model, management plane, or DoD/CMMC guidance | Technijian vCISO |

**Output of Step 9:** a recurring review calendar with owners; deviations flagged and driven to POA&M items.

---

## 12. Onboarding checklist

Use this checklist to track an engagement to completion. Each item maps to a step above.

**Step 1 — Scoping call**
- [ ] FCI and/or CUI presence confirmed
- [ ] DFARS 252.204-7012 (and 7019/7020/7021) obligations captured
- [ ] Assessment target chosen (self-assessment vs C3PAO) [VERIFY]
- [ ] Timeline and POCs recorded; scoping memo filed

**Step 2 — Boundary**
- [ ] CUI/FCI data inventory and locations documented
- [ ] Asset categories drafted (CUI / SPA / CRMA / out-of-scope) [VERIFY with assessor]
- [ ] Technijian ESP role (backup + security, ciphertext-only, client-keyed) confirmed in writing
- [ ] Data-flow + key-custody diagram produced per CMMC-024

**Step 3 — Encrypted backup**
- [ ] NAKIVO source-side encryption configured, FIPS-validated module [VERIFY] (per CMMC-022)
- [ ] Client holds keys; no Technijian escrow/access
- [ ] QNAP/Nimbus ciphertext-only store configured in TPX Irvine (per CMMC-023)
- [ ] No-decrypt demonstration recorded as evidence
- [ ] Client-keyed restore test passed (per CMMC-024) and recorded

**Step 4 — Management plane**
- [ ] Separate ScreenConnect session group created
- [ ] Separate ManageEngine instance stood up
- [ ] Dedicated Entra admin group created (least privilege + MFA)
- [ ] FIPS mode enabled where required [VERIFY] (built per CMMC-020)

**Step 5 — Governance artifacts**
- [ ] CRM ([[CMMC-004]]) tailored and delivered
- [ ] SSP template ([[CMMC-001]]) delivered with diagram
- [ ] POA&M template ([[CMMC-003]]) delivered and seeded
- [ ] Client population assisted and underway

**Step 6 — Evidence**
- [ ] Per-control-domain evidence folders created (mirror `clients/<code>/evidence/`)
- [ ] Owners and cadence assigned
- [ ] ESP-side evidence pre-loaded (no-decrypt, restore, access records, TPx SOC 2)

**Step 7 — Contracts**
- [ ] MSA/SOW DoD addendum signed (per CMMC-016)
- [ ] DFARS flow-down clauses confirmed [VERIFY]
- [ ] NDA in place for assessor sharing

**Step 8 — Incident reporting**
- [ ] Client 72-hour DoD reporting obligation documented
- [ ] Technijian IRP notification flow tied to the deadline (`../Incident_Response_Plan_IRP.md`, [[CMMC-010]])
- [ ] Incident-response evidence folder ready; contacts/timelines recorded

**Step 9 — Ongoing cadence**
- [ ] Monthly POA&M review scheduled
- [ ] Annual SSP review scheduled
- [ ] Annual TPx SOC 2 review scheduled
- [ ] On-change re-review trigger documented

---

## 13. References

| ID / Path | Document | Why it is referenced here |
|---|---|---|
| [[CMMC-100]] | Client-Support Program | Parent program this onboarding operates under |
| [[CMMC-019]] | CUI Scope Position Statement | Governing scope: ciphertext-only, client-keyed, no Technijian decryption |
| [[CMMC-005]] | CUI / FCI Handling | Handling rules referenced during boundary definition |
| [[CMMC-004]] | Customer Responsibility Matrix (CRM) | Delivered in Step 5; responsibility split |
| [[CMMC-001]] | SSP template | Delivered in Step 5 |
| [[CMMC-003]] | POA&M template | Delivered in Step 5; seeded with gaps |
| CMMC-020 | Segregated management-plane build spec | Built in Step 4 |
| CMMC-022 | FIPS-validated, client-keyed encryption config | Configured in Step 3 |
| CMMC-023 | Ciphertext-only storage (QNAP/Nimbus) spec | Configured in Step 3 |
| CMMC-024 | Data-flow / key-custody diagram + restore-test standard | Produced in Step 2; restore test in Step 3 |
| [[CMMC-016]] | MSA / SOW DoD addendum | Executed in Step 7 |
| [[CMMC-010]] | CMMC incident handling / reporting integration | Wired in Step 8 |
| `../Incident_Response_Plan_IRP.md` | Technijian Incident Response Plan | Supports the client's 72-hour DoD reporting |
| `../tpx-dc/` | TPx SOC 2 Type II report | Physical/environmental controls relied upon for TPX Irvine DC |
| `../../templates/evidence-collection/quarterly-evidence-checklist.md` | Quarterly evidence checklist | Evidence cadence in Steps 6 and 9 |
| DFARS 252.204-7012 / 7019 / 7020 / 7021 | Federal clauses | Client contractual drivers and flow-downs |
| NIST SP 800-171 Rev 2 | Control set | The standard the client is assessed against |

---

## 14. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Principal / CEO | Ravi Jain | ________________ | __________ |
| Information Security Lead / vCISO | ________________ | ________________ | __________ |

---

### Version history
| Ver | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-19 | Technijian InfoSec | Initial draft for approval |
