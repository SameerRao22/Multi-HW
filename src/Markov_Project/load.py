from markov import *
from matrix import *

def main(file, origin, length):

    origin = origin.split(' ')

    ind, model = load(file)

    vector = word_to_vector(origin, ind)
    
    s = generate(model, vector, ind, length)
    print('Sentence Generated:')
    o = ''
    for i in origin:
        o += i + ' '
    s = o + s
    print(s)


if __name__ == '__main__':
    main(file='models/model1.txt', origin='dumb farm animals', length=12)