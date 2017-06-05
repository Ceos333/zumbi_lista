controle=True
while controle !=False:
    d= int(input("informe os dias: \n"))
    h= int(input("informe horas: \n"))
    mint= int(input("informe minutos: \n"))
    s= int(input("informe segundos: \n"))
    
    tot_s= ((mint*60) + (h*3600) + (d*(24*3600) + s))
    
    print("%d dias %d horas %d minutos e %d segundos são ao todo= %d " % (d,h,mint,s,tot_s))
    
    #controle do laço
    pergunta=input("Deseja fazer nova conversão? \n")
    if pergunta=="sim":
        controle=True
    else:
        controle=False

