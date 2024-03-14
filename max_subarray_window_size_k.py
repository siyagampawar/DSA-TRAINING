#Approach 1

# import sys
# arr = [100,200,300,400]
# i=0
# k=4
# j=0
# max = -sys.maxsize - 1
# while i+j<=len(arr):
#     j=0
#     sum = 0
#     while j<k:
#         m = int(i+j)
#         sum = sum +arr[m]
#         j = j+1
#     if(sum>max):
#         max =sum
#     i = i+1
        
# print(max)

#Approach 2
# def maximum_subarray(arr,k):
#     l=len(arr)
#     sum1=0
#     max1=0
#     for i in range (k):
#         sum1=sum1+arr[i]
#     j=0
#     max1=max(max1,sum1)
#     for i in range(k,l):
#         sum1=sum1-arr[j]
#         sum1=sum1+arr[i]
#         j=j+1
#         if(sum1>max1):
#             max1=sum1
#         max1=max(max1,sum1)
#     return  max1

# arr = [100,200,300,400]
# k=3
# print(maximum_subarray(arr,k))