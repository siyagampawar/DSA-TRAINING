# def is_palin(str):
#     i = 0
#     j = len(str)-1
#     flag = 1
#     while i<=j:
#         if(str[i]==str[j]):
#             return 1
#         else:
#             i+=1
#             j-=1
#             return 0
#             break

# def palindrome_subs(str,alist,listemp):
#     if(len(str)==0):
#         copy = []
#         alist.append(copy)
#         # print(alist)
#         # print(listemp)
#         return
#     for i in range (len(str)):
#         piece = str[:i+1]
#         if(is_palin(piece)):
#             listemp.append(piece)
#             palindrome_subs(str[i+1:],alist,listemp)
#             listemp.pop(len(listemp)-1)
# alist=[]
# temp=[]
# palindrome_subs("aab",alist,temp)
# print(alist)

def is_palin(sub):
    return sub == sub[::-1]

def palindrome_subs(s, alist, listemp):
    if len(s) == 0:
        alist.append(list(listemp))
        return
    for i in range(len(s)):
        sub = s[:i+1]
        if is_palin(sub):
            listemp.append(sub)
            palindrome_subs(s[i+1:], alist, listemp)
            listemp.pop()

alist = []
temp = []
palindrome_subs("aab", alist, temp)
print(alist)


