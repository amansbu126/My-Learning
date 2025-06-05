arr = [-1, 2, 8, 1]

# Filter non-negative numbers
new_list = [num for num in arr if num >= 0]

# Compute count and average
cnt = len(new_list)
res = sum(new_list)

# Avoid division by zero
average = res / cnt if cnt > 0 else 0

print(f"Filtered List: {new_list}")
print(f"Count: {cnt}")
print(f"Average: {average}")