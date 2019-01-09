t = int(input())
import math

def checkForPrime(num):
    cnt = 0
  
    for i in range(2, int(math.sqrt(num)) + 1): 
        while num % i == 0: 
            num /= i 
            cnt += 1 
  
        if cnt >= 2:  
            break

    if(num > 1): 
        cnt += 1
  
    # Return '1' if count is equal to '2' else 
    # return '0' 
    return cnt == 2

def checkForSum(n):
    for i in range(2, n-2):
        a = checkForPrime(i)
        b = checkForPrime(n-i)
        if(a and b ):
            print('YES')
            return
    else:
        print('NO')

for i in range(t):
    n = int(input())
    checkForSum(n)
