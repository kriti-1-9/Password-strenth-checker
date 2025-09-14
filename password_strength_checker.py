import re

def check_password_strength(password: str) -> str:
    """
    Returns: 'Weak', 'Medium', or 'Strong' based on length and complexity
    """
    length = len(password)
    score = 0

    # Length
    if length >= 8:
        score += 2
    if length >= 12:
        score += 2
    if length < 6:
        score -= 1

    # Character types
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[^A-Za-z0-9]', password):  # special characters
        score += 1

    # Decide strength
    if score <= 2:
        return "Weak"
    elif 3 <= score <= 5:
        return "Medium"
    else:
        return "Strong"


# Demo
if __name__ == "__main__":
    pw = input("Enter a password: ")
    print(f"Strength: {check_password_strength(pw)}")