def find_short1(s):
    words = s.split(" ")
    short = 100
    for w in words:
        if len(w) < short:
            short = len(w)
    return short

def find_short2(s):
    return min(len(x) for x in s.split())

def find_short3(s):
    return len(min(s.split(' '), key=len))
    
