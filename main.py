import sys
import os


class Node:
    def __init__(self):
        self.children = {
            'A': None,
            'C': None,
            'G': None,
            'T': None
        }
        self.target = ""

    def set_child(self, child):
        self.children[child] = Node()

    def set_target(self, target):
        self.target = target

    def get_child(self, nucleotide):
        return self.children[nucleotide]

    def get_target(self):
        return self.target


class Trie:
    def __init__(self, sequence_list):
        self.root = Node()
        for sequence in sequence_list:
            self.insert(sequence)

    def insert(self, sequence):
        current = self.root
        for nucleotide in sequence:
            if nucleotide == '/' or 'n':
                pass
            if current.get_child(nucleotide) is None:
                current.set_child(nucleotide)
                current.target += nucleotide
            current = current.get_child(nucleotide)

    def find(self, gene, filename):
        i = 0
        holder = ""
        leaf = {'A': None, 'C': None, 'G': None, 'T': None}
        while i < len(gene):
            current = self.root
            j = i
            while current is not None:
                nucleotide = gene[j].upper()
                if nucleotide == 'N':
                    break
                current = current.get_child(nucleotide)
                if current is None:
                    break
                if current.children == leaf or current.get_target() is not None:
                    holder += filename + "\t" + str(i) + "\t" + current.get_target()
                    break
                j += 1
            i += 1
        return holder


with open(sys.argv[1], 'r', encoding='utf8') as d:
    targets = d.read().splitlines()

targettrie = Trie(targets)

with open(sys.argv[3], 'w', encoding='utf8') as g:
    for filename in os.listdir(sys.argv[2]):
        with open(os.path.join(sys.argv[2], filename), 'r', encoding='utf8') as f:
            genome = f.read().splitlines()
            for gene in genome:
                g.write(targettrie.find(gene, filename))


