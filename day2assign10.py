inp = "How much wood would a wood chuck chuck if the wood chuck could chuck wood"
uni_lst = []
li = inp.split(" ")

di = {}

for i in li:
    if not i in di:
        di[i] = 1
    else:
        di[i] += 1

for key in di:
    if di[key] == 1:
        uni_lst.append(key)
    print(f"{key} : {di[key]}")

print("unique item length is " ,len(uni_lst))