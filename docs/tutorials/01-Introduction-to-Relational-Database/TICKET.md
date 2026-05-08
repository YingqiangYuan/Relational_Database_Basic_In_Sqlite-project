# TICKET: Relational Database Basics — Learning Checklist

## Objective

Track your progress through the relational database module (branch `01-Introduction-to-Relational-Database`). Work through each section in order. Check items off as you go.

## Checklist

### Setup
- [ ] Clone the repo and switch to the `01-Introduction-to-Relational-Database` branch
- [ ] Run `mise install && mise run inst`
- [ ] Verify all five example scripts run: `uv run python examples/s01_create_table.py` through `s05`

### Absorb (learn the content)
- [ ] Run `/learn-this-project-absorb`, complete the full walkthrough
- [ ] Run each example script yourself, read the SQL output and ASCII tables
- [ ] Understand why SQLAlchemy Core instead of ORM (stays close to SQL, builds mental model first)
- [ ] Understand `engine.begin()` vs `engine.connect()` (writes vs reads)
- [ ] Understand why each script redefines the schema (`:memory:` is per-process + deliberate pedagogical repetition)

### Quiz (verify understanding)
- [ ] Run `/learn-this-project-quiz`, complete at least one full round
- [ ] Score 80%+ on a 10-question random round
- [ ] Review and re-study any topics where you scored poorly

### Elevate (see what's beyond)
- [ ] Run `/learn-this-project-elevate`, explore at least 1-2 directions
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

### Show Your Work
- [ ] Create your own public repo (renamed, no "learn" prefix)
- [ ] Commit incrementally (10-15+ commits)
- [ ] Delete all teaching artifacts (`docs/learn-this-project/`, `docs/tutorials/`, skills, `README-cn.md`, etc.)
- [ ] Keep `.claude/skills/learn-this-project-meta/` (it shows you learned to generate your own skills — bonus)
- [ ] Write your own README
