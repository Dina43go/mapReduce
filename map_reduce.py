from os import listdir
from fuction import *
from collections import defaultdict
from time import sleep

fichiers = listdir('text/')

collectionMap = []
collectionReduce = []

collection = collectFileText(fichiers)

for key,value in collection :
    collectionMap.append(map(key, value))
    
collectionMap = combineCollectionList(collectionMap)
collectionMap = mergeKeyCollection(collectionMap)

for key,value in collectionMap:
    collectionReduce.append(reduce(key, value))

### print DATA ###
    ## STEP BY STEP

for element in collectionReduce:
    occurence = 'occurences' if element[1] >1 else 'occurence'
    print(f'le mot : {element[0]} possède {element[1]} {occurence}','...')
    # sleep(2.5) 
print('size of colection :' ,collectionReduce.__len__())
