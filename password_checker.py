"""Week 1: a simple password strength checker.

Uses: variables, strings, lists, loops, functions, if/else.
"""

# A tiny sample of passwords attackers try first (real lists have millions).
COMMON_PASSWORDS = ["123456","admin", "password", "qwerty", "letmein", "111111", "abc123", "welcome"]

MIN_LENGTH = 8


def is_long_enough(password):
    """Return True if the password has at least MIN_LENGTH characters."""
    return len(password) >= MIN_LENGTH


def has_digit(password):
    """Return True if the password contains at least one number."""
    for char in password:
        if char.isdigit():
            return True
    return False

def has_characters(password):
    """Return True if the password contains at least one special character."""
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
    for char in password:
        if char in special_characters:
            return True
        return False
    
def has_upper_and_lower(password):
    """Return True if the password has both uppercase and lowercase letters."""
    has_upper = False
    has_lower = False
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
    return has_upper and has_lower


def is_common(password):
    """Return True if the password is on the common-passwords list."""
    return password.lower()in COMMON_PASSWORDS

def contain_password_word(password):
    """Return True if the password contains the word 'password'."""
    return "password" in password.lower()


def check_password(password):
    """Run all checks and return a list of problems found."""
    problems = []
    if not is_long_enough(password):
        problems.append(f"shorter than {MIN_LENGTH} characters")
    if not has_digit(password):
        problems.append("no number")
    if not has_upper_and_lower(password):
        problems.append("needs both upper and lower case letters")
    if is_common(password):
        problems.append("is one of the most commonly used passwords")
    if not has_characters(password):
        problems.append("needs special character")
    if contain_password_word(password):
        problems.append("contains the word 'password'")
    return problems

def score_password(password):
    score = 0
    if is_long_enough(password):
        score += 1
    if has_digit(password):
        score += 1
    if has_upper_and_lower(password):
        score += 1
    if not is_common(password):
        score += 1
    if has_characters(password):
        score += 1  
    if score <= 2:
        label = "Weak"
    elif score <= 4:
        label = "Moderate"
    else:
        label = "Strong"
    return score, label

def main():
    test_passwords = ["123456", "hello", "Hello123", "Tr0ub4dor&3xtra@", "admin", "welcome", "mypassword"]

    for pw in test_passwords:
        problems = check_password(pw)
        if problems:
            print(f"WEAK   '{pw}': " + "; ".join(problems))
        else:
            print(f"OK     '{pw}': passed all checks")

    #Score the passwords based on the number of problems found
    for pw in test_passwords:
        score, label = score_password(pw)
        print(f"{pw}: score {score}/5 -> {label}")


if __name__ == "__main__":
    main()
