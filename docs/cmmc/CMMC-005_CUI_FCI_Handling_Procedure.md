# Technijian, Inc.

# CUI and FCI Data Handling Procedure (WISP Addendum)

**Document ID:** TJN-CMMC-005
**Owner:** Technijian Corporation (Information Security)
**Classification:** Internal — provided to clients and assessors under NDA
**Status:** DRAFT for principal approval
**Version:** 0.1 (2026-06-19)
**Related:** WISP §5 (Data Classification); CMMC-019 (CUI Scope Position); CMMC-004 (CRM); Data_Classification_Retention_Policy

---

## 1. Purpose and Scope

This procedure governs how Technijian personnel and systems handle **Federal Contract Information (FCI)** and **Controlled Unclassified Information (CUI)** encountered in the course of Technijian's **External Service Provider (ESP)** services to clients in the Defense Industrial Base (DIB). It is an **addendum to the Technijian Information Security Program (WISP)** and operationalizes the scoping position recorded in [CMMC-019 — CUI Scope Position Statement](CMMC-019_CUI_Scope_Position_Statement.md).

**Audience and applicability.** This procedure applies to all Technijian employees, contractors, and subcontractors who administer, monitor, or otherwise touch the backup and storage management plane that holds client backup data, and to the systems that provide that service.

**Technijian's posture (controlling context).** Technijian is a managed IT services provider / ESP that **helps DIB clients meet their CMMC 2.0 / NIST SP 800-171 Rev 2 obligations**. Technijian is **not itself CMMC-certified** and does not represent itself as such. Critically, **Technijian does not store, process, or transmit plaintext CUI**. The only client data that reaches Technijian infrastructure in connection with CUI is **encrypted backup ciphertext** for which the **client holds the encryption keys**; Technijian **cannot decrypt** it. This document describes the rules and controls that keep that boundary intact.

**Out of scope.** This procedure does not govern the client's own handling of CUI/FCI inside the client's boundary (marking, in-use protection, dissemination control), nor does it substitute for the client's System Security Plan (SSP) or for a C3PAO assessment. Those remain **client responsibilities**.

---

## 2. Definitions

| Term | Definition |
|---|---|
| **FCI (Federal Contract Information)** | Information, not intended for public release, that is provided by or generated for the Government under a contract to develop or deliver a product or service to the Government. FCI excludes information provided to the public (such as on public websites) and simple transactional information. Source authority: FAR 52.204-21. |
| **CUI (Controlled Unclassified Information)** | Government-created or -owned information that requires safeguarding or dissemination controls consistent with applicable law, regulation, and Government-wide policy, but that is not classified. CUI categories and markings are defined by the National Archives (NARA) CUI Registry. Protection baseline for nonfederal systems: NIST SP 800-171 Rev 2. |
| **ESP (External Service Provider)** | An entity (such as Technijian) external to the client organization that provides IT and/or cybersecurity services and may have access to, or store/process/transmit, the client's information or security-relevant data. |
| **Ciphertext / backup blob** | Client backup data encrypted at the client boundary before it leaves the client's control. To Technijian, a backup blob is **opaque** — it cannot be read, mounted, or interpreted without the client's key. |
| **CUI enclave** | A defined boundary of systems that store, process, or transmit CUI **in usable (plaintext) form**. See §3 — Technijian's environment is **not** a CUI enclave. |

**Data owner / marking authority.** The **client is the data owner** and is the sole authority on **whether information is FCI or CUI and how it is marked**. Technijian does not classify, re-classify, or mark client information. Where Technijian personnel are uncertain about the nature of data they encounter, the data is treated at the **higher sensitivity** and the matter is escalated per §5.

---

## 3. The ESP Boundary

Restating the controlling invariant from [CMMC-019](CMMC-019_CUI_Scope_Position_Statement.md):

> **Technijian does not store, process, or transmit CUI in plaintext on any Technijian-operated system.** The only client data that reaches Technijian infrastructure in connection with CUI is **encrypted backup ciphertext**, for which the **client retains sole control of the encryption keys**. Technijian has **no access to the means of decryption** and therefore cannot read, render, or reconstitute any CUI contained in that ciphertext.

**Technijian's environment is NOT a CUI enclave** — because **Technijian cannot decrypt**. A CUI enclave is a boundary in which CUI exists in usable (plaintext) form. On Technijian-operated storage, client backups exist **only as ciphertext to which Technijian holds no key**, so no CUI is present in usable form. Technijian therefore acts as a **security-protection / backup-and-storage ESP**, not as a CUI processing, storage, or transmission environment.

**Division of responsibility (summary).**

