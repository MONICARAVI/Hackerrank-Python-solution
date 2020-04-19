from collections import OrderedDict
n = int(input())
word_dict = OrderedDict()
for _ in range(n):
    word = input()
    word_dict[word] = word_dict.get(word,0)+1
print(len(word_dict))
for v in word_dict.values():
    print(v,end=' ')
