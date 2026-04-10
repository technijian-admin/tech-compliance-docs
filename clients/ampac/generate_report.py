"""
AMPAC Business Capital — Compliance Framework & IT Controls Report
Technijian Branded | Institutional Cartography Design Philosophy
"""

import os, math, urllib.request, io
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from PIL import Image

# ─── PATHS ────────────────────────────────────────────────────
BASE = r"c:\vscode\tech-compliance-docs\tech-compliance-docs\clients\ampac"
FONT_DIR = os.path.join(BASE, "fonts")
OUT_PDF = os.path.join(BASE, "AMPAC_Compliance_Framework_Report.pdf")

# ─── BRAND TOKENS ─────────────────────────────────────────────
BLUE       = HexColor("#006DB6")
ORANGE     = HexColor("#F67D4B")
TEAL       = HexColor("#1EAAC8")
DARK       = HexColor("#1A1A2E")
GREY       = HexColor("#59595B")
LIGHT_GREY = HexColor("#E9ECEF")
OFF_WHITE  = HexColor("#F8F9FA")
CHART_GREEN = HexColor("#CBDB2D")

W, H = letter  # 612 x 792

# ─── REGISTER FONTS ───────────────────────────────────────────
pdfmetrics.registerFont(TTFont("OpenSans-Light",     os.path.join(FONT_DIR, "OpenSans-Light.ttf")))
pdfmetrics.registerFont(TTFont("OpenSans",           os.path.join(FONT_DIR, "OpenSans-Regular.ttf")))
pdfmetrics.registerFont(TTFont("OpenSans-SemiBold",  os.path.join(FONT_DIR, "OpenSans-SemiBold.ttf")))
pdfmetrics.registerFont(TTFont("OpenSans-Bold",      os.path.join(FONT_DIR, "OpenSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("OpenSans-ExtraBold", os.path.join(FONT_DIR, "OpenSans-ExtraBold.ttf")))

# ─── LOGOS ─────────────────────────────────────────────────────
LOGO_WHITE = r"c:\vscode\tech-branding\tech-branding\assets\Technijian Logo - white text.png"
LOGO_COLOR = r"c:\vscode\tech-branding\tech-branding\assets\logos\png\technijian-logo-full-color-1200x251.png"

# ─── HELPERS ──────────────────────────────────────────────────

def draw_logo(c, x, y, h=28, dark_bg=False):
    """Draw logo at position, scaled to height h. Use white version on dark backgrounds."""
    logo_path = LOGO_WHITE if dark_bg else LOGO_COLOR
    try:
        img = Image.open(logo_path)
        aspect = img.width / img.height
        w = h * aspect
        c.drawImage(logo_path, x, y, width=w, height=h, preserveAspectRatio=True, mask='auto')
        return w
    except:
        return 0

def draw_dot_grid(c, x0, y0, w, h, spacing=12, radius=0.6, color=None):
    """Subtle dot grid pattern — cartographic reference marks."""
    if color is None:
        color = Color(0.85, 0.87, 0.90, 0.4)
    c.setFillColor(color)
    cols = int(w / spacing)
    rows = int(h / spacing)
    for row in range(rows):
        for col in range(cols):
            cx = x0 + col * spacing + spacing / 2
            cy = y0 + row * spacing + spacing / 2
            c.circle(cx, cy, radius, fill=1, stroke=0)

def draw_ruled_line(c, x0, x1, y, color=LIGHT_GREY, width=0.5):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(x0, y, x1, y)

def draw_vertical_rule(c, x, y0, y1, color=LIGHT_GREY, width=0.5):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(x, y0, x, y1)

def draw_accent_bar(c, x, y, w, h, color=BLUE):
    c.setFillColor(color)
    c.rect(x, y, w, h, fill=1, stroke=0)

def text_block(c, text, x, y, font="OpenSans", size=9, color=GREY, max_w=None, leading=None):
    """Draw text, returns y position after text."""
    c.setFont(font, size)
    c.setFillColor(color)
    if leading is None:
        leading = size * 1.45
    if max_w is None:
        c.drawString(x, y, text)
        return y - leading
    # Word wrap
    words = text.split()
    lines = []
    current = ""
    for w in words:
        test = current + (" " if current else "") + w
        if pdfmetrics.stringWidth(test, font, size) <= max_w:
            current = test
        else:
            if current:
                lines.append(current)
            current = w
    if current:
        lines.append(current)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


# ═══════════════════════════════════════════════════════════════
#  PAGE 1 — COVER
# ═══════════════════════════════════════════════════════════════

def page_cover(c):
    """Full dark cover with cartographic grid overlay — refined second pass."""
    # Deep gradient-emulating background (layered rects)
    c.setFillColor(DARK)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    # Slightly lighter zone top-right for depth
    c.setFillColor(Color(0.05, 0.10, 0.18, 0.4))
    c.rect(W * 0.55, H * 0.4, W * 0.45, H * 0.6, fill=1, stroke=0)

    # Cartographic dot grid — precise, quiet reference marks
    draw_dot_grid(c, 0, 90, W, H - 90, spacing=20, radius=0.45,
                  color=Color(1, 1, 1, 0.03))

    # Top registration marks — surveyor's precision
    c.setStrokeColor(Color(1, 1, 1, 0.08))
    c.setLineWidth(0.25)
    # Cross-hair marks in corners
    for cx, cy in [(36, H - 24), (W - 36, H - 24)]:
        c.line(cx - 6, cy, cx + 6, cy)
        c.line(cx, cy - 6, cx, cy + 6)

    c.setFont("OpenSans-Light", 6.5)
    c.setFillColor(Color(1, 1, 1, 0.18))
    c.drawString(48, H - 27, "REF: AMPAC-CFR-2026-001")
    c.drawRightString(W - 48, H - 27, "CLASSIFICATION: CLIENT CONFIDENTIAL")

    # Horizontal ruling lines — topographic section marker
    for i in range(7):
        y = H - 75 - i * 2.5
        c.setStrokeColor(Color(1, 1, 1, 0.05))
        c.setLineWidth(0.25)
        c.line(36, y, W - 36, y)

    # Logo — white text version on dark background, positioned with authority
    draw_logo(c, 36, H - 135, h=36, dark_bg=True)

    # Orange accent bar — warm signal, deliberate length
    c.setFillColor(ORANGE)
    c.rect(36, H - 172, 72, 2.5, fill=1, stroke=0)

    # Title block — monumental typography with refined spacing
    c.setFont("OpenSans-ExtraBold", 44)
    c.setFillColor(white)
    c.drawString(36, H - 240, "Compliance")
    c.drawString(36, H - 292, "Framework")
    c.setFont("OpenSans-Light", 44)
    c.setFillColor(Color(1, 1, 1, 0.88))
    c.drawString(36, H - 344, "& IT Controls")

    # Teal rule under title — precise cartographic underline
    c.setFillColor(TEAL)
    c.rect(36, H - 360, 180, 1.5, fill=1, stroke=0)

    # Client name — secondary monumental
    c.setFont("OpenSans-Bold", 18)
    c.setFillColor(ORANGE)
    c.drawString(36, H - 400, "AMPAC BUSINESS CAPITAL")

    c.setFont("OpenSans", 12)
    c.setFillColor(Color(1, 1, 1, 0.70))
    c.drawString(36, H - 424, "SBA 504 Lender  |  CDFI")
    c.setFont("OpenSans-Light", 11)
    c.setFillColor(Color(1, 1, 1, 0.50))
    c.drawString(36, H - 444, "California  \u00b7  Arizona  \u00b7  Nevada")

    # Right-side cartographic legend — framework + controls metrics
    bx = W - 200
    by = H - 220

    # Legend box — subtle border, well-spaced
    c.setStrokeColor(Color(1, 1, 1, 0.06))
    c.setLineWidth(0.5)
    c.setFillColor(Color(1, 1, 1, 0.04))
    c.roundRect(bx - 16, by - 140, 192, 170, 3, fill=1, stroke=1)

    # Legend title — well above the numbers
    c.setFont("OpenSans-SemiBold", 7)
    c.setFillColor(Color(1, 1, 1, 0.35))
    c.drawString(bx - 4, by + 14, "ASSESSMENT SUMMARY")
    c.setStrokeColor(Color(1, 1, 1, 0.08))
    c.line(bx - 4, by + 6, bx + 160, by + 6)

    # Metric 1: Frameworks — number left, labels right, no overlap
    c.setFont("OpenSans-ExtraBold", 42)
    c.setFillColor(BLUE)
    c.drawString(bx, by - 28, "8")
    c.setFont("OpenSans", 11)
    c.setFillColor(Color(1, 1, 1, 0.60))
    c.drawString(bx + 36, by - 16, "Regulatory")
    c.drawString(bx + 36, by - 30, "Frameworks")

    # Divider
    c.setStrokeColor(Color(1, 1, 1, 0.06))
    c.line(bx - 4, by - 50, bx + 160, by - 50)

    # Metric 2: Controls — clear spacing below divider
    c.setFont("OpenSans-ExtraBold", 42)
    c.setFillColor(TEAL)
    c.drawString(bx - 2, by - 88, "52")
    c.setFont("OpenSans", 11)
    c.setFillColor(Color(1, 1, 1, 0.60))
    c.drawString(bx + 48, by - 76, "IT Controls")
    c.drawString(bx + 48, by - 90, "Identified")

    # Bottom band — layered for depth
    c.setFillColor(Color(0, 0, 0, 0.35))
    c.rect(0, 0, W, 88, fill=1, stroke=0)

    # Orange accent — bottom edge
    c.setFillColor(ORANGE)
    c.rect(0, 0, W, 3.5, fill=1, stroke=0)

    # Teal thin line above orange
    c.setFillColor(TEAL)
    c.rect(0, 3.5, W, 0.5, fill=1, stroke=0)

    # Bottom info — three columns, precise alignment
    col1 = 36
    col2 = W / 2 - 40
    col3 = W - 175

    c.setFont("OpenSans-SemiBold", 7)
    c.setFillColor(Color(1, 1, 1, 0.40))
    c.drawString(col1, 58, "PREPARED BY")
    c.setFont("OpenSans-Bold", 11)
    c.setFillColor(TEAL)
    c.drawString(col1, 40, "Technijian")
    c.setFont("OpenSans-Light", 7.5)
    c.setFillColor(Color(1, 1, 1, 0.40))
    c.drawString(col1, 24, "Technology as a Solution")

    c.setFont("OpenSans-SemiBold", 7)
    c.setFillColor(Color(1, 1, 1, 0.40))
    c.drawString(col2, 58, "DATE")
    c.setFont("OpenSans-Bold", 11)
    c.setFillColor(white)
    c.drawString(col2, 40, "April 10, 2026")

    c.setFont("OpenSans-SemiBold", 7)
    c.setFillColor(Color(1, 1, 1, 0.40))
    c.drawString(col3, 58, "DOCUMENT ID")
    c.setFont("OpenSans-Bold", 11)
    c.setFillColor(white)
    c.drawString(col3, 40, "AMPAC-CFR-001")

    c.showPage()


# ═══════════════════════════════════════════════════════════════
#  PAGE 2 — EXECUTIVE OVERVIEW / FRAMEWORK MAP
# ═══════════════════════════════════════════════════════════════

def page_exec_overview(c):
    """Framework overview — cartographic map of all 8 frameworks."""
    # Off-white background
    c.setFillColor(OFF_WHITE)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Use standard header
    draw_header(c, 2, "COMPLIANCE FRAMEWORK OVERVIEW")

    # Section title
    y = H - 80
    c.setFont("OpenSans-ExtraBold", 13)
    c.setFillColor(BLUE)
    c.drawString(36, y, "REGULATORY LANDSCAPE")
    draw_ruled_line(c, 36, W - 36, y - 8, LIGHT_GREY, 0.5)

    # Intro text
    y -= 28
    y = text_block(c,
        "As an SBA 504 lender and CDFI, AMPAC Business Capital operates under eight intersecting regulatory "
        "frameworks. Each framework mandates specific IT controls that Technijian will implement, monitor, and "
        "maintain. The map below identifies each framework, its governing authority, and the number of IT controls required.",
        36, y, "OpenSans", 9.5, GREY, max_w=W - 72)
    y -= 12

    # Framework cards — 2 columns, 4 rows
    frameworks = [
        ("01", "SBA LOAN PROGRAMS", "SOP 50 10 / 13 CFR 120", "SBA", "8 Controls", BLUE),
        ("02", "CDFI COMPLIANCE", "12 CFR 1805 / Treasury", "Treasury CDFI Fund", "6 Controls", TEAL),
        ("03", "FAIR LENDING / ECOA", "Regulation B / FHA", "CFPB / DOJ", "7 Controls", BLUE),
        ("04", "AML / BSA / KYC", "31 USC 5301 / FinCEN", "FinCEN / OCC", "9 Controls", ORANGE),
        ("05", "INFORMATION SECURITY", "GLBA Safeguards Rule", "FTC / CFPB", "8 Controls", TEAL),
        ("06", "FCRA", "15 USC 1681", "CFPB / FTC", "5 Controls", BLUE),
        ("07", "DATA PRIVACY", "CCPA / CPRA / CalOPPA", "CA Privacy Agency", "5 Controls", ORANGE),
        ("08", "CONSUMER PROTECTION", "TILA / UDAAP / Dodd-Frank", "CFPB", "4 Controls", TEAL),
    ]

    card_w = (W - 72 - 16) / 2  # two columns with 16pt gap
    card_h = 72
    gap_x = 16
    gap_y = 10
    start_x = 36
    start_y = y

    for i, (num, name, reg, auth, ctrls, color) in enumerate(frameworks):
        col = i % 2
        row = i // 2
        cx = start_x + col * (card_w + gap_x)
        cy = start_y - row * (card_h + gap_y)

        # Card background
        c.setFillColor(white)
        c.roundRect(cx, cy - card_h, card_w, card_h, 3, fill=1, stroke=0)

        # Left accent bar
        c.setFillColor(color)
        c.rect(cx, cy - card_h, 4, card_h, fill=1, stroke=0)

        # Number
        c.setFont("OpenSans-ExtraBold", 24)
        c.setFillColor(color)
        c.drawString(cx + 14, cy - 30, num)

        # Name
        c.setFont("OpenSans-Bold", 10)
        c.setFillColor(DARK)
        c.drawString(cx + 50, cy - 18, name)

        # Regulation
        c.setFont("OpenSans-Light", 8)
        c.setFillColor(GREY)
        c.drawString(cx + 50, cy - 31, reg)

        # Authority
        c.setFont("OpenSans-Light", 8)
        c.drawString(cx + 50, cy - 43, f"Authority: {auth}")

        # Controls badge
        badge_w = pdfmetrics.stringWidth(ctrls, "OpenSans-SemiBold", 8) + 16
        bx = cx + card_w - badge_w - 12
        by_badge = cy - 64
        c.setFillColor(Color(color.red, color.green, color.blue, 0.12))
        c.roundRect(bx, by_badge, badge_w, 18, 9, fill=1, stroke=0)
        c.setFont("OpenSans-SemiBold", 8)
        c.setFillColor(color)
        c.drawString(bx + 8, by_badge + 5, ctrls)

    # Bottom summary bar
    bar_y = start_y - 4 * (card_h + gap_y) - 20
    c.setFillColor(DARK)
    c.roundRect(36, bar_y - 40, W - 72, 40, 4, fill=1, stroke=0)

    c.setFont("OpenSans-SemiBold", 8)
    c.setFillColor(Color(1, 1, 1, 0.5))
    c.drawString(50, bar_y - 17, "TOTAL FRAMEWORKS")
    c.setFont("OpenSans-ExtraBold", 16)
    c.setFillColor(ORANGE)
    c.drawString(50, bar_y - 34, "8")

    c.setFont("OpenSans-SemiBold", 8)
    c.setFillColor(Color(1, 1, 1, 0.5))
    c.drawString(180, bar_y - 17, "TOTAL IT CONTROLS")
    c.setFont("OpenSans-ExtraBold", 16)
    c.setFillColor(TEAL)
    c.drawString(180, bar_y - 34, "52")

    c.setFont("OpenSans-SemiBold", 8)
    c.setFillColor(Color(1, 1, 1, 0.5))
    c.drawString(320, bar_y - 17, "GOVERNING AUTHORITIES")
    c.setFont("OpenSans-ExtraBold", 16)
    c.setFillColor(BLUE)
    c.drawString(320, bar_y - 34, "12+")

    c.setFont("OpenSans-SemiBold", 8)
    c.setFillColor(Color(1, 1, 1, 0.5))
    c.drawString(460, bar_y - 17, "CRITICALITY")
    c.setFont("OpenSans-ExtraBold", 16)
    c.setFillColor(ORANGE)
    c.drawString(460, bar_y - 34, "HIGH")

    # Footer
    draw_footer(c, 2)
    c.showPage()


# ═══════════════════════════════════════════════════════════════
#  FRAMEWORK DETAIL PAGES (Pages 3-6) — Two frameworks per page
# ═══════════════════════════════════════════════════════════════

FRAMEWORK_DETAILS = [
    {
        "num": "01",
        "name": "SBA LOAN PROGRAMS",
        "subtitle": "SOP 50 10  |  13 CFR Part 120  |  SBA Form 1919",
        "color": BLUE,
        "desc": "The Small Business Administration governs all SBA 504 and 7(a) loan programs through Standard Operating Procedure 50 10. Lenders must verify 100% U.S. citizen ownership, perform credit analysis, and maintain minimum activity levels.",
        "controls": [
            ("Identity & Ownership Verification System", "Automated borrower identity verification with multi-layer ownership tracing through entity structures. Integration with government databases for citizenship confirmation."),
            ("Loan Origination System (LOS) Compliance Module", "Configurable underwriting rules engine enforcing SBA eligibility criteria, loan limits ($350K for 7(a) small loans), and credit analysis documentation requirements."),
            ("Document Management & Retention", "Encrypted digital vault for Form 1919, ownership documentation, credit memoranda, and SBA correspondence with 7-year retention and audit trail."),
            ("SBA Reporting Automation", "Automated generation of SBA-required reports including loan activity, portfolio performance, and compliance certifications."),
            ("Credit Scoring & Decision Engine", "Alternative credit scoring models replacing FICO SBSS (sunset March 2026) with documented decision rationale and audit capabilities."),
            ("Segregation of Duties Controls", "Role-based access ensuring loan origination, underwriting, approval, and servicing are performed by separate authorized personnel."),
            ("Change Management for Regulatory Updates", "Tracked process for implementing SBA policy changes with testing, approval workflows, and rollback capabilities."),
            ("Audit Trail & Compliance Logging", "Immutable logging of all loan decisions, document access, system changes, and regulatory submissions."),
        ]
    },
    {
        "num": "02",
        "name": "CDFI COMPLIANCE",
        "subtitle": "12 CFR Part 1805  |  U.S. Treasury CDFI Fund",
        "color": TEAL,
        "desc": "As a certified CDFI, AMPAC must demonstrate service to target markets, maintain development services alongside lending, comply with anti-discrimination requirements, and provide full transparency to Treasury oversight.",
        "controls": [
            ("Target Market Analytics Platform", "GIS-enabled system tracking lending activity by Investment Area and Targeted Population demographics with real-time compliance dashboards."),
            ("Community Impact Reporting System", "Automated data collection and reporting for CDFI Fund annual submissions including financial products, development services, and impact metrics."),
            ("Anti-Discrimination Policy Management", "Digital policy repository with annual certification workflows, employee acknowledgment tracking, and CDFI Fund audit-ready documentation."),
            ("Treasury Audit Access Controls", "Secure, role-based access provisioning for CDFI Fund examiners with granular permissions to books, records, and financial statements."),
            ("Development Services Tracking", "CRM module tracking technical assistance, financial literacy programs, and business development services provided alongside lending products."),
            ("CDFI Certification Compliance Dashboard", "Continuous monitoring of all CDFI certification requirements with alerting for approaching thresholds or material changes."),
        ]
    },
    {
        "num": "03",
        "name": "FAIR LENDING / ECOA",
        "subtitle": "Regulation B (12 CFR 202)  |  Fair Housing Act",
        "color": BLUE,
        "desc": "ECOA and the Fair Housing Act prohibit discrimination in all credit transactions. AMPAC must monitor lending decisions for disparate treatment and disparate impact across all protected classes.",
        "controls": [
            ("Fair Lending Monitoring & Analytics", "Statistical analysis engine testing underwriting decisions, pricing, and marketing for disparate impact across race, sex, age, national origin, and other protected classes."),
            ("Adverse Action Notice System", "Automated generation of compliant adverse action notices with specific denial reasons, credit reporting agency information, and consumer rights disclosures."),
            ("Loan Pricing Compliance Engine", "Rate and fee validation ensuring consistent pricing across borrower demographics with exception reporting and management override documentation."),
            ("Application Data Integrity Controls", "Input validation preventing collection of prohibited information on applications while enabling HMDA-required demographic monitoring fields."),
            ("Decision Documentation System", "Structured underwriting decision capture requiring documented rationale, supporting data, and supervisor review for all credit decisions."),
            ("Marketing & Outreach Compliance Review", "Workflow for legal/compliance review of all marketing materials, advertising, and outreach programs before distribution."),
            ("Fair Lending Training & Certification Tracker", "LMS integration tracking mandatory fair lending training completion, testing scores, and annual recertification for all lending staff."),
        ]
    },
    {
        "num": "04",
        "name": "AML / BSA / KYC",
        "subtitle": "Bank Secrecy Act  |  31 USC 5301  |  FinCEN  |  OFAC",
        "color": ORANGE,
        "desc": "Financial crime prevention requires comprehensive customer due diligence, transaction monitoring, suspicious activity reporting, and sanctions screening across all borrower relationships.",
        "controls": [
            ("Customer Identification Program (CIP)", "Automated identity verification integrating government ID validation, address verification, and tax ID confirmation against authoritative databases."),
            ("Beneficial Ownership Registry", "Entity resolution system identifying and documenting all beneficial owners (25%+ threshold) with ongoing monitoring for ownership changes."),
            ("OFAC / Sanctions Screening Engine", "Real-time screening of all borrowers, guarantors, and beneficial owners against SDN, Sectoral Sanctions, and consolidated screening lists with automated alerting."),
            ("Transaction Monitoring System", "Rule-based and behavioral analytics monitoring loan disbursements, payments, and related transactions for structuring, layering, and anomalous patterns."),
            ("SAR Filing & Case Management", "Secure workflow for suspicious activity investigation, SAR preparation, FinCEN e-filing, and 5-year record retention with strict access controls."),
            ("Enhanced Due Diligence (EDD) Module", "Risk-tiered CDD framework with automated triggers for EDD based on geography, entity complexity, PEP status, and negative media screening."),
            ("BSA/AML Risk Assessment", "Enterprise-wide annual risk assessment tool evaluating products, services, customers, and geographies with documented risk ratings and mitigation strategies."),
            ("BSA Training & Compliance Calendar", "Automated scheduling and tracking of annual BSA training, independent audit, board reporting, and regulatory filing deadlines."),
            ("Currency Transaction Reporting (CTR)", "Automated detection and filing of transactions exceeding $10,000 with aggregation logic for multiple same-day transactions."),
        ]
    },
    {
        "num": "05",
        "name": "INFORMATION SECURITY",
        "subtitle": "GLBA Safeguards Rule  |  16 CFR 314",
        "color": TEAL,
        "desc": "The Safeguards Rule requires a comprehensive information security program with a designated CISO, annual risk assessments, encryption, access controls, and continuous monitoring.",
        "controls": [
            ("Information Security Program & Governance", "Written infosec program with CISO designation, board reporting, policy library, and annual program assessment aligned to NIST CSF."),
            ("Risk Assessment & Management", "Annual risk assessment of all systems processing customer information with threat modeling, vulnerability identification, and risk treatment plans."),
            ("Data Encryption (Transit & Rest)", "TLS 1.3 for data in transit, AES-256 for data at rest across all systems storing customer financial information, PII, and credentials."),
            ("Identity & Access Management (IAM)", "Centralized IAM with MFA enforcement, least-privilege access, quarterly access reviews, and automated deprovisioning for terminated employees."),
            ("Endpoint Detection & Response (EDR)", "Enterprise EDR deployment across all endpoints with 24/7 SOC monitoring, automated threat containment, and incident response integration."),
            ("Vulnerability Management & Patching", "Continuous vulnerability scanning with risk-based prioritization, 30/60/90-day SLA patching cycles, and compensating control documentation."),
            ("Incident Response & Breach Notification", "Documented IR plan with defined roles, communication templates, forensic procedures, and regulatory notification workflows (state AG, consumers)."),
            ("Vendor Risk Management", "Third-party security assessment program with SOC 2 / penetration test requirements, contractual security obligations, and ongoing monitoring."),
        ]
    },
    {
        "num": "06",
        "name": "FCRA",
        "subtitle": "Fair Credit Reporting Act  |  15 USC 1681",
        "color": BLUE,
        "desc": "FCRA governs the use of consumer credit information in lending decisions, requiring proper disclosures, consent, adverse action notices, and dispute resolution procedures.",
        "controls": [
            ("Credit Report Consent & Disclosure System", "Digital consent capture with timestamp, IP logging, and secure storage prior to any credit bureau inquiry. Clear disclosure of intended use."),
            ("Adverse Action Integration", "Automated adverse action notices triggered by credit-based decisions including specific factors, CRA contact information, and free report rights."),
            ("Dispute Resolution Workflow", "Consumer dispute intake, investigation tracking, 30-day response SLA monitoring, and correction propagation to credit bureaus."),
            ("Credit Bureau Access Controls", "Restricted access to credit pull capabilities with role-based permissions, permissible purpose documentation, and usage audit logging."),
            ("Pre-Screen Opt-Out Compliance", "Firm offer of credit procedures with opt-out list maintenance, IRS pre-screen certification, and marketing compliance documentation."),
        ]
    },
    {
        "num": "07",
        "name": "DATA PRIVACY",
        "subtitle": "CCPA / CPRA  |  CalOPPA  |  GLBA Privacy Rule",
        "color": ORANGE,
        "desc": "California privacy laws and the GLBA Privacy Rule require transparent data practices, consumer rights fulfillment, opt-out mechanisms, and privacy-by-design across all systems processing personal information.",
        "controls": [
            ("Privacy Notice & Policy Management", "Centralized privacy notice generation covering GLBA annual notice, CCPA/CPRA disclosures, and CalOPPA online privacy policy with version control."),
            ("Consumer Rights Request Portal", "Self-service portal and workflow for CCPA rights: access, deletion, correction, portability, and opt-out of sale/sharing with 45-day SLA tracking."),
            ("Data Inventory & Classification", "Automated data discovery and classification across all systems identifying PII, financial data, and sensitive categories with data flow mapping."),
            ("Opt-Out & Consent Management", "Granular consent management for GLBA non-affiliated sharing, CCPA Do Not Sell, and marketing preferences with centralized preference store."),
            ("Data Retention & Disposal", "Automated retention schedule enforcement with secure disposal procedures (NIST 800-88) and certificate-of-destruction documentation."),
        ]
    },
    {
        "num": "08",
        "name": "CONSUMER PROTECTION",
        "subtitle": "TILA / Regulation Z  |  UDAAP  |  Dodd-Frank",
        "color": TEAL,
        "desc": "Truth in Lending and UDAAP protections require transparent loan disclosures, fair lending terms, accurate APR calculations, and prohibition of unfair, deceptive, or abusive practices.",
        "controls": [
            ("Loan Disclosure Engine", "Automated Loan Estimate and Closing Disclosure generation with APR calculation, fee itemization, and 3-day delivery tracking for TILA compliance."),
            ("UDAAP Monitoring Framework", "Complaint analytics, marketing review workflows, and fee structure analysis identifying potential unfair, deceptive, or abusive practices."),
            ("APR Calculation & Validation", "Independent APR calculation engine with tolerance testing, finance charge verification, and exception reporting for regulatory accuracy."),
            ("Complaint Management System", "Centralized intake, categorization, investigation, and resolution tracking for consumer complaints with CFPB reporting integration."),
        ]
    },
]


def draw_header(c, page_num, title=""):
    """Standard page header — refined with registration marks."""
    c.setFillColor(DARK)
    c.rect(0, H - 52, W, 52, fill=1, stroke=0)
    c.setFillColor(ORANGE)
    c.rect(0, H - 54.5, W, 2.5, fill=1, stroke=0)
    # Teal hairline above orange
    c.setFillColor(TEAL)
    c.rect(0, H - 52, W, 0.4, fill=1, stroke=0)

    draw_logo(c, 36, H - 42, h=22, dark_bg=True)
    if title:
        c.setFont("OpenSans-Bold", 11)
        c.setFillColor(white)
        c.drawString(155, H - 37, title)

    c.setFont("OpenSans-Light", 7)
    c.setFillColor(Color(1, 1, 1, 0.45))
    c.drawRightString(W - 36, H - 37, f"AMPAC-CFR-001  |  P.{page_num:02d}")


def draw_footer(c, page_num):
    """Standard page footer — refined with dual accent lines."""
    c.setFillColor(DARK)
    c.rect(0, 0, W, 26, fill=1, stroke=0)
    c.setFillColor(ORANGE)
    c.rect(0, 26, W, 2, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.rect(0, 28, W, 0.4, fill=1, stroke=0)

    c.setFont("OpenSans-Light", 6)
    c.setFillColor(Color(1, 1, 1, 0.40))
    c.drawString(36, 9, "Technijian  |  18 Technology Dr, Ste 141, Irvine, CA 92618  |  949.379.8500  |  technijian.com")
    c.drawRightString(W - 36, 9, f"CONFIDENTIAL  |  Page {page_num}")


def draw_framework_section(c, fw, y_start, available_h):
    """Draw a single framework section. Returns y after section."""
    x_left = 36
    x_right = W - 36
    content_w = x_right - x_left
    y = y_start

    # Framework number + name header
    # Accent bar
    c.setFillColor(fw["color"])
    c.rect(x_left, y - 2, content_w, 2, fill=1, stroke=0)
    y -= 22

    # Number circle
    c.setFillColor(fw["color"])
    c.circle(x_left + 15, y - 2, 15, fill=1, stroke=0)
    c.setFont("OpenSans-ExtraBold", 13)
    c.setFillColor(white)
    nw = pdfmetrics.stringWidth(fw["num"], "OpenSans-ExtraBold", 13)
    c.drawString(x_left + 15 - nw / 2, y - 7, fw["num"])

    # Name
    c.setFont("OpenSans-ExtraBold", 14)
    c.setFillColor(DARK)
    c.drawString(x_left + 40, y - 5, fw["name"])

    # Subtitle
    c.setFont("OpenSans-Light", 8.5)
    c.setFillColor(GREY)
    c.drawString(x_left + 40, y - 19, fw["subtitle"])

    y -= 34

    # Description
    y = text_block(c, fw["desc"], x_left + 8, y, "OpenSans", 9, GREY, max_w=content_w - 16, leading=12.5)
    y -= 10

    # Controls table header
    c.setFillColor(Color(fw["color"].red, fw["color"].green, fw["color"].blue, 0.08))
    c.rect(x_left, y - 16, content_w, 16, fill=1, stroke=0)
    c.setFont("OpenSans-SemiBold", 8)
    c.setFillColor(fw["color"])
    c.drawString(x_left + 8, y - 12, "IT CONTROL")
    c.drawString(x_left + 190, y - 12, "IMPLEMENTATION REQUIREMENT")
    y -= 20

    # Controls rows
    CTRL_NAME_W = 175
    DESC_X = x_left + 190
    DESC_W = content_w - 198
    FONT_NAME_SZ = 8
    FONT_DESC_SZ = 7.5

    for i, (ctrl_name, ctrl_desc) in enumerate(fw["controls"]):
        # Estimate row height
        desc_lines = max(1, int(pdfmetrics.stringWidth(ctrl_desc, "OpenSans-Light", FONT_DESC_SZ) / DESC_W) + 1)
        name_lines_est = max(1, int(pdfmetrics.stringWidth(ctrl_name, "OpenSans-SemiBold", FONT_NAME_SZ) / CTRL_NAME_W) + 1)
        row_h = max(20, max(desc_lines, name_lines_est) * 11 + 8)

        if y - row_h < 40:
            break  # Don't overflow

        # Alternating row background
        if i % 2 == 0:
            c.setFillColor(Color(0.96, 0.97, 0.98, 1))
            c.rect(x_left, y - row_h, content_w, row_h, fill=1, stroke=0)

        # Control name — wrapped
        c.setFont("OpenSans-SemiBold", FONT_NAME_SZ)
        c.setFillColor(DARK)
        name_y = y - 12
        name_lines = []
        words = ctrl_name.split()
        current = ""
        for w in words:
            test = current + (" " if current else "") + w
            if pdfmetrics.stringWidth(test, "OpenSans-SemiBold", FONT_NAME_SZ) <= CTRL_NAME_W:
                current = test
            else:
                name_lines.append(current)
                current = w
        if current:
            name_lines.append(current)
        for nl in name_lines:
            c.drawString(x_left + 8, name_y, nl)
            name_y -= 11

        # Control description — wrapped
        c.setFont("OpenSans-Light", FONT_DESC_SZ)
        c.setFillColor(GREY)
        desc_y = y - 12
        dwords = ctrl_desc.split()
        dcurrent = ""
        for w in dwords:
            test = dcurrent + (" " if dcurrent else "") + w
            if pdfmetrics.stringWidth(test, "OpenSans-Light", FONT_DESC_SZ) <= DESC_W:
                dcurrent = test
            else:
                c.drawString(DESC_X, desc_y, dcurrent)
                desc_y -= 11
                dcurrent = w
        if dcurrent:
            c.drawString(DESC_X, desc_y, dcurrent)

        y -= row_h

    return y


def page_framework_detail(c, fw_pair, page_num):
    """Draw a page with one or two framework detail sections."""
    c.setFillColor(OFF_WHITE)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Subtle dot grid in left margin only
    draw_dot_grid(c, 0, 30, 28, H - 84, spacing=15, radius=0.3,
                  color=Color(0.82, 0.84, 0.88, 0.3))

    draw_header(c, page_num, "IT CONTROLS BY FRAMEWORK")
    draw_footer(c, page_num)

    y = H - 76

    for fw in fw_pair:
        y = draw_framework_section(c, fw, y, 0)
        y -= 18

    c.showPage()


# ═══════════════════════════════════════════════════════════════
#  PAGE 7 — COMPLIANCE PRIORITY MATRIX
# ═══════════════════════════════════════════════════════════════

def page_priority_matrix(c):
    c.setFillColor(OFF_WHITE)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    draw_header(c, 7, "COMPLIANCE PRIORITY MATRIX")
    draw_footer(c, 7)

    y = H - 82

    # Section title
    c.setFont("OpenSans-ExtraBold", 13)
    c.setFillColor(BLUE)
    c.drawString(36, y, "IMPLEMENTATION PRIORITY & TIMELINE")
    draw_ruled_line(c, 36, W - 36, y - 8, LIGHT_GREY, 0.5)
    y -= 28

    text_block(c,
        "The matrix below prioritizes framework implementation based on regulatory criticality, enforcement risk, "
        "and implementation complexity. All CRITICAL frameworks must be addressed within 90 days.",
        36, y, "OpenSans", 9.5, GREY, max_w=W - 72)
    y -= 38

    # Table header
    cols = [36, 200, 300, 385, 470, W - 36]
    headers = ["FRAMEWORK", "CRITICALITY", "EFFORT", "TIMELINE", "OWNER"]

    c.setFillColor(DARK)
    c.rect(cols[0], y - 20, cols[-1] - cols[0], 20, fill=1, stroke=0)
    c.setFont("OpenSans-SemiBold", 8)
    c.setFillColor(white)
    for i, h in enumerate(headers):
        c.drawString(cols[i] + 8, y - 14, h)
    y -= 22

    rows = [
        ("SBA Loan Programs (SOP 50 10)", "CRITICAL", ORANGE, "High", "90 days", "Compliance"),
        ("CDFI Compliance (Treasury)", "CRITICAL", ORANGE, "High", "90 days", "Operations"),
        ("Fair Lending / ECOA", "CRITICAL", ORANGE, "High", "60 days", "Legal"),
        ("AML / BSA / KYC", "CRITICAL", ORANGE, "High", "90 days", "BSA Officer"),
        ("Information Security (GLBA)", "HIGH", BLUE, "High", "120 days", "IT / CISO"),
        ("FCRA Compliance", "HIGH", BLUE, "Medium", "45 days", "Underwriting"),
        ("Data Privacy (CCPA/CPRA)", "HIGH", BLUE, "Medium", "90 days", "Legal"),
        ("Consumer Protection (TILA)", "MODERATE", TEAL, "Medium", "60 days", "Compliance"),
    ]

    for i, (name, crit, crit_color, effort, timeline, owner) in enumerate(rows):
        row_h = 28
        ry = y - row_h

        if i % 2 == 0:
            c.setFillColor(Color(0.96, 0.97, 0.98, 1))
            c.rect(cols[0], ry, cols[-1] - cols[0], row_h, fill=1, stroke=0)

        c.setFont("OpenSans-SemiBold", 8.5)
        c.setFillColor(DARK)
        c.drawString(cols[0] + 8, ry + 9, name)

        # Criticality badge
        badge_w = pdfmetrics.stringWidth(crit, "OpenSans-Bold", 7.5) + 16
        c.setFillColor(Color(crit_color.red, crit_color.green, crit_color.blue, 0.15))
        c.roundRect(cols[1] + 8, ry + 6, badge_w, 17, 8, fill=1, stroke=0)
        c.setFont("OpenSans-Bold", 7.5)
        c.setFillColor(crit_color)
        c.drawString(cols[1] + 16, ry + 10, crit)

        c.setFont("OpenSans", 8.5)
        c.setFillColor(GREY)
        c.drawString(cols[2] + 8, ry + 9, effort)
        c.drawString(cols[3] + 8, ry + 9, timeline)

        c.setFont("OpenSans-Light", 8)
        c.drawString(cols[4] + 8, ry + 9, owner)

        y -= row_h

    # Timeline visualization
    y -= 30
    c.setFont("OpenSans-ExtraBold", 13)
    c.setFillColor(BLUE)
    c.drawString(36, y, "IMPLEMENTATION TIMELINE")
    draw_ruled_line(c, 36, W - 36, y - 8, LIGHT_GREY, 0.5)
    y -= 32

    # Timeline bar chart
    phases = [
        ("Phase 1: Governance & Policy", 0, 30, ORANGE),
        ("Phase 2: Fair Lending & FCRA", 15, 60, BLUE),
        ("Phase 3: AML/BSA Program", 20, 90, ORANGE),
        ("Phase 4: Information Security", 30, 120, TEAL),
        ("Phase 5: Data Privacy & Consumer", 45, 90, BLUE),
        ("Phase 6: Testing & Audit", 60, 120, TEAL),
    ]

    bar_x = 220
    bar_max_w = W - 36 - bar_x
    max_days = 120

    # Day markers
    for d in [0, 30, 60, 90, 120]:
        dx = bar_x + (d / max_days) * bar_max_w
        c.setFont("OpenSans-Light", 7.5)
        c.setFillColor(GREY)
        c.drawCentredString(dx, y + 5, f"Day {d}")
        draw_vertical_rule(c, dx, y - len(phases) * 26 - 5, y, Color(0.85, 0.87, 0.90, 0.5), 0.3)

    for i, (label, start, end, color) in enumerate(phases):
        py = y - i * 26

        c.setFont("OpenSans-SemiBold", 8)
        c.setFillColor(DARK)
        c.drawRightString(bar_x - 10, py - 9, label)

        sx = bar_x + (start / max_days) * bar_max_w
        ew = ((end - start) / max_days) * bar_max_w
        c.setFillColor(Color(color.red, color.green, color.blue, 0.8))
        c.roundRect(sx, py - 14, ew, 13, 4, fill=1, stroke=0)

    c.showPage()


# ═══════════════════════════════════════════════════════════════
#  PAGE 8 — NEXT STEPS / CONTACT
# ═══════════════════════════════════════════════════════════════

def page_next_steps(c):
    c.setFillColor(OFF_WHITE)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    draw_header(c, 8, "NEXT STEPS & ENGAGEMENT")
    draw_footer(c, 8)

    y = H - 82

    c.setFont("OpenSans-ExtraBold", 13)
    c.setFillColor(BLUE)
    c.drawString(36, y, "RECOMMENDED NEXT STEPS")
    draw_ruled_line(c, 36, W - 36, y - 8, LIGHT_GREY, 0.5)
    y -= 30

    steps = [
        ("01", "COMPLIANCE GAP ASSESSMENT", "Technijian conducts a comprehensive gap analysis comparing AMPAC's current IT infrastructure, policies, and procedures against all 52 identified IT controls.", "5-10 Business Days", BLUE),
        ("02", "GOVERNANCE & POLICY DEVELOPMENT", "Establish compliance governance structure including CCO designation, BSA/AML Officer appointment, and board-level oversight. Develop all required policies and documentation.", "30 Days", ORANGE),
        ("03", "TECHNOLOGY IMPLEMENTATION", "Deploy and configure all IT control systems including identity verification, OFAC screening, transaction monitoring, encryption, IAM, EDR, and compliance platforms.", "60-90 Days", TEAL),
        ("04", "STAFF TRAINING & CERTIFICATION", "Deliver role-based compliance training covering fair lending, AML/KYC, data security, privacy requirements, and SBA regulatory updates. Establish ongoing training calendar and certification tracking.", "Ongoing", BLUE),
        ("05", "INDEPENDENT TESTING & AUDIT", "Conduct independent testing of all compliance programs including AML/BSA audit, fair lending review, information security risk assessment, and CDFI certification compliance verification.", "Annual", ORANGE),
    ]

    for num, title, desc, timeline, color in steps:
        # Step card
        card_h = 72
        c.setFillColor(white)
        c.roundRect(36, y - card_h, W - 72, card_h, 4, fill=1, stroke=0)

        # Left accent
        c.setFillColor(color)
        c.rect(36, y - card_h, 4, card_h, fill=1, stroke=0)

        # Number
        c.setFont("OpenSans-ExtraBold", 20)
        c.setFillColor(color)
        c.drawString(50, y - 26, num)

        # Title
        c.setFont("OpenSans-Bold", 10.5)
        c.setFillColor(DARK)
        c.drawString(84, y - 18, title)

        # Timeline badge
        tw = pdfmetrics.stringWidth(timeline, "OpenSans-SemiBold", 8) + 16
        c.setFillColor(Color(color.red, color.green, color.blue, 0.12))
        c.roundRect(W - 36 - tw - 12, y - 22, tw, 18, 9, fill=1, stroke=0)
        c.setFont("OpenSans-SemiBold", 8)
        c.setFillColor(color)
        c.drawString(W - 36 - tw - 4, y - 17, timeline)

        # Description
        text_block(c, desc, 84, y - 36, "OpenSans-Light", 8.5, GREY, max_w=W - 72 - 66, leading=11)

        y -= card_h + 10

    # Contact section
    y -= 12
    c.setFont("OpenSans-ExtraBold", 13)
    c.setFillColor(BLUE)
    c.drawString(36, y, "CONTACT")
    draw_ruled_line(c, 36, W - 36, y - 8, LIGHT_GREY, 0.5)
    y -= 28

    # Contact card
    c.setFillColor(DARK)
    c.roundRect(36, y - 90, W - 72, 90, 6, fill=1, stroke=0)

    draw_logo(c, 52, y - 55, h=26, dark_bg=True)

    c.setFont("OpenSans-Bold", 12)
    c.setFillColor(white)
    c.drawString(200, y - 25, "Technijian")
    c.setFont("OpenSans-Light", 9)
    c.setFillColor(Color(1, 1, 1, 0.7))
    c.drawString(200, y - 40, "Technology as a Solution")

    c.setFont("OpenSans", 9)
    c.setFillColor(TEAL)
    c.drawString(200, y - 58, "18 Technology Dr, Ste 141, Irvine, CA 92618")
    c.setFont("OpenSans", 8.5)
    c.setFillColor(Color(1, 1, 1, 0.6))
    c.drawString(200, y - 73, "949.379.8500  |  technijian.com  |  RJain@technijian.com")

    # Orange bottom accent on card
    c.setFillColor(ORANGE)
    c.rect(36, y - 90, W - 72, 3, fill=1, stroke=0)

    c.showPage()


# ═══════════════════════════════════════════════════════════════
#  BUILD PDF
# ═══════════════════════════════════════════════════════════════

def build():
    c = canvas.Canvas(OUT_PDF, pagesize=letter)
    c.setTitle("AMPAC Business Capital — Compliance Framework & IT Controls Report")
    c.setAuthor("Technijian")
    c.setSubject("Compliance Framework Assessment")

    # Page 1: Cover
    page_cover(c)

    # Page 2: Executive Overview
    page_exec_overview(c)

    # Pages 3-6: Framework Details (2 per page)
    pairs = [
        FRAMEWORK_DETAILS[0:2],
        FRAMEWORK_DETAILS[2:4],
        FRAMEWORK_DETAILS[4:6],
        FRAMEWORK_DETAILS[6:8],
    ]
    for i, pair in enumerate(pairs):
        page_framework_detail(c, pair, i + 3)

    # Page 7: Priority Matrix & Timeline
    page_priority_matrix(c)

    # Page 8: Next Steps & Contact
    page_next_steps(c)

    c.save()
    print(f"PDF generated: {OUT_PDF}")
    print(f"Pages: 8")


if __name__ == "__main__":
    build()
