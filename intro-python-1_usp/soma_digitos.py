n = int(input())
soma = 0

while n != 0:
    x = n%10
    n = n//10
    soma += x

print(soma)
