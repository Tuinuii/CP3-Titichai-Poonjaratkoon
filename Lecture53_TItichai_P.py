def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

price = float(input("Price : "))
print("Total Price = ",vatCalculate(price),"Baht")