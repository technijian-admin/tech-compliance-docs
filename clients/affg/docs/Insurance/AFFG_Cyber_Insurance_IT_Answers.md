# AFFG Cyber Liability Insurance — IT/Security Answer Workbook (DRAFT FOR REVIEW)

**Applicant:** American Fundstars Financial Group LLC ("AFFG") — dually registered RIA / broker-dealer, Irvine, CA
**Prepared by:** Technijian (managed IT / security provider)
**Date:** 2026-06-15
**Covers:** (1) Tokio Marine HCC — NetGuard® Plus Cyber Liability; (2) REDY Cyber (CRC Insurance)

---

## ⚠️ READ FIRST — answer on CURRENT controls, not the target stack

Both forms are **sworn applications**. Tokio Marine prints: *"ANY PERSON WHO KNOWINGLY AND WITH INTENT TO DEFRAUD ANY INSURANCE COMPANY … FILES AN APPLICATION … CONTAINING ANY FALSE INFORMATION … COMMITS A FRAUDULENT INSURANCE ACT, WHICH IS A CRIME,"* and *"this application shall be the basis of the contract."* If a control is answered **Yes** but isn't actually in place at bind, the carrier can **rescind coverage at claim time** — exactly when AFFG needs it.

Per the AFFG IT Compliance Strategy (REF AFFG-CS-2026-04, April 2026), AFFG's **documented current state** is ~15% compliant: personal/unmanaged laptops, no DLP, partial MFA (not enforced), inconsistent endpoint protection, no WORM archive, minimal logging, **no tested incident response plan**. The Technijian remediation (VDI, enforced MFA, CrowdStrike EDR, DLP, My Archive, V365 Backup, My Audit, Huntress SAT) is **in progress** — the very work these compliance tickets cover.

**Answers below default to the honest current state.** Each control that flips to "Yes" only once remediation is live is tagged **⚠️ CONFIRM**. Ravi: change to "Yes (provider)" ONLY where the control is genuinely deployed for AFFG today.

> **Strong recommendation:** Many cyber carriers now make MFA, EDR, tested backups, a written IR plan, and security-awareness training *conditions of coverage*. AFFG is short on several today. The cleanest path is to **complete Phase 1–2 remediation first, then bind** — at which point most answers become a truthful "Yes" and the premium/terms improve. If AFFG must bind now, submit the honest current-state answers and add the remediation timeline in the comments (carriers view active remediation favorably).

---

## Inputs only AFFG can provide (fill before submission)

| # | Field | Needed for |
|---|---|---|
| 1 | Exact legal name + principal **street address** (Irvine) | Both — General Info |
| 2 | **Gross revenue** — current + prior 2 fiscal years; fiscal year-end | Both — Revenues |
| 3 | **Total employee count** | Both |
| 4 | **# of PII records** held (electronic + paper) | Both — Records |
| 5 | NAICS code (likely **523930** Investment Advice or **523120** Securities Brokerage — confirm) | REDY |
| 6 | Desired **cyber policy effective date** | REDY |
| 7 | Form of business (LLC) + **date established** + any subsidiaries/affiliates | Tokio Marine §2 |
| 8 | Named **person responsible for network security** (title, phone, email, certs) — Technijian contact or AFFG officer | Tokio Marine §5a |
| 9 | **# IT staff / # dedicated security staff** (count Technijian's managed team or "0 in-house, outsourced to Technijian") | Tokio Marine §5c/d |
| 10 | **Loss history** — any claims, breaches, regulator actions, extortion, wire fraud, outages (last 3–5 yrs)? | Both §10/§22-28 |
| 11 | **PCI** — does AFFG ever handle credit-card payments? (assumed No) | Both |
| 12 | Current deployment status of each remediation control (see ⚠️ CONFIRM tags) | Both — security sections |

---

## APPLICATION 1 — Tokio Marine HCC, NetGuard® Plus

### §1 General Information
- Name / Street / City,State,Zip / Phone / Website / Fax → **[AFFG to provide]**

### §2 Form of Business
- a. **Corporation/LLC** → confirm (registered as **LLC**)
- b. Date established → **[AFFG]**
- c. Description of operations → **"Dually registered investment adviser (RIA) and broker-dealer providing securities brokerage and investment advisory services to retail and institutional clients."**
- d. Total employees → **[AFFG]**
- e. Subsidiaries/affiliates list → **[AFFG]**

### §3 Revenues — 3 fiscal years → **[AFFG]**

### §4 Records
- a. Collect/store private or sensitive info? **Yes** — paper count **[AFFG]**, electronic count **[AFFG]** (client NPI: SSNs, account numbers, financial data)
- b. Biometric info? **No** → second part N/A
- c. Credit-card transactions? **No (assumed — confirm)** → PCI-DSS question N/A

