
import fileinput
import sys
from trie import Trie


def count():
    trie = Trie()
    for l in fileinput.input():
        for word in l.split():
            trie.insert(word.lower())
    trie.traverse_all()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py <file>")
        exit(-1)
    count()
