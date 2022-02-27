# POO = Programação Orientada a Objetos
# É uma maneira da gente trazer os objetos do mundo real para o nosso código

# Pessoa
# Nome
# Idade

# Pessoa(nome, idade)


class Pessoa():

    def __init__(self, nome: str, idade: int, altura: float, fertil: bool) -> None:
        # Atributo de um objeto
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.fertil = fertil
        self.amigos = {}

    # Métodos
    def falar_oi(self):
        print(f'Oi, eu sou o {self.nome}')

    def expressar_saudade(self, outra_pessoa):
        print(f'Eu, {self.nome}, estou com saudades de {outra_pessoa.nome}')

    def fazer_amizade_com(self, outra_pessoa):
        self.amigos[outra_pessoa.nome] = outra_pessoa
        outra_pessoa.amigos[self.nome] = self

    def __add__(self, outra_pessoa):
        if not (self.fertil and outra_pessoa.fertil):
            raise ValueError(
                'As duas pessoas devem ser férteis para que a reprodução aconteça.')

        altura = (self.altura + outra_pessoa.altura) / 2
        return Pessoa(self.nome + outra_pessoa.nome, 0, altura, True)

    def __gt__(self, outra_pessoa):
        return self.altura > outra_pessoa.altura

    def __repr__(self) -> str:
        return f'Nome: {self.nome}\nIdade: {self.idade}\nAltura: {self.altura}\nFértil: {self.fertil}\nAmigos: {list(map(lambda chave: chave, self.amigos))}'


pessoax = Pessoa('X', 20, 1.90, True)
pessoay = Pessoa('Y', 19, 1.80, False)

pessoay.fazer_amizade_com(pessoax)

bebe = pessoay + pessoax

pessoay.fazer_amizade_com(bebe)

print(pessoay)
