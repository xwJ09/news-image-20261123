# news-image-20261123 — "The Day in Numbers: Scoreboard"

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/xwJ09/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/xwJ09/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Built for the make.fun bounty: https://make.fun/bounty/news-image-20261123

One image summing up the world news of **Monday 23 November 2026**,
drawn by `draw_image.py` (Pillow) as `entry.png`.

## The image

A scoreboard. A full-width gold hero band leads with the day's biggest
number — **31%**, Nvidia's jump as Jensen Huang returns as CEO — then a
3×2 grid of navy number-cards (7 drones sink a corvette, 17 years since
the last failed climate summit, 24 mourners lost at sea, 400+ drones
fired at Ukraine overnight, 60 banks facing a SWIFT cut-off, 429
Brussels flights cancelled), and a "MORE TODAY" ticker strip with seven
more stories. 14 stories in all. Navy + gold throughout.

## How to run

```sh
python3 draw_image.py        # renders entry.png (1024x1024, deterministic)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # copies it to out/entry.png
```

`main.ts` is standard-library only and copies the image; it needs no
network. Running `draw_image.py` twice writes byte-identical PNGs.

## Sources

CNN, Reuters, Al Jazeera, The Times, and the day's news recaps — every
number and event in the image was reported on 23 November 2026.

## License

MIT — see `LICENSE`.
