num = int(input("digite um numero:  "))
total = 0
for i in range(1, num):
    if num % i == 0:
        print(f' divisor : {i}')
        total += 1

print(f'total de divisores = {total}')