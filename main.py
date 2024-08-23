#funções progressão geometrica
#lambda e lista
calcular_pg = lambda x: x*2



numeros =[1,2,3,4,5,6,7,8,9]


pg = list(map(calcular_pg,numeros))

# exibe na tela alista 
for  i in pg:
    print(i)
