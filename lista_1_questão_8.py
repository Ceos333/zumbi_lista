controle=True
while controle !=False:
    print("Escolha a Conversão:")
    print("Celsius para Fahrenheit: 1")
    print("Fahrenheit para Celsius: 2 \n")
    opcao= int(input("\n"))
    if opcao==1:
        C= int(input("Informe a temperatura em Celsius: \n"))

        F = (9*(C/5))+32
    
        print("De Celsius para Fahrenheit: %d º = %d F" % (C, F))
    if opcao==2:

        F= int(input("Informe a temperatura em Fahrenheit: \n"))

        C = 5/9*(F-32)
    
        print("De Fahrenheit para Celsius: %d F = %d º " % (F, C))
    else:
        print("Essa opção não exite \n")      
    
    #controle do laço
    pergunta=input("Deseja fazer nova operação? \n")
    if pergunta=="sim":
        controle=True
    else:
        controle=False
