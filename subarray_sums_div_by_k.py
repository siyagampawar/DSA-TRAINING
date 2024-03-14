# nums = [4,5,0,-2,-3,1]
# count = {0:1}
# sum = 0
# rem = 0
# p = 0
# k=5
# for i in nums :
#     sum = sum+i
#     rem = (sum % k+k) % k
#     if rem in count:
#         p = p+ count[rem]
#     else:
#         count[rem] = 1
        
#     count[rem] = count[rem]+1

# print(p)


#Approach
nums=[4,5,0,-2,-3,1]
k=5
prefix=[0]
rem={}
count=0
for i in nums:
    prefix.append(prefix[-1]+i)
for i in prefix:
    if i%k in rem:
        count=count+rem[i%k]
        value=rem[i%k]+1
        rem.update({i%k:value})
    else:
        #adding the key value pair in the dictonary
        rem[i%k]=1
print(count)
