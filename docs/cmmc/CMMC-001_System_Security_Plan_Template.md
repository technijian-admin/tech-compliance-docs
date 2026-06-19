# Technijian, Inc.

# System Security Plan (SSP) Template — NIST SP 800-171 Rev 2

**Document ID:** TJN-CMMC-001
**Owner:** Technijian Corporation (Information Security)
**Classification:** Internal — provided to clients and assessors under NDA
**Status:** DRAFT for principal approval
**Version:** 0.1 (2026-06-19)
**Related:** CMMC-100 (Client-Support Program); CMMC-004 (Customer Responsibility Matrix); CMMC-019 (CUI Scope); CMMC-003 (the sibling POA&M template)

---

## 1. How to use this template

This is a **client-fillable template**. It produces a **System Security Plan (SSP)** that documents how an organization seeking CMMC 2.0 **Level 2** assessment (aligned to **NIST SP 800-171 Rev 2**) implements each of the 110 security requirements across its in-scope environment.

**Ownership and division of labor:**

- **The client owns this document.** The client (the **Organization Seeking Assessment / OSA**) is the system owner, is responsible for the accuracy of every statement herein, and must formally **approve** the SSP (Section 9). An SSP is a required artifact for a Level 2 assessment, and the assessor evaluates the *as-implemented* environment against it.
- **Technijian assists** as the client's **MSP / External Service Provider (ESP)**. Technijian helps author and maintain this plan, supplies implementation statements for the controls Technijian operates or shares, and provides supporting evidence for those controls. **Technijian is not CMMC-certified** and does not assert certification; Technijian's role is to help the client meet CMMC / NIST SP 800-171.
- **Responsibility allocation** for every control (Client / Technijian / Shared / Inherited) is governed by the **Customer Responsibility Matrix (CRM)** — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md). Where this SSP and the CRM disagree on who owns a control, **reconcile before assessment**; the CRM is the authoritative responsibility allocation and [CMMC-019](./CMMC-019_CUI_Scope_Position_Statement.md) is the authoritative CUI-scoping statement.

**How to complete it:**

1. Fill every field marked **[CLIENT TO COMPLETE]** with information specific to your organization and system.
2. Resolve every **[VERIFY]** item — these depend on the specific engagement, architecture, or assessor determination and must be confirmed (often with Technijian and/or your C3PAO) before the SSP is finalized.
3. For each NIST 800-171 family (Section 6), write an implementation statement for **every** applicable control. This template provides the family structure and **example rows only** — it does **not** enumerate all 110 controls. The full control-by-control responsibility breakdown lives in the **CRM ([CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md))**.
4. Track every control that is **not yet fully met** in the **POA&M ([CMMC-003](./CMMC-003_POAM_Template.md))**. The SSP says what is implemented; the POA&M says what is planned and when it will close.
5. Keep this SSP and the broader **WISP** ([../Information_Security_Program_WISP.md](../Information_Security_Program_WISP.md)) consistent — the WISP is the program-level policy set; the SSP is the system-level implementation record.

> ⚠️ **This template is a starting point, not a finished SSP.** A completed SSP must reflect the client's actual, as-implemented environment. Do not submit this template with placeholders intact.

---

## 2. System identification

[CLIENT TO COMPLETE] — Complete the table below. This identifies the information system this SSP covers and the people accountable for it.

| Field | Value |
|---|---|
| **System name** | [CLIENT TO COMPLETE] |
| **System acronym / short name** | [CLIENT TO COMPLETE] |
| **System owner (organization)** | [CLIENT TO COMPLETE] |
| **System owner (individual + title)** | [CLIENT TO COMPLETE] |
| **Information System Security Officer (ISSO) / Security POC** | [CLIENT TO COMPLETE] |
| **ISSO contact (email / phone)** | [CLIENT TO COMPLETE] |
| **Authorizing official / executive sponsor** | [CLIENT TO COMPLETE] |
| **Legal entity name** | [CLIENT TO COMPLETE] |
| **CAGE code** | [CLIENT TO COMPLETE] |
| **DUNS / UEI** | [CLIENT TO COMPLETE] |
| **Primary contract(s) / programs driving CUI obligations** | [CLIENT TO COMPLETE] |
| **Applicable contract clauses** | [VERIFY] — typically DFARS 252.204-7012 / 7019 / 7020 / 7021; confirm per contract |
| **Target assessment level** | CMMC 2.0 **Level 2** (NIST SP 800-171 Rev 2) |
| **Assessment type** | [VERIFY] — self-assessment vs. C3PAO certification assessment (per contract requirement) |
| **External Service Provider(s)** | Technijian, Inc. (MSP / ESP — backup & security-protection services). Others: [CLIENT TO COMPLETE] |
| **SPRS posture** | [VERIFY] — current self-assessment score and date submitted to SPRS (see [CMMC-003](./CMMC-003_POAM_Template.md) §5) |

