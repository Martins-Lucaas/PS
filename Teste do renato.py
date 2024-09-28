def main(): #definindo a função main

    L = int(input()) #inserindo n° inteiro de linhas da grade

    C = int(input()) #inserindo n° inteiro de colunas da grade

    M = [] #lsita vazia em que se guardará a matriz

    if L>=2 and C<=100: #condição proposta pelo enunciado do trabalho para Linhas e Colunas
        for l in range(L): #laço para inserir os elementos de cada linha numa lista de lista
            linha = [x for x in input().split()] #inserindo os elementos de cada linha na entrada
            M.append(linha) #guarda na lista M os itens digitados

    N = int(input()) #inserindo n° inteiro de palavras buscadas

    buscas = [] #lista vazia para inserir as palavras buscadas
    if 1<=N<=10: #condição proposta pelo enunciado do trabalho para o numero de palavras buscadas
        for x in range(N): #laço para inserir as palavras buscadas na lista vazia
            busca = str(input()) #insere na entrada a palavra buscada uma de cada vez
            buscas.append(busca) #guarda na lista buscas as palavras buscadas

    
    print('----------------------------------------') #printa elemento grafico na saida
    print('Lista de Palavras')#mostra na tela a frase 'Lista de Palavras'
    
    for n in buscas: #laço dentro da lista buscas para procurar as palavras
        ocorrencias, nova = caçaPalavra(M,L,C,n) #chamada da função que ira procurar as palavras e irá guardar dois elementos: um para ocorrencias e a matriz modificada com as palavras em destaque
        print('----------------------------------------')#printa elemento grafico na saida
        print('Palavra: {}'.format(n)) #mostra na tela a 'palavra' seguida da palavra buscada
        print('Ocorrencias: {}'.format(ocorrencias)) #mostra na tela 'ocorrencias' seguida do numero de ocorrencias identificadas da palavra
        

    print('----------------------------------------')#printa elemento grafico na saida

   
    for p in nova: #laço para imprimir
        print(*p) #mostra na tela a matriz modificada 
  
    
def caçaPalavra(M,L,C,n): #definindo a função caçaPalavra
    soma = 0
    nova = M #a variavel nova receberá M com as letras em destaque
    ocorrencias = 0 #variavel ocorrencias que sera usada para contagem
    x = len(n) #variavel x que irá guardar o tamanho da palavra buscada
    for i in range(L):  #laço para analisar as linhas
        for j in range(C-x+1): #laço encaixado para analisar as linhas 
            if M[i][j] == n[0] or M[i][j] == '*': #achou a posição da primeira letra ou a letra é um asterisco
                atual = j #variavel local para variar a posiçao j
                for c in range(x): #laço que lerá a matriz e irá parar no tamanho da palavra buscada 
                    if M[i][j] == n[c] or M[i][j] == '*': #se a proxima letra for igual a da palavra buscada ou for igual a um asterisco
                        j+=1 #j sofre um acrescimo
                        c+=1 #c sofre um acrescimo para passar para a letra seguinte
                        if c == (x): #quando o numero de letras atingir o tamanho da palavra, obedecidas as condições
                            ocorrencias += 1 #ocorrencias sofre um acrescimo
                            for a in range(x): #outro laço que visa transformar a palavra buscada em maiuscula
                                nova[i][atual+a] = nova[i][atual+a].upper() #transforma cada letra da palavra em maisucula
                            break #para o laço
                    else: #caso nao se alcance nenhuma condição descrita
                        break #para o laço

    for j in range(C): #laço para analisar as colunas
        for i in range(L-x+1): #laço encaixado para analisar as colunas
            if M[i][j] == n[0] or M[i][j] == '*': #achou a posição da primeira letra ou a letra é um asterisco
                atual2 = i #variavel local para variar a posiçao i
                for d in range(x): #laço que lerá a matriz e irá parar no tamanho da palavra buscada 
                    if M[i][j] == n[d] or M[i][j] == '*': #se a proxima letra for igual a da palavra buscada ou for igual a um asterisco
                        i+=1 #i sofre um acrescimo
                        d+=1 #d sofre um acrescimo para passar para a letra seguinte
                        if d == (x): #quando o numero de letras atingir o tamanho da palavra, obedecidas as condições
                            ocorrencias +=1 #ocorrencias sofre um acrescimo
                            for b in range(x):#outro laço que visa transformar a palavra buscada em maiuscula
                                nova[atual2+b][j] = nova[atual2+b][j].upper()#transforma cada letra da palavra em maisucula
                            break #para o laço
                    else: #caso nao se alcance nenhuma condição descrita
                        break #para o laço
        
    for j in range(C): #laço para analisar as diagonais
        for i in range(L-x+1): #laço encaixado para analisar as colunas
            if M[i][j] == n[0] or M[i][j] == '*': #achou a posição da primeira letra ou a letra é um asterisco
                atual2 = i #variavel local para variar a posiçao i
                atual3 = j
                for d in range(x): #laço que lerá a matriz e irá parar no tamanho da palavra buscada 
                        if M[i][j] == n[d] or M[i][j] == '*': #se a proxima letra for igual a da palavra buscada ou for igual a um asterisco
                            i+=1 #i sofre um acrescimo
                            j+=1
                            if d == (x-1): #quando o numero de letras atingir o tamanho da palavra, obedecidas as condições
                                ocorrencias +=1 #ocorrencias sofre um acrescimo
                                for c in range(x):#outro laço que visa transformar a palavra buscada em maiuscula
                                    nova[atual2+c][atual3+c] = nova[atual2+c][atual3+c].upper()#transforma cada letra da palavra em maisucula
                                break #para o laço
                        else: #caso nao se alcance nenhuma condição descrita
                            break #para o laço

                        
    for j in range(C): #laço para analisar as diagonais
        for i in range(L-x+1): #laço encaixado para analisar as colunas
            if M[i][j] == n[0] or M[i][j] == '*': #achou a posição da primeira letra ou a letra é um asterisco
                atual2 = i #variavel local para variar a posiçao i
                atual3 = j
                for d in range(x): #laço que lerá a matriz e irá parar no tamanho da palavra buscada 
                        if M[i][j] == n[d] or M[i][j] == '*': #se a proxima letra for igual a da palavra buscada ou for igual a um asterisco
                            i-=1 #i sofre um acrescimo
                            j+=1 
                            if d == (x-1): #quando o numero de letras atingir o tamanho da palavra, obedecidas as condições
                                ocorrencias +=1 #ocorrencias sofre um acrescimo
                                for c in range(x):#outro laço que visa transformar a palavra buscada em maiuscula
                                    nova[atual2-c][atual3+c] = nova[atual2-c][atual3+c].upper()#transforma cada letra da palavra em maisucula
                                break #para o laço
                        else: #caso nao se alcance nenhuma condição descrita
                            break #para o laço

    
    
    return ocorrencias, nova #retorna os valor da ocorrencia de cada palavra e a matriz alterada com as palavras em destaque(maiuscula)


main() #chamada da função main
