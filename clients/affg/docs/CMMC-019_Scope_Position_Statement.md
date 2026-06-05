# Technijian CMMC Scope Position Statement
**Document ID:** CMMC-019  
**Version:** 1.0  
**Date:** June 4, 2026  
**Owner:** Ravi Jain, CEO  
**Classification:** Internal / Client-Distributable  
**Portal Ticket:** #1459371  

---

## 1. Purpose

This document states Technijian's formal architectural position with respect to Controlled Unclassified Information (CUI) and Federal Contract Information (FCI) under the Cybersecurity Maturity Model Certification (CMMC) framework and DFARS 252.204-7012/7021.

Every tool configuration, Customer Responsibility Matrix (CRM), System Security Plan (SSP), and client engagement must preserve the invariant defined in Section 3 of this document.

---

## 2. Background

Technijian is an IT Managed Service Provider (MSP) headquartered in Irvine, California. Technijian provides managed IT services, cybersecurity monitoring, backup and disaster recovery, and remote endpoint management to commercial and regulated-industry clients, including clients that are DoD contractors or subcontractors subject to DFARS 252.204-7012 and CMMC requirements.

Technijian is **not** a Certified Third-Party Assessment Organization (C3PAO) and has **not** undergone a CMMC Level 2 certification assessment as of the date of this document. Technijian is pursuing registration as a Registered Provider Organization (RPO) with the Cyber AB to demonstrate verifiable CMMC competency to DoD-adjacent clients.

---

## 3. Scope Position — The Architectural Invariant

> **Technijian does not store, process, or transmit Controlled Unclassified Information (CUI) or Federal Contract Information (FCI) on its own systems.**

The only client data that reaches Technijian's infrastructure is **encrypted backup ciphertext**:

- Backup data is encrypted at the source (on the client's systems or at the client's network boundary) using a FIPS 140-2/3 validated cryptographic module **before** transmission to Technijian storage.
- The encryption key is held exclusively by the client. Technijian does not have, manage, or have access to the client's encryption key.
- Technijian's storage target (QNAP/Nimbus infrastructure in the TPX data center, Irvine, CA) receives and stores opaque, encrypted blobs. Without the client-held key, this data cannot be read, decrypted, or accessed by Technijian or any third party with access to Technijian's storage.
- Technijian physically and logically **cannot decrypt** client backup data.

This ciphertext-only architecture means:

| Question | Answer |
|---|---|
| Does Technijian store CUI? | No |
| Does Technijian process CUI? | No |
| Does Technijian transmit CUI? | No (only encrypted ciphertext is transmitted) |
| Can Technijian read client backup data? | No (client holds the key) |
| Is Technijian an External Service Provider (ESP) within a client's CMMC boundary? | Yes — as a Security Protection Asset provider (RMM, remote management tools) |
| Does Technijian's ESP role put its own systems in CUI scope? | No, provided this invariant is preserved |

---

## 4. How Technijian Appears in a Client's CMMC Assessment

Under 32 CFR Part 170 and the CMMC final rule, Technijian's services touch the following CMMC asset categories within a DoD contractor's environment:

**Security Protection Assets (SPA):**  
Technijian's Remote Monitoring and Management (RMM) tool (ScreenConnect / ConnectWise Control), patch management platform (ManageEngine Endpoint Central), and SIEM/EDR monitoring capabilities are Security Protection Assets — they protect or monitor CUI assets, but do not directly store or process CUI themselves. These assets fall within the DoD contractor's CMMC assessment scope as Security Protection Assets.

**Contractor Risk Managed Assets (CRMA):**  
Technijian-managed assets that do not meet the criteria for CUI Assets or Security Protection Assets, where risk is managed through Technijian's contractual obligations, Customer Responsibility Matrix, and this Scope Position Statement.

**Not in scope:**  
Technijian's own data center infrastructure (TPX), backup storage (QNAP/Nimbus), and corporate M365 tenant, because CUI never reaches these systems in decryptable form.

---

## 5. Conditions That Would Invalidate This Position

This scope position is valid only while the following conditions are continuously maintained. A violation of any condition would pull Technijian's infrastructure into CUI scope and require immediate architectural remediation:

1. **Encryption-before-transmission:** Backup data must be encrypted with the client-held key before leaving the client's environment. If Technijian's backup agent ever transfers unencrypted data to Technijian storage, this position is void for that client.

2. **Client key custody:** The client must hold the encryption key exclusively. If Technijian's key management system (KMS) ever stores or has access to a client backup encryption key, this position is void.

3. **No CUI in logs or telemetry:** Technijian's RMM agents, SIEM log collectors, and monitoring tools must not incidentally capture CUI file contents. Log collection must be scoped to system metadata and events, not file contents. (See CMMC-032 — Recurring CUI Re-Scope Check.)

4. **Segregated management plane:** DoD client environments must be managed through dedicated, segregated access groups (CMMC-ScreenConnect-Operators, CMMC-EC-Technicians, CMMC-Backup-Admins) that are isolated from Technijian's commercial book of business. (See CMMC-020.)

5. **FIPS-validated cryptography:** All cryptographic modules used in the CUI data path must maintain active CMVP certificates. Modules that transition to "Historical" status must be replaced. (See CMMC-029 — CMVP Module Register.)

---

## 6. How to Use This Document

**In client System Security Plans (SSP):**  
Reference this document as the basis for scoping Technijian out of CUI Asset scope while retaining Security Protection Asset status. Include a copy in the client's SSP appendix.

**In the Customer Responsibility Matrix (CRM):**  
This document is the foundational assumption underlying every "Technijian" or "Shared" assignment in the CRM. Any control assignment that contradicts this invariant must be escalated for architectural review before the CRM is finalized.

**In contract addenda:**  
Reference Section 3 in the Technijian DoD-Client MSA/SOW Addendum (CMMC-016) to establish contractual recognition of this scoping model.

**In C3PAO assessments:**  
Provide a copy to the C3PAO assessor at the outset of each client CMMC assessment. This document defines the boundary between what the client must demonstrate and what Technijian demonstrates on the client's behalf.

---

## 7. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| CEO / Authorized Representative | Ravi Jain | _________________ | __________ |
| Security Officer | Rishad Mohamed | _________________ | __________ |

---

## 8. Review and Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-04 | Ravi Jain / Claude (Technijian AI) | Initial document |

**Review cadence:** Annually, or immediately upon any material change to Technijian's backup architecture, key management model, or tool stack.
