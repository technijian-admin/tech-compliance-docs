# Technijian Corporation

# Incident Response Plan (IRP)

**Version:** 1.0
**Date:** March 6, 2026
**Classification:** Confidential
**Document Owner:** Ravi Jain - CEO/Owner
**Approved By:** Ravi Jain - CEO/Owner
**Next Review Date:** March 6, 2027

---

## 1. Purpose and Scope

The purpose of this Incident Response Plan is to establish procedures for detecting, responding to, containing, eradicating, and recovering from security incidents affecting Technijian Corporation's internal systems or client environments managed by Technijian. This plan ensures a consistent, coordinated, and effective response to minimize damage, reduce recovery time, and meet regulatory and contractual notification obligations.

### 1.1 Scope

This plan covers:

- All Technijian-owned systems, networks, and infrastructure
- All client environments managed or monitored by Technijian
- Employee-issued devices (laptops, workstations, mobile devices)
- BYOD devices enrolled in Technijian MDM
- Cloud services used by Technijian (Microsoft 365, Azure, AWS, SaaS platforms)
- Third-party integrations and vendor connections to Technijian or client systems

### 1.2 Incident Definition

A **security incident** is any event that actually or potentially compromises the confidentiality, integrity, or availability of Technijian's or its clients' information systems or data. Incidents include but are not limited to:

- **Unauthorized Access:** Unauthorized login, privilege escalation, or access to systems or data
- **Data Breach:** Confirmed unauthorized acquisition, access, use, or disclosure of protected data (NPI, PII, PHI, payment card data)
- **Malware Infection:** Virus, trojan, worm, spyware, or other malicious software detected on a system
- **Ransomware:** Encryption of systems or data by malicious actors with a demand for payment
- **Denial of Service:** Attack rendering systems or services unavailable
- **Insider Threat:** Malicious or negligent actions by an employee, contractor, or subcontractor that compromise security
- **Policy Violation:** Intentional or repeated violation of Technijian's Information Security Program or Acceptable Use Policy
- **Lost or Stolen Device:** Loss or theft of a device containing Technijian or client data
- **Credential Compromise:** Exposure of user credentials through phishing, dark web exposure, or other means
- **Social Engineering:** Successful or attempted manipulation of personnel to gain unauthorized access or information
- **Physical Security Breach:** Unauthorized physical access to Technijian facilities or the TPX data center

---

## 2. Incident Response Team

### 2.1 Team Composition

The Incident Response Team (IRT) consists of the following roles:

| Role | Primary | Backup |
|---|---|---|
| **Incident Commander** | Security Officer | Senior IT Operations Lead |
| **Technical Lead** | Senior Engineer | Designated backup engineer |
| **Communications Lead** | Account Manager / Operations Manager | Security Officer |
| **Legal/Compliance Liaison** | External Legal Counsel | Security Officer |
| **Executive Sponsor** | CEO/Founder | Designated executive delegate |

**After-Hours Contact Information:** Maintained in Appendix B. All IRT members must be reachable within 30 minutes during off-hours via phone.

### 2.2 Roles and Responsibilities

**Incident Commander (Security Officer):**
- Leads the overall incident response effort
- Makes containment and escalation decisions
- Determines incident severity and adjusts classification as information evolves
- Coordinates IRT activities and maintains the incident timeline
- Approves external communications and regulatory notifications
- Conducts post-incident review

**Technical Lead (Senior Engineer):**
- Leads technical investigation and forensic analysis
- Implements containment and eradication actions
- Preserves evidence per chain-of-custody procedures
- Provides technical findings and recommendations to the Incident Commander
- Executes recovery procedures and validates system integrity

**Communications Lead:**
- Manages all external communications, including client notifications
- Drafts and distributes status updates using approved templates
- Serves as the single point of contact for affected clients during the incident
- Coordinates with the Legal/Compliance Liaison on regulatory notifications

**Legal/Compliance Liaison:**
- Advises on legal obligations, including regulatory notification requirements
- Reviews client notification content before distribution
- Determines applicability of breach notification laws
- Coordinates with external legal counsel as needed
- Engages with regulators and law enforcement as directed

**Executive Sponsor (CEO):**
- Provides executive authority and resource allocation
- Approves high-impact decisions (e.g., system shutdowns affecting client services, public statements)
- Receives executive briefings at defined intervals
- Interfaces with board of directors or investors if required

