'''
Lucas Martins Primo
12021EBI022
'''

a = float(input())
b = float(input())# Pedido dos pontos flutuantes
c = float(input())

if a == 0:
    print("Impossivel calcular") # Caso a = 0
    
else:
    
    d = (b**2)-(4*a*c) # calculando delta
    if d < 0:
            print("Impossivel calcular") # Caso delta < 0

    else:
        x = (-b + d ** 0.5) / (2 * a)
        xe = (-b - d ** 0.5) / (2 * a) # Calculo das raizes
        
        if x != xe:
            print(f'R1 = %.5f' %(x))
            print(f'R2 = %.5f' %(xe)) # %.5f para formatar as casas decimais

        else:
             print(f'R1 = %.5f' %(x)) # Caso tenha só um caso de teste
                
