''' program to add the elements of 2 arrays that are of the same dimension.(Hint:Usemapmethod.) '''

li1 = [1,2,3,4]

li2 = [5,6,7,8]

li3 = list(map(lambda x,y : x + y , li1 ,li2 ))

print(li3)