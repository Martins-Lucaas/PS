def main():
    matriz = []
    a = input().split()
    matriz.append(a)
    b = input().split()
    matriz.append(b)
    c = input().split()
    matriz.append(c)
    d = input().split()
    matriz.append(d)
    e = input().split()
    matriz.append(e)
    f = input().split()
    matriz.append(f)
    g = input().split()
    matriz.append(g)
    h = input().split()
    matriz.append(h)
    nsensor = int(input())
    alcance = int(input())
    tesouro = []
    posição1 = []
    for i in range(nsensor):
        posição = [int(x) for x in input().split()]
        posição1.append(posição)
    analisedes(matriz, nsensor, alcance, posição, tesouro)


##############################descendo
def analisedes(matriz, nsensor, alcance, posição, tesouro):
     for k in range(nsensor):
         print(posição)

    
main()
