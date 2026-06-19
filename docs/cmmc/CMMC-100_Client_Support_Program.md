# Technijian, Inc.

# CMMC Client-Support Program — ESP Service Description and Shared-Responsibility Overview

**Document ID:** TJN-CMMC-100
**Owner:** Technijian Corporation (Information Security)
**Classification:** Internal — provided to clients and assessors under NDA
**Status:** DRAFT for principal approval
**Version:** 0.1 (2026-06-19)
**Related:** WISP; CMMC-019 (CUI Scope Position); CMMC-005 (CUI/FCI Handling); CMMC-004 (Customer Responsibility Matrix); CMMC-001 (SSP template); CMMC-003 (POA&M template); CMMC-101 (Client Onboarding)

---

## 1. Purpose & Audience

This document describes the **CMMC Client-Support Program** offered by Technijian, Inc. ("Technijian") to its Defense Industrial Base (DIB) clients. It explains, in one place, **what Technijian delivers**, **how Technijian's role is bounded**, and **who is responsible for what** when a client pursues **CMMC 2.0 Level 2** assessment against **NIST SP 800-171 Rev 2**.

It is written for two audiences:

- **Clients** — DIB organizations (contractors and subcontractors) that handle Federal Contract Information (FCI) and/or Controlled Unclassified Information (CUI) and need help preparing for, and sustaining, CMMC Level 2 compliance.
- **Assessors** — C3PAOs and assessment teams evaluating a client's environment who need to understand how Technijian (as an External Service Provider) supplies, shares, or inherits specific controls, and where Technijian's responsibility begins and ends.

> **This is a service description and a responsibility map — not a control implementation record.** A client's specific control evidence lives in that client's **System Security Plan (SSP)** and **Customer Responsibility Matrix (CRM)**. This program document tells you how Technijian helps the client populate those artifacts.

## 2. Technijian's Role — External Service Provider (Explicitly NOT Certified)

### 2.1 What Technijian is

Technijian is a **Managed Service Provider (MSP)** acting as an **External Service Provider (ESP)** to its DIB clients. An ESP, in CMMC terms, is an external entity that provides **information technology and/or cybersecurity services** that are relevant to a client's compliance — for example, managed security operations, logging, backup, and infrastructure that a client relies on as part of its security posture.

Technijian's ESP role is deliberately narrow and is governed by **CMMC-019 (CUI Scope Position Statement)**: Technijian provides a **security-protection and encrypted-backup environment**, **not** a CUI processing, storage, or transmission environment.

### 2.2 What Technijian is NOT — read this first

> **Technijian is NOT CMMC-certified and does not pursue its own CMMC certification.** Technijian **helps clients meet** CMMC 2.0 Level 2 / NIST SP 800-171 Rev 2 requirements; it does not represent that Technijian itself is "certified," "assessed," or "compliant" under CMMC.

- Technijian is **not a C3PAO** and does **not** conduct CMMC assessments or grant certifications.
- Technijian does **not** store, process, or transmit **plaintext CUI** on any Technijian-operated system.
- Engaging Technijian does **not** by itself make a client compliant. The client remains the **Organization Seeking Assessment (OSA)** and **owns its CMMC outcome**.

### 2.3 Why the ESP distinction matters

Because Technijian provides defined services rather than holding CUI, the client and its assessor can treat Technijian's in-scope systems as **Security Protection Assets / Contractor Risk-Managed Assets** (per CMMC-019), and can **inherit or share** specific controls that Technijian operates — while keeping ownership of CUI handling, marking, and the SSP firmly with the client.

## 3. The Service Offering — How Technijian Helps a DIB Client Reach CMMC Level 2

Technijian delivers the following to support a client's CMMC Level 2 readiness. Each item maps to one or more NIST SP 800-171 control families; the **client's CRM** records the precise mapping for that client's environment.

### 3.1 Managed security operations (logical controls)

Technijian operates and maintains the **logical security controls** on the systems it manages on the client's behalf — for example: identity and access management, multi-factor authentication enforcement, endpoint detection and response (EDR), patch and configuration baselines, vulnerability management, DNS-layer security, and centralized logging/alerting. These contribute to the **Access Control (AC)**, **Audit & Accountability (AU)**, **Configuration Management (CM)**, **Identification & Authentication (IA)**, **System & Information Integrity (SI)**, and **System & Communications Protection (SC)** families. *(Specific tooling and coverage are client-architecture-dependent — [VERIFY] per engagement and record in the client CRM.)*

