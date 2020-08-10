import math

def find_next_square(sq):
    r = int(math.sqrt(sq))
    if sq%r != 0:
        return -1
    else:
        sq +=1
        test = True
        while test:
            if sq:
                ri = int(math.sqrt(sq))
                if sq%ri != 0:
                    sq += 1
                else:
                    test = False
        return sq
                
print(find_next_square(9))