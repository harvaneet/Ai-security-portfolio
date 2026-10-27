# Concepts Recap (Weeks 1-2), in plain language

Read this when something feels fuzzy. Every idea has a real-world picture first, then the code.

---

## Variable = a labeled box

Picture a moving box with "KITCHEN" written on it. The label is the variable's name. What's inside is its value.

```python
username = "priya"     # box labeled username, containing text
failed_attempts = 3    # box labeled failed_attempts, containing a number
```

You can change what's in the box later: `failed_attempts = 4`.

## String = text, list = a numbered row of things

A **string** is text in quotes: `"hello"`. A **list** is several things in order, in square brackets:

```python
blocked_ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
blocked_ips[0]      # "10.0.0.1"  (Python counts from 0, not 1)
len(blocked_ips)    # 3
"10.0.0.2" in blocked_ips   # True
```

Real picture: a guest list at a door. "Is this person on the list?" is `in`.

## Loop = "do this for every item"

Picture a security guard checking every ID in a queue.

```python
for ip in blocked_ips:
    print("checking", ip)
```

The line `for ip in blocked_ips:` means: take each item in turn, call it `ip`, and run the indented lines below it. **The indentation (spaces at the start) is how Python knows what's inside the loop.**

## If / else = a decision

```python
if failed_attempts >= 5:
    print("lock the account")
else:
    print("allow another try")
```

Picture a bouncer: if you are over 21, enter; otherwise, no.

## Function = a reusable recipe

A recipe takes ingredients, follows steps, and gives you a dish. A function takes inputs, runs code, and gives back an output with `return`.

```python
def is_locked(failed_attempts):
    return failed_attempts >= 5

is_locked(3)    # False
is_locked(7)    # True
```

`def` creates the recipe. Calling `is_locked(7)` uses it. You write once and reuse everywhere. That's why security tools are built from many small functions.

## Dictionary = a phone book

A list finds things by position. A dictionary finds them by **name** (the *key*), like looking up a person in a phone book.

```python
failures = {"203.0.113.5": 8, "198.51.100.7": 2}
failures["203.0.113.5"]          # 8
failures["1.1.1.1"] = 1          # add a new entry
failures.get("9.9.9.9", 0)       # 0, a safe default when the key doesn't exist
```

The counting trick from Week 2, in plain words:

```python
counts[ip] = counts.get(ip, 0) + 1
```

"Look up this IP's count (or use 0 if it's new), add one, write it back." It's a tally sheet: each time you see an IP, add a mark next to its name.

## Reading a file

```python
with open("auth.log") as f:
    lines = f.read().splitlines()
```

Picture opening a notebook and copying each line onto a list. `with` closes the notebook for you afterwards.

## split() = cutting a sentence into words

```python
line = "2026-10-20 08:01:12 FAILED user=admin ip=203.0.113.5"
parts = line.split()
parts[2]                    # "FAILED"
parts[4].split("=")[1]      # "203.0.113.5"
```

`split()` cuts at spaces; `split("=")` cuts at the equals sign. `[1]` picks the second piece, because counting starts at 0.

## try / except = a safety net

```python
try:
    open("missing.log")
except FileNotFoundError:
    print("file not found, but the program keeps running")
```

Without the net, one missing file crashes the whole program. Real logs are messy, so security tools must survive bad data.

---

## Three mistakes almost everyone makes (and how to read the error)

| Error message | What it usually means |
|---|---|
| `IndentationError` | Your spaces at the start of a line are inconsistent. Use 4 spaces. |
| `NameError: name 'x' is not defined` | You used a variable before creating it, or misspelled it. |
| `TypeError` / `IndexError` | You mixed text with numbers, or asked for item `[5]` in a list of 3. |

**How to read any Python error:** go to the *last* line first. It says what went wrong. The line above it says where.

## Self-check (answer without looking)

1. What is the difference between a list and a dictionary?
2. What does `return` do?
3. Why does Python count from 0?  (Honest answer: convention. Just remember it.)
4. Why do we wrap file reading in `try/except`?

Write your answers in `NOTES.md`. If you can't answer one, that's the thing to re-read.
