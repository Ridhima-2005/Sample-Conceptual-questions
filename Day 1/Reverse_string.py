# WAP to reverse a string using 2 pointers

# Time Complexity:- O(n)
# Space Complexity:- O(n)

s = input("Enter a string: ")
lst = list(s)
l = 0 
r = len(lst) - 1
while (l<r):
    lst[l],lst[r] = lst[r],lst[l]
    l+=1
    r-=1
rev = "".join(lst)
print("Reversed string is:",rev)
