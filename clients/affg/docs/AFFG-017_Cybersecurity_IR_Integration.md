# AFFG Cybersecurity Incident Response Integration
**Document ID:** AFFG-017  
**Version:** 1.0  
**Date:** June 5, 2026  
**Prepared by:** Ravi Jain, CEO — Technijian  
**Status:** DRAFT — Pending Registered Principal Approval (see AFFG-016)  
**Portal Ticket:** #1459361  
**Regulatory Basis:** SEC Regulation S-P (2024 amendments); FINRA Rule 4370; NIST SP 800-61r2  

---

## 1. Purpose and Relationship to Other Documents

This document integrates AFFG's cybersecurity incident response capabilities into the Business Continuity Plan (BCP) framework. It replaces the former vague "Unauthorized Access" section with concrete, tool-specific procedures tied to the security stack Technijian manages for AFFG.

**Document hierarchy:**

| Document | Role |
|---|---|
| **AFFG-001** — Incident Response Plan | Master IR plan: detection → containment → forensics → eradication → recovery. **Go there first for any incident.** |
| **AFFG-002** — Breach Notification Procedures | When and how to notify customers under Reg S-P (30-day clock, letter templates) |
| **AFFG-003** — Service Provider Oversight Framework | Vendor breach notifications, 72-hour clause requirements |
| **AFFG-017** ← *this document* | Cybersecurity-specific control integration: tool configuration, network architecture, law enforcement, cyber insurance |
| **AFFG-005/006** — BCP Recovery Procedures | Operational recovery after a cyber incident (RTO/RPO, system restart sequences) |

---

## 2. Security Control Architecture

### 2.1 Technijian-Managed Security Stack

The following controls are active and managed by Technijian on behalf of AFFG. All alerts route to Technijian's monitoring team before escalation per AFFG-001 Section 4.

| Layer | Tool | Version / Device | Coverage | Alert Routing |
|---|---|---|---|---|
| **Endpoint Detection & Response** | Huntress (EDR/MDR) | Latest — auto-updated | All AFFG endpoints; device LEON confirmed | Portal ticket → Sai Revanth → Ravi Jain |
| **Network Perimeter** | Sophos Firewall | AFFG-HQ-FW-02 | All ingress/egress traffic at main office | Portal ticket → Technijian NOC → Ravi Jain |
| **DNS Security** | Cisco Umbrella | Tenant-wide | All DNS queries from AFFG network + endpoints | Alert → Technijian monitoring |
| **Identity / Cloud** | Microsoft 365 Admin | Tenant-wide | Sign-in anomalies, admin changes, bulk data access | Technijian M365 monitoring → Ravi Jain |
| **Backup Integrity** | Nakivo / Veeam 365 | Job: `Bkp_AFFG365` | M365 data + local backup to Synology NAS | Portal ticket (auto-generated on failure) |
| **Endpoint Management** | ManageEngine Endpoint Central | All endpoints | Patch deployment, software inventory, policy enforcement | Technijian managed |

### 2.2 Coverage Gaps and Known Limitations

The following gaps must be tracked and remediated:

| Gap | Risk | Remediation Owner | Target |
|---|---|---|---|
| Huntress agent coverage drift (LEON only confirmed) | Endpoints without agents are blind spots | Sai Revanth | Verify 100% enrollment — AFFG-022 |
| No SIEM/log aggregation | Correlating events across tools requires manual effort | Ravi Jain | Evaluate in Phase 3 |
| Synology NAS — no remote monitoring agent | Local backup appliance not monitored for unauthorized access | Sai Revanth | Add Technijian monitoring access |
| Email filtering / anti-phishing | No dedicated phishing simulation or mail security tool confirmed | Ravi Jain | Verify M365 Defender ATP status |

---

## 3. Network Architecture and Segmentation

### 3.1 Current Architecture (as of June 2026)

```
Internet
    │
    ▼
Sophos Firewall (AFFG-HQ-FW-02)      ← perimeter control
    │
    ├── AFFG Office LAN
    │       ├── LEON (workstation — Huntress-protected)
    │       ├── Synology NAS DiskStation (local backup)
    │       └── [additional endpoints — verify with Iris]
    │
    └── Cloud Services (via Umbrella DNS protection)
            ├── Microsoft 365 (Exchange, SharePoint, OneDrive)
            ├── AWS (cloud-hosted applications/data — [verify scope with Iris])
            └── RingCentral / AT&T (telecommunications)
```

### 3.2 Segmentation Requirements

| Requirement | Status | Owner |
|---|---|---|
| Backup devices (Synology NAS) isolated from primary LAN | [VERIFY WITH IRIS] | Sai Revanth |
| Guest Wi-Fi separated from corporate LAN | [VERIFY WITH IRIS] | Sai Revanth |
| Admin credentials not shared between systems | [VERIFY WITH IRIS] | Sai Revanth |
| Remote access limited to MFA-enforced VPN or Zero Trust | [VERIFY WITH IRIS] | Ravi Jain |

