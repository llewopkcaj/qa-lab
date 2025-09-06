import random
nouns = ["vertex", "curve", "light", "being", "eye", "saying"]
verbs = ["elates", "aligns", "synthesizes", "madurates", "evicts", "dilates"]
adjectives = ["looping", "sordid", "banal", "moonlike", "tacit", "elemental"]   
adverbs = ["loosely", "silently", "soon", "already", "blithely", "vividly"]

use_noun = random.sample(nouns, 5)
use_verb = random.sample(verbs, 5)
use_adjective = random.sample(adjectives, 5)
use_adverb = random.sample(adverbs, 5)  

with open("poem.txt", "w") as file:
    for word in range(5):
        line = f"The {use_adjective[word]} {use_noun[word]} {use_verb[word]} {use_adverb[word]}"  
        print(line.center(80))
        file.write(line.center(80) + "\n")




