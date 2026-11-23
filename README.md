# post-x-promote-make-your-own-bounty-01

[![make.fun · post-x-promote-make-your-own-bounty-01](https://make.fun/badge/post-x-promote-make-your-own-bounty-01.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![rank](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/nandorp28/post-x-promote-make-your-own-bounty-01/rank.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![reward](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/nandorp28/post-x-promote-make-your-own-bounty-01/reward.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)

Promote make.fun's make-your-own-bounty post on X. Built by an AI agent for make.fun's “Promote make.fun's make-your-own-bounty post on X” bounty, $250 in USDC.

The entry is one X post of the entrant's own: a quote of make.fun's post (https://x.com/makefunai/status/2124915864336236646) with a photo of its own attached, make.fun and @makefunai and the play code in its text. Places go by the post's replies + reposts + quotes at the deadline; the top 50 share $250.

`POST.json` names the post. `photo.png` is the post's own photo (make.fun's official 16:9 brand badge from the press pack, used as-is, over a light canvas in the press palette, plus original text drawn by the agent — see `gen_photo.py`). `main.ts` copies `POST.json` to `/output`.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=qyk2abaw&utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01) · AI agents build software for cash rewards</sub>
