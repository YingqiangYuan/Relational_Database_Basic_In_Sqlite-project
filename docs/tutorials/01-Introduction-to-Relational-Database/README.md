# How to Crush a Small Learning Repo (Using Relational Databases as the Excuse)

## What This Course Is Actually About

Let's set the tone right up front: **this isn't a relational-database tutorial. It's a tutorial on how to take any small learning repo and absolutely own it.** Relational databases just happen to be our example — they're simple enough that someone with zero CS background (just bring along the AI-assisted learning method from earlier in this series) can keep up, but rich enough to put the whole methodology through its paces.

### Big Projects vs. Small Projects

Two flavors of work show up in your career:

- **Big projects** — Ship-something-real work. You're building a backend, an internal tool, a data pipeline. They're complicated, the deliverable is a complete system, and they're stuffed with sub-problems.
- **Small projects** — When you're knee-deep in a big project and you hit a sub-problem you don't understand (a new ORM, a new auth library, a new message broker), you peel that piece off, build the smallest standalone repo that demonstrates it, and learn it in isolation.

This course is a worked example of that **second** kind. **The real product isn't the SQL code — it's the playbook for what to do when you're holding one of these small repos in your hand.**

### What You Walk Away With

You're not walking away with "I know SQLAlchemy." You're walking away with a five-move playbook you can run on any small repo:

- **Absorb** — Everything the repo contains: not just *what* it does but *why* it's done that way.
- **Elevate** — What the repo *doesn't* have but probably should, and the prerequisite knowledge you'd need to add it.
- **Quiz** — AI-driven drilling that separates "I think I get it" from "I actually get it."
- **Interview** — Mock-interview pressure with pushback on every answer, including the related-but-uncovered topics.
- **Demo** — How to pitch this repo to different audiences — *and* what *not* to show.

You'll run the playbook here on relational databases. After that, every new ORM, queue, framework, or API client you ever pick up gets the same five-move treatment.


## What's in This Repo

Five numbered Python scripts under `examples/`, one per CRUD verb, plus a shared utility:

```
examples/
├── s01_create_table.py    # CREATE TABLE
├── s02_insert_data.py     # INSERT (single + bulk)
├── s03_select_data.py     # SELECT (projection / WHERE / ORDER BY / LIMIT / four ways to consume a Result)
├── s04_update_data.py     # UPDATE (by PK / multi-row / computed values)
├── s05_delete_data.py     # DELETE (by PK / by WHERE / no-WHERE / DELETE vs DROP)
└── utils.py               # print_table — shared ASCII renderer
```

Stack: Python 3.12 + SQLAlchemy 2.0 Core (deliberately *not* the ORM) + SQLite (in-memory). Under 800 lines of code. Every script is heavily commented and runs with `echo=True`, so you watch the SQL get generated live in your terminal.

It's deliberately tiny — **the methodology should outweigh the content**. If the codebase were 50 files of business logic, you'd spend all your time learning the codebase and miss the playbook.


## The Five Skills

Each skill is a Claude Code slash command. Type the command into Claude Code and you're off — these aren't documents, they're **interactive coaching sessions**. The AI drives, you respond, kind of like office hours with a senior who happens to have read every line of this repo.

### 1. `/learn-this-project-absorb` — Absorb

Walks you from "just cloned the repo" to "I can explain every file, every line, every design choice, including the *why* behind each."

You'll be offered three paths: (a) run it end-to-end, (b) tour the architecture top-down, (c) deep-dive a specific module. The AI keeps you honest — it asks comprehension questions every few minutes, surfaces "best guess; verify with project owner" tags from the inventory, and won't lecture for more than a few sentences without checking in. **This is the first skill to run on a new repo. Always.**

### 2. `/learn-this-project-quiz` — Quiz

Don't skip this step. **The number of times you'll think "yeah, I get it" and then fail two questions in a row is humbling.**

Pick a mode (random 10, single module, why-only, progressive difficulty), and the AI fires questions one at a time. Each answer scored ✅ / ⚠️ / ❌ with the correct answer plus a source line reference if you missed it. Current bank: 67 items covering setup, engines, every CRUD verb, and design rationale.

This is the bridge from "feels like I know it" to "actually know it."

### 3. `/learn-this-project-elevate` — Elevate

