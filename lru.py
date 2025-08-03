def lru(pages, capacity):
    memory = []
    faults = 0
    for p in pages:
        if p not in memory:
            if len(memory) == capacity:
                memory.pop(0)
            faults += 1
        else:
            memory.remove(p)
        memory.append(p)
    print("Page Faults:", faults)

#TEST
lru([1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5], 3)