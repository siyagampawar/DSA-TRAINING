def path(i,j,flag,input,temp,count):
    if(i>=len(input) or j>=len(input[0]) or i<0 or j<0 or flag[i][j]==1 or input[i][j]=='X'):
        return count
    # if(flag[i][j]==1 or input[i][j]=='X'):
    #     return
    if(i==len(input)-1 and j==len(input[0])-1):
        flag[i][j] = 1
        count = count+1
        print("===============")
        print(temp)
        for i in range(len(input)):
            for j in range (len(input[0])):
                print(flag[i][j],end="")
            print()
        flag[i][j] = 0
        print("===============")
        #flag = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        return count
     
    flag[i][j] = 1
    count =  + path(i-1,j,flag,input,temp+'U',count)
    count = path(i,j+1,flag,input,temp+'R',count)
    count = path(i+1,j,flag,input,temp+'D',count)
    count = path(i,j-1,flag,input,temp+'L',count)
    flag[i][j] = 0
    return count
    
    
    
flag = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
input = [['O','X','O','O'],['O','O','O','O'],['O','O','X','O'],['X','O','O','O'],['X','X','O','O']]
ans = path(0,0,flag,input,"",0)
print("Total Paths",ans)

#Approachgpt
# def path(i, j, flag, input, temp):
#     if (i >= len(input) or j >= len(input[0]) or i < 0 or j < 0):
#         return
#     if (flag[i][j] == 1 or input[i][j] == 'X'):
#         return
#     if (i == len(input) - 1 and j == len(input[0]) - 1):
#         flag[i][j] = 1
#         print(temp)
#         print(flag)
#         flag[i][j] = 0
#         return

#     flag[i][j] = 1
#     path(i - 1, j, flag, input, temp + 'U')
#     path(i, j + 1, flag, input, temp + 'R')
#     path(i + 1, j, flag, input, temp + 'D')
#     path(i, j - 1, flag, input, temp + 'L')

# flag = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# input = [['O', 'X', 'O', 'O'], ['O', 'O', 'O', 'O'], ['O', 'O', 'X', 'O'], ['X', 'O', 'O', 'O'], ['X', 'X', 'O', 'O']]
# path(0, 0, flag, input, "")
