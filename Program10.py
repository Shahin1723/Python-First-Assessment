data = {'a': 100, 'b':200, 'c':300}
print(data)
print ("Choose your option") # prints a message
menu = 0 # initializes a variable (menu) of type int to 0
menu =int(input("""
1. ADD
2. MODIFY
"""))
if (menu) == 1:
    key = input("enter the key :")
    value = input("enter the value :")
    data[key] = value
    print(data)
elif (menu) == 2:
    key = input("enter the key you want to update :")
    value = input("enter the value you want to update :")
    del data[key]
    data[key] = value
    print(data)
