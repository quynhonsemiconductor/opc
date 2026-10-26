// Redesign (structure) build: src/<screen>.html → <screen>.html (Ocean) and calm/<screen>.html (Calm: + calm.css),
// with the Lucide sprite injected at <!--@icons-->. Only the icons a file uses are emitted. Usage: node build.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const icons = {
  ...JSON.parse(fs.readFileSync(path.resolve(here, '../../../assets/icons/lucide-map.json'), 'utf8')),
  ...JSON.parse(fs.readFileSync(path.join(here, 'icons-extra.json'), 'utf8')),
};
fs.mkdirSync(path.join(here, 'calm'), { recursive: true });

for (const f of fs.readdirSync(path.join(here, 'src')).filter((f) => f.endsWith('.html'))) {
  const html = fs.readFileSync(path.join(here, 'src', f), 'utf8');
  const used = [...new Set([...html.matchAll(/href="#(i-[\w-]+)"/g)].map((m) => m[1]))];
  const missing = used.filter((id) => !icons[id]);
  const sprite = '<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">\n' +
    used.filter((id) => icons[id]).map((id) => `  <symbol id="${id}" viewBox="0 0 24 24">${icons[id]}</symbol>`).join('\n') + '\n</svg>';
  const ocean = html.replace('<!--@icons-->', sprite);
  fs.writeFileSync(path.join(here, f), ocean);
  // calm/ is one level deeper: every relative stylesheet/asset path gains one "../"; calm.css loads last
  const calm = ocean
    .replace(/(href|src)="(\.\.\/[^"]*)"/g, '$1="../$2"')
    .replace('<link rel="stylesheet" href="redesign.css">', '<link rel="stylesheet" href="../redesign.css">\n<link rel="stylesheet" href="../calm.css">');
  fs.writeFileSync(path.join(here, 'calm', f), calm);
  console.log(f, `${used.length} icons`, missing.length ? `MISSING: ${missing.join(', ')}` : '');
}