### §5 IT Department
- a. Responsible for network security → **Outsourced to Technijian Corporation** (named contact, title, phone, email, certs) — **[confirm named individual]**
- b. Network security is: **Outsourced** ☑
- c. # IT personnel → **[Technijian managed team count / "0 in-house"]**
- d. # dedicated security personnel → **[count]**

### §6 Email Security Controls
| Q | Honest answer | Note |
|---|---|---|
| a. Tag external emails | **⚠️ CONFIRM** (target: Yes via M365) | "No" today unless external tagging is enabled in M365 now |
| b. Pre-screen attachments/links | **⚠️ CONFIRM** — Yes if Defender for O365 active; sandbox detonation = Safe Attachments | only "Yes" if licensed/enabled |
| c. SPF / DKIM / DMARC | **⚠️ CONFIRM each** — check the M365 tenant; commonly SPF yes, DKIM/DMARC partial | list only those actually published |
| d. Email via web/non-corp device + MFA | Web access **Yes**; MFA **⚠️ partial today** | target: enforced via Conditional Access |
| e. Office 365? **Yes**. ATP add-on? | **⚠️ CONFIRM** (Defender for O365 = the ATP successor) | |

> Comment to add: "AFFG is mid-deployment of Microsoft 365 Defender, Conditional Access (VDI-only sign-in), and enforced MFA under a documented remediation plan; target completion [date]."

### §7 Internal Security Controls
| Q | Honest answer (current) | Target / note |
|---|---|---|
| a. Cloud provider to store data/host apps | **Yes** — Microsoft 365 / OneDrive (largest sensitive store); AWS | name M365 as largest |
| b. MFA on all cloud services | **⚠️ partial today** | target: Yes (Entra Conditional Access) |
| c. Encrypt sensitive data at rest | **⚠️ CONFIRM** — M365 server-side yes; **personal laptops not encrypted today** | compensating: role-based access yes; segregation ⚠️ |
| d. Remote access allowed? **Yes**; MFA on all remote/RDP? | **⚠️ partial today** | target: VDI + MFA (no direct RDP) |
| e. NGAV on all endpoints? | **⚠️ No (current: inconsistent across personal devices)** | target: CrowdStrike Falcon |
| f. EDR with centralized monitoring/logging? | **⚠️ No today (not 100%)** | target: **CrowdStrike Falcon Insight** |
| g. MFA on privileged accounts | **⚠️ CONFIRM** | target: Yes |
| h. PAM software (CyberArk/BeyondTrust)? | **No** | not currently |
| i. Monitor admin access for anomalies | **⚠️ CONFIRM** (Technijian SOC/SIEM if AFFG onboarded) | target: My Audit + SIEM |
| j. Hardened baseline across devices | **No today (personal laptops)** | target: Yes (VDI golden image) |
| k. Asset inventory tool | **⚠️ CONFIRM** (Technijian RMM if AFFG onboarded) | |
| l. Non-IT users have local admin? | **⚠️ likely Yes today (personal laptops)** — answer truthfully | target: No (VDI) |
| m. Critical patch frequency | **⚠️ CONFIRM** — likely **8-30 days / informal** today | target: 1-7 days |
| n. End-of-life software? + segregated | **⚠️ CONFIRM** | |
| o. Protective DNS (Zscaler/Quad9/OpenDNS)? | **⚠️ CONFIRM** (Cisco Umbrella if deployed) | |
| p. Endpoint app isolation/containment | **No** | |
| q. Office macros enabled by default? | **⚠️ CONFIRM** (answer truthfully; target: blocked) | |
| r. PowerShell best practices | **⚠️ CONFIRM** | |
| s. SIEM? | **⚠️ CONFIRM** (Technijian SIEM if AFFG onboarded; current state = "minimal/no unified log") | |
| t. SOC, 24/7? | **⚠️ CONFIRM** (Technijian 24/7 SOC if AFFG subscribed) | |
| u. Vulnerability management tool? | **⚠️ CONFIRM** | |

### §8 Backup & Recovery
- Data backup solution? **Yes** — Synology NAS + cloud (per BCP). Frequency → **⚠️ CONFIRM (likely Daily)**.
- Restore time after ransomware → **⚠️ CONFIRM** (current backups not validated; honest pick likely **1-3 days** — do not claim 0-24h unless tested).
- Measures — check only what's true today: encrypted ⚠️ · offline/air-gapped ⚠️ · separate creds ⚠️ · MFA on backups ⚠️ · cloud-sync ☐ · **tested restoration in last 6 months ⚠️ (AFFG-005/-024 establishes this — likely NOT yet, leave unchecked if so)** · integrity test ⚠️.