| Layer | Provided by | Notes |
|---|---|---|
| Logical controls over the storage / management plane (access control, logging, change control, integrity/availability of ciphertext) | **Technijian** | Documented in the CRM ([CMMC-004](CMMC-004_Customer_Responsibility_Matrix.md)) as Technijian or Shared. |
| Physical and environmental controls at the data center | **TPX (Irvine, CA)** | Relied upon under TPX's **SOC 2 Type II**; physical access, power, cooling, fire suppression, media-handling at the facility. See [tpx-dc](../tpx-dc). |
| Marking, in-use protection, and dissemination control of CUI/FCI in plaintext | **Client** | Inside the client's own boundary; out of scope for Technijian. |
| Custody of encryption keys | **Client** | Never escrowed with or accessible to Technijian (see §4). |

> ⚠️ **Assessor validation required.** The "encrypted-with-no-key-access = not CUI handling" position and the resulting asset categorization must be confirmed with the client's C3PAO for each engagement; interpretations vary by assessor. This procedure records Technijian's controls and basis to support that determination — it does not substitute for the assessor's scoping decision.

---

## 4. Data Flow and Key Custody

### 4.1 Lifecycle

The CUI/FCI backup lifecycle, end to end:

1. **Mark & encrypt (client boundary).** The client identifies and marks FCI/CUI within its own environment and encrypts the backup set using a **FIPS 140-2/3 validated cryptographic module (AES-256)** under a **client-controlled key**, **before** any data leaves the client boundary.
2. **Transit.** The resulting ciphertext is transmitted to the Technijian-managed storage target over **TLS 1.2 or higher**. (Transit protection is layered on top of the data already being encrypted at rest by the client's module — i.e. defense in depth, not the primary confidentiality control.)
3. **At rest (Technijian / TPX).** Ciphertext is stored on **QNAP / Nimbus storage in the TPX data center, Irvine, CA**, as **ciphertext only**. Without the client key, the contents are not recoverable by Technijian personnel or systems.
4. **Restore.** A restore operation returns the **ciphertext** to the client. Technijian's role ends at delivery of the encrypted blob.
5. **Decrypt (client boundary).** The client decrypts the restored ciphertext **within its own boundary**, using its own key and FIPS-validated module. Plaintext CUI never exists on Technijian infrastructure.

```
[CLIENT BOUNDARY]                         [TRANSIT]            [TECHNIJIAN / TPX]
mark + encrypt (FIPS module,   ── TLS 1.2+ ──▶  ciphertext at rest
client-held key, AES-256)                       (QNAP / Nimbus, Irvine CA)
        ▲                                                 │
        │                                                 │
   decrypt in client boundary  ◀── TLS 1.2+ ──  restore returns ciphertext
```

### 4.2 Key custody statement

**Encryption keys for client CUI/FCI are generated and retained by the client (or a client-controlled KMS). Keys are never escrowed with, accessible to, or recoverable by Technijian.** Technijian operates **no process, service account, or tooling capable of decrypting client backups**. There is no Technijian-held key, no key-recovery agent, and no break-glass path to client plaintext. Because Technijian cannot decrypt, a compromise of Technijian infrastructure does not yield usable CUI (see §9).

---

## 5. Handling Rules for Technijian Staff

These rules are mandatory for all personnel who touch the backup/storage management plane.

**Technijian staff MUST:**

- **Treat all client backup blobs as opaque ciphertext.** Assume any backup set may contain CUI/FCI and handle it accordingly, regardless of marking visible to Technijian (there generally is none).
- **Preserve the integrity and availability** of stored ciphertext per the backup service commitments.
- **Use least-privilege, MFA-protected access** to the storage and management plane only as required for an assigned task (see §7).
- **Report any suspected exposure of plaintext CUI immediately** — see "report" rule below.

**Technijian staff MUST NOT:**

- **Request, store, or escrow client encryption keys**, or ask the client to share them, under any circumstances.
- **Attempt to decrypt, mount, open, or inspect the contents** of client CUI/FCI backups.
- **Copy, export, or move client backup data outside the TPX storage target** (no local copies, no personal devices, no unsanctioned cloud, no email of backup data).
- **Re-classify, re-mark, or alter** client data or its markings.

**Mandatory reporting.** Any Technijian person who **suspects that plaintext CUI/FCI has become exposed** to Technijian systems or personnel — e.g. an unencrypted backup set arriving at the storage target, a client transmitting plaintext, a key inadvertently shared with Technijian, or any indication that the ciphertext boundary has been breached — **MUST report it immediately** to the Information Security Lead and follow the [Incident Response Plan (IRP)](../Incident_Response_Plan_IRP.md). Such an event is a **scope-breaking event**: it may bring CUI into the Technijian boundary and must be contained, escalated to the affected client, and remediated (including return/secure destruction of any plaintext and re-establishment of encryption) before normal service resumes.

---

## 6. Marking and Labeling

- **Marking is a client responsibility.** Per NARA CUI guidance and the client's contract, the **client** is responsible for identifying, marking, and applying dissemination controls to CUI/FCI **within its own environment, before encryption**.
- **Technijian does not mark, re-mark, or strip markings.** Technijian receives ciphertext in which any markings are inside the encrypted blob and not visible to Technijian.
- **Technijian's role is limited to preserving ciphertext integrity** — Technijian ensures the stored blob is not altered, truncated, or corrupted, so that when the client decrypts the restored data, the original (marked) content is intact.
- For Technijian's own internal records *about* the backup service (job logs, capacity reports, tickets), the **Data Classification and Retention Policy** labeling rules apply ([Data_Classification_Retention_Policy](../Data_Classification_Retention_Policy.md) §3.2). These records describe the service, not the CUI content.

---

## 7. Access Control

- **Least privilege to the storage/management plane.** Access to the QNAP/Nimbus storage targets and their management interfaces is restricted to the minimum set of personnel required to operate the backup service, granted on a need-to-know basis and reviewed periodically.
- **MFA and strong authentication** are required for all administrative access, consistent with the [Access Control Policy](../Access_Control_Policy.md).
- **Segregated CMMC management plane.** Administration of DIB-client backup infrastructure is performed through a **segregated management plane** dedicated to CMMC-scoped work, separated from general-purpose MSP tooling, as defined in [CMMC-020 — CMMC Management Plane](CMMC-020_CMMC_Management_Plane.md). This limits the blast radius of a tooling compromise and keeps the security-protection assets distinguishable from the rest of the MSP environment.
- **Logging and review.** Administrative actions on the storage/management plane are logged and subject to review per the Access Control Policy and the WISP. Cross-client access requires separate authorization.
- **Physical access** to the underlying hardware is controlled by **TPX** at the Irvine data center under its SOC 2 Type II program; Technijian personnel do not require physical access to operate the logical service.

---

## 8. Media Protection and Sanitization

- **Sanitization standard.** Decommissioned storage media that held client ciphertext are sanitized in accordance with **NIST SP 800-88 Rev. 1 "Guidelines for Media Sanitization."** Method is selected by media type (e.g. cryptographic erase / ATA Secure Erase for flash; secure overwrite or physical destruction for HDDs) per the [Data_Classification_Retention_Policy](../Data_Classification_Retention_Policy.md) §5.
- **Cryptographic erasure benefit.** Because the data at rest is already encrypted under a key Technijian never holds, **destruction of the storage does not risk CUI disclosure**; sanitization is performed nonetheless as a media-protection control and to meet the policy baseline.
- **Documentation.** Confidential/Restricted destruction events are documented and retained (date, media identifier, method, performer, witness where required, certificate of destruction) per the Data Classification and Retention Policy §5.3.
- **Decommissioning at TPX.** Where media decommissioning involves the TPX facility, physical destruction and chain-of-custody are handled under TPX's media-handling controls; Technijian obtains a certificate of destruction for outsourced destruction events.

---

## 9. Incident Handling

- **Follow the IRP.** Any suspected or confirmed security event affecting the backup/storage management plane is handled under the [Incident Response Plan (IRP)](../Incident_Response_Plan_IRP.md) — detection, containment, eradication, recovery, and post-incident review.
- **Residual risk of ciphertext exfiltration is limited.** If ciphertext is exfiltrated from Technijian/TPX storage, the **residual confidentiality risk is limited because the client holds the keys** and Technijian cannot decrypt — the exfiltrated blob is not usable CUI without the client's key. This does **not** waive the incident process: the event is still triaged, contained, documented, and communicated to the affected client, and integrity/availability impacts are assessed.
- **Plaintext-exposure events are escalated.** A suspected **plaintext** CUI/FCI exposure (per §5) is treated as a high-severity, scope-breaking incident.
- **Regulatory reporting obligations.** **DoD / DFARS rapid (72-hour) cyber-incident reporting is the client's obligation as the DIB contractor.** Technijian's role is to **support** the client — provide timely notification, forensics support, and evidence — within the timelines in the IRP and the client's contract. Technijian also meets its own client-notification commitment (notify the affected client within 24 hours of confirming a breach involving client data, per the Data Classification and Retention Policy §6.4). [VERIFY] exact client-by-client reporting clocks against each DIB client's SOW/MSA DoD addendum.

---

## 10. Training

- Personnel who touch the **backup/management plane** for DIB clients receive **CUI-awareness training** covering: what FCI and CUI are, the ESP boundary and why Technijian must not decrypt, the MUST/MUST-NOT handling rules in §5, how to recognize a suspected plaintext-exposure event, and the immediate-reporting path.
- Training is completed at onboarding for in-scope roles and refreshed at least annually, consistent with the WISP and the Employee Security Policy. Completion is recorded.
- General security-awareness and acceptable-use training (per the WISP / [Acceptable_Use_Policy_AUP](../Acceptable_Use_Policy_AUP.md)) apply to all staff in addition to this role-specific module.

---

## 11. NIST SP 800-171 Rev 2 Family Mapping

This procedure supports the following NIST SP 800-171 Rev 2 control families. Mapping reflects the controls **Technijian implements as an ESP for the security protection and storage of encrypted client data**; the client remains responsible for control implementation inside its own CUI boundary. Final allocation is recorded in the CRM ([CMMC-004](CMMC-004_Customer_Responsibility_Matrix.md)).

| Family | Representative controls | How this procedure addresses them |
|---|---|---|
| **MP — Media Protection** | 3.8.1, 3.8.2, 3.8.3 (protect/limit access to media; sanitize before disposal) | §8 — NIST SP 800-88 sanitization of decommissioned storage; ciphertext-at-rest; integrity preservation. |
| **SC — System & Communications Protection** | 3.13.8, 3.13.10, 3.13.11, 3.13.16 (encrypt CUI in transit and at rest; key management; FIPS-validated cryptography) | §4 — FIPS 140-2/3 validated AES-256 at the client boundary; TLS 1.2+ in transit; client-held keys; ciphertext at rest. |
| **AC — Access Control** | 3.1.1, 3.1.2, 3.1.3, 3.1.5 (limit access; least privilege; control flow; separation) | §5, §7 — least-privilege MFA access to the storage/management plane; segregated CMMC management plane; no copying data outside the storage target. |
| **MA — Maintenance** | 3.7.1, 3.7.2, 3.7.5 (perform maintenance with controls; control maintenance tools; MFA for nonlocal maintenance) | §7 — segregated management plane, MFA, logged administrative actions; [VERIFY] mapping to specific maintenance procedures. |
| **IR — Incident Response** | 3.6.1, 3.6.2 (incident-handling capability; track and report incidents) | §9 — IRP-driven handling; client notification; support for the client's DoD 72-hour reporting. |
| **AT — Awareness & Training** | 3.2.1, 3.2.2 (security awareness; role-based training) | §10 — CUI-awareness training for in-scope roles, refreshed annually. |
| **AU — Audit & Accountability** | 3.3.1, 3.3.2 (create/retain audit logs; trace actions to users) | §7 — logging and review of management-plane actions; retention per Data Classification and Retention Policy. |

> Control IDs are provided as a cross-reference aid. The authoritative, per-control responsibility allocation (Technijian / Shared / Client) lives in the **Customer Responsibility Matrix** and the client's **SSP**.

---

## 12. References

**Internal — Technijian compliance set:**

- [Information Security Program (WISP)](../Information_Security_Program_WISP.md) — parent program; this procedure is a WISP addendum (esp. WISP §5, Data Classification).
- [CMMC-019 — CUI Scope Position Statement](CMMC-019_CUI_Scope_Position_Statement.md) — the controlling scoping assumption.
- [CMMC-004 — Customer Responsibility Matrix](CMMC-004_Customer_Responsibility_Matrix.md) — per-control Technijian/Shared/Client allocation. [VERIFY] filename when CRM is authored.
- [CMMC-020 — CMMC Management Plane](CMMC-020_CMMC_Management_Plane.md) — segregated administration of DIB-client infrastructure. [VERIFY] filename when authored.
- [Data Classification and Retention Policy](../Data_Classification_Retention_Policy.md) — classification, handling, retention, NIST SP 800-88 sanitization.
- [Access Control Policy](../Access_Control_Policy.md) — least privilege, MFA, logging, access review.
- [Incident Response Plan (IRP)](../Incident_Response_Plan_IRP.md) — detection through post-incident review; notification timelines.
- [Acceptable Use Policy (AUP)](../Acceptable_Use_Policy_AUP.md) — general-staff acceptable-use and awareness.
- [TPX data center references](../tpx-dc) — physical/environmental controls relied upon (SOC 2 Type II).

**External — authorities:**

- NIST SP 800-171 Rev 2 — *Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations.*
- NIST SP 800-88 Rev. 1 — *Guidelines for Media Sanitization.*
- FAR 52.204-21 — *Basic Safeguarding of Covered Contractor Information Systems* (FCI).
- 32 CFR Part 2002 / NARA CUI Registry — CUI categories and marking.
- CMMC 2.0 program guidance and DFARS 252.204-7012 (cyber-incident reporting) — applicable to the client as the DIB contractor.

---

### Version history

| Ver | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-19 | Technijian InfoSec | Initial draft for principal approval. |

---

**Technijian, Inc.**
18 Technology Drive, Suite 141, Irvine, CA 92618

*This document is the property of Technijian, Inc. and is classified Internal — provided to clients and assessors under NDA. Unauthorized distribution or reproduction is prohibited.*
