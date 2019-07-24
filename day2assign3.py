''' program to determine the work hours of the day entered based on the timetable provided below. '''

li = ["mon" , "tue" , "wed" , "thur" ,"fri" , "sat" , "sun"]

week1 = [3,3,3,3,3,3,0]
week2 = [2,2,2,2,2,1,0]
week3 = [2,2,2,1,1,0,0]

inp = input("Enter Which Day u want to check :")

inp = inp.lower()

ind = li.index(inp)

l1 = [i for i in zip(week1,week2,week3) ]

print(l1[ind])

