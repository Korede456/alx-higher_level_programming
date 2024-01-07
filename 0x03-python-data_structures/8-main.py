#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
sentence2 = ""
length, first = multiple_returns(sentence)
lengt, fir = multiple_returns(sentence2)
print("length: {:d} - First character: {}".format(length, first))
print("length: {:d} - First character: {}".format(lengt, fir))
