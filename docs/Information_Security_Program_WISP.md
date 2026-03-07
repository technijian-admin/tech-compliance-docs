# Technijian Corporation

# Information Security Program (WISP)

**Version:** 1.0
**Date:** March 6, 2026
**Classification:** Confidential
**Document Owner:** Ravi Jain - CEO/Owner
**Approved By:** Ravi Jain - CEO/Owner
**Next Review Date:** March 6, 2027

---

## 1. Purpose and Scope

The purpose of this Information Security Program (Written Information Security Program, or WISP) is to establish administrative, technical, and physical safeguards for protecting the confidentiality, integrity, and availability of Technijian Corporation's information assets and client data. This program defines the policies, standards, and procedures that govern how Technijian identifies, manages, and mitigates information security risks across all operations.

### 1.1 Scope

This program applies to:

- All Technijian employees, contractors, subcontractors, and temporary personnel
- All information systems, networks, applications, and infrastructure owned or managed by Technijian
- All data processed, stored, or transmitted by Technijian, including internal data and client data
- All Technijian facilities, including headquarters at 18 Technology Drive, Suite 141, and the TPX data center
- Remote workers operating from home offices or alternate locations
- Personal devices (BYOD) used to access Technijian or client systems
- Cloud services and third-party platforms used in service delivery

### 1.2 Regulatory Alignment

This program is designed to align with the following frameworks and regulations:

| Framework / Regulation | Applicability |
|---|---|
| NIST Cybersecurity Framework (CSF) | Primary security framework |
| SOC 2 Trust Services Criteria | Technijian relies on the TPX data center's SOC 2 Type II report for production system assurance. Technijian implements complementary user entity controls (CUECs) as specified in the TPX report |
| HIPAA Security Rule | Healthcare client environments |
| PCI-DSS | Payment card data handling |
| SEC Regulation S-P | Financial services client data |
| FINRA Cybersecurity Guidance | Broker-dealer client environments |
| CCPA / CPRA | California consumer privacy |
| FTC Safeguards Rule | Financial institution client data |
| GDPR | Where applicable to EU data subjects |

### 1.3 Definitions

| Term | Definition |
|---|---|
| **NPI** | Nonpublic Personal Information, as defined under the Gramm-Leach-Bliley Act. Includes financial data such as account numbers, income, credit history, and Social Security numbers. |
| **PII** | Personally Identifiable Information. Any data that can be used to identify a specific individual, including name, address, email, phone number, SSN, and date of birth. |
| **PHI** | Protected Health Information, as defined by HIPAA. Individually identifiable health information transmitted or maintained in any form. |
| **ePHI** | Electronic Protected Health Information. PHI that is created, stored, transmitted, or received electronically. |
| **Confidential Data** | Information classified as Confidential or Restricted per Section 5.1, including client NPI, PHI, PII, and Technijian trade secrets. |
| **Critical Systems** | Information systems essential to Technijian's service delivery or client operations, as defined in the Business Impact Analysis. |
| **Authorized Users** | Individuals who have been granted access to Technijian or client systems through the formal access request and approval process. |
| **Security Incident** | An event that actually or potentially compromises the confidentiality, integrity, or availability of an information system or the data it processes, stores, or transmits. |
| **MSP** | Managed Service Provider. Technijian's primary business model for delivering IT services to clients. |
| **RMM** | Remote Monitoring and Management. ManageEngine Endpoint Central Plus is used to monitor and manage client endpoints and infrastructure. |
| **PSA** | Professional Services Automation. Technijian Internal Client Portal is used for ticketing, billing, and client management. |
| **SIEM** | Security Information and Event Management. Platform used to aggregate, correlate, and analyze security logs. Technijian does not currently operate a dedicated SIEM platform; log review is performed manually and through vendor-native consoles. Huntress SIEM is planned for deployment within the next 6 months. |
| **EDR** | Endpoint Detection and Response. Security solution deployed on endpoints to detect and respond to threats. |

---

## 2. Governance and Organizational Security

### 2.1 Security Leadership

Technijian designates a Security Officer (or virtual Chief Information Security Officer, vCISO) who is responsible for the overall management and enforcement of this Information Security Program. The current Security Officer is **Ravi Jain, CEO/Owner**, who serves in a dual capacity. The Security Officer:

- Reports directly to the CEO/Founder on all security matters
- Has the authority to establish and enforce security policies across the organization
- Is responsible for maintaining this program, conducting risk assessments, and overseeing incident response
- Serves as the primary point of contact for security-related inquiries from clients, auditors, and regulators
- Coordinates with external security consultants and assessors as needed

The CEO/Founder (**Ravi Jain**) retains ultimate accountability for the security program and provides executive sponsorship, resource allocation, and strategic direction.

### 2.2 Roles and Responsibilities

| Role | Security Responsibilities |
|---|---|
| **CEO/Founder** | Executive accountability for the security program. Approves policies. Allocates resources. Serves as Executive Sponsor during security incidents. |
| **Security Officer** | Day-to-day management of the security program. Conducts risk assessments. Manages incident response. Oversees compliance. Reports to CEO. Manages vendor security reviews. |
| **IT Operations** | Implements and maintains technical security controls. Manages patching and vulnerability remediation. Monitors security alerts. Maintains backup systems. Enforces endpoint security. |
| **Engineers with Client Access** | Adhere to client security requirements. Use only authorized access methods. Report security anomalies immediately. Follow least-privilege principles. Protect client credentials. |
| **Human Resources** | Conducts background screening. Manages security awareness training enrollment. Executes onboarding/offboarding security procedures. Maintains personnel records for access management. |
| **All Employees** | Complete security awareness training. Report suspected incidents immediately. Follow acceptable use policies. Protect credentials. Lock workstations when unattended. Comply with data classification and handling requirements. |
| **Subcontractors** | Bound by contractual security requirements. Must complete security awareness training. Subject to the same access control and data handling requirements as employees. Supervised access to client environments. |