---

## 3. System environment & boundary

### 3.1 System description

[CLIENT TO COMPLETE] — Provide a narrative describing the system's purpose, the mission/business function it supports, the major components (servers, endpoints, network, cloud tenants, applications), the user population (employees, contractors, external parties), and the technologies in use.

### 3.2 Authorization boundary

[CLIENT TO COMPLETE] — Define the **authorization boundary**: everything that stores, processes, or transmits **FCI** and **CUI**, plus the **Security Protection Assets** that protect it. State clearly what is **in** the boundary and what is **out**, and how the boundary is enforced (network segmentation, identity boundaries, tenancy separation).

For each asset category in scope, identify it explicitly:

| Asset category | In this environment? | Notes |
|---|---|---|
| **CUI Assets** (store/process/transmit CUI) | [CLIENT TO COMPLETE] | The protected core of the boundary |
| **Security Protection Assets** (provide security functions to the boundary) | [CLIENT TO COMPLETE] | Includes Technijian-provided protection services — see §3.4 |
| **Contractor Risk-Managed Assets** | [CLIENT TO COMPLETE] | [VERIFY] categorization with C3PAO |
| **Specialized Assets** (IoT/OT/GFE/test equipment) | [CLIENT TO COMPLETE] | |
| **Out-of-scope assets** | [CLIENT TO COMPLETE] | Document the separation that keeps them out |

### 3.3 Where FCI and CUI live

[CLIENT TO COMPLETE] — Enumerate every location where **FCI** and **CUI** are stored, processed, or transmitted in **usable (plaintext) form**: file shares, endpoints, email/collaboration platforms, line-of-business apps, cloud services, removable media, and physical documents. This is the heart of the scope and drives which controls apply where.

### 3.4 Technijian-hosted backup — ciphertext-only, client-keyed (scope note)

> **The Technijian-hosted backup is not a CUI enclave.** Client data that reaches Technijian-operated infrastructure in connection with CUI does so **only as encrypted backup ciphertext**, for which **the client retains sole control of the encryption keys**. Technijian holds **only the ciphertext**, has **no access to the means of decryption**, and therefore **cannot read, render, or reconstitute** any CUI in that ciphertext.

Implications for this SSP's boundary:

- The Technijian backup service is a **security-protection / backup service**, **not** a CUI processing, storage, or transmission environment. Technijian-operated systems holding only client-keyed ciphertext are treated as **Security Protection Assets**, not **CUI Assets**, because they do not hold CUI in usable form.
- **Inherited physical/environmental protections** for the Technijian-operated infrastructure come from the **TPX data center**, which maintains a **SOC 2 Type II** attestation. See §5 and the CRM.
- The authoritative articulation of this position, its technical basis, and the assessor-validation caveat is [CMMC-019](./CMMC-019_CUI_Scope_Position_Statement.md). **[VERIFY]** this asset categorization with the client's C3PAO during each engagement — interpretations vary by assessor.

### 3.5 Network / boundary diagram

[CLIENT TO COMPLETE] — Embed or attach a current network diagram showing the authorization boundary, segmentation, ingress/egress points, and external connections (including the encrypted backup path to Technijian). See §4 for the recommended data-flow diagram content.

---

## 4. Data flow & CUI inventory

[CLIENT TO COMPLETE] — Document how FCI/CUI enters, moves through, is stored within, and leaves the boundary. Maintain a CUI inventory keyed to each location identified in §3.3.

### 4.1 CUI inventory

