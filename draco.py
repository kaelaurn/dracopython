# draco
try:
    draco = float(input('Entre valor Draco: '))
    dracon = float(input('Quantos dracos possui: '))
    dolar = float(input('Valor Dolar: '))
    dracov = dracon * (dolar * draco)
    porcentagem = dracov * 1.7 / 100
    resultado = dracov - porcentagem
    print("Sem taxa:",dracov)
    print("Com taxa:",resultado)
except ValueError:
    print("Valor inválido!")
input('Pressione ENTER para sair...')
