# TSC - Evidence Repository

## Folder Guide

| Folder | What Goes Here | Examples |
|---|---|---|
| `access-control/` | User access reviews, MFA reports, termination checklists, privileged account lists | Entra ID access review exports, MFA status reports |
| `asset-management/` | Hardware/software inventories, disposal records, MDM reports | Intune device exports, asset disposal certificates |
| `backup-recovery/` | Backup logs, restore test results, retention policy proof | Veeam/Datto job reports, restore test screenshots |
| `change-management/` | Change tickets, CAB minutes, emergency change records | ConnectWise/ServiceNow change tickets |
| `configuration-management/` | Hardening baselines, GPO exports, CIS benchmark scans | GPO export XMLs, CIS-CAT scan results |
| `data-protection/` | Encryption configs, DLP reports, data classification records | BitLocker status, TLS config screenshots, DLP alerts |
| `endpoint-security/` | AV/EDR coverage, detection reports, endpoint compliance | SentinelOne/Defender reports, compliance dashboards |
| `incident-response/` | IR drill results, incident tickets, post-mortems | Tabletop exercise notes, incident timeline docs |
| `logging-monitoring/` | SIEM status, alert triage summaries, log retention proof | Sentinel/Splunk dashboards, alert investigation samples |
| `network-security/` | Firewall rules, vuln scans, pen test reports, network diagrams | Nessus/Qualys scans, firewall rule exports |
| `patch-management/` | Patch compliance reports, remediation timelines | WSUS/Intune patch reports, critical patch tracking |
| `physical-security/` | Badge logs, visitor logs, camera status | Access control system exports |
| `risk-management/` | Risk registers, risk assessments, treatment plans | Annual risk assessment, risk register spreadsheet |
| `security-awareness/` | Training completions, phishing sim results, onboarding records | KnowBe4/Proofpoint reports, training certificates |
| `vendor-management/` | BAAs, DPAs, vendor risk assessments, SLA reports | Signed BAAs, vendor security questionnaires |

## Naming Convention

```
{YYYY-MM-DD}--{description}.{ext}
```

Examples:
- `2026-03-01--quarterly-access-review.pdf`
- `2026-02-15--firewall-rule-export.xlsx`
- `2026-01-10--phishing-sim-results-q1.pdf`

## Collection Cadence

| Frequency | Control Domains |
|---|---|
| **Monthly** | Patch Management, Endpoint Security, Backup & Recovery |
| **Quarterly** | Access Control, Logging & Monitoring, Security Awareness, Vulnerability Scans |
| **Annually** | Risk Management, Vendor Management, Pen Testing, IR Drills, Physical Security |
| **On Change** | Change Management, Configuration Management, Asset Management |
