# import sys


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.count = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.is_word = True
        node.count += 1

    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.count

    def startsWith(self, prefix=""):
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True

    def traverse(self, node, prefix=""):
        if node.is_word:
            print "{}\toccurred {} times".format(prefix, node.count)
        if node.children:
            for letter, child in node.children.items():
                self.traverse(child, prefix + letter)

    def traverse_all(self):
        # Analyze allocation of memory
        # print sys.getsizeof(self.root)
        return self.traverse(self.root)
