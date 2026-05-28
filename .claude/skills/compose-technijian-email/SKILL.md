---
name: compose-technijian-email
description: Use when composing, drafting, or sending an email as Ravi Jain / Technijian — replies to prospects, clients, vendors, or SDR-relayed inquiries. Captures the house voice, the exact email signature, and the Microsoft Graph send procedure for RJain@technijian.com. Trigger on "compose an email", "draft a reply", "respond to <person>", "send this from my mailbox".
---

# Compose a Technijian email (as Ravi Jain)

Produce send-ready email in Ravi Jain's house style, with his exact signature, and
(optionally) send it from `RJain@technijian.com` via Microsoft Graph.

## Voice & format (derived from his Sent folder)

- **Greeting:** first name + comma on its own line — `Lewis,` (never "Dear", never "Hi all").
- **Open with continuity/context**, not a pitch: "Still thinking about…", "I've been thinking about the … you're building for…", or a one-line reason for writing.
- **Short, conversational paragraphs** (2–4 sentences). Plain language. Name *one specific* risk or gap relevant to the reader — concrete, not generic "cybersecurity is important" filler.
- **One soft CTA near the end**, usually a question: "Is that still an open question, or has the direction been settled?" / "What does your calendar look like in the next week or two?" Avoid hard-sell.
- **Honesty is non-negotiable** on compliance claims. Never state Technijian is "CMMC certified" / "CMMC Level 2 compliant" — it is not C3PAO-assessed. Misrepresentation on DoD-adjacent work = False Claims Act exposure. State status plainly, then pivot to what *is* true and to a call.
- **Light structure is OK** when answering explicit numbered questions (e.g., an SDR relaying a prospect's Q&A) — answer each clearly, then add scoping questions. Default to prose otherwise; these emails rarely use bullet lists.
- **Close:** `Thank you,` then a blank line, then the signature.
- Tone: calm, senior, specific. He is the CEO writing personally.

## The signature

Two ways to apply it:

1. **Sending via Graph (HTML):** inject `assets/signature.html` verbatim after the body.
   It is the real signature lifted from his Sent folder — orange top-border, headshot,
   contact block, Book-a-Meeting + Book-time-with-Support links, social links, and the
   confidentiality disclaimer. Do not retype it; use the file.
2. **Plain-text / when he pastes into Outlook himself:** Outlook auto-appends the HTML
   signature, so hand over **body only** and tell him the signature will attach. If a
   plain-text rendering is needed, use this:

```
Thank you,

Ravi Jain
CEO
Technijian
T: 949.379.8499 x201
C: 714.402.3164
S: 949.379.8501 (support)
E: rjain@technijian.com
W: technijian.com
Book a Meeting | Book time with Support
USA: 18 Technology Dr., Ste 141, Irvine, CA 92618
India: Plot No. 07, 1st Floor, Panchkula IT Park, Panchkula, Haryana 134109
LinkedIn | Facebook | YouTube | Instagram | X | TikTok | Pinterest
```

Signature links (for reference):
- Book a Meeting → `https://outlook.office.com/bookwithme/user/ceb349088c264d73b4854612958471e9@technijian.com/...`
- Book time with Support → `https://outlook.office365.com/owa/calendar/Meetingwithsupport@Technijian365.onmicrosoft.com/bookings/`
- LinkedIn `linkedin.com/company/technijian` · Facebook `facebook.com/Technijian01` · YouTube `@TechnijianIT` · Instagram `technijianinc` · X `technijian_` · TikTok `@technijian` · Pinterest `technijian01`
- Headshot `https://technijian.com/wp-content/uploads/2026/03/ravi-jain.jpg` · Logo `https://technijian.com/wp-content/uploads/2026/03/technijian-logo-full-color-600...`

## Sending via Microsoft Graph

Credentials live ONLY in the key vault — never hardcode them. App **HiringPipeline-Automation**
(`Mail.Send` on `RJain@technijian.com`), tenant `Technijian365.onmicrosoft.com`. See repo
`CLAUDE.md` and `keys\m365-graph.md`. Always confirm with the user before sending.

Paste-safe pattern (reads the secret at runtime; no placeholders, no secrets on screen):

```powershell
$vault = "C:\Users\rjain\OneDrive - Technijian, Inc\Documents\VSCODE\keys\m365-graph.md"
$t = Get-Content -Raw $vault
$tenant = [regex]::Match($t,'Tenant ID:\*\*\s*([0-9a-fA-F-]{36})').Groups[1].Value
$client = [regex]::Match($t,'App Client ID:\*\*\s*([0-9a-fA-F-]{36})').Groups[1].Value
$secret = [regex]::Match($t,'Client Secret:\*\*\s*(\S+)').Groups[1].Value
$tok = (Invoke-RestMethod -Method POST -Uri "https://login.microsoftonline.com/$tenant/oauth2/v2.0/token" `
  -Body @{client_id=$client;scope='https://graph.microsoft.com/.default';client_secret=$secret;grant_type='client_credentials'}).access_token
$h = @{ Authorization = "Bearer $tok"; 'Content-Type'='application/json' }

# Body = your composed HTML + the signature asset
$bodyHtml = (Get-Content -Raw '<path-to-body.html>') + (Get-Content -Raw `
  "C:\VSCode\tech-compliance-docs\tech-compliance-docs\.claude\skills\compose-technijian-email\assets\signature.html")

# To REPLY on an existing thread, first find the message id, then use /reply (keeps threading):
#   POST /users/RJain@technijian.com/messages/{id}/reply  { "message": { "body": {...} }, "comment": "" }
# To send NEW:
$msg = @{ message = @{
    subject = '<subject>'
    body = @{ contentType='HTML'; content=$bodyHtml }
    toRecipients = @(@{ emailAddress=@{ address='<recipient>' } })
  }; saveToSentItems = $true } | ConvertTo-Json -Depth 8
Invoke-RestMethod -Method POST -Headers $h -Uri "https://graph.microsoft.com/v1.0/users/RJain@technijian.com/sendMail" -Body $msg
```

Prefer the `/messages/{id}/reply` endpoint for replies so the thread stays intact and the
original is quoted automatically — set the reply `body` to your HTML + signature.

## Workflow

1. Read 3–6 recent items from `mailFolders/SentItems/messages` if unsure of current voice.
2. Draft **body only** in the voice above. Show it to the user.
3. On approval, send via Graph (reply endpoint for replies) with `signature.html` appended.
4. Never send without explicit go-ahead.
