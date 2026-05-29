# CLAUDE.md — tech-compliance-docs

Repo-specific context for Claude Code. Read this first every session.

This repo holds Technijian's compliance documentation (control mappings, WISP/IRP/BCP
policies, evidence collection, attestation + audit-response templates) for clients
**ORX, TSC, affg** plus shared `docs/` and `templates/`.

---

## Vault & key locations (memorize — do not re-derive)

| What | Path | Purpose |
|---|---|---|
| **Key vault** (credentials) | `C:\Users\rjain\OneDrive - Technijian, Inc\Documents\VSCODE\keys\` | ALL API keys, tokens, passwords, certs. One `.md`/`.cer`/`.pfx` per service or client. |
| **Compliance vault** (this repo's Obsidian vault) | `C:\Users\rjain\OneDrive - Technijian, Inc\Documents\obsidian\tech-compliance-docs\tech-compliance-docs\` | Project knowledge / sessions / memory for this repo. Currently bare (only `Welcome.md`) — initialize Dashboard + Sessions + memory on first substantive session. |
| **Cortex vault** (`rjain557-knowledge`) | `C:\Users\rjain\OneDrive - Technijian, Inc\Documents\obsidian\rjain557-knowledge\rjain557-knowledge\` | Cross-repo "brain." Durable knowledge in `claude-memory/topics/*.md`, working notes in `claude-memory/auto-memory/`, index at `claude-memory/index.md`. Shared across all of Ravi's Claude Code repos. |

Notes:
- All three live under **OneDrive**, so they sync across workstations automatically —
  **no separate vault git-commit step is needed** for new content.
- The username segment is `rjain` on this workstation; some cortex notes record it as
  `Administrator` (a different box). Use `rjain` here.
- When in doubt about anything cross-repo (paths, M365, conventions), the Cortex vault's
  `claude-memory/topics/` is the source of truth — see `vault_locations.md`,
  `m365_mail_credentials.md`, `conventions.md`.

---

## Email access via Microsoft Graph (the key vault provides this)

The key vault holds credentials that grant programmatic access to Technijian mailboxes
over Microsoft Graph. **Tenant:** `Technijian365.onmicrosoft.com`
(Tenant ID `cab8077a-3f42-4277-b7bd-5c9023e826d8`). Use the SMTP address as `-UserId`
(not `"me"`).

| App | Vault file | Auth | Mailbox it acts on | Graph perms |
|---|---|---|---|---|
| **HiringPipeline-Automation** | `keys\m365-graph.md` | Client secret (rotated 2026-05-19) | **`RJain@technijian.com`** (Ravi's mailbox) | `Mail.Read`, `Mail.Send`, `Mail.ReadWrite` |
| **Technijian-Agent-Harness** | `keys\m365-agent-harness.md` (+ `Technijian-Agent-Harness.pfx`) | Certificate (valid to 2028-05-04) | `Knowledge@technijian.com` (shared) + tenant-wide | `Mail.ReadWrite`, `Mail.Send`, `MailboxSettings.Read`, `User.Read.All`, `Directory.Read.All`, etc. |

To read **Ravi's own email** (e.g. an inbound message a session needs to review), use
**HiringPipeline-Automation** against `RJain@technijian.com`. Load the client secret /
tenant / client ID from `keys\m365-graph.md` at runtime — never paste them inline.
`Connect-MgGraph -TenantId <…> -ClientSecretCredential $cred -NoWelcome`, then
`Get-MgUserMessage -UserId 'RJain@technijian.com'`.

---

## Secrets policy (NON-NEGOTIABLE)

Per the user's standing rule (stated explicitly, twice):

- **API keys, tokens, passwords, and certificates live ONLY in the key vault above.**
  The repo holds **none** — not in code, configs, docs, commits, or even a gitignored
  `.env`. The vault is the single source of truth so a key is rotated in exactly one place.
- This CLAUDE.md records credential **locations and identifiers** (app names, mailbox
  addresses, tenant ID) — those are pointers, not secrets. **Never** copy a client secret,
  PFX password, or token value into this repo.
- Load secrets at runtime from the vault file. Never echo a full secret to the terminal
  or into a committed file.
- **Paste-safe commands:** the user copy-pastes commands verbatim. Never hand over a
  command containing a `<placeholder>` on an executable line — bake real (non-secret)
  values in, or read the secret at runtime from the vault.
