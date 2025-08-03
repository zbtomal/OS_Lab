def bankers(n, m, alloc, maxm, avail):
    need = [[maxm[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    safe_seq = []
    work = avail.copy()

    while len(safe_seq) < n:
        allocated = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += alloc[i][j]
                finish[i] = True
                safe_seq.append(i)
                allocated = True
        if not allocated:
            print("System is not in safe state")
            return
    print("Safe sequence:", " -> ".join(f"P{p}" for p in safe_seq))

# Example
n = 5  # processes
m = 3  # resources
alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
maxm = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
avail = [3, 3, 2]
bankers(n, m, alloc, maxm, avail)