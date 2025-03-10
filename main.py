"""
Lista 1 = Funcionarios que tem carro e trabalham a noite
Lista 2 = Funcionarios que tem carro e trabalham de dia
lista 3 = funcionarios que não tem carro
"""

funcionarios = ['ana', 'marcos', 'alice', 'pedro', 'sophia', 'bruno', 'melissa']
turno_dia = ['ana', 'marcos', 'alice', 'melissa']
turno_noite = ['pedro', 'sophia', 'bruno']
tem_carro = ['marcos', 'alice', 'bruno', 'melissa']

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

lista2 = set(turno_dia).intersection(tem_carro)
print(lista2)

lista3 = set(funcionarios).difference(tem_carro)
print(lista3)