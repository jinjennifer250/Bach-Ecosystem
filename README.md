# Bach and the Ecosystem

A Computational Study of Pitch-Class Competition in Six Bach Works.

## The Question

Why does tonal music sound "natural"? Music theory tells us which intervals are consonant, but it does not explain why certain pitches become stable centers. This project asks: if the twelve pitch classes are treated as competing species in an ecosystem, do they converge to the tonic triad?

## The Method

Six Bach works were analyzed (BWV 861, 848, 855, 784, 772, 565). Each note was reduced to its pitch class. A 12×12 competition matrix was defined: consonant intervals promote growth, dissonant intervals suppress it. A 1000-generation simulation was run for each piece.

## The Finding

Four of six works converged to the tonic triad. Two works showed a different pattern: the tonic was displaced by the leading tone.

The ecosystem model captures a real feature of Bach's music: the tonic triad is the natural stable state of consonant pitch competition. But the exceptions reveal a boundary condition. Bach's music is anchored in ecological stability but not fully determined by it.

## Files

- `main.py` — the simulation code
- `Bach and the Ecosystem.pdf` — full research report
- `One Pager.pdf` — one-page summary
- `result_848.png`,`result_565.png`,`result_861.png`,`result_855.png`,`result_784.png`,`result_772.png` — simulation output charts
