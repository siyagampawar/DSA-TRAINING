#Approach 1
nums=[1,2,3]
k=3
rem={0:1}
count=0
sum= 0
sub = 0
# for i in nums:
#     prefix.append(prefix[-1]+i)
# print(prefix)
for i in nums:
    sum = sum+i
    sub = sum-k
    if sub in rem:
        count=count+rem[sub]
        
    if sum not in rem:
        rem[sum]=1
    else:
        rem[sum] =rem[sum]+1
print(count)