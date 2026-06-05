# How to Crush a Small Learning Repo (Using Relational Databases as the Excuse)

> Read this README slowly. It is long on purpose — the methodology here is the actual product of the course, and you will use it again on dozens of repos after this one.

## Part 1 — The Real Subject of This Course

### This isn't a relational-database tutorial

Let me set the tone right up front: **this course is not about relational databases**. The SQL is a vehicle — small enough that even someone with zero CS background can keep up (provided they've finished the earlier "learn with AI" prerequisite course), rich enough to put a complete learning methodology through its paces. What you are actually here to learn is **a repeatable, AI-assisted method for taking any small skill-sized repository and absorbing it completely**.

That distinction matters. If you walk away from this course remembering "`select(users_table).where(...)`", you got 10% of the value. If you walk away with a six-move playbook that you can run on the *next* small repo (a queue library, an auth library, an embedding model client, a new framework, a vertical-domain mini-project), you got the other 90%.

### Project work vs skill-sized projects

You will encounter two flavors of work in your career:

- **Project work** — building something real. A backend, a dashboard, a data pipeline, a feature. Complicated, multi-month, the deliverable is a whole system, and the project is composed of dozens of smaller sub-problems.
- **Skill-sized projects** — when you're knee-deep in real project work and you hit a sub-problem you don't fully understand (a new ORM, a queueing library, a particular auth flow), the move is to *peel that piece off*, build the smallest standalone repo that demonstrates exactly that one thing, and learn it in isolation before you wire it back into the big system.

The course you are reading right now is a worked example of the **second** flavor. The actual deliverable is the playbook for that move. Relational databases are just the topic that this particular small project happens to teach.

### Why this matters: there will be hundreds of these

Here is the part most students under-appreciate when they first start: **the next few years of your career will produce a long stream of skill-sized projects**. Every new framework, every new database, every new SDK, every new vertical-domain technique (a particular kind of LLM evaluation, a particular kind of statistics, a particular kind of UI pattern) deserves its own small-repo treatment.

If each one takes you a week of unstructured tutorial-following + Stack-Overflow-googling + "I think I get it" hand-waving, you will be slow. If each one takes you **two focused days** running the same six-move playbook, you will be fast. Multiply that across a career and the gap is enormous.

The whole point of building the *first* one of these (this one, on relational databases) carefully is so that you internalize the moves. The next one will go faster. The tenth one will feel automatic. **That automaticity is the actual skill.**

### The six-move playbook (one-line summary; we'll expand each below)

- **Absorb** — Everything the repo *contains*. Not just what it does — also *why* it's done that way. **Act first, then understand *how* it works, then understand *why*.**
- **Quiz** — Drilling that separates "I think I get it" from "I actually get it." A *lower-bound* guarantee, plus a Q&A pattern you can extend.
- **Elevate** — Everything the repo *doesn't* contain but probably should. Plus the prerequisite knowledge you'd need to add it.
- **Interview** — Mock-interview pressure on the whole project, with pushback on every answer.
- **Demo** — How to *present* the project to other humans — and what *not* to show.
- **Publish** — Turn this absorbed-and-rehearsed repo into a clean public portfolio piece on your own GitHub. The skill deletes teaching artifacts, generates a commit cheat-sheet, and co-writes your README — so the published result reads as *your* project, not a tutorial copy.

The rest of this README explains each move, the order to run them in, and — most importantly — how to use them as tools rather than as scripts to follow blindly.


## Part 2 — What's in This Repo (the concrete example)

The teaching content lives in `examples/` as **two parallel five-script series**, plus a shared utility and an on-ramp README:

```
examples/
├── README.md                 # background: why scripts, why SQLite, why SQLAlchemy,
│                               and the reading order (read this first)
├── s11_create_table.py       # raw SQL via text(): CREATE TABLE
├── s12_insert_data.py        # raw SQL: INSERT (single + executemany, :name binding)
├── s13_select_data.py        # raw SQL: SELECT (all / cols / WHERE / ORDER / consumption)
├── s14_update_data.py        # raw SQL: UPDATE (PK / multi-row / age = age + 1)
├── s15_delete_data.py        # raw SQL: DELETE (PK / WHERE / all + DELETE-vs-DROP)
├── s21_create_table.py       # Core Expression: same lessons, MetaData + Table
├── s22_insert_data.py        # Core: insert(t).values(...) + executemany
├── s23_select_data.py        # Core: select(t).where(...).order_by(...).limit(...)
├── s24_update_data.py        # Core: update(t).where(...).values(...)
├── s25_delete_data.py        # Core: delete(t).where(...)
└── utils.py                  # print_table — shared ASCII renderer for both series
```

Stack: Python 3.12 + SQLAlchemy 2.0 (raw SQL via `text(...)` first, then Core Expression — **deliberately not the ORM**) + SQLite in-memory. Under ~1000 lines of code. Every script is heavily commented and runs end-to-end with one command.

The codebase is **deliberately small**. If it were 50 files of business logic, you would spend the whole course learning the codebase and miss the playbook. The methodology has to outweigh the content.


## Part 3 — The Six Core Actions (the heart of the course)

Each of the six actions is exposed as a Claude Code slash command — a `/learn-this-project-<name>` skill that loads a small set of instructions and walks you through an interactive session. **Important: these are not chatbots and they are not documents-with-buttons. Think of each one as a specific *coaching mode* that an expert mentor of this project might enter when you ask them a particular kind of question.**

We'll go through each in detail. The order matters — read all six before you run any of them, so you have a mental model of how they fit together.

### 1. `/learn-this-project-absorb` — Absorb

> The premise: *the project's original author (your mentor) has written down everything you need to know about this repo as a set of analysis documents under `docs/learn-this-project/`. The AI has indexed those documents. The Absorb skill walks you, step by step, through what the mentor has prepared, in an order that makes sense.*

The conceptual move here is straightforward: **first you do, then you understand HOW it works, then you understand WHY it works**. In that order.

- **Do (act)** — You run the scripts. You watch the output. You don't try to understand anything yet; you just want to *see what happens when you run this code*. This step is non-creative on purpose. You are not innovating. You are just walking through what's there.
- **How** — Now you go back to each script with the AI and trace what each line does mechanically. What does `engine.begin()` actually return? What does `inspect(engine)` look at? What does `text(...)` wrap? The how-question is answered by reading the code together with the AI as your guide.
- **Why** — Once you can describe *what* the code does, you ask *why it's written that way and not another way*. Why raw SQL first, then Core? Why `:memory:` instead of a file? Why is the schema redefined in every script? This is the layer where you stop being a copy-paster and start being someone who can *make design decisions of their own*.

Absorb is the **first** skill to invoke on a fresh repo. Always. But — and this is the part people miss — **absorb is not a thing you sit through end-to-end with the AI dragging you along**. We'll talk about how to *actually* use it in Part 6 (Recommended Path). For now: it gives you the high-level map and the why-questions to come back to.

### 2. `/learn-this-project-quiz` — Quiz

The mentor has pre-written a question bank — roughly 30–60 carefully-shaped questions covering the parts of the repo a serious learner is expected to internalize. The Quiz skill fires these questions at you one at a time, you answer in your own words, and you get scored against the model answer.

**Quiz is a lower-bound guarantee, not an upper-bound test.** If you answer every quiz question correctly, you have demonstrated that you cleared a floor — you know everything the mentor thinks every learner should know about this repo. But it cannot certify that you have *mastered* the repo; mastery extends beyond what any pre-written bank can probe. So treat the quiz score as "did I clear the floor?", not "am I a 10/10 on this topic?".

There is a second, less-obvious use of the Quiz skill that most students miss: **the Quiz skill is also a Q&A interaction pattern**. Once you've drained the pre-written bank, you can ask the skill to *generate new questions* on a topic of your choosing — "give me five harder questions just about bound parameters", "quiz me on the differences between `lastrowid` and `inserted_primary_key`", and so on. The skill defines a question-and-answer behavior; the question source can be the bank or it can be you driving the agenda. That second mode is where Quiz becomes a thinking tool instead of a memorization tool.

### 3. `/learn-this-project-elevate` — Elevate

Absorb tells you what the repo *contains*. Elevate tells you what the repo *doesn't* contain but probably should — and what you'd need to learn in order to add those things.

For this particular repo, the elevation roadmap covers things like: a real test suite that smoke-tests both script series, a third script series teaching the ORM (`s31`–`s35`), a multi-table example with foreign keys to introduce JOINs, a logging layer instead of `echo=True`, and so on. Each upgrade area is documented with (a) current state, (b) what a senior-engineer version would look like, (c) alternative approaches and their tradeoffs, and (d) the prerequisite knowledge you'd need to do the upgrade well.

The conceptual move: **conceptual understanding alone is not enough**. If you elevate something purely as a discussion ("yeah I'd add tests, here's roughly how"), you absorb maybe 30% of it. If you elevate something *and then actually build it on top of this repo*, you absorb 90%. So the Elevate skill pairs naturally with Absorb in a feedback loop:

1. Use **Elevate** to identify an upgrade direction you care about, understand what good looks like, and learn the prerequisite knowledge.
2. Pick one of those upgrade goals as a concrete deliverable ("I'll add a tests directory that smoke-tests each script and assert the headers appear").
3. **Switch back to Absorb** with that goal. Tell it: "given this elevation goal, walk me through the parts of the existing code I need to touch, and help me build it on top of the existing structure." Now Absorb is helping you *do* the elevation, not just understand it.

This Elevate-then-Absorb loop is the fastest way to grow a new skill from this repo — much faster than just reading more tutorials.

### 4. `/learn-this-project-interview` — Interview

Quiz uses a fixed template: a specific question, a specific answer, scored against a specific rubric. Useful, but bounded.

Interview is more open-ended. **You treat the whole project as if it were your own work**, and the skill plays the role of a sharp interviewer probing your understanding under pressure. Five rounds — what you have / what you'd elevate / alternatives considered / problems you've hit / production-grade pushbacks — and every answer gets pushback at least once. No mid-question coaching; all feedback held until a debrief at the end.

Use Interview when you genuinely want to find out whether you understand the project at the level needed to *defend it to a stranger* — for example, before putting this on a résumé, before a real interview where you'll discuss it, or just to see whether you can survive scrutiny on a topic. It's where surface-level knowledge gets caught.

### 5. `/learn-this-project-demo` — Demo

This is the one most students under-use, and it's actually the one that has the most career leverage.

Here's the situation Demo is designed for: in an interview, on a call, in a conversation with a peer, someone asks "*do you know X?*" where X is some skill. The strongest possible way to prove you know X is not "yes I do" plus a verbal description — it's **opening the project where you learned X and walking the other person through it live**.

That project is *this repo* (or, more generally, the next learn-this-project repo, and the one after that, and so on). The Demo skill teaches you how to *present this project effectively under different audience conditions* — how to pick the right entry point, how to sequence the wow moments, what to skip, what to absolutely not show. Many students have done good work but can't structure a presentation of it — the work is there, the framing isn't. Demo fixes the framing.

A consequential side-benefit: the Demo skill's "what NOT to show" list (placeholder READMEs, scratch directories, half-finished features) makes you brutally aware of the boundary between *what's presentable* and *what would make you look junior*. Running the demo skill once will tell you more about your own repo's hygiene than any code-review skim.

### 6. `/learn-this-project-publish` — Publish

This is the move that turns the rehearsed repo into an *external artifact*: a clean public repository on your own GitHub that reads as your own work. It's the long-term-leverage step of the playbook — every learn-this-project repo you complete becomes a portfolio piece, and the collection becomes evidence of a *systematic learning method*.

The skill has two modes. **Transform mode** walks you through the conversion in one session: it asks for your new repo name and your name (intake), deletes the cardinal teaching artifacts (`docs/learn-this-project/`, `README-cn.md`, the five generated sibling skills — but keeps `learn-this-project-meta/` as a portfolio bonus), asks about borderline files one by one, generates a dependency-ordered commit cheat-sheet to `tmp/publish-commit-plan.md`, and co-writes a personal English README in your own voice (D-mode — it asks questions, you answer, it drafts each section, you edit). **Audit mode** is a hostile scanner — assume an interviewer is looking for any sign that this came from a tutorial, and the skill flags every tell across files, README phrasing, commit messages, and git tags/branches.

Two important constraints worth knowing up front. **The skill never touches git** — you do every `git add` / `commit` / `push` yourself by copy-pasting from the cheat-sheet, so the resulting commit history is genuinely yours. **The skill never creates the GitHub repo** — that's your deliberate publication act. Everything else (file deletion, renames, the README, the audit) happens locally with the skill driving and you consenting at each step.


## Part 4 — Two Kinds of Knowledge (and where the skills sit)

Before you run any skill, you should understand *what the skills are actually doing* underneath. This is a brief framing — the next course in the series will go deeper.

There are **two kinds of knowledge** in any project like this:

1. **The work itself.** The code in `examples/`, the configuration in `pyproject.toml` and `mise.toml`, the data, the design choices, the artifacts that *are* the project. This is the part you came to learn. It's what you'd actually be doing if you were working on a problem.
2. **The mentor's notes about the work.** The analysis documents under `docs/learn-this-project/` — a component inventory, a runbook, an elevation roadmap, a quiz bank, an interview playbook, a demo playbook. These are *not* the project's content; they are the mentor's commentary on how to *teach* and *learn* the project. Treat them as an index.

The skills under `.claude/skills/learn-this-project-*/` read the mentor's notes first, consult the project's actual content based on what the notes point at, and then guide you through digesting it. The skills are **not the book you sit down and read cover to cover**. They are coaching modes that lean on the mentor's notes when you need help.

What this means in practice:

- **The skill is most valuable when you don't know what to do next.** If you've just cloned the repo and have no map, Absorb's overview is invaluable. If you've hit a wall while exploring some file, switching back to a skill lets it orient you. If you're about to demo, Demo gives you structure.
- **The skill is least valuable when you already know what you're doing.** When you're running scripts and reading code with purpose, you don't need a coaching mode — you need to be *doing the work*. Don't drag the AI into a chatty back-and-forth about every line; you'll learn slower.
- **The real main path is YOU doing the work, with the agent helping where helpful** — not "I open Absorb and follow it from beginning to end". We'll lay this out concretely in Part 6.

(The deeper version of "what the skill is doing" — including how the meta-skill generates these analysis docs in the first place, and how to build your own — is covered in a later course. For now this is the model you need.)


## Part 5 — Prerequisites and Setup

We assume you've finished:

1. **The Claude Code course** — you know how to invoke Claude Code slash commands and how to read its output.
2. **mise-en-place** — you've used `mise` to manage a dev environment at least once.

If either of those is shaky, finish that one first; the steps below will fight you otherwise.

> This course **runs entirely on your local machine**. No external database, no cloud account, nothing to register for. SQLite is in-memory — every script creates the database when it starts and discards it when it exits. **Zero cost, zero risk, zero cleanup.**

### One-time setup

From the repository root:

```bash
mise install               # installs Python 3.12 and uv at the versions mise.toml pins
mise run venv-create       # creates .venv/ (== uv venv)
mise run inst              # installs dependencies (== uv sync --all-extras)
```

That's it — you can now run any example script:

```bash
uv run python examples/s11_create_table.py
```

If something breaks, the recovery move is the same as the rest of the course: open Claude Code, run `/learn-this-project-absorb`, paste the error, and ask the AI to walk you through the fix.


## Part 6 — The Recommended Learning Path (read this carefully)

This is the most important section of this README. Most students misuse the six skills by treating each one as a single linear "open the skill, follow it end-to-end" session. That is not how to use them, and it produces shallow learning.

The right model: **the skills are an expert mentor who happens to know this repo cold. You use a mentor differently from how you use a textbook.** You ask the mentor for orientation when you're lost. You ask them for help on a specific problem when you're stuck. You don't dictate-and-record every sentence they say.

What follows is the *recommended sequence*, with explicit guidance on how to use each skill correctly.

### Step 1 — Absorb, three-stage style (this is more nuanced than it looks)

#### Stage 1A: get the overview

Open Claude Code, run `/learn-this-project-absorb`. Let it walk you through **just the high-level map**: what's in `examples/`, what's the two-series structure (s1x raw SQL, s2x Core), what `utils.py` does, what the empty `learn_this_project/` package is for. Don't dive into any one file yet. The goal of this stage is exactly one thing: **leave with a mental table-of-contents of the repo, and a clear sense of which files you need to *read* vs which files you need to *run***.

That last distinction is critical and the skill should help you draw it. In this repo:

- Files to *read*: the docstrings in each script, `examples/README.md`, `utils.py`. You're not running these to learn; you're reading them like prose.
- Files to *run*: the ten numbered scripts. You are not just reading them — you are typing `uv run python examples/sNN_*.py` and watching the output. Without that, you haven't learned them; you've only previewed them.

If the absorb session ends without you knowing which files fall into which bucket, you missed Stage 1A's point — ask the skill again.

#### Stage 1B: leave the skill, explore on your own

Close the Absorb chat. Open a **fresh** AI conversation (or no AI at all) and start *doing*. Read the files marked "read". Run the files marked "run". Stare at the output. Notice things. Form your own questions. **This stage is non-negotiable.** Without it you've outsourced the entire learning experience to the agent, and you'll have nothing in your head once the session window closes.

When you find yourself stopping at a specific spot — "wait, what does `result.lastrowid` actually do? why is it different from `inserted_primary_key`?" — that is the cue for Stage 1C.

#### Stage 1C: re-open the skill, with context

Now open `/learn-this-project-absorb` *again*. But this time, tell it **where you are and what you're doing**: "I'm in `s12_insert_data.py` around line 80, I'm trying to understand why `result.lastrowid` exists and how it relates to the Core counterpart in `s22`". The skill is now genuinely useful: you've given it a context, and it can deepen your understanding *of that context* rather than dragging you through the whole tour again.

A second use case for Stage 1C: **when you're stuck and don't know what to do next**. Open the skill and tell it "I just finished the SELECT lessons but I'm not sure what to focus on next — what would you suggest given that I'm trying to be ready to demo this in two weeks?". The skill can sequence the next step for you.

A third use case (and this is where it gets really powerful): **when you want to attempt something the curriculum doesn't cover** — adding a small extension, modifying a script to test a hypothesis, exploring a path the lessons don't take. The skill has the whole project map in mind; it can advise on which files to touch and what design choices to consider. Treat it as an omniscient project expert, not as a tutorial reader.

### Step 2 — Quiz, with two modes

After you've gone through at least the first few scripts in Stage 1B, run a Quiz round.

**Mode A: the pre-written bank.** Let the skill fire 5–10 random questions. Score yourself honestly — when you got something wrong, *the answer wasn't on the tip of your tongue, that's just you covering for yourself*. Errors here are gold; each one identifies a hole in your model that two minutes of going back to the relevant file will plug.

**Mode B: open-ended.** Once you've cleared the bank's floor, switch into open-ended mode by asking the skill directly: "generate five harder questions about bound parameters specifically, focused on the security implications". You're now using the skill's Q&A *behavior* with your own question source. This is where Quiz becomes a thinking tool.

Keep cycling between Stage 1 (absorb + explore) and Step 2 (quiz both modes) until you can answer the kind of question that doesn't appear in any bank but that you can imagine an experienced engineer asking — "where would this design break down if the table had 50 million rows?", "what does `engine.begin()` actually do if I raise inside it and catch the exception higher up?".

### Step 3 — Elevate (and the Elevate-Absorb loop)

When you can defend the repo as-is, run `/learn-this-project-elevate`. Pick one or two upgrade directions that actually interest you — not the longest list, not the most impressive-sounding, the ones that hook your curiosity. The skill will walk you through current state → senior target state → alternatives → prerequisite knowledge for each.

Then — and this is where most students stop — **do not stop**. Take one of the elevation directions as a concrete goal ("I want to add a minimal `tests/` directory that smoke-tests both script series") and switch back to Absorb with that goal in hand. Now Absorb's role changes from "explain the existing code" to "help me build something new on top of the existing code". This Elevate → Absorb loop is the single most valuable cycle in this course. Conceptual understanding is one tier; hands-on extension is two tiers above it.

You don't have to ship the elevation upgrade. The point is to *try* — to spend a day or two actually building a piece of it. That's where the muscle memory forms.

### Step 4 — Interview

Once you've done at least one elevation pass, run `/learn-this-project-interview`. This is the completeness check. The skill probes you across the whole project, with pushback. Take it seriously: when it asks "why not Postgres?" and you answer, expect a follow-up "but you said SQLite has dialect quirks — name one that would actually mislead a beginner". If you don't have an answer, you don't really understand the tradeoff yet. Go back, fix it, run interview again.

Use Interview as the test that decides whether you're ready to put this repo on a résumé or take it into a real conversation.

### Step 5 — Demo

Run `/learn-this-project-demo`, tell it the audience you're imagining (be specific — "a hiring manager for a data-engineering role at a small company"), and let the skill walk you through the recommended sequence + a forced pass through the "do NOT show" list. This last list is the one most people skip and most need; it's the difference between a polished demo and a demo that broadcasts "I am an intermediate engineer".

### Step 6 — Publish

If you want this repo to become a portfolio artifact you can point at in interviews (and you should), run `/learn-this-project-publish` in Transform mode. It walks the conversion top-to-bottom: deletes the teaching artifacts, generates a commit cheat-sheet, co-writes your README in English, and finishes with a hostile-scan audit. After it's done you'll have a clean local repo plus a commit cheat-sheet in `tmp/publish-commit-plan.md`; you create the public GitHub repo yourself, copy-paste the commits in order, and push.

Once you've done Publish on this repo, you have one full pass of the playbook under your belt — and a public artifact to show for it. The next repo will go faster, and the collection of these artifacts becomes a visible track record of your learning method.


## Part 7 — Show Your Work (the long-term play)

This section is the longest-term-leverage part of the course. Read it like you mean it.

### Why this matters

Every learn-this-project repo you complete becomes a *portfolio artifact*. Not the original tutorial repo we gave you — that one's a teaching artifact and shouldn't be your public-facing work. The artifact is **a fresh public repository of your own**, in which you carefully recreate the project's content piece by piece, committing as you go, so that your GitHub history reads as "I figured this out one step at a time".

There are three reasons this matters:

1. **In job interviews, when someone asks if you know a skill, the strongest possible answer is to open the project where you learned that skill and walk them through it.** A verbal "yes" plus a vague description is weak. A live walk-through of a clean, well-staged repo is overwhelming evidence.
2. **As you complete more learn-this-project repos across different skills, the collection becomes a knowledge map of you.** A relational-database POC, an LLM-evaluation POC, a queue-library POC, a particular-statistics POC. Looking at the collection, someone can see your growth trajectory and your range. That's much more compelling than a CV bullet list.
3. **You learn the *act of producing a presentable artifact*.** Many engineers do good work that they can't surface convincingly. The discipline of staging it for an external viewer — incremental commits, a hand-written README, no teaching artifacts left in — is itself a skill, and you build it by doing it repeatedly.

### The cardinal rule: don't be detected as a teaching project

Your audience must not be able to tell that this came from a tutorial. If they can, the demo's persuasive value goes from "this person learned a hard thing" to "this person ran a tutorial", which is a *negative* signal in an interview, not a positive one.

This means everything teaching-material-shaped must be removed from your public version:

- The teaching README files (`README.md`, `README-cn.md` — the one you're reading now).
- The mentor's analysis docs under `docs/learn-this-project/`.
- Any tutorial archive under `docs/tutorials/` if present.
- The five generated sibling skills under `.claude/skills/learn-this-project-{absorb,quiz,elevate,interview,demo}/`. (Keep `learn-this-project-meta/` — that's a portfolio bonus.)

The cleaner your repo looks like a *genuine first-person project*, the stronger the signal. The knowledge needs to live in your head, in your hand-written README, and in the way you walk a viewer through the code — not in artifacts that visibly point back to a course.

### Use the Publish skill — `/learn-this-project-publish`

The whole pipeline above is automated by the **`/learn-this-project-publish`** skill. Run it in Transform mode; it walks you through every step in sequence and stops to ask for consent at each destructive action. The mechanical details below explain *what the skill does* and *why it does each step that way* — read them once so you know what's happening, then let the skill drive.

If you've already converted your repo and want a second pair of eyes, run the same skill in **Audit mode** — it does a hostile scan looking for residual teaching tells (filenames, README phrasing, commit-message tone, residual `.claude/skills/learn-this-project-*` directories, suspicious git tags/branches).

### What the skill walks you through

#### 1. Intake — your new repo name and your name

The skill's first move is to ask for two things: the public repo name you'll create on GitHub (suggested pattern: `<firstname>-<lastname>-relational-database-basic-poc`) and your name for use in commit messages and an optional README byline. Both are required before any work begins.

#### 2. Delete cardinal teaching artifacts (skill does this, with your consent)

The skill lists every teaching artifact it found — exactly the items in the cardinal-rule list above — prints a dry-run preview, and on your yes runs `rm -rf` directly. You do not need to type `rm` yourself; the skill handles the mechanical deletion. **The skill keeps `.claude/skills/learn-this-project-meta/`** because that one represents a meta-skill you can legitimately apply to future projects — it's a portfolio bonus, not a tell.

#### 3. Borderline review (one question per file)

For files that *might* be teaching material but might also be your own work (scratch dirs, `tmp/`, `*.bak`, notes), the skill asks you one at a time: keep or delete? Your call on each.

#### 4. Generate a commit cheat-sheet to `tmp/publish-commit-plan.md`

The skill **does not run any `git` commands**. Instead it generates a numbered table of 10–15+ commits — dependency-ordered (least-dependent first), each with a file list, a suggested first-person commit message, and a one-sentence rationale. You copy-paste the commands from this file into your terminal yourself, so the resulting commit history is genuinely produced by your fingers, not by an automation.

The typical commit sequence for this repo looks like: root config (`mise.toml`, `pyproject.toml`, `.gitignore`) → empty package skeleton → shared utilities (`examples/utils.py`) → `examples/README.md` → each of `s11`–`s15` → each of `s21`–`s25` → your hand-written `README.md`. Resist the urge to combine scripts into one commit; each is its own piece of the lesson, and the resulting history is part of the signal.

#### 5. Co-write your README in your own voice (D-mode)

This is the only part of Publish where the skill has to be careful about authorship. It uses a **co-write loop**: ask 2–4 prompts about one section (e.g., "In one sentence, what is this project?", "What surprised you most?"), take your answers in your actual words, draft that section in prose that reflects your phrasing, and show you the draft to edit before locking it in. The skill does *not* invent insight you didn't supply — your words are the source. The final `README.md` is written to the repo root, in English, ~250–500 words total.

#### 6. Final hostile-scan audit

After the README is written, the skill switches into Audit mode automatically and scans the now-transformed repo against the full hostile-scan rule set (file patterns, README phrases, commit-message tone, git refs, residual directories, hygiene). Findings are grouped 🔴 HIGH RISK / 🟡 MEDIUM / 🔵 LOW. Transform is complete only when there are zero HIGH RISK findings — or when you explicitly accept the remaining flags.

After all six steps, the skill prints a final summary telling you what's left to do *outside* the skill: create the public GitHub repo, copy-paste the commits from the cheat-sheet, `git remote add origin <url>`, and `git push`.

### What "done" looks like

Your public repo should look like:

- 10–15+ incremental commits with personal-voice messages.
- A short README *you* co-wrote with the skill in your own voice.
- Zero teaching artifacts: no `README-cn.md`, no `docs/learn-this-project/`, no `.claude/skills/learn-this-project-{absorb,quiz,elevate,interview,demo}/`. (`learn-this-project-meta/` is fine and even encouraged.)
- A `mise.toml` + `pyproject.toml` that actually works (someone else can `mise install && mise run inst && uv run python examples/s11_create_table.py` and have it work).
- Code that you can walk through live — meaning you've actually read every line during Absorb, not just transcribed it.

That collective signal — "this person can break problems down, work through them step by step, and produce something at the end" — is the actual product of this course.


## Part 8 — Mentor's Note

> A note from your mentor — read this slowly. It matters more than any of the technical content.

**The thing you're really walking away with isn't SQL.** It's muscle memory for these six moves and the discipline to apply them as a system, not as separate scripts to follow blindly.

I picked relational databases for this course because the topic is simple enough not to drown you in framework specifics. That leaves attention free for the meta-question — *"why am I using this skill right now?"* — which is the actual lesson. Over the next few years you will inherit dozens of small repos, one per skill: a new ORM, a new queue, an auth library, an AI client, a particular evaluation methodology, a particular kind of statistical method. Every single one deserves this same six-move treatment. **Once the pattern is automatic, your rate of skill acquisition goes up by an order of magnitude.**

Most engineers learn new skills by reading a tutorial start-to-finish, building one toy thing, and jumping back into production work. Result: a Swiss-cheese mental model where they can't tell where the holes are. **Absorb + Quiz + Elevate + Interview + Demo + Publish plug those holes.** Absorb makes sure you don't miss anything. Quiz forces you to face what you missed. Elevate shows you the ceiling. Interview tests you against external pressure. Demo forces you to output — which is the ultimate test of understanding. Publish turns the absorbed work into a portable artifact you can carry into interviews, into demos, into the next role.

Three pieces of explicit guidance before you start:

**Be honest with yourself.** When the quiz tells you you got something wrong, you got it wrong — don't tell yourself "I knew that, I just phrased it badly". Every honest miss is a cheap upgrade opportunity, and the earlier you catch them the cheaper they are.

**Don't run a skill in isolation.** Absorb without Quiz is wishful thinking. Quiz without Elevate has no ceiling. Interview without Demo is shadowboxing. The five skills compound — running all five is much more than the sum of running each.

**Don't treat the skill as a script you follow.** Treat it as a mentor on call. Use it when you're lost. Use it when you're stuck. Use it when you want to attempt something the curriculum doesn't cover. The work of learning happens when *you* are running code and reading files — the skill is the helper, not the work.

The six-move playbook is a long-term investment. The course you're holding is the first repetition. There will be many more. Run this one carefully — slowly, even — and the next one will go faster.
