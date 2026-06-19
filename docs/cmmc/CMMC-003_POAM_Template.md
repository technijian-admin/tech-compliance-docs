# Technijian, Inc.

# Plan of Action & Milestones (POA&M) Template — NIST SP 800-171 Rev 2

**Document ID:** TJN-CMMC-003
**Owner:** Technijian Corporation (Information Security)
**Classification:** Internal — provided to clients and assessors under NDA
**Status:** DRAFT for principal approval
**Version:** 0.1 (2026-06-19)
**Related:** CMMC-100 (Client-Support Program); CMMC-004 (Customer Responsibility Matrix); CMMC-019 (CUI Scope); CMMC-001 (the sibling SSP template)

---

## 1. Purpose & how to use

A **Plan of Action & Milestones (POA&M)** is the companion to the **SSP ([CMMC-001](./CMMC-001_System_Security_Plan_Template.md))**. Where the SSP records what **is** implemented, the POA&M records every **NIST SP 800-171 Rev 2 requirement that is not yet fully met** and tracks it **to closure** with concrete remediation actions, milestones, owners, and dates.

**Ownership and division of labor:**

- **The client owns this POA&M.** The client (the **Organization Seeking Assessment / OSA**) is responsible for its accuracy and for driving items to closure. The client **approves** it (Section 6).
- **Technijian assists** as the client's **MSP / External Service Provider (ESP)** — helping author remediation actions, supplying status for items Technijian operates or shares, and providing supporting evidence. **Technijian is not CMMC-certified**; Technijian helps the client meet CMMC / NIST SP 800-171.
- **Responsibility for each item** (Client / Technijian / Shared / Inherited) follows the **CRM ([CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md))**. The owner field below must match the CRM allocation.

**How to use it:**

1. For every control marked anything other than **Implemented** / **Inherited** / **N/A** in the SSP (Section 6 of [CMMC-001](./CMMC-001_System_Security_Plan_Template.md)), create a row in the **POA&M register** (Section 2).
2. Fill every field. Mark client-specific gaps as **[CLIENT TO COMPLETE]** and engagement-dependent details as **[VERIFY]**.
3. Assign each item a **severity** (Section 3) to prioritize remediation.
4. Record realistic **milestones with dates** and a **scheduled completion** date, and update **status** as work progresses.
5. **Review monthly** (Section 4). When an item is fully remediated and evidenced, mark it **Closed** and reflect the change back in the SSP and, if applicable, the **SPRS score** (Section 5).
6. Keep the POA&M, SSP, CRM, and **WISP ([../Information_Security_Program_WISP.md](../Information_Security_Program_WISP.md))** consistent.

> ⚠️ **Open POA&M items carry risk and affect eligibility.** Not all requirements are POA&M-eligible at assessment time, and POA&M items must be **closed within the timeframe allowed by the applicable CMMC rule** (commonly 180 days). **[VERIFY]** current eligibility limits and the closure window against the governing rule and your contract before relying on a POA&M for any requirement.

---

## 2. The POA&M register

Track every not-yet-met requirement here. The illustrative rows below are marked **EXAMPLE** to show the expected format — **delete them** and replace with real items. A **blank template row** follows for copy/paste.

| Item ID | Control / Objective | Weakness / Gap | Severity | Remediation action | Resources required | Milestones (with dates) | Responsible owner | Scheduled completion | Status | Compensating control |
|---|---|---|---|---|---|---|---|---|---|---|
| **EXAMPLE-001** | 3.5.3 — Multifactor authentication | MFA enforced for remote VPN but **not** for privileged local console logons on two admin servers | High | Deploy MFA to privileged local logons; update IdP conditional-access policy; validate on all admin accounts | IdP admin time; MFA license seats; change window | M1: scope admin accounts (2026-07-15); M2: pilot MFA (2026-08-01); M3: enforce all (2026-08-20) | Client ISSO (Technijian assists) | 2026-08-31 | In progress | Privileged logons restricted to a jump host with logging until MFA enforced |
| **EXAMPLE-002** | 3.3.1 — Audit logging | Endpoint logs retained 14 days; requirement/policy is 90 days | Medium | Forward endpoint logs to centralized log store with 90-day retention | SIEM/log-store capacity; agent rollout | M1: stand up retention tier (2026-07-30); M2: roll out agents (2026-08-30) | Shared (Client + Technijian for Technijian-operated systems) | 2026-09-15 | Open | Daily manual log export to secured share pending centralization |
| **EXAMPLE-003** | 3.14.1 — Flaw remediation | No documented patch SLA for third-party applications | Low | Define and adopt patch-management SLA; integrate app patching into RMM | Policy author time; RMM configuration | M1: draft SLA (2026-07-20); M2: approve + enable RMM policy (2026-08-10) | Client (Technijian RMM support) | 2026-08-15 | Open | Critical app patches applied ad hoc within 7 days during interim |
| [CLIENT TO COMPLETE] | [CLIENT TO COMPLETE] (e.g., 3.x.x) | [CLIENT TO COMPLETE] | [CLIENT TO COMPLETE] (Critical/High/Medium/Low) | [CLIENT TO COMPLETE] | [CLIENT TO COMPLETE] | [CLIENT TO COMPLETE — milestone + date] | [CLIENT TO COMPLETE — per [CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md)] | [CLIENT TO COMPLETE — date] | Open / In progress / Closed / Risk-accepted | [CLIENT TO COMPLETE or "None"] |

