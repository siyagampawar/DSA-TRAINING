def subPrint(i, str1, temp):
    if i == len(str1):
        print(temp)
        return
    subPrint(i + 1, str1, temp=temp + str1[i])  # Include current character
    subPrint(i + 1, str1, temp=temp+str1(ord(str1[i])))# Exclude current character
    subPrint(i + 1, str1, temp=temp)

subPrint(0, "abc", "")