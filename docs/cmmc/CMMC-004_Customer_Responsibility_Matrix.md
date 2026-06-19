# Technijian, Inc.

# Customer Responsibility Matrix — NIST SP 800-171 Rev 2 (CMMC Level 2)

**Document ID:** TJN-CMMC-004
**Owner:** Technijian Corporation (Information Security)
**Classification:** Internal — provided to clients and assessors under NDA
**Status:** DRAFT for principal approval
**Version:** 0.1 (2026-06-19)
**Related:** CMMC-100 (Client-Support Program); CMMC-019 (CUI Scope); CMMC-005 (CUI/FCI Handling); CMMC-001 (SSP template); WISP and underlying policies

---

## 1. Introduction

### 1.1 What this matrix is

This **Customer Responsibility Matrix (CRM)** maps all **110 security requirements** of **NIST SP 800-171 Rev 2** (the technical baseline for **CMMC 2.0 Level 2**) to the party responsible for implementing and operating each control when a Defense Industrial Base (DIB) client engages Technijian as its managed IT services provider / External Service Provider (ESP).

It is the **keystone inheritance artifact**: a DIB client drops this CRM into its own **System Security Plan (SSP)** to show, control by control, which protections it implements itself, which it **inherits** from Technijian and the underlying data center, and which are **shared**. It also feeds the client's Plan of Action & Milestones (POA&M) and supports the client's C3PAO assessment by documenting the security-protection and backup services Technijian provides.

> **Technijian is an MSP / ESP. Technijian is NOT CMMC-certified.** This CRM does not assert that Technijian is assessed or certified to CMMC. It documents how Technijian **helps a client meet** CMMC / NIST SP 800-171 and which control responsibilities the client may inherit or share. The client (the DIB contractor / OSC — Organization Seeking Certification) remains accountable for its own assessment and for the controls assigned to it below.

### 1.2 Architectural context that drives every responsibility assignment

The responsibility split in this matrix follows directly from how Technijian's service is built (see **CMMC-019, CUI Scope Position Statement**, which controls where this document is silent or ambiguous):

- **Technijian holds only encrypted backup ciphertext.** The only client data that reaches Technijian-operated infrastructure in connection with CUI is **encrypted backup ciphertext**. **The client retains sole control of the encryption keys.**
- **Technijian cannot decrypt.** Encryption is performed **client-side** with **FIPS 140-2/3 validated** cryptography (AES-256) **before** transmission. Technijian operates no process, service account, or tooling capable of decrypting client CUI. Therefore **Technijian's systems are not a CUI processing, storage, or transmission environment** — they store ciphertext to which Technijian has no key.
- **Ciphertext at rest sits in the TPX data center.** Backups reside as ciphertext on QNAP / Nimbus storage physically located in the **TPX (TierPoint) data center**. TPX's **SOC 2 Type II** is relied upon for **physical and environmental controls**; those controls are therefore **Inherited (TPX)** in this matrix.
- **Consequence for the split.** Because Technijian cannot see CUI content, most **CUI-confidentiality controls** (marking, plaintext handling, content access) are **Client** or **Inherited**. Technijian **owns** the controls for the services it actually operates — its **segregated management plane**, the **backup/storage service**, and the **logical and personnel controls** on Technijian-managed systems.

### 1.3 Responsibility legend

| Term | Meaning |
|---|---|
| **Client** | The DIB contractor (OSC) implements and operates the control inside its own CUI environment. Technijian does not perform it because it concerns CUI content, the client's own network/endpoints, or the client's own governance. |
| **Technijian (ESP)** | Technijian implements and operates the control for the services it provides (management plane, backup/storage service, its own personnel and logical controls). Evidence comes from Technijian policies, configurations, and logs. |
| **Shared** | Both parties hold a portion. Typically Technijian operates the control on Technijian-managed systems / the backup service while the client operates the equivalent control inside its own CUI environment. The CRM note states the split. |
| **Inherited (TPX)** | The control is satisfied by the underlying data-center provider (TPX / TierPoint) and evidenced by TPX's **SOC 2 Type II** report. Applies primarily to physical and environmental protection (family 3.10). |

### 1.4 How a client uses this CRM in its SSP

1. For each of the 110 requirements, read the **Responsibility** column to see who implements it.
2. For **Client** rows, document your own implementation in your SSP as you normally would.
3. For **Technijian (ESP)**, **Shared**, and **Inherited (TPX)** rows, cite this CRM (and, on request and under NDA, the referenced Technijian policy and the TPX SOC 2 report) as your inheritance evidence; for **Shared** rows, also document the client-side portion.
4. Anything you cannot fully inherit becomes a **client SSP entry** or a **POA&M** item.

### 1.5 Important scoping caveat

