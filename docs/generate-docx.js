#!/usr/bin/env node
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, ImageRun,
        Header, Footer, AlignmentType, LevelFormat, TabStopType,
        HeadingLevel, BorderStyle, WidthType, ShadingType,
        PageNumber, PageBreak } = require('docx');
const fs = require('fs');

// === CONFIG ===
const inputFile = process.argv[2];
const outputFile = process.argv[3];
const docTitle = process.argv[4];
const docVersion = process.argv[5] || '1.0';
const docDate = process.argv[6] || 'March 6, 2026';
const coverLogoPath = process.argv[7];
const headerLogoPath = process.argv[8];

const BLUE = "0077B6";
const ORANGE = "E8762B";
const GRAY = "6D6E71";
const DARK = "333333";
const WHITE = "FFFFFF";
const LIGHT_BLUE = "E8F4FB";
const LIGHT_GRAY = "F5F5F5";

const PAGE_WIDTH = 12240;
const PAGE_HEIGHT = 15840;
const MARGIN = 1440;
const CONTENT_WIDTH = PAGE_WIDTH - 2 * MARGIN; // 9360

const coverLogoData = fs.readFileSync(coverLogoPath);
const headerLogoData = fs.readFileSync(headerLogoPath);

// === INLINE PARSER ===
function parseInline(text, baseStyle = {}) {
  if (!text) return [new TextRun({ text: '', ...baseStyle })];
  const runs = [];
  const pattern = /(\*\*(.+?)\*\*|`(.+?)`)/g;
  let lastIdx = 0;
  let m;
  while ((m = pattern.exec(text)) !== null) {
    if (m.index > lastIdx) {
      runs.push(new TextRun({ text: text.slice(lastIdx, m.index), ...baseStyle }));
    }
    if (m[2]) {
      runs.push(new TextRun({ text: m[2], bold: true, ...baseStyle }));
    } else if (m[3]) {
      const s = { ...baseStyle }; delete s.font;
      runs.push(new TextRun({ text: m[3], font: "Consolas", size: 20, ...s }));
    }
    lastIdx = m.index + m[0].length;
  }
  if (lastIdx < text.length) {
    runs.push(new TextRun({ text: text.slice(lastIdx), ...baseStyle }));
  }
  if (runs.length === 0) runs.push(new TextRun({ text: text, ...baseStyle }));
  return runs;
}

// === ASCII TABLE PARSER (for code blocks containing ASCII art tables) ===
function parseAsciiTable(codeLines) {
  const rawRows = [];
  for (const line of codeLines) {
    const trimmed = line.trim();
    // Skip separator lines (+---+---+) and empty lines
    if (!trimmed || trimmed.match(/^\+[-+\s]+\+$/) || !trimmed.includes('|')) continue;
    const cells = trimmed.split('|');
    // Remove empty entries from leading/trailing |
    if (cells[0].trim() === '') cells.shift();
    if (cells.length > 0 && cells[cells.length - 1].trim() === '') cells.pop();
    rawRows.push(cells.map(c => c.trim()));
  }
  if (rawRows.length < 2) return null;

  // Find max columns and pad shorter rows (prepend empty cells)
  const maxCols = Math.max(...rawRows.map(r => r.length));
  for (let i = 0; i < rawRows.length; i++) {
    while (rawRows[i].length < maxCols) rawRows[i].unshift('');
  }

  // Merge continuation rows (rows where most cells are empty = multi-line cell)
  const merged = [];
  for (const row of rawRows) {
    const nonEmpty = row.filter(c => c !== '').length;
    if (merged.length > 0 && nonEmpty <= 1 && row.length === merged[merged.length - 1].length) {
      const prev = merged[merged.length - 1];
      for (let j = 0; j < row.length; j++) {
        if (row[j]) prev[j] = prev[j] ? `${prev[j]} ${row[j]}` : row[j];
      }
    } else {
      merged.push([...row]);
    }
  }
  return merged;
}

