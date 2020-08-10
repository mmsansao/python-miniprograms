def delete_nth1(order,max_e):
    contagem = False
    while not contagem:
        lista = []
        for i in order:
            if lista.count(i) < max_e:
                lista.append(i)
            else:
                contagem = True
    return lista

def delete_nth2(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans

def delete_nth3(order,max_e):
    return [o for i,o in enumerate(order) if order[:i].count(o)<max_e ]

# Array para teste:

a = [1,1,1,1,3,3,7,2,2,2,2]
