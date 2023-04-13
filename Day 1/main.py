# part 1
with open("calories.txt") as file:
    num = 0
    max_num = 0

    for item in file:
        if item == '\n':
            max_num = max(num, max_num)
            num = 0
        else: 
            num += int(item)

    print("part 1 answer: ", max_num)
file.close()


# part 2
with open("calories.txt") as file:
    num = 0
    maxvals = [0, 0, 0]

    for item in file:
        if item == '\n':
            maxvals.append(num)
            maxvals.sort(reverse=True)
            maxvals.pop()
            num = 0

        else: 
            num += int(item)
    
    max3sum = sum(maxvals)
    print("part 2 answer: ", max3sum)
file.close()