import itertools

r = int(input("Enter Number of rows"))
c = int(input("Enter Number of columns"))

main_list = []

for i in range(r):
  temp_list = []
  for j in range(c):
    temp_list.append(input("Element {0}:{1}: ".format(i, j)))
  main_list.append(temp_list)

i = 0

for l in main_list:
    print(f"Max Of {i} th Row is : {max(l)}")
    i += 1

i = 0

for l in main_list:
    print(f"Min Of {i} th Row is : {min(l)}")
    i += 1
    
l=list(itertools.chain.from_iterable(main_list))

print(f"Max of all elements in list is {max(l)} and min is {min(l)}")
