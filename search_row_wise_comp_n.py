arr = [[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
x  =29

#start from 40 bada number toh niche,chota number toh left

# print(len(arr))
i=0
j=len(arr[0])-1
print(j)
flag = 0

while(i<len(arr) and j>=0):
    start = arr[i][j]
    if start < x :
        i = i+1
        print("less",start)
    elif start > x:
        j = j-1
        print("greater",start)
    elif start == x:
        flag = 1
        break
        
if(flag):
    print("true")
else:
    print(-1)