### 2.3 External Resources

Technijian maintains pre-arranged relationships with the following external resources:

| Resource | Purpose | Contact Details |
|---|---|---|
| **External Forensics Firm** | Digital forensic investigation, evidence preservation, expert testimony | Maintained in Appendix B |
| **Cyber Insurance Carrier** | Claims process initiation, breach coach assignment, coverage consultation | Policy number and claims hotline in Appendix B |
| **Outside Legal Counsel** | Legal advice on breach notification, regulatory compliance, litigation risk | Maintained in Appendix B |
| **FBI Internet Crime Complaint Center (IC3)** | Federal law enforcement reporting | ic3.gov |
| **FBI Local Field Office** | Federal law enforcement coordination | Contact number in Appendix B |
| **State Attorneys General** | State breach notification filings | Per-state contact list maintained separately |

These relationships are established in advance so that engagement can occur rapidly during an incident without delays for contract negotiation or onboarding.

---

## 3. Incident Classification and Severity

### 3.1 Severity Levels

| Severity | Definition | Examples | Response Timeframe | Escalation |
|---|---|---|---|---|
| **Critical** | Confirmed breach of client data, active ransomware, or widespread system compromise | Exfiltration of client NPI/PHI, ransomware encrypting production systems, active attacker in client environment | Immediate (within 15 minutes) | Full IRT activated immediately. CEO notified within 1 hour. Clients notified within 24 hours of confirmation. |
| **High** | Active intrusion, credential compromise with evidence of use, or significant system compromise | Active unauthorized access, compromised admin credentials being used, large-scale malware outbreak | Within 1 hour | IRT activated. Technical Lead and Incident Commander engaged. CEO notified within 4 hours. |
| **Medium** | Contained malware, policy violation with potential data exposure, or single-system compromise | Malware on single endpoint (contained by EDR), employee accessing unauthorized data, compromised credentials (not yet used) | Within 4 hours | Incident Commander and Technical Lead engaged. Escalation to full IRT if scope expands. |
| **Low** | Failed attack attempt, informational alert, or minor policy deviation | Phishing email received but not clicked, failed brute-force attempt blocked, minor policy deviation without data exposure | Within 24 hours | Logged and investigated by SOC analyst. Escalated if further analysis reveals higher severity. |

### 3.2 Classification Criteria

When classifying an incident, evaluate the following criteria:

- **Data Types Affected:** Is Restricted data (NPI, PHI, PCI) involved? Classification increases with data sensitivity
- **Number of Records:** Larger volumes of affected records increase severity and regulatory obligations
- **Systems Impacted:** Is the incident affecting production systems, client environments, or only internal non-critical systems?
- **Client Impact:** Are clients experiencing service disruption or data exposure?
- **Regulatory Notification Triggers:** Does the incident meet thresholds for mandatory breach notification under HIPAA, state breach notification laws, SEC/FINRA rules, or other regulations?
- **Reputational Impact:** Is there potential for public disclosure or media attention?
- **Active vs. Contained:** Is the threat still active, or has it been contained?

Incidents may be reclassified as new information becomes available. Always classify at the higher level when uncertain.

---

## 4. Detection and Identification

### 4.1 Detection Sources

Security incidents may be detected through the following sources:

| Source | Description |
|---|---|
| **Security Log Review** | Manual review and vendor-native console monitoring across log sources (dedicated SIEM not currently deployed; Huntress SIEM planned within 6 months) |
| **CrowdStrike EDR Alerts** | Endpoint detection and response alerts for malware, suspicious behavior, and exploitation attempts |
| **Dark Web Monitoring** | Alerts when Technijian or client credentials appear on dark web markets, forums, or paste sites |
| **Client Reports** | Clients report suspicious activity, unusual system behavior, or potential incidents |
| **Employee Reports** | Employees report phishing attempts, suspicious emails, lost devices, or policy violations |
| **Vulnerability Scan Findings** | Scan results revealing actively exploited vulnerabilities or critical exposures |
| **Third-Party Notifications** | Notifications from vendors, partners, law enforcement, or security researchers about threats or compromises |
| **Automated Monitoring** | System health monitors, backup failure alerts, and configuration drift detection |

