import sys
nums = [3,-1,5,-100,4,2]
sum1=0
min1 = sys.maxsize+1
for i in range(len(nums)):
    sum1 = sum1 + nums[i]
    if(sum1<min1):
        min1 = sum1
    if(sum1>0):
        sum1 = 0
    # print(min1)

sum2=0
max1 = -sys.maxsize-1
for i in range(len(nums)):
    sum2 = sum2 + nums[i]
    if(sum2>max1):
        max1 = sum2
    if(sum2<0):
        sum2 = 0
    # print(max1)

act_sum=0
for i in range(len(nums)):
    act_sum = act_sum + nums[i]

max_case1 = act_sum - min1

    # print(act_sum)
if (max1<0):
    print(max1)
else:
    print(max(max_case1,max1))

        
                
