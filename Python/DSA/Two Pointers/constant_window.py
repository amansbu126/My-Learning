arr = [-1, 2, 3, 3, 4, 5, -1]
k = 4

l = 0
r = k - 1

# Step 1: compute the first window sum
curr_sum = sum(arr[l:r + 1])
max_sum = curr_sum
print(max_sum)
'''
# Step 2: slide the window
while r < len(arr) - 1:
    curr_sum = curr_sum - arr[l]      # remove element going out
    l += 1
    r += 1
    curr_sum = curr_sum + arr[r]      # add new element coming in
    max_sum = max(max_sum, curr_sum)  # update max

print(max_sum)
'''