// === RENDER TABLE HELPER ===
function renderTable(rows, isAscii = false) {
  const numCols = Math.max(...rows.map(r => r.length));
  const colW = Math.floor(CONTENT_WIDTH / numCols);
  const colWidths = Array(numCols).fill(colW);
  colWidths[numCols - 1] = CONTENT_WIDTH - colW * (numCols - 1);

  const bdr = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
  const borders = { top: bdr, bottom: bdr, left: bdr, right: bdr };

  const tableRows = rows.map((row, ri) => {
    const isHdr = ri === 0;
    const cells = [];
    for (let ci = 0; ci < numCols; ci++) {
      const cellText = (ci < row.length) ? row[ci] : '';
      cells.push(new TableCell({
        borders,
        width: { size: colWidths[ci], type: WidthType.DXA },
        shading: isHdr
          ? { fill: BLUE, type: ShadingType.CLEAR }
          : (ri % 2 === 0 ? { fill: LIGHT_GRAY, type: ShadingType.CLEAR } : { fill: WHITE, type: ShadingType.CLEAR }),
        margins: { top: 50, bottom: 50, left: 80, right: 80 },
        children: [new Paragraph({
          spacing: { before: 20, after: 20 },
          alignment: (isHdr || (ci > 0 && isAscii)) ? AlignmentType.CENTER : AlignmentType.LEFT,
          children: parseInline(cellText, {
            font: "Arial", size: 19,
            color: isHdr ? WHITE : DARK,
            bold: isHdr
          })
        })]
      }));
    }
    return new TableRow({ children: cells });
  });

  return new Table({
    width: { size: CONTENT_WIDTH, type: WidthType.DXA },
    columnWidths: colWidths,
    rows: tableRows
  });
}

// === MARKDOWN PARSER ===
function parseMarkdown(content) {
  const lines = content.split('\n');
  const elements = [];
  let i = 0;

  // Skip metadata before first ## heading
  while (i < lines.length && !lines[i].startsWith('## ')) i++;

  while (i < lines.length) {
    const line = lines[i];

    // Skip blank, horizontal rules, end markers
    if (line.trim() === '' || line.trim() === '---' || line.trim() === '*End of Document*') { i++; continue; }

    // Headings
    if (line.startsWith('#### ')) { elements.push({ type: 'h4', text: line.slice(5).trim() }); i++; continue; }
    if (line.startsWith('### '))  { elements.push({ type: 'h3', text: line.slice(4).trim() }); i++; continue; }
    if (line.startsWith('## '))   { elements.push({ type: 'h2', text: line.slice(3).trim() }); i++; continue; }

    // Table
    if (line.trim().startsWith('|')) {
      const rows = [];
      while (i < lines.length && lines[i].trim().startsWith('|')) {
        const row = lines[i].trim();
        if (!/^\|[\s\-:|]+\|$/.test(row)) {
          rows.push(row.split('|').slice(1, -1).map(c => c.trim()));
        }
        i++;
      }
      if (rows.length > 0) elements.push({ type: 'table', rows });
      continue;
    }

    // Blockquote
    if (line.startsWith('> ') || line === '>') {
      const qlines = [];
      while (i < lines.length && (lines[i].startsWith('> ') || lines[i] === '>' || lines[i].startsWith('>>'))) {
        qlines.push(lines[i].replace(/^>\s?/, ''));
        i++;
      }
      elements.push({ type: 'blockquote', lines: qlines });
      continue;
    }

    // Code block
    if (line.trim().startsWith('```')) {
      const code = []; i++;
      while (i < lines.length && !lines[i].trim().startsWith('```')) { code.push(lines[i]); i++; }
      i++; // skip closing
      elements.push({ type: 'code', lines: code });
      continue;
    }

    // Numbered list
    if (line.match(/^\s*\d+\.\s/)) {
      const items = [];
      while (i < lines.length) {
        const cur = lines[i];
        const nm = cur.match(/^(\s*)\d+\.\s+(.+)/);
        if (nm) {
          items.push({ text: nm[2].trim(), level: Math.floor(nm[1].length / 3), sub: [] });
          i++; continue;
        }
        // Indented bullet sub-item
        const bm = cur.match(/^\s{2,}-\s+(.+)/);
        if (bm && items.length > 0) {
          items[items.length - 1].sub.push(bm[1].trim());
          i++; continue;
        }
        // Indented continuation
        if (cur.match(/^\s{3,}\S/) && items.length > 0 && !cur.match(/^\s*\|/)) {
          items[items.length - 1].text += ' ' + cur.trim();
          i++; continue;
        }
        // Empty line - look ahead for more numbered items
        if (cur.trim() === '') {
          let la = i + 1;
          while (la < lines.length && lines[la].trim() === '') la++;
          if (la < lines.length && lines[la].match(/^\s*\d+\.\s/)) { i++; continue; }
          break;
        }
        break;
      }
      elements.push({ type: 'numList', items });
      continue;
    }

    // Bullet list
    if (line.match(/^(\s*)-\s/)) {
      const items = [];
      while (i < lines.length) {
        const cur = lines[i];
        const bm = cur.match(/^(\s*)-\s+(.+)/);
        if (bm) {
          items.push({ text: bm[2].trim(), level: Math.floor(bm[1].length / 2) });
          i++; continue;
        }
        // Continuation line (indented, not a new item)
        if (cur.match(/^\s{2,}\S/) && items.length > 0 && !cur.match(/^\s*-\s/) && !cur.match(/^\s*\d+\./) && !cur.match(/^\s*\|/)) {
          items[items.length - 1].text += ' ' + cur.trim();
          i++; continue;
        }
        break;
      }
      elements.push({ type: 'bulletList', items });
      continue;
    }

    // Regular paragraph
    elements.push({ type: 'para', text: line.trim() });
    i++;
  }
  return elements;
}

