import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']

print("Welcome to the pypassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"how many symbols would you like?\n"))
nr_numbers = int(input(f"how many numbers would you like?\n"))

#Easy level
#Generate password components
password_letters = [random.choice(letters) for _ in range(nr_letters)]
password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]


#combine all components
password_list = password_letters + password_symbols + password_numbers

#shuffle the combined list
random.shuffle(password_list)
#convert list to string
password = ''.join(password_list)

#Display the password
print(f"\nYour generated password is : {password}")