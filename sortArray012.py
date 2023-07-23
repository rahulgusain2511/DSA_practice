def sortArray(arr, n):
	cnt0=0
	cnt1=0
	cnt2=0
	for i in range (n):
		if arr[i]==0:
			cnt0+=1
		elif arr[i]==1:
			cnt1+=1
		else:
			cnt2+=1
	for i in range (cnt0):
		arr[i]=0
	for i in range (cnt0,cnt0+cnt1):
		arr[i]=1
	for i in range (cnt0+cnt1,n):
		arr[i]=2