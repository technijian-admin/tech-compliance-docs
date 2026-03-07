# Technijian Corporation

# Business Continuity & Disaster Recovery Plan (BCP/DR)

**Version:** 1.0
**Date:** March 6, 2026
**Classification:** Confidential
**Document Owner:** Ravi Jain - CEO/Owner
**Approved By:** Ravi Jain - CEO/Owner
**Next Review Date:** March 6, 2027

---

## 1. Purpose and Scope

The purpose of this Business Continuity and Disaster Recovery Plan is to ensure that Technijian Corporation can continue delivering managed IT services to its clients during and after disruptive events, and recover critical systems within defined Recovery Time Objective (RTO) and Recovery Point Objective (RPO) targets. This plan establishes the framework for maintaining essential business operations, communicating with stakeholders, and restoring normal service delivery as rapidly as possible.

### 1.1 Scope

This plan covers:

- **Technijian Internal Operations:** All internal systems, processes, and personnel required to deliver managed IT services
- **Client Service Delivery:** Monitoring, alerting, helpdesk, infrastructure management, and security operations delivered to clients
- **Infrastructure at TPX Data Center:** Servers, networking equipment, and storage hosted at the TPX colocation facility
- **Cloud Services:** Microsoft 365, Azure, AWS, SaaS platforms (RMM, PSA, SIEM, EDR)
- **Communications:** Phone, email, messaging, and collaboration platforms
- **Personnel:** All Technijian employees, contractors, and key subcontractors

**Disruptive Events Addressed:**

| Event Category | Examples |
|---|---|
| Natural Disasters | Earthquake, flood, wildfire, severe weather, power grid failure |
| Cyberattacks | Ransomware, data breach, denial of service, destructive malware |
| Equipment Failure | Server failure, storage failure, network equipment failure |
| Provider Outages | ISP outage, cloud provider outage, SaaS platform outage |
| Pandemic / Health Crisis | Widespread illness affecting workforce availability |
| Facility Loss | Fire, structural damage, landlord lockout, environmental hazard |

### 1.2 Relationship to Other Plans

This plan operates in conjunction with:

- **Incident Response Plan (IRP):** Security events that escalate to a disaster recovery scenario trigger both plans. The IRP governs the security investigation and containment; this BCP/DR plan governs business continuity and system recovery
- **Information Security Program (WISP):** The security controls in the WISP prevent many scenarios that would otherwise require plan activation. Recovery procedures in this plan adhere to the security standards in the WISP
- **Client-Specific DR Plans:** Individual clients may have their own DR plans with specific requirements. Client-specific RTO/RPO targets and procedures are documented separately and referenced during recovery operations

---

## 2. Business Impact Analysis

### 2.1 Critical Business Functions

Technijian's business functions are ranked by criticality based on their impact to client service delivery and business operations:

| Priority | Function | Description | Impact of Loss |
|---|---|---|---|
| 1 | Client Monitoring & Alerting (RMM) | 24/7 monitoring of client endpoints and infrastructure | Undetected outages, security events, and system failures across all client environments |
| 2 | Helpdesk / Ticket Response | Client support ticket intake, triage, and resolution | Client issues unresolved, SLA violations, client dissatisfaction |
| 3 | Client Infrastructure Management | Active Directory, servers, networking, cloud resources | Inability to manage or remediate client systems |
| 4 | Security Operations (SOC/SIEM) | Security event monitoring, detection, and response | Security threats undetected and unaddressed |
| 5 | Email & Communications | Microsoft 365, phone system, messaging platforms | Internal and client communication disrupted |
| 6 | Billing & PSA | Professional services automation, invoicing, time tracking | Delayed billing, lost revenue tracking, SLA reporting unavailable |
| 7 | Internal File Storage & Documentation | SharePoint, file servers, internal wiki/knowledge base | Reduced efficiency, lost institutional knowledge |

### 2.2 RTO and RPO Targets

Recovery objectives are defined by system tier:

| Tier | Description | RTO | RPO | Examples |
|---|---|---|---|---|
| **Tier 1** | Client production systems | 4 hours | 1 hour | Client servers, Active Directory, critical applications, production databases |
| **Tier 2** | Technijian operational systems | 4 hours | 4 hours | RMM platform, PSA system, SIEM, SOC tooling, VPN infrastructure |
| **Tier 3** | Non-critical systems | 24 hours | 24 hours | Internal file shares, marketing systems, development/test environments, training platforms |

**Important Notes:**
- Client-specific RTO/RPO targets may differ based on individual SLA agreements. Where client SLAs specify tighter targets, those targets take precedence
- RTO is measured from the time the disruption is declared to the time the system is restored to functional operation
- RPO is measured as the maximum acceptable data loss expressed in time (e.g., RPO of 1 hour means no more than 1 hour of data may be lost)

### 2.3 Dependencies

Critical dependencies that must be available for recovery operations:

