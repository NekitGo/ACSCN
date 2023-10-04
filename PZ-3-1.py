import itertools

def BoolTable(expression, massive, variables_eval):
    vars_for_eval = {}
    eval_massive = list(massive)
    for key in range(len(variables_eval)):
        if eval_massive[key] == 1:
            vars_for_eval[variables_eval[key]] = True
        else:
            vars_for_eval[variables_eval[key]] = False

    return eval(expression, {}, vars_for_eval)

infunc = input('Enter your function: ')
variables = sorted(set([c for c in infunc if c.isalpha()]))
n = len(variables)
infunc = infunc.replace("-", "not")
infunc = infunc.replace("+", "or")
infunc = infunc.replace("*", "and")
infunc = infunc.replace("→", "<=")
infunc = infunc.replace("⇔", "==")

header = "| " + " | ".join(variables) + " | Result |"
separator = "+-" + "-+-".join(["-" * len(variable) for variable in variables]) + "-+-------+"

print(separator)
print(header)
print(separator)

for mas in itertools.product(*[range(0, 2) for i in range(n)]):
    row = "| " + " | ".join([str(key) for key in mas]) + f" |   {BoolTable(infunc, mas, variables)}   |"
    print(row)
print(separator)
