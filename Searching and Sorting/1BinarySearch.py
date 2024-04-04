def binary_search(l, start, end, k):
    if start <= end:
        mid = (start + end) // 2
        if l[mid] == k:
            return mid
        elif l[mid] > k:
            return binary_search(l, start, mid - 1, k)
        else:
            return binary_search(l, mid + 1, end, k)
    return -1

l = [3, 4, 56, 388, 450]
k = 388
index_of_binary_search = binary_search(l, 0, len(l) - 1, k)
if index_of_binary_search == -1:
    print("Not found")
else:
    print("Target found at index:", index_of_binary_search)


        