### 3.2 FIPS-validated, client-keyed encrypted backup

Technijian provides **backup and storage of encrypted data only**. Client data is encrypted **at the client boundary** with a **FIPS 140-2/3 validated** cryptographic module (**AES-256**) **before** it leaves the client environment, transmitted over **TLS 1.2+**, and stored as **ciphertext only** on Technijian storage (QNAP / Nimbus) in the **TPX data center, Irvine, CA**. **The client holds the encryption keys; Technijian cannot decrypt.** Restores return **ciphertext** to the client, who decrypts inside its own boundary. This supports the **Media Protection (MP)**, **Recovery / contingency**, and **SC** objectives without Technijian ever handling plaintext CUI. See **Section 5** and **CMMC-019**.

### 3.3 A segregated CMMC management plane

Technijian administers managed client systems through a **segregated management plane** — separated administrative tooling, accounts, and access paths used to deliver managed services. Segregation limits the blast radius of administrative access and supports **AC** (least privilege, separation of duties) and **SC** (boundary protection) objectives. *(The exact topology and segregation boundaries are client-architecture-dependent — [VERIFY] and document per engagement.)*

### 3.4 Evidence-collection support

Technijian helps the client **collect and organize assessment evidence** for the systems and services Technijian operates — for example: access reviews, MFA enforcement reports, patch/vulnerability status, log retention configuration, backup success records, and screenshots/exports that demonstrate control operation. This evidence feeds the client's SSP narratives and the assessor's review. **Technijian supplies evidence for what Technijian operates; the client compiles the complete evidence package.**

### 3.5 Authoring help for the client's SSP / CRM / POA&M

Technijian provides **authoring and templating assistance** for the client's:

- **System Security Plan (SSP)** — using the **CMMC-001** template,
- **Customer Responsibility Matrix (CRM)** — using **CMMC-004**, allocating each control to Client / Technijian / inherited, and
- **Plan of Action & Milestones (POA&M)** — using **CMMC-003**, tracking gaps to closure.

> **Authoring help is not ownership.** Technijian helps draft and structure these documents; the **client reviews, approves, and owns** them, and the client attests to their accuracy.

## 4. Shared-Responsibility Model

The matrix below allocates responsibility across the **Client (OSA)**, **Technijian (ESP)**, and **TPX (data center — inherited)**. It is a program-level overview; the **binding, control-by-control allocation lives in the client's CRM (CMMC-004)**.

Legend: **R** = Responsible/owns · **S** = Supports/shares · **I** = Inherited by client from provider · **—** = Not applicable.

| Area | Client (OSA) | Technijian (ESP) | TPX (data center — inherited) |
|---|---|---|---|
| **Physical & environmental security** (facility, power, cooling, physical access to racks) | — | **S** — relies on TPX; manages logical access to Technijian-operated systems | **I / R** — provides physical/environmental controls per its **SOC 2 Type II** |
| **CUI processing** (creating, using, rendering CUI) | **R** — sole processor inside client boundary | **—** — no plaintext CUI on Technijian systems | **—** |
| **CUI at rest** (storage) | **R** — plaintext CUI inside client boundary | **S** — stores **ciphertext only**; cannot decrypt | **I** — provides the physically secured facility for that ciphertext storage |
| **Encryption keys** (generation, custody, rotation) | **R** — client generates and **holds all keys** | **—** — **no access**, not escrowed, cannot recover | **—** |
| **Logical access to managed systems** (admin identities, MFA, least privilege) | **S** — approves access; owns access in client-controlled systems | **R** — operates IAM/MFA/least-privilege on systems Technijian manages | **—** |
| **Backup service** (encrypted backup + restore of ciphertext) | **R** — encrypts at boundary, owns keys, validates restores | **R** — operates the backup/storage service for ciphertext | **I** — hosts the storage infrastructure |
| **Monitoring & logging** (collection, alerting, retention) | **S** — owns monitoring in client-controlled systems | **R** — logging/alerting/retention for systems Technijian operates | **I** — facility-level/environmental monitoring |
| **Incident response** (detection, containment, notification) | **R** — owns IR for the client environment and CUI; reports to DoD as required | **S** — detects/contains/notifies for Technijian-operated systems per the **IRP**; supports client IR | **S** — facility/infrastructure incidents per TPX procedures |
| **Personnel screening** (background checks, security training) | **R** — for client personnel | **R** — for Technijian personnel with access to managed systems, per the **Employee Security Policy** | **R** — for TPX personnel, per its SOC 2 |
| **SSP & POA&M ownership** (authoring, approval, attestation) | **R** — **owns and attests** to SSP/CRM/POA&M | **S** — provides authoring/templating help (CMMC-001/003/004) | **—** |

