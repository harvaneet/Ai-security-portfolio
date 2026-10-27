# AI Security Portfolio

My journey learning **cybersecurity for AI** with Python, from zero to portfolio projects. Each folder is one week of work.

## What this repo shows

- Python fundamentals applied to security problems
- Securing the application around an AI system (authentication, authorization, API tests, threat modeling)
- Machine learning for threat detection (fraud, spam, anomalies)
- Attacks on ML models (evasion, poisoning, prompt injection)
- Defenses and threat modeling (OWASP API and LLM Top 10, MITRE ATLAS)

## Projects

| # | Project | Status |
|---|---------|--------|
| 1 | Secure API with security tests | Planned (Week 6) |
| 2 | Fraud detector | Planned (Week 11) |
| 3 | Attack on the fraud detector | Planned (Week 12) |
| 4 | Prompt injection test lab | Planned (Week 14) |
| 5 | Hardened system with before/after report | Planned (Week 15) |

## Progress

- [x] Week 1: Python basics through password checking
- [ ] Week 2: Log analysis
- [ ] Week 3: Consolidation (rebuild Weeks 1-2 from memory)
- [ ] Weeks 4-16: see [SYLLABUS.md](SYLLABUS.md)

Stuck on a concept? See [CONCEPTS.md](CONCEPTS.md).

## Run it yourself

```bash
git clone <your-repo-url>
cd ai-security-portfolio
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python week01_python_basics/password_checker.py
```

## Ethics

All attacks in this repo target models, data, and systems I created myself, for learning and defense.
