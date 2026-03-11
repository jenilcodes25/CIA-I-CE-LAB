from collections import defaultdict

# number of parsing table entries
n = int(input("Enter number of table entries: "))

table = defaultdict(dict)

start = None

# reading table entries
for i in range(n):
    nt, terminal, production = input().split()

    if start is None:
        start = nt

    table[nt][terminal] = production

# input string
inp = list(input("\nEnter input string: "))
inp.append('$')

stack = ['$', start]

print("\nSTACK\t\tINPUT\t\tACTION")

while True:

    top = stack[-1]
    current = inp[0]

    print(stack, inp, end=" ")

    # accept condition
    if top == '$' and current == '$':
        print("Match")
        print("Input String is valid")
        break

    # if terminal
    if top == current:
        stack.pop()
        inp.pop(0)
        print("Match")

    # if non terminal
    elif top in table and current in table[top]:

        production = table[top][current]
        stack.pop()

        print(f"{top} -> {production}")

        if production != '@':
            for sym in reversed(production):
                stack.append(sym)

    else:
        print("\nInput String is invalid")
        break





Example Input
Enter number of table entries: 3
S a aA
A b b
A $ @

Enter input string: ab
Example Output
STACK           INPUT           ACTION
['$', 'S']      ['a', 'b', '$'] S -> aA
['$', 'A', 'a'] ['a', 'b', '$'] Match
['$', 'A']      ['b', '$']      A -> b
['$', 'b']      ['b', '$']      Match
['$']           ['$']           Match
Input String is valid
