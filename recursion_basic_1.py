def printing(start,end):
    
    if(start>end):
        return
    print(start)
    printing(start+1,end)
    print(start)
    
printing(1,5)