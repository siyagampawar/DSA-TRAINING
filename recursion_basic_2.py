def printing(start,end):
    
    if(end<start):
        return
    print(end)
    printing(start,end-1)
    print(end)
    
printing(1,5)