| CUI category / type | Source / origin | Where stored | How transmitted | Owner / steward | Marking applied? |
|---|---|---|---|---|---|
| [CLIENT TO COMPLETE] | [CLIENT TO COMPLETE] | [CLIENT TO COMPLETE] | [CLIENT TO COMPLETE] | [CLIENT TO COMPLETE] | [CLIENT TO COMPLETE] |
| [CLIENT TO COMPLETE] | | | | | |

### 4.2 Sample data-flow diagram (description)

A complete data-flow diagram should show, at minimum:

1. **Ingress** — how CUI arrives (e.g., DoD/prime portal, encrypted email, SFTP) and the boundary control it crosses.
2. **Processing/storage** — the in-boundary systems where CUI is used and stored (e.g., a segmented file server and managed endpoints inside an identity boundary).
3. **Backup path (Technijian)** — CUI is **encrypted at the client boundary (AES-256) before transit**, sent over **TLS 1.2+** to the **Technijian / TPX data center**, and stored **as ciphertext only**; the client **holds the keys** and Technijian **cannot decrypt**. Restoration returns **ciphertext** to the client, who decrypts inside their own boundary.
4. **Egress** — any authorized outbound flow of CUI to external parties, and the protections applied.

> Annotate each flow with the protection in force (encryption in transit/at rest, access control, logging). Mark the Technijian backup leg clearly as **ciphertext-only / client-keyed** so the diagram matches §3.4 and [CMMC-019](./CMMC-019_CUI_Scope_Position_Statement.md).

---

## 5. Inherited & shared controls

Not every control is implemented solely by the client. Some are **inherited** from a provider, and some are **shared** (split responsibility). The control-by-control allocation is authoritative in the **CRM ([CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md))**; this section summarizes the model.

| Control source | Provided by | Nature | Examples (illustrative) |
|---|---|---|---|
| **Inherited — physical & environmental** | **TPX data center** (**SOC 2 Type II**) | Inherited by the Technijian-operated infrastructure | Physical access control to the facility, environmental controls, power/HVAC, facility monitoring (supports parts of **3.10 Physical Protection**) |
| **Shared — logical & backup protection** | **Technijian (MSP / ESP)** | Shared with the client | Backup/restore of **client-keyed ciphertext**, security protection of the backup service, admin access control and logging on Technijian-operated systems, personnel screening for Technijian staff |
| **Client-owned** | **Client (OSA)** | Implemented by the client | CUI marking/handling, in-boundary identity & access management, endpoint config, awareness training, IR for the client environment, **custody of encryption keys** |

Notes:

- **Inheritance from Technijian/TPX is limited.** Technijian holds only **ciphertext** and **cannot decrypt** (see §3.4 and [CMMC-019](./CMMC-019_CUI_Scope_Position_Statement.md)); therefore Technijian/TPX provide **security-protection and backup** controls and **physical/environmental** inheritance — **not** CUI handling controls.
- For each control marked **Inherited** or **Shared** in Section 6, the responsible party and evidence source must match the CRM. **[VERIFY]** the current TPX SOC 2 Type II report date and scope, and obtain it as inheritance evidence.
- Request Technijian's **ESP / shared-responsibility documentation** ([CMMC-100](./CMMC-100_Client_Support_Program.md)) as supporting evidence for shared controls.

---

## 6. Control implementation

This section documents the implementation of the **14 NIST SP 800-171 Rev 2 families (3.1–3.14)**. For each family, complete the implementation table: write an implementation statement for **every** applicable control objective, set its status, and name the responsible party.

**Status legend:** **Implemented** = fully in place; **Planned** = not yet met, tracked in the [POA&M](./CMMC-003_POAM_Template.md); **Inherited** = provided by TPX/Technijian per §5 and the CRM; **N/A** = not applicable (justify).

> This template gives the family headers and **a couple of example control rows per family** to show the expected format. It does **not** enumerate all 110 controls. **[CLIENT TO COMPLETE] the remaining controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility allocation**, and open a [POA&M](./CMMC-003_POAM_Template.md) item for anything not yet **Implemented**.

### 3.1 Access Control

