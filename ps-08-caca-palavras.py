"""
Lucas Martins Primo
12021EBI022
"""

def main():
    
    l = int(input()) #tamanho das linhas
    c = int(input()) #tamanho das colunas
    joguinho = [] 

    
    #Recebe a matriz do joguinho
    for i in range(l):
        linha = []
        linha = [str(x) for x in input().split()]
        
        joguinho.append(linha)
        
    #Recebe as palavras    
    joguinho2 = joguinho
    n = int(input())
    palavras = []

    print("----------------------------------------")#Inicio do print
    print("Lista de Palavras") #Ainda inicio do print
    
    for i in range(n):
        palavras.append(input()) #Pega as palavras do usuario e coloca na lista 
        
    encontre(l, c, joguinho, n, palavras, joguinho2)#Executando este trecho para cada palavra


def encontre(l, c, joguinho, n, palavras, joguinhoAux):

    #Verifica cada palavras, pelo numero de letrinhas
    for letrinhas in palavras:
        soma=0 # Variavrel para contar tudo direitinho
        a = len(letrinhas) #Facilitar para nao colocar len em tudo
        #Percorre toda a matriz
        for i in range(l):
            for j in range(c):
                if letrinhas == letrinhas[::-1]:#Verifica se é palindromo
                    if horizontais(l, c, joguinho, i, j, letrinhas, a) == True: #Va para def horizontal
                        soma+=1 #Se todas as condicoes forem cumpridas vai acrescentar +1
                        for k in range(a):
                            joguinhoAux[i][j+k] = joguinhoAux[i][j+k].upper() #Coloca em maiusculo 
                else:
                    if horizontais(l, c, joguinho, i, j, letrinhas, a) == True: #Va para def horizontal
                        soma+=1 #Se todas as condicoes forem cumpridas vai acrescentar +1
                        for k in range(a):
                            joguinhoAux[i][j+k] = joguinhoAux[i][j+k].upper()
                    elif horizontais2(l, c, joguinho, i, j, letrinhas, a) == True: #Va para def horizontal2
                        soma+=1 #Se todas as condicoes forem cumpridas vai acrescentar +1
                        for k in range(a):
                            joguinhoAux[i][j-k] = joguinhoAux[i][j-k].upper()#Coloca em maiusculo 
                    
                if letrinhas == letrinhas[::-1]: #Verifica se é palindromo
                    if verticais(l, c, joguinho, i, j, letrinhas, a) == True: #Va para def verticais
                        soma+=1 #Se todas as condicoes forem cumpridas vai acrescentar +1
                        for k in range(a):
                            joguinhoAux[i+k][j] = joguinhoAux[i+k][j].upper()#Coloca em maiusculo 
                else:
                    if verticais(l, c, joguinho, i, j, letrinhas, a) == True: #Va para def verticais
                        soma+=1 #Se todas as condicoes forem cumpridas vai acrescentar +1
                        for k in range(a):
                            joguinhoAux[i+k][j] = joguinhoAux[i+k][j].upper()#Coloca em maiusculo 
                    elif verticais2(l, c, joguinho, i, j, letrinhas, a) == True: #Va para def verticais2
                        soma+=1 #Se todas as condicoes forem cumpridas vai acrescentar +1
                        for k in range(a):
                            joguinhoAux[i-k][j] = joguinhoAux[i-k][j].upper()#Coloca em maiusculo 

                if letrinhas == letrinhas[::-1]: #Verifica se é palindromo
                    if diagonal(l, c, joguinho, i, j, letrinhas, a) == True: #Va para def diagonal1
                        soma+=1 #Se todas as condicoes forem cumpridas vai acrescentar +1
                        for k in range(a):
                            joguinhoAux[i+k][j+k] = joguinhoAux[i+k][j+k].upper()#Coloca em maiusculo 
                else:
                    if diagonal(l, c, joguinho, i, j, letrinhas, a) == True: #Va para def diagonal1
                        soma+=1 #Se todas as condicoes forem cumpridas vai acrescentar +1
                        for k in range(a):
                            joguinhoAux[i+k][j+k] = joguinhoAux[i+k][j+k].upper()#Coloca em maiusculo 
                    elif diagonal2(l, c, joguinho, i, j, letrinhas, a) == True: #Va para def diagonal2
                        soma+=1 #Se todas as condicoes forem cumpridas vai acrescentar +1
                        for k in range(a):
                            joguinhoAux[i-k][j-k] = joguinhoAux[i-k][j-k].upper()#Coloca em maiusculo 

                if letrinhas == letrinhas[::-1]: #Verifica se é palindromo        
                    if diagonal3(l, c, joguinho, i, j, letrinhas, a) == True: #Va para def diagonal3
                        soma+=1 #Se todas as condicoes forem cumpridas vai acrescentar +1
                        for k in range(a):
                            joguinhoAux[i+k][j-k] = joguinhoAux[i+k][j-k].upper()#Coloca em maiusculo 
                else:
                    if diagonal3(l, c, joguinho, i, j, letrinhas, a) == True: #Va para def diagonal3
                        soma+=1 #Se todas as condicoes forem cumpridas vai acrescentar +1
                        for k in range(a):
                            joguinhoAux[i+k][j-k] = joguinhoAux[i+k][j-k].upper()#Coloca em maiusculo 
                    elif diagonal4(l, c, joguinho, i, j, letrinhas, a) == True: #Va para def diagonal4s
                        soma+=1 #Se todas as condicoes forem cumpridas vai acrescentar +1
                        for k in range(a):
                            joguinhoAux[i-k][j+k] = joguinhoAux[i-k][j+k].upper()#Coloca em maiusculo 
        #Coloca outra parte do print
        print1(soma, letrinhas)

        
    #Fim do print da matriz com as palavras com letras maiusculas 
    print("----------------------------------------")
    for r in range(l):
        if r > 0:
            print()
        for t in range(c):
            if t == c-1:
                print(joguinhoAux[r][t], end = "")
            else:
                print(joguinhoAux[r][t], end = " ")
    print()