| Dependency | Provider | Function | Criticality | Alternate |
|---|---|---|---|---|
| Data Center Hosting | TPX | Physical hosting for core infrastructure | Critical | DR environment at Technijian DC |
| Internet / WAN | Primary ISP | Network connectivity | Critical | Secondary ISP with automatic failover |
| Microsoft 365 | Microsoft | Email, Teams, SharePoint, Azure AD | Critical | Alternate communication channels (phone, personal email) |
| RMM Platform (ManageEngine Endpoint Central Plus) | ManageEngine (SaaS) | Client endpoint monitoring and management | Critical | Manual monitoring procedures, direct access |
| CrowdStrike Falcon | CrowdStrike | Endpoint detection and response | High | Endpoint isolation, manual monitoring |
| SIEM Platform (Huntress — planned) | Not currently deployed; Huntress SIEM planned within 6 months | Security log aggregation and alerting | High | Direct log review via CrowdStrike console and vendor-native tools |
| Cloud Platforms | Technijian DC | Client workloads, DR hosting | High | TPX data center |
| Phone System / VoIP (3CX) | 3CX | Client and internal phone communications | High | Mobile phones, Microsoft Teams calling |
| Backup Platform (Veeam) | Veeam | Data backup and recovery | Critical | Local backup copies, manual recovery |

---

## 3. Recovery Strategies

### 3.1 Data Center (TPX) Disruption

**Scenario:** The TPX data center facility is unavailable due to physical damage, environmental failure, extended power outage, or network provider failure.

**Recovery Strategy:**

1. **Assess Duration:** Contact TPX NOC to determine the expected outage duration and scope
2. **Short Outage (< 4 hours expected):** Wait for TPX to restore services using their redundant infrastructure (UPS, generator, redundant cooling, diverse network paths). Monitor TPX status updates
3. **Extended Outage (> 4 hours or indeterminate):**
   - Activate DR environment at Technijian DC
   - Initiate failover of Tier 1 systems using replicated data:
     - Restore virtual machines from replicated images
     - Update DNS records to point to DR environment
     - Verify data integrity against last known-good replication point
     - Test application functionality before declaring services restored
   - Failover Tier 2 systems once Tier 1 is confirmed operational
   - Notify clients per the communication plan
4. **Return to Primary:** Once TPX is restored, plan and execute failback to the primary site during a maintenance window. Verify data synchronization before cutover

**Data Replication Architecture:**
- Tier 1 systems: Continuous replication to Technijian DC DR environment (RPO: 1 hour)
- Tier 2 systems: Replication every 4 hours to Technijian DC DR environment
- Tier 3 systems: Daily backups to geographically separate storage

**TPX DR Capabilities:** TPX's own disaster recovery capabilities are documented in their SOC 2 Type II report (which Technijian relies on for production system assurance), including redundant power (N+1 UPS, diesel generators), redundant cooling, fire suppression, and diverse network connectivity.

### 3.2 Technijian Office / Facility Loss

**Scenario:** Technijian headquarters at 18 Technology Drive, Suite 141 is inaccessible due to fire, flood, structural damage, environmental hazard, or other event.

**Recovery Strategy:**

Technijian operates a remote-first support model. All engineers and support staff are equipped and trained to work remotely. Facility loss does not inherently disrupt client service delivery.

1. **Immediate Actions:**
   - Account for all personnel (confirm safety)
   - Activate remote work for all staff
   - Confirm VPN and remote access infrastructure is operational
   - Verify all engineers can access client environments from remote locations
2. **Alternate Work Locations:**
   - Primary: Home offices (all staff are equipped with laptops, VPN access, and softphones)
   - Secondary: TPX Datacenter (pre-identified alternate work location)
3. **Equipment:**
   - Staff already possess company-issued laptops configured for remote work
   - Spare equipment inventory is maintained off-site for replacement needs
   - Cloud-based tooling (RMM, PSA, M365) is accessible from any location
4. **Communication:**
   - Microsoft Teams remains the primary collaboration platform (cloud-hosted, unaffected by facility loss)
   - VoIP phone system continues functioning via softphone clients
   - Physical mail forwarding arranged with postal service if extended displacement
5. **Physical Assets:** Coordinate with building management and insurance for recovery of on-premises equipment and documents. Engage disaster recovery services if needed for hardware salvage

### 3.3 Cyberattack / Ransomware

**Scenario:** Technijian's own internal systems are compromised by ransomware, destructive malware, or a sophisticated cyberattack.

**Recovery Strategy:**

1. **Activate Incident Response Plan:** The IRP takes precedence for detection, containment, and eradication. This BCP/DR plan governs the business continuity and recovery aspects
2. **Isolate Affected Systems:** Immediately disconnect compromised systems from the network to prevent lateral spread. Preserve evidence per IRP procedures
3. **Assess Scope:** Determine which systems are affected and which remain clean. Identify the attack vector and any persistence mechanisms
4. **Client Communication:** Notify affected clients via alternate channels (phone, personal email) if corporate communication systems are compromised. Use pre-drafted templates from Appendix C
5. **Restore from Clean Backups:**
   - Identify the last known-good backup that pre-dates the compromise
   - Verify backup integrity (checksums, test restoration)
   - Rebuild affected systems from clean images
   - Restore data from verified clean backups
   - Apply all security patches and hardening before reconnecting to the network
