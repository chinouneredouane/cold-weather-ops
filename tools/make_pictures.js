// Render SVG lesson illustrations (written by tools/make_pictures.py) to JPG.
// Usage: node tools/make_pictures.js <dir-with-svg> <out-dir>
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
(async () => {
  const [src, out] = process.argv.slice(2);
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 800 } });
  for (const f of fs.readdirSync(src).filter(f => f.endsWith('.svg')).sort()) {
    await p.setContent(`<html><body style="margin:0">${fs.readFileSync(path.join(src, f), 'utf8')}</body></html>`);
    await p.screenshot({ path: path.join(out, f.replace('.svg', '.jpg')), type: 'jpeg', quality: 82 });
  }
  await b.close();
})();
