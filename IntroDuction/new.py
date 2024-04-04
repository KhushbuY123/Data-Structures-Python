def FindMaxSum(a):
        sum=0
        res=0
        for i in range(0,len(a),2):
            sum+=a[i]
            if sum>res:
                res=sum
            else:
                sum=0
        return res
a=[1,5,3,5]
print(FindMaxSum(a))