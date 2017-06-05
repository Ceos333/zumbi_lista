controle=True
while controle !=False:
    preco= int(input("O preçoa da mercardoria: \n"))
    descon= float(input("Informe o desconto: \n"))
    
    valor = preco*(descon/100)
    
    
    
    print("O Preço de %.2f sofreu o desconto de %.2f. Total %.2f " % (preco, descon, (preco-valor)))
    
    #controle do laço
    pergunta=input("Deseja fazer nova operação? \n")
    if pergunta=="sim":
        controle=True
    else:
        controle=False
