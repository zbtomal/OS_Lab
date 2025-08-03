def mru(pages, capacity):
    memory = []
    faults = 0
    for p in pages:
        if p not in memory:
            if len(memory) == capacity:
                memory.pop(-1)
            faults += 1
        else:
            memory.remove(p)
        memory.append(p)
    print("Page Faults:", faults)

mru([1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5], 3)
