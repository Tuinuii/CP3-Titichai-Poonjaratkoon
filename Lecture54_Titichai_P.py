def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "Tuinui" and passwordInput == "happy":
        return True
    else:
        return False

def showMenu():
    print("------Tuinui Shop------")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelect = int(input("Menu Select >> "))
    return userSelect

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * 7/100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)


# Main Program
print(login())
print(menuSelect())
print(priceCalculator())
