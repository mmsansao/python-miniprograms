def comp1(a1, a2):
    for n in a2:
        if (n**(1/2)) in a1:
            comp = True
        else:
            comp = False
            break
    return comp


def comp2(a1, a2):
    if a1 == None or a2 == None:
        return False
    else:
        a2_1 = []
        for n in a2:
            if n**(1/2)%int(n**(1/2)) != 0.00000:
                return False
                break
            else:
                a2_1.append(n**(1/2))
        if all(elem in a2_1 for elem in a1):
            return True
        else:
            return False


# Arrays de teste:
a1 = [58, 58, 94, 18, 73, 63, 56]
a2 = [3364, 3364, 8836, 324, 5329, 3969, 3136]
