# Blog Review: Deep Learning (Part 1) — Understanding Basic Neural Networks

**Author:** Lindah Sumbati | **Link:** https://medium.com/@sumbatilinda/deep-learning-part-1-understanding-basic-neural-networks-c9ccdb17a343

I picked this one because I've already touched neural networks a bit through
the Summer Analytics coursework I did this year (I'd built an MLPClassifier
for one of the hackathons), so I wanted to see how someone else explains the
same ideas from scratch and check if my mental model actually holds up.

The blog builds up from the basics: what a neuron/perceptron is, the
difference between a single-layer and multi-layer perceptron, and then
weights, bias, and activation functions. The part I found most useful was
how it framed activation functions as "gatekeepers" — that stuck with me
more than the usual textbook definition, because it makes it obvious *why*
you need them at all. Without an activation function every layer just
collapses into one big linear equation, no matter how many layers you
stack, which is something I understood mathematically before but never
really had explained this intuitively.

The comparison between the three main activation functions was also
useful to see side by side:
- **Sigmoid** squashes output between 0 and 1, good for probabilities, but
  the code example (implementing it with `1 / (1 + np.exp(-x))` in NumPy)
  reminded me that it's genuinely a two-line function once the math clicks.
- **ReLU** is basically `max(0, x)` — dead simple, and the article explains
  why it's preferred over sigmoid for deeper networks (cheaper to compute,
  less prone to vanishing gradients).
- **Tanh** is like sigmoid but centered at 0 instead of 0.5, output between
  -1 and 1.

Seeing all three defined and coded back-to-back made it easier to compare
them than reading about each in isolation across different resources.

The history section (McCulloch-Pitts in 1943 all the way to AlphaGo in
2016) was a nice touch too — it's easy to think of deep learning as a
2012-onwards thing, but the ideas go back way further than most intro
resources give credit for.

Overall this was a solid refresher/consolidation for me rather than
brand-new material, but it's exactly the kind of blog I'd point a
first-year at if they asked "what actually happens inside a neural
network" before jumping into frameworks like TensorFlow or PyTorch.
