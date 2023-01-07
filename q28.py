with open('q28.txt', 'r') as myfile:
    lines = myfile.readlines()

last_col = lines[0].strip()
patterns = lines[1].strip().split(" ")

first_col = sorted(last_col)
first_col_temp = first_col.copy()
last_to_first = []
for e in last_col:
    ind = first_col_temp.index(e)
    last_to_first.append(ind)
    first_col_temp[ind] = "*"


def BWMatching(last_col, pattern, last_to_first):
    top = 0
    bottom = len(last_col) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[0:len(pattern) - 1]
            top_to_bottom = last_col[top: (bottom + 1)]
            if symbol in top_to_bottom:
                top_index = top_to_bottom.index(symbol) + top
                bottom_index = len(top_to_bottom) - 1 - top_to_bottom[::-1].index(symbol) + top
                top = last_to_first[top_index]
                bottom = last_to_first[bottom_index]
            else:
                return 0
        else:
            return bottom - top + 1


matches = ''
for pattern in patterns:
    num = BWMatching(last_col, pattern, last_to_first)
    matches += str(num) + " "

print(matches)
# BWMATCHING(FirstColumn, LastColumn, Pattern, LastToFirst)
#         top ← 0
#         bottom ← |LastColumn| − 1
#         while top ≤ bottom
#             if Pattern is nonempty
#                 symbol ← last letter in Pattern
#                 remove last letter from Pattern
#                 if positions from top to bottom in LastColumn contain an occurrence of symbol
#                     topIndex ← first position of symbol among positions from top to bottom in LastColumn
#                     bottomIndex ← last position of symbol among positions from top to bottom in LastColumn
#                     top ← LastToFirst(topIndex)
#                     bottom ← LastToFirst(bottomIndex)
#                 else
#                     return 0
#             else
#                 return bottom − top + 1
