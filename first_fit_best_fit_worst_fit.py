def first_fit(blocks, processes):
    print("First Fit:")
    allocation = [-1] * len(processes)
    for i, p in enumerate(processes):
        for j, b in enumerate(blocks):
            if b >= p:
                allocation[i] = j
                blocks[j] -= p
                break
    for i, a in enumerate(allocation):
        print(f"Process {i} -> Block {a if a != -1 else 'Not Allocated'}")

def best_fit(blocks, processes):
    print("\nBest Fit:")
    allocation = [-1] * len(processes)
    for i, p in enumerate(processes):
        best = -1
        for j, b in enumerate(blocks):
            if b >= p and (best == -1 or b < blocks[best]):
                best = j
        if best != -1:
            allocation[i] = best
            blocks[best] -= p
    for i, a in enumerate(allocation):
        print(f"Process {i} -> Block {a if a != -1 else 'Not Allocated'}")

def worst_fit(blocks, processes):
    print("\nWorst Fit:")
    allocation = [-1] * len(processes)
    for i, p in enumerate(processes):
        worst = -1
        for j, b in enumerate(blocks):
            if b >= p and (worst == -1 or b > blocks[worst]):
                worst = j
        if worst != -1:
            allocation[i] = worst
            blocks[worst] -= p
    for i, a in enumerate(allocation):
        print(f"Process {i} -> Block {a if a != -1 else 'Not Allocated'}")

# Test
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
first_fit(blocks[:], processes)
best_fit(blocks[:], processes)
worst_fit(blocks[:], processes)
