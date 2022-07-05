import requests
import data
import os
import re



def prepatate_str(st):
	if isinstance(st,list):
		st = st[0][0]
		return st.split('/')[-2]
	return st.split('/')[-2]

def clear():
	try: return os.system("clear")
	except: return os.system("cls")

def get_first_page():
	return data.use_database()


def get_second_page(number,tag=False):
	qi_tuple = {}
	links_dict ={}
	lst = data.use_database(number)
	for ide,title,link in lst:
	
		qi_tuple[ide]=title
		links_dict[ide]=link	
	if tag: return links_dict
	return qi_tuple.items()



def get_third_page(previousN,currentN,info=None):
	links_dict = (get_second_page(previousN,True))
	table_name = prepatate_str( links_dict[currentN])
	
	short_info_dict = {}
	full_info_dict = {}
	query_result = data.use_database(currentN,table_name)
	for id,name,art,price in query_result:
		short_info_dict[id]=name
		full_info_dict[id]=name,art,price

	if not info:
		return short_info_dict.items()
	else:
		return full_info_dict[info]


def get_format_info(info:tuple)->str:
	if isinstance(info, tuple):
		name,art,price = info
		return f"Название продукта: {name}\n{art}\nЦена: {replace_price(price)} руб./шт"
	return "Your data is not a tuple"

		
def add_user_item(item:tuple):
	name,art,price = item
	price = replace_price(price)
	item = (name,art,price)
	data.write_user_cart((name,art,price))
	# try:
	# 	data.write_user_cart((name,art,price))
	# except:
	# 	print("bl add_user_item is not work correctly")

def replace_price(price):
	new_price = re.search("^[\d\.]*",price)
	return float(new_price.group(0))


def get_cart_data():
	# query_result = data.read_user_cart()
	while True:
		
		try:
			clear()
			query_result = data.read_user_cart()
			for id,name,art,price in query_result:
				
				print(f"Продукт №{id}\nНазвание:{name}\n{art}\nЦена: {price} руб./шт\n")
			print(f'Shopping Cart Total Price is {get_price()}\n')
			user_inp = int(input("1. to pay all items\n2. to delete one or all items\n0. to close the cart\nEnter to continue: "))
			if user_inp==0:break
			elif user_inp==1:
				clear()
				print("You have successfully paid your order! ")
				user_inp = (input("Enter to continue: "))
			elif user_inp==2:
				
				user_del = input("\nPress 0 to come back\nEnter number of item which you want to delete or type 'all' to delete all entries: ")
				clear()
				if user_del == 'all':
					data.delete_all_items()
				elif user_del.isdigit() and user_del!=0:
					data.delete_user_item(int(user_del))
				
				elif user_del == 0:
					continue
		except:
			clear()
			ent = input("Your cart is empty! Press enter to continue: ")
			break


def get_price():
	result = float(data.read_cart_price()[0][0])
	return round(result,2)


def delete_item(num):
	return 



