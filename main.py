#!/usr/bin/python3
import os

os.system('python3 src/generate.py')

print('\n\n------Benchmark------')
os.system('python3 src/benchmark.py')

# os.system('python3 src/grammar.py data/corpus3.txt')