import re

def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r'[A-Z]', password):
        score += 1

    if re.search(r'[a-z]', password):
        score += 1

    if re.search(r'[0-9]', password):
        score += 1

    if re.search(r'[!@#$%^&*(),.?":{@}|<>]', password):
        score += 1

    if score == 5:
        return "Very Strong"
    elif score >= 3:
        return "Strong"
    elif score == 2:
        return "Moderate"
    elif score == 1:
        return "Weak"
    else:
        return "Very Weak"

password = input("Enter your password: ")
strength = password_strength(password)
print("Password strength:", strength)
