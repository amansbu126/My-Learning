"""
Write a program to return entire element as a tuple which can have a list 
in the tuple inputs.

Input: test_tuple =([5,6],[6,7,8,9],[3])
Output: (5,6,6,7,8,9,3)
Also talk about the time and space complexity
"""
result=()
test_tuple =([5,6],[6,7,8,9],[3])
for i in test_tuple:
    new_var=tuple(i)
    result=result+new_var
print(result)


#time complexity = O(n)
#space complexity = o(n)