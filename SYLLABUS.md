# 12-Week Syllabus: Python + Cybersecurity in AI (from zero)

**Time needed:** about 6 hours per week. **Goal:** finish with 4 portfolio projects and enough knowledge to interview for AI security, ML security, or security engineering roles.

**How each week works:** read the lesson, run the code, do the exercises, commit your work to Git. One commit per week gives you a visible learning history on GitHub, which recruiters like.

---

## Phase 1: Python foundations (Weeks 1-3)

You do not need to master Python. You need enough to read and write security scripts.

| Week | Topic | Real-life example | You build |
|------|-------|-------------------|-----------|
| 1 | Variables, strings, lists, loops, functions | Checking if a password is weak | `password_checker.py` |
| 2 | Dictionaries, files, error handling | Reading a server log and counting failed logins | `log_analyzer.py` |
| 3 | Libraries: `pandas`, `numpy`, plotting | Spotting a suspicious spike in login attempts on a chart | `login_report.py` |

## Phase 2: Machine learning basics (Weeks 4-6)

A model is a program that learns patterns from examples instead of following hand-written rules.

| Week | Topic | Real-life example | You build |
|------|-------|-------------------|-----------|
| 4 | What is ML? Train/test split, scikit-learn | Teaching a computer to tell spam from normal email | Spam classifier |
| 5 | Measuring a model: accuracy, precision, recall | Why "99% accurate" fraud detection can still be useless | Evaluation notebook |
| 6 | Anomaly detection | Flagging a credit card used in two countries within an hour | Fraud detector (**Project 1**) |

## Phase 3: Attacking AI (Weeks 7-9)

Now you think like an attacker, which is how defenders learn.

| Week | Topic | Real-life example | You build |
|------|-------|-------------------|-----------|
| 7 | Evasion attacks (adversarial examples, FGSM) | A fraudster tweaking a transaction so the detector misses it | Attack on your Project 1 model (**Project 2**) |
| 8 | Data poisoning | An attacker slipping bad training data into a spam filter | Poisoning experiment |
| 9 | LLM attacks: prompt injection, data leakage | A hidden instruction in a web page that hijacks a chatbot | Prompt injection test lab (**Project 3**) |

## Phase 4: Defending AI and getting hired (Weeks 10-12)

| Week | Topic | Real-life example | You build |
|------|-------|-------------------|-----------|
| 10 | Defenses: adversarial training, input validation | Bank hardening its detector after an attack | Hardened model + before/after report |
| 11 | Frameworks: OWASP Top 10 for LLMs, MITRE ATLAS, NIST AI RMF | How a security team writes a threat model | Threat model document (**Project 4**) |
| 12 | Portfolio polish and interview prep | Explaining your project in 2 minutes | Final README, demo, interview notes |

---

## Rules for learning

1. **Type the code yourself.** Do not copy and paste. Typing builds the skill.
2. **Break things on purpose.** Change a number, see what happens.
3. **Commit weekly.** `git add . && git commit -m "Week N: what I learned"`.
4. **Only attack systems you own.** Everything in this course targets models you train yourself.
