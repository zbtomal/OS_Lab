def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i, p in enumerate(processes):
        best_idx = -1
        for j, b in enumerate(blocks):
            if b >= p and (best_idx == -1 or blocks[j] < blocks[best_idx]):
                best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= p
    print("Process \t Size \t Block")
    for i, a in enumerate(allocation):
        print(f"{i} \t\t {processes[i]} \t {a if a != -1 else 'Not Allocated'}")

best_fit([100, 500, 200, 300, 600], [212, 417, 112, 426])