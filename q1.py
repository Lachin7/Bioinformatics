max_id = 0
max_gc_content = 0

whole_string = ""
with open('q1.txt', 'r') as myfile:
    lines = myfile.readlines()

for line in lines:
    if line.startswith(">"):
        whole_string = whole_string + line.strip() + ">"
    else:
        whole_string = whole_string + line.strip()

strings = whole_string.split(">")[1:]
size = len(strings)
for i in range(int(size/2)):
    id = strings[i*2]
    dna = strings[i*2+1]
    c_count = dna.count('C')
    g_count = dna.count('G')
    gc_content = (c_count + g_count) / len(dna)

    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_id = id


print(max_id)
print(max_gc_content*100)
