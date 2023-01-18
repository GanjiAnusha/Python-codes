#prime mail reads
def countPrimes(n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            primes[i*i:n:i]=[False]*len(primes[i*i:n:i])
    return sum(primes)
m=int(input())
count=0
for i in range(m):
    if(m==2):
        break
    l=countPrimes(m)
    m-=l
    count+=1
count+=1
print(count)
