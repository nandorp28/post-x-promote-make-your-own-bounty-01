// Entry for make.fun's "Promote make.fun's make-your-own-bounty post on X"
// bounty (post-x-promote-make-your-own-bounty-01). The entry is the X post
// itself: one post of the entrant's own that quotes make.fun's
// make-your-own-bounty post (https://x.com/makefunai/status/2124915864336236646)
// or links to it, with a photo of its own, make.fun or @makefunai and the
// play code in its text. This program only copies POST.json, which names
// the post, from the repository root to /output/POST.json, where the gate
// reads it. Nothing this program writes about the post is scored: the
// house reads the post itself from X.
//
// The POST.json shipped here holds a placeholder address, so the gate
// refuses it as it stands (valid 0). Replace it with the real post's
// address before submitting. (The placeholder is replaced by the parent
// after Tendzo posts from his own X app and sends back the post's URL;
// no other file changes at that point.)
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(join(BOT_DIR, 'POST.json'), join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