**Responsibility depends on the client's actual architecture and must be confirmed per engagement.** This CRM reflects Technijian's standard **security-protection + encrypted-backup** service. If a given engagement expands Technijian's role (e.g., Technijian manages client endpoints, identity, firewalls, or a CUI enclave), responsibilities shift toward **Shared** or **Technijian**. Rows whose assignment depends on the specific engagement architecture are marked **[VERIFY per engagement]**. The final, client-specific CRM is produced and signed per client; this document is the **template**.

---

## 2. Responsibility matrix by family

> Legend recap: **Client** · **Technijian (ESP)** · **Shared** · **Inherited (TPX)**. Requirement text is a faithful short paraphrase of NIST SP 800-171 Rev 2; consult the standard for exact wording.

### 3.1 Access Control (22 controls: 3.1.1–3.1.22)

| Control ID | Requirement (short) | Responsibility | How Technijian supports / inheritance note |
|---|---|---|---|
| 3.1.1 | Limit system access to authorized users, processes, and devices | **Shared** | Client controls access to its CUI systems. Technijian enforces least-privilege access to the management plane and backup service per [Access Control Policy](../Access_Control_Policy.md). |
| 3.1.2 | Limit access to the transactions/functions authorized users may execute | **Shared** | Client scopes function-level access in its environment; Technijian role-restricts admin functions on Technijian-managed systems ([Access Control Policy](../Access_Control_Policy.md), §2 least privilege). |
| 3.1.3 | Control the flow of CUI per approved authorizations | **Client** | CUI flows occur in the client environment; ciphertext-only at Technijian (no CUI flow to control). See [CMMC-019](CMMC-019_CUI_Scope_Position_Statement.md). |
| 3.1.4 | Separate duties of individuals to reduce malevolent activity risk | **Shared** | Client enforces SoD in its environment; Technijian enforces SoD for its operations ([Access Control Policy](../Access_Control_Policy.md), §2.2; [WISP](../Information_Security_Program_WISP.md)). |
| 3.1.5 | Employ least privilege, including for privileged accounts | **Shared** | Both parties; Technijian PAM, JIT, and privileged-account separation per [Access Control Policy](../Access_Control_Policy.md), §6. |
| 3.1.6 | Use non-privileged accounts for non-security functions | **Shared** | Technijian privileged/standard account separation ([Access Control Policy](../Access_Control_Policy.md), §6.1); client mirrors in its environment. |
| 3.1.7 | Prevent non-privileged users from executing privileged functions; capture in audit logs | **Shared** | Technijian privileged-action logging ([Access Control Policy](../Access_Control_Policy.md), §6.1); client implements for its systems. |
| 3.1.8 | Limit unsuccessful logon attempts | **Shared** | Technijian lockout thresholds ([Access Control Policy](../Access_Control_Policy.md), §4.2); client enforces on CUI systems. |
| 3.1.9 | Provide privacy and security notices consistent with CUI rules | **Client** | Logon banners on CUI systems are client-owned. Technijian provides equivalents on its own systems where applicable. |
| 3.1.10 | Use session lock with pattern-hiding displays after inactivity | **Shared** | Technijian session-lock standards ([Access Control Policy](../Access_Control_Policy.md), §4.3, §7.2); client enforces on CUI endpoints. |
| 3.1.11 | Terminate user sessions after a defined condition | **Shared** | Technijian session timeout/termination ([Access Control Policy](../Access_Control_Policy.md), §4.3); client on its systems. |
| 3.1.12 | Monitor and control remote access sessions | **Shared** | Technijian VPN/ZTNA, logging of remote sessions ([Access Control Policy](../Access_Control_Policy.md), §7); client controls remote access to its CUI environment. |
| 3.1.13 | Use cryptographic mechanisms to protect remote access sessions | **Shared** | Technijian TLS/IPsec AES-256 tunnels ([Access Control Policy](../Access_Control_Policy.md), §7.1); client for its own remote access. |
| 3.1.14 | Route remote access through managed access control points | **Shared** | Technijian routes admin access through controlled VPN/ZTNA points ([Access Control Policy](../Access_Control_Policy.md), §7.3); client for its environment. |
| 3.1.15 | Authorize remote execution of privileged commands and remote access to security-relevant info | **Shared** | Technijian authorizes/logs privileged remote actions ([Access Control Policy](../Access_Control_Policy.md), §6, §7); client for its systems. |
| 3.1.16 | Authorize wireless access prior to allowing connections | **Client** | Wireless policy applies to the client's CUI network. Technijian governs its own corporate wireless; **[VERIFY per engagement]** if Technijian manages client wireless. |
| 3.1.17 | Protect wireless access using authentication and encryption | **Client** | Client-owned for the CUI network; Technijian secures its own WLAN. **[VERIFY per engagement]**. |
| 3.1.18 | Control connection of mobile devices | **Client** | Mobile-device connection to CUI systems is client-owned. **[VERIFY per engagement]** if Technijian provides MDM. |
| 3.1.19 | Encrypt CUI on mobile devices and mobile computing platforms | **Client** | CUI never resides in plaintext on Technijian devices; client encrypts CUI on its mobile platforms. See [Data Classification & Retention Policy](../Data_Classification_Retention_Policy.md). |
| 3.1.20 | Verify/control/limit connections to external systems | **Shared** | Technijian controls external connections of its managed systems ([Access Control Policy](../Access_Control_Policy.md), §7–8); client for its CUI boundary. |
| 3.1.21 | Limit use of portable storage devices on external systems | **Client** | Portable-media use around CUI is client-owned; Technijian media controls per [Data Classification & Retention Policy](../Data_Classification_Retention_Policy.md). |
| 3.1.22 | Control CUI posted/processed on publicly accessible systems | **Client** | Public-facing content review is a client governance function; no CUI is published from Technijian systems. |

