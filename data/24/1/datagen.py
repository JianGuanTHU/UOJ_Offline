
import numpy as np
import random
import string
ds = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Subday"]
rm = []

def check(m1, d1):
    for r in rm:
        if r[0] == m1 and r[1] == d1:
            return False
    return True
for d in range(1, 11):
    print(d)
    rm = []
    f = open("data"+str(d)+".in", "w")
    f.write("100\n")
    for i in range(1, 101):
        m1, d1 = np.random.randint(1, 13), np.random.randint(1, 29)
        while not check(m1, d1):
            m1, d1 = np.random.randint(1, 13), np.random.randint(1, 29)
        rm.append((m1, d1))
        f.write(str(m1) + " " + str(d1) + " " + random.choice(ds) + "\n")
    f.write("100\n")
    for i in range(1, 101):
        r = random.choice(rm)
        s = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
        f.write(str(r[0]) + " " + str(r[1]) + " " + s + "\n")
    
