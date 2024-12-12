# INVENTORY MANAGEMENT SYSTEM
inventory = {
    1: {
        "ProductName": "Laptop",
        "ProductCategory": "Electronics",
        "QuantityinStock": 20,
        "PriceperUnit": 800,
        "ExpiryDate": "2023-12-31"
    },
    2: {
        "ProductName": "Backpack",
        "ProductCategory": "Fashion",
        "QuantityinStock": 50,
        "PriceperUnit": 30,
        "ExpiryDate": None
    },
    3: {
        "ProductName": "Coffee Maker",
        "ProductCategory": "Appliances",
        "QuantityinStock": 15,
        "PriceperUnit": 100,
        "ExpiryDate": "2024-06-30"
    },
    4: {
        "ProductName": "Running Shoes",
        "ProductCategory": "Footwear",
        "QuantityinStock": 30,
        "PriceperUnit": 50,
        "ExpiryDate": None
    },
    5: {
        "ProductName": "Notebook",
        "ProductCategory": "Stationery",
        "QuantityinStock": 100,
        "PriceperUnit": 5,
        "ExpiryDate": None
    },
    6: {
        "ProductName": "Protein Powder",
        "ProductCategory": "Health",
        "QuantityinStock": 25,
        "PriceperUnit": 25,
        "ExpiryDate": "2024-04-15"
    },
    7: {
        "ProductName": "Desk Chair",
        "ProductCategory": "Furniture",
        "QuantityinStock": 10,
        "PriceperUnit": 150,
        "ExpiryDate": None
    },
    8: {
        "ProductName": "Smartphone",
        "ProductCategory": "Electronics",
        "QuantityinStock": 15,
        "PriceperUnit": 600,
        "ExpiryDate": "2023-11-30"
    },
    9: {
        "ProductName": "T-shirt",
        "ProductCategory": "Fashion",
        "QuantityinStock": 40,
        "PriceperUnit": 20,
        "ExpiryDate": None
    },
    10: {
        "ProductName": "Microwave Oven",
        "ProductCategory": "Appliances",
        "QuantityinStock": 12,
        "PriceperUnit": 120,
        "ExpiryDate": "2024-07-15"
    },
    11: {
        "ProductName": "Umbrella",
        "ProductCategory": "Accessories",
        "QuantityinStock": 60,
        "PriceperUnit": 10,
        "ExpiryDate": None
    },
    12: {
        "ProductName": "Yoga Mat",
        "ProductCategory": "Health",
        "QuantityinStock": 20,
        "PriceperUnit": 15,
        "ExpiryDate": None
    }
}


#add products
def addproduct(inventory,P_id,P_Name,P_Cat,Quantity,Price,E_Date):
    newproduct = {
        "ProductName": P_Name,
        "ProductCategory": P_Cat,
        "QuantityinStock": Quantity,
        "PriceperUnit": Price,
        "ExpiryDate": E_Date
     }

    inventory[P_id] = newproduct
 
    print("Product ID {} added to the inventory".format(P_id))


#display current inventory
def display(inventory):
    for id,value in inventory.items():
        print('-'*40)
        print(id)
        for id2,value2 in value.items():
            print(id2,":",value2)
       

#search for a product
def search_product(p_id):
    print('-'*40)
    print("product id:",p_id)
    print("ProductName:",inventory[p_id]['ProductName'])
    print("ProductCategory:",inventory[p_id]['ProductCategory'])
    print("QuantityinStock:",inventory[p_id]['QuantityinStock'])
    print("PriceperUnit:",inventory[p_id]['PriceperUnit'])
    print("ExpiryDate:",inventory[p_id]['ExpiryDate'])
    print('-'*40)


#update product details
def update_product(inventory,p_id,p_quantity,p_price):
    inventory[p_id]['QuantityinStock']=p_quantity
    inventory[p_id]['PriceperUnit']=p_price
    print("product updated",inventory[p_id])

#delete a product
def delete_product(inventory,prod_to_delete):
    inventory=inventory.pop(prod_to_delete)
    print("The deleted product",inventory)


#calculate total value
def TotalValue(inventory):
    lst=[]
    total=0
    for id in inventory:
        productvalue=inventory[id]['QuantityinStock']*inventory[id]['PriceperUnit']
        lst.append(productvalue)
    #print(lst)
    for value in lst:
        total=total+value
    print("Total value of entire inventory",total)


#menu system
while(True):
    choice=int(input("enter your choice from 1-6: "))
    if choice==1:
        print("add product")
        P_id=int(input('key value of product to be added in inventory '))
        P_Name=input("enter the new product name ")
        P_Cat=input("enter the category of new product ")
        Quantity=int(input("enter the quantity of new product "))
        Price=int(input("enter the price of new product "))
        E_Date=input("enter the date in year-month-date format ")
        addproduct(inventory,P_id,P_Name,P_Cat,Quantity,Price,E_Date)
    elif choice==2:
        print("display inventory")
        display(inventory)
    elif choice==3:
        print("search for a product")
        p_id=int(input("enter the product's key to be searched "))
        search_product(p_id)
    elif choice==4:
        print("update product details")
        p_id=int(input("enter the product key "))
        p_quantity=int(input("enter the updated quantity "))
        p_price=int(input("enter the updated price "))
        update_product(inventory,p_id,p_quantity,p_price)
    elif choice==5:
        print("delete a product")
        p_id=int(input("enter the product's key to be removed "))
        delete_product(inventory,p_id)
    elif choice==6:
        print("calculate total value")
        TotalValue(inventory)
    else:
        print("invalid choice")
    user=input("operation to continue(yes) or stop(no) ")
    if user=='no':
        break
