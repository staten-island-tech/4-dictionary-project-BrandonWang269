""" def occupied(N,y,t):
    found = 0
    for i in range(N):
        if y[i] == "C" and t[i] == "C":
            found += 1
    print(found)
    occupied(5, "CC.CC", ".CC..") """

""" def language(sent):
    t = 0
    s = 0
    for i in sent:
        if i == "s" or i == "S":
            s +=1
        elif i == "t" or i == "T":
            t +=1
    if s >= t:
        print('French')
    else:
        print('English')
language('The red cat sat on the mat.') """

def croation(COCI):
    search = 1
    H == 1
    O == 2
    N == 3
    I == 4
    for i in COCI:
        if i == 'H':
            H +=1
            search = 2
        elif i == "O":
            O +=1
            search = 3
        elif i == 'N':
            N +=1
            search = 4
        elif i == 'I':
            I +=1
            search +=1
            search = 1
        if search + 1:
         print('search')
        croation('PROHODNIHODNIK')