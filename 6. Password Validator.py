def is_password_length_valid(password: str):
    if 6 <= len(password) <= 10:

        return True

    return False


def is_password_alphanumeric(password: str):
    return password.isalnum()


def got_2_digits(password: str):
    digit = 0

    for ch in password:
        if ch.isnumeric():
            digit += 1

    if digit >= 2:
        return True

    else:
        return False


def validate_pass(password: str):
    is_valid = True

    if not is_password_length_valid(password):
        print(f"Password must be between 6 and 10 characters")
        is_valid = False

    if not is_password_alphanumeric(password):
        print(f"Password must consist only of letters and digits")
        is_valid = False

    if not got_2_digits(password):
        print(f"Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print(f"Password is valid")


password_value = input()

validate_pass(password_value)
