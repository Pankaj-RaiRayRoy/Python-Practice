names = []
scores = []
total = 0

def analyze_performance(names, scores):
    lowest = scores[0]
    index = 0
    for counter in range(len(scores)):
        if scores[counter] < lowest:
            lowest = scores[counter]
            index = counter

    #for counter in range(len(scores)):
        #total = total + scores[counter]

    print("The average team scores is : ", total / len(scores))
    print("The lowest score in the team is : ", lowest)
    print("Employee with the lowest score is  :", names[index])




while True:
    member = input("Enter the employee's name ('done' to exit): ")
    if member == 'done':
        break
    else:
        names.append(member)

while True:
    performance = input("Enter the corresponding scores : ")
    if performance == 'done':
        break
    else:
        scores.append(performance)
    total = total + int(performance)

analyze_performance(names, scores)
