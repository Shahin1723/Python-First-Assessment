data_input = input("Enter the word : ")
lower_count = 0
upper_count = 0
for i in data_input:
    if(str(i) == str(i).lower()):
        lower_count = lower_count + 1
    else:
        upper_count = upper_count + 1

print("Upper Cases are",upper_count)
print("Lower Cases are",lower_count)
