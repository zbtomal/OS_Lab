def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, p in enumerate(processes):
        for j, b in enumerate(blocks):
            if b >= p:
                allocation[i] = j
                blocks[j] -= p
                break
    print("Process\tSize\tBlock")
    for i, a in enumerate(allocation):
        print(f"{i}\t{processes[i]}\t{a if a != -1 else 'Not Allocated'}")

first_fit([100, 500, 200, 300, 600], [212, 417, 112, 426])