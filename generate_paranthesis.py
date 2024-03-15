
#all possible combinations
# # def paranthesis(n,temp,i,list):
#     if(i==2*n):
#         list.append(temp)
#         print(temp)
#     if(i>2*n):
#         return
#     paranthesis(n,temp +"(",i+1,list)
#     paranthesis(n,temp +")",i+1,list)
    
# paranthesis(3,"",0,[])

def paranthesis(n,temp,open,close,list):
    if(open == close == n):
        list.append(temp)
        print(temp)
        return
    if(open>n or close>open):
        return
    
    paranthesis(n,temp +"(",open+1,close,list)
    paranthesis(n,temp +")",open,close+1,list)
    
paranthesis(3,"",0,0,[])

#valid paranthesis
# def parentheses(n, temp, open_count, close_count, result):
#     if len(temp) == 2 * n:
#         result.append(temp)
#         print(temp)
#         return
    
#     if open_count < n:
#         parentheses(n, temp + "(", open_count + 1, close_count, result)
#     if close_count < open_count:
#         parentheses(n, temp + ")", open_count, close_count + 1, result)

# result = []
# parentheses(3, "", 0, 0, result)