### 3.2 Awareness & Training (3 controls: 3.2.1–3.2.3)

| Control ID | Requirement (short) | Responsibility | How Technijian supports / inheritance note |
|---|---|---|---|
| 3.2.1 | Make managers/admins/users aware of security risks of their activities | **Shared** | Technijian trains its own personnel ([Employee Security Policy](../Employee_Security_Policy.md)); client trains its CUI workforce. |
| 3.2.2 | Train personnel to carry out assigned security-related duties | **Shared** | Technijian role-based security training for its staff ([Employee Security Policy](../Employee_Security_Policy.md); [WISP](../Information_Security_Program_WISP.md)); client for its roles. |
| 3.2.3 | Provide insider-threat awareness training | **Shared** | Technijian insider-threat awareness for its staff ([Employee Security Policy](../Employee_Security_Policy.md)); client for its workforce. |

### 3.3 Audit & Accountability (9 controls: 3.3.1–3.3.9)

| Control ID | Requirement (short) | Responsibility | How Technijian supports / inheritance note |
|---|---|---|---|
| 3.3.1 | Create and retain system audit logs enabling monitoring/analysis/investigation | **Shared** | Technijian logs management-plane and backup-service activity ([Access Control Policy](../Access_Control_Policy.md), §10; [WISP](../Information_Security_Program_WISP.md)); client logs its CUI systems. |
| 3.3.2 | Ensure actions can be uniquely traced to individual users (accountability) | **Shared** | Technijian unique-ID + privileged-action logging ([Access Control Policy](../Access_Control_Policy.md), §3.2, §6.1); client for its environment. |
| 3.3.3 | Review and update logged events | **Shared** | Technijian reviews its log scope periodically ([WISP](../Information_Security_Program_WISP.md)); client for its systems. |
| 3.3.4 | Alert on audit logging process failure | **Shared** | Technijian monitors/alerts on its logging pipeline; client for its CUI systems. |
| 3.3.5 | Correlate audit review/analysis/reporting for investigation | **Shared** | Technijian correlation via its monitoring/SIEM for its systems ([Incident Response Plan](../Incident_Response_Plan_IRP.md)); client for its environment. |
| 3.3.6 | Provide audit record reduction and report generation | **Shared** | Technijian tooling for its logs; client for its CUI systems. |
| 3.3.7 | Use authoritative time source to synchronize records | **Shared** | Technijian NTP-synced timestamps on its systems; client for its environment. |
| 3.3.8 | Protect audit information and tools from unauthorized access/modification/deletion | **Shared** | Technijian tamper-protected, access-restricted logs ([Access Control Policy](../Access_Control_Policy.md), §6.1); client for its logs. |
| 3.3.9 | Limit management of audit logging to a privileged subset of users | **Shared** | Technijian restricts log management to privileged admins ([Access Control Policy](../Access_Control_Policy.md), §6); client for its systems. |

### 3.4 Configuration Management (9 controls: 3.4.1–3.4.9)

