num = int(input("Enter a number: "))
factorial = 1
if num>=1:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of the number is: ",factorial)
else:
    print("Please enter a valid number!!!")