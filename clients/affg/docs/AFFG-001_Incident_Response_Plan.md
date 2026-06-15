# AFFG Incident Response Plan (IRP)
**Document ID:** AFFG-001  
**Version:** 1.0  
**Date:** June 5, 2026  
**Prepared by:** Ravi Jain, CEO — Technijian  
**Status:** DRAFT — Pending Registered Principal Approval (see AFFG-016)  
**Portal Ticket:** #1459345  
**Regulatory Basis:** SEC Regulation S-P (2024 amendments)  

---

## 1. Purpose and Scope

This Incident Response Plan (IRP) establishes written procedures for American Fundstars Financial Group LLC (AFFG) to detect, respond to, contain, investigate, and recover from security incidents involving unauthorized access to — or reasonably likely unauthorized access to — customer information, as required by SEC Regulation S-P (17 CFR §248.30).

This plan applies to all AFFG systems, personnel, and service providers that store, process, or transmit customer information, including but not limited to:
- Microsoft 365 (email, SharePoint, OneDrive)
- Client account management systems
- Trade execution and order management platforms
- Local and cloud backup systems (Synology NAS, cloud facilities)
- Network infrastructure (Sophos Firewall AFFG-HQ-FW-02)

This plan is integrated with and references AFFG's Business Continuity Plan (BCP) for operational recovery procedures.

---

## 2. Incident Response Team (IRT)

### 2.1 Team Members

| Role | Name | Organization | Email | Office Phone | Cell/After-Hours |
|---|---|---|---|---|---|
| **Incident Response Lead** | Ravi Jain | Technijian (IT Provider) | rjain@technijian.com | 949.379.8499 x201 | 714.402.3164 |
| **AFFG Primary Contact** | Iris Liu | AFFG | iris.liu@americanfundstars.com | [TO VERIFY WITH IRIS] | [TO VERIFY WITH IRIS] |
| **AFFG Emergency Contact** | Fan Feng | AFFG | [TO VERIFY WITH IRIS] | [TO VERIFY WITH IRIS] | [TO VERIFY WITH IRIS] |
| **Technijian Support** | Sai Revanth | Technijian (IRV:TS1) | sravanth@technijian.com | 949.379.8501 | [on-call via portal] |

### 2.2 IRT Responsibilities

**Ravi Jain (Incident Response Lead):**
- Overall incident command and decision-making authority
- Determination of whether a Reg S-P reportable event has occurred
- Authorization of customer notification
- Coordination with AFFG principal and legal counsel
- Liaison with regulators (SEC, FINRA) if required

**Iris Liu (AFFG Primary Contact):**
- Point of contact for all incident communications within AFFG
- Coordination with AFFG management and staff
- Authorization of business decisions during incident response
- Approval of customer notification letters

**Fan Feng (AFFG Emergency Contact):**
- Backup contact when Iris Liu is unavailable
- FINRA Contact System registered emergency contact

**Sai Revanth (Technijian Technical Lead):**
- Technical containment and remediation execution
- Tool management (Huntress, Sophos, Nakivo/Veeam, Umbrella)
- Evidence preservation and forensic data collection
- System restoration and recovery

### 2.3 External Resources

| Resource | Purpose | Contact |
|---|---|---|
| Forensics Firm | Digital forensics and evidence analysis | [TO ESTABLISH — see IRP-005] |
| AFFG Legal Counsel | Regulatory guidance, notification review | [TO VERIFY WITH IRIS] |
| Cyber Insurance Carrier | Coverage activation, breach response services | [TO VERIFY WITH IRIS — see AFFG-017] |
| CISA | Federal cybersecurity resources | cisa.gov / 1-888-282-0870 |
| FBI Cyber Division | Law enforcement (major breaches) | ic3.gov |

---

## 3. Incident Classification

### 3.1 Severity Levels

| Severity | Criteria | Response Time | Examples |
|---|---|---|---|
| **P1 — Critical** | Confirmed unauthorized access to customer information; active attack; ransomware | Immediate (within 1 hour) | Data breach, ransomware, account takeover with data exfiltration |
| **P2 — High** | Suspected unauthorized access; significant system compromise; service provider breach notification received | Within 4 hours | Phishing success, suspicious privileged access, vendor breach |
| **P3 — Medium** | Potential vulnerability; anomalous activity under investigation | Within 24 hours | Failed brute force, anomalous login attempts, Huntress alert without confirmed compromise |
| **P4 — Low** | Security event with no confirmed impact | Within 72 hours | Blocked malware, policy violations, minor misconfigurations |

### 3.2 Reg S-P Trigger Determination

An incident becomes a **Reg S-P reportable event** requiring the 30-day customer notification clock to start when the Incident Response Lead determines that sensitive customer information **was, or is reasonably likely to have been, accessed without authorization**.

Sensitive customer information means any record containing a customer's name combined with: Social Security number, driver's license number, account number, credit or debit card number, or any security code, access code, or password that would permit access to a customer's account.

