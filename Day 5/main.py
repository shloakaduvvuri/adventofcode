# part 1
with open("crates.txt") as file:
    idx = 0
    arr_of_stacks = [[], [], [], [], [], [], [], [], []]
    
    for item in file:
        if idx < 8: # populate 9 stacks in reverse order
            i = 1
            j = 0
            while i < len(item):
                if item[i] != ' ':
                    arr_of_stacks[j].append(item[i])   
                j += 1
                i += 4
            idx += 1

        elif idx == 8: # reverse the 9 stacks
            for i in range(9):
                arr_of_stacks[i].reverse()
            idx += 2

        else:
            words = item.split()
            if len(words) != 0:
                quantity = int(words[1])
                source = int(words[3])
                destination = int(words[5])
                for i in range(quantity):
                    crate = arr_of_stacks[source - 1].pop()
                    arr_of_stacks[destination - 1].append(crate)

    print(arr_of_stacks)
    file.close()
    
# part 2
with open("crates.txt") as file:
    idx = 0
    arr_of_stacks = [[], [], [], [], [], [], [], [], []]
    
    for item in file:
        if idx < 8: # populate 9 stacks in reverse order
            i = 1
            j = 0
            while i < len(item):
                if item[i] != ' ':
                    arr_of_stacks[j].append(item[i])   
                j += 1
                i += 4
            idx += 1

        elif idx == 8: # reverse the 9 stacks
            for i in range(9):
                arr_of_stacks[i].reverse()
            idx += 2

        else:
            words = item.split()
            if len(words) != 0:
                quantity = int(words[1])
                source = int(words[3])
                destination = int(words[5])
                for i in range(quantity):
                    crate = arr_of_stacks[source - 1].pop(len(arr_of_stacks[source - 1]) - quantity)
                    arr_of_stacks[destination - 1].append(crate)
                    quantity -= 1

    print(arr_of_stacks)
    file.close()
