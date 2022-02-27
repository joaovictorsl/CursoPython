class Animal():
    def __init__(self, cor: str, qnt_patas: int, rabo: bool, penas: bool, sexo: str, tamanho_do_rabo: float = 5) -> None:
        self.cor = cor
        self.qnt_patas = qnt_patas
        self.rabo = rabo

        if self.rabo:
            self.tamanho_do_rabo = tamanho_do_rabo
        else:
            self.tamanho_do_rabo = 0

        self.penas = penas
        self.sexo = sexo

    def comer(self):
        print('Estou comendo')

    def dormir(self):
        print('Estou dormindo')

    def defecar(self):
        print('Estou defecando')

    def respirar(self):
        print('Estou respirando')

    def comunicar(self):
        print('Roaaar')

# Herança


class Gato(Animal):
    def __init__(self, cor: str, qnt_patas: int, rabo: bool, sexo: str, tamanho_do_rabo: float = 5) -> None:
        super().__init__(cor, qnt_patas, rabo, False, sexo, tamanho_do_rabo)

    def comunicar(self):
        print('Miau Miau')

    def brincadeira_de_cachorro(self):
        print('Estou brincando como um cachorro')


class Cachorro(Animal):
    def __init__(self, cor: str, qnt_patas: int, rabo: bool, sexo: str, tamanho_do_rabo: float = 5) -> None:
        super().__init__(cor, qnt_patas, rabo, False, sexo, tamanho_do_rabo)

    def brincadeira_de_cachorro(self):
        print('Estou brincando como um cachorro')

    def comunicar(self):
        print('Au Au')


animal = Animal('Preto', 4, True, False, 'Macho')
cachorro = Cachorro('Preto', 4, True, 'Macho')
gato = Gato('Branco', 4, True, 'Fêmea')

animal.comunicar()
cachorro.comunicar()
gato.comunicar()
