s=input()
hash=[]
for i in range(26):
    hash.append(0)
for i in range(len(s)):
    hash[ord(s[i])-97]+=1

q=int(input())
while q>0:
    f=input()
    print(hash[ord(f)-97],sep="")
    q=q-1
print()