import random

tam=random.randint(5,15)
t=()
for i in range(tam):
    n=random.randrange(100)
    t+=(n,)

print(t)

mitadTupla=t[:3]
print(mitadTupla)