| Control ID | Requirement (short) | Responsibility | How Technijian supports / inheritance note |
|---|---|---|---|
| 3.4.1 | Establish/maintain baseline configurations and inventories | **Shared** | Technijian baselines and asset inventory for its managed systems ([Change Management Policy](../Change_Management_Policy.md)); client for its CUI assets. |
| 3.4.2 | Establish/enforce security configuration settings | **Shared** | Technijian hardening standards on its systems ([Change Management Policy](../Change_Management_Policy.md)); client for its environment. |
| 3.4.3 | Track, review, approve/disapprove, and log system changes | **Shared** | Technijian change-control workflow ([Change Management Policy](../Change_Management_Policy.md)); client for changes in its CUI environment. |
| 3.4.4 | Analyze the security impact of changes before implementation | **Shared** | Technijian security-impact analysis in change process ([Change Management Policy](../Change_Management_Policy.md)); client for its systems. |
| 3.4.5 | Define/document/approve/enforce access restrictions for changes | **Shared** | Technijian restricts who may change its systems ([Change Management Policy](../Change_Management_Policy.md); [Access Control Policy](../Access_Control_Policy.md), §6); client for its environment. |
| 3.4.6 | Employ least functionality (essential capabilities only) | **Shared** | Technijian disables unnecessary services on its systems ([Change Management Policy](../Change_Management_Policy.md)); client for its CUI systems. |
| 3.4.7 | Restrict/disable/prevent nonessential programs, ports, protocols, services | **Shared** | Technijian on its managed systems; client on its CUI systems. |
| 3.4.8 | Apply deny-by-exception (blacklist) or permit-by-exception (whitelist) for software | **Shared** | Technijian application-control on its systems; client for its environment. **[VERIFY per engagement]** if Technijian manages client endpoints. |
| 3.4.9 | Control and monitor user-installed software | **Shared** | Technijian controls software installs on its systems; client for its CUI endpoints. **[VERIFY per engagement]**. |

### 3.5 Identification & Authentication (11 controls: 3.5.1–3.5.11)

| Control ID | Requirement (short) | Responsibility | How Technijian supports / inheritance note |
|---|---|---|---|
| 3.5.1 | Identify system users, processes, and devices | **Shared** | Technijian unique identifiers for its accounts/service accounts ([Access Control Policy](../Access_Control_Policy.md), §3); client for its environment. |
| 3.5.2 | Authenticate (or verify) identities before granting access | **Shared** | Technijian authentication on its systems ([Access Control Policy](../Access_Control_Policy.md), §4); client for its CUI systems. |
| 3.5.3 | Use multifactor authentication for local/network access to privileged accounts and network access to non-privileged accounts | **Shared** | Technijian MFA per [Access Control Policy](../Access_Control_Policy.md), §4.1 (TOTP/FIDO2; SMS prohibited for privileged); client enforces MFA on its CUI access. |
| 3.5.4 | Employ replay-resistant authentication for network access | **Shared** | Technijian uses replay-resistant mechanisms (TLS, modern MFA) on its systems; client for its environment. |
| 3.5.5 | Prevent reuse of identifiers for a defined period | **Shared** | Technijian identifier-management practice ([Access Control Policy](../Access_Control_Policy.md), §3); client for its systems. |
| 3.5.6 | Disable identifiers after a defined period of inactivity | **Shared** | Technijian disables inactive accounts (45 days) ([Access Control Policy](../Access_Control_Policy.md), §3.3); client for its environment. |
| 3.5.7 | Enforce a minimum password complexity and change of characters when new passwords are created | **Shared** | Technijian password complexity standards ([Access Control Policy](../Access_Control_Policy.md), §4.2); client for its systems. |
| 3.5.8 | Prohibit password reuse for a specified number of generations | **Shared** | Technijian password-history enforcement ([Access Control Policy](../Access_Control_Policy.md), §4.2); client for its environment. |
| 3.5.9 | Allow temporary password use for system logons with immediate change to a permanent password | **Shared** | Technijian temporary-credential practice ([Access Control Policy](../Access_Control_Policy.md), §3–4); client for its systems. |
| 3.5.10 | Store and transmit only cryptographically-protected passwords | **Shared** | Technijian vaulting/hashing of credentials ([Access Control Policy](../Access_Control_Policy.md), §4.2, §6.1); client for its environment. |
| 3.5.11 | Obscure feedback of authentication information | **Shared** | Technijian masks authentication feedback on its systems; client for its CUI systems. |

### 3.6 Incident Response (3 controls: 3.6.1–3.6.3)

| Control ID | Requirement (short) | Responsibility | How Technijian supports / inheritance note |
|---|---|---|---|
| 3.6.1 | Establish an operational incident-handling capability (prep, detect, analyze, contain, recover, respond) | **Shared** | Technijian operates an IR capability for its systems and supports client IR for events affecting the backup/management service ([Incident Response Plan](../Incident_Response_Plan_IRP.md)); client owns IR for its CUI environment. |
| 3.6.2 | Track, document, and report incidents to designated internal/external authorities | **Shared** | Technijian notifies the client per the engagement/SLA and documents incidents ([Incident Response Plan](../Incident_Response_Plan_IRP.md)); client performs DoD/DIBNet (DFARS 252.204-7012) reporting. **[VERIFY per engagement]** for notification timelines. |
| 3.6.3 | Test the organizational incident-response capability | **Shared** | Technijian tests its IR plan ([Incident Response Plan](../Incident_Response_Plan_IRP.md)); client tests its own. |

### 3.7 Maintenance (6 controls: 3.7.1–3.7.6)

