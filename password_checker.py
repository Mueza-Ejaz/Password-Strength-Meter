import re # regular expressions (searching characters)

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append(" Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password): # r = raw string
        score += 1
    else:
        feedback.append(" Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password): # \d = digits
        score += 1
    else:
        feedback.append(" Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append(" Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return score, "Strong", feedback
    elif score == 3:
        return score, "Moderate", feedback
    else:
        return score, "Weak", feedback





