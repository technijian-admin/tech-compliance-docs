# AFFG — American Fundstars Financial Group LLC
## Client Profile (sourced from client portal 2026-06-04)

**Client Code:** AFFG  
**Portal DirID:** 8141  
**Client Type:** Registered Investment Advisor / Broker-Dealer (SEC + FINRA)  
**Address:** 1 Park Plaza, Irvine, CA 92618  
**Billing Terms:** Net 30 · Sales Tax: 7.75%  
**Alternate Site:** 84 Spacial, Irvine, CA 92618

---

## Contacts

| Name | Role | Email | Notes |
|---|---|---|---|
| Iris Liu | Primary IT Contact | iris.liu@americanfundstars.com | Confirmed 2026-06-04 |
| Fan Feng | Emergency Contact | — | In BCP (verify current) |
| Joshua Yang | — | — | In BCP doc metadata (verify current) |

---

## Security Tools (Technijian-Managed)

Confirmed from portal ticket history (June 2026):

| Tool | Category | Notes |
|---|---|---|
| **Huntress** | EDR / MDR | Active monitoring — coverage drift and agent stale alerts tracked weekly. Device: LEON (workstation). |
| **Sophos Firewall** | Network Security | Hardware firewall managed by Technijian. Device: **AFFG-HQ-FW-02**. Weekly config backups, firmware updates, Central console managed. |
| **Nakivo / Veeam 365** | M365 Backup | M365 backup job `Bkp_AFFG365` running. Storage growth alerts active. |
| **Cisco Umbrella** | DNS Security | Included in multi-platform correlator alerts. |
| **Microsoft 365** | Productivity | M365 tenant — admin sign-in failure monitoring active. |
| **Synology NAS** | Local Backup | Referenced in BCP — backup storage on-premise. |

---

## Vendor / Service Provider Inventory

| Vendor | Category | Customer Data Access? | Notes |
|---|---|---|---|
| AT&T | Telecommunications | Yes | Connectivity / phone lines |
| RingCentral | Communications | Yes | Business phone/UCaaS |
| AWS | Cloud Infrastructure | Yes | Cloud hosting/storage |
| Microsoft 365 | Cloud Productivity | Yes | Email, documents, calendar |
| Synology | Local Backup | Yes | NAS backup device on-site |
| Huntress | Cybersecurity | Indirect | MDR agent on endpoints |
| Sophos | Network Security | Indirect | Firewall — managed by Technijian |
| Nakivo / Veeam | Backup | Indirect | M365 backup — Technijian-managed |
| Cisco Umbrella | DNS Security | Indirect | DNS filtering |

*Vendor list source: BCP Compliance Review findings + portal ticket history. Confirm with Iris Liu for completeness.*

---

## Systems & Devices

| Device | Type | Notes |
|---|---|---|
| AFFG-HQ-FW-02 | Sophos Firewall | Main office firewall — managed by Technijian |
| LEON | Workstation | Has Huntress agent — coverage drift alerts |
| Synology 2 Bay NAS DiskStation | Backup Appliance | On-site backup storage |

---

## Regulatory Profile

- **SEC Reg S-P** (2024 amendments) — customer data safeguarding
- **FINRA Rule 4370** — Business Continuity Plans
- **FINRA Rule 3110** — Supervision
- BCP last dated: October 2023 (stale — refresh underway, AFFG-019)

---

## Open Compliance Tickets (Ravi — Phase 1 due June 27)

| Ticket | Portal # | Priority |
|---|---|---|
| AFFG-001 Create Written IRP | 1459345 | CRITICAL |
| AFFG-002 Breach Notification Procedures | 1459346 | CRITICAL |
| AFFG-003 Service Provider Oversight Framework | 1459347 | CRITICAL |
| AFFG-017 Cybersecurity IR Integration | 1459361 | CRITICAL |
| CMMC-019 CMMC Scope Position Statement | 1459371 | Do first |

*Full ticket list in [CTO_Compliance_Work_Plan.md](../../../docs/CTO_Compliance_Work_Plan.md)*
