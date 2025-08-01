def bankers_algorithm():
    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resources: "))

    allocation = []
    maxm = []
    available = []

    print("\nEnter Allocation Matrix:")
    for i in range(n):
        allocation.append(list(map(int, input().split())))

    print("\nEnter Max Matrix:")
    for i in range(n):
        maxm.append(list(map(int, input().split())))

    print("\nEnter Available Resources:")
    available = list(map(int, input().split()))

    # Calculate Need Matrix = Max - Allocation
    need = [[maxm[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    finish = [False] * n
    safe_seq = []
    count = 0

    while count < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= available[j] for j in range(m)):
                    for k in range(m):
                        available[k] += allocation[i][k]
                    safe_seq.append(i)
                    finish[i] = True
                    count += 1
                    found = True
        if not found:
            break

    if count != n:
        print("\nDeadlock detected!")
    else:
        print("\nSafe Sequence: ", end="")
        for p in safe_seq:
            print(f"P{p}", end=" ")
        print()


# Run the function
bankers_algorithm()
