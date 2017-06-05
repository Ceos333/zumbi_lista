controle=True
while controle !=False:
    fumo_dia= int(input("Quantos cigarros fuma por dia: \n"))      
    fumo_ano= int(input("Por quantos anos você fumou: \n"))
    
    fumo_ano_em_dias=fumo_ano*365
    min_perdido= ((fumo_dia * 10)*fumo_ano_em_dias)
    quando_vai_morrer = (min_perdido/1440)

    print("Você perdeu %f dias de vida " % (quando_vai_morrer))

    
    #controle do laço
    pergunta=input("Deseja fazer nova operação? \n")
    if pergunta=="sim":
        controle=True
    else:
        controle=False
