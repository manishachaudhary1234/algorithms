import sys
import heapq
def p1():
  
  print "\nGreedy Scheduling Algorithm using W-L (Difference), decreasing order"
  fi = open("jobs.txt", "r")
  print "Sum of weighted completion times: " , greedyScheduling(fi, "diff")
def p2():
  
  print "\nGreedy Scheduling Algorithm using W/L (Ratio)"
  fi = open("jobs.txt", "r")
  print "Sum of weighted completion times: ", greedyScheduling(fi, "ratio")
def p3():
  fi = open("edges.txt", "r")

  x = []

  for line in fi:
    i = line.split()
    if i[0] not in x: x.append(i[0])
    if i[1] not in x: x.append(i[1])

  x = map(int, x)
  x.sort()

  print x




def greedyScheduling(fi, alg = "ratio"):
  '''
  Greedy Scheduling for Tasks
  
  Parameters:
    fi  - input file
    alg - algorithm to use ("diff" or "ratio") 
  '''
  
  if not fi:
    return "No input file"

  jobs = []  
  for line in fi:
    task = map(int, line.split())
    if alg is "ratio":  wlrate = float(task[0]) / float(task[1])
    elif alg is "diff": wlrate = task[0] - task[1]
    else:               return "Invalid Algorithm"
    jobs.append([wlrate, task[0], task[1]])
  jobs.sort(reverse=True)
  comptime = accumtime = 0
  for job in jobs:
    accumtime += job[2]
    comptime  += accumtime * job[1]

  return comptime


if __name__ == "__main__":
  p3()