> This section maps directly to ticket **AFFG-005** (backup specs) and Sai's **AFFG-024** (restore test). Until those run, several boxes here are honestly unchecked.

### §9 Phishing Controls
- a. Social-engineering training (finance / non-finance staff)? **⚠️ No today** (Huntress SAT is in the target stack) → "willing to implement" comment. Phishing simulation? **No today**.
- b. Send/receive wire transfers? **⚠️ CONFIRM**. If yes, wire authorization protocol — (1) request form (2) written auth (3) separation of authority (4) **callback to new vendor on number they provided** (5) **callback on account-change requests** → **[AFFG to confirm each — these are core financial-firm controls and likely Yes; answer truthfully]**.

### §10 Loss History → **[AFFG to confirm — assumed all No]** (a.1–7, b, c). Any "Yes" requires a Claim Supplemental Form.

---

## APPLICATION 2 — REDY Cyber (CRC Insurance)

### General Information → **[AFFG to provide]**: full name, mailing + physical address, industry ("Investment adviser / broker-dealer"), NAICS (523930/523120), employee count, website, cyber effective date, revenue.

| Q | Honest answer | Note |
|---|---|---|
| 1. Adult / cannabis / crypto activities | **None of the above** | |
| 2a. Data stored: PII / healthcare / PCI / MSP / payment-processing | **Personal Information** only | broker-dealer NPI |
| 2 (#PII records) | **[AFFG]**; healthcare **0**; payment-card txns **0** | |
| 3. Prevent unauthorized employees initiating wires | **⚠️ CONFIRM (likely Yes)** | |
| 4. Secondary validation for funds-transfer requests | **For ALL Requests** (recommended/confirm) | |
| 5. Verify vendor bank accounts before AP | **⚠️ CONFIRM (Yes recommended)** | |
| 6. Maintain secured backups | **Yes** (Synology + cloud) | quality flagged in §8 above |
| 7. Protect sensitive data: de-identify / encrypt at rest / encrypt external email | check only what's true; **⚠️ encryption partial today** | |
| 8. Sensitive info on cloud | **Yes** (M365/OneDrive); 8a frequency **⚠️**; 8b offline-or-cloud **Yes (cloud)** | |
| 9. MFA enforced for: Email / Remote / VPN / Mission-critical / Admin | **⚠️ partial today** — check only enforced ones | target: all |
| 10. Mandatory infosec training annually | **⚠️ No today** → "willing to implement during policy period: **Yes**" | |
| 11. Content-removal review procedures | **No / N/A** — AFFG is not a publisher | explain in comments |
| 12. Website-content complaints (3 yrs) | **No** | |
| 13. Legal counsel for IP review | **No / N/A** | not a content creator |
| 14. Biometric records annually | **0** | |
| 15. EDR covering 100% of environment | **⚠️ No today** | target: CrowdStrike Falcon |
| 16. Backup measures (MFA/segmentation/AV scan/immutable/test/encryption/online-cloud) | check only what's true today | several **⚠️** pending AFFG-005 |
| 17. Formal 30-day patch cadence; critical/zero-day ≤7 days | **⚠️ No today (informal)** | target: Yes |
| 18. Create content for others | **No** | |
| 19. Cyber extortion experienced | **No** *(confirm)* | |
| 20. Revenue outside domiciled country | **No** *(confirm)* | |
| 21. Update frequency for critical systems/apps | **⚠️ CONFIRM** (honest: Monthly/informal today) | |
| 22. Breach requiring notification (last 5 yrs) | **No** *(confirm)* | |
| 23. **IR plan — tested and in effect** | **⚠️ No today — in development (ticket AFFG-001)** | becomes Yes once IRP is written + tabletop-tested |
| 24. Device protection: AV / anti-malware / endpoint / firewall (+ EDR product) | check what's true; EDR = **CrowdStrike Falcon Insight** ⚠️ once live | |
| 25. Email precautions: screen attachments / screen links / tag external | **⚠️ CONFIRM each** | |
| 26/27/28. Prior incidents / circumstances / regulatory proceedings | **No** *(confirm)* | |

---

## Bottom line for Ravi
1. **Fill the AFFG-input table** (revenue, employees, record counts, named security contact, loss history).
2. **Walk the ⚠️ CONFIRM rows** and flip to "Yes (provider)" only where the control is genuinely live for AFFG **today**. Be conservative — a wrong "Yes" voids the policy at claim time.
3. The honest answer to several controls (EDR 100%, enforced MFA, tested backups, written/tested IRP, security-awareness training) is currently **No / in progress**. That's the case *for* finishing Phase 1–2 remediation before binding — then re-answer truthfully as "Yes" for better terms and valid coverage.
