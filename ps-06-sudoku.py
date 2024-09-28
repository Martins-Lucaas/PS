def main():
    
    n = int(input()) #Recebe o numero de sudokus a serem conferidos
    matriz = [] #Lista vazia para receber as matrizes mais tarde

    for k in range(1, n+1): #Define quantas vezes este programa vai rodar dependendo da quantidade de matrizes
        #Constroi 9 linhas 
        for i in range(9):
            linha= [int(x) for x in input().split()] 
            matriz.append(linha) #coloca linha por linha na matriz
        sudoku(matriz, n, k) # vai conferir se o sudoku estÃ¡ correto n vezes
        matriz.clear() # Assim a cada vez que passar um sudoku se tiver outro, vai resetar a lista para trabalhar com outra



 #Funcao que vai conferir se ta certo ou errado   
def sudoku(matriz, n, k):
    l = len(matriz) #Define as linhas
    c = len(matriz[0]) #Define as colunas
    soma_linhas = [] #lista criada para receber as somas de cada linha individualmente
    
    for i in range(l):
        soma = 0
        for j in range(c):
            soma += matriz[i][j] #A cada vez que o codigo passa aqui vai somando em sequencia os valores da lista
        soma_linhas.append(soma) #e no fim quando somar a linha toda vai adicionar o valor resultante aqui

    soma_colunas = [] #lista criada para receber as somas de cada coluna individualmente
    for j in range(c):
        soma = 0
        for i in range(l):
            soma += matriz[i][j]             
        soma_colunas.append(soma)#Coloca a soma de cada coluna aqui


    juncao = soma_colunas + soma_linhas #literalmente a juncao das duas listas das somas em uma so
    print1(juncao, k, soma_colunas, soma_linhas) #chamda da funcao print1


   
def print1(juncao, k, soma_colunas, soma_linhas):
    for i in juncao:
        a = juncao.count(45) # A  serÃ¡ igual ao numero de vezes que o numero 45 aparece, sendo 45 o resultado da soma de uma linha ou coluna
        
    if a == 18: #Se for igual a 18 quer dizer que o numero 45 apareceu 18 vezes o que equivale aos nove resultados das colunas e das linhas juntos
        print("Instancia {}\nSIM".format(k))#assim sendo se o numero 45 apareceu 18 vezes quer dizer que nao tem nenhum numero repetido, errado, ou fora do lugar o que deixa o sudoku correto
        print()
        
        #Limpa todas as listas usadas para serem usadas no caso de vir outro sudoku para a conferencia
        soma_colunas.clear()
        soma_linhas.clear()
        juncao.clear()
        
    else: #Se for diferente de 18 quer dizer que tem algum numero diferente de 45 dentro da juncao o que quer dizer que tem algum numero errado na matriz
        print("Instancia {}\nNAO".format(k))
        print()
        
        ##Limpa todas as listas usadas para serem usadas no caso de vir outro sudoku para a conferencia
        soma_colunas.clear()
        soma_linhas.clear()
        juncao.clear()
            
main()
