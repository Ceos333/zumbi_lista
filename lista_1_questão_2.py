converter=True
while converter !=False:
    mm= int(input("informe o número em Milimetro para ser convertio: \n"))

    print("O valor de  %d  em metros é: %.4f" % (mm,mm/1000))


    #controle do laço
    pergunta=input("Deseja fazer nova conversão? \n")
    if pergunta=="sim":
        converter=True
    else:
        converter=False

