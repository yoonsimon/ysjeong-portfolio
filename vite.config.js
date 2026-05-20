import { defineConfig } from 'vite';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import tailwindcss from '@tailwindcss/vite';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export default defineConfig({
  base: '/ysjeong-portfolio/',
  build: {
    outDir: 'dist',
  },
  plugins: [
    tailwindcss(),
    {
      name: 'copy-portfolio-and-targets',
      closeBundle() {
        // Copy portfolio.md
        if (fs.existsSync(path.resolve(__dirname, 'portfolio.md'))) {
          fs.copyFileSync(
            path.resolve(__dirname, 'portfolio.md'),
            path.resolve(__dirname, 'dist', 'portfolio.md')
          );
        }

        // Generate target-specific entry pages
        const distIndex = path.resolve(__dirname, 'dist', 'index.html');
        if (fs.existsSync(distIndex)) {
          const html = fs.readFileSync(distIndex, 'utf-8');
          const targets = ['oliveyoung', 'celimax'];
          for (const target of targets) {
            const targetDir = path.resolve(__dirname, 'dist', target);
            fs.mkdirSync(targetDir, { recursive: true });
            const targetHtml = html.replace(
              '<head>',
              `<head>\n  <meta name="portfolio-target" content="${target}">`
            );
            fs.writeFileSync(path.resolve(targetDir, 'index.html'), targetHtml);
          }
        }
      }
    }
  ]
});
