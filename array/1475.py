n = int(input())
arr = [0]*10
while n > 0:
	arr[n%10] += 1
	n = n // 10
check = (arr[6] + arr[9])//2 + (arr[6] + arr[9])%2
arr[6] = arr[9] = check
print(max(arr))