#victoria de paula paschoal - 12021EBI014

def main(): #definindo a função main
    Matriz = []
    for i in range(8): #matriz 8x8
        linha = [(x) for x in input().split()]
        Matriz.append(linha)
    ns = int(input())
    alcance = int(input())
    for j in range (ns): #posição dos sensores
        posicao = [int(x) for x in input().split()]
        analise(Matriz, ns, alcance, posicao) #chamando a função para ler a matriz
        
        
def analise(Matriz, ns, alcance, posicao):
    tesouro = []
    
    for k in range(alcance):
        
        if Matriz[posicao[0]-k][posicao[1]] == "o" or posicao[0]-k>6: #verificando o alcance do sensor para cima
            break
        if Matriz[posicao[0]-k][posicao[1]]== "." or Matriz[posicao[0]-k][posicao[1]] == "v":
            continue
        else:
            tesouro.append(Matriz[posicao[0]-k][posicao[1]])
            Matriz[posicao[0]-k][posicao[1]]== "v"  #pra trocar o x para nenhum sensor achar o mesmo tesouro



            
        if Matriz[posicao[0]+k][posicao[1]] == "o" or posicao[0]+k>6:#verificando o alcance do sensor para baixo
            break
        
        if Matriz[posicao[0]+k][posicao[1]]== "." or Matriz[posicao[0]+k][posicao[1]]== "v":
            continue
        else:
            tesouro.append(Matriz[posicao[0]+k][posicao[1]])
            Matriz[posicao[0]+k][posicao[1]]== "v"


            
        if Matriz[posicao[0]][posicao[1]-k] == "o" or posicao[1]-k>6:#verificando o alcance do sensor para esquerda
            break    
        if Matriz[posicao[0]][posicao[1]-k]== "." or Matriz[posicao[0]][posicao[1]-k] == "v":
            continue

        else:
            tesouro.append(Matriz[posicao[0]][posicao[1]-k])
            Matriz[posicao[0]][posicao[1]-k]== "v"
            
        if Matriz[posicao[0]][posicao[1]+k] == "o" or posicao[1]+k>6:#verificando o alcance do sensor para direita
            break
            
        if Matriz[posicao[0]][posicao[1]+k]== "." or Matriz[posicao[0]][posicao[1]+k] == "v":
            tesouro.append(Matriz[posicao[0]][posicao[1]+k])
            Matriz[posicao[0]][posicao[1]+k]== "v"

            
    print(tesouro)
        


main()
