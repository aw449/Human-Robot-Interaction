import numpy as np

from trie import Trie

raw_data = np.load("test.npy")
t = Trie()
for n in range(len(raw_data)):
    t.__setitem__(raw_data[n][0], raw_data[n][1])

sub = []
trj = []
arm = []
cup = []
spd = []
while True:
    i = input("Enter desired subjects(001-007) or 0 for all subjects:")
    if i == '0':
        break
    else:
        i = "".join("_")
        sub.append(i)
while True:
    i = input("Enter desired trajectories(claw,curve,straight,straight_down,short) or 0 for all trajectories:")
    if i == '0':
        break
    else:
        i = "".join("_")
        trj.append(i)
while True:
    i = input("Enter desired manipulator arm(right, left) or 0 for all arms:")
    if i == '0':
        break
    else:
        i = "".join("_")
        arm.append(i)
while True:
    i = input("Enter desired cups(0-12) or 0 for all arms:")
    if i == '0':
        break
    else:
        i = "".join("_")
        cup.append(i)
while True:
    i = input("Enter desired speeds(5,10,15) or 0 for all speeds:")
    if i == '0':
        break
    else:
        i = "".join(".0.ts")
        spd.append(i)

m = False
o = False
# A completely inefficient search
if sub:
    if trj:
        if arm:
            if cup:
                if spd:
                    for i in range(len(sub)):
                        for j in range(len(trj)):
                            for k in range(len(arm)):
                                for l in range(len(cup)):
                                    for m in range(len(spd)):
                                        h = (sub[i], "trj_", trj[j], arm[k], cup[l], spd[m])
                                        prf = "".join(h)
                                        m = True
                else:
                    for i in range(len(sub)):
                        for j in range(len(trj)):
                            for k in range(len(arm)):
                                for l in range(len(cup)):
                                    h = (sub[i], "trj_", trj[j], arm[k], cup[l])
                                    prf = "".join(h)
                                    m = True
            else:
                for i in range(len(sub)):
                    for j in range(len(trj)):
                        for k in range(len(arm)):
                            h = (sub[i], "trj_", trj[j], arm[k])
                            prf = "".join(h)
                            o = True
        else:
            for i in range(len(sub)):
                for j in range(len(trj)):
                    h = (sub[i], "trj_", trj[j])
                    prf = "".join(h)
    else:
        for i in range(len(sub)):
            h = (sub[i], "trj_")
            prf = "".join(h)
else:
    prf = ""

keys = t.keys(prf)
values = []
if m:
    for i in range(len(keys)):
        values.append(t.get(keys[i]))


else:
    ls = []
    if trj:
        ls.append(trj)
    if arm:
        ls.append(arm)

    if cup:
        ls.append(cup)

    if spd:
        ls.append(arm)

    new_keys = []
    for i in range(len(keys)):
        if all(it in keys[i] for it in ls):
            new_keys.append(keys[i])
    if not o:
        for i in range(len(trj)):
            if trj[i] == "straight_down_":
                b = True
            if trj[i] == "straight_":
                a = True
        if a and not b:
            # search for any straight_down_ since both share the same prefix
            for i in range(len(list(new_keys))):
                if new_keys[i].__contains__("stright_down_"):
                    new_keys.pop(i)

    for i in range(len(new_keys)):
        values.append(t.get(new_keys[i]))




