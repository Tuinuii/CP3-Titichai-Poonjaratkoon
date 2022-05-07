class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to ",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Tui"
customer1.lastName = "hello"
customer1.addCart()

customer2 = Customer()
customer2.name = "Earn"
customer2.lastName = "hello"
customer2.addCart()

customer3 = Customer()
customer3.name = "Tae"
customer3.lastName = "hello"
customer3.addCart()

customer4 = Customer()
customer4.name = "Kaew"
customer4.lastName = "hello"
customer4.addCart()
