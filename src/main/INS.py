def resolvename(name):
    scenes = [["Title Scene","Title Screen","Title"], ["Death Scene","Death","Death Screen"],["Debug","Debug Area","Debug Room"],["Kitchen 01","Kitchen Level 1"]]
    for x in range(len(scenes)):
        i = scenes[x]
        if type(i) == type(["hi","hi"]):
            if name in i:
                return x
        elif name == i:
            return x
    return 0