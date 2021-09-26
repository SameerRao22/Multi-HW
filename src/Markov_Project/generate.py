from matrix import *
from markov import *
import sys

def main(file, model_name, k):
    file = file
    model_name = model_name

    # print('Enter the starting word')
    # origin = input()
    # print('Enter the size of the sentence')
    # size = int(input())
    print('Reading corpus...')
    words = tokenize(file)
    print('Corpus read')
    print('')
    ind = gen_index(words)

    k = k
    origin = 'and'

    origin = origin.split(' ')

    dm = dict_model(words, k=k)
    model = transition_model(dm, ind)
    model = normalize(model, ind)
    print('Model created')
    print('')

    save(model, ind, model_name)

if __name__ == '__main__':
    main(file='data/corpus3.txt', model_name='models/model1.txt', k=3)