### 2.3 Policy Review Cycle

This Information Security Program and all supporting policies are reviewed and approved on an annual basis by the Security Officer and CEO/Founder. The annual review occurs no later than the anniversary of the last approval date.

Out-of-cycle reviews are triggered by:

- Changes in applicable laws, regulations, or contractual requirements
- Significant security incidents or breaches
- Major changes to Technijian's infrastructure, technology stack, or service offerings
- Results of risk assessments or audits that identify policy gaps
- Organizational changes such as mergers, acquisitions, or new lines of business
- Changes in the threat landscape relevant to Technijian's operations

All policy changes are documented in the Version History (Section 18.2), communicated to affected personnel, and stored in the controlled document repository.

### 2.4 Asset Inventory Management

Technijian maintains a comprehensive inventory of all information assets. The inventory is the foundation for risk assessment, access control, vulnerability management, and incident response.

**Assets tracked include:**

| Asset Category | Examples | Attributes Tracked |
|---|---|---|
| Hardware | Servers, workstations, laptops, network equipment, mobile devices, storage | Owner, location, serial number, model, OS, classification tier, warranty |
| Software | Operating systems, applications, SaaS platforms, licenses | Version, vendor, license count, deployment scope, patch status |
| Data Stores | Databases, file shares, cloud storage, backups | Data classification, owner, location, encryption status, retention |
| Network Assets | Firewalls, switches, routers, VPN concentrators, wireless APs | IP address, location, firmware version, configuration baseline |
| Cloud Services | M365 tenant, Azure subscriptions, AWS accounts, SaaS tools | Service type, data classification, administrator, contract expiration |
| Client Environments | Per-client systems managed by Technijian | Client name, system type, SLA tier, RTO/RPO, primary engineer |

**Inventory Maintenance:**

- **New Assets:** Added to the inventory before deployment to production. Includes security configuration verification
- **Decommissioned Assets:** Removed from the inventory upon decommissioning. Data destruction per Section 5.3 is completed and documented before disposal
- **Quarterly Review:** The asset inventory is reviewed quarterly by IT Operations for accuracy. Discrepancies are investigated and resolved
- **Annual Reconciliation:** A full reconciliation of the asset inventory against physical and logical assets is conducted annually as part of the risk assessment process
- **Unauthorized Assets:** Any asset discovered on the network that is not in the inventory is investigated immediately. Unauthorized assets are quarantined until ownership and authorization are confirmed

---

## 3. Risk Assessment and Management

### 3.1 Risk Assessment Process

Technijian employs a structured risk assessment methodology to identify, analyze, and evaluate information security risks. The process includes the following steps:

1. **Asset Identification:** Inventory all information assets, including hardware, software, data, personnel, and facilities. Classify assets by criticality and data sensitivity.

2. **Threat Identification:** Identify potential threat sources and events relevant to each asset. Sources include external actors (cybercriminals, nation-states), internal actors (employees, contractors), environmental threats (natural disasters, power failures), and technical threats (hardware failure, software bugs).

3. **Vulnerability Assessment:** Identify weaknesses in controls that could be exploited by identified threats. Sources include vulnerability scans, penetration test results, audit findings, and industry advisories.

4. **Likelihood Assessment:** Estimate the probability of each threat exploiting each vulnerability, using a scale of Low, Medium, and High, based on historical data, threat intelligence, and environmental factors.

5. **Impact Assessment:** Estimate the potential impact of each risk event on confidentiality, integrity, and availability, using a scale of Low, Medium, High, and Critical, considering financial loss, regulatory penalties, reputational damage, and client impact.

6. **Risk Rating:** Calculate the overall risk rating by combining likelihood and impact scores using the following matrix:

| | Low Impact | Medium Impact | High Impact | Critical Impact |
|---|---|---|---|---|
| **High Likelihood** | Medium | High | Critical | Critical |
| **Medium Likelihood** | Low | Medium | High | Critical |
| **Low Likelihood** | Low | Low | Medium | High |

7. **Risk Treatment:** For each identified risk, select a treatment strategy:
   - **Mitigate:** Implement controls to reduce likelihood or impact
   - **Transfer:** Transfer risk through insurance or contractual arrangements
   - **Accept:** Formally accept the residual risk with documented justification and management approval
   - **Avoid:** Eliminate the risk by discontinuing the activity or removing the asset

### 3.2 Risk Assessment Frequency

- **Formal Risk Assessment:** Conducted annually by the Security Officer, with results reviewed and approved by the CEO/Founder.
- **Ad-Hoc Assessments:** Conducted when significant changes occur, including new client engagements with elevated security requirements, major infrastructure changes, introduction of new technologies or vendors, significant security incidents, and regulatory changes.
- **Assessment Documentation:** All risk assessment results, including methodology, findings, treatment decisions, and approvals, are stored in the controlled document repository and retained for a minimum of 3 years.

### 3.3 Risk Register

Technijian maintains a risk register that documents:

| Field | Description |
|---|---|
| Risk ID | Unique identifier for each risk |
| Risk Description | Description of the risk scenario |
| Risk Owner | Individual accountable for managing the risk |
| Likelihood | Assessed likelihood rating |
| Impact | Assessed impact rating |
| Overall Rating | Calculated risk rating |
| Treatment Strategy | Selected treatment approach |
| Treatment Plan | Specific actions to address the risk |
| Target Date | Expected completion date for treatment |
| Status | Current status (Open, In Progress, Closed, Accepted) |
| Residual Risk | Risk rating after treatment implementation |

The risk register is:
- Updated as new risks are identified or existing risks change
- Reviewed quarterly by the Security Officer
- Presented to the CEO/Founder at least annually
- Used as input for resource allocation and security investment decisions

---

## 4. Access Control

### 4.1 Least Privilege and Role-Based Access

