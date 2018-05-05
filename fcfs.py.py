import time
count =input("Enter the number of processes you want to enter in the ready queue : ")
list=[]
for a in range(int(count)):
  x=input("Enter the process number like p1 ,p2....  ")
  y=input("Enetr the arrival time:  ")
  z=input("Enter the burst time: ")
  list.append([y,z,x])
list.sort()
print(list)
print(" ")
time.sleep(int(list[0][1]))
print("process ",list[0][2]," started at ",list[0][0]," and ended at ",int(list[0][1])+int(list[0][0]))
