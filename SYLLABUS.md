# 16-Week Syllabus: Python + Cybersecurity in AI (true beginner)

**Time needed:** about 5 hours per week. **Goal:** finish with 5 portfolio projects and enough knowledge to interview for AI security, ML security, or security engineering roles.

**Big idea:** AI systems get hacked in two places. Most breaches happen in the **application around the model** (logins, APIs, secrets, data). Others happen in the **model itself** (fooling it, poisoning it, tricking it with prompts). You will learn both, in that order, because the first is easier and is where most real jobs are.

---

## How every week works (the same 5 steps)

1. **Read** the lesson (1 hour).
2. **Type** the code yourself, never copy-paste (1 hour).
3. **Break it** on purpose: change a number, delete a line, see what happens (30 min).
4. **Exercises + explain-it-back**: write 3 sentences in `NOTES.md` explaining the week's idea as if to a friend. If you can't, you haven't got it yet. Re-read before moving on (1.5 hours).
5. **Commit and push** to GitHub (15 min).

**Stuck rule:** if you're stuck for more than 30 minutes, paste your code and the exact error into Claude. Struggling for hours teaches nothing.

---

## Phase 1: Python foundations (Weeks 1-3)

| Week | Topic | Real-life example | You build |
|------|-------|-------------------|-----------|
| 1 (done) | Variables, strings, lists, loops, functions | Spotting weak passwords | `password_checker.py` |
| 2 (done) | Files, dictionaries, error handling | Catching password guessing in a server log | `log_analyzer.py` |
| 3 | **Consolidation: no new concepts.** Re-read `CONCEPTS.md`, rebuild both programs from a blank file, then extend them | Same examples, now from memory | Rewritten checkers + short quiz |

Week 3 is deliberate. Skipping it is the most common reason beginners get lost later.

## Phase 2: How applications get attacked (Weeks 4-7)

This is the "security around the AI" block. Most AI security incidents are here.

| Week | Topic | Real-life example | You build |
|------|-------|-------------------|-----------|
| 4 | How the web works: HTTP, requests, JSON, status codes (200, 401, 403) | What happens when you open a banking app | Python script that calls a public API |
| 5 | Authentication vs authorization, password hashing, tokens, secrets | Logging in is not the same as being allowed to see someone else's data | Password hashing demo + secrets handling |
| 6 | Build a tiny API and test it with `pytest` | User A must not read user B's chat history | A small API with security tests (**Project 1**) |
| 7 | Threat modeling + OWASP API Security Top 10; start the PortSwigger API labs | How a security team thinks "what could go wrong?" | One-page threat model for your Week 6 API |

## Phase 3: Machine learning basics (Weeks 8-11)

A model is a program that learns patterns from examples instead of following hand-written rules.

| Week | Topic | Real-life example | You build |
|------|-------|-------------------|-----------|
| 8 | `pandas` and charts | Plotting login attempts to see the attack spike | `login_report.py` |
| 9 | What is ML? Train/test split, scikit-learn | Teaching a computer to tell spam from real email | Spam classifier |
| 10 | Measuring a model: accuracy, precision, recall | Why "99% accurate" fraud detection can be useless | Evaluation notebook |
| 11 | Anomaly detection | Flagging a card used in two countries in one hour | Fraud detector (**Project 2**) |

## Phase 4: Attacking AI (Weeks 12-14)

Now you think like an attacker, which is how defenders learn.

| Week | Topic | Real-life example | You build |
|------|-------|-------------------|-----------|
| 12 | Evasion attacks (adversarial examples) | A fraudster tweaking a transaction so the detector misses it | Attack on your fraud detector (**Project 3**) |
| 13 | Data poisoning | An attacker slipping bad examples into a spam filter's training data | Poisoning experiment |
| 14 | LLM attacks: prompt injection, data leakage | A hidden instruction in a web page that hijacks a chatbot | Prompt injection test lab (**Project 4**) |

## Phase 5: Defending and getting hired (Weeks 15-16)

| Week | Topic | Real-life example | You build |
|------|-------|-------------------|-----------|
| 15 | Defenses; OWASP Top 10 for LLMs, MITRE ATLAS, NIST AI RMF | How a bank hardens its detector after an attack | Hardened system + before/after report (**Project 5**) |
| 16 | Portfolio polish and interview prep | Explaining your project in 2 minutes | Final README, demo, interview notes |

---

## Rules

1. **Only attack systems you own.** Everything here targets code and models you build yourself.
2. **One idea at a time.** Never start a new week with the old one unclear.
3. **Commit weekly.** A visible history on GitHub shows recruiters you finish what you start.
