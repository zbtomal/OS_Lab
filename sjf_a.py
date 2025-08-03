# SJF (Non-Preemptive) Scheduling Algorithm with Arrival Time

def sjf(processes, arrival_time, burst_time):
    n = len(processes)
    completed = 0
    current_time = 0
    is_completed = [False] * n

    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n

    print("\nSJF Schedule:")

    while completed != n:
        idx = -1
        min_burst = float('inf')

        for i in range(n):
            if arrival_time[i] <= current_time and not is_completed[i]:
                if burst_time[i] < min_burst:
                    min_burst = burst_time[i]
                    idx = i
                elif burst_time[i] == min_burst:
                    if arrival_time[i] < arrival_time[idx]:
                        idx = i

        if idx != -1:
            current_time += burst_time[idx]
            completion_time[idx] = current_time
            turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
            waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
            is_completed[idx] = True
            completed += 1

            print(f"P{processes[idx]}: Arrival={arrival_time[idx]}, Burst={burst_time[idx]}, "
                  f"Waiting={waiting_time[idx]}, Turnaround={turnaround_time[idx]}, Completion={completion_time[idx]}")
        else:
            current_time += 1  # CPU is idle

    avg_waiting = sum(waiting_time) / n
    avg_turnaround = sum(turnaround_time) / n

    print(f"\nAverage Waiting Time = {avg_waiting:.2f}")
    print(f"Average Turnaround Time = {avg_turnaround:.2f}")


# Test Example
processes = [1, 2, 3, 4]
arrival_time = [0, 2, 3, 5]
burst_time = [6, 8, 7, 3]

sjf(processes, arrival_time, burst_time)
