from collections import defaultdict

g = {
    'G': ['E'],
    'E': ['TZ'],
    'Z': ['+TZ', '-TZ', '@'],
    'T': ['FY'],
    'Y': ['*FY', '/FY', '@'],
    'F': ['(E)', 'i', 'n']
}

first = {
    'G': ['(', 'i', 'n'],
    'E': ['(', 'i', 'n'],
    'Z': ['+', '-', '@'],
    'T': ['(', 'i', 'n'],
    'Y': ['*', '/', '@'],
    'F': ['(', 'i', 'n']
}

follow = {
    'G': ['$', ')'],
    'E': ['$', ')'],
    'Z': ['$', ')'],
    'T': ['+', '-', '$', ')'],
    'Y': ['+', '-', '$', ')'],
    'F': ['*', '/', '+', '-', '$', ')']
}


table = defaultdict(dict)

for nt in g:
    for prod in g[nt]:

        if prod=="@":
            for f in follow[nt]:
                table[nt][f]=prod
        else:
            symbol = prod[0]
            if symbol in first:
                for t in first[symbol]:
                    if t!="@":
                        table[nt][t]=prod
            else:
                table[nt][symbol]=prod

print("LL[1]\n")
for nt in table:
    for t in table[nt]:
        print(f"T[{nt}][{t}] = {nt} -> {table[nt][t]}")                
