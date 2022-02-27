# Baseado em respostas de um colega, decida se ele vai ou não jogar.
# Perguntas:
# Você está machucado?
# Você quer jogar?
# O colega só irá jogar se ele quiser e não estiver machucado
# S / N
ta_machucado = input('Você está machucado? ')
quer_jogar = input('Você quer jogar? ')

if quer_jogar == 'S' and not ta_machucado == 'S':
    print('Então, venha jogar.')
else:
    print('Acho melhor você não jogar.')
