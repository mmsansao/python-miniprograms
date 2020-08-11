def high_and_low1(numbers):
    l = numbers.split(' ')
    inte = []
    for x in l:
        inte.append(int(x))
    return str(max(inte)) + ' ' + str(min(inte))


def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn), min(nn))


# String para teste
numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