*Action: Sai Revanth to confirm segmentation status during next on-site visit and document in AFFG-022 (Security Baseline Assessment).*

---

## 4. Multi-Factor Authentication (MFA) Requirements

MFA is mandatory for all AFFG accounts with access to customer data. Non-negotiable minimum:

| System | MFA Required | Current Status | Owner |
|---|---|---|---|
| Microsoft 365 (all users) | Yes | [VERIFY enrollment via M365 Admin → MFA Status report] | Ravi Jain |
| AWS Management Console | Yes | [VERIFY with Iris] | Iris Liu |
| Sophos Central (firewall management) | Yes | Managed by Technijian | Sai Revanth |
| Huntress portal | Yes | Managed by Technijian | Sai Revanth |
| RingCentral admin portal | Yes | [VERIFY with Iris] | Iris Liu |

**During a cybersecurity incident:** MFA enrollment verification is a required step in containment. If any user account involved in an incident lacks MFA, Ravi Jain must be notified immediately for P1 escalation treatment regardless of initial severity classification.

---

## 5. Cyber Insurance

### 5.1 Policy Information

| Field | Value |
|---|---|
| Carrier | [TO VERIFY WITH IRIS] |
| Policy Number | [TO VERIFY WITH IRIS] |
| Claims Contact | [TO VERIFY WITH IRIS] |
| Coverage Type | Cyber liability / data breach response [verify scope] |
| Annual Review Date | [TO VERIFY WITH IRIS] |

*Action: Iris Liu to provide cyber insurance carrier, policy number, and claims contact. This information is referenced in AFFG-001 Section 5.2 (Secondary Containment) and required before AFFG-016 capstone sign-off.*

### 5.2 Incident Notification Trigger

Notify the cyber insurance carrier when **any** of the following occur:

1. A P1 incident is declared (confirmed unauthorized access to customer data)
2. Ransomware is detected on any AFFG system
3. A Reg S-P Notification Determination is made
4. A service provider notifies AFFG of a breach involving AFFG customer data

**Who notifies:** Ravi Jain contacts the carrier within 24 hours of a P1 declaration or Notification Determination.

**What to provide:** Date and time of discovery, brief description of incident, systems affected, estimated scope (if known), point of contact for the carrier.

### 5.3 Breach Response Services via Insurance

Many cyber insurance policies include pre-arranged breach response services. Confirm with carrier whether the policy includes:
- Digital forensics firm (on retainer through carrier)
- Legal counsel specializing in SEC/FINRA breach notification
- Credit monitoring vendor (for affected customers)
- Public relations support

---

## 6. Forensic Investigation Procedures

These procedures supplement AFFG-001 Section 6. They define the specific tools and commands for AFFG's environment.

### 6.1 Evidence Collection Checklist

When a P1 or P2 incident is declared, Sai Revanth collects the following before any remediation:

**Huntress:**
- [ ] Export incident report from Huntress portal (PDF + JSON)
- [ ] Download all process execution logs and file activity logs for affected endpoints
- [ ] Capture Huntress isolation state before re-enabling network access
- [ ] Export any threat hunting results for the 30 days prior to incident

**Sophos Firewall (AFFG-HQ-FW-02):**
- [ ] Export firewall logs for 30 days prior to incident (Sophos Central → Reports → Log Viewer)
- [ ] Export allowed/blocked connection reports
- [ ] Export IPS alerts for the incident period
- [ ] Capture current firewall configuration backup before any changes

**Microsoft 365:**
- [ ] Export Unified Audit Log (M365 Compliance Center → Audit → 90-day window)
- [ ] Export sign-in logs (Entra ID → Sign-in logs → affected accounts)
- [ ] Export mailbox audit logs for affected accounts (Exchange Admin Center)
- [ ] Capture current Azure AD Risky Users report

**Cisco Umbrella:**
- [ ] Export DNS query logs for affected IP addresses (30-day window)
- [ ] Export security events and blocked requests

**Nakivo / Veeam 365:**
- [ ] Export backup job history for `Bkp_AFFG365`
- [ ] Note last successful backup timestamp before incident
- [ ] Check for backup tampering or unusual deletion activity

### 6.2 Chain of Custody

All evidence must be logged with:

| Field | Required |
|---|---|
| Item description | Yes |
| Collection date/time (UTC) | Yes |
| Collected by | Yes |
| Storage location | Yes |
| Hash (SHA-256) for disk images and log exports | Yes |
| Any transfers of custody (date, from, to) | Yes |

Use the chain-of-custody log template in the AFFG-001 incident records repository.

### 6.3 Third-Party Forensics Engagement

For P1 incidents involving confirmed customer data exfiltration or ransomware, engage a third-party forensics firm:

