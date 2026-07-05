import secrets
import string


def generate_password(length=16, use_uppercase=True, use_digits=True, use_special=True):
    # Always include lowercase letters
    letters = string.ascii_lowercase
    
    # Add optional character sets based on preferences
    if use_uppercase:
        letters += string.ascii_uppercase
    if use_digits:
        letters += string.digits
    if use_special:
        letters += string.punctuation

    # Ensure the password length is at least 4 to avoid logic issues
    if length < 4:
        length = 4

    # Guarantee at least one character from each selected set is included
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase) if use_uppercase else secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits) if use_digits else secrets.choice(string.ascii_lowercase),
        secrets.choice(string.punctuation) if use_special else secrets.choice(string.ascii_lowercase)
    ]

    # Fill the rest of the password length with random characters from the combined pool
    password += [secrets.choice(letters) for _ in range(length - len(password))]

    # Shuffle the list securely to randomize the guaranteed characters' positions
    secrets.SystemRandom().shuffle(password)

    # Convert the list back into a string
    return "".join(password)


# --- Example Usage ---
if __name__ == "__main__":
    # Generate a default 16-character strong password
    print("Default Secure Password:", generate_password())

    # Generate a custom 24-character password
    print("Custom 24-char Password:", generate_password(length=24, use_special=False))