Technijian implements Role-Based Access Control (RBAC) to ensure that users are granted only the minimum permissions necessary to perform their job functions. The following principles govern access control:

- **Role Definitions:** Standardized role definitions are maintained for each job function, specifying the systems, data, and permissions required. Roles are reviewed and updated as job functions change.
- **Access Request Workflow:** All access requests are submitted through a formal process that includes:
  1. Request submitted by the user or their manager
  2. Approval by the user's direct manager
  3. Approval by the system owner or Security Officer for sensitive systems
  4. Provisioning by IT Operations
  5. Confirmation and documentation of access granted
- **Least Privilege Enforcement:** Users are granted access only to the specific resources required for their role. No user receives administrative or elevated access by default. Access to client environments requires additional approval from the account manager.
- **Separation of Duties:** Critical functions are divided among multiple individuals to prevent fraud, error, and conflicts of interest. No single individual has unchecked control over any critical process.

### 4.2 Authentication Standards

**Multi-Factor Authentication (MFA):**
- MFA is required for all access to administrative interfaces, client environments, cloud services, VPN connections, and email
- SMS-based MFA is prohibited for administrative accounts due to SIM-swap and interception risks
- Approved MFA methods:
  - Authenticator applications (TOTP-based, e.g., Microsoft Authenticator, Google Authenticator)
  - Hardware security tokens (e.g., YubiKey)
  - FIDO2/WebAuthn keys
- MFA is enforced via conditional access policies where supported

**Password Requirements:**
- Minimum length: 14 characters
- Complexity: Must include a mix of uppercase, lowercase, numbers, and special characters, or a passphrase of 4+ random words
- No reuse of the last 12 passwords
- Maximum age: 90 days for standard accounts, 60 days for privileged accounts
- Account lockout after 5 consecutive failed attempts, with a 15-minute lockout period
- Passwords must not appear in known breach databases (checked at creation and rotation)

### 4.3 Access Reviews

Access reviews are conducted quarterly to ensure that user access remains appropriate and aligned with current job responsibilities:

1. **Review Process:**
   - IT Operations generates access reports for all systems, including user lists, role assignments, and permission levels
   - Managers review access for their direct reports and confirm or revoke permissions
   - The Security Officer reviews privileged access and access to sensitive data
   - System owners verify that service accounts and shared accounts remain necessary and appropriately scoped

2. **Evidence Retention:**
   - Access review records, including reviewer sign-off, date, systems reviewed, and actions taken, are retained for a minimum of 3 years

3. **Remediation:**
   - Excess or inappropriate permissions identified during reviews are revoked within 5 business days
   - Orphaned accounts (accounts with no active owner) are disabled immediately and investigated

### 4.4 Privileged Access Management

Privileged accounts (administrative access, root accounts, domain admin, and similar elevated permissions) are subject to additional controls:

- **Just-in-Time (JIT) Access:** Privileged access is granted on a just-in-time basis where technically feasible. Permanent standing privileged access is minimized.
- **Privileged Account Inventory:** All privileged accounts are inventoried and have a designated owner.
- **Logging:** All actions performed using privileged accounts are logged, including authentication events, configuration changes, and data access.
- **Log Review:**
  - High-risk system logs (domain controllers, firewalls, client production systems): Reviewed weekly
  - Standard system logs: Reviewed monthly
- **Privileged Account Passwords:** Managed through a password vault with unique, complex passwords per account.

### 4.5 Remote Access

Technijian engineers and staff access internal and client systems remotely. The following controls apply:

- **VPN Required:** All remote access to internal Technijian networks requires connection through the corporate VPN
- **Encryption:** All remote connections use TLS 1.2 or higher
- **Endpoint Compliance:** Devices must pass endpoint compliance checks before VPN connection is established, including:
  - Current and active EDR agent (CrowdStrike Falcon)
  - Operating system and patches within compliance thresholds
  - Full-disk encryption enabled
  - Active screen lock configured
- **Session Timeouts:** VPN and remote desktop sessions automatically disconnect after 30 minutes of inactivity
- **Split Tunneling:** Split tunneling is disabled on VPN connections to ensure all traffic routes through monitored infrastructure

---

## 5. Data Protection

### 5.1 Data Classification

All data processed, stored, or transmitted by Technijian is classified according to the following levels:

| Classification | Definition | Examples | Handling Requirements |
|---|---|---|---|
| **Restricted** | Highest sensitivity. Unauthorized disclosure would cause severe harm. | Client NPI, PHI/ePHI, payment card data (PCI), Social Security numbers, credentials/keys | Encrypted at rest and in transit. Access on strict need-to-know basis. Logged access. No storage on personal devices. Secure destruction required. |
| **Confidential** | Sensitive business or client information. Unauthorized disclosure would cause significant harm. | Client infrastructure documentation, Technijian security policies, contracts, employee PII, financial records | Encrypted at rest and in transit. Access limited to authorized personnel. Secure destruction required. |
| **Internal** | For internal use only. Not intended for public disclosure. | Internal procedures, meeting notes, project documentation, training materials | Protected from unauthorized external access. Standard access controls. |
| **Public** | Information approved for public release. | Marketing materials, published blog posts, public-facing website content | No special handling required. Approved by management before release. |

Data owners are responsible for classifying their data. When in doubt, data is classified at the higher sensitivity level until formally assessed.

### 5.2 Encryption Standards

**Data in Transit:**
- All data transmitted over networks uses TLS 1.2 or higher
- SSL, TLS 1.0, and TLS 1.1 are disabled on all Technijian-managed systems
- VPN connections use IPsec or TLS-based tunnels with AES-256 encryption
- SFTP or SCP is used for file transfers containing Confidential or Restricted data (FTP is prohibited)

**Data at Rest:**
- AES-256 encryption is the standard for all data at rest
- Full-disk encryption is required on all endpoints:
  - Windows: BitLocker with TPM
  - macOS: FileVault 2
