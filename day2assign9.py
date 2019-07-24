inp = "Comprehensions are a feature of Python which I would really miss if I ever have to leave it.Comprehensions are constructs that allow sequences to be built from other sequences.Several types of comprehensions are supported in both Python2 and Python3"

li = inp.strip(" ").split(" ")

di = {}

for l in li:
    if not l in di:
        di[l] = 1
    else:
        di[l] += 1


ma = max(di.values())
mi = min(di.values())

