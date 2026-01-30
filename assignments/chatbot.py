my_money = 50
my_bag = []

shop_products = [
    {
        "name":"Hotdog",
        "category":"food",
        "cost":10
    },
    {
        "name":"Manti",
        "category":"food",
        "cost":20
    },
    {
        "name":"Somsa",
        "category":"food",
        "cost":15
    },
    {
        "name":"Harry Potter",
        "category":"book",
        "cost":25
    },
    {
        "name":"The lord of the rings",
        "category":"book",
        "cost":30
    },
]

def say_hi():
    print("Hello I am your chat bot assistant")

def show_info():
    print("\nI am here to make your shopping easier")
    print("I can show all products, show single product, put it in your bag and buy them for you.")
    print("\nCommands: \n")
    for key in chatbot_data.keys():
        print(key, "\n")
    print("exit\n")

def show_products():
    print("Products: \n")
    for product in shop_products:
        print("name: ", product["name"])
        print("category: ", product["category"])
        print("cost: ", product["cost"], "\n")
    print("\n")

def show_single_product():
    product_inp = input("Which one? ")
    for product in shop_products:
        if product["name"] == product_inp:
            print("\nname: ", product["name"])
            print("category: ", product["category"])
            print("cost: ", product["cost"], "\n")

            ask = input("Do you wnat to put it in bag: ")
            if ask == "Yes":
                add_to_bag(product)

def add_to_bag(item):
    my_bag.append(item)
    print(my_bag)

def show_bag():
    print(my_bag)

def buy_all():
    global my_money
    total = 0
    for item in my_bag:
        total += item["cost"]
    if total < my_money:
        my_money-=total
        my_bag.clear()
    else:
        print("You don't have enough money")

    print("bought")


chatbot_data = {
    "hello":say_hi,
    "What can you do":show_info,
    "Show me products":show_products,
    "Show me this product": show_single_product,
    "Show my bag":show_bag,
    "Buy all of them":buy_all,
}

def run_program():
    running = True
    print("Shop chatbot")
    while running:
        question = input("What do you want to do: ")
        if question in chatbot_data:
            chatbot_data[question]()
        elif question == "exit":
            running = False

run_program()