# user_logger.py

username = input("Enter your name: ")
email = input("Enter your email: ")

with open("user_info.txt", "w") as file:
    file.write(f"user: {username}\nEmail: {email}\n")

print("USer information logged sucessfully.")
