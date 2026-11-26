# officeplacard
[![make.fun](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/konzlodon74-dot/officeplacard/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/konzlodon74-dot/officeplacard/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
Bounty: https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2

> Ceremonial stapler, c. 2019 CE. Painted steel and plastic. Recovered from the Ruins of Cubicle Row, Level 3; gift of the Facilities Department, 2024.

## How it works
`main.py` holds the placard in a `SENTENCE` constant and asserts it is non-blank, unpadded, single-line, and within the character limit. It then creates `/output` if needed and writes the sentence as UTF-8 bytes with no trailing newline to `/output/entry.txt`.

## Run
```bash
python3 main.py
```
