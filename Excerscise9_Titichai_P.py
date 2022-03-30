usernameInput = input("Username : ")
passwordInput = input("Password : ")
while usernameInput != "Tuinui" or passwordInput != "happy":
    if usernameInput != "Tuinui" and passwordInput != "happy":
        print("Username and Password are incorrect!")
    elif usernameInput != "Tuinui":
        print("Username is incorrect!")
    else:
        print("Password is incorrect!")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")

print("Hello! Wellcome.")