controle=True
while controle !=False:
    dist= int(input("Distancia percorrida: \n"))
    vel_med= float(input("Velocidade média: \n"))
    
    temp = dist/vel_med
    
    
    
    print("O Tempo do percurso da distancia %.2f a uma de velocidade %.2f é: %.2f " % (dist, vel_med, (temp)))
    
    #controle do laço
    pergunta=input("Deseja fazer nova operação? \n")
    if pergunta=="sim":
        controle=True
    else:
        controle=False
