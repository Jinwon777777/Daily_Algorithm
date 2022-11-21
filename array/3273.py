n = int(input())
arr = list(map(int, input().split()))
x = int(input())
chk_lst = [0]*2000001
ans = 0

for i in arr:
	chk_lst[i] += 1

for j in range(1, (x+1)//2):
	if chk_lst[j] == 1 and chk_lst[x-j] == 1:
		ans+=1
print(ans)

#### 투포인터 방법

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()

left = 0
right = n-1
count = 0

while left < right:
	if arr[left] + arr[right] == x:
		count+=1
		left += 1
	elif arr[left] + arr[right] > x:
		right-=1
	else:
		left += 1
print(count)
