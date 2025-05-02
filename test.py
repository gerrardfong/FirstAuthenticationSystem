import bcrypt

salt = b"$2b$12$ieYNkQp8QumgedUo30nuPO"

def main():
    password = "monkey"
    input_password = input("What's your password? ")
    hashed_password = bcrypt.hashpw(password.encode(), salt=salt)
    if bcrypt.checkpw(input_password.encode(), hashed_password):
        print("Logged in.")
    else:
        print("You are no. ")

main()

