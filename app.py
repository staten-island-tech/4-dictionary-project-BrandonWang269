""" def occupied(N,y,t):
    found = 0
    for i in range(N):
        if y[i] == "C" and t[i] == "C":
            found += 1
    print(found)
    occupied(5, "CC.CC", ".CC..") """

def language(sent):
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
language('The red cat sat on the mat.')