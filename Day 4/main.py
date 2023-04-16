# part 1
with open("pairs.txt") as file:
    enclosed = 0
    for item in file:
        pairs = item.strip().split(',')
        first = pairs[0].split('-')
        second = pairs[1].split('-')

        first[0] = int(first[0])
        first[1] = int(first[1])
        second[0] = int(second[0])
        second[1] = int(second[1])

        if second[0] <= first[0] <= second[1] and second[0] <= first[1] <= second[1]:
            enclosed += 1
        elif first[0] <= second[0] <= first[1] and first[0] <= second[1] <= first[1]:
            enclosed += 1

    print("part 1 answer: ", enclosed)

    file.close()

# part 2
with open("pairs.txt") as file:
    enclosed = 0
    for item in file:
        pairs = item.strip().split(',')
        first = pairs[0].split('-')
        second = pairs[1].split('-')

        first[0] = int(first[0])
        first[1] = int(first[1])
        second[0] = int(second[0])
        second[1] = int(second[1])

        if second[0] <= first[0] <= second[1] or second[0] <= first[1] <= second[1]:
            enclosed += 1

        elif first[0] <= second[0] <= first[1] or first[0] <= second[1] <= first[1]:
            enclosed += 1

    print("part 2 answer: ",enclosed)

    file.close()