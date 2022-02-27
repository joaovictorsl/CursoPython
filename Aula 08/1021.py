num = float(input())

bill_list = [100, 50, 20, 10, 5, 2]
coin_list = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')

for value in bill_list:
    amount = num // value
    num -= value * amount
    print(f'{amount:.0f} nota(s) de R$ {value:.2f}')

print('MOEDAS:')

for value in coin_list:
    value *= 100
    num *= 100
    amount = num // value
    num -= value * amount
    value /= 100
    num /= 100
    print(f'{amount:.0f} moeda(s) de R$ {value:.2f}')