// === DOCUMENT BUILDER ===
function buildContent(elements) {
  const body = { font: "Arial", size: 22, color: DARK };
  const children = [];
  let numListIdx = 0;

  for (const el of elements) {
    switch (el.type) {
      case 'h2':
        children.push(new Paragraph({
          pageBreakBefore: true, heading: HeadingLevel.HEADING_1,
          children: parseInline(el.text, { font: "Arial", size: 32, color: BLUE, bold: true })
        }));
        break;

      case 'h3':
        children.push(new Paragraph({
          heading: HeadingLevel.HEADING_2, spacing: { before: 300, after: 200 },
          children: parseInline(el.text, { font: "Arial", size: 26, color: BLUE, bold: true })
        }));
        break;

      case 'h4':
        children.push(new Paragraph({
          heading: HeadingLevel.HEADING_3, spacing: { before: 240, after: 120 },
          children: parseInline(el.text, { font: "Arial", size: 24, color: DARK, bold: true })
        }));
        break;

      case 'para':
        children.push(new Paragraph({
          spacing: { before: 100, after: 100 },
          children: parseInline(el.text, body)
        }));
        break;

      case 'bulletList':
        for (const item of el.items) {
          let text = item.text;
          const isCheckbox = text.startsWith('[ ] ');
          if (isCheckbox) text = text.slice(4);

          if (isCheckbox) {
            children.push(new Paragraph({
              spacing: { before: 50, after: 50 },
              indent: { left: 720, hanging: 360 },
              children: [
                new TextRun({ text: "\u2610  ", font: "Segoe UI Symbol", size: 22, color: BLUE }),
                ...parseInline(text, body)
              ]
            }));
          } else {
            children.push(new Paragraph({
              numbering: { reference: "bullets", level: Math.min(item.level, 2) },
              spacing: { before: 50, after: 50 },
              children: parseInline(item.text, body)
            }));
          }
        }
        break;

      case 'numList': {
        const ref = `num_${numListIdx++}`;
        for (const item of el.items) {
          children.push(new Paragraph({
            numbering: { reference: ref, level: Math.min(item.level, 1) },
            spacing: { before: 60, after: 60 },
            children: parseInline(item.text, body)
          }));
          // Sub-bullets under this numbered item
          for (const sub of item.sub) {
            children.push(new Paragraph({
              numbering: { reference: "bullets", level: 1 },
              spacing: { before: 30, after: 30 },
              children: parseInline(sub, body)
            }));
          }
        }
        break;
      }

      case 'table': {
        children.push(new Paragraph({ spacing: { before: 100 }, children: [] }));
        children.push(renderTable(el.rows));
        children.push(new Paragraph({ spacing: { after: 100 }, children: [] }));
        break;
      }

      case 'blockquote': {
        // Render as a professional template box with shaded background
        const boxChildren = [];
        for (const ql of el.lines) {
          if (ql.trim() === '') {
            boxChildren.push(new Paragraph({ spacing: { before: 60, after: 60 }, children: [] }));
          } else {
            boxChildren.push(new Paragraph({
              spacing: { before: 40, after: 40 },
              children: parseInline(ql, { font: "Arial", size: 20, color: DARK })
            }));
          }
        }

        const boxWidth = CONTENT_WIDTH - 360;
        children.push(new Paragraph({ spacing: { before: 120 }, children: [] }));
        children.push(new Table({
          width: { size: boxWidth, type: WidthType.DXA },
          columnWidths: [boxWidth],
          rows: [new TableRow({
            children: [new TableCell({
              borders: {
                top: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" },
                bottom: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" },
                right: { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" },
                left: { style: BorderStyle.SINGLE, size: 6, color: BLUE }
              },
              shading: { fill: LIGHT_BLUE, type: ShadingType.CLEAR },
              margins: { top: 140, bottom: 140, left: 240, right: 240 },
              width: { size: boxWidth, type: WidthType.DXA },
              children: boxChildren
            })]
          })]
        }));
        children.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
        break;
      }

      case 'code': {
        // Check if this is an ASCII art table (contains | and +--- patterns)
        const hasTableMarkers = el.lines.some(l => l.includes('|')) && el.lines.some(l => l.trim().startsWith('+'));
        if (hasTableMarkers) {
          const asciiData = parseAsciiTable(el.lines);
          if (asciiData && asciiData.length > 1) {
            children.push(new Paragraph({ spacing: { before: 100 }, children: [] }));
            children.push(renderTable(asciiData, true));
            children.push(new Paragraph({ spacing: { after: 100 }, children: [] }));
            break;
          }
        }
        // Regular code block - render in a shaded box
        const codeParas = el.lines.map(cl => new Paragraph({
          spacing: { before: 10, after: 10 },
          children: [new TextRun({ text: cl || ' ', font: "Consolas", size: 17, color: DARK })]
        }));
        const codeBoxWidth = CONTENT_WIDTH - 360;
        children.push(new Paragraph({ spacing: { before: 80 }, children: [] }));
        children.push(new Table({
          width: { size: codeBoxWidth, type: WidthType.DXA },
          columnWidths: [codeBoxWidth],
          rows: [new TableRow({
            children: [new TableCell({
              borders: {
                top: { style: BorderStyle.SINGLE, size: 1, color: "DDDDDD" },
                bottom: { style: BorderStyle.SINGLE, size: 1, color: "DDDDDD" },
                left: { style: BorderStyle.SINGLE, size: 1, color: "DDDDDD" },
                right: { style: BorderStyle.SINGLE, size: 1, color: "DDDDDD" }
              },
              shading: { fill: LIGHT_GRAY, type: ShadingType.CLEAR },
              margins: { top: 100, bottom: 100, left: 200, right: 200 },
              width: { size: codeBoxWidth, type: WidthType.DXA },
              children: codeParas
            })]
          })]
        }));
        children.push(new Paragraph({ spacing: { after: 80 }, children: [] }));
        break;
      }
    }
  }
  return { children, numListCount: numListIdx };
}

// === COVER PAGE ===
function buildCoverPage(title, version, date) {
  return [
    ...Array(5).fill(null).map(() => new Paragraph({ children: [] })),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new ImageRun({
        type: "png", data: coverLogoData,
        transformation: { width: 400, height: 84 },
        altText: { title: "Technijian Logo", description: "Technijian Corporation Logo", name: "cover-logo" }
      })]
    }),
    new Paragraph({ children: [] }),
    new Paragraph({ children: [] }),
    // Blue accent bar
    new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: BLUE } }, children: [] }),
    // Orange accent bar
    new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: ORANGE } }, children: [] }),
    new Paragraph({ children: [] }),
    // Title
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { after: 200 },
      children: [new TextRun({ text: title, font: "Arial", size: 48, color: BLUE, bold: true })]
    }),
    new Paragraph({ children: [] }),
    // Orange + blue bars
    new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: ORANGE } }, children: [] }),
    new Paragraph({ border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: BLUE } }, children: [] }),
    new Paragraph({ children: [] }),
    new Paragraph({ children: [] }),
    // Metadata
    new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: `Version ${version}`, font: "Arial", size: 24, color: GRAY })] }),
    new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: date, font: "Arial", size: 24, color: GRAY })] }),
    new Paragraph({ children: [] }),
    new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: "Classification: Confidential", font: "Arial", size: 24, color: ORANGE, bold: true })] }),
    new Paragraph({ children: [] }),
    new Paragraph({ children: [] }),
    new Paragraph({ children: [] }),
    // Company info
    new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: "Technijian Corporation", font: "Arial", size: 22, color: DARK, bold: true })] }),
    new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: "18 Technology Drive, Suite 141, Irvine, CA 92618", font: "Arial", size: 20, color: GRAY })] }),
    new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: "949-379-8499  |  www.technijian.com", font: "Arial", size: 20, color: GRAY })] }),
    new Paragraph({ children: [] }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200 },
      children: [new TextRun({ text: "Document Owner: Ravi Jain - CEO/Owner", font: "Arial", size: 20, color: GRAY })] }),
    new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: "Approved By: Ravi Jain - CEO/Owner", font: "Arial", size: 20, color: GRAY })] }),
    new Paragraph({ alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: "Next Review Date: March 6, 2027", font: "Arial", size: 20, color: GRAY })] }),
  ];
}

