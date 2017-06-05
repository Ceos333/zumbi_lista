controle=True
while controle !=False:
    sal= int(input("informe salario: \n"))
    porcent= float(input("informe a porcentagem do aumento: \n"))
    
    sal_corr = sal*(porcent/100)
    
    
    
    print("O salario de %.2f sofreu o aumento de %.2f. Total %.2f " % (sal, porcent, (sal_corr+sal)))
    
    #controle do laço
    pergunta=input("Deseja fazer nova conversão? \n")
    if pergunta=="sim":
        controle=True
    else:
        controle=False

