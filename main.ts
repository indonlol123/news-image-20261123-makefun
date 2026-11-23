// Entry point for the 23 November 2026 news image.
// Copies the pre-rendered front page (entry.png, built by render.py)
// into the grader's output directory. No network, no randomness:
// the same file is written on every run.
import { copyFileSync, mkdirSync, existsSync, statSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "out";

mkdirSync(outDir, { recursive: true });
const src = join(here, "entry.png");
if (!existsSync(src)) {
  throw new Error("entry.png is missing next to main.ts");
}
if (statSync(src).size > 1048576) {
  throw new Error("entry.png is over the 1 MiB limit");
}
copyFileSync(src, join(outDir, "entry.png"));
console.log("wrote entry.png to", outDir);
