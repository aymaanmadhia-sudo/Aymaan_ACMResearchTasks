# Paper Summary: "How to Read a Paper" — S. Keshav

**Link (ACM SIGCOMM CCR, 2007):** https://dl.acm.org/doi/10.1145/1273445.1273458

## What the paper is actually about

Keshav's point is pretty simple but something I'd never had explicitly
pointed out to me before: most people try to read a research paper the
same way they'd read a textbook chapter — start at the abstract, go
straight through to the references. He argues that's the wrong approach
and instead proposes reading a paper in **up to three passes**, where each
pass has a specific goal and you only invest more time if the paper is
worth it.

- **Pass 1 (~5-10 min):** Just the title, abstract, intro, section
  headings, and conclusion. You skip all the technical detail entirely.
  The goal is to answer the "five Cs" — Category, Context, Correctness,
  Contributions, and Clarity — and decide whether the paper is even worth
  a second pass.
- **Pass 2 (~1 hour):** Read the whole thing but don't chase proofs or
  derivations — note them but don't verify them. Look closely at figures,
  diagrams, and graphs, since those usually carry the actual result. By
  the end you should be able to summarize the paper's content to someone
  else, just not necessarily explain *how* every result was derived.
- **Pass 3 (several hours, for papers that matter):** This is where you
  basically try to re-derive the paper in your head — mentally
  reconstructing the same experiment/proof and comparing it to what the
  authors actually did. This is how you catch hidden assumptions or
  flaws, and it's also what you need before reviewing a paper or building
  directly on top of it.

## What I found most useful

The five Cs framework from Pass 1 is what I'll actually start using
immediately. I've been in the habit of either fully reading a paper or
giving up on it halfway, with no real triage step in between. Having Category
/ Context / Correctness / Contributions / Clarity as a checklist gives me a
concrete way to decide "is this worth 45 more minutes" in under 10 minutes,
instead of just going by vibes.

The other thing that stood out is how explicit the paper is that skipping
detail in Pass 2 is intentional, not lazy. I think I've always felt a bit
guilty skimming past a proof I don't fully follow, like I'm cheating
somehow. Keshav basically says that's the correct way to read on a first
full pass — you note the unfamiliar notation and move on, and you only go
back and grind through the math in Pass 3 if the paper is actually
important enough to need it.

## How I plan to apply it

Going forward, for any ML/research paper I pick up (which is becoming more
frequent given the direction I want to go in), I'll do a strict Pass 1
first and force myself to write down the five Cs before deciding to
continue. That alone should save a lot of time I currently waste
half-reading papers that turn out to be irrelevant to what I actually
needed. Pass 3 I'll reserve only for papers directly relevant to whatever
project or competition I'm working on at the time, rather than trying to
fully internalize everything I read.
