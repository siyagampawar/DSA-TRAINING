#Approach1 
# def jump(n,temp):
#     if(n==0):
#         print(temp)
#         return
#     if(n<0):
#         return
#     jump(n-1,temp+'1')
#     jump(n-2,temp+'2')
#     jump(n-3,temp+'3')
    

# jump(5,"")

#Approach2 
#different way of handling -ve base case

def jump(n,temp):
    if(n==0):
        print(temp)
        return
    # if(n<0):
    #     return
    if(n-1>=0):
        jump(n-1,temp+'1')
    if(n-2>=0):
        jump(n-2,temp+'2')
    if(n-3>=0):
        jump(n-3,temp+'3')
        
jump(3,"")

