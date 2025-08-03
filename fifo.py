def fifo(pages, capacity):
    memory = []
    faults = 0
    for p in pages:
        if p not in memory:
            if len(memory) == capacity:
                memory.pop(0)
            memory.append(p)
            faults += 1
    print("Page Faults:", faults)

fifo([1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5], 3)