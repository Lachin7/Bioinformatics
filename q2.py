dna = input()

# A --> X --> T
# T --> Y --> A
# G --> Z --> C
# C --> K --> G

result = dna.replace('A', 'X').replace('T', 'Y').replace('G', 'Z').replace('C', 'K').replace('X', 'T').replace('Y', 'A').replace(
    'Z', 'C').replace('K', 'G')

print(result[::-1])