All personnel are trained to recognize and report potential security incidents. Reports can be submitted via email to the security alias, through the ticketing system, or by direct contact with the Security Officer.

### 4.2 Initial Triage

Upon receipt of a security alert or report, the following triage process is executed:

1. **Acknowledgment:** The SOC analyst or on-call engineer acknowledges the alert within **15 minutes** of receipt
2. **Initial Assessment:** Determine whether the event is:
   - A **true positive** (confirmed security event requiring investigation)
   - A **false positive** (benign event incorrectly flagged)
   - **Indeterminate** (requires further investigation to determine)
3. **Severity Classification:** Classify the event per the severity matrix in Section 3.1
4. **Escalation:** Escalate per the severity matrix:
   - Critical/High: Immediately notify the Incident Commander
   - Medium: Notify the Incident Commander within 4 hours
   - Low: Document and route to the investigation queue
5. **Incident Ticket Creation:** If the event is a true positive or indeterminate, create an incident ticket in the tracking system

### 4.3 Threat Intelligence

Technijian integrates threat intelligence from the following sources to improve detection and response capabilities:

- **Vendor Threat Feeds:** CrowdStrike threat intelligence is automatically integrated into endpoint detection rules. Huntress (when deployed) will provide additional managed threat intelligence
- **Industry Advisories:** CISA alerts, MS-ISAC advisories, and vendor security bulletins are monitored by the Security Officer and used to update detection rules and patching priorities
- **Dark Web Monitoring:** Continuous monitoring for credential exposure, data leaks, and threat actor discussions targeting Technijian or its clients
- **Peer Information Sharing:** Threat intelligence is shared with trusted MSP peers and industry groups (e.g., CompTIA ISAO) to improve collective defense
- **Indicator of Compromise (IOC) Management:** IOCs from incidents, threat feeds, and advisories are cataloged and applied to detection systems (firewall rules, EDR custom IOCs, email gateway block lists)

### 4.4 Documentation

All incidents are documented from the moment of first detection:

- **Incident Ticket:** Created in the incident tracking system with a unique identifier
- **Time-Stamped Entries:** Every action, decision, communication, and finding is logged with timestamp, author, and description
- **Evidence Log:** All evidence collected is cataloged with chain-of-custody information
- **Communication Log:** All internal and external communications related to the incident are recorded
- **Decision Log:** All significant decisions (containment actions, escalations, notifications) are documented with the decision-maker, rationale, and timestamp

Documentation is maintained in a secure, access-controlled location. Access to incident records is restricted to IRT members and authorized personnel.

---

## 5. Containment

### 5.1 Short-Term Containment

The objective of short-term containment is to stop the immediate spread and damage of the incident while preserving evidence. Actions are initiated immediately upon classification and include:

- **Isolate Affected Systems:** Disconnect compromised systems from the network (disable network ports, quarantine via EDR, or physically disconnect). Do not power off systems if forensic evidence may be in memory
- **Disable Compromised Accounts:** Immediately disable any accounts confirmed or suspected to be compromised. Force password resets
- **Block Malicious Indicators:** Block known malicious IP addresses, domains, email addresses, and file hashes at the firewall, DNS, email gateway, and endpoint levels
- **Preserve Forensic Evidence:** Before any remediation actions, capture:
  - Disk images of affected systems
  - Memory dumps
  - Relevant log exports
  - Screenshots of indicators of compromise
- **Engage Tier 2:** A senior engineer is engaged within **1 hour** for all Medium, High, and Critical incidents to assist with investigation and containment

### 5.2 Long-Term Containment

If the investigation requires extended time, long-term containment measures are implemented to maintain security while the investigation continues:

- **Clean System Deployment:** Stand up clean replacement systems from known-good images to restore service while compromised systems are investigated
- **Compensating Controls:** Apply temporary controls to address the exploited vulnerability, such as:
  - Additional firewall rules
  - Enhanced authentication requirements
  - Restricted access to affected services
  - Temporary network segmentation changes
- **Enhanced Monitoring:** Increase monitoring on related systems, user accounts, and network segments to detect any expansion of the incident
- **Communication:** Provide regular status updates to the IRT and affected stakeholders per the communication plan

### 5.3 Evidence Preservation

Chain-of-custody procedures are followed for all evidence:

1. **Collection:** Evidence is collected by trained personnel using forensically sound methods
2. **Documentation:** Each piece of evidence is documented with:
   - Description and type
   - Source system and location
   - Date and time of collection
   - Collector's name
   - Collection method
   - Hash values (SHA-256) for digital evidence
3. **Storage:** Evidence is stored in a secure, access-controlled location (encrypted storage with restricted access)
4. **Chain of Custody:** A chain-of-custody log tracks every transfer of evidence, including who handled it, when, and why
5. **External Forensics:** If an external forensics firm is engaged, evidence handoff follows documented chain-of-custody procedures with signed transfer receipts

---

## 6. Eradication

### 6.1 Root Cause Analysis

Once the incident is contained, the Technical Lead conducts a root cause analysis to determine:

- **Attack Vector:** How did the attacker gain initial access? (e.g., phishing email, exploited vulnerability, compromised vendor, stolen credentials, insider action)
- **Exploited Vulnerability:** What specific weakness was exploited? (e.g., unpatched software, misconfiguration, weak credentials, social engineering susceptibility)
- **Lateral Movement:** How did the attacker expand access within the environment?
- **Persistence Mechanisms:** Did the attacker establish persistence (backdoors, scheduled tasks, new accounts, modified configurations)?
- **Data Accessed/Exfiltrated:** What data was accessed, modified, or exfiltrated?

Findings are documented in the incident record and inform both eradication actions and long-term remediation.

### 6.2 Remediation Actions

Based on the root cause analysis, the following remediation actions are taken to remove the threat:

- **Malware Removal:** Remove all identified malicious software, scripts, and artifacts from affected systems
- **Credential Resets:** Reset passwords for all compromised accounts. For widespread compromise, perform organization-wide or domain-wide password resets. Revoke and reissue API keys, tokens, and certificates as needed
- **Vulnerability Patching:** Apply patches or configuration changes to close the exploited vulnerability
- **Configuration Hardening:** Harden system configurations to prevent recurrence (tighten firewall rules, disable unnecessary services, update access controls)
- **Persistence Removal:** Remove any backdoors, unauthorized accounts, scheduled tasks, or other persistence mechanisms
- **Policy Updates:** Update security policies and procedures to address gaps identified during the investigation

**Verification:** Before proceeding to recovery, the Technical Lead verifies that eradication is complete by:
- Scanning affected systems for remaining indicators of compromise
- Reviewing logs for any continued malicious activity
- Confirming that all identified vulnerabilities have been remediated
- Validating that all compromised credentials have been reset

---

## 7. Recovery

### 7.1 System Restoration

Affected systems are restored to normal operation following eradication:

1. **Restore from Clean Sources:** Systems are restored from known-clean backups or rebuilt from trusted images. Backups are verified to pre-date the compromise
2. **Patch and Harden:** Restored systems have all current security patches applied and are hardened per current configuration standards before returning to production
3. **Validation Testing:** Before reconnecting to the production network:
   - Verify system integrity (file checksums, configuration baselines)
   - Confirm all security controls are active (EDR, logging, access controls)
   - Run vulnerability scans to confirm no known vulnerabilities
4. **Staged Return:** Systems are returned to production in a staged manner with enhanced monitoring
5. **Enhanced Monitoring:** Increased monitoring remains in place for a minimum of 30 days after recovery to detect any recurrence

### 7.2 Validation

Recovery is confirmed complete when:

- All affected systems are operating normally and serving their intended functions
- No indicators of compromise remain on any system in scope
- All security controls (EDR, SIEM, firewalls, access controls) are re-enabled and verified functional
- All compromised credentials have been reset and verified
- Backup systems are confirmed operational and completing successfully
- Monitoring has returned to baseline with no anomalous alerts related to the incident

The Incident Commander formally declares the incident resolved and authorizes transition to the post-incident review phase.

---

## 8. Client Notification and Communication

### 8.1 Client Notification

When an incident affects or potentially affects client data or services, Technijian notifies affected clients:

- **Timing:** Initial notification within **24 hours** of confirming an incident that affects client data or services
- **Initial Notification Content:**
  - Description of the incident (what happened, in general terms)
  - Known scope and impact to the client
  - Containment actions already taken
  - Immediate steps the client should take (if any)
  - Next steps and expected timeline for follow-up
  - Point of contact for questions
