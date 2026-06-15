# AFFG Customer Breach Notification Procedures
**Document ID:** AFFG-002  
**Version:** 1.0  
**Date:** June 5, 2026  
**Prepared by:** Ravi Jain, CEO — Technijian  
**Status:** DRAFT — Pending Registered Principal Approval (see AFFG-016)  
**Portal Ticket:** #1459346  
**Regulatory Basis:** SEC Regulation S-P (2024 amendments), 17 CFR §248.30(a)(2)  

---

## 1. Purpose

This document establishes AFFG's written procedures for notifying customers whose sensitive information was, or is reasonably likely to have been, accessed without authorization. These procedures satisfy the requirement under SEC Regulation S-P (2024 amendments) that covered institutions must notify affected individuals no later than **30 days** after determining a notification event has occurred.

---

## 2. Notification Trigger Criteria

A notification obligation arises when the Incident Response Lead (Ravi Jain) makes a **Notification Determination**: a documented finding that sensitive customer information **was, or is reasonably likely to have been, accessed without authorization**.

### 2.1 What Constitutes Sensitive Customer Information

Notification is required when any of the following customer data elements were involved in an unauthorized access event, in combination with the customer's name:

| Data Element | Examples |
|---|---|
| Social Security Number (SSN) | Full or partial SSN |
| Government-issued ID number | Driver's license, passport, state ID |
| Financial account number | Brokerage account, bank account number |
| Credit or debit card number | With or without expiration/CVV |
| Security codes / passwords | Account passwords, security questions, PINs |
| Access credentials | Username + password combinations |

*Note: Name alone, or name + publicly available information, does not trigger notification.*

### 2.2 "Reasonably Likely" Standard

Notification is required even where unauthorized access is **not confirmed** but is **reasonably likely** — meaning a reasonable person would conclude there is a material probability that data was accessed without authorization. Indicators include:

- Evidence of unauthorized access to systems containing customer data (even if exfiltration is not confirmed)
- Receipt of a service provider notification that customer data in their custody was accessed
- Discovery of customer data in an unexpected location (dark web, public repository)
- Malware or ransomware on systems that store customer data
- Theft of a device containing unencrypted customer data

**When in doubt, notify.** The cost of unnecessary notification is far lower than the regulatory risk of failing to notify when required.

---

## 3. Determination Process

### Step 1 — Incident Assessment (Day 0 to Day 5)

The Incident Response Team (IRT) conducts a forensic investigation per AFFG-001 to determine:
1. What systems were accessed?
2. Do those systems contain sensitive customer information?
3. Is there evidence the attacker accessed, read, copied, or exfiltrated customer data?
4. Even without confirmed exfiltration, is unauthorized access reasonably likely given the attack vector and attacker capability?

### Step 2 — Formal Notification Determination (must occur by Day 5)

Ravi Jain (Incident Response Lead) makes a formal written determination:
- **Notification required:** Sensitive customer information was or is reasonably likely to have been accessed without authorization. **30-day clock starts today.**
- **Notification not required:** No sensitive customer information was involved or access was not unauthorized. Document the basis for this determination.

The determination is documented in the incident record with:
- Date of determination
- Basis for the determination
- Name of person making the determination (Ravi Jain)
- Iris Liu's confirmation/acknowledgment

### Step 3 — Scope Determination (Day 5 to Day 15)

Identify the specific customers who must be notified:
1. Pull the list of all customers whose data was stored on or accessible through the affected systems
2. Cross-reference with evidence of access to narrow the list where possible
3. When scope cannot be precisely determined, apply the reasonably-likely standard — include all customers whose data *could* have been accessed
4. Document the scoping methodology and the final customer list

---

## 4. The 30-Day Notification Timeline

| Milestone | Target Day | Owner |
|---|---|---|
| Notification Determination made and documented | Day 0 | Ravi Jain |
| Iris Liu notified and acknowledges determination | Day 0 | Ravi Jain → Iris Liu |
| Scoping complete (affected customer list finalized) | Day 10 | Ravi Jain / Sai Revanth |
| Draft notification letter prepared | Day 12 | Ravi Jain |
| Legal counsel review of notification letter | Day 15 | AFFG legal counsel |
| AFFG registered principal approves final letter | Day 18 | AFFG principal |
| Notification letters sent to all affected customers | **Day 25** | Iris Liu / Ravi Jain |
| Copies of all notifications filed in Reg S-P records | Day 25 | Ravi Jain |
| **Regulatory deadline** | **Day 30** | — |

*Day 25 target provides a 5-day buffer against the Day 30 regulatory deadline.*

---

## 5. Notification Letter Content Requirements

All customer notification letters must include the following elements per Reg S-P:

1. **Description of the incident** — What happened, when it was discovered, and what the nature of the unauthorized access was (at a level of detail appropriate without compromising the investigation)

2. **Data elements involved** — The specific types of sensitive information that were or may have been accessed (SSN, account numbers, etc.)

3. **Date range** — The approximate timeframe during which the unauthorized access occurred

4. **Steps AFFG has taken** — What AFFG has done in response (system remediation, enhanced security measures, investigation)

5. **Protective steps for the customer** — Specific actions customers should take:
   - Monitor financial accounts and statements for unauthorized activity
   - Place a fraud alert or credit freeze with credit bureaus
   - Report suspicious activity to AFFG immediately
   - Contact information for the FTC identity theft hotline (1-877-438-4338)