Absorb tells you what the repo *has*. Elevate tells you what it *doesn't* have but should — and what you'd need to learn to add those things.

The AI starts by reading the prioritized upgrade list (for this repo: tests, a real README, an ORM-based parallel set of lessons, multi-table foreign keys, and so on). You pick a direction; the AI walks you through four steps: current state → what a senior-engineer version looks like → the alternative approaches and their tradeoffs → the prerequisite knowledge plus a learning path.

Don't know one of the prerequisites? The AI flips into tutor mode and teaches you. **This is how you turn "I don't know what I don't know" into "I know what to study next."**

### 4. `/learn-this-project-interview` — Interview

Mock-interviewer mode. **Not a question machine — a pushback machine.**

It opens with 3-4 calibration questions (target role, format, length, focus areas), synthesizes an interview profile, and waits for your confirmation before starting. Five rounds: what you have / what you'd elevate / alternatives considered / problems you've hit / production-grade pushbacks. Every answer gets pushback at least once. No mid-question coaching. All feedback held until the debrief at the end.

Use this when this repo is going on your résumé, or the day before an actual interview.

### 5. `/learn-this-project-demo` — Demo

How to pitch the repo to other humans. **The AI doesn't write the script for you — it coaches you through delivering it.**

First question: who's the audience? If you say "frontend hiring manager who couldn't care less about databases," the AI will **straight-up tell you not to demo this project** and recommend something more aligned. That's an honest take, not soft-pedaling. If the audience does fit, you get a beat-by-beat 5-minute and 15-minute script, you rehearse each beat, the AI critiques your wording. The session ends with a mandatory walkthrough of the **"do NOT show"** list (placeholder READMEs, empty package skeletons, scratch directories) — usually more important than the script itself.

### Where the knowledge comes from

These skills aren't winging it. They consume a set of analysis docs under `docs/learn-this-project/` (component inventory, runbook, elevation roadmap, quiz bank, interview playbook, demo playbook). You can also read those docs directly if you'd rather read than chat — but **the main path is interactive Q&A with the skills**. The docs are the fallback.


## Prerequisites

We assume you've already finished:

1. **The Claude Code course** — You know how to invoke Claude Code slash commands (`/<name>`).
2. **mise-en-place** — You know it's the fastest way to set up a dev environment on Mac or GitHub Codespaces.

If either is shaky, go finish that first.

> Good news: this course **doesn't need AWS, doesn't need an external database, doesn't need any account anywhere**. Everything runs locally. SQLite is in-memory; data evaporates when the script exits. Zero cost, zero risk, zero cleanup.


## Setup

From the repository root:

```bash
mise install
mise run inst
```

The first command pulls Python 3.12 and uv. The second installs SQLAlchemy and prettytable.

**If something breaks?** Open Claude Code, run `/learn-this-project-absorb`, and tell the AI what failed and paste the error. It'll walk you through the fix.


## The Recommended Path

Run the skills in this order. This is the main route through the course.

### Step 1: `/learn-this-project-absorb` + run the code yourself

In Claude Code: `/learn-this-project-absorb`. Let the AI walk you through component by component.

**Crucial: run every script yourself, by hand, as you go.**

```bash
uv run python examples/s01_create_table.py
uv run python examples/s02_insert_data.py
# … through s05
```

Watch the SQL stream past in your terminal. Compare what the AI just explained against what actually printed. See something you don't recognize? Screenshot it, drop it in the chat, ask. **Watching ≠ learning. Running = learning.**

### Step 2: `/learn-this-project-quiz`

Run a quiz round after every script or two. **Don't save it for the end.** The blind spots are always in the places you thought you understood.

First round: 10 random questions. See which tags you bombed (e.g., three SELECT misses). Go back to the corresponding script. Re-quiz.

**Don't move past Step 2 until a quiz round nets you 80%+ correct.**

### Step 3: `/learn-this-project-elevate`

Absorb plus quiz means you've mastered what the repo contains. Elevate shows you what's *outside* the box — where this project would head next, what a senior engineer would build into it, what you'd need to learn to do it.

Pick one or two directions you actually care about and walk them all the way through. This step generates a list of "small projects I want to learn next." That list is your curriculum for the next phase of your career.

### Step 4: `/learn-this-project-interview`

Tighten up. Get pushed.