| Control ID | Implementation statement | Status (Implemented/Planned/Inherited/N-A) | Responsible party |
|---|---|---|---|
| 3.1.1 | [CLIENT TO COMPLETE] — Describe how access to the system is limited to authorized users, processes, and devices (e.g., identity provider, account provisioning/deprovisioning workflow). | [CLIENT TO COMPLETE] | Client |
| 3.1.2 | [CLIENT TO COMPLETE] — Describe how access is limited to the transactions/functions authorized users are permitted (RBAC / least privilege). | [CLIENT TO COMPLETE] | Client |
| ... | [CLIENT TO COMPLETE remaining 3.1 controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility] | | |

### 3.2 Awareness and Training

| Control ID | Implementation statement | Status (Implemented/Planned/Inherited/N-A) | Responsible party |
|---|---|---|---|
| 3.2.1 | [CLIENT TO COMPLETE] — Describe security awareness training for managers, system administrators, and users (content, frequency, tracking). | [CLIENT TO COMPLETE] | Client |
| 3.2.2 | [CLIENT TO COMPLETE] — Describe role-based training that ensures personnel are trained to carry out their assigned security duties. | [CLIENT TO COMPLETE] | Client |
| ... | [CLIENT TO COMPLETE remaining 3.2 controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility] | | |

### 3.3 Audit and Accountability

| Control ID | Implementation statement | Status (Implemented/Planned/Inherited/N-A) | Responsible party |
|---|---|---|---|
| 3.3.1 | [CLIENT TO COMPLETE] — Describe creation/retention of system audit logs sufficient to monitor, analyze, investigate, and report unlawful or unauthorized activity. | [CLIENT TO COMPLETE] | Shared (Client + Technijian for Technijian-operated systems) |
| 3.3.2 | [CLIENT TO COMPLETE] — Describe how actions are traceable to individual users to support accountability. | [CLIENT TO COMPLETE] | Client |
| ... | [CLIENT TO COMPLETE remaining 3.3 controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility] | | |

### 3.4 Configuration Management

| Control ID | Implementation statement | Status (Implemented/Planned/Inherited/N-A) | Responsible party |
|---|---|---|---|
| 3.4.1 | [CLIENT TO COMPLETE] — Describe how baseline configurations and inventories of system components are established and maintained. | [CLIENT TO COMPLETE] | Shared |
| 3.4.2 | [CLIENT TO COMPLETE] — Describe enforcement of security configuration settings for IT products. | [CLIENT TO COMPLETE] | Client |
| ... | [CLIENT TO COMPLETE remaining 3.4 controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility] | | |

### 3.5 Identification and Authentication

| Control ID | Implementation statement | Status (Implemented/Planned/Inherited/N-A) | Responsible party |
|---|---|---|---|
| 3.5.1 | [CLIENT TO COMPLETE] — Describe how users, processes, and devices are uniquely identified. | [CLIENT TO COMPLETE] | Client |
| 3.5.3 | [CLIENT TO COMPLETE] — Describe **multifactor authentication** for local and network access to privileged accounts and network access to non-privileged accounts. | [CLIENT TO COMPLETE] | Client |
| ... | [CLIENT TO COMPLETE remaining 3.5 controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility] | | |

### 3.6 Incident Response

| Control ID | Implementation statement | Status (Implemented/Planned/Inherited/N-A) | Responsible party |
|---|---|---|---|
| 3.6.1 | [CLIENT TO COMPLETE] — Describe the operational incident-handling capability (preparation, detection, analysis, containment, recovery, user response). Reference the [Incident Response Plan](../Incident_Response_Plan_IRP.md). | [CLIENT TO COMPLETE] | Shared |
| 3.6.2 | [CLIENT TO COMPLETE] — Describe tracking, documenting, and reporting of incidents to designated internal/external authorities (incl. DoD reporting where applicable). | [CLIENT TO COMPLETE] | Client |
| ... | [CLIENT TO COMPLETE remaining 3.6 controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility] | | |

### 3.7 Maintenance

| Control ID | Implementation statement | Status (Implemented/Planned/Inherited/N-A) | Responsible party |
|---|---|---|---|
| 3.7.1 | [CLIENT TO COMPLETE] — Describe how system maintenance is performed and controlled. | [CLIENT TO COMPLETE] | Shared |
| 3.7.2 | [CLIENT TO COMPLETE] — Describe controls on the tools, techniques, mechanisms, and personnel used to conduct maintenance. | [CLIENT TO COMPLETE] | Shared |
| ... | [CLIENT TO COMPLETE remaining 3.7 controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility] | | |

