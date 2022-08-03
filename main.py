'''
Desenvolva uma função que (mostre na tela o resultado chamando a função e receba o retorno caso haja):
Escreva uma frase qualquer na tela


Receba por parâmetro um nome e mostre na tela: “Bom dia <nome>” sendo <nome> o valor do parâmetro


Receba um número por parâmetro e mostre na tela o seu valor multiplicado por 2.


Receba dois números por parâmetro e mostre na tela a soma deles (dentro da função)


Receba dois números por parâmetro e retorne a sua subtração.


Receba dois textos por parâmetro e retorne a sua união.


Receba um número por parâmetro e retorne True se o número for par e False se for ímpar.

'''


class FazTudo:

    def __init__(self, nome, numero_1, numero_2, texto_1, texto_2):
        self.nome = nome
        self.numero_1 = numero_1
        self.numero_2 = numero_2
        self.texto_1 = texto_1
        self.texto_2 = texto_2

    def frase_qualquer(self):
        return 'Lorem ipsum dolor sit amet'

    def dar_bom_dia(self):
        return f'Bom dia {self.nome}!'

    def multiplicar_por_2(self):
        return self.numero_1 * 2

    def somar(self):
        print(self.numero_1 + self.numero_2)
        return

    def subtrair(self):
        return self.numero_1 - self.numero_2

    def unir_textos(self):
        return self.texto_1 + self.texto_2

    def is_pair(self):
        if self.numero_1 % 2 == 0:
            return True
        else:
            return False


faz_tudo = FazTudo('João', 50, 33, 'Et nulla dolorem sed quis inventore et quibusdam numquam.',
                   'Hic esse dolor sed quod eaque et ratione similique in quam facilis.')

print(faz_tudo.frase_qualquer())
print(faz_tudo.dar_bom_dia())
print(faz_tudo.multiplicar_por_2())
faz_tudo.somar()
print(faz_tudo.subtrair())
print(faz_tudo.unir_textos())
print(faz_tudo.is_pair())





