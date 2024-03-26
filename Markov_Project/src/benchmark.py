import markovify

def main(file):
    with open(file) as f:
        text = f.read()

    # Train model
    text_model = markovify.Text(text)

    # Generate sentences
    print(text_model.make_sentence())
    print()

if __name__ == '__main__':
    main('data/corpus3.txt')
