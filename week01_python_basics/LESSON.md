# Week 1: Python basics through password security

**Real-life story:** In 2012 millions of LinkedIn passwords leaked, and a huge share were things like `123456` and `password`. Attackers don't guess randomly. They try the most common passwords first. Today you'll write a program that spots weak passwords the way a security tool would.

You'll learn five Python ideas. Each one is used in the script `password_checker.py`.

---

## 1. Variables: labeled boxes

A variable stores a value under a name.

```python
password = "hello123"
min_length = 8
```

`password` is text (called a **string**). `min_length` is a number (an **integer**).

## 2. Strings: text and what you can ask about it

```python
password = "Hello123"
len(password)          # 8, the number of characters
password.lower()       # "hello123"
password.isdigit()     # False, because it has letters too
```

Real use: a checker needs to ask "how long is it?" and "does it have a number in it?"

## 3. Lists: a collection of things

```python
common_passwords = ["123456", "password", "qwerty", "letmein"]
"qwerty" in common_passwords    # True
```

Real use: attackers keep lists of leaked passwords. Defenders check new passwords against the same lists.

## 4. Loops: do something for each item

```python
for char in "abc":
    print(char)
```

Real use: to check if a password contains at least one digit, look at each character in turn.

## 5. Functions: reusable recipes

```python
def is_long_enough(password):
    return len(password) >= 8
```

A function takes input, does work, and gives back a result with `return`. Once written, you can reuse it everywhere. Security tools are built from many small functions like this.

## 6. If / else: making decisions

```python
if len(password) < 8:
    print("Too short")
else:
    print("Length OK")
```

---

## Run the code

From the repo folder:

```bash
python3 week01_python_basics/password_checker.py
```

Read the script top to bottom. Every line uses only the ideas above.

## Exercises (do these before Week 2)

1. **Easy:** Add `"admin"` and `"welcome"` to the common password list. Run it again.
2. **Medium:** Add a check that the password has at least one special character like `!` or `@`. Hint: loop over characters and test `char in "!@#$%"`.
3. **Medium:** Make the checker reject any password containing the word `password` anywhere inside it, such as `mypassword99`.
4. **Challenge:** Give each password a score out of 5 (one point per passed check) and print "weak", "okay", or "strong".

## Interview-style question

*"Why is a long password usually better than a complex short one?"* Write your answer in 3 sentences in a file called `notes.md`. Hint: think about how many guesses an attacker needs.

## Commit your work

```bash
git add .
git commit -m "Week 1: password checker and exercises"
```
