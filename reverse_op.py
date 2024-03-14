def reverse(str):
    temp = ""
    for i in range(len(str)):
        temp+=str[-1-i]
    return(temp)

def operation(s,op,arr):
    # middle = ""
    for i in range (op):
        val = len(s)-arr[i]+1
        if(arr[i]<val):
            s = s[:arr[i]] + reverse(s[arr[i]:val]) + s[val:]
            # middle = reverse(str[arr[i]][val])
        else:
            s = s[:val] + reverse(s[val:arr[i]]) + s[arr[i]:]
            # middle = reverse(str[val][arr[i]])
        print(s)
    return s

# str = "vwxyz"
str = "siyagampawar"
op = 2
arr = [2, 2]  # Indices to perform operations on
result = operation(str, op, arr)
print("Ans:",result)  
# Output: "aebcdfg"
# def reverse_substring(s, start, end):
#     return s[:start] + s[start:end+1][::-1] + s[end+1:]

# def operation(s, op, arr):
#     for i in range(op):
#         start = arr[i]
#         end = len(s) - arr[i] + 1
#         if start <= end:
#             s = reverse_substring(s, start, end)
#         else:
#             s = reverse_substring(s, end, start)
#         print(s)
#     return s

# # Example usage:
# s = "abcdefg"
# op = 2
# arr = [1, 4]  # Indices to perform operations on
# result = operation(s, op, arr)
# print(result)  # Output: "aebcdfg"
# #afdcbeg