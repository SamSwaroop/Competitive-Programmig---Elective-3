text="HelloWorld"

f=set(text)
print(f)
g=list(f)
print(g)
# w="".join(g)
# print(w)
w=""
for i in range(len(text)):
    if(text[i] in g):
        w+=text[i]
        g.pop(g.index(text[i]))

print(w)




