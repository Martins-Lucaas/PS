"""
Lucas Martins Primo
12021EBI022
"""
#Aquele inicio de sempre para receber as entradas
def main():
    n = int(input()) #Recebe o numero de cartas
    titulo = input().split() #Recebe "O inicio - NOME EM DIANTE"


    conjunto_cartinhas = [] #Listinha para receber as cartas
    for i in range(n):
        cartinhas = []
        cartinhas = [str(x) for x in input().split()]
        conjunto_cartinhas.append(cartinhas)

    atributos_prioridade = input().split() #Recebe a ordem de prioridade dos status

    arrayPrioridades = [] #Lista para receber os atributos em ordem para conferir depois
    arrayPrioridades = prioridade(titulo, atributos_prioridade, arrayPrioridades) #Va para a funcao prioridades

    ordenacao(n, conjunto_cartinhas, arrayPrioridades)#Va para a funcao ordenacao

    print1(titulo, conjunto_cartinhas, atributos_prioridade) #Va para a funcao print1


def prioridade(titulo, atributos_prioridade, arrayPrioridades):
    for i in range(len(atributos_prioridade)):
        for j in range(len(titulo)):
            if atributos_prioridade[i] == titulo[j]: #Compara as prioridades vindas dos atributos e compara com o título para saber onde cada uma fica
                arrayPrioridades.append(j) #Coloca tudo bonitinho aqui
    return arrayPrioridades #Retorna uma lista com os numeros das prioridades em ordem ex: [3,2,1] para ser usado nas posicoes em matriz da funcao ordenacao


def ordenacao(p, conjunto_cartinhas, arrayPrioridades):
    for i in range(len(conjunto_cartinhas)): #Metodo bubble igual ao dos slides, ainda acho que fazendo por sort() seria mais facil
        for j in range(len(conjunto_cartinhas)-1, i, -1):
            if int(conjunto_cartinhas[j][arrayPrioridades[0]])==int(conjunto_cartinhas[j-1][arrayPrioridades[0]]):#compara se os numeros sao iguais, aproveitei para converter para inteiro aqui
                for k in range(len(arrayPrioridades)): #Pega aquela lista das prioridades na ordem certa para trabalharmos caso tenha dados iguais
                    if int(conjunto_cartinhas[j][arrayPrioridades[k]])>int(conjunto_cartinhas[j-1][arrayPrioridades[k]]): #Compara novamente e se for maior ja chama a troca para substituir
                        troca(conjunto_cartinhas, j, j-1) #funcao troca
                        break
                    elif int(conjunto_cartinhas[j][arrayPrioridades[k]])<int(conjunto_cartinhas[j-1][arrayPrioridades[k]]):
                        break
            elif int(conjunto_cartinhas[j][arrayPrioridades[0]])>int(conjunto_cartinhas[j-1][arrayPrioridades[0]]): #continuacao do primeiro if caso nao tenha numero igual no status de maior prioridade
                troca(conjunto_cartinhas, j, j-1) #chama a troca novamente

    return conjunto_cartinhas


def troca(conjunto_cartinhas, i, j):
    conjunto_cartinhas[i], conjunto_cartinhas[j] = conjunto_cartinhas[j], conjunto_cartinhas[i] #Isso daqui e o def swap dos slides, pega as duas posicoes e troca de lugar

def print1(titulo, conjunto_cartinhas, atributos_prioridade ):

    for inicio in titulo: #Fiz esse aqui usando o de baixo como de exemplo
        print('{:15s}'.format(inicio), ''.join('{:>10}'.format(item) for item in titulo[1:]))
        break #Break por que se nao imprime varias vezes e so queremos uma

    for atributo in conjunto_cartinhas:
        print('{:15s}'.format(atributo[0]), ''.join('{:>10}'.format(item) for item in atributo[1:]))

main()
