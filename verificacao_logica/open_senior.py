def open_or_senior1(data):
    lista = []
    for person in data:
        if person[0] >= 55 and person[1] > 7:
            lista.append("Senior")
        else:
            lista.append("Open")
    return lista


def open_or_senior2(data):
    return [
        "Senior" if age >= 55 and handicap >= 8 else "Open" for age, handicap in data
    ]


def open_or_senior3(data):
    return ["Senior" if m[0] > 54 and m[1] > 7 else "Open" for m in data]


# Lista para testes:

membros = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
