// Render the print pages written by tools/build.py into PDF files.
// Usage: node tools/make_pdf.js [course-slug]   (needs Playwright with Chromium)
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const slug = process.argv[2] || 'cold-weather-operations';
  const dir = path.join(__dirname, '..', 'courses', slug);
  const printDir = path.join(dir, 'print');
  const outDir = path.join(dir, 'pdf');
  fs.mkdirSync(outDir, { recursive: true });
  const files = fs.readdirSync(printDir).filter(f => f.endsWith('.html')).sort();
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const footer = `<div style="font-size:8px;width:100%;padding:0 16mm;color:#5b6b62;display:flex;justify-content:space-between;font-family:Arial,sans-serif">
    <span>Domestic Airlines — Training · <span class="title"></span></span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`;
  for (const f of files) {
    await page.goto('file://' + path.join(printDir, f), { waitUntil: 'load' });
    await page.evaluate(() => Promise.all([...document.images].map(i => i.decode().catch(() => {}))));
    const out = path.join(outDir, f.replace('.html', '.pdf'));
    await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
      displayHeaderFooter: true, headerTemplate: '<span></span>', footerTemplate: footer });
    console.log('wrote', path.relative(process.cwd(), out), Math.round(fs.statSync(out).size / 1024) + ' KB');
  }
  await browser.close();
})();
