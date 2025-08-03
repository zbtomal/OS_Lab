# FCFS Scheduling with Arrival Time and Average Waiting Time
def fcfs(processes, arrival_time, burst_time):
    n = len(processes)
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Sort processes by arrival time
    zipped = list(zip(arrival_time, burst_time, processes))
    zipped.sort()
    arrival_time, burst_time, processes = zip(*zipped)

    # First process
    completion_time[0] = arrival_time[0] + burst_time[0]
    turnaround_time[0] = completion_time[0] - arrival_time[0]
    waiting_time[0] = turnaround_time[0] - burst_time[0]

    # Rest of the processes
    for i in range(1, n):
        if arrival_time[i] > completion_time[i - 1]:
            # CPU idle time
            completion_time[i] = arrival_time[i] + burst_time[i]
        else:
            completion_time[i] = completion_time[i - 1] + burst_time[i]

        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]

    # Print results
    print("FCFS Schedule:")
    for i in range(n):
        print(f"P{processes[i]}: Arrival={arrival_time[i]}, Burst={burst_time[i]}, Waiting={waiting_time[i]}, Turnaround={turnaround_time[i]}, Completion={completion_time[i]}")

    avg_waiting = sum(waiting_time) / n
    avg_turnaround = sum(turnaround_time) / n

    print(f"\nAverage Waiting Time = {avg_waiting:.2f}")
    print(f"Average Turnaround Time = {avg_turnaround:.2f}")


# Test
processes = [1, 2, 3]
arrival_time = [0, 0, 0]
burst_time = [5, 2, 8]
fcfs(processes, arrival_time, burst_time)
