---
title: Thinking in Priors
parent: Tech
nav_order: 2
---

# Thinking in Priors

> Dummy note — replace with your own.

The Bayesian reframing that stuck with me: you never start from zero. You start
from a *prior*, and data nudges it. The interesting question is never "what does
the data say" but "how much should this data move me, given what I already
believed."

## A rough sketch

$$P(\theta \mid D) \propto P(D \mid \theta)\, P(\theta)$$

Note: math rendering needs MathJax, which isn't on by default in
just-the-docs — see the README if you want equations to render nicely.

## Where it bites

- Strong prior + weak data → you barely move. Usually correct, occasionally
  stubborn.
- Weak prior + strong data → you swing hard. Usually fine, occasionally
  overfit to noise.

The skill is calibrating which situation you're actually in.