- **Ongoing Updates:** Status updates are provided at regular intervals (at minimum every 24 hours for Critical incidents, every 48 hours for High incidents) until resolution
- **Resolution Notification:** Final notification includes:
  - Summary of the incident
  - Root cause (at an appropriate level of detail)
  - Full scope of impact
  - Remediation actions taken
  - Steps taken to prevent recurrence
- **Templates:** Pre-drafted notification templates for common incident types are maintained in Appendix A

### 8.2 Regulatory Notification

The Legal/Compliance Liaison determines regulatory notification obligations based on:

| Regulation | Trigger | Timeline | Filing Entity |
|---|---|---|---|
| **HIPAA (HHS/OCR)** | Breach of unsecured PHI affecting 500+ individuals | Within 60 days of discovery | Technijian (as Business Associate, coordinating with Covered Entity) |
| **HIPAA (HHS/OCR)** | Breach of unsecured PHI affecting <500 individuals | Annual log submission | Technijian (coordinating with Covered Entity) |
| **State Breach Notification Laws** | Unauthorized acquisition of PII (varies by state) | Varies by state (typically 30-60 days) | Technijian and/or affected client |
| **SEC / FINRA** | Cybersecurity incident affecting broker-dealer client | Per regulatory guidance | Affected client (Technijian provides supporting documentation) |
| **FTC** | Breach affecting data subject to FTC jurisdiction | As required | Technijian |
| **GDPR (EU DPA)** | Breach affecting EU data subjects | Within 72 hours of awareness | Data controller (Technijian supports as processor) |

All regulatory notifications are reviewed by legal counsel before submission. Copies of all filings are retained in the incident record.

### 8.3 Internal Communication

During an active incident:

- **Need-to-Know:** Information about the incident is shared only with IRT members and personnel who need to know for response purposes
- **Secure Channels:** Use communication channels confirmed to be uncompromised. If corporate email or messaging is potentially compromised, use pre-established alternate channels (personal phones, alternate email accounts)
- **Status Update Cadence:**
  - Critical: Every 2 hours during active response, then every 6 hours
  - High: Every 4 hours during active response, then every 12 hours
  - Medium: Daily updates
- **Management Briefing:** CEO receives briefings per the escalation schedule. Format: situation summary, actions taken, next steps, resource needs, client impact assessment

### 8.4 Media and Public Communication

**Policy:** Technijian does not proactively issue public statements about security incidents unless required by regulation or contractual obligation. All media inquiries are handled exclusively by the CEO/Founder or a designated spokesperson.

**Procedures:**

- **No Unauthorized Statements:** No employee, contractor, or IRT member may speak to the media, post on social media, or make any public statement about an active or resolved security incident without explicit written approval from the CEO/Founder
- **Media Inquiry Routing:** All media inquiries regarding security incidents are immediately routed to the CEO/Founder. Employees receiving media inquiries respond only with: "I am not authorized to comment. Please contact our corporate office at 949-379-8499"
- **Public Statement Approval:** If a public statement is necessary (regulatory requirement, widespread impact, or reputational risk), the statement is:
  1. Drafted by the Communications Lead
  2. Reviewed by the Legal/Compliance Liaison
  3. Approved by the CEO/Founder
  4. Coordinated with affected clients before release
- **Social Media Monitoring:** During active incidents, social media is monitored for public discussion of the incident. Unauthorized disclosures are escalated immediately
- **Post-Incident Public Communication:** If a public statement was issued, a follow-up resolution statement is published after the incident is resolved

### 8.5 Cyber Insurance Claims Process

When an incident may result in an insurance claim, the following process is followed:

1. **Early Notification:** Notify the cyber insurance carrier (Tokyo Marine HCC) as early as possible during a Critical or High severity incident, even before the full scope is known. Early notification preserves coverage options
2. **Breach Coach Assignment:** The carrier assigns a breach coach (attorney) who coordinates forensics, legal, and notification activities under attorney-client privilege
3. **Pre-Approved Vendors:** Use carrier-approved forensics firms and breach notification vendors when possible to ensure cost coverage
4. **Documentation:** Maintain detailed records of all incident-related expenses, including:
   - Forensic investigation costs
   - Legal fees
   - Client notification costs
   - Business interruption losses (lost revenue, overtime, contractor costs)
   - System restoration and remediation costs
