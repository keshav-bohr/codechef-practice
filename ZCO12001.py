n = int(input())

a = list(map(int, input().split(' ')))

counter = 0
maxSymbol = 0

for i in range(n):
    if(a[i] == 1):
        counter = counter + 1
        maxSymbol = counter if maxSymbol < counter else maxSymbol
    else:
        counter = counter - 1