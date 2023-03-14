from string import ascii_letters, digits

valid = (ascii_letters + digits + "-" + "_")

usernames = input().split(", ")

for username in usernames:
    if len(username) < 3 or len(username) > 16:
        continue

    # contain_forbidden = False
    # for char in username:
    #     if char not in valid:
    #         contain_forbidden = True
    #         break
    #
    # if contain_forbidden:
    #     continue
    allow_chars = all([char in valid for char in username])
    if not allow_chars:
        continue

    print(username)


