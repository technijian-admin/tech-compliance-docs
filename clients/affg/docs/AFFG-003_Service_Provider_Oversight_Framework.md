# AFFG Service Provider Oversight Framework
**Document ID:** AFFG-003  
**Version:** 1.0  
**Date:** June 5, 2026  
**Prepared by:** Ravi Jain, CEO — Technijian  
**Status:** DRAFT — Pending Registered Principal Approval (see AFFG-016)  
**Portal Ticket:** #1459347  
**Regulatory Basis:** SEC Regulation S-P (2024 amendments), 17 CFR §248.30(a)(1)  

---

## 1. Purpose

SEC Regulation S-P (2024 amendments) requires covered institutions to oversee service providers that access, maintain, or otherwise are permitted to use sensitive customer information. This framework documents AFFG's procedures for managing such providers, including contractual requirements, due diligence, and ongoing monitoring.

---

## 2. Service Provider Inventory

The following vendors have been identified as having access to, or responsibility for, AFFG customer information. **This list must be reviewed and updated at least annually** (see AFFG-026 — Annual Service Provider Oversight Review).

| # | Vendor | Category | Customer Data Access | Primary Contact | Contract in Place? | 72-Hr Breach Clause? |
|---|---|---|---|---|---|---|
| 1 | **AT&T** | Telecommunications | Yes — voice/data transmission | [TO VERIFY WITH IRIS] | [VERIFY] | [VERIFY] |
| 2 | **RingCentral** | Business Communications (UCaaS) | Yes — business phone, voicemail, messaging | [TO VERIFY WITH IRIS] | [VERIFY] | [VERIFY] |
| 3 | **Amazon Web Services (AWS)** | Cloud Infrastructure | Yes — cloud-hosted data/applications | [TO VERIFY WITH IRIS] | [VERIFY] | AWS DPA + BAA if applicable |
| 4 | **Microsoft 365** | Cloud Productivity | Yes — email, documents, calendar, client data | [TO VERIFY WITH IRIS] | Microsoft Customer Agreement | Microsoft DPA in place |
| 5 | **Synology (NAS)** | Local Backup | Yes — backup copies of customer data | Hardware vendor (on-site) | N/A — hardware | [VERIFY cloud component] |
| 6 | **Technijian** | IT Managed Services | Yes — access to manage all above systems | Ravi Jain / Iris Liu | MSA with AFFG | ✅ Included in MSA |

*Note: Verify completeness of this list with Iris Liu. Add any additional vendors with access to customer data (clearing firms, custodians, compliance software, portfolio management platforms, etc.).*

---

## 3. Contractual Requirements

### 3.1 Required Contractual Provisions

All service provider agreements for vendors with access to customer information must include, or be amended to include, the following provisions:

**3.1.1 — 72-Hour Breach Notification**
> *"[Vendor] shall notify American Fundstars Financial Group LLC in writing within seventy-two (72) hours of determining that any Sensitive Customer Information maintained, processed, or transmitted on behalf of AFFG has been, or is reasonably believed to have been, accessed, acquired, or disclosed without authorization. Notification shall be provided to [AFFG designated contact] and shall include: (1) a description of the nature of the incident; (2) the categories and approximate number of customer records involved; (3) the measures taken or planned to address the incident; and (4) the name and contact information of the vendor representative responsible for the incident response."*

**3.1.2 — Security Program Requirements**
> *"[Vendor] shall maintain administrative, technical, and physical safeguards appropriate to the sensitivity of the customer information in its custody, at a level no less protective than the standards set forth in SEC Regulation S-P and applicable NIST guidance."*

**3.1.3 — Right to Audit**
> *"AFFG reserves the right, upon reasonable notice, to audit [Vendor]'s information security practices as they relate to AFFG customer information, or to require [Vendor] to provide a current third-party security audit report (e.g., SOC 2 Type II) upon request."*

**3.1.4 — Data Return and Destruction**
> *"Upon termination of this agreement, [Vendor] shall return to AFFG or securely destroy all AFFG customer information in its possession within [30] days, and provide written certification of destruction."*

### 3.2 Priority Remediation Schedule

