inputFile = open("direct_LR_input.txt", "r")
production = inputFile.read()
print("*******TEXT INPUT*******\n", production)

p = production.split("->")

for i in range(0, len(p)):
    p[i] = p[i].strip(" ")
    #print(p[i])

non_Terminal = p[0]
print("Non Terminal =", non_Terminal)

RHS = p[1].split("|")
terms_With_LR_Term = {}
terms_Without_LR_Term = {}

for i in range(0, len(RHS)):
    if RHS[i] != RHS[i].strip(non_Terminal):
        terms_With_LR_Term[len(terms_With_LR_Term)] = RHS[i]
        #print("LR term exists")
    else:
        terms_Without_LR_Term[len(terms_Without_LR_Term)] = RHS[i]
        #print("LR term does not exist")

#print(terms_With_LR_Term)
#print(terms_Without_LR_Term)
new_RHS = ["",""]

new_Non_Terminal = non_Terminal + "'"
print("New Non Terminal =", new_Non_Terminal)
print()
for i in range(0, len(terms_Without_LR_Term)):
    new_RHS[0] = new_RHS[0] + terms_Without_LR_Term[i] + new_Non_Terminal + "|"
new_RHS[0] = new_RHS[0][:-2]

for i in range(0, len(terms_With_LR_Term)):
    new_RHS[1] = new_RHS[1] + terms_With_LR_Term[i].strip(non_Terminal) + new_Non_Terminal + "|"
new_RHS[1] = new_RHS[1] + "epsilon"

print("*****OUTPUT*****")
print(non_Terminal + "->" + new_RHS[0])
print(new_Non_Terminal + "->" + new_RHS[1])