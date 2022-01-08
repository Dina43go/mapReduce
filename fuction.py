from collections import defaultdict

def collectFileText(fichiers):
    
    collection = []
    for fichier in fichiers:
        text = open(f'text/{fichier}').read().replace('.', '').replace(',', '').lower()
        collection.append((fichier , text))
    return collection



def map(key,value):
    intermadiate = []
    for word in value.split():
        intermadiate.append((word,1))
    return intermadiate

def reduce(key,value):
    s = 0
    for c in value:
        s = s + c
    return (key , s)

def mergeKeyCollection(collection):
    d = defaultdict(list)
    for k, v in collection:
        d[k].append(v)
    return list(d.items())

def combineCollectionList(list):
    newList = []
    for l in list:
        newList = newList + l
    return newList