- SQL Server instances containing Confidential or Restricted data use Transparent Data Encryption (TDE)
- Backup files are encrypted using AES-256 before storage

**Key Management:**
- Encryption keys are generated, stored, and rotated according to industry best practices
- Keys are stored separately from the data they protect
- Key access is restricted to authorized personnel only
- Key rotation occurs annually at minimum, or immediately upon suspected compromise
- Key management procedures are documented and reviewed annually

### 5.3 Data Retention and Destruction

**Retention Periods:**

| Data Type | Retention Period | Regulatory Basis |
|---|---|---|
| Client NPI / financial data | 7 years after end of engagement | SEC/FINRA requirements |
| PHI / ePHI | 6 years after last use | HIPAA requirements |
| Employee personnel records | 7 years after termination | Federal/state labor laws |
| Security logs and audit trails | Minimum 1 year (3 years recommended) | SOC 2 / regulatory requirements |
| Incident response records | 6 years | HIPAA / regulatory requirements |
| Contracts and agreements | Duration + 7 years | Legal requirements |
| General business records | 7 years | Tax and legal requirements |

**Destruction Methods (per NIST SP 800-88):**

| Media Type | Destruction Method |
|---|---|
| SSDs / Flash storage | Cryptographic erasure (sanitize command) followed by verification |
| HDDs | Secure overwrite (3-pass minimum) or physical destruction (degaussing + shredding) |
| Optical media | Physical shredding |
| Paper documents | Cross-cut shredding (minimum P-4 per DIN 66399) |
| Cloud / virtual storage | Cryptographic erasure with key destruction, followed by platform-specific secure deletion |

- Certificates of destruction are obtained and retained for all Restricted and Confidential data destruction events
- Destruction activities are logged with date, method, media description, and responsible personnel

### 5.4 Client Data Segregation

Technijian maintains strict separation of client data to prevent unauthorized cross-client access:

- **Logical Segregation:** Client environments are isolated using dedicated tenancies, separate Active Directory domains or organizational units, and unique access credentials per client
- **Network Segregation:** Client networks are separated using VLANs, firewall rules, and dedicated VPN tunnels. Cross-client network traffic is prohibited
- **Database Segregation:** Client data is stored in separate database instances. Shared databases across clients are prohibited for Restricted or Confidential data
- **Access Controls:** Engineers are granted access only to specific client environments required for their assignments. Cross-client access requires separate authorization
- **Monitoring:** Access to client environments is logged and monitored. Anomalous cross-client access patterns trigger alerts

---

## 6. Network and Infrastructure Security

### 6.1 Network Architecture

Technijian's network architecture implements defense-in-depth principles:

- **Network Segmentation:** The network is segmented into distinct zones based on function and sensitivity:
  - DMZ for public-facing services
  - Internal corporate network for Technijian operations
  - Management network for infrastructure administration
  - Client-facing networks, individually segmented per client
- **Firewalls:** Next-generation firewalls are deployed at all network boundaries with rule sets following deny-by-default principles. Firewall rules are reviewed quarterly and after significant changes
- **VLAN Isolation:** VLANs are used to isolate network traffic between functional zones. Inter-VLAN routing is controlled by firewall policies
- **TPX Data Center:** Physical infrastructure security at the TPX data center is governed by TPX's SOC 2 Type II controls. Technijian reviews the TPX SOC 2 report annually and validates that complementary user entity controls are in place

### 6.2 Endpoint Protection

CrowdStrike Falcon EDR is deployed on all Technijian-managed endpoints (workstations, laptops, and servers):

- **Deployment:** All endpoints must have an active CrowdStrike Falcon sensor. Endpoints without a functioning sensor are quarantined from the network
- **Configuration:** Sensors are configured per Technijian's standard security profile, including real-time detection, automated prevention, and telemetry collection
- **Updates:** Sensor versions and detection content are kept current. Updates are applied within 7 days of release
- **Compliance Monitoring:** Endpoint compliance is monitored continuously via ManageEngine Endpoint Central Plus. Non-compliant endpoints are flagged and remediated within 24 hours
- **Mobile Devices:** Company-owned and BYOD mobile devices accessing corporate email or data are enrolled in mobile device management (MDM) with security policies enforced

### 6.3 Vulnerability Management

Technijian maintains a continuous vulnerability management program:

- **Scanning Cadence:**
  - External vulnerability scans: Monthly at minimum
  - Internal vulnerability scans: Monthly at minimum
  - Scans after significant infrastructure changes
  - Penetration testing: Annually by a qualified third party

- **Remediation SLAs:**

| Severity | Remediation Timeframe |
|---|---|
| Critical (CVSS 9.0-10.0) | 72 hours |
| High (CVSS 7.0-8.9) | 7 calendar days |
| Medium (CVSS 4.0-6.9) | 30 calendar days |
| Low (CVSS 0.1-3.9) | 90 calendar days or next maintenance window |

- **Patch Management:** Security patches are tested and deployed according to the remediation SLAs above. Emergency patches for actively exploited vulnerabilities are deployed on an expedited basis. All patching activities are documented
- **Exceptions:** Vulnerabilities that cannot be remediated within the defined timeframes require a documented exception with compensating controls, approved by the Security Officer

### 6.4 Wireless Security

Wireless networks at Technijian facilities and client sites are secured with the following controls:

- **Encryption:** All wireless networks use WPA3 (or WPA2-Enterprise as a minimum). WEP and open/unencrypted wireless networks are prohibited
- **Authentication:** Corporate wireless networks require 802.1X authentication against Active Directory / Azure AD. Pre-shared key (PSK) networks are limited to guest use only
- **Segmentation:** Guest wireless networks are isolated from internal corporate and client networks via VLAN segmentation and firewall rules. Guest networks provide internet access only with no access to internal resources
- **SSID Management:** Corporate SSIDs are not broadcast publicly where feasible. Guest SSIDs use clear naming conventions (e.g., "Technijian-Guest")
- **Rogue AP Detection:** Wireless infrastructure is monitored for rogue access points. Unauthorized APs detected on the network are investigated and removed immediately
- **Client Site Wireless:** When deploying or managing wireless infrastructure at client sites, the same security standards apply unless the client's own wireless security policy specifies stricter requirements

