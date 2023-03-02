import random
t = random.randint(1, 10)

print(t)
for i in range(t):
    n = random.randint(1, 500)
    m = random.randint(1, 5000)
    g = random.randint(0, n)
    print("{0} {1} {2}".format(n, m, g))
    for j in range(n):
        print(random.randint(1,50), end=" ")
    print()

    for j in range(m):
        print("{0} {1} {2}".format(j % (n+1), random.randint(0,n),random.randint(1,50)))

    print()

