# arr = [3,-1,5,-100,4,2]
# i=0
# j=1
# sum =0
# max = 0
# while(i<len(arr)):
#     sum = arr[i]
#     # print ("sum",sum)
#     j=i+1
#     while(j<len(arr)):
#         # print("j",j)
#         sum = sum+arr[j]
#         if(sum>max):
#             max = sum
#         j +=1
#     i+=1
# print(max)

# Approach 2
# import sys
# arr = [3,-1,5,-100,4,2]
# i=0
# sum =-sys.maxsize-1
# current_sum = 0

# for i in range(len(arr)):
#     current_sum = max(current_sum+arr[i],arr[i])
#     sum = max(sum,current_sum)

# print(sum)

#Approach 3
import sys
arr = [3,-1,5,-100,4,2]
sum1=0
max1 = -sys.maxsize-1
for i in range(len(arr)):
    sum1 = sum1 + arr[i]
    if(sum1>max1):
        max1 = sum1
    if(sum1<0):
        sum1 = 0
print(max1)



