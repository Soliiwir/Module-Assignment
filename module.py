import random
Start = 0
End = 500

totalNumber =5

list =[]

for i in range(totalNumber):
    randomNumber = random.randrange(Start, End)
    list.append(randomNumber)

print("List:", list)