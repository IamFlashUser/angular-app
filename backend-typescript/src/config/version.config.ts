import { readFileSync } from 'fs';
import { resolve } from 'path';

const env = process.env.NODE_ENV || 'development';

let versionInfo = {
  version: 'unknown',
  buildTime: 'unknown',
  env: env,
};

if (env === 'production') {
  try {
    const versionPath = resolve(__dirname, './version.json');
    versionInfo = JSON.parse(readFileSync(versionPath, 'utf-8'));
  } catch {
    console.error('❌ version.json introuvable en production.');
  }
} else {
  try {
    const projectRoot = resolve(__dirname, '../../');
    const pkg = JSON.parse(readFileSync(resolve(projectRoot, 'package.json'), 'utf-8'));

    versionInfo = {
      version: pkg.version || '0.0.0',
      buildTime: new Date().toISOString(),
      env: env,
    };
  } catch {
    console.error('❌ Impossible de lire la version en développement.');
  }
}

export { versionInfo };
