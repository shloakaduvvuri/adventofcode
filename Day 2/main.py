# part 1
with open("strategy.txt") as file:
    points = 0
    for item in file:
        opponent = item[0]
        you = item[2]

        if opponent == 'A':
            # rock rock
            if you == 'X':
                points += 4
            # rock paper
            if you == 'Y':
                points += 8
            # rock scissors
            if you == 'Z':
                points += 3

        if opponent == 'B':
            # paper rock
            if you == 'X':
                points += 1
            # paper paper
            if you == 'Y':
                points += 5
            # paper scissors
            if you == 'Z':
                points += 9

        if opponent == 'C':
            # scissors rock
            if you == 'X':
                points += 7
            # scissors paper
            if you == 'Y':
                points += 2
            # scissors scissors
            if you == 'Z':
                points += 6

    print("part 1 answer: ", points)

    file.close()

# part 2
with open("strategy.txt") as file:
    points = 0
    for item in file:
        opponent = item[0]
        you = item[2]

        if opponent == 'A':
            # lose, play scissors
            if you == 'X':
                points += 3
            # draw, play rock
            if you == 'Y':
                points += 4
            # win, play paper
            if you == 'Z':
                points += 8

        if opponent == 'B':
            # lose, play rock
            if you == 'X':
                points += 1
            # draw, play paper
            if you == 'Y':
                points += 5
            # win, play scissors
            if you == 'Z':
                points += 9

        if opponent == 'C':
            # lose, play paper
            if you == 'X':
                points += 2
            # draw, play scissors
            if you == 'Y':
                points += 6
            # win, play rock
            if you == 'Z':
                points += 7

    print("part 2 answer: ", points)

    file.close()