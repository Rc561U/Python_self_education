import bl


def show_first_category_page(): 
    return bl.get_first_page()


def show_second_category_page(number,opt=None):
    
    return bl.get_second_page(number)

def show_third_category_page(number1,number2):
    return bl.get_third_page(number1,number2)



def show_product_info(number1,number2,number3):
    try:
        return bl.get_third_page(number1,number2,number3)
    except:
        print(f"That category temporaly is not exist, press 0 to come back")

def format_info(info_tuple):
    return bl.get_format_info(info_tuple)

def add_product(item:tuple):
    bl.add_user_item(item)
    

def show_cart():
    bl.get_cart_data()


def main_flow():
    while True:
        bl.clear
        print(""" Welcom to the shop!
    Enter the number of operation:
    1.Show whole catalog
    2.Show your cart
    3.Exit""")
        operation = int(input("Enter number: "))
        if operation == 1:
            print("0 Come back")
            [print(*i) for i in show_first_category_page()]
            
            user_input_1 = int(input("Press 0 to come back\nChoose the category: "))
            while True:
                second = show_second_category_page(user_input_1)
                #test = bl.get_second_page(user_input_1,True)
                bl.clear()
                print("0 Come back")
                [print(*i) for i in second]
                #print(test)
                
                user_input_2 = int(input("Press 0 to come back\nChoose the category: "))
                if user_input_2 == 0: break
                while True:
                    result = show_third_category_page(user_input_1, user_input_2)
                    [print(*i) for i in result]
                    user_input_3 = int(input("Press 0 to come back\nChoose the item: "))
                    if user_input_3 == 0: break
                    while True:
                        bl.clear()
                        full_prod_info = (show_product_info(user_input_1,user_input_2,user_input_3))
                        print(format_info(full_prod_info))
                        print("\nPress 0 to go back\nPress 1 to add items to the shopping cart")
                        user_input_4 = int(input("Enter to continue: "))
                        
                        if user_input_4 == 0: break
                        if user_input_4 == 1:
                            bl.clear()
                            add_product(full_prod_info)
                            print("You successfully add new item in your cart!\n\nPress 0 to continue\nPress 2 to view shopping cart")
                            user_input_5= int(input("Enter to continue: "))
                            if user_input_5 == 0: break
                        if user_input_4 == 2:
                            show_cart()

        elif operation ==2:
            show_cart()
        elif operation == 3:
            print("Have a nice day!")
            break

if __name__ == "__main__":
    main_flow()