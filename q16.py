import numpy as np

whole_string = ""
with open('q16.txt', 'r') as myfile:
    lines = myfile.readlines()

for line in lines:
    if line.startswith(">"):
        whole_string = whole_string + line.strip() + ">"
    else:
        whole_string = whole_string + line.strip()

strings = whole_string.split(">")[1:]
# extract only the dna parts and not the id
strings = strings[1::2]
n = len(strings)

def hamming_dist(string1, string2):
    return sum(s1 != s2 for s1, s2 in zip(string1, string2))

corrects = []
incorrects = []
for s in strings:
    complement = (s.replace('A', 'X').replace('T', 'Y').replace('G', 'Z').replace('C', 'K').replace('X', 'T').replace('Y', 'A').replace(
    'Z', 'C').replace('K', 'G'))[::-1]
    if complement in strings or strings.count(s) > 1:
        corrects.append(s)
    else:
        incorrects.append(s)

# print(corrects)
corrects = list(dict.fromkeys(corrects))
incorrects = list(dict.fromkeys(incorrects))
# print(incorrects)
# print(corrects)
res = {}
for incorrect in incorrects:
    for correct in corrects:
        complement = (correct.replace('A', 'X').replace('T', 'Y').replace('G', 'Z').replace('C', 'K').replace('X','T').replace('Y', 'A').replace('Z', 'C').replace('K', 'G'))[::-1]
        # print(complement)

        if hamming_dist(correct, incorrect) == 1:
            res[incorrect] = correct

        elif hamming_dist(incorrect, complement) == 1:
            res[incorrect] = complement



for key, value in res.items():
    print(key+'->'+value)