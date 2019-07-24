'''program to accept an input string from the user and determine the vowels in the string and calculate the number of vowels. (Hint:Usefiltermethod.) '''

inp = input("Enter Input :")

li = ['a' , 'e' , 'i' , 'o' , 'u']

inp = inp.lower()

l2 = list(filter(lambda x: x in li , inp))

print(len(l2))