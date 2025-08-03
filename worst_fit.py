def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, p in enumerate(processes):
        worst_idx = -1
        for j, b in enumerate(blocks):
            if b >= p and (worst_idx == -1 or blocks[j] > blocks[worst_idx]):
                worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= p
    print("Process\tSize\tBlock")
    for i, a in enumerate(allocation):
        print(f"{i}\t{processes[i]}\t{a if a != -1 else 'Not Allocated'}")

worst_fit([100, 500, 200, 300, 600], [212, 417, 112, 426])