systemMenu = {"ข้าวมันไก่":40, "ข้าวขาหมู":45, "ข้าวหน้าเป็ด":50, "ข้าวหน้าหมูย่าง":40}
menuList = []

def showBill():
    totalPrice = 0
    print("--- Tuinui Restaurant ---")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
        totalPrice += menuList[i][1]
    print("Total Price :",totalPrice)
while True:
    menuName = input("Pease enter menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showBill()
