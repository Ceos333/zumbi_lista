controle=True
while controle !=False:
    C= int(input("Informe a temperatura em Celsius: \n"))

    F = (9*(C/5))+32
    
    print("De Celsius para Fahrenheit: %d = %d " % (C, F))
    
    #controle do laço
    pergunta=input("Deseja fazer nova operação? \n")
    if pergunta=="sim":
        controle=True
    else:
        controle=False
