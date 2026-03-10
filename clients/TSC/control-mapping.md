# TSC - Control Domain to Framework Mapping

> Use this matrix to quickly locate evidence when responding to audit requests.
> Each row maps a control domain folder to the specific framework requirements it satisfies.

| # | Control Domain | Evidence Folder | HIPAA | SOC 2 (TSC) | PCI-DSS 4.0 | GDPR |
|---|---|---|---|---|---|---|
| 1 | **Access Control** | `evidence/access-control/` | §164.312(a)(1) - Access Control | CC6.1 Logical Access | Req 7 - Restrict Access; Req 8 - Identify Users | Art 32(1)(b) - Confidentiality |
| 2 | **Asset Management** | `evidence/asset-management/` | §164.310(d)(1) - Device & Media Controls | CC6.1, CC6.5 | Req 9.4 - Media Controls; Req 12.5 - Asset Inventory | Art 30 - Records of Processing |
| 3 | **Backup & Recovery** | `evidence/backup-recovery/` | §164.308(a)(7)(ii)(A) - Data Backup Plan | A1.2 - Recovery Objectives | Req 9.5 - Backup Media | Art 32(1)(c) - Availability & Resilience |
| 4 | **Change Management** | `evidence/change-management/` | §164.308(a)(8) - Evaluation | CC8.1 - Change Management | Req 6.5 - Change Management | Art 32(1)(d) - Testing & Evaluation |
| 5 | **Configuration Management** | `evidence/configuration-management/` | §164.312(a)(2)(iv) - Encryption Mechanism | CC6.1, CC7.1 | Req 2 - Secure Configurations | Art 25 - Data Protection by Design |
| 6 | **Data Protection** | `evidence/data-protection/` | §164.312(a)(2)(iv) - Encryption; §164.312(e)(1) - Transmission Security | CC6.1, CC6.7 | Req 3 - Protect Stored Data; Req 4 - Encrypt Transmissions | Art 32(1)(a) - Encryption & Pseudonymisation |
| 7 | **Endpoint Security** | `evidence/endpoint-security/` | §164.308(a)(5)(ii)(B) - Malicious Software Protection | CC6.8, CC7.1 | Req 5 - Anti-Malware; Req 6.3 - Patching | Art 32 - Security of Processing |
| 8 | **Incident Response** | `evidence/incident-response/` | §164.308(a)(6) - Security Incident Procedures | CC7.3, CC7.4, CC7.5 | Req 12.10 - Incident Response Plan | Art 33 - Breach Notification (72hr); Art 34 - Communication to Data Subject |
| 9 | **Logging & Monitoring** | `evidence/logging-monitoring/` | §164.312(b) - Audit Controls | CC7.1, CC7.2, CC7.3 | Req 10 - Log & Monitor Access; Req 10.4 - Audit Trails | Art 32 - Security of Processing |
| 10 | **Network Security** | `evidence/network-security/` | §164.312(e)(1) - Transmission Security | CC6.1, CC6.6 | Req 1 - Network Security Controls; Req 11 - Test Security | Art 32 - Security of Processing |
| 11 | **Patch Management** | `evidence/patch-management/` | §164.308(a)(1) - Risk Management | CC7.1, CC8.1 | Req 6.3 - Security Patches | Art 32(1)(d) - Testing & Evaluation |
| 12 | **Physical Security** | `evidence/physical-security/` | §164.310(a)(1) - Facility Access Controls | CC6.4 - Physical Access | Req 9 - Physical Access | Art 32(1)(b) - Physical Security |
| 13 | **Risk Management** | `evidence/risk-management/` | §164.308(a)(1)(ii)(A) - Risk Analysis | CC3.1, CC3.2, CC3.3 | Req 12.2 - Risk Assessment | Art 35 - Data Protection Impact Assessment |
| 14 | **Security Awareness** | `evidence/security-awareness/` | §164.308(a)(5) - Security Awareness Training | CC1.4, CC2.2 | Req 12.6 - Security Awareness Training | Art 39(1)(b) - Awareness Raising |
| 15 | **Vendor Management** | `evidence/vendor-management/` | §164.308(b)(1) - Business Associate Contracts | CC9.2 - Vendor Risk | Req 12.8 - Third-Party Service Providers | Art 28 - Processor Agreements |

---

## Evidence Naming Convention

Use this format for all evidence files:

```
{YYYY-MM-DD}--{description}.{ext}
```

Examples:
- `2026-03-01--quarterly-access-review.pdf`
- `2026-02-15--firewall-rule-export.xlsx`
- `2026-01-10--phishing-sim-results-q1.pdf`

## Quick Lookup by Framework

### When responding to a HIPAA audit, pull from:
- Access Control, Data Protection, Backup & Recovery, Incident Response, Logging & Monitoring, Risk Management, Security Awareness, Vendor Management (BAAs)

### When responding to a SOC 2 audit, pull from:
- All 15 domains (SOC 2 Trust Services Criteria span all control areas)

### When responding to a PCI-DSS audit, pull from:
- Network Security, Access Control, Data Protection, Endpoint Security, Patch Management, Logging & Monitoring, Physical Security, Change Management, Incident Response, Vendor Management, Risk Management, Security Awareness

### When responding to a GDPR audit, pull from:
- Data Protection, Access Control, Incident Response, Risk Management, Vendor Management, Security Awareness, Configuration Management
