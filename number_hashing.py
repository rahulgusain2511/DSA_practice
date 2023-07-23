n=int(input("Number of elements in array :"))

arr=[]
for i in range(n):
    element=int(input("Print element : "))
    arr.append(element)

hash=[]
for i in range(13):
    hash.append(0)
for i in range(n):
    hash[arr[i]]+=1

q=int(input())
while q>0:
    number=int(input())
    print(hash[number],sep="")
    q=q-1
print()