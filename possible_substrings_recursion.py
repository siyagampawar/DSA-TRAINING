#question 1
# def subPrint(i, str, temp):
#     if i == len(str):
#         print(temp)
#         return
#     subPrint(i + 1, str, temp=temp + str[i])  # Include current character
#     subPrint(i + 1, str, temp=temp)  # Exclude current character

# subPrint(0, "abcd", "")


#maintain index

#ascii value ke saath 3 recursie calls 
#question2
def subPrint(i, str1, temp):
    if i == len(str1):
        print(temp)
        return
    subPrint(i + 1, str1, temp=temp + str1[i])  # Include current character
    subPrint(i + 1, str1, temp=temp+str(ord(str1[i])))# Exclude current character
    subPrint(i + 1, str1, temp=temp)

subPrint(0, "abc", "")

#Approachgpt
# def subPrint(i, string, temp):
#     if i == len(string):
#         print(temp)
#         return
#     subPrint(i + 1, string, temp=temp + string[i])  # Include current character
#     subPrint(i + 1, string, temp=temp + str(ord(string[i])))  # Exclude current character
#     subPrint(i + 1, string, temp=temp)

# subPrint(0, "abc", "")

