#eliminating permutations eliminating repeated values
def jump(n,arr,idx,temp):
    if(n==0):
        print(temp)
        return
    if(n<0):
        return
    for i in range(idx,len(arr)):
        jump(n-arr[i],arr,i,temp+str(arr[i]))
    

arr = [1,2,3]       
jump(4,arr,0,"")

#recirsion ke andar loop hint