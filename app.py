def occupied(N,y,t):
    found = 0
    for i in range(N):
        if y[i] == "C" and t[i] == "C":
            found += 1
    print(found)
    occupied(5, "CC.CC", ".CC..")
