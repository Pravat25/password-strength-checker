import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 2
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase letters
    if re.search("[A-Z]", password):
        score += 2
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase letters
    if re.search("[a-z]", password):
        score += 2
    else:
        suggestions.append("Add lowercase letters")

    # Numbers
    if re.search("[0-9]", password):
        score += 2
    else:
        suggestions.append("Include numbers")

    # Special characters
    if re.search("[@#$%^&*!]", password):
        score += 2
    else:
        suggestions.append("Use special characters (@#$%^&*)")

    # Determine strength
    if score <= 4:
        strength = "Weak"
    elif score <= 7:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, score, suggestions


password = input("Enter a password to check: ")

strength, score, suggestions = check_password_strength(password)

print("\n===== Password Security Report =====")
print(f"Password Strength: {strength}")
print(f"Security Score: {score}/10")

if suggestions:
    print("\nSuggestions to improve password:")
    for s in suggestions:
        print(f"- {s}")
