class User:
    products = [
        {"name": "1", "price": 200, "qnt": 10},
        {"name": "product2", "price": 700, "qnt": 20},
        {"name": "product3", "price": 999, "qnt": 5}
    ]


class Buyer(User):
    def buyerproducts(self):
        name = input("Enter the product name you want to buy ")
        # price = input("Enter thr product price you wnat to buy ")
        qnt = int(input("Enter the Quantity you want to buy "))
        total_price = 0
        product_buy = self.products
        counter = 0

        for i in self.products:
            if i['name'] == name:
                print(counter)
                if qnt >= i['qnt']:
                    print("only ", i['qnt'], "remining")
                else:
                    i['qnt'] = i['qnt'] - qnt
                    print(self.products)

                break;
            counter = counter + 1
        total_price = i['price'] * qnt
        print("Your total bill is ", total_price)


class Seller(User):
    def addproducts(self):
        name = input("Enter the product name ")
        price = int(input("Enter the product price "))
        qnt = int(input("Enter the Quantity "))
        temp = {"name": name, "price": price, "qnt": qnt}
        self.products.append(temp)
        print(self.products)

    def deleteproducts(self):
        name = input("Enter product name ")
        product_name = []
        for product in self.products:
            if product["name"] == name:
                product_name = product
                break
        if product_name:
            self.products.remove(product_name)
            print("product removed ")
            print(self.products)
        else:
            print("product not found ")


print("Welcome To Store systumm......")
role = input("Enter seller for sell Enter buyer for buy \n")
if role == "seller":
    ch = int(input("1. Add Product For Sell\n2. Delete Product\n"))
    if ch == 1:
        s1 = Seller()
        s1.addproducts()
    elif ch == 2:
        s2 = Seller()
        s2.deleteproducts()
else:
    # role == Buyer():
    b = Buyer()
    b.buyerproducts()
