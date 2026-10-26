// Builds Direction "Modern" previews from the real app screens — screens themselves are never edited.
// For each screen: swap the stylesheet links to system + tokens-override + skin-modern, replace the inline
// icon sprite with Lucide paths (same ids), and set <html data-brand> for the variant.
// Usage: node build.mjs [screen ...]   (default: home counter)
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const screensDir = path.resolve(here, '../../../apps/app/screens');
const lucide = JSON.parse(fs.readFileSync(path.resolve(here, '../../assets/icons/lucide-map.json'), 'utf8'));
const screens = process.argv.slice(2).length ? process.argv.slice(2) : ['home', 'counter'];
const variants = { ocean: null, lime: 'lime' };

// preview/<variant>/<screen>.html → paths relative to that folder
const links = [
  '../../../../tokens.css',
  '../../../../components/components.css',
  '../../../../components/recipes.css',
  '../../../../../apps/app/app-tokens.css',
  '../../tokens-override.css',
  '../../skin-modern.css',
].map((h) => `<link rel="stylesheet" href="${h}">`).join('\n');

for (const [variant, brand] of Object.entries(variants)) {
  const out = path.join(here, 'preview', variant);
  fs.mkdirSync(out, { recursive: true });
  for (const name of screens) {
    let html = fs.readFileSync(path.join(screensDir, `${name}.html`), 'utf8');
    // 1. stylesheets: drop the original system/app links, insert the Modern stack in their place
    html = html.replace(/(?:<link rel="stylesheet" href="[^"]*(?:tokens|components|recipes|app-tokens)\.css">\s*)+/, links + '\n');
    // 2. icons: same ids, Lucide geometry
    let missing = [];
    html = html.replace(/<symbol id="([^"]+)" viewBox="[^"]*">[\s\S]*?<\/symbol>/g, (m, id) => {
      if (!lucide[id]) { missing.push(id); return m; }
      return `<symbol id="${id}" viewBox="0 0 24 24">${lucide[id]}</symbol>`;
    });
    // 3. variant + links between previews stay inside the preview folder
    if (brand) html = html.replace(/<html lang="vi"/, `<html lang="vi" data-brand="${brand}"`);
    // 4. assets referenced as ../../../system/… from screens/ live at ../../../../ from preview/<variant>/
    html = html.replaceAll('../../../system/', '../../../../');
    fs.writeFileSync(path.join(out, `${name}.html`), html);
    console.log(`${variant}/${name}.html${missing.length ? '  (kept original icons: ' + missing.join(', ') + ')' : ''}`);
  }
}
