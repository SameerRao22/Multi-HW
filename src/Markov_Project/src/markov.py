import string
import random
import matrix
import nltk


def tokenize(corpus):
    f = open(corpus, 'r')
    words = f.read().lower()
    f.close()
    words = nltk.word_tokenize(words)
    words = nltk.pos_tag(words, tagset='universal')
    return words

def gen_model(words):
    index = []
    for x in words:
        if x not in index:
            index.append(x)
    model = matrix.zero(len(index))
    for i in range(len(words)-1):
        f = words[i]
        t = words[i+1] 
        from_index = index.index(f)
        to_index = index.index(t)
        model[to_index][from_index] += 1
    return index, model

def normalize(model):
    for c in range(len(model)):
        sum = 0.0
        for r in range(len(model)):
            sum += model[r][c]
        for v in range(len(model)):
            if sum != 0:
                model[v][c] /= sum
    return model

def word_to_vector(word, index):
    val = index.index(word)
    v = []
    for i in range(len(index)):
        if i == val:
            v.append([1.])
        else:
            v.append([0.])
    return v

def vector_to_word(v, index):
    weights = []
    for i in v:
        for l in i:
            l = round(l*1000000)
            weights.append(l)
    w = random.choices(index, weights=weights, k=1)
    return w[0]

def generate(model, vector, index, k=None):
    sentence = vector_to_word(vector, index) + ' '
    v = vector
    if k != None:
        for i in range(k):
            v = matrix.multiply(model, v)
            word = vector_to_word(v, index)
            v = word_to_vector(word, index)
            if word in string.punctuation:
                sentence = sentence[:len(sentence)-1]
            sentence += word + ' '
    else:
        while True:
            v = matrix.multiply(model, v)
            word = vector_to_word(v, index)
            v = word_to_vector(word, index)
            if word in string.punctuation:
                sentence = sentence[:len(sentence)-1]
            sentence += word + ' '
            if word in '.!?':
                break
    return sentence