> **How to read this matrix:** wherever Technijian is **S** or **R**, Technijian's operation of that control can be **inherited or shared** by the client and cited in the client's SSP/CRM. Wherever the Client is **R**, the obligation stays inside the client boundary regardless of Technijian's services.

## 5. The CUI Boundary — In One Paragraph

Per **CMMC-019** and **CMMC-005**, **Technijian does not store, process, or transmit plaintext CUI on any Technijian-operated system.** The only CUI-related data that reaches Technijian infrastructure is **encrypted backup ciphertext**: it is encrypted **at the client boundary** with a **FIPS 140-2/3 validated** module (**AES-256**) **before transit**, moves over **TLS 1.2+**, and rests as **ciphertext only** on Technijian's QNAP/Nimbus storage in the **TPX data center, Irvine, CA**. **The client holds the encryption keys and Technijian cannot decrypt**, so Technijian cannot read, render, or reconstitute the CUI; **restores return ciphertext to the client**, who decrypts inside its own boundary. Technijian's systems are therefore a **security-protection and encrypted-backup environment**, not a CUI processing/storage/transmission environment. See **CMMC-019 (CUI Scope Position)** for the controlling statement and technical basis, and **CMMC-005 (CUI/FCI Handling)** for the handling rules.

## 6. How Technijian's Existing Program Provides Inherited / Shared Controls

Technijian does not build CMMC support from scratch — it maps its **existing, operating security program** to the client's CRM so the client can **inherit or share** mature controls. The documents below are **referenced, not duplicated here**; each supplies controls and evidence that the client's CRM can cite for the systems Technijian operates.

| Program document | Contributes to (NIST 800-171 themes) |
|---|---|
| [Information Security Program (WISP)](../Information_Security_Program_WISP.md) | Overarching governance, risk management, administrative/technical/physical safeguards |
| [Access Control Policy](../Access_Control_Policy.md) | **AC**, **IA** — least privilege, MFA, account management for managed systems |
| [Incident Response Plan (IRP)](../Incident_Response_Plan_IRP.md) | **IR** — detection, containment, notification for Technijian-operated systems |
| [Data Classification & Retention Policy](../Data_Classification_Retention_Policy.md) | **MP**, **AU** — classification, handling, retention of data and logs |
| [Employee Security Policy](../Employee_Security_Policy.md) | **PS**, **AT** — personnel screening, onboarding/offboarding, security awareness |
| [Vendor Risk Management Policy](../Vendor_Risk_Management_Policy.md) | **SR / supply chain** — third-party/subservice oversight (including TPX) |
| [Change Management Policy](../Change_Management_Policy.md) | **CM** — change control, configuration baselines for managed systems |
| [Business Continuity & Disaster Recovery Plan (BCP/DR)](../Business_Continuity_Disaster_Recovery_Plan_BCP_DR.md) | Contingency/recovery — availability of the backup service |

> **Physical/environmental controls are inherited from TPX, not audited by Technijian.** Technijian relies on the **TPX SOC 2 Type II** report for physical and environmental controls at the Irvine data center and **does not undergo its own SOC 2 audit**. Technijian implements the **complementary user-entity controls (CUECs)** identified in the TPX report and provides the **logical** controls on the systems it operates. The TPX report is available to clients/assessors under NDA.

## 7. Companion Documents

The following CMMC-series documents work together with this program description. Each is referenced here; the authoritative content lives in the named document.

| Document | One-line description |
|---|---|
| **CMMC-019 — CUI Scope Position Statement** | The controlling statement that no plaintext CUI resides on Technijian systems (ciphertext-only, client-held keys). |
| **CMMC-005 — CUI/FCI Handling** | How CUI and FCI are handled, including the WISP CUI addendum and ciphertext-only backup rules. |
| **CMMC-004 — Customer Responsibility Matrix (CRM)** | The binding, control-by-control allocation of each 800-171 requirement to Client / Technijian / inherited. |
| **CMMC-001 — SSP Template** | The System Security Plan template the client populates (with Technijian authoring help). |
| **CMMC-003 — POA&M Template** | The Plan of Action & Milestones template used to track gaps to closure. |
| **CMMC-101 — Client Onboarding** | The onboarding runbook that operationalizes the engagement phases in Section 8. |