| Control ID | Requirement (short) | Responsibility | How Technijian supports / inheritance note |
|---|---|---|---|
| 3.7.1 | Perform maintenance on organizational systems | **Shared** | Technijian maintains its managed systems and the backup service ([Change Management Policy](../Change_Management_Policy.md); [BCP/DR](../Business_Continuity_Disaster_Recovery_Plan_BCP_DR.md)); client maintains its CUI systems. |
| 3.7.2 | Control tools, techniques, mechanisms, and personnel used for maintenance | **Shared** | Technijian controls maintenance tools/personnel for its systems ([Change Management Policy](../Change_Management_Policy.md)); client for its environment. |
| 3.7.3 | Sanitize equipment for off-site maintenance to remove CUI | **Client** | No CUI plaintext on Technijian equipment; ciphertext-only. Client sanitizes CUI-bearing equipment. See [Data Classification & Retention Policy](../Data_Classification_Retention_Policy.md). |
| 3.7.4 | Check media containing diagnostic/test programs for malicious code | **Shared** | Technijian scans diagnostic media used on its systems; client for its environment. |
| 3.7.5 | Require MFA to establish nonlocal maintenance sessions and terminate when complete | **Shared** | Technijian MFA + session termination for remote maintenance ([Access Control Policy](../Access_Control_Policy.md), §4.1, §7); client for its systems. |
| 3.7.6 | Supervise maintenance activities of personnel without required access | **Shared** | Technijian supervises uncleared maintenance personnel on its systems; client for its environment. |

### 3.8 Media Protection (9 controls: 3.8.1–3.8.9)

| Control ID | Requirement (short) | Responsibility | How Technijian supports / inheritance note |
|---|---|---|---|
| 3.8.1 | Protect (physically control and securely store) system media containing CUI | **Shared / Inherited (TPX)** | Technijian holds **ciphertext-only** media in the TPX DC (no CUI plaintext); physical control of that media is **Inherited (TPX)** SOC 2. Client protects CUI plaintext media. See [CMMC-019](CMMC-019_CUI_Scope_Position_Statement.md). |
| 3.8.2 | Limit access to CUI on system media to authorized users | **Client** | CUI plaintext access control is client-owned; Technijian cannot access ciphertext content ([CMMC-019](CMMC-019_CUI_Scope_Position_Statement.md)). |
| 3.8.3 | Sanitize or destroy media containing CUI before disposal or reuse | **Shared** | Technijian sanitizes/destroys its storage media (holding only ciphertext) per [Data Classification & Retention Policy](../Data_Classification_Retention_Policy.md); client sanitizes CUI plaintext media. |
| 3.8.4 | Mark media with necessary CUI markings and distribution limitations | **Client** | CUI marking is a client content function; Technijian cannot see content to mark it ([CMMC-005](CMMC-005_CUI_FCI_Handling_Procedures.md); [Data Classification & Retention Policy](../Data_Classification_Retention_Policy.md)). |
| 3.8.5 | Control access to media during transport outside controlled areas | **Shared** | Technijian controls ciphertext media in transit (encrypted) for the backup service; client controls CUI plaintext media transport. |
| 3.8.6 | Use cryptographic mechanisms to protect CUI on digital media during transport (unless physically safeguarded) | **Shared** | Client-side FIPS-validated encryption (AES-256) protects backup data in transit; client for its own media. See [CMMC-019](CMMC-019_CUI_Scope_Position_Statement.md). |
| 3.8.7 | Control the use of removable media on system components | **Client** | Removable-media control around CUI is client-owned; Technijian media controls per [Data Classification & Retention Policy](../Data_Classification_Retention_Policy.md). **[VERIFY per engagement]** if Technijian manages client endpoints. |
| 3.8.8 | Prohibit use of portable storage devices with no identifiable owner | **Client** | Client policy on its CUI systems; Technijian equivalent on its own systems. |
| 3.8.9 | Protect the confidentiality of backup CUI at storage locations | **Shared / Inherited (TPX)** | **Core Technijian service:** ciphertext-only backup at rest on QNAP/Nimbus in the TPX DC; **client holds keys** so confidentiality is preserved even from Technijian. Physical storage protection **Inherited (TPX)** SOC 2. See [BCP/DR](../Business_Continuity_Disaster_Recovery_Plan_BCP_DR.md) and [CMMC-019](CMMC-019_CUI_Scope_Position_Statement.md). |

### 3.9 Personnel Security (2 controls: 3.9.1–3.9.2)