6. **Credential Reset:** Perform organization-wide password resets. Revoke and reissue all API keys, tokens, and certificates
7. **Enhanced Monitoring:** Deploy enhanced monitoring and detection rules focused on the identified attack patterns for a minimum of 90 days post-recovery

**Ransomware-Specific Guidance:**
- Do not pay ransoms without executive and legal counsel approval and law enforcement consultation
- Report to FBI IC3 and local FBI field office (Los Angeles: 310-477-6565)
- Engage cyber insurance carrier (Tokyo Marine HCC, Policy #H25TG32029-04) for breach coach and forensics support
- Preserve encrypted files and ransom notes as evidence

### 3.4 Key Personnel Loss

**Scenario:** One or more critical staff members are unavailable due to illness, injury, resignation, or other cause.

**Recovery Strategy:**

1. **Cross-Training:** All critical functions have at least two trained personnel. Cross-training documentation is maintained for each critical role
2. **Backup Personnel Assignments:**

| Critical Role | Primary | Backup | Tertiary |
|---|---|---|---|
| Security Officer / vCISO | Ravi Jain | Rishad Mohammed | External consultant |
| Senior Engineer (Client Infra) | Sai Revanth | Ravi Jain | Rishad Mohammed |
| SOC Analyst (Lead) | Ravi Jain | Sai Revanth | Rishad Mohammed |
| Helpdesk Manager | Aditya Saraf | Ravi Jain | Alex Alcantar |
| Account Manager | Ravi Jain | Alex Alcantar | Rishad Mohammed |

3. **Documentation:** Operational runbooks, client environment documentation, and standard operating procedures are maintained in the knowledge base and accessible to backup personnel
4. **Vendor Escalation:** For specialized skills or surge capacity, pre-arranged relationships with staffing vendors and consulting firms allow rapid augmentation
5. **Minimum Staffing:** The minimum staffing level for continued client service delivery is:
   - At least 1 senior engineer available 24/7
   - At least 1 helpdesk technician during business hours
   - Security Officer or backup available for incident response

### 3.5 Pandemic / Workforce Reduction

**Scenario:** A pandemic, widespread illness, or other event reduces workforce availability below minimum staffing levels defined in Section 3.4.

**Recovery Strategy:**

1. **Activate Remote Work:** All staff transition to full-time remote work immediately. Technijian's remote-first model ensures continuity of client service delivery without physical office access
2. **Workforce Assessment:** Determine the number and roles of available staff. Identify critical gaps against minimum staffing requirements
3. **Prioritize Services:** If staffing falls below minimum levels:
   - Tier 1 client services (monitoring, alerting, critical incident response) are maintained first
   - Tier 2 services (routine maintenance, non-urgent tickets) are deferred or reduced in frequency
   - Tier 3 services (projects, internal initiatives) are suspended
4. **Cross-Training Activation:** Deploy backup and tertiary personnel per Section 3.4 backup assignments
5. **Vendor Augmentation:** Engage pre-arranged staffing vendors and consulting firms for surge capacity. Temporary staff must complete expedited security onboarding before accessing client environments
6. **Client Communication:** Notify clients of any service level adjustments, including revised response times and deferred activities. Provide regular updates on staffing recovery
7. **Health and Safety:** Follow CDC/local health authority guidelines. Do not require staff to report to the office during active health advisories. Provide mental health and wellness resources
8. **Return to Normal:** Gradually restore full service levels as staff return. Prioritize backlog of deferred work by client criticality

**Minimum Viable Operations:**

| Function | Minimum Staff Required | Notes |
|---|---|---|
| Client Monitoring & Alerting | 1 engineer (24/7 rotation) | Automated monitoring reduces manual effort |
| Helpdesk / Ticket Response | 1 technician (business hours) | Prioritize critical tickets only |
| Security Operations | 1 security analyst (on-call) | Automated alerting via CrowdStrike |
| Management / Client Communication | 1 manager | Client updates and escalation decisions |

### 3.6 Vendor/Provider Outage

**Scenario:** A critical vendor or service provider experiences an extended outage affecting Technijian's ability to deliver services.

**Recovery Strategy by Vendor:**

| Vendor/Service | Acceptable Outage | Alternate/Workaround |
|---|---|---|
| **RMM Platform (ManageEngine Endpoint Central Plus)** | 4 hours | Direct RDP/SSH access to client systems. Manual monitoring via ping/SNMP scripts. CrowdStrike console for endpoint visibility. |
| **SIEM Platform (Huntress — planned)** | 8 hours | Direct log review on source systems. CrowdStrike console for endpoint alerts. Manual firewall log review. |
| **Microsoft 365** | 4 hours | Personal email for urgent communications. Phone calls for client contact. Local cached files for document access. Alternate collaboration tool. |
| **ISP (Primary)** | 1 hour | Automatic failover to secondary ISP. Mobile hotspots as tertiary backup. |
| **VoIP/Phone (3CX)** | 2 hours | Microsoft Teams calling. Mobile phones. Client contact via email. |
| **CrowdStrike** | 8 hours | Network-level monitoring via firewall and system logs. Endpoint isolation procedures. Manual log review. |
| **Technijian DC** | 4 hours | Failover to TPX data center. Activate alternate DR infrastructure if available. |

**Process:**
1. Detect the outage via monitoring or vendor notification
2. Assess expected duration from vendor status page and support channels
3. If duration exceeds acceptable threshold, activate the alternate/workaround
4. Notify affected clients if service delivery is impacted
5. Monitor vendor status for restoration
6. Return to normal operations when vendor service is restored and verified stable

---

## 4. Backup Architecture

### 4.1 Backup Strategy

| Tier | Backup Frequency | Backup Type | Destinations | Encryption |
|---|---|---|---|---|
| **Tier 1** (Client production) | Continuous / Hourly | Incremental with daily full | On-site (TPX), Off-site (cloud), Geographically separate cloud region | AES-256 |
| **Tier 2** (Technijian ops) | Every 4 hours | Incremental with daily full | On-site (TPX), Off-site (cloud) | AES-256 |
| **Tier 3** (Non-critical) | Daily | Full with daily incremental | Off-site (cloud) | AES-256 |

**Backup Principles:**
- **3-2-1 Rule:** At least 3 copies of data, on at least 2 different media types, with at least 1 copy off-site and geographically separated
- **Immutable Backups:** Tier 1 and Tier 2 backups include immutable copies that cannot be modified or deleted for a defined retention period (protection against ransomware)
- **Air-Gapped Copies:** Critical backups maintain an air-gapped copy that is physically or logically isolated from the production network
- **Retention:** Backup retention follows the data retention policy in the WISP. Minimum: 30 days of daily backups, 12 months of monthly backups
- **Geographic Separation:** Off-site backups are stored in a geographically separate region (minimum 100 miles from primary site) to protect against regional disasters

### 4.2 Backup Monitoring

- **24/7 Automated Monitoring:** All backup jobs are monitored continuously. The backup monitoring system checks for:
  - Successful completion within expected timeframes
  - Incomplete or partial backups
  - Missed schedules
  - Storage capacity thresholds
  - Replication lag exceeding RPO thresholds
- **Alerting:** Failed, incomplete, or missed backup jobs generate immediate alerts to the on-call engineer
- **Remediation SLA:** Failed backup jobs are investigated and remediated within 4 hours. If a backup cannot be completed within 8 hours, the Security Officer is notified
- **Integrity Verification:** Backup integrity is validated using checksum verification (SHA-256) on a sample of backup files weekly. Full integrity verification is performed monthly
- **Reporting:** Weekly backup status reports are generated and reviewed by IT Operations. Reports include success/failure rates, storage utilization, and any open remediation items

### 4.3 Restoration Testing

Regular restoration testing validates that backups are recoverable and meet RTO/RPO targets:

| Test Type | Frequency | Scope |
|---|---|---|
| **File-Level Restore** | Monthly | Restore individual files from each backup tier. Verify file integrity and content |
| **System-Level Restore** | Quarterly | Restore complete Tier 1 systems to an isolated test environment. Verify system boots, applications function, and data integrity |
| **Bare-Metal Recovery** | Semi-annually | Full bare-metal recovery of a representative system. Measure actual recovery time against RTO target |
| **Full DR Drill** | Annually | Simulate a disaster scenario and execute full recovery procedures. Measure against RTO/RPO targets for all tiers |

**Test Documentation:**
- Each test is documented with: date, tester, systems tested, recovery time achieved, data integrity verified (yes/no), pass/fail against RTO/RPO, and issues identified
- Test results are retained for audit purposes (minimum 3 years)
- Failed tests trigger immediate investigation and remediation. Retesting occurs within 30 days of remediation

---

## 5. Communication Plan

### 5.1 Internal Communication

**Notification Chain During a Disruption:**

1. **Plan Activation:** The CEO/Founder or Security Officer declares plan activation
2. **IRT/BC Team Notification:** IRT members notified immediately via:
   - **Primary:** Microsoft Teams (if available)
   - **Secondary:** Phone tree (each team member calls the next person on the list)
   - **Tertiary:** Personal email (pre-registered personal email addresses)
3. **All-Staff Notification:** Once the BC team is assembled, all staff are notified via the same channel cascade
4. **Status Updates:** Regular status updates provided to all staff during the disruption:
   - Every 2 hours during active recovery
   - Every 6 hours once recovery is stable
   - Resolution notification when normal operations resume

**Emergency Contact List:** Maintained in Appendix B. Includes home/personal phone numbers and personal email addresses for all critical personnel. Verified quarterly.

### 5.2 Client Communication

**Client Notification Procedures During Service Disruption:**

| Phase | Timing | Content | Channel |
|---|---|---|---|
| **Initial Notification** | Within 2 hours of plan activation | What happened (general), which services affected, expected impact, that recovery is in progress | Email + phone for high-priority clients |
| **Status Updates** | Every 4 hours during active recovery | Recovery progress, revised time estimates, any changes to impact scope | Email, status page |
| **Recovery Update** | When recovery milestones reached | Services restored, any residual impact, monitoring status | Email |
| **Resolution** | When normal operations confirmed | Services fully restored, summary of incident, prevention measures | Email |

- **Communication Channels:** Email (primary), phone (for urgent/high-priority clients), client status page (if available)
- **Templates:** Pre-drafted communication templates are maintained in Appendix C for common disruption scenarios
- **Client Priority:** Communication priority follows client SLA tier. Clients with the most critical SLAs are notified first

### 5.3 Vendor Communication

- **Escalation Procedures:** When a critical vendor outage is detected, Technijian's designated vendor contact initiates escalation through the vendor's support channels per the vendor's SLA
- **Key Vendor Support Contacts:**

| Vendor | Support Channel | SLA | Technijian Contact |
|---|---|---|---|
| TPX Data Center | NOC hotline | Per contract | Sai Revanth |
| RMM Platform (ManageEngine Endpoint Central Plus) | Support portal + phone | Per contract | Aditya Saraf |
| Microsoft 365 | Admin portal + Premier Support | Per agreement | Rishad Mohammed |
| CrowdStrike | Support portal + TAM | Per contract | Ravi Jain |
| 3CX (VoIP/Phone) | Support portal | Per contract | Ravi Jain |
| Veeam (Backup) | Support portal + phone | Per contract | Sai Revanth |
| SIEM Platform (Huntress — planned) | Not currently deployed | N/A | Ravi Jain |
| Primary ISP | NOC hotline (via TPX) | Per contract | Ravi Jain |

- **Status Monitoring:** Vendor status pages are monitored and integrated into Technijian's alerting where possible

---

## 6. Plan Activation

### 6.1 Activation Criteria

This plan is activated when any of the following criteria are met:

- **Duration:** Any disruption to Tier 1 or Tier 2 services lasting or expected to last more than 1 hour
- **Scope:** Disruption affecting multiple client environments simultaneously
- **Client Count:** Disruption affecting 25% or more of Technijian's client base
- **Type:** Any ransomware or destructive cyberattack on Technijian systems (regardless of scope, activate immediately)
- **Facility:** Technijian HQ is inaccessible and on-site resources are required
- **Personnel:** Loss of critical personnel with no immediately available backup
- **Vendor:** Critical vendor outage exceeding acceptable outage thresholds defined in Section 3.6

**Activation Authority:** The following individuals have authority to activate this plan:
1. CEO/Founder
2. Security Officer
3. Senior IT Operations Lead (in absence of the above)

### 6.2 Activation Procedures

**Step-by-Step Activation Checklist:**

| Step | Action | Responsible | Timeline |
|---|---|---|---|
| 1 | Assess the situation: confirm the disruption, scope, and expected duration | First responder | Immediate |
| 2 | Determine if activation criteria are met | Activation authority | Within 15 minutes |
| 3 | Declare plan activation and notify the BC team | Activation authority | Within 30 minutes |
| 4 | Assemble the BC/IRT team (virtual or in-person) | BC team lead | Within 1 hour |
| 5 | Initiate internal communication plan (notify all staff) | Communications Lead | Within 1 hour |
| 6 | Initiate client communication (initial notification) | Communications Lead | Within 2 hours |
| 7 | Begin recovery procedures per the applicable scenario (Section 3) | Technical Lead | Immediately upon assembly |
| 8 | Establish status update cadence | BC team lead | Upon assembly |
| 9 | Log all actions, decisions, and communications | All team members | Continuous |
| 10 | Report progress against RTO/RPO targets | Technical Lead | Every status update |

### 6.3 Deactivation and Return to Normal

**Deactivation Criteria:**
- All Tier 1 systems are restored and confirmed operational
- All Tier 2 systems are restored or have a confirmed restoration timeline
- Client services are operating at normal levels
- No active threats remain (if triggered by a security event)
- Enhanced monitoring is in place

**Return-to-Normal Process:**
1. Technical Lead confirms all recovery objectives have been met
2. Activation authority declares return to normal operations
3. All-staff notification that the disruption is resolved
4. Client resolution notifications sent
5. Enhanced monitoring maintained for a minimum of 7 days post-recovery
6. Post-event review scheduled within 5 business days

---

## 7. Testing and Maintenance

### 7.1 Testing Schedule

| Test Type | Frequency | Description |
|---|---|---|
| **Tabletop Exercise** | Semi-annually | Walk-through of disruption scenarios with the BC team. Discussion-based, no actual systems affected |
| **Communication Test** | Quarterly | Test notification chains (phone tree, email, messaging). Verify contact information accuracy |
| **Backup Restoration Drill** | Quarterly / Semi-annually | Per Section 4.3 restoration testing schedule |
| **Pandemic Staffing Drill** | Annually | Simulate reduced staffing scenario per Section 3.5. Validate minimum viable operations and vendor augmentation procedures |
| **Live Failover Drill** | Annually | Actual failover of a representative system to the DR environment. Measure RTO/RPO achievement |
| **Full DR Exercise** | Annually | Comprehensive test simulating a major disruption. Includes communication, decision-making, and technical recovery |

**Additional Testing:**
- After significant infrastructure changes (new hosting, network redesign, new backup platform)
- After a plan-activating event (test any corrective actions)
- When new critical client SLAs introduce tighter recovery requirements

### 7.2 BCP Awareness Training

All Technijian personnel receive BCP awareness training to ensure readiness:

- **Onboarding:** New employees are briefed on the BCP/DR plan during their first week, including their role during a disruption, communication procedures, and remote work expectations
- **Annual Refresher:** All staff complete annual BCP awareness training covering plan updates, lessons learned from tests or activations, and their specific responsibilities
- **Role-Specific Training:** Personnel with assigned roles in the BC team (Appendix B) receive additional training on their specific duties, including decision-making authority, recovery procedures, and communication responsibilities
- **Training Records:** Completion is tracked and retained for audit purposes (minimum 3 years)

### 7.3 Financial Continuity

Technijian maintains the following provisions for financial continuity during a disruption:

- **Emergency Operating Reserve:** A minimum of 90 days of operating expenses is maintained in accessible accounts to fund recovery operations, temporary staffing, emergency equipment purchases, and other disruption-related costs
- **Cyber Insurance:** Technijian maintains a cyber insurance policy (Tokyo Marine HCC, Policy #H25TG32029-04) covering breach response costs, forensic investigation, legal fees, notification costs, business interruption, and ransomware-related expenses
- **Business Interruption Insurance:** Coverage for lost revenue and ongoing expenses during extended disruptions
- **Vendor Payment Continuity:** Critical vendor payments (hosting, SaaS platforms, insurance) are set to auto-pay to prevent service interruptions during a disruption
- **Payroll Continuity:** Payroll processing is cloud-based and can continue during facility loss or personnel disruption

### 7.4 Test Documentation

All test activities are documented with:

| Field | Description |
|---|---|
| Test Date | Date and time of the test |
| Test Type | Tabletop, communication, restoration, failover, or full DR |
| Participants | Names and roles of all participants |
| Scenario | Description of the simulated disruption |
| Objectives | Specific objectives the test was designed to validate |
| Results | Detailed results, including measured recovery times and data integrity validation |
| RTO/RPO Achievement | Actual vs. target for applicable tests |
| Gaps Identified | Issues, failures, or gaps discovered during the test |
| Improvement Actions | Specific actions to address gaps, with owners and target dates |
| Sign-Off | Approval by the Security Officer and/or CEO |

Test documentation is retained for a minimum of 3 years for audit purposes.

### 7.5 Plan Review

- **Annual Review:** This plan is reviewed and approved annually by the Security Officer and CEO/Founder
- **Out-of-Cycle Updates:** This plan is updated outside the normal cycle when triggered by:
  - Infrastructure changes (new hosting, network changes, new vendors)
  - New client SLA requirements with specific DR obligations
  - Vendor changes affecting critical dependencies
  - Lessons learned from incidents, disruptions, or DR tests
  - Regulatory updates affecting business continuity or disaster recovery requirements
  - Organizational changes (personnel, roles, structure)
- **Review Scope:** Each review validates:
  - RTO/RPO targets remain appropriate
  - Recovery strategies are current and technically feasible
  - Contact information is accurate
  - Dependencies are current
  - Backup architecture meets requirements
  - Communication templates are appropriate

### 7.6 Version History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | March 6, 2026 | Ravi Jain | Initial release |
| | | | |
| | | | |

---

## Appendices

### Appendix A: Critical Systems Inventory

| System Name | Function | Owner | Hosting Location | Tier | RTO | RPO | Backup Method | Recovery Procedure |
|---|---|---|---|---|---|---|---|---|
| Client Active Directory | Identity & authentication | IT Operations | TPX / Client site | 1 | 4 hrs | 1 hr | Continuous replication | Restore from replica or backup |
| Client File Servers | File storage & sharing | IT Operations | TPX / Client site | 1 | 4 hrs | 1 hr | Hourly incremental, daily full | Restore from backup |
| Client SQL Databases | Application data | IT Operations | TPX / Cloud | 1 | 4 hrs | 1 hr | Continuous replication + hourly backup | Restore from replica or backup |
| RMM Platform (ManageEngine Endpoint Central Plus) | Endpoint monitoring & mgmt | IT Operations | SaaS (ManageEngine) | 2 | 4 hrs | 4 hrs | Vendor-managed | Vendor restore + manual workaround |
| PSA System (Technijian Internal Client Portal) | Ticketing, billing, CRM | Operations | Technijian-hosted | 2 | 4 hrs | 4 hrs | Vendor-managed + data export | Vendor restore + data import |
| SIEM Platform (Huntress — planned) | Security monitoring (Huntress SIEM planned within 6 months) | Security Officer | N/A | 2 | 4 hrs | 4 hrs | Log archives in cloud storage | Platform restore + log reimport |
| Microsoft 365 | Email, Teams, SharePoint | IT Operations | Microsoft Cloud | 2 | 4 hrs | 4 hrs | Microsoft native + third-party backup | Microsoft restore + backup restore |
| VPN Infrastructure | Remote access | IT Operations | TPX | 2 | 4 hrs | 4 hrs | Config backup daily | Rebuild from config backup |
| CrowdStrike Falcon | EDR | Security Officer | CrowdStrike Cloud | 2 | 4 hrs | N/A | Vendor-managed | Vendor restore |
| Internal File Shares | Internal docs & knowledge base | IT Operations | TPX / SharePoint | 3 | 24 hrs | 24 hrs | Daily backup | Restore from backup |
| Marketing Systems | Website, CRM, social | Marketing | Cloud (various) | 3 | 24 hrs | 24 hrs | Daily backup | Restore from backup |

### Appendix B: Emergency Contact List

**Internal Team:**

| Name | Role | Phone (Work) | Phone (Personal) | Personal Email | Notes |
|---|---|---|---|---|---|
| Ravi Jain | CEO/Founder | 949-379-8499 x201 | 714-402-3164 | rjain557@gmail.com | Activation authority |
| Ravi Jain | Security Officer / vCISO | 949-379-8499 x201 | 714-402-3164 | rjain557@gmail.com | Activation authority |
| Rishad Mohammed | Senior IT Ops Lead | 949-379-8499 x313 | | rmohammed@technijian.com | Activation authority (backup) |
| Sai Revanth | Senior Engineer | 949-379-8499 x334 | | srevanth@technijian.com | Technical Lead |
| Alex Alcantar | Operations Manager | 949-379-8499 x226 | | aalcantar@technijian.com | Communications Lead |
| Aditya Saraf | Helpdesk Manager | 949-379-8499 x322 | | asaraf@technijian.com | Client-facing support |

**External Contacts:**

| Organization | Contact | Phone | Email | Purpose |
|---|---|---|---|---|
| TPX Data Center NOC | Erica Cuevas | 877-487-8722 | ericka.cuevas@tpx.com | Data center support (24/7) |
| Cyber Insurance Carrier (Tokyo Marine HCC) | Abigail Billington | 818-479-4330 | abillington@tmhcc.com | Policy #H25TG32029-04 |
| Outside Legal Counsel (Callahan & Blaine) | Edward Susolik | 714-241-4444 | ES@Callahan-Law.com | Legal guidance — Engagement letter on file |
| External Forensics Firm (Salvage Data) | George Pavel | 800-972-3282 x220 | gpavel@salvagedata.com | Forensic investigation — No retainer agreement |
| Primary ISP | TPX Datacenter (multiple ISPs) | TBD | TBD | Network support — TPX manages ISP redundancy |
| Secondary ISP | N/A (managed by TPX) | N/A | N/A | TPX provides 99.999% uptime via multiple ISPs |
| Equipment Vendor (Technijian — internal) | Ravi Jain | 949-379-8499 x201 | rjain@technijian.com | Emergency hardware — sourced internally |

*Contact list verified quarterly. Last verified: March 7, 2026*

### Appendix C: Client Notification Templates

#### Template 1: Initial Disruption Notification

> **Subject: Service Disruption Notification - Technijian**
>
> Dear [Client Contact],
>
> We are writing to inform you that Technijian is currently experiencing a service disruption that may affect your environment.
>
> **What is happening:**
> [Brief description of the disruption]
>
> **Services Affected:**
> [List of affected services]
>
> **Impact to Your Environment:**
> [Known or potential impact]
>
> **What We Are Doing:**
> Our team has activated our Business Continuity Plan and is actively working to restore services. [Brief description of recovery actions underway]
>
> **Expected Timeline:**
> We expect to provide an update within [timeframe]. Our target for service restoration is [estimated time if known].
>
> Please contact [name] at [phone] or [email] with urgent questions.
>
> Sincerely,
> [Name, Title]
> Technijian Corporation

#### Template 2: Status Update

> **Subject: Service Disruption Update #[number] - Technijian**
>
> Dear [Client Contact],
>
> This is an update on the service disruption reported on [date/time].
>
> **Current Status:** [In Progress / Partially Restored / Near Resolution]
>
> **Progress:**
> [Summary of recovery progress since last update]
>
> **Remaining Impact:**
> [Any continuing impact to client services]
>
> **Next Update:**
> We will provide the next update by [date/time].
>
> [Name, Title]
> Technijian Corporation

#### Template 3: Resolution Notification

> **Subject: Service Disruption Resolved - Technijian**
>
> Dear [Client Contact],
>
> We are pleased to confirm that the service disruption reported on [date] has been fully resolved. All services are operating normally.
>
> **Summary:**
> [Brief summary of what occurred]
>
> **Duration:**
> [Start time] to [end time]
>
> **Impact:**
> [Confirmed impact to client]
>
> **Prevention:**
> [Steps taken to prevent recurrence]
>
> We apologize for any inconvenience and appreciate your patience. Please contact [name] at [contact info] with any questions or if you experience any residual issues.
>
> Sincerely,
> [Name, Title]
> Technijian Corporation

### Appendix D: Recovery Checklists

#### Checklist 1: Data Center Failover

- [ ] Confirm TPX outage scope and expected duration with TPX NOC
- [ ] Declare BCP activation if duration exceeds 4 hours
- [ ] Notify BC team and initiate communication plan
- [ ] Verify cloud DR environment is accessible and healthy
- [ ] Initiate Tier 1 system failover to cloud DR
- [ ] Update DNS records for affected services
- [ ] Verify Tier 1 systems are operational in DR environment
- [ ] Test client connectivity to failed-over services
- [ ] Initiate Tier 2 system failover
- [ ] Verify Tier 2 systems are operational
- [ ] Send client status update confirming service restoration
- [ ] Monitor for stability (minimum 4 hours)
- [ ] Plan failback to TPX when primary site is restored
- [ ] Execute failback during maintenance window
- [ ] Verify all systems operational at primary site
- [ ] Confirm backup replication is current
- [ ] Deactivate BCP and send resolution notification

#### Checklist 2: Ransomware Recovery

- [ ] Activate Incident Response Plan (IRP takes precedence for containment)
- [ ] Isolate all affected systems from the network
- [ ] Preserve evidence (disk images, memory captures, ransom notes)
- [ ] Assess scope: identify all encrypted/affected systems
- [ ] Contact cyber insurance carrier and engage breach coach
- [ ] Report to FBI IC3 and local FBI field office
- [ ] Identify last known-good backup for each affected system
- [ ] Verify backup integrity (confirm backups are not encrypted/compromised)
- [ ] Rebuild affected systems from clean images
- [ ] Restore data from verified clean backups
- [ ] Apply all current security patches before reconnecting
- [ ] Perform organization-wide credential reset
- [ ] Reconnect restored systems with enhanced monitoring
- [ ] Verify client services are operational
- [ ] Send client notifications per communication plan
- [ ] Maintain enhanced monitoring for minimum 90 days
- [ ] Conduct post-incident review within 5 business days

#### Checklist 3: Facility Loss

- [ ] Account for all personnel (confirm safety)
- [ ] Declare BCP activation
- [ ] Activate remote work for all staff
- [ ] Verify VPN infrastructure is operational
- [ ] Verify all engineers can access client environments remotely
- [ ] Confirm cloud-based tools are accessible (RMM, PSA, SIEM, M365)
- [ ] Test phone system/softphone functionality
- [ ] Notify clients if any service impact is expected
- [ ] Arrange temporary office space if needed
- [ ] Coordinate with building management regarding facility access timeline
- [ ] Arrange equipment replacement for any lost hardware
- [ ] File insurance claim if applicable
- [ ] Update staff on facility status and return timeline
- [ ] Deactivate BCP when facility is restored or permanent alternate established

#### Checklist 4: Vendor Outage

- [ ] Confirm vendor outage via status page, support channels, or monitoring
- [ ] Assess expected outage duration
- [ ] Determine if acceptable outage threshold is exceeded (see Section 3.6)
- [ ] Activate alternate/workaround if threshold exceeded
- [ ] Notify clients if service delivery is impacted
- [ ] Monitor vendor status for updates
- [ ] Test workaround functionality
- [ ] Provide client status updates per communication plan
- [ ] When vendor service is restored, verify stability
- [ ] Return to normal operations from workaround
- [ ] Verify all data/functionality is intact after vendor restoration
- [ ] Document the outage and response for lessons learned
- [ ] Send client resolution notification

#### Checklist 5: Pandemic / Workforce Reduction

- [ ] Assess workforce availability: determine number and roles of available staff
- [ ] Declare BCP activation if staffing falls below minimum levels (Section 3.5)
- [ ] Activate remote work for all available staff
- [ ] Identify critical gaps against minimum staffing requirements
- [ ] Prioritize services: maintain Tier 1 (monitoring, alerting, critical incidents) first
- [ ] Defer or reduce Tier 2 services (routine maintenance, non-urgent tickets)
- [ ] Suspend Tier 3 services (projects, internal initiatives) if needed
- [ ] Deploy backup and tertiary personnel per Section 3.4 assignments
- [ ] Contact pre-arranged staffing vendors for surge capacity if needed
- [ ] Expedited security onboarding for any temporary staff before client access
- [ ] Notify clients of service level adjustments and revised response times
- [ ] Provide regular status updates to clients on staffing recovery
- [ ] Follow CDC/local health authority guidelines for workplace safety
- [ ] Monitor staff health and availability daily
- [ ] Gradually restore full service levels as staff return
- [ ] Prioritize backlog of deferred work by client criticality
- [ ] Conduct post-event review when staffing returns to normal
- [ ] Document lessons learned and update plan as needed

---

*End of Document*
