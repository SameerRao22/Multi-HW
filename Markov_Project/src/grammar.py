from nltk import classify
from nltk.util import pr
from markov import *
import string

'''
IC -> NP VP
AP -> ADJ | ADJ AP
NP -> NOUN | DET NP | AP NP | NOUN PP
VP -> VERB | VERB NP | VERB NP PP | VERB ADV
PP -> PRT NP
S  -> IC | IC CONJ IC
'''

'''
ADJ     (adjective) 
ADP     (adposition)    ex. on, of, at, with, by, into, under
ADV     (adverb)
CONJ    (conjunction)
DET     (determiner, article)
NOUN    (noun)
NUM	    (numeral)
PRT     (particle)      ex. at, on, out, over per, that, up, with
PRON    (pronoun)
VERB	(verb)
.	    (punctuation marks)
X	    (other)
'''
def seed(raw_words, next = ['NOUN', 'DET']):
    origin = random.choice(raw_words)
    while origin[1] not in next:
        origin = random.choice(raw_words)
    origin = origin[0]
    return origin

def sentence_write(sentence, clear=False):
    if clear:
        f = open('sentence.txt', 'w')
    else:
        f = open('sentence.txt', 'a')
    for i in sentence:
        f.write(i + ' ')
    f.write('\n')
    f.close()

def next(pos, pos_chain):
    ret = []
    if pos == 'NOUN' or pos == 'PRON':
        ret = ['VERB','CONJ','ADV', 'PRT']

    elif pos == 'VERB':
        ret = ['NOUN','DET', 'ADV', 'ADP']

    elif pos == 'ADV':
        if len(pos_chain) == 1:
            ret = ['NOUN']
        else:
            ret = ['VERB', 'ADV']

    elif pos == 'ADJ':
        ret = ['NOUN']

    elif pos == 'CONJ':
        ret = ['NOUN']

    elif pos == 'DET':
        ret = ['NOUN', 'ADJ']

    elif pos == 'ADP' or pos == 'PRT':
        ret = ['DET', 'NOUN', 'PRON']
    
    if pos_chain.count('ADP') > 2:
        try:
            ret.remove('ADP')
        except:
            pass
    if pos_chain.count('CONJ') > 2:
        try:
            ret.remove('CONJ')
        except:
            pass
    if pos_chain.count('PRT') > 2:
        try:
            ret.remove('PRT')
        except:
            pass
    return ret

def valid(pos_chain):
    pronouns = pos_chain.count('ADP') + pos_chain.count('PRT')
    nouns = pos_chain.count('NOUN') + pos_chain.count('PRON')
    return (nouns >= pronouns) and ('VERB' in pos_chain) and (pos_chain[len(pos_chain)-1] == 'NOUN')
    

def g_generate(model, vector, index, pos, words):
    sentence_write([], clear=True)
    sentence = []
    pos_chain = []
    v = vector
    sentence.append(vector_to_word(v, index))
    for i in sentence:
        pos_chain.append(pos[words.index(i)][1])
    sentence_write(sentence)
    sentence_write(pos_chain)
    while True:
        pos_initial = pos_chain[len(pos_chain)-1]
        pos_next = next(pos_initial, pos_chain)

        if pos_next == []:
            sentence = sentence[:len(sentence)-1]
            pos_chain = pos_chain[:len(pos_chain)-1]
            v = word_to_vector(sentence[len(sentence)-1], index)
            continue

        count = 0
        while True:
            word_list = []
            v = matrix.multiply(model, v)
            word = vector_to_word(v, index)
            word_list.append(word)
            v = word_to_vector(word, index)
            pos_current = pos[words.index(word)][1]

            if (pos_current in pos_next):
                sentence.append(word)
                pos_chain.append(pos[words.index(word)][1])
                sentence_write(sentence)
                sentence_write(pos_chain)
                if len(sentence) >= 5 and valid(pos_chain):
                    return sentence
                break
            else:
                if count >= 5:
                    v = word_to_vector(sentence[len(sentence)-1], index)
                    word = vector_to_word(matrix.multiply(model, v), index)
                    if word in word_list:
                        new_word = seed(pos,next=pos_next)
                        sentence.append(new_word)
                        pos_chain.append(pos[words.index(new_word)][1])
                        v = word_to_vector(sentence[len(sentence)-1], index)
                        break
                v = word_to_vector(sentence[len(sentence)-1], index)
                count += 1

def main(file):
    raw_words = tokenize(file)
    words = list(map(lambda word : word[0], raw_words))
    ind, model = gen_model(words)
    print('[Completed]')

    print('\nCreating Model...')
    model = normalize(model)    #Normalize model
    print('[Completed]\n')


    origin = seed(raw_words)
    
    vector = word_to_vector(origin, ind)
    s = ""
    for i in g_generate(model, vector, ind, raw_words, words):
        if i not in string.punctuation:
            s += i + ' '
    s = s[:len(s)-1]+'.'
    print(s)


if __name__ == "__main__":
    main('/Users/sameer/Documents/School/SeniorYear/Multi/Python/src/Markov_Project/data/corpus3.txt')