// === MAIN ===
async function main() {
  const md = fs.readFileSync(inputFile, 'utf8');
  const elements = parseMarkdown(md);
  const { children, numListCount } = buildContent(elements);
  const coverChildren = buildCoverPage(docTitle, docVersion, docDate);

  // Build numbering configs
  const numberingConfig = [
    { reference: "bullets", levels: [
      { level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 720, hanging: 360 } } } },
      { level: 1, format: LevelFormat.BULLET, text: "\u25E6", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 1440, hanging: 360 } } } },
      { level: 2, format: LevelFormat.BULLET, text: "\u25AA", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 2160, hanging: 360 } } } },
    ]},
    ...Array.from({ length: Math.max(numListCount, 1) }, (_, idx) => ({
      reference: `num_${idx}`,
      levels: [
        { level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } },
        { level: 1, format: LevelFormat.LOWER_LETTER, text: "%2.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 1440, hanging: 360 } } } },
      ]
    }))
  ];

  // Header
  const headerPara = new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 1, color: BLUE } },
    spacing: { after: 100 },
    tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_WIDTH }],
    children: [
      new ImageRun({
        type: "jpg", data: headerLogoData,
        transformation: { width: 130, height: 32 },
        altText: { title: "Technijian", description: "Technijian Logo", name: "hdr-logo" }
      }),
      new TextRun({ text: "\t", font: "Arial", size: 16 }),
      new TextRun({ text: docTitle, font: "Arial", size: 16, color: GRAY, italics: true }),
    ]
  });

  // Footer
  const footerPara = new Paragraph({
    border: { top: { style: BorderStyle.SINGLE, size: 1, color: BLUE } },
    spacing: { before: 100 },
    tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_WIDTH }],
    children: [
      new TextRun({ text: "Confidential", font: "Arial", size: 16, color: ORANGE, italics: true }),
      new TextRun({ text: "\t", font: "Arial", size: 16 }),
      new TextRun({ text: "Page ", font: "Arial", size: 16, color: GRAY }),
      new TextRun({ children: [PageNumber.CURRENT], font: "Arial", size: 16, color: GRAY }),
    ]
  });

  const doc = new Document({
    styles: {
      default: { document: { run: { font: "Arial", size: 22 } } },
      paragraphStyles: [
        { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: 32, bold: true, font: "Arial", color: BLUE },
          paragraph: { spacing: { before: 360, after: 240 }, outlineLevel: 0 } },
        { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: 26, bold: true, font: "Arial", color: BLUE },
          paragraph: { spacing: { before: 300, after: 200 }, outlineLevel: 1 } },
        { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
          run: { size: 24, bold: true, font: "Arial", color: DARK },
          paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 2 } },
      ]
    },
    numbering: { config: numberingConfig },
    sections: [
      {
        properties: {
          page: {
            size: { width: PAGE_WIDTH, height: PAGE_HEIGHT },
            margin: { top: MARGIN, right: MARGIN, bottom: MARGIN, left: MARGIN }
          }
        },
        children: coverChildren
      },
      {
        properties: {
          page: {
            size: { width: PAGE_WIDTH, height: PAGE_HEIGHT },
            margin: { top: 1800, right: MARGIN, bottom: 1440, left: MARGIN }
          }
        },
        headers: { default: new Header({ children: [headerPara] }) },
        footers: { default: new Footer({ children: [footerPara] }) },
        children
      }
    ]
  });

  const buffer = await Packer.toBuffer(doc);
  fs.writeFileSync(outputFile, buffer);
  console.log(`Created: ${outputFile} (${(buffer.length / 1024).toFixed(0)} KB)`);
}

main().catch(err => { console.error(err); process.exit(1); });
