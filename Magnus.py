def croation(COCI):
    count = 0
    state = 0
    for i in COCI:
        if state == 0 and i.upper() == "H":
            state = 1
        elif state == 1 and i.upper() == "O":
            state = 2
        elif state == 2 and i.upper() == "N":
            state = 3
        elif state == 3 and i.upper() == "I":
            state = 0
            count +=1
    print(count)
croation('HHHHHHOOOOOONNNNNNNNNIIIIIIIIIIII')