---

## 4. Detection Procedures

### 4.1 Detection Sources

AFFG's security posture relies on the following Technijian-managed detection capabilities:

| Tool | What It Detects | Alert Routing |
|---|---|---|
| **Huntress (EDR/MDR)** | Endpoint compromise, malware, persistence mechanisms, suspicious process execution | Technijian portal ticket → Sai Revanth → Ravi Jain escalation |
| **Sophos Firewall (AFFG-HQ-FW-02)** | Network intrusions, anomalous traffic, blocked connections, policy violations | Technijian portal ticket → Satish Sharma/team → escalation |
| **Cisco Umbrella** | DNS-layer threats, malicious domain lookups, phishing attempts | Alerts to Technijian monitoring |
| **Microsoft 365 Admin** | Impossible travel logins, bulk email/data access, admin account changes, sign-in failures | Technijian M365 monitoring |
| **Nakivo/Veeam 365** | Backup failures, unusual data growth, encryption indicators | Technijian portal ticket (auto-generated) |
| **Manual Reporting** | Staff-reported suspicious activity, client complaints, vendor notifications | Report to Iris Liu → Ravi Jain |

### 4.2 What Constitutes an Incident

Staff must immediately report to Iris Liu (who notifies Ravi Jain) if they observe:

- Unexpected password reset or account lockout notifications
- Login alerts from unfamiliar locations or devices
- Unusual file access patterns (bulk downloads, access to all client records)
- System behavior suggesting ransomware (encrypted files, ransom notes, inability to access files)
- Phishing email that was clicked or credentials entered
- Receipt of a breach notification from any service provider
- Missing or tampered audit logs
- Unauthorized new user accounts or permission changes
- Any vendor notifying AFFG of a breach involving AFFG customer data

### 4.3 Reporting Contact

**Business hours:** Contact Iris Liu immediately. She will notify Ravi Jain.  
**After hours/weekend:** Contact Ravi Jain directly: cell 714.402.3164.

---

## 5. Containment Protocols

Containment steps are executed by Sai Revanth (Technijian) under direction of Ravi Jain.

### 5.1 Immediate Containment (within 1 hour for P1)

1. **Isolate compromised systems** — Disconnect affected workstations/servers from the network using Huntress remote isolation or manual network disconnection. Do NOT power off (preserves volatile memory evidence).
2. **Revoke compromised credentials** — Force password reset on all suspected compromised accounts via Microsoft 365 Admin Center. Revoke all active sessions.
3. **Block malicious indicators** — Add identified malicious IPs, domains, and file hashes to Sophos Firewall block list and Cisco Umbrella block list.
4. **Disable compromised service provider access** — If a service provider (AT&T, RingCentral, AWS, M365, Synology) is the vector, revoke their access tokens and notify them immediately.
5. **Preserve network traffic logs** — Export Sophos Firewall logs for the relevant time period before any log rotation.
6. **Notify IRT** — Ravi Jain convenes the IRT via phone/email within 30 minutes of P1 determination.

### 5.2 Secondary Containment (within 4 hours)

1. **Enable enhanced monitoring** — Increase logging verbosity on Huntress and Sophos for remaining systems.
2. **Audit all privileged account activity** — Review M365 Admin Center unified audit log for the 30 days prior to incident.
3. **Assess scope of customer data exposure** — Determine which customers, and what data elements, may have been accessed. Document the determination process.
4. **Engage cyber insurance** — Contact AFFG's cyber insurance carrier to notify of potential claim and request breach response services. [CARRIER/POLICY — see AFFG-017]
5. **Engage forensics retainer** — If P1, engage the pre-retained forensics firm for evidence collection and chain-of-custody documentation.

---

## 6. Forensic Investigation Steps

### 6.1 Evidence Preservation (Do Not Delete)

Before any remediation, preserve:
- Forensic images of affected systems (full disk images)
- Memory dumps of live systems where possible
- All relevant logs (Huntress, Sophos, M365 Unified Audit, Nakivo/Veeam)
- Network flow data from Sophos Firewall
- Any malware samples discovered
- All communications related to the incident (emails, chat logs)

**Chain of Custody:** Document every item collected with: item description, collection date/time, collector name, storage location. Use write-blockers for disk images.

### 6.2 Investigation Process

1. **Timeline reconstruction** — Build a chronological timeline of attacker activity from log analysis
2. **Entry point identification** — Determine how the attacker gained access (phishing, credential theft, unpatched vulnerability, insider, vendor compromise)
3. **Lateral movement mapping** — Identify all systems and accounts the attacker accessed after initial entry
4. **Data accessed determination** — Identify specifically which customer records were accessed, read, copied, or exfiltrated. This is the critical determination for Reg S-P notification obligations.
5. **Scope of exposure** — List every customer whose sensitive information was or may have been accessed
6. **Attacker persistence check** — Confirm no backdoors, scheduled tasks, new accounts, or remote access tools remain

