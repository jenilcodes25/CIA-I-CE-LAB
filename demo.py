from collections import defaultdict

# Grammar Definition
grammar = {
    "E": [["T", "E'"]],
    "E'": [["+", "T", "E'"], ["%"]],
    "T": [["F", "T'"]],
    "T'": [["*", "F", "T'"], ["%"]],
    "F": [["(", "E", ")"], ["id"]]
}

non_terminals = list(grammar.keys())
first = defaultdict(set)
follow=defaultdict(set)


terminals = set()
for head in grammar:
    for production in grammar[head]:
        for symbol in production:
            if symbol not in non_terminals and symbol != "%":
                terminals.add(symbol)

#First Symbol
def firstt():
    changed=True
    while changed:
        changed=False
        for head in grammar:
            for production in grammar[head]:
                for symbol in production:
                    before = len(first[head])
                    if symbol in terminals:
                        first[head].add(symbol)
                        break
                    elif symbol == "%":
                        first[head].add("%")
                        break
                    else:
                        first[head] |= (first[symbol]-{"%"})
                        if "%" not in first[symbol]:
                            break
                else:
                    first[head].add("%")
                
                if before != len(first[head]):
                    changed=True

follow=defaultdict(set)

def followw():
    start = non_terminals[0]
    follow[start].add("$")
    changed=True
    while changed:
        changed=False
        for head in grammar:
            for production in grammar[head]:
                trailer = follow[head].copy()
                for symbol in reversed(production):
                    if symbol in non_terminals:
                        before = len(follow[symbol])
                        follow[symbol] |= trailer

                        if "%" in first[symbol]:
                            trailer |= (first[symbol]-{"%"})
                        else:
                            trailer = first[symbol]

                        if before != len(follow[symbol]):
                            changed=True
                    else:
                        trailer={symbol}

                    

firstt()
followw()

print("FIRST Sets:")
for nt in non_terminals:
    print(f"FIRST({nt}) = {first[nt]}")

print("\nFOLLOW Sets:")
for nt in non_terminals:
    print(f"FOLLOW({nt}) = {follow[nt]}") 