### 6.5 Monitoring and Logging

- **Log Aggregation:** Technijian does not currently operate a dedicated SIEM platform. Security event monitoring is performed through CrowdStrike Falcon console, Microsoft 365 security center, and direct log review on source systems. Huntress SIEM is planned for deployment within the next 6 months.
- **Log Sources:** The following sources are reviewed for security events:
  - Firewalls and network devices
  - CrowdStrike EDR
  - Windows Event Logs (authentication, privilege use, policy changes)
  - Active Directory / Azure AD
  - VPN concentrators
  - Cloud platforms (Azure, AWS, Microsoft 365)
  - Email gateway
  - DNS servers
  - Application logs for critical systems
- **Log Retention:** Minimum 1 year of online log storage, with 3 years of archived storage for compliance purposes
- **Automated Alerting:** Detection rules are configured for common attack patterns, policy violations, and anomalous behavior. Alerts are triaged per the severity matrix
- **Security Monitoring:** Security events are monitored by designated personnel through CrowdStrike Falcon and vendor-native consoles. Critical alerts receive immediate response; all alerts are triaged within defined SLAs
- **Dark Web Monitoring:** Continuous monitoring for Technijian and client credential exposure on dark web marketplaces, forums, and paste sites. Exposed credentials trigger immediate forced password reset and incident investigation

---

## 7. Email Security

### 7.1 Email Authentication

Technijian implements the following email authentication standards to prevent spoofing, phishing, and business email compromise:

- **SPF (Sender Policy Framework):** SPF records are published in DNS for all Technijian domains, specifying authorized sending sources. SPF policy is set to `-all` (hard fail) to reject unauthorized senders
- **DKIM (DomainKeys Identified Mail):** All outbound email from Technijian domains is signed with DKIM. DKIM keys are rotated annually or upon suspected compromise
- **DMARC (Domain-based Message Authentication, Reporting, and Conformance):** DMARC policy is set to `p=reject` for all Technijian domains. DMARC aggregate and forensic reports are monitored to detect unauthorized use of Technijian domains
- **Email Gateway Protection:** Inbound email is filtered through an email security gateway that provides:
  - Anti-spam and anti-malware scanning
  - URL rewriting and time-of-click analysis
  - Attachment sandboxing for executable and macro-enabled files
  - Impersonation and display name spoofing detection
  - External sender tagging (banners warning recipients of external origin)

### 7.2 Business Email Compromise (BEC) Controls

- **Wire Transfer / Payment Change Verification:** Any request to change payment details, wire transfer instructions, or banking information received via email must be verified by phone using a previously known phone number (not one provided in the email)
- **Executive Impersonation Alerts:** Email rules flag messages that appear to originate from executives but are sent from external domains
- **Training:** BEC awareness is included in security awareness training and phishing simulations

---

## 8. Data Loss Prevention

### 8.1 DLP Controls

Technijian implements controls to prevent unauthorized exfiltration of Restricted and Confidential data:

- **Email DLP:** Rules are configured in the email gateway and Microsoft 365 to detect and block outbound email containing patterns matching SSNs, credit card numbers, and other Restricted data indicators. Violations are logged and reviewed by the Security Officer
- **Endpoint DLP:** Endpoint agents monitor and control the transfer of sensitive data to removable media (USB drives, external hard drives). Unauthorized transfers of Restricted data to removable media are blocked
- **Cloud DLP:** Microsoft 365 DLP policies are configured to detect and prevent sharing of Restricted data via SharePoint, OneDrive, and Teams with unauthorized external recipients
- **Alerting:** DLP policy violations generate alerts that are reviewed within 24 hours. Confirmed data exfiltration triggers the Incident Response Plan
- **Exceptions:** DLP exceptions for legitimate business needs require documented approval from the Security Officer and are reviewed quarterly

---

## 9. Cloud Security

### 9.1 Cloud Service Controls

Technijian uses cloud services (Microsoft 365, Azure, AWS, SaaS platforms) to deliver managed IT services. The following controls apply:

- **Identity and Access Management:** Cloud services are integrated with centralized identity management where possible. MFA is enforced for all cloud service access per Section 4.2
- **Conditional Access Policies:** Microsoft 365 and Azure conditional access policies enforce:
  - MFA for all users
  - Block legacy authentication protocols
  - Require compliant devices for access to sensitive data
  - Restrict access from untrusted locations or networks
  - Session timeout and reauthentication requirements
- **Tenant Hardening:** Microsoft 365 tenant is configured per CIS Microsoft 365 Foundations Benchmark:
  - Global admin accounts are limited and use dedicated accounts (not daily-use accounts)
  - Azure AD security defaults or equivalent conditional access policies enabled
  - Audit logging enabled for all services
  - External sharing restricted to authorized domains
  - Guest access reviewed quarterly
- **Shadow IT Prevention:** Unauthorized cloud services (shadow IT) are prohibited. Cloud app discovery tools are used to identify unauthorized SaaS usage. Identified unauthorized services are blocked or brought into compliance

### 9.2 Cloud Backup and Recovery

- Microsoft 365 data (Exchange, SharePoint, OneDrive, Teams) is backed up using a third-party backup solution in addition to Microsoft's native retention
- Cloud workloads in Azure and AWS follow the same backup and recovery standards defined in the BCP/DR Plan Section 4
- Cloud service configurations (infrastructure-as-code, tenant settings, conditional access policies) are documented and version-controlled to enable rapid rebuilding

---

## 10. Cyber Insurance

### 10.1 Coverage

Technijian maintains a cyber insurance policy to transfer residual risk and provide financial protection for security incidents:

