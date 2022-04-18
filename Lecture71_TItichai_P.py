menuList = []
priceList = []

def showBill():
    totalPrice = 0
    print("--- Tuinui Restaurant ---")
    for i in range(len(menuList)):
        print(menuList[i],priceList[i])
        totalPrice += priceList[i]
    print("Total Price :",totalPrice,"Baht.")

while True:
    menuName = input("Pease enter menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()
