import string
import secrets


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password


print("===== PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Please enter a positive number.")
        elif length < 8:
            print("For better security, use at least 8 characters.")
        else:
            password = generate_password(length)

            print("\nGenerated Password:", password)
            break

    except ValueError:
        print("Please enter a valid number.")
