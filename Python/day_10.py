'''Linear Search
Linear search is a sequential searching algorithm where 
we start from one end and check every element of the list 
until the desired element is found. It is the simplest 
searching algorithm.'''
array=[1,2,3,4,5]
n = len(array)
k=3

for i in range(0,n):
    if (array[i]==k):
        print('element found',i)
print('element not found')