1. Confirm with cyber insurance carrier whether carrier's preferred forensics firm should be used (carriers often require this for coverage)
2. If no carrier-preferred firm: use firm identified in IRP-005 (Forensics Retainer) — **[TO ESTABLISH per AFFG-001 Section 2.3]**
3. Forensics firm must sign an NDA and business associate agreement (if HIPAA-adjacent data is involved) before receiving any evidence
4. All forensic analysis findings are privileged if conducted under direction of legal counsel — **engage AFFG legal counsel before briefing the forensics firm in writing**

---

## 7. Law Enforcement Coordination

### 7.1 Decision Framework

| Condition | Action |
|---|---|
| Ransomware with confirmed data exfiltration | Report to FBI Cyber Division (ic3.gov) and CISA |
| Nation-state or sophisticated persistent threat indicators | Report to CISA (cisa.gov / 1-888-282-0870) |
| Financial fraud (unauthorized account access, fund transfers) | Report to FBI and FinCEN |
| Identity theft of AFFG customers | FTC (reportfraud.ftc.gov) + local FBI field office |
| Any incident meeting FINRA's significant cybersecurity incident threshold | Notify FINRA per Rule 4370 |

**Who makes the decision to contact law enforcement:** Ravi Jain in consultation with Iris Liu and AFFG legal counsel. **Do not contact law enforcement independently without authorization from AFFG principal/legal.**

### 7.2 What to Preserve for Law Enforcement

If law enforcement involvement is anticipated:
- Do NOT wipe, reimage, or destroy any affected systems until law enforcement provides clearance or explicitly waives interest
- Preserve the original infected media separately — restore operations from backup to a *new or imaged clean* system, not the original
- Maintain all communications with attackers (ransom notes, emails) verbatim — do not alter

### 7.3 FINRA Notification (Rule 4370)

AFFG must notify FINRA of a significant cybersecurity incident as soon as practicable. Iris Liu coordinates with AFFG's FINRA compliance counsel. Ravi Jain provides technical incident summary for the notification.

---

## 8. Cybersecurity Controls Integration with BCP

### 8.1 Triggering BCP Activation from a Cyber Incident

A cybersecurity incident activates the BCP when:

| Condition | BCP Activation Level |
|---|---|
| Ransomware encrypting production systems | Full BCP activation — Ravi Jain + Iris Liu jointly |
| M365 tenant compromised or inaccessible | Partial BCP — communications failover procedures |
| Sophos Firewall failure or compromise | Partial BCP — network failover + emergency internet access |
| AWS or cloud provider outage caused by attack | Partial BCP — application failover procedures |
| Synology NAS compromised or encrypted | Partial BCP — recovery from M365 cloud backup only |

### 8.2 Recovery Sequencing After a Cyber Incident

Recovery from a cyber incident follows this sequence to avoid re-infection:

1. **Eradication complete** (AFFG-001 Section 9) — confirmed by Huntress rescan showing clean
2. **Backup integrity verified** — Sai Revanth confirms last known-clean backup from Nakivo/Veeam is restorable and untampered
3. **Restore to clean environment** — restore to reimaged or new hardware where possible; do not restore onto known-compromised systems
4. **Phased reconnection** — reconnect in stages: internal LAN first → M365 → external services; monitor Huntress and Sophos at each stage
5. **MFA verification** — confirm all accounts have MFA re-enrolled before granting user access to restored systems
6. **30-day enhanced monitoring** — Huntress and Sophos maintain elevated alerting thresholds for 30 days post-recovery

For specific system RTO/RPO targets, see AFFG-005 (Backup Specifications) and AFFG-006 (System Recovery Procedures).

---

## 9. Annual Cybersecurity Review

This section of the BCP shall be reviewed and updated annually in conjunction with:

| Review Item | Document | Frequency |
|---|---|---|
| IRP tabletop exercise | AFFG-029 | Annual |
| Security tools coverage audit | AFFG-022 | Annual |
| Vulnerability assessment | AFFG-028 | Annual |
| Service provider oversight review | AFFG-026 | Annual |
| Cyber insurance policy renewal review | This document §5 | Annual (at renewal) |
| Network segmentation verification | This document §3.2 | Annual |

---

## 10. Approval and Version History

| Role | Name | Signature | Date |
|---|---|---|---|
| IT Provider / Author | Ravi Jain, CEO — Technijian | _________________ | __________ |
| AFFG Primary Contact | Iris Liu | _________________ | __________ |
| AFFG Registered Principal | _________________ | _________________ | __________ |

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-05 | Ravi Jain / Technijian | Initial document — replaces vague "Unauthorized Access" section in prior BCP |

---

*Open items requiring Iris Liu input: (1) cyber insurance carrier/policy/claims contact [§5.1]; (2) network segmentation confirmation [§3.2]; (3) AWS scope clarification [§3.1]; (4) complete vendor list verification [AFFG-003]; (5) forensics retainer establishment [IRP-005]. See composed email to iris.liu@americanfundstars.com for all open items.*
