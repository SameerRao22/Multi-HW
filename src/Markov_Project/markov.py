import string
import random
import matrix


def tokenize(corpus):
    f = open(corpus, 'r')
    raw_text = f.read()
    f.close()
    raw_text = raw_text.replace('\n', ' ')
    # raw_text = raw_text.translate(None, "(){}<>'.,;!:~`\|")
    # raw_text = raw_text.translate(None, '"')
    raw_text = raw_text.translate(str.maketrans('','',string.punctuation))
    raw_text = raw_text.lower()
    return raw_text.split(' ')

def gen_index(words):
    key = []
    for x in words:
        if x not in key:
            key.append(x)
    return key

def dict_model(words, k=2):  
    model = {}
    for i in range(len(words)-k):
        if model.get(words[i+k]) == None:
            model[words[i+k]] = {}
            model[words[i+k]][words[i]] = 1
        else:
            if model[words[i+k]].get(words[i]) == None:
                model[words[i+k]][words[i]] = 1
            else:
                model[words[i+k]][words[i]] += 1
    return model

def transition_model(dict_model, index):
    model = []
    for j in range(len(index)):
        model.append([])
        for k in range(len(index)):
            key = index[j]
            value = index[k]
            if dict_model.get(key) != None:
                num = dict_model[key].get(value)
                if num != None:
                    model[j].append(num)
                else:
                    model[j].append(0)
            else:
                model[j] = [0]*len(index)
    return model
    
def normalize(model, index):
    for c in range(len(model)):
        sum = 0.0
        for r in range(len(model)):
            sum += model[r][c]
        for v in range(len(model)):
            if sum != 0:
                model[v][c] /= sum
    return model

def save(model, index, name='model.txt'):
    f = open(name, 'w')

    s = ''
    for i in index:
        s += i + ' '
    s += '\n'
    f.write(s)

    for j in model:
        s = ''
        for k in j:
            s += str("{:.6f}".format(k)) + ' '
        s += '\n'
        f.write(s)
    f.close

def load(file):
    f = open(file, 'r')
    raw_text = f.readlines()
    index = raw_text[0].split(' ')
    index.pop(len(index)-1)
    raw_text = raw_text[1:]
    model = []
    for line in raw_text:
        row = []
        data = line.split(' ')
        for val in data:
            try:
                row.append(float(val))
            except:
                pass
        model.append(row)
    return index, model

def word_to_vector(word, index):
    val = []
    for i in word:
        val.append(index.index(i))
    v = []
    for i in range(len(index)):
        if i in val:
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

def generate(model, vector, index, k=5):
    sentence = ''
    v = vector
    for i in range(k):
        v = matrix.multiply(model, v)
        word = vector_to_word(v, index)
        sentence += word + ' '
    return sentence