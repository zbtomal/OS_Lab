# FCFS Scheduling
def fcfs(processes, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]
    
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    print("FCFS Schedule:")
    for i in range(n):
        print(f"P{processes[i]}: Waiting={waiting_time[i]}, Turnaround={turnaround_time[i]}")


#test
processes = [1, 2, 3]
burst_time = [5, 2, 8]
fcfs(processes, burst_time)