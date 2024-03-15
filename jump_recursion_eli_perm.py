#eliminating permutations eliminating repeated values
def jump(n,temp):
    if(n==0):
        
        print(temp)
        return
    # if(n<0):
    #     return
    if(n-arr[0]>=0):
        jump(n-arr[0],temp+'1')
    if(n-arr[1]>=0):
        jump(n-arr[1],temp+'2')
    if(n-arr[2]>=0):
        jump(n-arr[2],temp+'3')

arr = [1,2,3]       
jump(3,"",arr)

#recirsion ke andar loop hint