The following vendors require immediate contract review to verify or add the 72-hour breach notification clause:

| Priority | Vendor | Action Required | Owner | Target |
|---|---|---|---|---|
| 1 | AT&T | Review contract; add 72-hr clause if missing | Iris Liu / AFFG counsel | 30 days |
| 2 | RingCentral | Review contract; add 72-hr clause if missing | Iris Liu / AFFG counsel | 30 days |
| 3 | AWS | Review DPA for breach notification timeline | Iris Liu / AFFG counsel | 30 days |
| 4 | Microsoft 365 | Microsoft DPA includes breach notification; verify timeline | Ravi Jain | 30 days |
| 5 | Synology | NAS is on-site; if cloud component used, review terms | Ravi Jain | 30 days |

---

## 4. Vendor Due Diligence Procedures

### 4.1 Initial Due Diligence (Before Onboarding a New Vendor)

Before granting any new vendor access to customer information, AFFG and/or Technijian must complete:

1. **Security questionnaire** — Require the vendor to complete a written security questionnaire covering: data encryption practices, access controls, incident response capabilities, subcontractor management, and compliance certifications
2. **SOC 2 report review** — Request the vendor's most recent SOC 2 Type II report (or equivalent audit report). Review auditor opinion and any exceptions
3. **Contract review** — Confirm all required provisions per Section 3.1 are present before execution
4. **Risk rating** — Assign a risk tier based on: volume of customer data handled, sensitivity of data, vendor's security maturity

| Risk Tier | Criteria | Due Diligence Level |
|---|---|---|
| Tier 1 — High | Direct access to large volumes of customer PII/financial data | Full security questionnaire + SOC 2 + contract review |
| Tier 2 — Medium | Indirect access; limited customer data | Abbreviated questionnaire + contract review |
| Tier 3 — Low | No direct customer data access | Contract clause + annual confirmation |

### 4.2 Ongoing Monitoring

| Activity | Frequency | Owner |
|---|---|---|
| Review updated SOC 2 Type II reports from Tier 1 vendors | Annually | Ravi Jain |
| Re-send security questionnaire to Tier 1/2 vendors | Annually | Ravi Jain |
| Verify 72-hr notification clause remains in force | Annually | Iris Liu |
| Update vendor inventory for additions/removals | On change + annually | Iris Liu + Ravi Jain |
| Full annual oversight review (AFFG-026) | Annually | Sai Revanth (operational) |

---

## 5. Receiving and Processing Vendor Breach Notifications

When AFFG receives a breach notification from any service provider:

1. **Log receipt** — Record date and time of notification, vendor name, notification method
2. **Notify Ravi Jain within 24 hours** — Forward the notification immediately
3. **Request additional information** — If the vendor notification does not include all required details (nature of incident, customer records affected, timeframe), request in writing within 24 hours
4. **Reg S-P assessment** — Ravi Jain makes a Notification Determination within 24 hours of receiving complete information (see AFFG-002 Section 3)
5. **Document** — File all vendor notifications and AFFG's response in the Reg S-P compliance records

---

## 6. Vendor Records

The following must be retained for **5 years** per Reg S-P:

- This framework and all updates
- The vendor inventory (annual snapshots)
- Security questionnaire responses from each vendor
- SOC 2 reports obtained from vendors
- Contracts and signed amendments containing the breach notification clause
- All vendor breach notifications received and AFFG's response
- Results of the annual oversight review (AFFG-026)

Storage location: [AFFG designated compliance records repository — designate with custodian per AFFG-004]

---

## 7. Approval and Version History

| Role | Name | Signature | Date |
|---|---|---|---|
| IT Provider / Author | Ravi Jain, CEO — Technijian | _________________ | __________ |
| AFFG Primary Contact | Iris Liu | _________________ | __________ |
| AFFG Registered Principal | _________________ | _________________ | __________ |

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-05 | Ravi Jain / Technijian | Initial document |

---

*Action required: Iris Liu to confirm complete vendor list and initiate contract amendments with AT&T, RingCentral, and AWS to add 72-hour breach notification clauses before AFFG-016 capstone sign-off.*