| Control ID | Requirement (short) | Responsibility | How Technijian supports / inheritance note |
|---|---|---|---|
| 3.9.1 | Screen individuals prior to authorizing access to systems containing CUI | **Shared** | Technijian screens its personnel (background checks) before granting access to its systems ([Employee Security Policy](../Employee_Security_Policy.md); [Access Control Policy](../Access_Control_Policy.md), §9.1); client screens its own CUI personnel. |
| 3.9.2 | Ensure CUI and systems are protected during/after personnel actions (termination/transfer) | **Shared** | Technijian same-day deprovisioning and credential rotation ([Access Control Policy](../Access_Control_Policy.md), §9.2; [Employee Security Policy](../Employee_Security_Policy.md)); client for its workforce. |

### 3.10 Physical Protection (6 controls: 3.10.1–3.10.6)

| Control ID | Requirement (short) | Responsibility | How Technijian supports / inheritance note |
|---|---|---|---|
| 3.10.1 | Limit physical access to systems, equipment, and operating environments to authorized individuals | **Inherited (TPX)** | Backup storage resides in the **TPX data center**; physical access control is satisfied by **TPX SOC 2 Type II**. Client controls physical access to its own CUI facilities. |
| 3.10.2 | Protect and monitor the physical facility and support infrastructure | **Inherited (TPX)** | TPX provides facility monitoring, power, HVAC, fire suppression (SOC 2 Type II). Client for its own sites. |
| 3.10.3 | Escort visitors and monitor visitor activity | **Inherited (TPX)** | TPX visitor escort/monitoring at the DC (SOC 2 Type II). Client for its own facilities. |
| 3.10.4 | Maintain audit logs of physical access | **Inherited (TPX)** | TPX physical-access logging (SOC 2 Type II). Client for its facilities. |
| 3.10.5 | Control and manage physical access devices (keys, badges, locks) | **Inherited (TPX)** | TPX manages badges/keys/locks at the DC (SOC 2 Type II). Client for its facilities. |
| 3.10.6 | Enforce safeguarding measures for CUI at alternate work sites | **Client** | Remote/alternate-site safeguarding of CUI is client-owned; Technijian applies equivalent controls to its own remote workforce ([Access Control Policy](../Access_Control_Policy.md), §7). |

### 3.11 Risk Assessment (3 controls: 3.11.1–3.11.3)

| Control ID | Requirement (short) | Responsibility | How Technijian supports / inheritance note |
|---|---|---|---|
| 3.11.1 | Periodically assess risk to operations, assets, and individuals from system operation/CUI processing | **Shared** | Technijian assesses risk to its services ([WISP](../Information_Security_Program_WISP.md); [Vendor Risk Management Policy](../Vendor_Risk_Management_Policy.md)); client assesses risk to its CUI environment. |
| 3.11.2 | Scan for vulnerabilities periodically and when new vulnerabilities are identified | **Shared** | Technijian vulnerability scanning of its managed systems ([WISP](../Information_Security_Program_WISP.md)); client scans its CUI systems. **[VERIFY per engagement]** if Technijian scans client assets. |
| 3.11.3 | Remediate vulnerabilities in accordance with risk assessments | **Shared** | Technijian remediates on its systems ([Change Management Policy](../Change_Management_Policy.md)); client for its environment. |

### 3.12 Security Assessment (4 controls: 3.12.1–3.12.4)

| Control ID | Requirement (short) | Responsibility | How Technijian supports / inheritance note |
|---|---|---|---|
| 3.12.1 | Periodically assess security controls for effectiveness | **Shared** | Technijian assesses its own control effectiveness ([WISP](../Information_Security_Program_WISP.md)); client assesses its 800-171 controls for its SSP. |
| 3.12.2 | Develop and implement plans of action (POA&Ms) to correct deficiencies | **Shared** | Technijian maintains remediation plans for its services; client owns its 800-171 POA&M. |
| 3.12.3 | Monitor security controls on an ongoing basis | **Shared** | Technijian continuous monitoring of its systems ([WISP](../Information_Security_Program_WISP.md); [Incident Response Plan](../Incident_Response_Plan_IRP.md)); client for its environment. |
| 3.12.4 | Develop, document, and periodically update a System Security Plan (SSP) | **Client** | The 800-171 SSP belongs to the client (the OSC). Technijian provides this CRM and supporting evidence as inheritance inputs ([CMMC-001](CMMC-001_SSP_Template.md)). |

### 3.13 System & Communications Protection (16 controls: 3.13.1–3.13.16)

