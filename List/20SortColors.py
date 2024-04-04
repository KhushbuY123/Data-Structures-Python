def sort012(arr,n):
        l=0
        m=0
        r=len(arr)-1
        i=0
        while(m<=r):
            if arr[m]==0:
                arr[m],arr[l]=arr[l],arr[m]
                m+=1
                l+=1
            elif arr[m]==1:
                m+=1
            else:
                arr[m],arr[r]=arr[r],arr[m]
                r-=1
        return arr
n=7
arr=[0,1,2,2,0,1,1]
print(sort012(arr,n))