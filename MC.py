def Answer(A,B,C):
    correct = 0
    for i in range(A):
        if B[i] == C[i]:
            correct += 1
    print(correct)
Answer(7, "AAAAAAA", "AAAAAAB")
Answer(3, "ACA", "BCA")