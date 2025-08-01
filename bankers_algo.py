def is_safe(processes, avail, maxm, allot):
    n = len(processes)
    m = len(avail)
    need = [[maxm[i][j] - allot[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    safe_seq = []
    work = avail.copy()

    while len(safe_seq) < n:
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                work = [work[j] + allot[i][j] for j in range(m)]
                finish[i] = True
                safe_seq.append(i)
                break
        else:
            print("System is not in a safe state")
            return False
    print("Safe sequence:", safe_seq)
    return True

# Test
processes = [0, 1, 2, 3, 4]
avail = [3, 3, 2]
maxm = [[7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]]
allot = [[0, 1, 0],
         [2, 0, 0],
         [3, 0, 2],
         [2, 1, 1],
         [0, 0, 2]]
is_safe(processes, avail, maxm, allot)
