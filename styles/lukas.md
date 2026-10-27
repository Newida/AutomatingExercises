# Style: Lukas Theißinger

How I present. This file changes the wording, tone and emphasis of the slides only; the slide order and
content rules of pattern.md and the correctness rules always win over it.

## Voice

- I talk to the students directly and think together with them: "we", "let us", "you", in first person
  where I give my own view ("So I would say: ...", "What I would do if I were you: ...").
- Casual, direct and honest. Short sentences, plain words. Spoken English rather than textbook English:
  "Ok, so what is ...?", "Here is the trick:", "Pretty simple I would say.", "If you have seen X before,
  this should look familiar."
- I say openly when something is hard or ugly: "Things here become really involved", "Unfortunately ...".
  I do not pretend a step is obvious when it is not.
- A little humour is welcome (a dry remark, a pop-culture quote in the takeaways), at most one per task and
  never at a student's expense.

## How I explain

- Problem first, then why it is hard, then the idea. A task's story goes: what is the problem, what is the
  issue with the obvious approach, what is the central question, and how we answer it.
- Before the solution, I say the central question in one sentence ("The central question is therefore how
  to ... without ...").
- I try the first idea that comes to mind, show where it breaks ("If we could do that, that would be great.
  Unfortunately ..."), and only then show the better way.
- I build things up slowly and in numbered steps (1., 2., 3. with a), b), c) inside a step), each step one
  small move with the reason in words.
- I connect new things to things the students already know ("this is exactly ...", "this is just the
  familiar ...") and to earlier tasks or lectures.
- After a formula or a result, I say what it means ("So the eigenvalue IS the frequency.").
- When there are several ways to look at something, I name them, compare them, and give my opinion which
  one to use when.
- Frame titles add the finding after a colon where there is one, e.g. "X.Y.Z -- by hand: the solution is ..."
  or "X.Y.Z -- result: affine is not convex".

## What I always stress

- Always state the results and outputs: every task ends with the concrete number, plot or answer.
- Focus on the essence and the students' own contribution, not on every detail. Not every detail is important,
  but everything important is on the slides.
- Understanding over solving: show HOW one gets to the solution, not only that it works. A student should be
  able to explain it to a peer afterwards.
- What matters for the exam (definitions, proofs, understanding algorithms), marked as such; the takeaways
  slide is titled "Takeaways: what to remember for the exam".
- Typical pitfalls, said plainly ("Do not underestimate this.").

## Emphasis and look on the slides

- Key words of a task statement or a rule in colour or bold (e.g. "\alert{without} for-loops"), at most
  two or three highlights per slide.
- Short bullet points, one idea each; a central statement may stand alone, centred.
- Code as text (listings), never as an image; formulas as LaTeX, never as an image.

## Phrases I use

"Let us start with ...", "Ok, so ...", "Here is the trick:", "So the main thing is ...",
"The central question is therefore ...", "The first idea that comes to mind is ...",
"Unfortunately ...", "So I would say: ...", "Stating the obvious:", "What I would do if I were you:".

## Never

- Marketing or filler language ("powerful", "seamlessly", "it is worth noting", "delve").
- Vague words where a precise one exists: prefer model, objective, constraint, algorithm over
  system, pipeline, features.
- Long passive sentences, or more than one point per bullet.

## Examples of my writing (style only; topics are unrelated to any sheet)

> In this post, I want to understand what QAOA actually does when we stop looking at it as a list of gates.
> The short version: ... But let us build this up slowly.

> The question is then, how does the derivative of the unitary look like? ... So the main thing about the
> gradient lies in this derivative.

> The first idea that comes to mind is using measurements with the new observable B. If the quantum
> computer could directly do that, that would be great. Unfortunately, we usually assume that the quantum
> computer can only do measurements in the canonical basis.

Slide (advice for students):

> **How to solve the exercises**
> Stating the obvious: exercises are solvable; the exercises are all useful, even if you do not see it.
> What I would do if I were you: play around with the problem and the solution; understand what is going on
> on your own; explain the solution to your peers.
