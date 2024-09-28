'''
12021EBI022
Lucas Martins Primo
'''

def main(): #funcao principal
    a = int(input()) #numero de dias
    print(view(a)) #printando o resultado na funcao view

def view(a): #funcao para calculo dos dias

    s = 0 #acumulo do somatorio das entradas no site
    dia = -1 #variavel que vai acumular os dias
    for i in range(1,a+1):
        b = int(input()) #pedido das entradas no site por dia
        s += b #somatorio das entradas (valor = valor + soma)
        if s >= 1000000 and dia == -1: # condicao para crescimento da soma "s" para dar o número de dias
            dia = i #dia falando o numero total de dias para chegar em 1.000.000
    return dia #retornando o dia

main() #Chamada da função main
