somar=True
while somar !=False:
    x= int(input("informe o primeiro número para ser somado: \n"))
    y= int(input("informe o segundo número para ser somado: \n"))
    print("A soma dos dois números é:  %d " % (x+y))


    #controle do laço
    pergunta=input("Deseja fazer nova soma: \n")
    if pergunta=="sim":
        somar=True
    else:
        somar=False

