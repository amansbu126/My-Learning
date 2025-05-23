"""
Write a program to retrun a tuple which is exponential of given two
tuples as an input

Example:-
Input: 
    tuple1=(100,2,3,5,6)
    tuple2=(3,6,4,3)
"""
result=()
tuple1=(100,2,3,5)
tuple2=(3,6,4,3)

for i in range(len(tuple1)):
    new=(tuple1[i]**tuple2[i],)
    result=result+new
print(result)