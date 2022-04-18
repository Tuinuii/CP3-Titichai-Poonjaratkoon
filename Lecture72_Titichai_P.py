menuList = []

def showBill():
    totalPrice = 0
    print("--- Tuinui Restaurant ---")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
        totalPrice += int(menuList[i][1])
    print("Total Price :",totalPrice)
while True:
    menuName = input("Pease enter menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName,menuPrice])

showBill()