### 6.3 Documentation Requirements

Maintain a running incident log throughout the investigation recording:
- All actions taken (with timestamps and person responsible)
- All evidence collected
- All determinations made (and the basis for each)
- All communications (internal and external)

This log is the primary record for Reg S-P compliance and potential regulatory inquiry.

---

## 7. Escalation Matrix

| Situation | Escalate To | Within |
|---|---|---|
| Any Huntress P1/P2 alert | Ravi Jain | 1 hour |
| Any confirmed unauthorized access to customer data | Ravi Jain + Iris Liu | 30 minutes |
| Reg S-P reportable determination | Ravi Jain notifies Iris Liu; Iris notifies AFFG principal | 1 hour |
| 30-day notification clock starts | Ravi Jain logs determination date in incident record | Immediately on determination |
| Customer notification required | Iris Liu approves letter; Ravi Jain coordinates mailing | Within 25 days of determination (buffer before 30-day deadline) |
| Regulatory notification required | Legal counsel + Ravi Jain | Within 48 hours of determination |
| Ransomware/major system loss | Activate BCP; Ravi Jain and Iris Liu jointly | Immediately |
| Service provider breach notification received | Ravi Jain reviews and makes Reg S-P determination | Within 24 hours of receipt |

---

## 8. Evidence Preservation

### 8.1 Minimum 90-Day Preservation

All digital evidence related to a confirmed incident must be preserved for a minimum of **90 days** from the date of incident determination (required for DFARS-adjacent clients; industry best practice for all clients).

### 8.2 Five-Year Record Retention (Reg S-P)

The following records must be retained for **five years** per SEC Regulation S-P:
- This incident response plan and all updates
- All incident reports (whether or not customer notification was required)
- All customer breach notifications sent
- Evidence of the determination that notification was (or was not) required, and the basis
- All testing and exercise results related to this plan

Storage location: [AFFG designated records repository — designate with custodian per AFFG-004]

### 8.3 Malware Samples

Malware discovered during an incident must be preserved in an isolated, quarantined environment for potential submission to law enforcement or CISA.

---

## 9. Eradication Procedures

After containment and investigation are complete:

1. **Remove malware and attacker tools** — Using Huntress remediation and manual removal. Verify with Huntress re-scan.
2. **Patch exploited vulnerabilities** — Deploy patches for any vulnerability used as the attack vector via ManageEngine Endpoint Central. Verify within 24 hours.
3. **Reset all credentials** — Force password reset for all accounts on affected systems. Require new strong passwords and verify MFA is enabled.
4. **Remove unauthorized accounts** — Delete any accounts created by the attacker.
5. **Review and harden configurations** — Correct any misconfigurations identified during the investigation.
6. **Update firewall rules** — Add permanent blocks for all confirmed malicious indicators to Sophos and Umbrella.
7. **Verify backup integrity** — Confirm backup data was not corrupted or encrypted prior to restoring from backups.

---

## 10. Recovery Procedures

1. **Restore from clean backup** — Restore affected systems from the last known-clean Nakivo/Veeam backup. Verify backup integrity before restoration.
2. **Phased reconnection** — Reconnect restored systems to the network in stages, monitoring for re-infection via Huntress.
3. **Validate system integrity** — Confirm applications, data, and access controls are functioning correctly before returning systems to production.
4. **Customer access verification** — Confirm customers can access their accounts and funds/securities (see AFFG-008 procedures).
5. **Enhanced monitoring period** — Maintain elevated monitoring for 30 days post-recovery.

Recovery time objectives are governed by AFFG's BCP (see AFFG-005 and AFFG-006 for backup/system specifications).

---

## 11. Post-Incident Review

Within **30 days** of incident closure:

1. Conduct a post-incident review meeting with the full IRT
2. Document: root cause, timeline, what worked, what failed, gaps in detection/response
3. Update this IRP based on lessons learned
4. Update training materials if staff behavior was a contributing factor
5. File the final incident report in the Reg S-P records repository
6. Present findings to AFFG principal/registered principal

---

## 12. Annual Testing

This IRP shall be tested annually via a tabletop exercise (see AFFG-029 — Annual Reg S-P Incident Response Tabletop). Exercise results must be documented and any identified gaps remediated.

---

## 13. Approval and Version History

| Role | Name | Signature | Date |
|---|---|---|---|
| IT Provider / Incident Response Lead | Ravi Jain, CEO — Technijian | _________________ | __________ |
| AFFG Primary Contact | Iris Liu | _________________ | __________ |
| AFFG Registered Principal | _________________ | _________________ | __________ |

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-05 | Ravi Jain / Technijian | Initial document |

---

*This document satisfies SEC Regulation S-P (17 CFR §248.30) requirement for a written incident response program. It references AFFG's BCP (AFFG-001 through AFFG-020) for operational recovery and the Service Provider Oversight Framework (AFFG-003) for vendor breach procedures.*
