import re
import time

import numpy as np
from bintrees import FastRBTree
import matplotlib.pyplot as plt

vocab_gb = []
grail = []

"""question 3"""
def count_word(vocab, text_ref):
    cnt = 0
    start_process = time.time()

    for item_ref in text_ref:
        if item_ref in vocab:
            cnt += 1

    time_process = time.time() - start_process

    return cnt, time_process

def decode(file):
    words = []

    sepwords = re.compile("[^a-zA-Z']+")
    with open(file) as f:
        for line in f:
            for word in sepwords.split(line.strip()):
                if len(word) > 0:
                    words.append(word)

    return words

def get_first_word(list_word, nb_word):
    tree = FastRBTree()

    list = list_word[:nb_word]
    dico = set(list)

    for i in range(nb_word):
        tree.insert(list_word[i], None)

    return list, dico, tree


def main():
    grail = decode("grail.txt")
    vocab_gb = decode("dico_gb.txt")

    """ question 4 à 6 """
    # vocab_hundred_word_list, vocab_hundred_word_set, vocab_hundred_word_tree = get_first_word(vocab_gb, 100)
    #
    # #print(vocab_hundred_word_list, vocab_hundred_word_set, vocab_hundred_word_tree, sep="\n")
    #
    # cnt, time_process = count_word(vocab_hundred_word_list, grail)
    # print("cnt: %s, time process: %s" %(cnt, time_process))
    # cnt, time_process = count_word(vocab_hundred_word_set, grail)
    # print("cnt: %s, time process: %s" %(cnt, time_process))
    # cnt, time_process = count_word(vocab_hundred_word_tree, grail)
    # print("cnt: %s, time process: %s" %(cnt, time_process))

    #nb_words = [100, 300, 1000, 3000, 10000, 30000, 50000]
    nb_words = np.linspace(1, 50000, 100)
    time_list = []
    time_set = []
    time_tree = []

    for i_word in nb_words:
        nb_word = round(i_word)
        vocab_word_list, vocab_word_set, vocab_word_tree = get_first_word(vocab_gb, nb_word)
        print("nb word", nb_word)

        cnt, time_process = count_word(vocab_word_list, grail)
        time_list.append(time_process)
        cnt, time_process = count_word(vocab_word_set, grail)
        time_set.append(time_process)
        cnt, time_process = count_word(vocab_word_tree, grail)
        time_tree.append(time_process)

    #plt.plot(nb_words, time_list, label="list")
    plt.plot(nb_words, time_set, label="set")
    plt.legend()
    plt.show()
    plt.plot(nb_words, time_tree, label="tree")
    plt.legend()
    plt.show()



if __name__ == '__main__':
    main()





