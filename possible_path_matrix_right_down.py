def path(dest_row,dest_col,temp,i,j):
    if (dest_row == i and dest_col==j):
        print(temp)
        return
    # if i>dest_row:
    #     return
    # if j>dest_col:
    #     return
    #or
    if i>dest_row or j>dest_col:
         return

    path(dest_row,dest_col,temp+"R",i,j+1)
    path(dest_row,dest_col,temp+"D",i+1,j)

path(2,2,"",0,0)