- **Carrier:** Tokyo Marine HCC
- **Policy Number:** H25TG32029-04
- **Contact:** Abigail Billington, 818-479-4330

**Coverage Areas:**

| Coverage | Description |
|---|---|
| Breach Response Costs | Forensic investigation, breach coach (attorney), notification costs, credit monitoring for affected individuals |
| Business Interruption | Lost revenue and ongoing expenses during a covered cyber event |
| Ransomware / Cyber Extortion | Ransom payments (with carrier approval), negotiation services, recovery costs |
| Regulatory Defense | Legal defense costs for regulatory investigations and proceedings |
| Third-Party Liability | Claims from clients or third parties arising from a data breach or security failure |
| Media Liability | Claims arising from electronic media content |

### 10.2 Policy Management

- The Security Officer reviews the policy annually to ensure coverage limits and terms remain appropriate for Technijian's risk profile
- Policy is renewed annually. Coverage adjustments are made based on changes in revenue, client base, data volumes, and risk assessment findings
- All IRT members are aware of the insurance carrier contact information and the claims notification process documented in the IRP

---

## 11. Privacy

### 11.1 Privacy Principles

Technijian adheres to the following privacy principles in its handling of personal data:

- **Purpose Limitation:** Personal data is collected and processed only for specified, legitimate business purposes
- **Data Minimization:** Only the minimum personal data necessary for the stated purpose is collected and retained
- **Transparency:** Individuals are informed about how their data is collected, used, stored, and shared through privacy notices
- **Individual Rights:** Technijian supports data subject access requests (DSARs), correction requests, and deletion requests in accordance with applicable privacy laws (CCPA/CPRA, GDPR where applicable)
- **Accountability:** The Security Officer is responsible for ensuring privacy compliance and responding to privacy-related inquiries and complaints

### 11.2 Privacy Impact Assessments

Privacy impact assessments are conducted when:

- Implementing new systems or processes that collect or process personal data
- Making significant changes to existing data processing activities
- Engaging new vendors who will process personal data on Technijian's behalf
- Client engagements that involve processing of PHI, NPI, or large volumes of PII

Assessments evaluate the necessity and proportionality of data processing, identify privacy risks, and define mitigating controls. Results are documented and retained for a minimum of 3 years.

---

## 12. Change Management

### 12.1 Change Control Process

All changes to production systems, infrastructure, and security configurations follow a formal change management process:

1. **Change Request:** All changes are submitted as a formal change request documenting the proposed change, business justification, systems affected, risk assessment, rollback plan, and testing requirements
2. **Risk Classification:**

| Change Type | Risk Level | Approval Required | Testing Required |
|---|---|---|---|
| Standard (routine, pre-approved) | Low | Pre-approved by Security Officer | Per standard procedure |
| Normal (planned, non-routine) | Medium | Manager + system owner | Test in non-production environment |
| Emergency (urgent, unplanned) | High | Security Officer or CEO (verbal OK, documented post-change) | Post-implementation validation |

3. **Approval:** Changes are reviewed and approved before implementation. High-risk changes and changes to security controls require Security Officer approval
4. **Implementation:** Changes are implemented during approved maintenance windows where possible. Emergency changes are implemented as needed with post-implementation documentation
5. **Validation:** Post-implementation testing confirms the change achieved its objective and did not introduce unintended side effects
6. **Documentation:** All changes, approvals, test results, and outcomes are documented in the change management system and retained for audit purposes

### 12.2 Security Configuration Changes

Changes to security controls, firewall rules, access policies, and authentication configurations are subject to additional scrutiny:

- All security configuration changes require Security Officer review and approval
- Changes are logged with before-and-after configuration snapshots
- Emergency security changes (e.g., firewall rules to block an active attack) may be implemented immediately and documented within 24 hours

---

## 13. Security Metrics and Reporting

### 13.1 Key Security Metrics

The Security Officer tracks and reports on the following metrics to measure the effectiveness of the security program:

| Metric | Target | Frequency |
|---|---|---|
| Patch compliance (critical/high within SLA) | 95% | Monthly |
| MFA adoption rate | 100% | Monthly |
| EDR agent deployment coverage | 100% | Monthly |
| Phishing simulation click rate | < 5% | Quarterly |
| Mean time to detect (MTTD) security incidents | < 4 hours | Per incident |
| Mean time to respond (MTTR) security incidents | < 1 hour (Critical), < 4 hours (High) | Per incident |
| Backup success rate | > 99% | Weekly |
| Vulnerability scan remediation within SLA | 90% | Monthly |
| Access review completion rate | 100% | Quarterly |
| Security awareness training completion | 100% | Annually |
| Open risk register items overdue | 0 | Quarterly |

### 13.2 Reporting

- **Monthly Security Report:** The Security Officer produces a monthly security summary covering metrics, incidents, vulnerability status, and notable events. Distributed to the CEO/Founder
- **Quarterly Security Review:** A quarterly review meeting with the CEO/Founder covers security posture trends, risk register updates, compliance status, and resource needs
- **Annual Security Report:** An annual comprehensive report summarizes the year's security activities, incidents, audit findings, risk assessments, and program improvements. Used as input for annual program review and budget planning

---

## 14. Vendor and Subcontractor Management

### 14.1 Vendor Risk Assessment

Before engaging any new vendor or subcontractor with access to Technijian or client systems or data, the following due diligence is performed:

1. **Security Questionnaire:** Vendor completes Technijian's security assessment questionnaire covering access controls, encryption, incident response, business continuity, and compliance posture
2. **SOC 2 Report Review:** If available, the vendor's SOC 2 Type II report is reviewed for relevant control deficiencies. Alternative evidence (ISO 27001 certification, penetration test results) may be accepted where SOC 2 is not available
3. **NDA Execution:** A non-disclosure agreement is executed before any confidential information is shared
4. **Contractual Security Requirements:** Contracts include:
   - Data protection and confidentiality obligations
   - Incident notification requirements (within 24 hours)
   - Right to audit
   - Data return and destruction upon termination
   - Compliance with applicable regulations
   - Insurance requirements (cyber liability)

