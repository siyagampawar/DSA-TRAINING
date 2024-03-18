# Approach 1
# string1  ="ababc"
# temp = ""
# i=0
# for i in range(len(string1)):
#     temp+=string1[-1-i]
    
# if(string1 == temp):
#     print("palindrome")
# else:
#     print("not a palindrome")

# Approach 2
string1  ="abcaba"
i = 0
j = len(string1)-1
flag = 1
while i<=j:
    if(string1[i]==string1[j]):
        i +=1
        j-=1
        flag = 1
    else:
        flag = 0
        break

if(flag):
    print("String is palindrome")
else:
    print("String is not Palindrome")
    
#starting ending palindrome pointers 