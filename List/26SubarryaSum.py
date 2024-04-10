# A simple program to print subarray with sum as given sum
def subArraySum(arr, n, sum):
	maxlen=0
	for i in range(0,n):
		new_sum = arr[i]
		if(new_sum == sum):
			print(arr[i])
		else:
			for j in range(i+1,n):
				new_sum += arr[j]
				if(new_sum == sum):
					maxlen=max(len(arr[i:j+1]),maxlen)
	print(maxlen)
arr = [2,2,4,1,2]
n = len(arr)
sum = 2
subArraySum(arr, n, sum)








                