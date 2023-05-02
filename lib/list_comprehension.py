#!/usr/bin/env python3

def return_evens(num_list):
    even_num = [i for i in num_list if i % 2 == 0]
    return even_num
    pass

def make_exclamation(sentence_list):
    exclamation_sentence = [i + '!' for i in sentence_list]
    return exclamation_sentence