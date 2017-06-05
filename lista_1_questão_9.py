controle=True
while controle !=False:
    km= int(input("Informe a distancia percorrida em km: \n"))      
    dias= int(input("Dias de viagem: \n"))

    valor= (60.00*dias)+(km*0.15)

    print("Valor total a pagar: %f " % (valor))

    
    #controle do laço
    pergunta=input("Deseja fazer nova operação? \n")
    if pergunta=="sim":
        controle=True
    else:
        controle=False