6. **AFFG contact information** — How affected customers can reach AFFG for questions about the incident

7. **Credit monitoring offer** — AFFG should consider offering 12 months of free credit monitoring for affected customers (strongly recommended by regulators even if not explicitly required in all cases)

---

## 6. Approved Notification Letter Templates

### Template A — Confirmed Unauthorized Access

---

[AFFG Letterhead]

[Date]

[Customer Name]  
[Customer Address]

**IMPORTANT NOTICE REGARDING YOUR ACCOUNT SECURITY**

Dear [Customer Name],

We are writing to inform you of a security incident that may have affected your account information with American Fundstars Financial Group LLC (AFFG).

**What Happened**

On or about [DATE], we discovered that [DESCRIBE INCIDENT — e.g., "an unauthorized party gained access to our systems"]. Upon investigation, we determined on [DETERMINATION DATE] that your account information may have been accessed without authorization.

**Information Involved**

The information that may have been accessed includes: [LIST SPECIFIC DATA ELEMENTS — e.g., your name, Social Security number, and account number].

**What We Are Doing**

Upon discovering this incident, we immediately [DESCRIBE STEPS TAKEN — e.g., "secured our systems, engaged cybersecurity experts, and launched a full investigation"]. We have also [DESCRIBE ADDITIONAL MEASURES — e.g., "implemented additional security controls and are working with law enforcement"].

**What You Should Do**

We recommend you take the following steps to protect yourself:

1. **Monitor your accounts.** Review your brokerage account and other financial account statements carefully for any unauthorized activity. Contact us immediately if you notice anything suspicious.

2. **Place a fraud alert.** Contact one of the three major credit bureaus to place a free fraud alert on your credit file:
   - Equifax: 1-800-525-4595 / equifax.com
   - Experian: 1-888-397-3742 / experian.com
   - TransUnion: 1-800-680-7289 / transunion.com

3. **Consider a credit freeze.** A credit freeze prevents new credit from being opened in your name. Contact each credit bureau listed above.

4. **Report identity theft.** If you believe you are a victim of identity theft, contact the FTC at 1-877-438-4338 or IdentityTheft.gov.

**Complimentary Credit Monitoring**

We are offering you 12 months of complimentary credit monitoring services. To enroll, please [ENROLLMENT INSTRUCTIONS]. The enrollment code is: [CODE]. The offer expires [DATE].

**For More Information**

If you have questions about this notice, please contact us at:
- **Phone:** [AFFG PHONE NUMBER]
- **Email:** [AFFG CONTACT EMAIL]
- **Hours:** [BUSINESS HOURS]

We sincerely apologize for this incident and any concern it may cause you. Protecting your information is our highest priority.

Sincerely,

[AFFG Registered Principal Name]  
[Title]  
American Fundstars Financial Group LLC

---

### Template B — Reasonably Likely Access (Precautionary Notice)

*Use when the determination is "reasonably likely" rather than confirmed.*

Same structure as Template A, with the following modification to the "What Happened" section:

> *"While we have no definitive evidence that your information was accessed, our investigation determined that unauthorized access to systems containing your account information was reasonably likely. Out of an abundance of caution and in compliance with our regulatory obligations, we are notifying all customers whose information may have been at risk."*

---

## 7. Delivery Methods

Notification letters must be sent by one or more of the following methods, chosen to maximize the likelihood of receipt:

1. **First-class mail** to the customer's address of record — required in all cases
2. **Email** to the customer's email address of record — in addition to mail, not instead of
3. For high-risk accounts (large balances, prior concerns): **Certified mail** with return receipt

*Electronic-only notification is not sufficient to satisfy the 30-day requirement.*

---

## 8. Recordkeeping

All of the following must be filed in the Reg S-P compliance records repository within 5 business days of sending notifications, and retained for **5 years**:

- The notification determination document (date, basis, decision-maker)
- The final affected customer list
- Copies of all notification letters sent
- Proof of delivery (mailing confirmation, email delivery records)
- Any communications with legal counsel regarding the notification
- Documentation of why any customer on the exposure list was excluded from notification

---

## 9. Service Provider Notification Events

When AFFG receives a breach notification from a service provider (AT&T, RingCentral, AWS, Microsoft, Synology, or any other vendor), the following steps apply:

1. Ravi Jain reviews the service provider notification within **24 hours** of receipt
2. Makes a Notification Determination: did the vendor breach involve sensitive AFFG customer information?
3. If yes (or reasonably likely): 30-day clock starts from the date AFFG determines notification is required (not necessarily the date the vendor notified AFFG)
4. Requests from the vendor: full details of what data was accessed, the timeframe, and the affected records

---

## 10. Approval and Version History

| Role | Name | Signature | Date |
|---|---|---|---|
| IT Provider / Incident Response Lead | Ravi Jain, CEO — Technijian | _________________ | __________ |
| AFFG Primary Contact | Iris Liu | _________________ | __________ |
| AFFG Registered Principal | _________________ | _________________ | __________ |

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-05 | Ravi Jain / Technijian | Initial document |

---

*Note: Customer data inventory (specific categories of data AFFG holds) should be confirmed with Iris Liu and documented as an addendum to this plan. Standard RIA/BD data categories are assumed above.*
