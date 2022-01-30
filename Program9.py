def checkKey(dict, input_key):
    if input_key in dict.keys():
        print("Present ")
    else:
        print("Not present")

dict = {'a': 100, 'b':200, 'c':300}
input_key = input("Enter the value you want to search :")
checkKey(dict, input_key)
