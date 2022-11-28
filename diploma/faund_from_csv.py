while True:
    # index += 1
    for line in list_reader:

        found = False
        # print(line)  # список про 1 человека
        for elem in line:

            # print(elem) # разбили по слову
            if elem.find(poick) != -1:  # если есть совпадение
                #
                found = True
                continue

        if found:
            print(line)
    break