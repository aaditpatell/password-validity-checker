import random
import string

COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley",
    "michael", "shadow", "123123", "654321", "superman"
]


def generate_password(length, use_upper, use_digits, use_symbols):
    pool = string.ascii_lowercase

    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += "!@#$%^&*()-_=+[]{}|;:,.<>?"

    if length < 1:
        print("Length must be at least 1.")
        return None

    password = []

    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?"))

    while len(password) < length:
        password.append(random.choice(pool))

    random.shuffle(password)
    return ''.join(password)


def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1

    if len(password) >= 16:
        score += 1

    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    for ch in password:
        if ch in string.ascii_lowercase:
            has_lower = True
        elif ch in string.ascii_uppercase:
            has_upper = True
        elif ch in string.digits:
            has_digit = True
        else:
            has_symbol = True

    if has_lower:
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if has_upper:
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if has_digit:
        score += 1
    else:
        feedback.append("Add numbers")

    if has_symbol:
        score += 1
    else:
        feedback.append("Add special characters")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This is a commonly used password")

    has_sequence = False
    for i in range(len(password) - 2):
        if password[i] == password[i+1] and password[i+1] == password[i+2]:
            has_sequence = True
            break

    if has_sequence:
        score -= 1
        feedback.append("Avoid repeated characters (e.g. aaa)")

    has_sequential = False
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i+1]) and ord(password[i+1]) + 1 == ord(password[i+2]):
            has_sequential = True
            break

    if has_sequential:
        score -= 1
        feedback.append("Avoid sequential characters (e.g. abc, 123)")

    if score < 0:
        score = 0

    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Moderate"
    elif score <= 5:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return rating, score, feedback


def run_generator():
    print()
    try:
        length = int(input("Password length: "))
    except ValueError:
        print("Invalid length.")
        return

    use_upper = input("Include uppercase? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)
    if password is not None:
        print(f"\nGenerated password: {password}")
        rating, score, _ = check_strength(password)
        print(f"Strength: {rating} ({score}/7)")


def run_checker():
    print()
    password = input("Enter a password to check: ")
    rating, score, feedback = check_strength(password)

    print(f"\nStrength: {rating} ({score}/7)")
    if len(feedback) > 0:
        print("Suggestions:")
        for tip in feedback:
            print(f"  - {tip}")


def main():
    print("Password Tool")

    while True:
        print()
        print("1) Generate password")
        print("2) Check password strength")
        print("3) Quit")

        choice = input("> ").strip()

        if choice == "1":
            run_generator()
        elif choice == "2":
            run_checker()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