5. **Claims Filing:** The Security Officer coordinates with the insurance carrier to file the formal claim, providing all required documentation
6. **Coverage Coordination:** The Legal/Compliance Liaison reviews policy terms to ensure all eligible costs are captured and submitted

**Insurance Contact:** Tokyo Marine HCC, Abigail Billington, 818-479-4330, Policy #H25TG32029-04

### 8.6 Law Enforcement

Law enforcement is engaged when:

- The incident involves suspected criminal activity (theft, fraud, extortion, unauthorized access by external actors)
- Regulatory obligations require law enforcement notification
- The Incident Commander or Legal/Compliance Liaison determines that law enforcement assistance would benefit the investigation or recovery

**Contacts:**
- FBI Internet Crime Complaint Center (IC3): Report filed at ic3.gov
- FBI Local Field Office: Contact information maintained in Appendix B
- Local law enforcement: For physical security incidents

**Coordination:** When law enforcement is involved, the Legal/Compliance Liaison coordinates all interactions. Evidence sharing with law enforcement follows chain-of-custody procedures. Law enforcement requests that may conflict with client obligations or regulatory requirements are reviewed by legal counsel.

---

## 9. Post-Incident Review

### 9.1 Lessons Learned

A post-incident review meeting is conducted within **5 business days** of incident resolution:

**Attendees:** Full Incident Response Team plus relevant stakeholders (affected team members, client account managers, management)

**Agenda:**
1. **Timeline Review:** Walk through the complete incident timeline from detection to resolution
2. **What Worked Well:** Identify effective detection, response, and communication actions
3. **What Could Be Improved:** Identify gaps, delays, miscommunications, or inadequate procedures
4. **Root Cause Discussion:** Review the root cause analysis and validate findings
5. **Improvement Actions:** Define specific, actionable improvements with owners and target dates

**Documentation:** Meeting minutes, attendee list, and the improvement action register are documented and retained in the incident record.

### 9.2 Plan Updates

Based on lessons learned, the following may be updated:

- **This Incident Response Plan:** Revised procedures, updated contact information, improved escalation paths, or new playbooks for scenario types encountered
- **Information Security Program (WISP):** Policy changes to address identified gaps or new risks
- **Technical Controls:** New detection rules, updated firewall rules, hardened configurations, additional monitoring
- **Training:** Targeted training on topics identified as gaps (e.g., phishing awareness, evidence preservation, incident reporting)
- **Vendor Management:** Vendor security requirements or monitoring adjustments based on third-party involvement in the incident

Improvement actions are tracked in the remediation register and reviewed at the next monthly security review until all items are closed.

### 9.3 Incident Report

A formal incident report is produced for each Medium, High, and Critical incident. The report contains:

1. **Executive Summary:** Brief overview of the incident, impact, and resolution (1 page maximum)
2. **Incident Timeline:** Chronological record of events from detection through resolution
3. **Impact Assessment:** Systems affected, data affected, clients affected, service disruption duration, financial impact estimate
4. **Root Cause Analysis:** Detailed root cause findings, attack vector, and exploited vulnerabilities
5. **Actions Taken:** Containment, eradication, and recovery actions in detail
6. **Client Communications:** Record of all client notifications and communications
7. **Regulatory Filings:** Record of any regulatory notifications or filings
8. **Recommendations:** Actions to prevent recurrence and improve response capability

The incident report is reviewed and approved by the Incident Commander and CEO. Reports are retained per the data retention policy (minimum 6 years).

---

## 10. Testing and Maintenance

### 10.1 Tabletop Exercises

Tabletop exercises are conducted at least **annually** to test the Incident Response Plan and the readiness of the IRT:

**Scenarios must include (rotate across exercises):**
- **Ransomware Attack:** Ransomware encrypts Technijian's internal systems and/or client production environment
- **Client Data Breach:** Unauthorized access to client NPI/PHI with potential exfiltration
- **Insider Threat:** Employee or contractor with privileged access acting maliciously or negligently
- **Third-Party Compromise:** Critical vendor breach affecting Technijian's operations or client data

**Exercise Process:**
1. Scenario is presented by the exercise facilitator
2. IRT members walk through their response actions step-by-step
3. Facilitator introduces injects (new information, complications) to test decision-making
4. Discussion of notification obligations, communication actions, and recovery procedures
5. Debrief and identification of gaps and improvements

