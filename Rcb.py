n=int(input())
l=[ ]
c=0
for i in range(n):
      x=int(input())
      l.append(x)

for i in range(n):
         for j in range(2,l[i]+1):
             if l[i]%j==0 or 1%j==0:
                 break
             else:
                 c+=1
print(' count of prime numbers=',c)
