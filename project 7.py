#PROJECT 7
#shopping cart system- Add/remove item(list) track unique catogories set store item price pairs(dictionary), compute total bill
cart=[]
categories=set()
prices={}
while True:
    print("Enter your choice:--")
    print("1. Add item")
    print("2. Remove item")
    print("3.My bill")
    print("4.Exit")
    ch=(int(input("Enter your choice")))
    if (ch==1):
        item = input("Enter item name: ")
        price = int(input("Enter price: "))
        category = input("Enter category: ")
        cart.append(item)
        prices[item] = price
        categories.add(category)
    elif ch == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            del prices[item]

    elif ch == 3:
        total = 0
        for p in prices.values():
            total += p
        print("Total Bill:", total)
        print("Categories:", categories)

    elif ch == 4:
        break