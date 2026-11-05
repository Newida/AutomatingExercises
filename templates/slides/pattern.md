The deck presents the sheet in this order:

1. The title slide names the exercise sheet, the problems covered and the course. There is no roadmap or agenda slide.
2. The refresher (only if the sheet assumes background students may lack) explains one concept per slide: first the setting, then the definition with its formula, then the key property in words, and finally a common misunderstanding.
3. Then comes each problem in sheet order: first its recap, then each of its tasks.
4. The last slide states the takeaways: one line per lesson of the sheet.

A problem's recap (before its tasks; everything comes from the sheet, nothing is solved yet):

1. The Given slide states what the problem starts from. The first line names the data: where it comes from and what one entry means. The next lines name the model and the formulas the sheet provides, each with its equation number. Then come the functions and results from earlier tasks that this problem builds on. If the sheet shows an image of the data or the setting, it appears next to this list.
2. The overview slide lists the problem's tasks in sheet order, one line each: its number, its short title, and what it asks for in a few words.

A task follows the sheet: first the background the sheet puts before it, then its solution. How the solution is presented depends on the task's type. Before writing a task's slides, decide which of the task types below it is and follow that type's pattern. If no type fits, use the default type "computation".

Background (for every type; only if the sheet puts background info between the previous task and this one; one slide per idea):
1. Each background slide starts with the question it answers (for example "why this model?"), then gives the sheet's reasoning in short steps, and ends with what this means for the task. Formulas keep the sheet's equation numbers. If the sheet shows an image with this background, it appears on this slide.

Every slide stands on its own (for every slide of the deck): a slide never refers to an equation, formula or result on another slide ("by (2) on the slide before", "see the formula above", "as shown in step 3 of the previous slide"). If a slide uses a formula that was shown on an earlier slide, it writes the formula out again on this slide, with the sheet's equation number if it has one, and then uses it. The same holds for definitions: a symbol that is used is defined again in one phrase if it was introduced on another slide. The sheet's equation numbers only label a formula that is shown on the slide itself; they never replace it.

## Task types

### Computation (the default)

The task asks to compute, derive, implement or show something.

What is asked:
1. The task slide restates the task faithfully in the sheet's notation: what must be computed, implemented or shown, with the given starting values, constraints and hints. If the task statement shows an image, it appears here. The last sentence says what the sheet warns about or expects to come out, if it does.

Step 1, by hand:
2. The first by-hand slide works through a toy version small enough to do on paper: it states the toy problem, does each step with the actual numbers, and ends with the subtle point the toy reveals ("Why ...?"). There is a toy slide only if the real data is too big to work through by hand or hides the point (for example 1.1.1: the effect sits in the 10th decimal place, a 3-digit toy shows it). If the steps can be shown on the given data directly (for example 1.2.1: the rule tables are small already), there is no toy slide; the real-data slide then also ends with the subtle point.
3. The second by-hand slide does the same steps on the real data: a table of the key numbers, then one or two sentences of sanity checks. For a math task, this is the full derivation in numbered steps, with every step explained in words.

Step 2, algorithm:
4. The algorithm slide gives the method as numbered steps in words, from input to output, and ends with the main pitfall.

Step 3, implementation:
5. The implementation slide shows the essential lines of code, the figure next to them if there is one, and one short note per non-obvious line. A pure math task shows the check by computer instead, if the solution has one.
6. The result slide states the final answer in a box, then lists the independent checks that show it is right.
7. If the task has a plot, a plot slide shows it full width with one or two sentences on what to look at.

Finally, if the sheet compares methods or results with an earlier task, a comparison slide puts them side by side in a table and ends with a one-sentence conclusion.

### Proof

The task asks to prove a statement (a theorem, an identity, an inequality) and nothing is implemented. There is only one step, by hand. There is no algorithm slide, no implementation slide, no code check and no separate result slide.

What is asked:
1. The task slide restates the statement faithfully in the sheet's notation: the assumptions, the claim and the sheet's equation numbers. If the sheet allows any proof technique, the last sentence names the technique chosen.

Step 1, by hand (the whole proof):
2. The by-hand slides give the proof in numbered steps, one idea per slide, at most five steps per slide. The slide titles are numbered "by hand (k/m)". Nothing is skipped: every formula and every calculation is written out, and every step gets one sentence in words that says what it does and why it holds. "Clearly", "similarly" and "and so on" are not allowed. Examples of what "written out" means: the system of $n$ equations is written down row by row from the sheet's formula, then in matrix form with its entries; what row $j$ of a matrix product says is written as its own equation; a list of $n$ conditions is shown as the list $p(x_1)=0,\dots,p(x_n)=0$, not as "for all $j$"; a repeated argument is carried out for the first two cases before it is stated for all.
3. The proof follows this order: first rewrite the statement in a form that can be attacked, then reduce it to what remains to show and state that in an alert line, then prove it, then conclude. Facts that the proof uses (for example "a nonzero polynomial of degree $\le n-1$ has at most $n-1$ roots") are named, and a fact is proved on the slide if its proof takes only a few lines.
4. The last by-hand slide states the conclusion in a box, ends the proof with $\square$, and says in one sentence where each assumption was used (the "trick").

### Question list

The task is only a list of questions (for example "think about the meaning behind all this" followed by bullet points), with no new computation, code or derivation asked for. A question may ask what one finds by hand or by computer; its answer then uses the results of the earlier tasks and the solution. There is no "what is asked" slide and there are no steps; the questions themselves are the slides, in sheet order:
1. A question slide first repeats the question as the sheet asks it, numbered in sheet order (or with the sheet's label, if it has one).
2. Then it gives the short answer: the answer itself in one sentence, then the one reason, formula, example or earlier result that supports it, at most three sentences in total.
3. The next question follows on the next slide, in the same way. Questions whose answer fits in one line may share a slide, at most three per slide.

"Think about" questions, mini exercises and overarching questions are tasks too: choose their type the same way.