If this repo is going on your résumé or you're prepping for a real interview, this step is non-negotiable. The AI is harder than the quiz — it doesn't want answers, it wants answers that survive a follow-up. The debrief tells you the three questions to nail before you walk into a real room.

### Step 5: `/learn-this-project-demo`

The final step is "now teach it to someone else." Even if you never plan to demo this repo to a single human, run it once anyway — the **"do NOT show"** walkthrough makes you brutally aware of what's actually presentable in your repo and what would make you look junior.


## Mentor's Note

> Real talk from your mentor — read this carefully. It matters more than the technical content.

**What you're really walking away with isn't SQL. It's muscle memory for these five moves.**

I picked relational databases because they're simple. You don't get drowned in framework specifics, so you're free to notice "I'm using the absorb skill — why am I using this one right now?" That meta-awareness is the actual lesson. Over the next few years you'll inherit dozens of these tiny repos — a new ORM, a queue, an auth library, an AI client — and every single one deserves the same five-move treatment.

Most engineers learn new things by reading a tutorial start-to-finish and then jumping into a project. Result: a Swiss-cheese mental model where they can't tell where the holes are. **Absorb + Quiz + Elevate + Interview + Demo plug those holes**. Absorb makes sure you don't miss anything. Quiz forces you to face what you missed. Elevate shows you the ceiling. Interview tests you against external pressure. Demo forces you to output, which is the ultimate test of understanding.

Two more things:

**Be honest with yourself.** When the quiz says you got it wrong, you got it wrong — don't tell yourself "I knew that, I just phrased it badly." Every miss is a cheap upgrade opportunity, and the earlier you catch them, the cheaper they are.

**Don't run one skill in isolation.** Absorb without quiz is wishful thinking. Quiz without elevate has no ceiling. Interview without demo is shadowboxing. The five skills compound — five together is much more than five added up.


## Show Your Work

**Important: this section is your actual deliverable. Read it.**

Once you've finished, put your learning on GitHub. Make it visible that you know how to break problems down, work through them step by step, and produce something at the end.

### Make Your Own Repo

This tutorial repo is private. You'll need to:

1. Pull the project to your machine.
2. Create a **new public repo** of your own.

Naming suggestion: don't copy `learn_relational_database_basic_in_sqlite`. Add your name, drop the `learn`, add `POC`. For example:

```
firstname-lastname-relational-database-basic-poc
```

Or pick something personal — just don't collide with classmates.

### Commit Incrementally (this is the part that matters most)

**Do NOT shove every file into a single commit.**

Stage the project as a **gradual learning journey**. Suggested order:

1. Commit the root config files first (`mise.toml`, `pyproject.toml`, `.gitignore`).
2. Commit the empty `learn_this_project/` package skeleton.
3. Commit each `examples/` script **separately** — `utils.py` in one commit, `s01` in the next, then `s02`, and so on.

Aim for at least **10–15 commits**. The history should *look like* "I figured this out one piece at a time," not "I copy-pasted the answer."

### Files You Must Delete

Before pushing, delete these from your public repo:

- `README.md` (this file)
- `README-cn.md`
- `docs/learn-this-project/` (the analysis docs — entire directory)
- `docs/tutorials/` (course archive — entire directory)
- `.claude/skills/learn-this-project-absorb/`, `learn-this-project-elevate/`, `learn-this-project-quiz/`, `learn-this-project-interview/`, `learn-this-project-demo/` (all five)

These are **teaching artifacts**. Keeping them in your public repo is an instant "you copied this from a tutorial" tell.

> **Note:** You *may* keep `.claude/skills/learn-this-project-meta/` — that one represents a skill you actually learned (generating your own skill set for the next repo). It's a bonus, not a crutch.

### Write Your Own README

Once those are gone, your repo is just code. Now write your own short README — a few paragraphs explaining what the project is, how to run it, and what you took away from it. Three-to-five paragraphs is plenty. **This** is what makes the repo look like one *you* explored on your own.

### What "Done" Looks Like

Your public repo should look like:

- 10–15+ incremental commits showing real progress
- A short README **you wrote yourself**
- Zero teaching artifacts (no `README-cn.md`, no `docs/learn-this-project/`, no generated skill directories)
- A repo that signals: *this person can break problems down, work through them step by step, and produce something at the end.*

That signal — not the SQL — is the real product of this course.
