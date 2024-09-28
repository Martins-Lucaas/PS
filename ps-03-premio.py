"""
Lucas Martins Primo
12021EBI022
"""
def main():

    view()

def view():
    A=0 #Soma dos acessos
    dias=-1 #Qtde de dias para atingir o acesso
    while A<1000000: #Faça enquanto o número total de acessos for < 1 milhão
        #Entrada dos acessos naquele dia
        N=int(input()) 
        A+=N #Soma dos acessos com a entrada realizada
        dias+=1 #Soma 1 ao dia de acessos
    print(dias) #Msg de qtos dias chegamos a 1 milhão
main()
    
