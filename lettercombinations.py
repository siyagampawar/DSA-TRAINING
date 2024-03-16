# #17 leetcode

# def comb(string,temp,dictionary):
#     if(len(string)==0):
#         print(temp)
    
#     v = dictionary.get(string[0])
    
#     for i in range (len(v)):
#         comb(string-string[0],temp+v[i],dictionary)
        
# dict1 = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
# comb("23","",dict1)
# print(len(dict1.get(2)))

#Approach1
# def comb(string, temp, dictionary):
#     if len(string) == 0:
#         print(temp)
#         return  # Don't forget to return to avoid unnecessary recursion

#     digit = int(string[0])  # Convert the character to an integer
#     v = dictionary.get(digit)

#     if v is None:
#         return  # If the digit is not found in the dictionary, return

#     for char in v:
#         comb(string[1:], temp + char, dictionary)  # Pass the substring to the recursive call

# dict1 = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
# comb("23", "", dict1)

#Approach2
def comb(index,string, temp, dictionary,alist):
    if index == len(string):
        # print(temp)
        alist.append(temp)
        return
     
    digit = int(string[index])  # Convert the character to an integer
    v = dictionary.get(digit)

    # if v is None:
    #     return  # If the digit is not found in the dictionary, return
    for char in v:
        comb(index+1,string, temp + char, dictionary)  # Pass the substring to the recursive call

dict1 = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
comb(0,"23", "", dict1)
# print(alist)
#list wala implement karna
