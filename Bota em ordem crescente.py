"""
Lucas Martins Primo
12021EBI022
"""

lista = [1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30,
29]

def swap(l, i, j):
    l[i], l[j] = l[j], l[i]
    
def selection_sort(lista):
    for i in range(len(lista)-1):
        menor_pos = i
        for j in range(i+1, len(lista)):
            if(lista[j]>lista[menor_pos]):
                menor_pos = j
        swap(lista, i, menor_pos)
    print(lista)


selection_sort(lista)
