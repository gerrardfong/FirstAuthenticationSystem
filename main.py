users = ["sithLord", "d_Vader", "GENERALleia", "grogu", "there_is_no_try", "MyRey", "Luke"]
passwords = ["Ancient enimes r us", "I'm Your Father", "May the Force be with you", "patu", "Yoda", "Jedi", "May the Force be with you"]
new_passwords = []

end = True

def start():
    global end
    
    print(users)
    print(passwords)
    print("Welcome to the program.", end="\n"*2)
    print("1. Login")
    print("2. Register")
    print("3. Quit", end="\n"*2)

    while end:
        question = input("What would you like to do? ").capitalize().strip()
        if question == "Login" or question == "1":
            login()
            end == False
        elif question == "Register" or question == "2":
            register()
            end == False
        elif question == "Quit" or question == "3":
            print("Goodbye and Thank you.") 
            end == False
        else: 
            print("Invaild input. Try again.")
            continue


def newstart():
    end = True

    print("Welcome Back. ", end="\n"*2)
    print("1. Change Password")
    print("2. Logout", end="\n"*2)

    while end:
        question = input("What would you like to do? ").title().strip()
        if question == "Change Password" or question == "1":
            change_password()
            end == False

        elif question == "Logout" or question == "2":
            print("-"*50)
            start()
            end == False
            
        else:
            print("Invaild input. Try again.")
            continue
        

def login():
    c_user = input("Please enter your user: ").strip()    

    if c_user not in users:
        print("Do you need to register? ")
        print("-"*50)
        start()

    for i in range(len(users)):
        if c_user == users[i]:
            c_user = i
    

    else:
        password = input("Enter Password: ")

        for i in range(len(passwords)):
            if password == passwords[i]:
                password = i

        if c_user == password:
            print("-"*50)
            print("Successful login. ")
            print("-"*50)
            newstart()
    
        else:
            print("Your password was invalid.")
            login()


def change_password():
    print("This function does not work as of right now. ")
    newstart()
    
def register():
    new_user = input("What would you like your user to be? ")
    users.append(new_user)

    new_password = input("What is your password: ")               

    if len(new_password) < 4:
        print("Password must be longer than 4 character.")
        while True:
            new_password = input("What would like you new password to be: ")
            if len(new_password) < 4:
                continue
            else: 
                break
    
    passwords.append(new_password)
    print("Thank you for joining. ")
    print(passwords)
    print(users)
    print("-"*50)
    newstart()


def change_password():

    user = input("Please re-enter your user: ")

    if user not in users:
        print("Not a real user.")

    for i in range(len(users)):
            if user == users[i]:
                user = i

    else:
        n_password = input("What would like you new password to be: ")
    
        if len(n_password) < 4:
            print("Password must be longer than 4 character.")
            while True:
                n_password = input("What would like you new password to be: ")
                if len(n_password) < 4:
                    continue
                else: 
                    break
    
        passwords.append(n_password)
        print("-"*50)
        print("Yeah this function pretty much doesn't reassign the password so.")
        newstart()
    



start()




