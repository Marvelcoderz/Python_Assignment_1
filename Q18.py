str1 = str(input ("Enter string 1: "))
str2 = str(input ("Enter string 2: "))
str1 = sorted(str1.lower())
str2 = sorted(str2.lower())
def isAnagram():
    if (str1 == str2) :
        print("The string is anagram")
    else:
        print("The strings are not anagrams.")
print(isAnagram())
