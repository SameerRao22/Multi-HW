from matrix import *
from markov import *
from grammar import *
import sys

def main(file, length=None, origin=None):
    print('Reading Corpus...')  #Read corpus and generate model
    raw_words = tokenize(file)
    words = list(map(lambda word : word[0], raw_words))
    # pos = list(map(lambda word: word[1], raw_words))
    ind, model = gen_model(words)
    print('[Completed]')

    print('\nCreating Model...')
    model = normalize(model)    #Normalize model
    print('[Completed]\n')

    size = matrix.size(model)
    print('\nMatrix Size:')
    print(size)
    print('')

    if origin == None:
        origin = seed(raw_words)

    vector = word_to_vector(origin, ind)

    print('Generating Sentence Without Grammar...')
    s = generate(model, vector, ind, length)
    print('[Completed]\n')
    print('\n------Sentence------')
    print(s.capitalize())

    print('')

    print('Generating Sentence With Grammar...')
    g = g_generate(model, vector, ind, raw_words, words)
    print('[Completed]')
    print('\n------Sentence With Grammar------')

    s = ""
    for i in g:
        if i not in string.punctuation:
            s += i + ' '
    s = s[:len(s)-1]+'.'
    print(s)


if __name__ == '__main__':
    main(file='data/corpus3.txt')