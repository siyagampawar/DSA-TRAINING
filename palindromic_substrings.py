# Approach 1 (n3)


#Approach 2:

# def countSubstrings(s):
#         ans = 0
#         for i in range (len(s)):
#             ans = ans+ grow(s,i,i)
#             ans = ans + grow(s,i,i+1)
#         print(ans)

# def grow(str,left,right):
#     count  =0
#     while(left>=0 and right<len(str)):
#         if(str[left]==str[right]):
#             count+=1
#             left-=1
#             right+=1
#         else:
#             break
        

#     return count

# str = "aaa" 
# countSubstrings(str)

#Approach3
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         def isPalindrome(left, right):
#             if left >= right:
#                 return True
#             if s[left] != s[right]:
#                 return False
#             return isPalindrome(left + 1, right - 1)
        
#         n = len(s)
#         count = 0
#         for i in range(n):
#             for j in range(i, n):
#                 if isPalindrome(i, j):
#                     count += 1
#         return count