## 8. Engagement Phases

A typical CMMC Client-Support engagement moves through the phases below. The runbook detail lives in **CMMC-101 (Client Onboarding)**.

| Phase | What happens | Primary owner | Key output |
|---|---|---|---|
| **1. Scoping** | Identify the client's CUI/FCI, in-scope systems, contracts/flow-downs, and the services Technijian will provide. | Client (with Technijian support) | Scoping notes; asset/data inventory |
| **2. Boundary definition** | Define the CUI boundary and asset categories; confirm the ciphertext-only/client-keys position (CMMC-019). | Client + Technijian | Boundary diagram; asset categorization |
| **3. Backup + management-plane setup** | Stand up FIPS-validated client-keyed encrypted backup and the segregated CMMC management plane. | Technijian | Operating backup service; segregated management plane |
| **4. SSP / CRM / POA&M** | Author the SSP (CMMC-001), allocate responsibilities in the CRM (CMMC-004), and open the POA&M (CMMC-003). | Client (Technijian authoring help) | Draft SSP, CRM, POA&M for client approval |
| **5. Evidence** | Collect and organize evidence for Technijian-operated controls; assemble the client's full evidence package. | Client + Technijian | Evidence repository ready for assessment |
| **6. Ongoing review** | Periodic access reviews, patch/vulnerability and backup verification, log review, POA&M burn-down, and document refresh. | Technijian + Client | Recurring review records; updated POA&M/SSP |

## 9. Disclaimer

> **Read carefully.** Technijian is an **MSP / External Service Provider** that **helps support** clients in meeting CMMC 2.0 Level 2 / NIST SP 800-171 Rev 2 requirements. The following limits apply and control over any contrary implication elsewhere:

- **Not certified.** Technijian is **not CMMC-certified** and does **not** pursue its own CMMC certification. Nothing herein states or implies that Technijian is certified, assessed, or compliant under CMMC.
- **Not a C3PAO.** Technijian is **not** a CMMC Third-Party Assessment Organization, does **not** perform CMMC assessments, and **does not grant certification** of any kind.
- **No outcome guarantee.** Technijian **makes no guarantee** as to a client's assessment result, score, or certification decision. Use "**helps support**" / "**helps you meet**" — **never** "guarantees compliance."
- **Client owns the outcome.** The client is the Organization Seeking Assessment and **owns and attests to** its SSP, CRM, and POA&M and its CMMC posture. The assessor (C3PAO) makes the certification determination.
- **Assessor validation required.** Asset categorization and the "encrypted-with-no-key-access = not CUI handling" position (CMMC-019) must be **confirmed with the client's C3PAO** each engagement; interpretations vary by assessor.

## 10. References

- **NIST SP 800-171 Rev 2** — *Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations.*
- **NIST SP 800-171A** — *Assessing Security Requirements for Controlled Unclassified Information.*
- **CMMC 2.0 (32 CFR Part 170)** — Cybersecurity Maturity Model Certification Program rule; **48 CFR / DFARS 252.204-7012, -7019, -7020, -7021** — safeguarding and assessment clauses.
- **FIPS 140-2 / FIPS 140-3** — Security Requirements for Cryptographic Modules.
- **TPX Communications — SOC 2 Type II Report (2025)** — physical/environmental controls for the Irvine, CA data center (inherited; available under NDA): `../tpx-dc/TPx Communications-2025-Type 2 SOC 2-Final Report.pdf`.
- **Internal:** CMMC-019, CMMC-005, CMMC-004, CMMC-001, CMMC-003, CMMC-101; [WISP](../Information_Security_Program_WISP.md), [Access Control Policy](../Access_Control_Policy.md), [IRP](../Incident_Response_Plan_IRP.md), [Data Classification & Retention Policy](../Data_Classification_Retention_Policy.md), [Employee Security Policy](../Employee_Security_Policy.md), [Vendor Risk Management Policy](../Vendor_Risk_Management_Policy.md), [Change Management Policy](../Change_Management_Policy.md), [BCP/DR](../Business_Continuity_Disaster_Recovery_Plan_BCP_DR.md).

---

## Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Principal / CEO | Ravi Jain | ________________ | __________ |
| Information Security Lead | ________________ | ________________ | __________ |

---

### Version history
| Ver | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-19 | Technijian InfoSec | Initial draft for approval |