### 3.8 Media Protection

| Control ID | Implementation statement | Status (Implemented/Planned/Inherited/N-A) | Responsible party |
|---|---|---|---|
| 3.8.1 | [CLIENT TO COMPLETE] — Describe protection (physical and logical) of system media containing CUI. | [CLIENT TO COMPLETE] | Client |
| 3.8.9 | [CLIENT TO COMPLETE] — Describe protection of the **confidentiality of backup CUI** at storage locations. Note: the Technijian backup stores **client-keyed ciphertext only** (see §3.4); confidentiality at that location rests on client-held encryption. | [CLIENT TO COMPLETE] | Shared (Client keys; Technijian stores ciphertext) |
| ... | [CLIENT TO COMPLETE remaining 3.8 controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility] | | |

### 3.9 Personnel Security

| Control ID | Implementation statement | Status (Implemented/Planned/Inherited/N-A) | Responsible party |
|---|---|---|---|
| 3.9.1 | [CLIENT TO COMPLETE] — Describe how individuals are screened prior to authorizing access to systems containing CUI. Technijian screens its own personnel who operate Technijian systems. | [CLIENT TO COMPLETE] | Shared |
| 3.9.2 | [CLIENT TO COMPLETE] — Describe how CUI and systems are protected during personnel actions (termination, transfer). | [CLIENT TO COMPLETE] | Client |
| ... | [CLIENT TO COMPLETE remaining 3.9 controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility] | | |

### 3.10 Physical Protection

| Control ID | Implementation statement | Status (Implemented/Planned/Inherited/N-A) | Responsible party |
|---|---|---|---|
| 3.10.1 | [CLIENT TO COMPLETE] — Describe how physical access to systems, equipment, and operating environments is limited to authorized individuals. For Technijian-operated infrastructure, physical protection is **inherited from the TPX data center (SOC 2 Type II)** — see §5. | Inherited (TPX) for Technijian-hosted infra; [CLIENT TO COMPLETE] for client sites | Inherited (TPX) / Client |
| 3.10.2 | [CLIENT TO COMPLETE] — Describe protection and monitoring of the physical facility and support infrastructure. | [CLIENT TO COMPLETE] | Inherited (TPX) / Client |
| ... | [CLIENT TO COMPLETE remaining 3.10 controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility] | | |

### 3.11 Risk Assessment

| Control ID | Implementation statement | Status (Implemented/Planned/Inherited/N-A) | Responsible party |
|---|---|---|---|
| 3.11.1 | [CLIENT TO COMPLETE] — Describe periodic risk assessments of operations, assets, and individuals. | [CLIENT TO COMPLETE] | Client |
| 3.11.2 | [CLIENT TO COMPLETE] — Describe vulnerability scanning of the system and applications. | [CLIENT TO COMPLETE] | Shared |
| ... | [CLIENT TO COMPLETE remaining 3.11 controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility] | | |

### 3.12 Security Assessment

| Control ID | Implementation statement | Status (Implemented/Planned/Inherited/N-A) | Responsible party |
|---|---|---|---|
| 3.12.1 | [CLIENT TO COMPLETE] — Describe how security controls are periodically assessed for effectiveness. | [CLIENT TO COMPLETE] | Client |
| 3.12.2 | [CLIENT TO COMPLETE] — Describe the **plan of action (POA&M)** used to correct deficiencies and reduce/eliminate vulnerabilities — see [CMMC-003](./CMMC-003_POAM_Template.md). | [CLIENT TO COMPLETE] | Client |
| ... | [CLIENT TO COMPLETE remaining 3.12 controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility] | | |

### 3.13 System and Communications Protection

| Control ID | Implementation statement | Status (Implemented/Planned/Inherited/N-A) | Responsible party |
|---|---|---|---|
| 3.13.1 | [CLIENT TO COMPLETE] — Describe monitoring/control/protection of communications at the external and key internal boundaries. | [CLIENT TO COMPLETE] | Client |
| 3.13.11 | [CLIENT TO COMPLETE] — Describe use of **FIPS-validated cryptography** to protect the confidentiality of CUI. Note the backup path uses **AES-256 at the client boundary + TLS 1.2+ in transit** (see §4.2). | [CLIENT TO COMPLETE] / [VERIFY] FIPS validation | Shared |
| ... | [CLIENT TO COMPLETE remaining 3.13 controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility] | | |

