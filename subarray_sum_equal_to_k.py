# nums=[1,2,3]
# k=3
# prefix=[0]
# rem={}
# count=0
# for i in nums:
#     prefix.append(prefix[-1]+i)
# for i in prefix:
#     if i//k == 1:
#         count=count+1
# print(count)


# nums=[1,2,3]
# k=3
# prefix=[0]
# rem={0:1}
# count=0
# for i in nums:
#     prefix.append(prefix[-1]+i)
# for i in prefix:
#     sub = i-k
#     if sub in rem:
#          count=count+rem[i]
#          value=rem[sub]+1
#          rem.update({sub:value})
#     else:
#          #adding the key value pair in the dictonary
#         rem[i]=1
# print(count)


nums = [1, 2, 3]
k = 2
prefix = [0]
rem = {0: 1}
count = 0

for i in nums:
    prefix.append(prefix[-1] + i)

for i in prefix:
    sub = i - k
    if sub in rem:
        count += rem[sub]
    if i in rem:
        rem[i] += 1
    else:
        rem[i] = 1

print(count)

