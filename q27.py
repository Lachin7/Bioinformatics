with open('q27.txt', 'r') as myfile:
    lines = myfile.readlines()


read = lines[0].strip()
last_col = []
for char in read:
    last_col.append(char)

cols = last_col.copy()
cols.sort()
# print(cols)
while len(cols[0])!=len(read):
    # print(len(cols[0]))
    # print(len(read))
    new_cols = []
    for i in range(len(read)):
        new_cols.append(last_col[i]+cols[i])
    new_cols.sort()
    cols = new_cols

for e in cols:
    if e[-1]=="$":
        print(e)
        break


