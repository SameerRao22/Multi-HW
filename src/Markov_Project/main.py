import sys

def tokenize(corpus):
    f = open(corpus, 'r')
    raw_text = f.read()
    f.close()
    raw_text = raw_text.replace('\n', ' ')
    raw_text = raw_text.translate(None, "(){}<>'.,;!:~`\|")
    raw_text = raw_text.translate(None, '"')
    raw_text = raw_text.lower()
    return raw_text.split(' ')

def index(words):
    key = []
    for x in words:
        if x not in key:
            key.append(x)
    return key

def model(words, k=1):  
    model = {}
    for i in range(len(words)-k):
        if model.get(words[i]) == None:
            model[words[i]] = {}
            model[words[i]][words[i+k]] = 1
        else:
            if model[words[i]].get(words[i+k]) == None:
                model[words[i]][words[i+k]] = 1
            else:
                model[words[i]][words[i+k]] += 1
    return model

def normalize(model):
    keys = model.keys()
    for k in keys:
        s = 0.0
        for v in model[k]:
            s += model[k][v]
        for v in model[k]:
            model[k][v] /= s
    return model
 

if __name__ == '__main__':
    file = sys.argv[1]
    words = tokenize(file)
    index = index(words)
    model = model(words)
    model = normalize(model)
    print(index)
    print(model)