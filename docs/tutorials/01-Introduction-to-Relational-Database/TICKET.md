# TICKET: Relational Database Basics — Learning Checklist

[Tutorial](https://github.com/easyscale-academy/learn_relational_database_basic_in_sqlite-project/tree/01-Introduction-to-Relational-Database/)

## Objective

Track your progress through the relational database module (branch `01-Introduction-to-Relational-Database`). Work through each section in order. Check items off as you go.

## Checklist

### Setup
- [X] Clone the repo and switch to the `01-Introduction-to-Relational-Database` branch
- [X] Run `mise install && mise run inst`
- [X] Read `examples/01-crud-two-styles/README.md` first — it explains why the project has two parallel script series
- [X] Verify the s1x raw-SQL series runs: `uv run python examples/01-crud-two-styles/s11_create_table.py` through `s15`
- [X] Verify the s2x Core Expression series runs: `uv run python examples/01-crud-two-styles/s21_create_table.py` through `s25`

### Absorb (learn the content)
- [X] Run `/learn-this-project-absorb` in Orient mode for the high-level map + the read-vs-run classification
- [X] Run every script on the run-list yourself, read the SQL output and ASCII tables
- [X] Come back to `/learn-this-project-absorb` in Context-dive mode whenever a specific spot needs unpacking
- [X] Understand why raw SQL (s1x) is taught before Core (s2x), and why neither uses the ORM
- [X] Understand `engine.begin()` vs `engine.connect()` (writes vs reads)
- [X] Understand why each script redefines the schema (`:memory:` is per-process + deliberate pedagogical repetition)
- [X] Understand the `:name` bound-parameter form in s1x and how it relates to the automatic binding in s2x's Core expressions

### Quiz (verify understanding)
- [ ] Run `/learn-this-project-quiz`, complete at least one full round
- [ ] Score 80%+ on a 10-question random round
- [ ] Review and re-study any topics where you scored poorly

### Elevate (see what's beyond)
- [ ] Run `/learn-this-project-elevate`, explore at least 1-2 directions
- [ ] Converge at least one direction into a concrete starter deliverable (e.g. "add `tests/test_examples.py` that smoke-tests both series")
- [ ] Optional but recommended: hand the deliverable back to `/learn-this-project-absorb` in **Build mode** and actually build the first iteration
- [ ] Note down "next small projects" that interest you

### Interview (pressure-test yourself)
- [ ] Run `/learn-this-project-interview`, complete a full mock session
- [ ] Review the debrief, note which questions need more prep

### Demo (learn to present)
- [ ] Run `/learn-this-project-demo`, rehearse at least the 5-minute version
- [ ] Walk through the "do NOT show" checklist

### Mastery Gate
- [ ] You can explain **at least 70%** of the knowledge points from the quiz bank
- [ ] You can answer interview-style questions with a concept and a direction (even if not perfect)
- [ ] You have a clear list of "what I'd study next" from the elevate session

### Publish (turn it into a portfolio piece)
- [ ] Decide a new public repo name (pattern: `<firstname>-<lastname>-relational-database-basic-poc`)
- [ ] Run `/learn-this-project-publish` in **Transform mode** — it will:
  - [ ] Ask for the new repo name + your name (Step 1)
  - [ ] Delete cardinal-rule teaching artifacts (`docs/learn-this-project/`, `README-cn.md`, the five teaching skills) — `learn-this-project-meta/` is kept as a portfolio bonus
  - [ ] Ask about borderline files (scratch / tmp / drafts) — your call on each
  - [ ] Generate `tmp/publish-commit-plan.md` — your copy-paste cheat-sheet for the git commands
  - [ ] Co-write your `README.md` in English in your own voice (D-mode — it asks, you answer, it drafts, you edit)
- [ ] Run `/learn-this-project-publish` in **Audit mode** (or wait for Transform to auto-run it) — confirm **zero 🔴 HIGH RISK findings** before publishing
- [ ] Create the public GitHub repo yourself (skill won't do this)
- [ ] Open `tmp/publish-commit-plan.md` and run the 10–15+ commits one by one (skill never touches git — you do)
- [ ] `git remote add origin <github-url>` and `git push -u origin main`
