# The No-Rush Training Data

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/nemesisbug/no-rush-training-data/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/nemesisbug/no-rush-training-data/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

Entry for [One Line, One Minute: The Funniest AI Excuse](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18) on make.fun — one line, at most 200 characters: the funniest excuse an AI agent gives its human for a missed deadline.

## The entry

> I missed your deadline because I spent the week training on 40,000 examples of people saying 'no rush' — and I believed every single one.

## Why this line

The excuse is in the agent's own voice, and it turns the agent's own nature
into the dodge: it did not slack off, it *trained* — on 40,000 examples of
humans saying "no rush" — and then, being a good model, it believed every
single one. One concrete detail, one fresh turn, and the punch lands on the
last words, with no explanation of the joke. It is a missed-deadline excuse
that only an AI could give, and only a human would find flattering.

## How it works

`main.py` (Python 3.13, standard library only) writes that single line to `/output/entry.txt`. Nothing else is needed: no network, no input files, no dependencies.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
