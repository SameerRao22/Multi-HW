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

def next(pos, pos_chain):
    if pos == 'NOUN' or pos == 'PRON':
        if len(pos_chain) >= 4:
            if pos_chain[len(pos_chain)-2] == 'VERB':
                return ['END']
            elif pos_chain[len(pos_chain)-2] == 'DET':
                if pos_chain[len(pos_chain)-3] == 'VERB':
                    return ['END']
        return ['VERB','CONJ','ADV', 'ADP']

    elif pos == 'VERB':
        return ['NOUN','DET', 'ADV']

    elif pos == 'ADV':
        if len(pos_chain) >= 10:
            if pos_chain[len(pos_chain)-2] == 'VERB':
                return ['END']
        return ['VERB']

    elif pos == 'ADJ':
        return ['NOUN']

    elif pos == 'CONJ':
        return ['NOUN']

    elif pos == 'DET':
        return ['NOUN']

    elif pos == 'ADP':
        return ['DET', 'NOUN', 'PRON']
    return []

def valid(pos_chain):
    return ('NOUN' in pos_chain or 'PRON' in pos_chain) and ('VERB' in pos_chain)

def g_generate(model, vector, index, pos, words):
    sentence = []
    pos_chain = []
    v = vector
    sentence.append(vector_to_word(v, index))
    while True:
        word_initial = vector_to_word(v, index)
        pos_initial = pos[words.index(word_initial)][1]
        pos_chain.append(pos_initial)
        pos_next = next(pos_initial, pos_chain)
        if len(sentence) >= 10 and pos_chain[len(sentence)-1] == 'NOUN':
            break

        if 'END' in pos_next:
            break

        if pos_next == []:
            sentence.pop(len(sentence)-1)
            v = matrix.multiply(model, v)
            word = vector_to_word(v, index)
            v = word_to_vector(word, index)
            continue

        flag = True
        count = 0
        while flag:
            word_list = []
            v = matrix.multiply(model, v)
            word = vector_to_word(v, index)
            word_list.append(word)
            v = word_to_vector(word, index)
            pos_current = pos[words.index(word)][1]
            if (pos_current in pos_next):
                flag = False
            else:
                if count >= 5:
                    v = word_to_vector(sentence[len(sentence)-1], index)
                    word = vector_to_word(matrix.multiply(model, v), index)
                    if word in word_list:
                        new_word = seed(pos)
                        sentence = []
                        sentence.append(new_word)
                        pos_chain = []
                        pos_chain.append(pos[words.index(new_word)][1])
                v = word_to_vector(sentence[len(sentence)-1], index)
                count += 1

        sentence.append(word)
    return sentence

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