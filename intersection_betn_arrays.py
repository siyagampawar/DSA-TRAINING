arr1 = [1,1,2,3,3,4,4,4,5]
arr2 = [2,2,2,3,3,4,5,6,7]
intersection = []
i=0
j=0
while(i<len(arr1) and j<len(arr2)):
    if(arr1[i]<arr2[j]):
        i+=1
    elif (arr1[i]>arr2[j]):
        j+=1
    else:
        intersection.append(arr1[i])
        i+=1
        j+=1
 
print(intersection)   