# draco
try:
    draco = (input('Deseja calcular o Draco ou Darksteel?')).lower()
    if draco== "draco":
        draco = float(input('Entre valor Draco: '))
        dracon = float(input('Quantos dracos possui: '))
        dolar = float(input('Valor Dolar: '))
        dracov = dracon * (dolar * draco)
        porcentagem = dracov * 1.7 / 100
        resultado = dracov - porcentagem
        print("Sem taxa:",dracov)
        print("Com taxa:%.2f" %resultado)
    elif draco== "darksteel":
        print('Calculando valor do Draco para Darksteel')   
        draco = float(input('Entre quantos Dracos: ')) 
        darksteel = 104.921 * draco 
        perdeu= (draco * 105.921) - darksteel
        print("Darksteel:",darksteel)
        print("Perdeu:",perdeu) 
    else:
        print("Digite draco ou darksteel")
except ValueError:
    print('Valor Inválido')
input('Pressione ENTER para sair...')