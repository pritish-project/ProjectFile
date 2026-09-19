

while True:
    menu = {"Pizza":80,"pizza":80,
            "Burger":90,"burger":90,
            "Pasta":80,"pasta":80,
            "Chai":10,"chai":10
            }
    coupon = "lucky"
    total_order = 0
    order1 = input("Enter your order:")
    if order1 in menu:
       
        total_order+=menu[order1]
        print("Your order is placed",total_order)
    
    
    else:
        print("Your order not Available")
        print("You may try other FoodItems in Menu\nPizza:\nBurger\nPasta\nChai")
        order1 = input("Enter your order")
        if order1 in menu:
            if(order1=="Pizza" and order1=="n"):
                print("Sorry you cant order only pizza")
                break
            
            total_order+=menu[order1]
            print("Your order is placed",total_order)
        break

        
    another_order = input("Do u want to add another order:")
    if another_order == "y" or another_order == "Y":
        order2 = input("Plzzzz Enter your order")
        if order2 in menu:
            total_order+=menu[order2]
            print("Your order is placed:",total_order)


    coupon_code = input("Do u have coupon code:")
    if coupon_code=="y" or coupon_code=="Y":
        n = input("Enter a coupon code:")
        if(n==coupon):
            total_order=(total_order*20)/100
            print("Your Order After applying coupon",total_order)


    if another_order=="n" or another_order=="N":
        break
        
    break