**Documentation:** Exercise date, participants, scenario, actions discussed, gaps identified, improvement actions, and sign-off are documented and retained for audit.

### 10.2 Incident Playbooks

Technijian maintains scenario-specific playbooks that provide step-by-step response procedures for common incident types. Each playbook is a standalone reference document used by the IRT during an active incident:

| Playbook | Scope | Key Actions |
|---|---|---|
| **Ransomware** | Encryption of systems or data with ransom demand | Isolate, preserve evidence, engage insurance/forensics, restore from clean backups, credential reset, law enforcement reporting |
| **Phishing / Business Email Compromise** | Credential theft or fraudulent transactions via email | Identify affected accounts, disable/reset credentials, block sender/domain, scan for lateral movement, financial transaction reversal if applicable |
| **Insider Threat** | Malicious or negligent actions by trusted personnel | Preserve evidence, restrict access, coordinate with HR and legal, assess data exposure, forensic review of activity logs |
| **Client Data Breach** | Unauthorized access to or exfiltration of client NPI/PHI/PCI data | Scope affected records, engage breach coach, determine notification obligations, coordinate with affected clients, regulatory filings |
| **Third-Party / Supply Chain Compromise** | Vendor breach affecting Technijian or client data | Assess exposure via vendor, isolate vendor connections, reset vendor-related credentials, evaluate data at risk, client notification |
| **Lost / Stolen Device** | Loss or theft of a device containing Technijian or client data | Remote wipe, disable accounts on device, assess data exposure (was encryption active?), report to law enforcement if theft |
| **Denial of Service** | Attack rendering services unavailable | Activate ISP/CDN mitigation, identify attack vector, apply network-level blocks, coordinate with upstream providers, client communication |

Playbooks are reviewed and updated annually, after each tabletop exercise, and after any real incident in which the playbook was used. Playbooks are stored in the controlled document repository accessible to all IRT members.

### 10.3 Plan Review

- **Annual Review:** This plan is reviewed and approved annually by the Security Officer and CEO/Founder
- **Contact Verification:** All contact information in Appendix B is verified **quarterly** to ensure accuracy
- **Out-of-Cycle Updates:** This plan is updated outside the normal review cycle when triggered by:
  - Significant security incidents with lessons learned
  - Organizational changes (new roles, departures of key personnel)
  - Changes in regulatory requirements
  - Results of tabletop exercises identifying gaps
  - Changes in technology, infrastructure, or vendor relationships

### 10.4 Version History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | March 6, 2026 | Ravi Jain | Initial release |
| | | | |
| | | | |

---

## Appendices

### Appendix A: Notification Templates

#### Template 1: Initial Client Notification (Critical/High Incident)

> **Subject: Security Incident Notification - [Client Name]**
>
> Dear [Client Contact],
>
> We are writing to inform you of a security incident that may affect your environment. Technijian's security team detected [brief description of incident] on [date/time].
>
> **What We Know:**
> [Brief description of the incident and known scope]
>
> **Actions Taken:**
> [Summary of containment and response actions]
>
> **Impact to Your Environment:**
> [Known or potential impact to the client]
>
> **Recommended Actions:**
> [Any immediate actions the client should take]
>
> **Next Steps:**
> Our incident response team is actively investigating. We will provide an update within [timeframe].
>
> Please direct any questions to [Communications Lead name] at [contact information].
>
> Sincerely,
> [Name, Title]
> Technijian Corporation

#### Template 2: Status Update

> **Subject: Security Incident Update #[number] - [Client Name]**
>
> Dear [Client Contact],
>
> This is an update regarding the security incident reported on [original date].
>
> **Current Status:** [Contained / Under Investigation / Resolved]
>
> **Update:**
> [Summary of new findings, actions taken since last update]
>
> **Next Steps:**
> [Expected next actions and timeline]
>
> Next update will be provided by [date/time].
>
> [Name, Title]
> Technijian Corporation

#### Template 3: Resolution Notification

