# CMMC Scope Position Statement — No CUI on Technijian Systems

**Document ID:** TJN-CMMC-019
**Owner:** Technijian Corporation (Information Security)
**Classification:** Internal — provided to clients and assessors under NDA
**Status:** DRAFT for principal approval
**Version:** 0.1 (2026-06-15)
**Related:** Feeds the NIST SP 800-171 SSP ([[CMMC-001]]), the Customer Responsibility Matrix ([[CMMC-004]] / [[CMMC-021]]), the MSA/SOW DoD addendum ([[CMMC-016]]), and the WISP CUI addendum ([[CMMC-005]]).

---

## 1. Purpose

This statement establishes Technijian's authoritative position on the handling of Controlled Unclassified Information (CUI) within Technijian-operated systems. It is the **governing scoping assumption** for every downstream CMMC / NIST SP 800-171 artifact: the System Security Plan (SSP), the Customer Responsibility Matrix (CRM), tooling configurations, and CRM entries. Where any downstream document is silent or ambiguous, this statement controls.

## 2. Scope Position (the controlling statement)

> **Technijian does not store, process, or transmit Controlled Unclassified Information (CUI) in plaintext on any Technijian-operated system.** The only client data that reaches Technijian-operated infrastructure (the Technijian data center) in connection with CUI is **encrypted backup ciphertext**, for which **the client retains sole control of the encryption keys**. Technijian has **no access to the means of decryption** and therefore **cannot read, render, or reconstitute** any CUI contained in that ciphertext.

Because Technijian cannot decrypt the data, Technijian's systems are not a CUI processing, storage, or transmission environment. Technijian acts as an **External Service Provider (ESP)** that provides **security protection and backup/storage of encrypted data only**.

## 3. Technical basis

1. **Client-held keys.** Encryption keys for client CUI are generated and retained by the client (or a client-controlled KMS). Keys are not escrowed with, accessible to, or recoverable by Technijian.
2. **Encryption before transit.** Data is encrypted at the client boundary (AES-256) prior to transmission to the Technijian data center. Data in transit is additionally protected with TLS 1.2+.
3. **Ciphertext at rest.** Backups reside on Technijian storage solely as ciphertext. Without the client key, the contents are not recoverable by Technijian personnel or systems.
4. **No decryption capability.** Technijian operates no process, service account, or tooling capable of decrypting client CUI backups. Restoration delivers ciphertext to the client, who decrypts within their own boundary.

## 4. CMMC / NIST SP 800-171 implications

- **Asset categorization (CMMC Assessment Scope, Level 2):** Technijian-operated systems holding only client-key-encrypted ciphertext are treated as **Security Protection Assets / Contractor Risk-Managed Assets**, *not* CUI Assets, because they do not store, process, or transmit CUI in usable form.
- **ESP without CUI access:** Consistent with DoD guidance that a service provider storing only encrypted CUI to which it has **no access to the decryption keys** is not thereby processing or storing CUI, Technijian's role is limited to that of a security-protection/backup ESP.
- **What Technijian still owns:** The controls that protect the *availability and integrity* of the backup service and the *security protection* it provides (access control to Technijian systems, logging, physical security of the DC, personnel screening, etc.). These are documented in the CRM as Technijian or Shared responsibilities.
- **What Technijian does not own:** Marking, handling, and protection of CUI in plaintext within the client's own environment — those remain **Client** responsibilities in the CRM.

> ⚠️ **Assessor validation required.** Asset categorization and the "encrypted-with-no-key-access = not CUI handling" position must be confirmed with the client's C3PAO during each engagement; interpretations vary by assessor. This statement records Technijian's position and technical basis to support that determination — it is not a substitute for the assessor's scoping decision.

## 5. Boundaries

| In scope for Technijian | Out of scope for Technijian |
|---|---|
| Security protection of the backup service | Decryption or use of client CUI |
| Physical/logical security of Technijian DC and admin access | CUI marking/handling inside client environment |
| Integrity/availability of stored ciphertext | Custody of client encryption keys |
| Personnel screening, logging, IR for Technijian systems | Client's own SSP control implementation for CUI Assets |

## 6. Review & change control

Reviewed at least annually and upon any material change to the backup architecture, key-management model, or DoD/CMMC rule guidance. Changes require re-approval by the Technijian principal below. Version history maintained at the end of this document.

## 7. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Principal / CEO | Ravi Jain | ________________ | __________ |
| Information Security Lead | ________________ | ________________ | __________ |

---

### Version history
| Ver | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-15 | Technijian InfoSec | Initial draft for approval |
