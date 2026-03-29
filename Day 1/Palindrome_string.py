# WAP to check if a string is Palindrome or not using two pointers. 

s = input("Enter a string: ")
l = 0
r = len(s)-1
isPalindrome = True
while(l<r):
    if (s[l] != s[r]):
        isPalindrome = False
        break
    l+=1
    r-=1
if (isPalindrome == True):
    print("String is Palindrome")
else:
    print("String is not Palindrome")
