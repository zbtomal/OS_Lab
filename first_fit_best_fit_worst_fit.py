def first_fit(holes, process_size):
    for hole in holes:
        if hole >= process_size:
            print(f"First Fit: {hole}k")
            return
    print("Hey wait, you don't have sufficient space")


def best_fit(holes, process_size):
    holes.sort()
    for hole in holes:
        if hole >= process_size:
            print(f"Best Fit: {hole}k")
            return
    print("Hey wait, you don't have sufficient space")


def worst_fit(holes, process_size):
    holes.sort(reverse=True)
    if process_size <= holes[0]:
        print(f"Worst Fit: {holes[0]}k")
    else:
        print("Hey wait, you don't have sufficient space")

# Main Logic
n = input("Enter the number of Holes available: ")
holes = list(map(int, input("Enter the Hole Sizes: ").split()))

process_size = int(input("Enter process size: "))

first_fit(holes[:], process_size)   # use holes[:] to pass a copy
best_fit(holes[:], process_size)
worst_fit(holes[:], process_size)