license_plate_by_username = {}

n = int(input())
for _ in range(n):
    command_arg = input().split()
    command = command_arg[0]
    username = command_arg[1]

    if command == "register":
        license_plate = command_arg[2]
        if username in license_plate_by_username:
            print(f"ERROR: already registered with plate number {license_plate_by_username[username]}")
        else:
            license_plate_by_username[username] = license_plate
            print(f"{username} registered {license_plate} successfully")

    elif command == "unregister":
        if username not in license_plate_by_username:
            print(f"ERROR: user {username} not found")
        else:
            license_plate_by_username.pop(username)
            print(f"{username} unregistered successfully")

for key, value in license_plate_by_username.items():
    print(f"{key} => {value}")