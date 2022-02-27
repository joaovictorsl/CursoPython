# Compreensão de listas
# List Comprehension

# num_list = input().split()

# for idx in range(len(num_list)):
#     num_list[idx] = int(num_list[idx])

a, b, c, d = [int(num) for num in input().split()]

# A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a
# soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem
# "Valores aceitos", senão escrever "Valores nao aceitos".

if b > c and d > a and c + d > a + b and c >= 0 and d >= 0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
