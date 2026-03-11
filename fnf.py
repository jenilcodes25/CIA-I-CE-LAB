table = {}

# Read LL(1) table
n = int(input("Enter number of table entries: "))
print("Enter entries as: NonTerminal Terminal Production")

for i in range(n):
    nt, t, prod = input().split()
    table[(nt, t)] = prod

# Input string
inp = list(input("Enter input string: "))
inp.append('$')

stack = ['$', 'S']
i = 0

print("\nSTACK\tINPUT\tACTION")

while True:

    top = stack[-1]
    sym = inp[i]

    print(stack, "\t", inp[i:], "\t", end="")

    # Match terminal
    if top == sym:
        stack.pop()
        i += 1
        print("Match")

    # Use table rule
    elif (top, sym) in table:

        prod = table[(top, sym)]
        print(top, "->", prod)

        stack.pop()

        if prod != "@":
            for s in reversed(prod):
                stack.append(s)

    else:
        print("Error")
        print("Input String is invalid")
        break

    if stack == ['$'] and inp[i] == '$':
        print("Input String is valid")
        break