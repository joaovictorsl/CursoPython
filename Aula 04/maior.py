# Após receber três números inteiros da entrada diga qual o maior entre eles.

num1 = int(input())
num2 = int(input())
num3 = int(input())

maior = None

if num1 >= num2:
    if num1 >= num3:
        maior = num1
    else:
        maior = num3
else:
    if num2 >= num3:
        maior = num2
    else:
        maior = num3

print(f'{maior} é o maior.')