### 3.14 System and Information Integrity

| Control ID | Implementation statement | Status (Implemented/Planned/Inherited/N-A) | Responsible party |
|---|---|---|---|
| 3.14.1 | [CLIENT TO COMPLETE] — Describe how system flaws are identified, reported, and corrected in a timely manner (patch management). | [CLIENT TO COMPLETE] | Shared |
| 3.14.2 | [CLIENT TO COMPLETE] — Describe malicious-code protection at appropriate locations. | [CLIENT TO COMPLETE] | Shared |
| ... | [CLIENT TO COMPLETE remaining 3.14 controls — see [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md) for responsibility] | | |

---

## 7. Roles & responsibilities

[CLIENT TO COMPLETE] — Identify the people and parties accountable for the security program supporting this system.

| Role | Name / party | Responsibility |
|---|---|---|
| **System owner** | [CLIENT TO COMPLETE] | Owns the system and the accuracy of this SSP; approves it |
| **Authorizing official / executive sponsor** | [CLIENT TO COMPLETE] | Accepts residual risk; authorizes operation |
| **ISSO / Security POC** | [CLIENT TO COMPLETE] | Day-to-day security operations and SSP/POA&M maintenance |
| **CUI custodian(s) / data stewards** | [CLIENT TO COMPLETE] | Handle and mark CUI per policy |
| **Encryption key custodian** | [CLIENT TO COMPLETE] (**Client**) | Sole custody of backup encryption keys — Technijian has none |
| **MSP / ESP** | **Technijian, Inc.** | Backup of client-keyed ciphertext + security-protection services; assists with SSP/POA&M authoring and evidence; **not CMMC-certified** |
| **Data center (physical/environmental)** | **TPX (SOC 2 Type II)** | Inherited physical/environmental controls for Technijian-operated infrastructure |
| **C3PAO / assessor** | [VERIFY] | Conducts the Level 2 assessment (do not name until engaged) |

---

## 8. Plan maintenance & review cadence

- **Review frequency:** This SSP is reviewed at least **annually** and upon any **material change** to the system, boundary, data flows, key-management model, ESP relationship, or applicable CMMC/NIST guidance. **[VERIFY]** the cadence against contract requirements.
- **Change triggers:** new/decommissioned CUI Assets; boundary or segmentation changes; new external connections or ESPs; significant incidents; control implementation status changes (which must also update the [POA&M](./CMMC-003_POAM_Template.md)).
- **Consistency:** Keep the SSP, the **CRM ([CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md))**, the **POA&M ([CMMC-003](./CMMC-003_POAM_Template.md))**, the **CUI scope statement ([CMMC-019](./CMMC-019_CUI_Scope_Position_Statement.md))**, and the **WISP ([../Information_Security_Program_WISP.md](../Information_Security_Program_WISP.md))** in sync. A change in one frequently requires a change in the others.
- **Evidence refresh:** Re-collect inheritance evidence (e.g., the **TPX SOC 2 Type II** report) on each renewal and before each assessment.
- **Version control:** Record every change in the version history below; material changes require re-approval (Section 9).

---

## 9. Approval

By signing, the client confirms this System Security Plan accurately reflects the as-implemented environment and accepts ownership of it. Technijian's signature, where provided, attests only to the accuracy of the Technijian-provided (shared/inherited) implementation statements — **not** to CMMC certification of the client.

| Role | Name | Signature | Date |
|---|---|---|---|
| **System owner (Client)** | [CLIENT TO COMPLETE] | ________________ | __________ |
| **Authorizing official (Client)** | [CLIENT TO COMPLETE] | ________________ | __________ |
| **ISSO / Security POC (Client)** | [CLIENT TO COMPLETE] | ________________ | __________ |
| **Technijian (ESP) — for shared/inherited statements only** | [VERIFY] | ________________ | __________ |

---

### Version history

| Ver | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-19 | Technijian InfoSec | Initial client-fillable template for principal approval |