#Vai verificar cada palavra da esquerda para a direita nas horizontais e vai retornar True se a achar a palavra
def horizontais(l, c, joguinho, i, j, letrinhas, a):
    for k in range(a):
        if j < c: #condicao criada para o j nao sair de dentro da matriz
            if joguinho[i][j].lower() == letrinhas[k] or joguinho[i][j]== '*':
                j+=1
            else:
              return False
        else:
          return False

    return True

#Vai verificar cada palavra da direita para a esquerda nas horizontais e vai retornar True se a achar a palavra    
def horizontais2(l, c, joguinho, i, j, letrinhas, a):
    for k in range(a):
        if j >= 0: #condicao criada para o j nao sair de dentro da matriz
            if joguinho[i][j].lower() == letrinhas[k] or joguinho[i][j]== '*':
                j-=1
            else:
              return False
        else:
          return False

    return True

#Vai verificar cada palavra de cima para baixo nas verticais e vai retornar True se a achar a palavra    
def verticais(l, c, joguinho, i, j, letrinhas, a):
    for k in range(a):
        if i < l: #condicao criada para o l nao sair de dentro da matriz
            if joguinho[i][j].lower() == letrinhas[k] or joguinho[i][j]== '*':
                i+=1
            else:
              return False
        else:
          return False

    return True

#Vai verificar cada palavra de baixo para cima nas verticais e vai retornar True se a achar a palavra 
def verticais2(l, c, joguinho, i, j, letrinhas, a):
    for k in range(a):
        if i >= 0: #condicao criada para o l nao sair de dentro da matriz
            if joguinho[i][j].lower() == letrinhas[k] or joguinho[i][j]== '*':
                i-=1
            else:
              return False
        else:
          return False

    return True

#A patir daqui vira uma rosa dos ventos basicamento verifico cada direcao nas diagonais

#diagonal direcao sudeste
def diagonal(l, c, joguinho, i, j, letrinhas, a):
    for k in range(a):
        if i < l and j < c: #condicao criada para o l e o nao sairem de dentro da matriz
            if joguinho[i][j].lower() == letrinhas[k] or joguinho[i][j]== '*':
                i+=1
                j+=1
            else:
              return False
        else:
          return False

    return True

#diagonal direcao noroeste
def diagonal2(l, c, joguinho, i, j, letrinhas, a):
    for k in range(a):
        if i >= 0 and j >= 0: #condicao criada para o l e o nao sairem de dentro da matriz
            if joguinho[i][j].lower() == letrinhas[k] or joguinho[i][j]== '*':
                i-=1
                j-=1
            else:
              return False
        else:
          return False

    return True

#diagonal direcao sudoeste
def diagonal3(l, c, joguinho, i, j, letrinhas, a):
    for k in range(a):
        if i < l and j >= 0: #condicao criada para o l e o nao sairem de dentro da matriz
            if joguinho[i][j].lower() == letrinhas[k] or joguinho[i][j]== '*':
                i+=1
                j-=1
            else:
              return False
        else:
          return False

    return True

#diagonal direcao nordeste
def diagonal4(l, c, joguinho, i, j, letrinhas, a):
    for k in range(a):
        if i >= 0 and j < c: #condicao criada para o l e o nao sairem de dentro da matriz
            if joguinho[i][j].lower() == letrinhas[k] or joguinho[i][j]== '*':
                i-=1
                j+=1
            else:
              return False
        else:
          return False

    return True


#Continuacao daquela funcao print la de cima
def print1(contador, letrinhas):
    print("----------------------------------------")
    print("Palavra:",letrinhas)
    print("Ocorrencias:",contador)


    
main() 
