def dulplicates(arr):
    seen=set()
    dupli=[]
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
        else:
            dupli.append(arr[i])
    if len(dupli)==0:
        return -1
    else:
        return sorted(list(dupli))
arr=[1,1,2,2,3,8,1,2,3,4,5,6]
print(dulplicates(arr))