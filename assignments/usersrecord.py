def save_user_profile():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")

    with open(f"./lessons/users_profile.txt", "a") as f:
        f.write("=== User profile ===\n")
        f.write(f"Name:{name}\n")
        f.write(f"Age:{age}\n")
        f.write(f"Email:{email}\n")

        print("Saved")

stop = False

save_user_profile()
while not stop:
    action = input("Do you want to continue y/n: ")
    if action == "n":
        stop = True
    elif action == "y":
        save_user_profile()