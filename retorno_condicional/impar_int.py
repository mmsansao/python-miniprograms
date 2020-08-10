def find_it1(seq):
    for i in seq:
        if seq.count(i)%2 != 0:
            return i

def find_it2(seq):
    return [x for x in seq if seq.count(x) % 2][0]


# Array para teste:
a1 = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
