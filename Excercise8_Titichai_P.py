usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "tuinui" and passwordInput == "happy":
    print("Done !")
    print("----- Wellcome -----")
    print("----- Menu -----")
    print("1. pepsi")
    print("2. coke")
    print("3. est")

    userSelected = int(input("Select >>"))
    quantity = int(input("Quantity >>"))
    if userSelected == 1:
        pepsi = 15
        result = pepsi * quantity
        print(result)
    elif userSelected == 2:
        coke = 15
        result = coke * quantity
        print(result)
    elif userSelected == 3:
        est = 16
        result = est * quantity
        print(result)
else:
    print("Error")