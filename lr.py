grammar, action, goto = {}, {}, {}

# Read productions
n = int(input("Enter number of productions: "))
for i in range(1, n+1):
    p = input("Production: ")
    l, r = p.split("->")
    grammar[i] = (l.strip(), r.strip().split())

# Read ACTION table
n = int(input("Enter number of ACTION entries: "))
for _ in range(n):
    s, a, b = input().split()
    action[(int(s), a)] = b

# Read GOTO table
n = int(input("Enter number of GOTO entries: "))
for _ in range(n):
    s, a, b = input().split()
    goto[(int(s), a)] = int(b)

# Read input string
inp = input("Enter input string: ").split() + ["$"]

stack = [0]
i = 0

print("\nSTACK\t\tINPUT\t\tACTION")

while True:
    state = stack[-1]
    sym = inp[i]

    if (state, sym) not in action:
        print(stack, "\t", inp[i:], "\tError")
        print("Input String is invalid")
        break

    act = action[(state, sym)]
    print(stack, "\t", inp[i:], "\t", act)

    # Accept
    if act == "acc":
        print("Input String is valid")
        break

    # Shift
    elif act.startswith("S"):
        stack += [sym, int(act[1:])]
        i += 1

    # Reduce
    elif act.startswith("R"):
        p = int(act[1:])
        lhs, rhs = grammar[p]

        for _ in range(len(rhs) * 2):
            stack.pop()

        state = stack[-1]
        stack += [lhs, goto[(state, lhs)]]





📥 Example Input to Run
1
S->a
2
0 a S1
1 $ acc
1
0 S 2
a
📤 Example Output
Stack           Input           Action
[0]             ['a', '$']      S1
[0, 'a', 1]     ['$']           acc
Input String is valid
