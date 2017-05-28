"""Alice_words"""
file = open('alice_words.txt','w')
text = input('Alice’s Adventures in Wonderland:').lower()
word_count={}
from collections import Counter
word_count = Counter (text.split())

var = ('{:15}{:7}'.format('Word','Count'))

var1= []

for (word,occurance) in sorted(word_count.items()):
    x = ({'{:15}{:3}'.format(word,occurance)})
    var1.append(x)

var1.sort()

with open('alice_words.txt', 'a') as out:
    out.write(var + '\n')
    out.write('-' *22)
    out.write('\n')
    for item in var1:
        out.write("{}\n".format(item))

