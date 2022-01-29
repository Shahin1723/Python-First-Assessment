def factorial(num):
  if (num==1 or num==0):
      return 1
  else:
    return (num * factorial(num - 1))

num = int(input("Enter you number to check :"))
print("Entered number is: ",num)
print("Factorial is : ",factorial(num))
