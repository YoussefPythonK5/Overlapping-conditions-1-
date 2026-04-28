# nested if
drink = input("What would you like to drink ? (coffee/tea) : ")

if drink == "coffee":
	sugar =input("Do you it black or with sugar ? : ")
	if sugar =="black":
		print("Black Coffee")
	elif sugar =="with sugar":
		print("Nice Coffee With Suger")
	else:
		print("Sorry")
elif drink == "tea":
	type_of_tea = input("Green tea or Red tea : ")
	if type_of_tea == "Green":
		print ("Green tea")
	elif type_of_tea == "Red":
		print ("Red tea")
	else:
		print ("Sorry")
else:
	print ("Sorry")