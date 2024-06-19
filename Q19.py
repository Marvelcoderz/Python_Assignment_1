string = input("Enter a string: ")
print("The original string is: ", string)
str1 = ""
for i in string:
    if i not in['.','','!','@','?',':',';','"','_','&','$','*','^','{}','[]','()','~','-']:
        str1 = str1 + i
print("The string after removing all the punctuations from the string: ", str1)