### 14.2 Ongoing Vendor Monitoring

- **Annual Reassessment:** Critical vendors (those with access to Restricted or Confidential data, or providing critical infrastructure services) are reassessed annually using the same criteria as the initial assessment
- **Incident Monitoring:** Technijian monitors for publicly disclosed security incidents affecting vendors and assesses potential impact to Technijian and its clients
- **Performance Monitoring:** Vendor service performance, SLA compliance, and security posture are reviewed as part of the annual reassessment
- **Right to Audit:** Technijian reserves the right to audit vendor security controls, either directly or through a qualified third party, as stipulated in vendor contracts

### 14.3 Business Associate Agreements (HIPAA)

When Technijian provides managed IT services to healthcare clients or otherwise accesses, processes, or stores Protected Health Information (PHI/ePHI), a Business Associate Agreement (BAA) is required:

- **BAA Execution:** A BAA is executed with every client for whom Technijian may access, store, or transmit PHI, before any PHI is accessed or services commence
- **BAA Inventory:** A register of all active BAAs is maintained, including: client name, BAA execution date, scope of services, PHI data types, and BAA expiration/renewal date
- **Annual Review:** All active BAAs are reviewed annually to ensure terms remain current and accurately reflect the scope of services provided
- **Subcontractor BAAs:** When Technijian engages subcontractors or vendors who may access client PHI, a downstream BAA is executed with the subcontractor before PHI access is granted
- **Termination:** Upon termination of a client engagement involving PHI, Technijian returns or securely destroys all PHI per the BAA terms and WISP data destruction procedures (Section 5.3). Certificates of destruction are provided to the client

### 14.4 TPX Data Center

Technijian utilizes the TPX data center for hosting critical infrastructure:

- **Relationship:** TPX provides colocation and hosting services. TPX is responsible for physical security, environmental controls (power, cooling, fire suppression), and network connectivity to the facility. Technijian is responsible for all logical security controls on systems hosted at TPX
- **SOC 2 Report:** TPX maintains a SOC 2 Type II report. Technijian reviews this report annually and validates:
  - No unresolved control deficiencies that affect Technijian's security posture
  - Complementary user entity controls are implemented by Technijian as specified in the report
- **Contractual Requirements:** The TPX service agreement includes data protection obligations, incident notification requirements, and physical security commitments

---

## 15. Human Resources Security

### 15.1 Background Screening

All prospective Technijian employees undergo pre-employment background screening before their start date. Screening is conducted by a licensed third-party provider and includes:

- **Criminal History Check:** Federal and state criminal records search
- **Employment Verification:** Verification of employment history for the previous 7 years
- **Education Verification:** Verification of highest claimed degree or certification
- **Professional References:** Contact with professional references provided by the candidate

Background check results are reviewed by HR and the hiring manager. Adverse findings are evaluated on a case-by-case basis considering the nature of the offense, time elapsed, and relevance to the position. Results are maintained in the personnel file with restricted access.

Subcontractors with access to client environments or Confidential/Restricted data must have undergone equivalent background screening, documented by their employer.

### 15.2 Security Awareness Training

- **Onboarding Training:** All new employees and contractors complete security awareness training within their first week. Training covers:
  - Information security policies and acceptable use
  - Data classification and handling
  - Phishing and social engineering awareness
  - Password security and MFA
  - Incident reporting procedures
  - Client data protection responsibilities
  - Physical security and clean desk policy

- **Annual Refresher Training:** All personnel complete annual security awareness refresher training. Training content is updated annually to reflect current threats and any policy changes

- **Phishing Simulations:** Simulated phishing campaigns are conducted at least quarterly. Personnel who fail simulations receive additional targeted training. Repeat failures are escalated to management

- **Training Documentation:** Training completion is tracked in the HR system. Records include employee name, training completed, date, and assessment results. Records are retained for the duration of employment plus 3 years

### 15.3 Onboarding and Termination

**Onboarding:**
1. HR initiates the onboarding process and notifies IT Operations of the new hire's role and start date
2. Access is provisioned per the role definition, with approval from the direct manager
3. Manager approves the specific systems and client environments the employee requires access to
4. Security awareness training must be completed before access to client environments is granted
5. Employee signs the Acceptable Use Policy acknowledgment and confidentiality agreement
6. Equipment is issued with standard security configuration (encryption, EDR, screen lock)

**Termination (Voluntary or Involuntary):**
1. HR notifies IT Operations immediately upon notice of termination
2. All Technijian accounts (Active Directory, email, VPN, cloud services) are disabled within 1 hour of departure
3. Full deprovisioning of all system access, including client environments, is completed within 24 hours
4. Company-owned equipment (laptop, phone, tokens, badges) is recovered
5. Remote access credentials are revoked
6. The termination checklist is completed, signed by the manager and IT Operations, and retained in the personnel file
7. For involuntary terminations, accounts are disabled before or simultaneously with the notification meeting

### 15.4 Acceptable Use Policy

All Technijian personnel must acknowledge and comply with the Acceptable Use Policy, which governs the use of:

- **Company Systems:** Technijian workstations, servers, and infrastructure are for authorized business use. Limited personal use is permitted provided it does not interfere with work duties, violate policy, or introduce security risks
- **Client Systems:** Access to client systems is limited to authorized work activities. No personal use of client systems is permitted. All client system access follows the client's security policies in addition to Technijian's
- **Email:** Email is a business communication tool. Do not transmit Restricted data via unencrypted email. Be vigilant for phishing attempts. Report suspicious messages immediately
- **Internet:** Internet access is provided for business purposes. Accessing illegal, offensive, or high-risk websites is prohibited. Downloads from untrusted sources are prohibited
- **Mobile Devices:** Devices used to access Technijian or client systems must comply with MDM policies, including screen lock, encryption, and remote wipe capability

