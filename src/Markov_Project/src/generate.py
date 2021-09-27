from matrix import *
from markov import *

def main(file, length=None, origin=None):
    file = file
    print('Reading Corpus...')
    words = tokenize(file)
    ind, model = gen_model(words)
    print('[Completed]')
    print('\nCreating Model...')
    model = normalize(model)
    print('[Completed]\n')

    if origin == None:
        origin = random.choice(words)
    
    vector = word_to_vector(origin, ind)

    print('Generating Sentence...')
    s = generate(model, vector, ind, length)
    print('[Completed]\n')
    s = origin + ' ' + s
    print('\n------Sentence------')
    print(s.capitalize())


if __name__ == '__main__':
    main(file='data/corpus3.txt')
