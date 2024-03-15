#question 1
def subPrint(i, str, temp):
    if i == len(str):
        print(">",temp)
        return
    subPrint(i + 1, str, temp=temp + str[i])  # Include current character
    subPrint(i + 1, str, temp=temp)  # Exclude current character

subPrint(0, "abc", "")