All personnel sign the Acceptable Use Policy acknowledgment during onboarding, and re-acknowledge annually.

---

## 16. Physical Security

### 16.1 Technijian Office (HQ)

Physical security controls at 18 Technology Drive, Suite 141:

- **Access Control:** Entry requires key or badge access. Keys/badges are issued only to current employees and tracked in an access log. Badges are returned upon termination
- **Visitor Procedures:** All visitors must sign in at reception, provide identification, and be escorted by a Technijian employee at all times. Visitor logs are maintained and retained for 1 year
- **Clean Desk Policy:** Employees must clear Restricted and Confidential documents from desks and workspaces at the end of each workday and when leaving their desk unattended for extended periods. Documents are stored in locked drawers or cabinets
- **Secure Disposal:** Shred bins are provided for disposal of paper documents containing sensitive data. Cross-cut shredding is used (minimum P-4 per DIN 66399)
- **Equipment Security:** Servers, networking equipment, and other critical hardware are housed in locked areas with access restricted to authorized IT personnel
- **Monitoring:** Security cameras monitor entry points and common areas. Footage is retained for a minimum of 90 days

### 16.2 Data Center (TPX)

Physical security at the TPX data center is managed by TPX and documented in their SOC 2 Type II report. Key controls include:

- **Biometric Access Control:** Data center access requires biometric authentication (fingerprint or retinal scan) plus badge/PIN
- **24/7 Surveillance:** The facility is monitored by security cameras with 24/7 recording and on-site security personnel
- **Environmental Controls:** Redundant power (UPS + generator), redundant cooling (N+1), fire detection and suppression (pre-action dry pipe), water leak detection
- **Redundant Connectivity:** Multiple network providers with diverse entry paths

Technijian reviews the TPX SOC 2 Type II report annually and validates that complementary user entity controls are implemented.

---

## 17. Compliance and Audit

### 17.1 Regulatory Compliance

Technijian monitors and maintains compliance with applicable regulations through the following activities:

| Regulation | Compliance Activities |
|---|---|
| **HIPAA** | Business Associate Agreements with healthcare clients. Administrative, technical, and physical safeguards per the Security Rule. Breach notification procedures per the Breach Notification Rule. Annual risk assessments. |
| **SOC 2** | Technijian relies on the TPX data center's SOC 2 Type II report for production system assurance. Technijian reviews the TPX SOC 2 report annually, validates no unresolved control deficiencies, and implements all complementary user entity controls (CUECs) as specified. Technijian does not undergo its own independent SOC 2 audit. |
| **PCI-DSS** | Scope minimization (avoid storing cardholder data where possible). Encryption of payment data in transit and at rest. Access controls per PCI requirements. Annual self-assessment or QSA audit as required. |
| **FINRA / SEC** | Protection of client NPI. Books and records retention. Cybersecurity controls per regulatory guidance. Incident notification per regulatory requirements. |
| **CCPA / CPRA** | Data inventory and mapping for California consumers. Privacy notice. Data subject access and deletion request procedures. Vendor contractual requirements. |
| **FTC Safeguards Rule** | Designated qualified individual. Written information security program. Risk assessments. Access controls. Encryption. Multi-factor authentication. Incident response. |
| **GDPR** | Where applicable to EU data subjects: lawful basis for processing, data protection impact assessments, data subject rights procedures, cross-border transfer safeguards. |

The Security Officer monitors regulatory changes through industry publications, legal counsel advisories, and regulatory body communications, and updates this program accordingly.

### 17.2 Internal Audits

- **Frequency:** Annual internal review of security controls and policy compliance
- **Scope:** Review covers all sections of this Information Security Program, including access controls, data protection, network security, vendor management, HR security, physical security, and incident response readiness
- **Process:** Internal audits are conducted by the Security Officer or a designated internal reviewer who is independent of the function being audited
- **Findings:** Audit findings are documented with severity ratings, remediation actions, responsible parties, and target completion dates
- **Tracking:** Remediation items are tracked to completion. Overdue items are escalated to the CEO/Founder
- **Records:** Internal audit reports and remediation evidence are retained for a minimum of 3 years

### 17.3 External Audits and SOC 2 Reliance

- **TPX SOC 2 Type II Reliance:** Technijian does not undergo its own independent SOC 2 audit. Production systems are hosted at the TPX data center, which maintains a SOC 2 Type II report covering the Trust Services Criteria (Security, Availability, Confidentiality, and Processing Integrity). Technijian relies on the TPX SOC 2 report for assurance over the physical and environmental controls governing production infrastructure. Technijian's responsibilities under this arrangement:
  - Obtain and review the TPX SOC 2 Type II report annually upon release
  - Validate that there are no unresolved control deficiencies that affect Technijian's security posture
  - Implement and maintain all complementary user entity controls (CUECs) specified in the TPX report
  - Document the CUEC review with findings, gaps, and remediation actions
  - Provide the TPX SOC 2 report to clients upon request under NDA
- **Client Audits:** Technijian cooperates with client audit requests as permitted by contract. Information is provided under NDA. On-site visits are accommodated with reasonable advance notice
- **Regulatory Examinations:** Technijian cooperates with regulatory examinations and provides requested documentation within required timeframes

---

## 18. Program Maintenance

### 18.1 Annual Review

This Information Security Program is reviewed and approved annually by the Security Officer and CEO/Founder. The annual review incorporates:

- Regulatory and legal updates affecting information security requirements
- Lessons learned from security incidents occurring during the review period
- Findings from internal and external audits
- Results of the annual risk assessment
- Technology and infrastructure changes
- Changes in business operations, client base, or service offerings
- Employee and management feedback on policy effectiveness

### 18.2 Version History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | March 6, 2026 | Ravi Jain | Initial release |
| | | | |
| | | | |

---

*End of Document*