| Control ID | Requirement (short) | Responsibility | How Technijian supports / inheritance note |
|---|---|---|---|
| 3.13.1 | Monitor/control/protect communications at external and key internal boundaries | **Shared** | Technijian protects the boundary of its management plane / backup service ([Access Control Policy](../Access_Control_Policy.md), §7; [WISP](../Information_Security_Program_WISP.md)); client protects its CUI boundary. |
| 3.13.2 | Employ architectural designs/techniques that promote effective information security | **Shared** | Technijian secure-architecture practices for its services ([WISP](../Information_Security_Program_WISP.md); [Change Management Policy](../Change_Management_Policy.md)); client for its environment. |
| 3.13.3 | Separate user functionality from system management functionality | **Shared** | Technijian segregates its **management plane** from user-facing functions ([Access Control Policy](../Access_Control_Policy.md), §6); client for its systems. |
| 3.13.4 | Prevent unauthorized and unintended information transfer via shared system resources | **Shared** | Technijian multi-tenant isolation on its systems ([Access Control Policy](../Access_Control_Policy.md), §8 cross-client isolation); client for its environment. |
| 3.13.5 | Implement subnetworks for publicly accessible components, separated from internal networks | **Shared** | Technijian network segmentation/DMZ for its services; client for its CUI network. |
| 3.13.6 | Deny network traffic by default and allow by exception (deny-all, permit-by-exception) | **Shared** | Technijian default-deny firewall posture on its managed systems; client for its environment. |
| 3.13.7 | Prevent remote devices from simultaneously connecting and communicating with non-organizational networks (split tunneling) | **Shared** | Technijian disables split tunneling on its VPN ([Access Control Policy](../Access_Control_Policy.md), §7.1); client for its remote access. |
| 3.13.8 | Use cryptographic mechanisms to prevent unauthorized disclosure of CUI in transit (unless otherwise protected) | **Shared** | Client-side FIPS-validated encryption (AES-256) + TLS 1.2+ protect backup data in transit; client protects CUI in transit in its environment. See [CMMC-019](CMMC-019_CUI_Scope_Position_Statement.md). |
| 3.13.9 | Terminate network connections at end of session or after inactivity | **Shared** | Technijian session-termination on its systems ([Access Control Policy](../Access_Control_Policy.md), §4.3, §7.1); client for its environment. |
| 3.13.10 | Establish and manage cryptographic keys for cryptography employed | **Client** | **Client holds and manages all keys** for CUI/backup encryption; Technijian has no key access ([CMMC-019](CMMC-019_CUI_Scope_Position_Statement.md)). Technijian manages keys only for its own internal systems. |
| 3.13.11 | Employ FIPS-validated cryptography when used to protect CUI confidentiality | **Shared** | Backup encryption uses **FIPS 140-2/3 validated** client-side cryptography; client ensures FIPS validation across its own CUI cryptography. See [CMMC-019](CMMC-019_CUI_Scope_Position_Statement.md). |
| 3.13.12 | Prohibit remote activation of collaborative computing devices; indicate use to users | **Client** | Camera/mic collaborative-device policy applies to client CUI endpoints; Technijian equivalent on its own devices. |
| 3.13.13 | Control and monitor use of mobile code | **Shared** | Technijian mobile-code controls on its systems; client for its environment. |
| 3.13.14 | Control and monitor use of Voice over IP (VoIP) | **Client** | VoIP governance for the CUI environment is client-owned; Technijian for its own VoIP. **[VERIFY per engagement]** if Technijian provides VoIP. |
| 3.13.15 | Protect the authenticity of communications sessions | **Shared** | Technijian uses authenticated, integrity-protected sessions (TLS/IPsec) on its systems; client for its environment. |
| 3.13.16 | Protect the confidentiality of CUI at rest | **Shared / Inherited (TPX)** | **Core Technijian service:** CUI backup is stored as **ciphertext only** (client-held keys) on QNAP/Nimbus at TPX; physical protection **Inherited (TPX)** SOC 2. Client protects CUI at rest in its own environment. See [BCP/DR](../Business_Continuity_Disaster_Recovery_Plan_BCP_DR.md) and [CMMC-019](CMMC-019_CUI_Scope_Position_Statement.md). |

### 3.14 System & Information Integrity (7 controls: 3.14.1–3.14.7)

| Control ID | Requirement (short) | Responsibility | How Technijian supports / inheritance note |
|---|---|---|---|
| 3.14.1 | Identify, report, and correct system flaws in a timely manner | **Shared** | Technijian patch/flaw remediation on its managed systems ([Change Management Policy](../Change_Management_Policy.md); [WISP](../Information_Security_Program_WISP.md)); client for its CUI systems. |
| 3.14.2 | Provide protection from malicious code at appropriate locations | **Shared** | Technijian EDR/anti-malware on its systems ([Access Control Policy](../Access_Control_Policy.md), §7.2; [WISP](../Information_Security_Program_WISP.md)); client for its environment. **[VERIFY per engagement]** if Technijian provides client-endpoint EDR. |
| 3.14.3 | Monitor system security alerts and advisories and act in response | **Shared** | Technijian consumes/acts on advisories for its systems ([WISP](../Information_Security_Program_WISP.md); [Incident Response Plan](../Incident_Response_Plan_IRP.md)); client for its environment. |
| 3.14.4 | Update malicious-code protection mechanisms when new releases are available | **Shared** | Technijian keeps anti-malware signatures/engines current on its systems; client for its environment. |
| 3.14.5 | Perform periodic and real-time scans of files from external sources | **Shared** | Technijian real-time/scheduled scanning on its systems; client for its CUI systems. |
| 3.14.6 | Monitor systems, including inbound/outbound traffic, to detect attacks and indicators of potential attacks | **Shared** | Technijian network/host monitoring for its services ([Incident Response Plan](../Incident_Response_Plan_IRP.md); [WISP](../Information_Security_Program_WISP.md)); client for its environment. |
| 3.14.7 | Identify unauthorized use of organizational systems | **Shared** | Technijian anomaly detection on its systems ([Access Control Policy](../Access_Control_Policy.md), §10.2); client for its CUI environment. |

