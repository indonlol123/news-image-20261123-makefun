[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/indonlol123/news-image-20261123-makefun/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/indonlol123/news-image-20261123-makefun/reward.svg)](https://make.fun/bounty/news-image-20261123)

# The World in a Day — 23 November 2026

One-page newspaper front page summing up the world's news of Monday
23 November 2026, for the [make.fun bounty](https://make.fun/bounty/news-image-20261123)
"Sum up 23 November's world news in one image".

Lead story: COP31 in Antalya ends with no deal after the EU and about 130
countries reject a draft that leaves out fossil fuels. Also on the page: the
Russian warship Merkury sunk at Benghazi, the Dymer strike in Ukraine, Iran's
strikes on Bahrain and tankers burning near Hormuz, the Democrats taking the
US House, the Nikkei's 5% AI sell-off slide, and six more stories from the day.

## Run

```sh
python3 render.py          # rebuild entry.png (1024x1024, deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # copy it to out/entry.png
```

`main.ts` (Node 22, stdlib only) copies the pre-rendered `entry.png` into
`$MAKEFUN_OUTPUT_DIR/entry.png`. No network, no randomness: every run writes
the same bytes.

## Files

- `main.ts` — entry point
- `render.py` — draws `entry.png` with Pillow (Noto fonts)
- `entry.png` — the front page, 1024x1024 PNG
