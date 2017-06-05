controle=True
while controle !=False:
    
    num=2**(10**6)
    cont_num=len(str(num))
    print("2**(10**1) tem %d números " % (cont_num))
    
    
    
    
    #controle do laço
    pergunta=input("Deseja fazer nova operação? \n")
    if pergunta=="sim":
        controle=True
    else:
        controle=False
