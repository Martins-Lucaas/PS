"""
Lucas Martins Primo
12021EBI022
"""
def main():
    plataforma = [int(i) for i in input().split()]
    i = int(input())
    print(i) #print da posicao inicial
    plataformas_visitadas = [] #lista criada para a resolucao
    plataformas_repetidas = [] #lista para armazernar posição repetida
    posicao(i, plataforma, plataformas_visitadas, plataformas_repetidas) #chamada da funcao posicao

def posicao(i, plataforma, plataformas_visitadas,plataformas_repetidas):
    pos = i
    
    
    if pos > len(plataforma): # se a primeira posicao cair da lista pela direita
        print("direita")
        return # O programa para depois disso
    elif pos < 1:
        print ("esquerda")# se a primeira posicao cair da lista pela esquerda
        return # O programa para depois disso
    
    else: #Se nao cair vai continuar o programa
    
    
        for j in range (len(plataforma)):
            pos1 = pos
            pos = pos + plataforma[pos-1] #calculo de cada posicao
            plataformas_visitadas.append(pos)#Colocando todos os valores de posicoes dentro de uma nova lista plataformas_visitad
            
            if pos > len(plataformas_visitadas) or pos < 0: #Retira posicoes invalidas da lista de visitados
                plataformas_visitadas.remove(pos) 
                
            if pos < 1: # Sendo posicao < 1 indica que ele saiu da lista pela esquerda
                print("esquerda")
                break #finalza o loop


            if pos > len(plataforma): # Sendo posicao> 1 indica que ele saiu da lista pela direita
                print("direita")
                break #finalza o loop

        
            if pos != i and pos not in plataformas_repetidas: # adiciona valores repetidos nas plataformas repetidas para não entrarem no loop
                plataformas_repetidas.append(pos)

            
            else: # caso não se encaixe en nenhuma das condicoes acima sera loop pois, nao saiu da plataforma ou seja esta em loop dentro dela
                print("loop")
                break #finalza o loop

        
            print(pos)
main()
