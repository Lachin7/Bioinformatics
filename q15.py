

protein = input()

reverse_codon_table = {'A': {'GCA', 'GCC', 'GCU', 'GCG'}, 'C': {'UGC', 'UGU'}, 'E': {'GAG', 'GAA'}, 'D': {'GAU', 'GAC'}, 'G': {'GGU', 'GGG', 'GGA', 'GGC'}, 'F': {'UUU', 'UUC'}, 'I': {'AUA', 'AUC', 'AUU'}, 'H': {'CAC', 'CAU'}, 'K': {'AAG', 'AAA'}, '*': {'UAA', 'UGA', 'UAG'}, 'M': {'AUG'}, 'L': {'CUU', 'CUG', 'CUC', 'CUA', 'UUG', 'UUA'}, 'N': {'AAU', 'AAC'}, 'Q': {'CAA', 'CAG'}, 'P': {'CCU', 'CCG', 'CCA', 'CCC'}, 'S': {'UCU', 'AGC', 'UCG', 'UCC', 'UCA', 'AGU'}, 'R': {'AGG', 'CGC', 'AGA', 'CGA', 'CGG', 'CGU'}, 'T': {'ACC', 'ACA', 'ACG', 'ACU'}, 'W': {'UGG'}, 'V': {'GUC', 'GUA', 'GUG', 'GUU'}, 'Y': {'UAC', 'UAU'}}

result = 1
for aa in protein:
    result *= len(reverse_codon_table.get(aa)) % 1000000

print(result * 3 % 1000000)

