import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (min 8 characters recommended)")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    # Digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        feedback.append("Add at least one special character")

    # Common patterns
    common_patterns = ["123456", "password", "qwerty", "abc123"]
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 2
        feedback.append("Avoid common patterns (e.g., '123456', 'password')")

    return score, feedback


def get_strength_label(score):
    if score <= 2:
        return "Very Weak 🔴"
    elif score <= 4:
        return "Weak 🟠" 
    elif score <= 6:
        return "Moderate 🟡"
    elif score <= 8:
        return "Strong 🟢"
    else:
        return "Very Strong 💪"

 
def main():
    print("🔐 Password Strength Checker\n")

    password = input("Enter your password: ")

    score, feedback = check_password_strength(password)
    strength = get_strength_label(score) 

    print("\n--- Result ---")
    print(f"Strength: {strength}")
    print(f"Score: {score}/10")

    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print(f"- {f}")
    else:
        print("\nGreat password! No suggestions.")

if __name__ == "__main__":
    main()