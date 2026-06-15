# AFFG Cyber-Insurance Application — Fill Report (DRAFT)

**Applicant:** American Fundstars Financial Group LLC ("AFFG") — dually registered RIA / broker-dealer, 1 Park Plaza, Ste 210, Irvine, CA 92618
**Prepared by:** Technijian, Inc. (outsourced managed IT / security provider) — Ravi Jain, CEO · rjain@technijian.com · 949-379-8499
**Date prepared:** 2026-06-15
**Status:** DRAFT for AFFG review and signature. These are **sworn applications**. Do **not** sign until AFFG has verified every `[VERIFY]` item below and filled the `[AFFG]` financial/identity blanks.

## Output files (filled, values verified on re-open)
- `REDY Cyber Application_FILLED.pdf` — 55 fields set, read-back verified 55/55, NeedAppearances=true.
- `Tokio Marine -HCC - Cyber Liability Application_FILLED.pdf` — 87 fields set, read-back verified 87/87, NeedAppearances=true.

Blank source PDFs were **not** modified. Every value below was confirmed by re-opening the filled file and reading each field's stored value.

---

## How honest-answer constraints were applied
- **Loss history = CLEAN.** Every loss / incident / claim / breach / extortion / outage / regulatory-proceeding question answered **No**. (The June-12 alerts were false positives and are not referenced.)
- **Tested IRP = No** (REDY Q23) — being created under the compliance program.
- **Backup restoration tested in last 6 months = left UNCHECKED** (REDY Q16 "Test" radio; Tokio §8c box #7) — restore test not yet confirmed.
- **All `[AFFG]` financial/numeric fields left BLANK** (revenue, employee count, PII record counts, dates) — AFFG must supply.
- **Signature fields left BLANK** on both forms.

---

# FORM 1 — REDY Cyber Application
**File:** `REDY Cyber Application_FILLED.pdf` · 3 pages · 103 fields · 55 set · 48 deliberately blank/Off · 0 failed.

## Fields SET (value shown)
| Field | Value |
|---|---|
| Full Name of Applicant | American Fundstars Financial Group LLC |
| Mailing Address | 1 Park Plaza, Ste 210, Irvine, CA 92618 |
| Physical Address | 1 Park Plaza, Ste 210, Irvine, CA 92618 |
| Nature of business industry | Investment Adviser / Broker-Dealer (dually registered RIA/BD) |
| NAICS | 523930  **[VERIFY]** |
| Do you have a company website | Yes |
| Company Website | www.americanfundstars.com |
| Q1 business activities | **None of the Above** (Adult/Cannabis/Crypto/Debt/Gambling/Data-Aggregation/MSP/Managed-Care/Payment-Processing all left unchecked) |
| Q2a data stored | **Personal Information** only |
| Q2b healthcare records | 0 |
| Q2c payment-card transaction records | 0 |
| Q3 prevent unauthorized employees initiating wires | Yes  **[VERIFY]** |
| Q4 secondary validation for funds transfers | **For ALL Requests**  **[VERIFY]** |
| Q5 verify vendor/supplier bank accounts before AP | Yes  **[VERIFY]** |
| Q6 maintain secured backups | Yes |
| Q7 protect sensitive data | **Encrypt at Rest** + **Encrypt in External Emails**  **[VERIFY]** |
| Q8 sensitive info on cloud | Yes |
| Q8a backup frequency | **Weekly or More** |
| Q8b backups offline/cloud | **Cloud Service Provider** |
| Q9 MFA enforced for | **Email, Remote Access, VPN/Network Auth, Mission Critical Systems, Admin/Privileged-only**  **[VERIFY scope]** |
| Q10 mandatory infosec training annually | Yes (PHT) |
| Q11 content review/removal procedures | No |
| Q12 website-content complaints (3 yrs) | No |
| Q13 outside/inside counsel for IP review | No |
| Q14 biometric records annually | 0 |
| Q15 EDR covering 100% of environment | Yes  **[VERIFY — confirm all endpoints covered, legacy desktops retired]** |
| Q16 backups subject to measures | **MFA, Segmentation, Virus/Malware Scanning, Immutable, Encryption, Online/Designated Cloud**  (Test left UNCHECKED)  **[VERIFY]** |
| Q17 formal 30-day patch cadence, critical/zero-day ≤7 days | Yes  **[VERIFY]** |
| Q18 create content for others | No |
| Q19 experienced cyber extortion | No |
| Q20 revenue-generating ops outside domiciled country | No |
| Q21 update frequency critical systems/apps | **Weekly or More**  **[VERIFY]** |
| Q22 breach requiring notification (5 yrs) | No |
| Q23 IR plan tested & in effect | **No** (being created) |
| Q24 device protection | **Anti-virus, Anti-malware, Endpoint Protection Software, Firewall**; EDR product = **CrowdStrike Falcon Insight EDR** |
| Q25 email precautions | **Screening Attachments, Screening Links, Tagging External Emails** |
| Q26 prior incidents/losses | No |
| Q27 circumstances giving rise to claim | No |
| Q28 pending/completed regulatory proceedings | No |

## Fields left BLANK for AFFG `[AFFG]`
- Total Employee Count
- Revenue
- Cyber Effective Date
- Estimated number of PII records
- Sign block: Print/Type Applicant's Name, Title, **Signature**, Date Signed

## `[VERIFY]` items AFFG must confirm before signing (REDY)
1. **NAICS 523930** — confirm vs 523120 (Securities Brokerage).
2. **Q3 / Q4 / Q5** wire-transfer & vendor-bank-verification controls (AFFG treasury/AP process).
3. **Q7** encryption at rest + external-email encryption actually enabled.
4. **Q9** the exact MFA scope (only check uses genuinely enforced today).
5. **Q15** EDR truly covers 100% of endpoints (no unmanaged/legacy devices).
6. **Q16** which backup measures are truly in place (Test box intentionally left off).
7. **Q17 / Q21** patch cadence is formal and meets the stated frequency.

---

# FORM 2 — Tokio Marine HCC — NetGuard® Plus Cyber Liability
**File:** `Tokio Marine -HCC - Cyber Liability Application_FILLED.pdf` · 5 pages · 129 fields · 87 set · 42 deliberately blank/Off · 0 failed.

## Fields SET (value shown)
| Field | Value |
|---|---|
| Name of Applicant | American Fundstars Financial Group LLC |
| Street Address | 1 Park Plaza, Ste 210 |
| City / State / Zip | Irvine / CA / 92618 |
| Website | www.americanfundstars.com |
| §2a Form of business | **Other** → Limited Liability Company (LLC) |
| §2c Description of operations | Dually registered investment adviser (RIA) and broker-dealer — securities brokerage and investment advisory services. |
| §4a collect sensitive information | Yes |
| §4b biometric information | No |
| §4c credit-card transactions | No |
| §5a responsible for network security | Outsourced to Technijian, Inc. (managed security provider) |
| §5a Name / Title | Ravi Jain / CEO, Technijian, Inc. (outsourced MSP) |
| §5a Phone / Email | 949-379-8499 / rjain@technijian.com |
| §5a IT Security Designation(s) | Managed IT/Security Provider (MSP/MSSP); SOC 2  **[VERIFY]** |
| §5b network security is | **Outsourced** |
| §5c / §5d IT & security personnel | 0 in-house (outsourced to Technijian MSP) |
| §6a tag external emails | Yes  **[VERIFY]** |
| §6b pre-screen attachments/links | Yes |
| §6b sandbox detonation before delivery | **No**  **[VERIFY — Yes only if Defender for O365 Safe Attachments licensed]** |
| §6c phishing protections | **SPF + DKIM + DMARC** (None-of-the-above left off) |
| §6d email via web/non-corp device | Yes |
| §6d enforce MFA | Yes |
| §6e Office 365 | Yes |
| §6e O365 ATP add-on | **No**  **[VERIFY]** |
| §7a cloud provider used | Yes → Microsoft 365 / Microsoft Azure (primary); AWS |
| §7b MFA on all cloud services (host_applications) | Yes |
| §7 use_MFA | Yes |
| §7c encrypt sensitive data at rest | Yes |
| §7c(2) role-based access assignments | Yes (compensating; §7c(1) segregation left blank since encryption=Yes) |
| §7d remote access allowed | Yes |
| §7d(1) MFA on all remote/RDP | Yes |
| §7d MFA provider | combo **Other** → Microsoft Entra ID / Authenticator |
| §7e NGAV on all endpoints | Yes; provider combo **Other** → CrowdStrike Falcon |
| §7f EDR centralized monitoring/logging | Yes; provider combo **Other** → CrowdStrike Falcon |
| §7g MFA on privileged accounts | Yes |
| §7h PAM software (CyberArk/BeyondTrust) | No |
| §7i monitor admin access for anomalies | Yes → Technijian SOC / Huntress MDR / MyAudit UAM |
| §7j hardened baseline configuration | Yes |
| §7k track software/hardware assets | Yes → Microsoft Intune / ScreenConnect RMM |
| §7l non-IT users have local admin | **No**  **[VERIFY]** |
| §7m critical/high-severity patch frequency | **4-7 days**  **[VERIFY]** |
| §7n end-of-life/end-of-support software | No (§7n segregated left blank, N/A) |
| §7o protective DNS service | Yes → CloudBrink ZTNA |
| §7p endpoint app isolation/containment | **No**  **[VERIFY]** (containment provider combos left blank) |
| §7q Office macros enabled by default | **No**  **[VERIFY]** |
| §7r PowerShell best practices | Yes  **[VERIFY]** |
| §7s SIEM | Yes |
| §7t SOC | Yes |
| §7t monitored 24/7 | Yes |
| §7u vulnerability management tool | Yes → Technijian vulnerability scanning  **[VERIFY]** |
| §8 data backup solution | Yes |
| §8a frequency | **Daily** |
| §8b restore time after ransomware | **0-24 hours**  **[VERIFY]** |
| §8c backup measures | #1 encrypted, #2 offline/air-gapped-or-purpose-cloud, #3 separate creds, #4 MFA on backups, #8 can test integrity before restore (**#5 consumer cloud-sync, #6 cloud-sync MFA, #7 restore-tested-in-6-months left UNCHECKED**)  **[VERIFY #3,#4,#8]** |
| §9a(1) social-eng training (finance staff) | Yes |
| §9a(2) social-eng training (non-finance staff) | Yes |
| §9a phishing simulation included | Yes (PHT) |
| §10a(1) complaints/written demands | No |
| §10a(2) privacy regulatory proceedings | No |
| §10a(3) breach notification | No |
| §10a(4) extortion demand | No |
| §10a(5) network outage | No |
| §10a(6) property damage / business interruption | No |
| §10a(7) wire/telecom/phishing fraud | No |
| §10b knowledge of breach/incident/allegation | No |
| §10c service-provider outage >4 hrs | No |
| §10c interruption to business as result | No |

## Fields left BLANK for AFFG `[AFFG]`
- §1 Phone, Fax
- §2b Date established
- §2d Total number of employees
- §3 Revenues — all three fiscal-year month/year + gross-revenue fields (current, 1-yr-ago, 2-yr-ago)
- §4a Paper records count, Electronic records count
- §4b confirmed-compliance-with-attorney (N/A — biometric=No)
- §4c PCI-DSS Compliant (N/A — credit-card=No)
- §5 IT signer Print/Type Name, **Signature**
- §7c(1) segregation of servers (N/A — encryption=Yes)
- §7h PAM provider name (N/A — PAM=No)
- §7n segregated-network (N/A — EOL software=No)
- §7p containment provider combos + name (N/A — containment=No)
- §7u tool_provider combo (set to empty; provider noted in the name field instead)
- §8c backup boxes #5, #6, #7 (intentionally unchecked)
- **§9b wire-transfer questions** — `send_receive_wire_transfer` and all five sub-protocols (documentation form, written authorization, separation of authority, new-vendor callback, account-change callback) **LEFT BLANK** — these are AFFG's internal treasury/AP controls; **AFFG must answer.**
- Certification block: Print/Type Applicant's Name, Title, **Signature**, Date Signed

## `[VERIFY]` items AFFG must confirm before signing (Tokio)
1. **§5a IT Security Designation(s)** — confirm "SOC 2" claim is accurate for the managed program.
2. **§6a** external-email tagging actually enabled in M365.
3. **§6b sandbox detonation (delivery_to_the_end-user)** — currently **No**; flip to Yes only if Defender for O365 Safe Attachments is licensed/enabled.
4. **§6e O365 ATP add-on** — currently **No**; confirm Defender for O365 licensing.
5. **§7l** non-IT users do **not** have local admin (currently answered No).
6. **§7m** patch frequency truly 4-7 days.
7. **§7p / §7q** endpoint app-isolation = No, macros-by-default = No — confirm.
8. **§7r** PowerShell best practices implemented.
9. **§7u** vulnerability-management tooling/provider name.
10. **§8b** 0-24h restore time is achievable (i.e., validated by a real restore test).
11. **§8c #3, #4, #8** backup controls (separate creds, MFA on backups, integrity testing) are genuinely in place.
12. **§9b** the entire wire-transfer treasury/AP control section (left blank for AFFG).

---

## Method notes (for auditability)
- Filled with **pypdf 6.13.2** (`C:\Python314\python.exe`). Fill script: `C:\tmp\affg_extract\fill_forms.py`; verifier: `C:\tmp\affg_extract\verify_forms.py`.
- Radio/checkbox values set by each widget's **exact AP on-state** (e.g. `Yes_2`, `4-7 days`, `off site storage`, `local/network/tape/other`), making the mapping coordinate-independent and safe across the many duplicate field names (each Yes/No group shares one field name with two distinct on-states).
- Yes/No groups disambiguated against the extracted form-text question order. The REDY detail-file `y` coordinates are top-down while PDF rects are bottom-up — on-state matching avoided any coordinate-flip error.
- `NeedAppearances` set true on both files so all viewers render the values.
- No field could not be set; both files read back **100%** of expected values (REDY 55/55, Tokio 87/87) with all must-blank fields confirmed empty/Off.