**Field guidance:**

- **Item ID** — stable unique identifier (e.g., POAM-001). Never reuse a closed ID.
- **Control / Objective** — the NIST 800-171 Rev 2 control (and objective letter, if relevant) the gap maps to. Must trace to a control in the SSP.
- **Weakness / Gap** — what specifically is not met today.
- **Severity** — per Section 3.
- **Remediation action** — the concrete fix.
- **Resources required** — budget, licenses, staff/Technijian effort, change windows.
- **Milestones (with dates)** — interim checkpoints, each with a target date.
- **Responsible owner** — the accountable party, consistent with the **CRM**.
- **Scheduled completion** — the target closure date. **[VERIFY]** it is within the rule-allowed window.
- **Status** — Open / In progress / Closed / Risk-accepted (with justification).
- **Compensating control** — the interim measure reducing risk until closure ("None" if absent).

---

## 3. Severity & prioritization guidance

Assign severity from the **risk to CUI** (likelihood x impact). When the contract or assessment methodology assigns point values to requirements, weight those higher-value requirements up.

| Severity | Meaning | Indicative target window | Examples |
|---|---|---|---|
| **Critical** | Direct, exploitable exposure of CUI; or a foundational control absent | Immediate / shortest window | CUI reachable without authentication; no encryption on a CUI store |
| **High** | Significant control gap materially raising risk to CUI | Short | MFA gaps on privileged access; major logging gaps |
| **Medium** | Partial implementation; meaningful but contained risk | Moderate | Short log retention; incomplete baseline configs |
| **Low** | Minor/administrative gap; limited direct risk | Longer (still within rule window) | Missing documented SLA; cosmetic policy gaps |

Prioritization rules:

1. **Critical/High first**, then by **scheduled completion** date.
2. Weight requirements that carry **higher SPRS point values** upward (Section 5).
3. Prefer items that **unblock** others (e.g., centralized logging that satisfies multiple controls).
4. Track **compensating controls** for any item that cannot be closed quickly, so interim risk is explicit.

---

## 4. Review & governance cadence

- **Monthly review (minimum).** The client's **ISSO / Security POC** reviews the full register at least monthly: update status, confirm milestone progress, re-date slipped items (with reason), close completed items (with evidence), and escalate at-risk items. **[VERIFY]** whether the contract mandates a more frequent cadence.
- **Participants.** Client ISSO/Security POC (chair) and system owner; **Technijian** for shared/Technijian-operated items; the **authorizing official** for risk-acceptance decisions.
- **Technijian's role.** Technijian provides current status and evidence for shared/inherited items and assists with remediation it operates — but the client owns the register and its closure.
- **Evidence on closure.** Do not mark an item **Closed** without artifacts demonstrating the control is implemented and effective; retain them for assessment.
- **Traceability.** Every status change must remain consistent with the **SSP ([CMMC-001](./CMMC-001_System_Security_Plan_Template.md))** and the **CRM ([CMMC-004](./CMMC-004_Customer_Responsibility_Matrix.md))**; reflect closures in the SSP control status and, where applicable, in **SPRS** (Section 5).

---

## 5. Relationship to SPRS score

The client's **NIST SP 800-171 self-assessment score** (reported in the **Supplier Performance Risk System, SPRS**) is derived from the implemented controls: the assessment starts at the maximum and **deducts the weighted point value of each requirement not fully met**.

- **Open POA&M items lower the score.** Every requirement carried on the POA&M is a not-met requirement and **reduces the SPRS score** until it is closed; closing items **raises** the score.
- **Update SPRS as items close.** When remediation closes an item, update the SSP and **re-submit / update the SPRS score** per the governing process. **[VERIFY]** the current submission mechanics and required score thresholds against your contract.
- **Point weighting drives priority.** Because requirements carry different point values, prioritize closing the **highest-weighted** open items to raise the score fastest (see Section 3).
- **Eligibility caveat.** Some requirements may **not** be POA&M-eligible at assessment, and conditional status may require the score and POA&M to meet rule-specific thresholds. **[VERIFY]** against the applicable CMMC rule. This document does not assert a specific threshold or score.

---

## 6. Approval

By signing, the client confirms this POA&M accurately reflects the open gaps and remediation plan for the system described in the SSP, and accepts ownership of driving these items to closure. Technijian's signature, where provided, attests only to the accuracy of Technijian-provided (shared/inherited) status entries — **not** to CMMC certification of the client.

| Role | Name | Signature | Date |
|---|---|---|---|
| **System owner (Client)** | [CLIENT TO COMPLETE] | ________________ | __________ |
| **ISSO / Security POC (Client)** | [CLIENT TO COMPLETE] | ________________ | __________ |
| **Authorizing official (Client)** | [CLIENT TO COMPLETE] | ________________ | __________ |
| **Technijian (ESP) — for shared/inherited entries only** | [VERIFY] | ________________ | __________ |

---

### Version history

| Ver | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-19 | Technijian InfoSec | Initial client-fillable template for principal approval |
