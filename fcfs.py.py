queue = []
waitingtime = 0
processes = int(raw_input('Enter the total no of processes you want to enter in the ready queue: '))
for i in range(0,processes):
    queue.append([])
    queue[i].append(raw_input('Enter process name: '))
    queue[i].append(int(raw_input('Enter arrival time: ')))
    waitingtime += queue[i][1]
    queue[i].append(int(raw_input('Enter burst time: ')))
    print ''

queue.sort()

print 'Process_Name\tArrivalTime\tBurstTime'
for i in range(0,processes):
    print queue[i][0],'\t\t',queue[i][1],'\t\t',queue[i][2]
    
print 'Total waiting time of process: ',waitingtime
print 'Average waiting time: ',(waitingtime/processes)
