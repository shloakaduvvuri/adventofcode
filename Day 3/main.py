# part 1
with open("rucksack.txt") as file:
    priority = 0
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters += letters.upper()

    for item in file:
        item = item.strip()
        size = len(item)
        sack1 = item[0:round(size/2)]
        sack2 = item[round(size/2):size]
        
        for c in sack1:
            if c in sack2:
                priority += (letters.index(c) + 1)
                break

    print("part 1 answer: ", priority)

    file.close()

# part 2
with open("rucksack.txt") as file:
    priority = 0
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters += letters.upper()

    elf1 = ""
    elf2 = ""
    elf3 = ""
    for item in file:
        item = item.strip()
        if elf1 == "":
            elf1 = item
        elif elf2 == "":
            elf2 = item
        elif elf3 == "":
            elf3 = item
            for c in elf1:
                if c in elf2 and c in elf3:
                    priority += (letters.index(c) + 1)
                    break
            elf1 = ""
            elf2 = ""
            elf3 = ""

    print("part 2 answer: ", priority)

    file.close()