import sys
import random as ran




n = 20000
r = 75000

print("1")
print("20000 75000")
for i in range(0, r):
    AF = ran.randrange(0,2)
    if AF == 0:
        print("A "+str(ran.randrange(1, n))+" "+ str(ran.randrange(1, n)))

    else:
        print("F " + str(ran.randrange(1, n))+" "+ str(ran.randrange(1, n)))


