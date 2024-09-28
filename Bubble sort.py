lista = [13, 4451, 5487, 151, 1, 12, 789]

def swap(l, i, j):
    l[i], l[j] = l[j], l[i]

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1, i, -1):
            if(lista[j]>lista[j-1]):
                swap(lista, j, j-1)
    return lista

bubble_sort(lista)
print(lista)