---

## 3. Summary counts

Approximate responsibility distribution across the **110** NIST SP 800-171 Rev 2 requirements for Technijian's **standard security-protection + encrypted-backup** engagement. **Counts vary by engagement** — rows marked **[VERIFY per engagement]** can shift toward **Shared** or **Technijian** when Technijian manages additional client infrastructure (endpoints, identity, firewalls, a CUI enclave).

| Responsibility | Approx. count | Where it concentrates |
|---|---|---|
| **Client** | ~18 | CUI content, marking, plaintext handling, key management, the SSP, wireless/mobile/VoIP/collaborative devices in the client environment |
| **Technijian (ESP)** | ~0–2 (standard) | Pure Technijian-only rows are few; most Technijian obligations appear as **Shared** because the client must implement the equivalent in its own environment. Expands toward Technijian-owned where Technijian operates more of the client stack. |
| **Shared** | ~80 | Logical/operational controls Technijian operates for its management plane + backup service while the client operates the equivalent for its CUI environment (access control, audit, config mgmt, I&A, IR, maintenance, risk/assessment, SC, SI) |
| **Inherited (TPX)** | ~6 (+2 partial) | Physical/environmental protection (all of 3.10 except 3.10.6) plus the physical-storage portion of 3.8.1, 3.8.9, 3.13.16 |

> The large **Shared** count is expected and correct: for almost every operational control, Technijian implements it on the systems it runs and the client implements it on the systems it runs. Each client's signed CRM resolves these into the precise split for that engagement.

---

## 4. Assumptions & limits

1. **Technijian cannot decrypt client CUI.** This is the controlling fact behind the entire matrix. Technijian holds only **encrypted backup ciphertext**; the **client holds the keys**; Technijian has **no decryption capability**. Consequently Technijian's systems are **not a CUI processing environment**, and CUI-content-confidentiality controls fall to the **Client** or are satisfied as **Shared/Inherited** at the storage layer only. See **[CMMC-019](CMMC-019_CUI_Scope_Position_Statement.md)** (which governs where this document is silent or ambiguous).
2. **Physical/environmental controls are inherited from TPX.** Family **3.10** (except 3.10.6, alternate work sites) and the physical-storage portions of **3.8.1 / 3.8.9 / 3.13.16** are satisfied by the **TPX (TierPoint) data center** and evidenced by its **SOC 2 Type II** report, available to the client/assessor under NDA.
3. **Engagement-dependent rows are marked [VERIFY per engagement].** Where a row's assignment depends on whether Technijian manages client endpoints, identity, wireless, VoIP, MDM, or a CUI enclave, the standard assignment shown is the **baseline**; the actual split is confirmed and recorded in the client-specific CRM.
4. **This CRM is a template.** It is **finalized per client** against that client's real architecture, the contracted scope (SOW/MSA, including any DoD/DFARS 252.204-7012 addendum), and the assessor's scoping decisions. The signed, client-specific CRM — not this template — is what the client incorporates into its SSP.
5. **Technijian is not CMMC-certified.** Technijian is an MSP/ESP that **helps** clients meet CMMC / NIST SP 800-171. Nothing in this matrix asserts that Technijian itself is assessed or certified, nor relieves the client (OSC) of accountability for its own assessment and the controls assigned to it.
6. **Assessor validation required.** Asset categorization (Security Protection Asset vs. CUI Asset) and the "encrypted-with-no-key-access ≠ CUI handling" position must be confirmed with the client's C3PAO per engagement; interpretations vary by assessor.

---

## 5. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Principal / CEO | Ravi Jain | ________________ | __________ |
| Information Security Lead | ________________ | ________________ | __________ |

---

### Version history
| Ver | Date | Author | Change |
|---|---|---|---|
| 0.1 | 2026-06-19 | Technijian InfoSec | Initial draft for approval — all 110 NIST SP 800-171 Rev 2 controls mapped across 14 families |