> **Subject: Security Incident Resolution - [Client Name]**
>
> Dear [Client Contact],
>
> We are writing to confirm that the security incident reported on [date] has been resolved.
>
> **Summary:**
> [Brief summary of the incident]
>
> **Impact:**
> [Confirmed impact to the client's environment and data]
>
> **Root Cause:**
> [High-level root cause description]
>
> **Remediation:**
> [Actions taken to resolve and prevent recurrence]
>
> We have implemented additional safeguards to prevent similar incidents. A detailed incident report is available upon request.
>
> Please contact [Communications Lead name] at [contact information] with any questions.
>
> Sincerely,
> [Name, Title]
> Technijian Corporation

### Appendix B: Contact List

| Role | Name | Title | Phone (Primary) | Phone (Backup) | Email |
|---|---|---|---|---|---|
| Incident Commander | Ravi Jain | Security Officer / vCISO | 949-379-8499 x201 | 714-402-3164 | rjain@technijian.com |
| Technical Lead | Sai Revanth | Senior Engineer | 949-379-8499 x334 | | srevanth@technijian.com |
| Communications Lead | Alex Alcantar | Operations Manager | 949-379-8499 x226 | | aalcantar@technijian.com |
| Executive Sponsor | Ravi Jain | CEO/Founder | 949-379-8499 x201 | 714-402-3164 | rjain@technijian.com |
| Legal/Compliance | Edward Susolik | External Counsel (Callahan & Blaine) | 714-241-4444 | | ES@Callahan-Law.com |

**External Contacts:**

| Organization | Contact | Phone | Notes |
|---|---|---|---|
| External Forensics Firm (Salvage Data) | George Pavel | 800-972-3282 x220 | gpavel@salvagedata.com — No retainer agreement currently in place |
| Cyber Insurance Carrier (Tokyo Marine HCC) | Abigail Billington | 818-479-4330 | abillington@tmhcc.com — Policy #H25TG32029-04 |
| Outside Legal Counsel (Callahan & Blaine) | Edward Susolik | 714-241-4444 | ES@Callahan-Law.com — Engagement letter on file |
| FBI Local Field Office (Los Angeles) | 11000 Wilshire Blvd., Los Angeles, CA | 310-477-6565 | For cyber incident reporting and law enforcement coordination |
| TPX Data Center NOC | Erica Cuevas | 877-487-8722 | ericka.cuevas@tpx.com — 24/7 support line |

*Contact list is verified quarterly. Last verified: March 7, 2026*

### Appendix C: Severity/Escalation Matrix

```
                    +-----------+-----------+-----------+-----------+
                    |   LOW     |  MEDIUM   |   HIGH    | CRITICAL  |
+-------------------+-----------+-----------+-----------+-----------+
| Initial Response  |  24 hrs   |   4 hrs   |   1 hr    | Immediate |
+-------------------+-----------+-----------+-----------+-----------+
| SOC Analyst       |    Yes    |    Yes    |    Yes    |    Yes    |
+-------------------+-----------+-----------+-----------+-----------+
| Technical Lead    |    No     |    Yes    |    Yes    |    Yes    |
+-------------------+-----------+-----------+-----------+-----------+
| Incident Cmdr     |    No     |    Yes    |    Yes    |    Yes    |
+-------------------+-----------+-----------+-----------+-----------+
| Full IRT          |    No     |    No     |    Yes    |    Yes    |
+-------------------+-----------+-----------+-----------+-----------+
| CEO Notification  |  Weekly   |  24 hrs   |   4 hrs   |   1 hr    |
+-------------------+-----------+-----------+-----------+-----------+
| Client Notify     |    No     | If needed |  24 hrs   |  24 hrs   |
+-------------------+-----------+-----------+-----------+-----------+
| Legal Engaged     |    No     | If needed |    Yes    |    Yes    |
+-------------------+-----------+-----------+-----------+-----------+
| Forensics Firm    |    No     |    No     | If needed |    Yes    |
+-------------------+-----------+-----------+-----------+-----------+
| Law Enforcement   |    No     |    No     | If needed | If needed |
+-------------------+-----------+-----------+-----------+-----------+
| Status Updates    |  Daily    |  Daily    |  4 hrs    |  2 hrs    |
+-------------------+-----------+-----------+-----------+-----------+
| Post-Incident     |  Log only | If Medium+|    Yes    |    Yes    |
| Review            |           |           |           |           |
+-------------------+-----------+-----------+-----------+-----------+
```

---

*End of Document*
