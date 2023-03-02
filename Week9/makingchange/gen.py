import random
t = random.randint(1, 20)
n = random.randint(1, 100)
c = random.randint(1, 100000)

print(t)
for i in range(t):
    n = random.randint(1, 100)
    c = random.randint(1, 100000)
    print("{0} {1}".format(n, c))
    print(1, end=" ")
    for j in range(n-1):
        print(random.randint(1,10000), end=" ")
    print()
    print()
